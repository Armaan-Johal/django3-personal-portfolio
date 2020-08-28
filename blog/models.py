from django.db import models
import datetime

# Create your models here.
class Blog(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	date = models.DateField(("Date"), default=datetime.date.today)
	url = models.URLField(blank=True)

	def __str__(self):
		return self.title