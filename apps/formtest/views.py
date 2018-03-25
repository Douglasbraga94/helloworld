from django.shortcuts import render, redirect
from .forms import NameForm
from django.forms import models
from django.views.generic import TemplateView
# Create your views here.

class principal(TemplateView):
	template_name = 'formtest/index.html'

	def get(self, request):
		form = NameForm()
		return render(request, self.template_name, {'form': form})

	def post(self, request):
		form = NameForm(request.POST)
		if form.is_valid():
			text = form.cleaned_data['nome']
		
		args = {'form': form, 'text': text}
		return render(request, self.template_name, args)

