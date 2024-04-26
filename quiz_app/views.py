from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


from .models import CateringType, Question, Option, Result
from .forms import CateringTypeForm, OptionForm, MultipleOptionForm, UserRegisterForm


class RegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'login.html'
    success_url = reverse_lazy('type')

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(self.request, username=username, password=password)
        login(request=self.request, user=user)
        return redirect('type')


@login_required
def get_type_view(request):
    if request.method == "POST":
        form = CateringTypeForm(request.POST)
        type = request.POST.get('type')
        request.session['type'] = type
        request.session['options'] = {}
        return redirect('steps', step=1)
    else:
        form = CateringTypeForm()
        return render(request, 'index.html', {'form': form})


@login_required
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
        question = type_questions[step - 1]
    except IndexError:
        return redirect('confirm')

    options = Option.objects.filter(question=question).filter(catering__name=catering_type)
    if question.multiple:
        form = MultipleOptionForm(options=options)
    else:
        form = OptionForm(options=options)
        return render(request, 'index.html', {'form': form})


@login_required
def confirm_view(request):
    user = User.objects.get(username=request.user)

    options = request.session['options']
    catering_type = request.session['type']
    catering_obj = CateringType.objects.get(name=catering_type)
    result_text = f'{catering_type}\n{options}'

    quiz_result = Result.objects.create(
        patricipiant=user,
        text=result_text
    )
    quiz_result.save()
    quiz_result.catering_type.add(catering_obj)
    quiz_result.save()

    return render(
        request,
        'confirm.html',
        context={'options': options, 'catering_type': catering_type}
    )
