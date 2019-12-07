# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse

from django.shortcuts import render
from rest_framework import viewsets
from .models import Client, User, Location, Test_Standard, Product, Certificate, Test_Sequence, Performance_Data, \
    Service
from .serializers import ClientSerializer, UserSerializer, LocationSerializer, TestStandardSerializer, \
    ProductSerializer, CertificateSerializer, TestSequenceSerializer, PerformanceDataSerializer, ServiceSerializer


# Create your views here.


class ClientView(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class TestView(APIView):
    def get(self, request):
        queryset = Client.objects.all()
        serializer_class = ClientSerializer(queryset, many=True)
        return Response(serializer_class.data)


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LocationView(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class TestStandardView(viewsets.ModelViewSet):
    queryset = Test_Standard.objects.all()
    serializer_class = TestStandardSerializer


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CertificateView(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer


class TestSequenceView(viewsets.ModelViewSet):
    queryset = Test_Sequence.objects.all()
    serializer_class = TestSequenceSerializer


class PerformanceDataView(viewsets.ModelViewSet):
    queryset = Performance_Data.objects.all()
    serializer_class = PerformanceDataSerializer


class ServiceView(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
