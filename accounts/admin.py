from django.contrib import admin
from form.models import ClientDetails, FemaleParentDetails, MaleParentDetails, ServiceType, SupportPerson, CaseDescription, ContactForm


admin.site.register(ClientDetails)
admin.site.register(FemaleParentDetails)
admin.site.register(MaleParentDetails)
admin.site.register(ServiceType)
admin.site.register(SupportPerson)
admin.site.register(CaseDescription)
admin.site.register(ContactForm)
