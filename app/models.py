from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200, help_text="Enter the task title")
    description = models.TextField(blank=True, null=True, help_text="Enter a description for the task (optional)")
    completed = models.BooleanField(default=False, help_text="Is the task completed?")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']
