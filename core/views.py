from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PatientForm, EncounterForm
from django.http import HttpResponseRedirect, Http404

from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django_tables2 import RequestConfig
from .models import patient, encounter
from .tables import PatientTable, EncounterTable

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

def home(request):
    return render(request, 'home.html', {'table': table})

def base(request):
        return render(request, 'base.html')

def post_demogs(request):
    form = PatientForm(request.POST)
    if form.is_valid():
        form.save(commit=True)
    return HttpResponseRedirect('/home/')

def demographics(request):
    form = PatientForm()
    return render(request, 'demographics.html', {'form': form})

def c_demographics(request):
    form = PatientForm()
    return render(request, 'crispy_demographics.html', {'form': form})

class PatientListView(LoginRequiredMixin, ListView):
  model = patient
  template_name = 'patient_list.html'
  context_object_name = 'patients'
  ordering = ['id']

  def get_context_data(self, **kwargs):
    context = super(PatientListView, self).get_context_data(**kwargs)
    context['nav_patient'] = True
    table = PatientTable(patient.objects.all().order_by('-order_ID', 'card_ID', 'id'))
    RequestConfig(self.request, paginate={'per_page': 30}).configure(table)
    context['table'] = table
    return context

class MyPatientListView(LoginRequiredMixin, ListView):
  model = patient
  template_name = 'provider_patient_list.html'
  context_object_name = 'patients'
  ordering = ['id']

  def get_context_data(self, **kwargs):
    context = super(MyPatientListView, self).get_context_data(**kwargs)
    context['nav_patient'] = True
    table = PatientTable(patient.objects.filter(provider_id=self.request.user).order_by('-order_ID', 'card_ID', 'id'))
    RequestConfig(self.request, paginate={'per_page': 30}).configure(table)
    context['table'] = table
    return context


class HomePatientListView(LoginRequiredMixin, ListView):
  model = patient
  template_name = 'home.html'
  context_object_name = 'patients'
  ordering = ['id']

  def get_context_data(self, **kwargs):
    context = super(HomePatientListView, self).get_context_data(**kwargs)
    context['nav_patient'] = True
    table = PatientTable(patient.objects.filter(provider_id=self.request.user).order_by('-order_ID', 'card_ID', 'id'))
    RequestConfig(self.request, paginate={'per_page': 30}).configure(table)
    context['table'] = table
    return context

class MySeenListView(LoginRequiredMixin, ListView):
    model = encounter
    template_name = 'patient_list.html'
    context_object_name = 'patients'
    ordering = ['id']

    def get_context_data(self, **kwargs):
        context = super(MySeenListView, self).get_context_data(**kwargs)
        context['nav_patient'] = True
        table = EncounterTable(encounter.objects.select_related('patient_id').filter(provider_id=self.request.user).order_by('id'))
        RequestConfig(self.request, paginate={'per_page': 30}).configure(table)
        context['table'] = table
        return context

def post_encounter(request):
    form = EncounterForm(request.POST)
    if not request.user.is_authenticated():
        raise Http404
    if form.is_valid():
        instance = form.save(commit=False)
        instance.provider_id = request.user
        instance.save()
     #   form.save(commit=True)
    return HttpResponseRedirect('/home/')

def patient_encounter(request):
    form = EncounterForm()
    return render(request, 'patient_encounter.html', {'form': form})
