from django.db import models

class Track(models.Model):
    student_id = models.IntegerField(default=1)
    name = models.TextField(max_length=30)
    base = models.TextField(max_length=30)
    use = models.TextField(max_length=30)