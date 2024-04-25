from django.urls import path

from .views import get_type_view, quiz_view, lk_view

urlpatterns = [
	path('type/', get_type_view, name='type'),
	path('step-<int:step>/', quiz_view, name='steps'),
	path('lk/', lk_view, name='lk')
]