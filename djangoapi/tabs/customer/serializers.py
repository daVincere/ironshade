from rest_framework import serializers
from .models import Medicine, Name, Report


class MedicineSerializer(serializers.ModelSerializer):
	class Meta:
		model = Medicine
		fields = ['id', 'name', 'dosage', 'description', 'ingredients', 'sideeffects']


class ReportSerializer(serializers.ModelSerializer):
	class Meta:
		model = Report
		fields = ['date', 'content']


class NameSerializer(serializers.ModelSerializer):
	class Meta:
		model = Name
		fields = ['name',]
		