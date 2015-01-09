from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=200, unique=True)
	body = models.TextField()
	slug = models.SlugField(max_length=200, unique=True)
	created = models.DateTimeField(auto_now_add=True)
	
	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(Post, self).save(*args, **kwargs)
	
	def __unicode__(self):
		return self.title 