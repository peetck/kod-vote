from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Poll(models.Model):
    subject = models.CharField(max_length=255, null=False)
    detail = models.TextField()
    picture = models.ImageField(default='default.png')
    start_date = models.TimeField(auto_now=True)
    end_date = models.TimeField()
    password = models.CharField(max_length=255, blank=True, default='')
    create_by = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.TimeField(auto_now=True)

    def __str__(self):
        return f'{self.subject}'

class Poll_Choice(models.Model):
    subject = models.CharField(max_length=255)
    image = models.ImageField(default='default_choice.jpg')
    poll_id = models.ForeignKey(Poll, on_delete=models.CASCADE)

    def __str__(self):
        return f'Choice : {self.subject}'

class Poll_Vote(models.Model):
    poll_id = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice_id = models.ForeignKey(Poll_Choice, on_delete=models.CASCADE)
    vote_by = models.ForeignKey(User, on_delete=models.CASCADE)
