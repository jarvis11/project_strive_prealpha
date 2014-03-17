from django.db import models
from django.contrib import admin


# Create your models here.

class Athlete(models.Model):
	first_name = models.CharField(max_length = 20)
	last_name = models.CharField(max_length = 20)
	email = models.EmailField(max_length = 75)
	#PASSWORD NEED TO CHANGE NOT SECURE RIGHT NOW
	password = models.CharField(max_length = 50)
	gender = models.CharField(max_length = 6)
	#NEED TO ADD AN IMAGE FIELD
	sport = models.CharField(max_length = 45)

	def __unicode__(self):
		return unicode(self.first_name)

class Post(models.Model):
	author = models.ForeignKey(Athlete)
	created = models.DateTimeField(auto_now_add = True)
	category = models.CharField(max_length = 10)
	#taggedAthletes = models.ManyToManyField(Athlete)
	comment = models.CharField(max_length = 500)
	#NEED TO ADD AN IMAGE FIELD

	def __unicode__(self):
		return unicode(self.comment)

class Tip(models.Model):
	leading_post = models.ForeignKey(Post)
	author = models.ForeignKey(Athlete)
	created = models.DateTimeField(auto_now_add = True)
	comment = models.CharField(max_length = 200)

	def __unicode__(self):
		return unicode(self.comment)

class Like(models.Model):
	liked_tip = models.OneToOneField(Tip)
	liker = models.OneToOneField(Athlete)


class AthleteAdmin(admin.ModelAdmin):
	list_display = ["first_name", "last_name", "email", "password", "gender", "sport"]

class PostAdmin(admin.ModelAdmin):
	list_display = ["author", "created", "category", "comment"]

class TipAdmin(admin.ModelAdmin):
	list_display = ["author", "leading_post", "created", "comment"]

class LikeAdmin(admin.ModelAdmin):
	list_display = ["liker", "liked_tip"]



admin.site.register(Athlete, AthleteAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Tip, TipAdmin)
admin.site.register(Like, LikeAdmin)

