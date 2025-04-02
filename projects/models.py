from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    password = models.CharField(max_length=200, null=True)
    technology = models.CharField(max_length=200, null=True, blank=True)
    completed = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id}-{self.title}- {self.description} - {self.password} - {self.technology} - {self.completed} - {self.create_at} - {self.updated_at} "
