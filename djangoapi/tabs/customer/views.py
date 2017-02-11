from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Name, Medicine, Report

from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from .serializers import NameSerializer,MedicineSerializer, ReportSerializer

# @api_view(['GET'])
# def medicine_collection(request):
# 	if request.method == 'GET':
# 		medicines = Name.objects.all()
# 		serializer = NameSerializer(medicines)
# 		return Response(serializer.data)


# @api_view
# def medicine(request, id=id):
# 	try:
# 		medicine = Medicine.objects.get(id=id)
# 	except Medicine.DoesNotExist:
# 		return HttpResponse(status=404)


# 	if request.method == 'GET':
# 		serializer = MedicineSerializer(medicine)
# 		return Response(serializer.data)


from rest_framework import mixins
from rest_framework import generics

#using api view
from django.http import Http404
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.views import APIView


class nameViewSet(viewsets.ModelViewSet):
	queryset = Name.objects.all()
	serializer_class = NameSerializer


class medicinesViewSet(viewsets.ModelViewSet):
	queryset = Medicine.objects.all()
	serializer_class = MedicineSerializer