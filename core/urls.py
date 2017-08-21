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
        url(r'^home/$', core_views.home, name='home'),
        url(r'^demographics/$', core_views.demographics, name='demographics'),
        url(r'^demographics/post_demogs/$', core_views.post_demogs, name='post_demogs'),

]