from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth.decorators import login_required
from core import views as core_views

urlpatterns = [
        url(r'^$', auth_views.LoginView.as_view(template_name='landing.html'), name='landing'),
        url(r'^signup/$', core_views.signup, name='signup'),
        url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
        url(r'^home/$', login_required(core_views.HomePatientListView.as_view()), name='home'),
        url(r'^demographics/$', login_required(core_views.demographics), name='demographics'),
        url(r'^demographics/post_demogs/$', login_required(core_views.post_demogs), name='post_demogs'),
        url(r'^pt_incoming/$', login_required(core_views.PTPatientListView.as_view()), name='pt_incoming'),
        url(r'^gm_incoming/$', login_required(core_views.GMPatientListView.as_view()), name='gm_incoming'),
        url(r'^encounter/$', login_required(core_views.patient_encounter), name='patient_encounter'),
        url(r'^encounter/post_encounter/$', login_required(core_views.post_encounter), name='post_demogs'),
        url(r'^encounter_list/$', login_required(core_views.HomeEncounterView.as_view()), name='encounter_list'),
]