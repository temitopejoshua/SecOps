from . import views

from django.urls import path, include

urlpatterns = [

    path("elders/", views.EldersList.as_view(), name=views.EldersList.name),
    path("elders/<int:pk>", views.ElderDetail.as_view(), name=views.ElderDetail.name),
    path("natives/", views.NativesList.as_view(), name=views.NativesList.name),
    path("natives/<int:pk>", views.NativesDetail.as_view(), name=views.NativesDetail.name),
    path('api-auth/', include('rest_framework.urls')),
    path('citizens/', views.CitizensList.as_view(), name=views.CitizensList.name),
    path("citizens/<int:pk>", views.CitizensDetail.as_view(), name=views.CitizensDetail.name),
    path("", views.ActivitiesList.as_view(), name=views.ActivitiesList.name),
    path("activities/<int:pk>", views.ActivitiesDetails.as_view(), name=views.ActivitiesDetails.name),

    # User registration Details
    path("users/", views.UserList.as_view(), name=views.UserList.name),
    path("rest-auth/", include("rest_auth.urls")),

]
