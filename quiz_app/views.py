from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import CreateView
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


from .models import CateringType, Question, Option
from .forms import CateringTypeForm, OptionForm, MultipleOptionForm, UserRegisterForm


class RegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'login.html'
    success_url = reverse_lazy('type')

    def form_valid(self, form):
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(self.request, username=username, password=password)
        login(request=self.request, user=user)
        return redirect('type')


def get_type_view(request):
  if request.method == "POST":
    form = CateringTypeForm(request.POST)
    type =  request.POST.get('type')
    request.session['type'] = type
    request.session['options'] = {}
    print(request)
    return redirect('steps', step=1)
  else:
    form = CateringTypeForm()
    return render(request, 'index.html', {'form': form})


def quiz_view(request, step):
	if request.method == 'POST':
		option = request.POST.getlist('option')
		request.session['options'][f'step_{step}'] = option
		request.session.modified = True
		step += 1
		return redirect('steps', step=step)

	else:
		catering_type = request.session['type']
		type_questions = Question.objects.filter(catering__name=catering_type)

		try:
			question = type_questions[step-1]
		except IndexError:
			return redirect('confirm')

		options = Option.objects.filter(question=question).filter(catering__name=catering_type)
		if question.multiple:
				form = MultipleOptionForm(options=options)
		else:
				form = OptionForm(options=options)
		return render(request, 'index.html', {'form': form})


def confirm_view(request):
	options = request.session['options']
	catering_type = request.session['type']
	return render(request, 'confirm.html', context={'options': options, 'catering_type': catering_type})
