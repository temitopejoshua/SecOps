from . import views
from django.conf.urls import url

from django.urls import path, include

urlpatterns = [

    url(r"^elders/$", views.EldersList.as_view(), name=views.EldersList.name),
    url(r"^elders/(?P<pk>[0-9]+)$", views.ElderDetail.as_view(), name=views.ElderDetail.name),
    url(r"^natives/$", views.NativesList.as_view(), name=views.NativesList.name),
    url(r"^natives/(?P<pk>[0-9]+)$", views.NativesDetail.as_view(), name=views.NativesDetail.name),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^citizens/$', views.CitizensList.as_view(), name=views.CitizensList.name),
    url(r"^citizens/(?P<pk>[0-9]+)$", views.CitizensDetail.as_view(), name=views.CitizensDetail.name),
    url(r"^activities/$", views.ActivitiesList.as_view(), name=views.ActivitiesList.name),
    url(r"^activities/(?P<pk>[0-9]+)$", views.ActivitiesDetails.as_view(), name=views.ActivitiesDetails.name),

    # User registration Details
    url(r"^users/$", views.UserList.as_view(), name=views.UserList.name),
    url(r"^rest-auth/", include("rest_auth.urls")),

]
