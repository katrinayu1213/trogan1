from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PatientForm, EncounterForm
from django.http import HttpResponseRedirect, Http404
from django.utils import timezone

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

class PTPatientListView(LoginRequiredMixin, ListView):
  model = patient
  template_name = 'pt_incoming.html'
  context_object_name = 'patients'
  ordering = ['id']

  def get_context_data(self, **kwargs):
    context = super(PTPatientListView, self).get_context_data(**kwargs)
    context['nav_patient'] = True
    usergroup = self.request.user.groups.values_list('name', flat=True).first()
    print(usergroup)

    table = PatientTable(patient.objects.filter(status='W', department='PT', created_at__day=timezone.now().day).order_by('-order_ID', 'card_ID', 'id'))

    RequestConfig(self.request, paginate={'per_page': 30}).configure(table)
    context['table'] = table
    return context


class GMPatientListView(LoginRequiredMixin, ListView):
    model = patient
    template_name = 'gm_incoming.html'
    context_object_name = 'patients'
    ordering = ['id']

    def get_context_data(self, **kwargs):
        context = super(GMPatientListView, self).get_context_data(**kwargs)
        context['nav_patient'] = True
        usergroup = self.request.user.groups.values_list('name', flat=True).first()
        print(usergroup)

        table = PatientTable(patient.objects.filter(status='W', department='GM', created_at__day=timezone.now().day).order_by('-order_ID', 'card_ID', 'id'))

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
    usergroup = self.request.user.groups.values_list('name', flat=True).first()
    print(usergroup)
    if usergroup == 'Physical Therapy':
        table = PatientTable(patient.objects.filter(provider_id=self.request.user, status='W', department='PT', created_at__day=timezone.now().day).order_by('-order_ID', 'card_ID', 'id'))
    elif usergroup == 'Gen Med':
        table = PatientTable(patient.objects.filter(status='W', department='GM', created_at__day = timezone.now().day).order_by('-order_ID', 'card_ID', 'id'))
    else:
        table = PatientTable(patient.objects.filter(status='W', created_at__day=timezone.now().day).order_by('-order_ID', 'card_ID', 'id'))
    RequestConfig(self.request, paginate={'per_page': 10}).configure(table)
    context['table'] = table
    return context

class HomeEncounterView(LoginRequiredMixin, ListView):
    model = encounter
    template_name = 'encounter_list.html'
    context_object_name = 'encounters'
    ordering = ['id']

    def get_context_data(self, **kwargs):
        context = super(HomeEncounterView, self).get_context_data(**kwargs)
        context['nav_encounter'] = True

        table = EncounterTable(encounter.objects.filter(created_at__day=timezone.now().day))

        RequestConfig(self.request, paginate={'per_page': 1000}).configure(table)
        context['table'] = table
        return context

class BeingSeenView(LoginRequiredMixin, ListView):
    model = patient
    template_name = 'being_seen.html'
    context_object_name = 'being_seen'
    ordering = ['id']

    def get_context_data(self, **kwargs):
        context = super(BeingSeenView, self).get_context_data(**kwargs)
        context['nav_seen'] = True

        table = PatientTable(patient.objects.filter(status='B', created_at__day=timezone.now().day))

        RequestConfig(self.request, paginate={'per_page': 1000}).configure(table)
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


class MyEncountersListView(LoginRequiredMixin, ListView):
  model = encounter
  template_name = 'my_encounters.html'
  context_object_name = 'encounters'
  ordering = ['id']



  def get_context_data(self, **kwargs):
    context = super(MyEncountersListView, self).get_context_data(**kwargs)
    context['nav_patient'] = True
    usergroup = self.request.user.groups.values_list('name', flat=True).first()

    encounters_select_related = encounter.objects.filter(provider_id=self.request.user).select_related()
    my_encounters = []

    for enc in encounters_select_related:
        my_encounters.append({
            'provider_id': enc.provider_id,
            'patient_id': enc.patient_id,
            'last_name': enc.patient_id.last_name,
            'first_name': enc.patient_id.first_name,
            'Provider_Notes': enc.Provider_Notes,
            'Supplies_Used': enc.Supplies_Used,
            'medication_list': enc.medication_list,
        })

    filtered_encounters = EncounterTable(my_encounters)
    # EncounterTable(encounter.objects.filter(provider_id=self.request.user).select_related())
    # print(my_encounters)

    RequestConfig(self.request, paginate={'per_page': 30}).configure(filtered_encounters)
    context['table'] = filtered_encounters
    return context