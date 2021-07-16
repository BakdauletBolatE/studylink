from django.db import models

# Create your models here.

class TitlesCategory(models.Model):

    name = models.CharField(max_length=255, unique=True)

    def __str__(self):

        return self.name

class Title(models.Model):

    title = models.CharField(max_length=255)
    category = models.ForeignKey(TitlesCategory, on_delete=models.CASCADE)

    def __str__(self):

        return f"{self.name} in {self.category} category"

    

