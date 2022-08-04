from django.db import models

# Create your models here.
class Poll(models.Model):
	question = models.TextField()
	option1 = models.CharField(max_length=30)
	option2 = models.CharField(max_length=30)
	option3 = models.CharField(max_length=30)
	option1_checked = models.IntegerField(default=0)
	option2_checked = models.IntegerField(default=0)
	option3_checked = models.IntegerField(default=0)

	def total(self):
		return self.option1_checked + self.option2_checked + self.option3_checked

	def __str__(self):
		return self.question
