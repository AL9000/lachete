# -*- coding: utf-8 -*-

from django.views.generic import TemplateView
from django.shortcuts import render


class GPSView(TemplateView):
    template_name = "gps.html"

    def get(self, request):
        return render(request, self.template_name)
