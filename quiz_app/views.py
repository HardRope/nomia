from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from .models import CateringType, Question, Option
from .forms import CateringTypeForm, OptionForm

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
		option = request.POST.get('option')
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
			return redirect('lk')
			# options = request.session['options']
			# catering_type = request.session['type']
			# return render(request, 'lk.html', context={'options': options, 'catering_type': catering_type})


		options = Option.objects.filter(question=question).filter(catering__name=catering_type)

		form = OptionForm(options=options)
	return render(request, 'index.html', {'form': form})

def lk_view(request):
	options = request.session['options']
	catering_type = request.session['type']
	return render(request, 'lk.html', context={'options': options, 'catering_type': catering_type})
