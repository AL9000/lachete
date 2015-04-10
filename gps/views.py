# -*- coding: utf-8 -*-

from django.views.generic import TemplateView
from django.shortcuts import render
from django.conf import settings
from rest_framework import views
from rest_framework.response import Response
from django.contrib.auth.models import User
from gps.models import UserPosition


class GPSView(TemplateView):
    template_name = "gps/gps.html"

    def get(self, request):
        return render(request,
                      self.template_name,
                      {'field_position': settings.FIELD_POSITION})


class UsersPosition(views.APIView):

    def get(self, request):
        users_positions = User.objects.values('username',
                                              'userposition__longitude',
                                              'userposition__latitude')
        return Response(users_positions)

    def post(self, request, *args, **kwargs):
        longitude = request.DATA.get('longitude', None)
        latitude = request.DATA.get('latitude', None)
        if longitude and latitude:
            user = request.user
            try:
                user_position = user.userposition
            except UserPosition.DoesNotExist:
                user_position = UserPosition()
                user_position.user = user
            user_position.longitude = longitude
            user_position.latitude = latitude
            user_position.save()
            return Response({"success": True})
        else:
            return Response({"success": False})
