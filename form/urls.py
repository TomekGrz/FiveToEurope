"""twitterOnlyPyt04 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from form import views

urlpatterns = [
    path('contact-details/', views.CreateContactView.as_view(), name='basic_contact'),
    path('update-contact-details/<int:pk>/', views.UpdateContactView.as_view(), name='update-contact-details'),
    path('father-details/', views.AddMaleParentDetails.as_view(), name='father-details'),
    path('update-father-details/<int:pk>/', views.UdpateMaleParentDetails.as_view(), name='update-father-details'),
    path('mother-details/', views.AddFemaleParentDetails.as_view(), name='mother-details'),
    path('update-mother-details/<int:pk>/', views.UpdateFemaleParentDetails.as_view(), name='update-mother-details'),
    path('service-details/', views.SelectServiceType.as_view(), name='service-details'),
    path('update-service-details/<int:pk>/', views.UpdateServiceType.as_view(), name='update-service-details'),
    path('case-detail/', views.AddCaseDescription.as_view(), name='case-details'),
    path('update-case-detail/<int:pk>/', views.UpdateCaseDescription.as_view(), name='update-case-details'),
    path('client-details/', views.AddClientDetails.as_view(), name='client-details'),
    path('update-client-details/<int:pk>', views.UpdateClientDetails.as_view(), name='update-client-details'),
    path('support-details/', views.AddSupportPerson.as_view(), name='support-details'),
    path('update-support-details/<int:pk>/', views.UpdateSupportPerson.as_view(), name='update-support-details'),
    path('client-print-details/<int:pk>/', views.ClientDetailViewMaster.as_view(), name='review-and-submit'),
    path('send-email/', views.sendmail, name='send-email'),
]