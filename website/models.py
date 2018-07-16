from django.db import models
import datetime
# Create your forms here.

class Contact(models.Model):
	name = models.CharField(max_length=120)
	email = models.EmailField(max_length=120)
	message = models.CharField(max_length=500)
	timestamp = models.DateTimeField(blank=True, default=datetime.datetime.now())

	def __str__(self):
		return self.email

	class Meta:
		ordering = ['-timestamp']