from django.db import models

# Create your models here.
class typemodel(models.Model):

	titlename = models.CharField(max_length=100)
	discs = models.CharField(max_length=100)
	urls = models.URLField(blank = True)


	def __str__(self):
		return self.titlename




