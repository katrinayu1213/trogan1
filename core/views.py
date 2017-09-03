from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import PatientForm
from django.http import HttpResponseRedirect

from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django_tables2 import RequestConfig
from .models import patient
from .tables import PatientTable

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def base(request):
        return render(request, 'base.html')

def home(request):
        return render(request, 'home.html')

def post_demogs(request):
    form = PatientForm(request.POST)
    if form.is_valid():
        form.save(commit=True)
    return HttpResponseRedirect('/home/')

def demographics(request):
    form = PatientForm()
    return render(request, 'demographics.html', {'form': form})

class PatientListView(LoginRequiredMixin, ListView):
  model = patient
  template_name = 'patient_list.html'
  context_object_name = 'patients'
  ordering = ['id']

  def get_context_data(self, **kwargs):
    context = super(PatientListView, self).get_context_data(**kwargs)
    context['nav_patient'] = True
    table = PatientTable(patient.objects.all().order_by('patient_id'))
    RequestConfig(self.request, paginate={'per_page': 30}).configure(table)
    context['table'] = table
    return context