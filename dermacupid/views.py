from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class UpcomingTemplate(TemplateView):
    template_name = "upcoming.html"
