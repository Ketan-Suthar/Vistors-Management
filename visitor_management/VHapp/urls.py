from django.urls import path
from . import views
from .views import CreateNewVisitor, VisitorEntry, CreateNewEntry

urlpatterns = [
	path('',views.home, name='home'),
	path('CreateNewVisitor',CreateNewVisitor.as_view(), name='create-new-visitor'),
	path('VisitorEntry',views.VisitorEntry, name='visitor-entry'),
	path('CreateNewEntry',views.CreateNewEntry, name='create-new-entry')
]