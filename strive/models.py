from django.db import models
from django.contrib import admin


# Create your models here.

# General Models

class Like(models.Model):
	liker = models.ForeignKey('Athlete')

	def __unicode__(self):
		return unicode(self.liker)

class Image(models.Model):
	image = models.FileField(upload_to = "images/")
	created = models.DateTimeField(auto_now_add = True)

	def __unicode__(self):
		return unicode(self.created)

class Location(models.Model):
	latitude = models.FloatField()
	longitude = models.FloatField()
	name = models.CharField(max_length = 50)
	description = models.CharField(max_length = 500)
	image = models.OneToOneField(Image, blank = True, null = True)
	address = models.CharField(max_length = 100)

	def __unicode__(self):
		return unicode(self.name)

# Strive specific models		

class Athlete(models.Model):
	first_name = models.CharField(max_length = 20)
	last_name = models.CharField(max_length = 20)
	email = models.EmailField(max_length = 75)
	#PASSWORD NEED TO CHANGE NOT SECURE RIGHT NOW
	password = models.CharField(max_length = 50)
	gender = models.CharField(max_length = 6)
	profile_pic = models.OneToOneField(Image, blank = True, null = True)
	sport = models.CharField(max_length = 45)

	def __unicode__(self):
		return unicode(self.first_name)


class Post(models.Model):
	author = models.ForeignKey(Athlete)
	created = models.DateTimeField(auto_now_add = True)
	category = models.CharField(max_length = 10)
	#taggedAthletes = models.ManyToManyField(Athlete)
	comment = models.CharField(max_length = 500)
	image = models.OneToOneField(Image, blank = True, null = True)
	likes = models.ManyToManyField(Like, blank = True)
	checkin = models.OneToOneField(Location, blank = True, null = True)

	def __unicode__(self):
		return unicode(self.comment)

class Tip(models.Model):
	leading_post = models.ForeignKey(Post)
	author = models.ForeignKey(Athlete)
	created = models.DateTimeField(auto_now_add = True)
	comment = models.CharField(max_length = 200)
	image = models.OneToOneField(Image, blank = True, null = True)
	likes = models.ManyToManyField(Like, blank = True)

	def __unicode__(self):
		return unicode(self.comment)




class LikeAdmin(admin.ModelAdmin):
	list_display = ["liker"]

class AthleteAdmin(admin.ModelAdmin):
	list_display = ["first_name", "last_name", "email", "password", "gender", "sport", "profile_pic"]

class PostAdmin(admin.ModelAdmin):
	list_display = ["author", "created", "category", "comment"]

class TipAdmin(admin.ModelAdmin):
	list_display = ["author", "leading_post", "created", "comment"]

class LocationAdmin(admin.ModelAdmin):
	list_display = ["latitude", "longitude", "name", "description", "address"]




admin.site.register(Like, LikeAdmin)
admin.site.register(Athlete, AthleteAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Tip, TipAdmin)
admin.site.register(Location, LocationAdmin)

