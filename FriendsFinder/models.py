from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Category(models.Model):
	name = models.CharField(max_length=128, unique=True)
	views = models.IntegerField(default=0)
	likes = models.IntegerField(default=0)
	slug = models.SlugField(unique=True)
	
	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Category, self).save(*args, **kwargs)

	class Meta:
		verbose_name_plural = 'categories'

	def __str__(self):
		return self.name

class Page(models.Model):
	category = models.ForeignKey(Category)
	title = models.CharField(max_length=128)
	url = models.URLField()
	views = models.IntegerField(default=0)
	likes = models.IntegerField(default=0)

	class Meta:
		verbose_name_plural = 'pages'
	
	def __str__(self): # For Python 2, use __unicode__ too
		return self.title

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
##################################################################
##TODO link User to Character

#A Character instance exists for each User after they complete the quiz
class Character(models.Model):
	#TODO User account needs to link to this
	characterName = models.CharField(max_length=50, unique=True)
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
	threadCreator = models.OneToOneField(Character)
	threadTitle = models.CharField(max_length=128)
	threadCreationDate = models.DateField(auto_now_add=True)
	threadLastModified = models.DateField(auto_now=True)

	def __str__(self):
		return self.threadTitle + ":" + str(self.id)

class ThreadComment(models.Model):
	threadCommentCreator = models.OneToOneField(Character)
	threadCommentContent = models.CharField(max_length=500)
	threadCommentCreationDate = models.DateField(auto_now_add=True)
	threadCommentLastModified= models.DateField(auto_now=True)

	def __str__(self):
		return self.threadCommentCreator + ":" + str(self.id)