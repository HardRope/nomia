from django import forms

from .models import CateringType, Question, Option


class CateringTypeForm(forms.Form):
  catering_types = CateringType.objects.filter()

  CHOICES = [(type.name, type.name) for type in catering_types]

  type = forms.ChoiceField(
      widget=forms.RadioSelect,
      choices=CHOICES
      )

class OptionForm(forms.Form):
	option = forms.ChoiceField(
      widget=forms.RadioSelect,
      )

	def __init__(self,options,*args,**kwargs):
	      super().__init__(*args,**kwargs)
	      self.fields['option'].choices = [(option.text, option.text) for option in options]
