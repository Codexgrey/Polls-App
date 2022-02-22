from django.db import models

# Create your models here.
# modelled such that each poll has 3 options only
class Poll(models.Model):
    question = models.TextField()
    option_one = models.CharField(max_length=240)
    option_two = models.CharField(max_length=240)
    option_three = models.CharField(max_length=240)
    option_one_count = models.IntegerField(default=0)
    option_two_count = models.IntegerField(default=0)
    option_three_count = models.IntegerField(default=0)

    def total(self):
        return self.option_one_count + self.option_two_count + self.option_three_count