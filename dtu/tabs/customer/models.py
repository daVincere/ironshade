from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Name(models.Model):
	name = models.CharField(max_length=100)

	def __unicode__(self):
		return self.name

class Medicine(models.Model):
	name = models.ForeignKey(Name)
	dosage = models.TextField()
	description = models.TextField()
	ingredients = models.TextField()
	sideeffects = models.TextField()

	def __unicode__(self):
		return self.dosage

	# def get_absolute_url(self):
	# 	return reverse("Medicine", kwargs={"id": self.id})

class Report(models.Model):
	doc_type = models.TextField()
	date = models.DateTimeField()
	content = models.TextField()

	def __unicode__(self):
		return self.doc_type