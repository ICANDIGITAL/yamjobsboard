from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=100)
    skills = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.title} at {self.company}"
