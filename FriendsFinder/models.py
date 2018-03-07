from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


class UserProfile(models.Model):
	# This line is required. Links UserProfile to a User model instance.
	user = models.OneToOneField(User)
	# The additional attributes we wish to include.
	website = models.URLField(blank=True)
	picture = models.ImageField(upload_to='profile_images', blank=True)
	# Override the __unicode__() method to return out something meaningful!
	# Remember if you use Python 2.7.x, define __unicode__ too!
	def __str__(self):
		return self.user.username

#A Character instance exists for each User after they complete the quiz
class Character(models.Model):
	characterName = models.CharField(max_length=50, unique=True, blank=False)
	linkedUser = models.ForeignKey(User, null=True, blank=False)
	#TODO keep track of Characters created threads and comments, so admin would show name, thread,comments,datecreated,email

	#Save overwritten so that a unique number is assigned to the end of the name so you can tel between different users
	def save(self, *args, **kwargs):
		existingCount = Character.objects.filter(characterName__startswith=self.characterName).count()
		self.characterName = self.characterName + str(existingCount)
		super(Character, self).save(*args, **kwargs)

	def __str__(self):
		return self.characterName #Hack for now, idea is query how many XXXX exist and append count+1

class Question(models.Model):
	questionContent = models.CharField(max_length=500, blank=False)

	def __str__(self):
		return self.questionContent + ":" + str(self.id)

class Thread(models.Model):
	threadCreator = models.ForeignKey(Character, blank=False)
	threadTitle = models.CharField(max_length=128, blank=False)
	threadContent = models.CharField(max_length=500, blank=False)
	threadCreationDate = models.DateField(auto_now_add=True)
	threadLastModified = models.DateField(auto_now=True)

	def __str__(self):
		return self.threadTitle + ":" + str(self.id)

class ThreadComment(models.Model):
	threadCommentParent = models.ForeignKey(Thread, blank=False)
	threadCommentCreator = models.ForeignKey(Character, blank=False)
	threadCommentContent = models.CharField(max_length=500, blank=False)
	threadCommentCreationDate = models.DateField(auto_now_add=True)
	threadCommentLastModified= models.DateField(auto_now=True)

	def __str__(self):
		return self.threadCommentCreator + ":" + str(self.id)