from django.shortcuts import render
from django.views.generic import CreateView
from .models import visitor, isVisited
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


#83474 27397
def home(request):
	return render(request, 'VHapp/home.html')


class CreateNewVisitor(LoginRequiredMixin, CreateView):
	model = visitor
	fields = ['name','phone','email']

@login_required
def VisitorEntry(request):
	return render(request, 'VHapp/Visitor_Entry_Form.html')

@login_required
def CreateNewEntry(request):
	phone = int(request.POST['phone'])

	try:
		vis = visitor.objects.get(pk=phone)

		newvisitor = isVisited(visitor=vis, host = request.user)
		print(newvisitor.visitor,newvisitor.host, newvisitor.checkin,newvisitor.checkout, sep=' ')
		newvisitor.save()

		messages.success(request, f'New Entry Created Successfully')
		return render(request, 'VHapp/home.html')

	except visitor.DoesNotExist:
		messages.success(request, f'Visitor With This Number Does Not Exist')
		return render(request, 'VHapp/Visitor_Entry_Form.html')
