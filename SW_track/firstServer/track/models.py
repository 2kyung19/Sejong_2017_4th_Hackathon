from django.db import models

class Track(models.Model):
    student_id = models.IntegerField(default=1)
    name = models.TextField(max_length=256)
    base = models.TextField(max_length=256)
    use = models.TextField(max_length=256)

class Student(models.Model):
    index_id = models.IntegerField(default=1)
    name = models.TextField(max_length=256)
    student_id = models.TextField(max_length=256)
    track = models.TextField(max_length=256)
    base = models.TextField(max_length=256)
    use = models.TextField(max_length=256)