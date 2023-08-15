from django.db import models

class users_data(models.Model):
	user_name = models.CharField(max_length = 100)
	name = models.CharField(max_length = 100)
	followers = models.IntegerField()
	updatetime = models.DateTimeField()

# Create your models here.
