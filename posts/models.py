from django.db import models

# Create your models here.
class Posts(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    published=models.BooleanField(default=False)
    created_at=models.DateTimeField()

    def __str__(self):
        return self.title
    