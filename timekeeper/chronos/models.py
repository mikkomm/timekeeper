from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
	app_label = 'chronos'
	
	name = models.CharField(max_length=200)
	description = models.CharField(max_length=2000)
	
	created_date = models.DateTimeField('Date created')
	edited_date = models.DateTimeField('Date edited')
	created_by = models.ForeignKey(User, related_name='project_created_by')
	edited_by = models.ForeignKey(User, related_name='project_edited_by')

	def __unicode__(self):
		return self.name

class Task(models.Model):
	app_label = 'chronos'
	
	name = models.CharField(max_length=200)
	
	created_date = models.DateTimeField('Date created')
	edited_date = models.DateTimeField('Date edited')
	created_by = models.ForeignKey(User, related_name='task_created_by')
	edited_by = models.ForeignKey(User, related_name='task_edited_by')

	def __unicode__(self):
		return self.name

class Reference(models.Model):
	app_label = 'chronos'
	
	project = models.ForeignKey(Project, related_name='reference_project', null=True)
	name = models.CharField(max_length=200)
	
	created_date = models.DateTimeField('Date created')
	edited_date = models.DateTimeField('Date edited')
	created_by = models.ForeignKey(User, related_name='reference_created_by')
	edited_by = models.ForeignKey(User, related_name='reference_edited_by')

	def __unicode__(self):
		return self.name

class Chore(models.Model):
	app_label = 'chronos'
	
	date = models.DateField('Chore date')
	start_time = models.TimeField('Start time')
	end_time = models.TimeField('End time')
	
	owner = models.ForeignKey(User, related_name='chore_owner')
	project = models.ForeignKey(Project, related_name='chore_project')
	task = models.ForeignKey(Task, related_name='chore_task')
	reference = models.ForeignKey(Reference, related_name='chore_reference')
	comment = models.CharField(max_length=2000, null=True)
	
	created_date = models.DateTimeField('Date created')
	edited_date = models.DateTimeField('Date edited')
	created_by = models.ForeignKey(User, related_name='chore_created_by')
	edited_by = models.ForeignKey(User, related_name='chore_edited_by')
