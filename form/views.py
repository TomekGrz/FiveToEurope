import io
from datetime import timezone
from unittest import TestCase

import ctx as ctx
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core import mail
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail, EmailMessage
from django.http import FileResponse, HttpResponse, request
from django.shortcuts import render, redirect

# Create your views here.
from django.template.loader import render_to_string, get_template
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView, DetailView, ListView, UpdateView, FormView


from form.models import ContactForm, FemaleParentDetails, MaleParentDetails, ServiceType, CaseDescription, \
    ClientDetails, SupportPerson

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = "registration/../accounts/templates/registration/signup.html"


class Home(View):
    def get(self, request):
        return render(request, 'base.html')

class CreateContactView(CreateView):
    model = ContactForm
    template_name = 'contact-view.html'
    fields = ['phone', 'email', 'cbp', 'cbe']
    success_url = reverse_lazy('client-details')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        self.object = obj
        return redirect(self.get_success_url())


class UpdateContactView(UpdateView):
    model = ContactForm
    template_name = 'contact-view.html'
    fields = ['phone', 'email', 'cbp', 'cbe']
    success_url = reverse_lazy('client-details')


    def get_object(self):
        queryset = self.get_queryset()
        pk = self.kwargs.get(self.pk_url_kwarg)
        if pk is not None:
            queryset = queryset.filter(pk=pk)
        else:
            raise AttributeError()
        try:
            return queryset.get()
        except queryset.model.DoesNotExist:
            return None


class AddClientDetails(CreateView):
    model = ClientDetails
    template_name = 'personal-view.html'
    fields = ['name', 'surname', 'date_of_birth', 'place_of_birth', 'date_of_mariage','place_of_mariage']
    success_url = reverse_lazy('father-details')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        self.object = obj
        return redirect(self.get_success_url())


class UpdateClientDetails(UpdateView):
    model = ClientDetails
    template_name = 'personal-view.html'
    fields = ['name', 'surname', 'date_of_birth', 'place_of_birth', 'date_of_mariage','place_of_mariage']
    success_url = reverse_lazy('father-details')


    def get_object(self):
        queryset = self.get_queryset()
        pk = self.kwargs.get(self.pk_url_kwarg)
        if pk is not None:
            queryset = queryset.filter(pk=pk)
        else:
            raise AttributeError()
        try:
            return queryset.get()
        except queryset.model.DoesNotExist:
            return None


class AddMaleParentDetails(CreateView):
    model = MaleParentDetails
    template_name = 'father-details.html'
    fields = ['name', 'surname', 'date_of_birth', 'place_of_birth', 'date_of_mariage', 'place_of_mariage', 'military_service', 'occupation_before_51']
    success_url = reverse_lazy('mother-details')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        self.object = obj
        return redirect(self.get_success_url())


class UdpateMaleParentDetails(UpdateView):
    model = MaleParentDetails
    template_name = 'father-details.html'
    fields = ['name', 'surname', 'date_of_birth', 'place_of_birth','date_of_mariage', 'place_of_mariage', 'military_service', 'occupation_before_51']
    success_url = reverse_lazy('mother-details')


    def get_object(self):
        queryset = self.get_queryset()
        pk = self.kwargs.get(self.pk_url_kwarg)
        if pk is not None:
            queryset = queryset.filter(pk=pk)
        else:
            raise AttributeError()
        try:
            return queryset.get()
        except queryset.model.DoesNotExist:
            return None


class AddFemaleParentDetails(CreateView):
    model = FemaleParentDetails
    template_name = 'mother-details.html'
    fields = ['name', 'surname', 'date_of_birth', 'place_of_birth','date_of_mariage', 'place_of_mariage', 'maiden_name']
    success_url = reverse_lazy('service-details')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        self.object = obj
        return redirect(self.get_success_url())


class UpdateFemaleParentDetails(UpdateView):
    model = FemaleParentDetails
    template_name = 'mother-details.html'
    fields = ['name', 'surname', 'date_of_birth', 'place_of_birth','date_of_mariage', 'place_of_mariage', 'maiden_name']
    success_url = reverse_lazy('service-details')


    def get_object(self):
        queryset = self.get_queryset()
        pk = self.kwargs.get(self.pk_url_kwarg)
        if pk is not None:
            queryset = queryset.filter(pk=pk)
        else:
            raise AttributeError()
        try:
            return queryset.get()
        except queryset.model.DoesNotExist:
            return None


class SelectServiceType(CreateView):
    model = ServiceType
    template_name = 'service-details.html'
    fields = ['citizenship', 'research', 'grant', 'eligibility', 'comment']
    success_url = reverse_lazy('case-details')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        self.object = obj
        return redirect(self.get_success_url())


class UpdateServiceType(UpdateView):
    model = ServiceType
    template_name = 'service-details.html'
    fields = ['citizenship', 'research', 'grant', 'eligibility', 'comment']
    success_url = reverse_lazy('case-details')

    def get_object(self):
        queryset = self.get_queryset()
        pk = self.kwargs.get(self.pk_url_kwarg)
        if pk is not None:
            queryset = queryset.filter(pk=pk)
        else:
            raise AttributeError()
        try:
            return queryset.get()
        except queryset.model.DoesNotExist:
            return None


class AddCaseDescription(CreateView):
    model = CaseDescription
    template_name = 'case-details.html'
    fields = ['free_text', 'q1_last_relative_left_poland', 'q2_next_destination', 'q3_other_citizenships','q4_granfather_army','q5_grandfather_profession','q6_family_in_poland','q7_polish_docs','q8_addoption']
    success_url = reverse_lazy('support-details')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        self.object = obj
        return redirect(self.get_success_url())


class UpdateCaseDescription(UpdateView):
    model = CaseDescription
    template_name = 'case-details.html'
    fields = ['free_text', 'q1_last_relative_left_poland', 'q2_next_destination', 'q3_other_citizenships','q4_granfather_army','q5_grandfather_profession','q6_family_in_poland','q7_polish_docs','q8_addoption']
    success_url = reverse_lazy('support-details')

    def get_object(self):
        queryset = self.get_queryset()
        pk = self.kwargs.get(self.pk_url_kwarg)
        if pk is not None:
            queryset = queryset.filter(pk=pk)
        else:
            raise AttributeError()
        try:
            return queryset.get()
        except queryset.model.DoesNotExist:
            return None

class AddSupportPerson(CreateView):
    model = SupportPerson
    template_name = 'sup-details.html'
    fields = ['sup1', 'sup2', 'sup3']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        self.object = obj
        return redirect(self.get_success_url())

class UpdateSupportPerson(UpdateView):
    model = SupportPerson
    template_name = 'sup-details.html'
    fields = ['sup1', 'sup2', 'sup3']
    success_url = reverse_lazy('home')

    def get_object(self):
        queryset = self.get_queryset()
        pk = self.kwargs.get(self.pk_url_kwarg)
        if pk is not None:
            queryset = queryset.filter(pk=pk)
        else:
            raise AttributeError()
        try:
            return queryset.get()
        except queryset.model.DoesNotExist:
            return None


class ClientDetailViewMaster(DetailView):
    model = User
    template_name = 'review-and-submit.html'

    def get_context_data(self, **kwargs):
        context = super(ClientDetailViewMaster, self).get_context_data(**kwargs)
        context['contact'] = ContactForm.objects.filter(pk=self.kwargs.get('pk'))
        context['client'] = ClientDetails.objects.filter(pk=self.kwargs.get('pk'))
        context['father'] = MaleParentDetails.objects.filter(pk=self.kwargs.get('pk'))
        context['mother'] = FemaleParentDetails.objects.filter(pk=self.kwargs.get('pk'))
        context['service'] = ServiceType.objects.filter(pk=self.kwargs.get('pk'))
        context['case'] = CaseDescription.objects.filter(pk=self.kwargs.get('pk'))
        context['support'] = SupportPerson.objects.filter(pk=self.kwargs.get('pk'))
        return context

# def email(request):
#     subject = 'New client!'
#     message =
#     email_from = settings.EMAIL_HOST_USER
#     recipient_list = ['halunek@gmail.com',]
#     send_mail(subject, message, email_from, recipient_list )
#     return redirect('home')

def sendmail(request):
    ctx = {'user': ""}
    message = get_template('email.html').render(ctx)
    msg = EmailMessage('Subject',message, 'coderslabdjangotest@gmail.com',['halunek@gmail.com'],)
    msg.content_subtype = "html"
    msg.send()
    return render(request, 'suscess.html')