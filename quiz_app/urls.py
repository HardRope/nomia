from django.urls import path

from .views import get_type_view, quiz_view, confirm_view, RegisterView

urlpatterns = [
	  path('', RegisterView.as_view(), name='register'),
		path('type/', get_type_view, name='type'),
		path('step-<int:step>/', quiz_view, name='steps'),
		path('confirm/', confirm_view, name='confirm')
]