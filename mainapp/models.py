from django.db import models
from django.urls import reverse
# Create your models here.

class PageCategory(models.Model):

    name = models.CharField(max_length=255, unique=True)

    def __str__(self):

        return self.name

class Title(models.Model):

    title = models.CharField(max_length=255)
    category = models.ForeignKey(PageCategory, on_delete=models.CASCADE)

    def __str__(self):

        return f"{self.title}: in {self.category} category"


class Block(models.Model):

    title = models.CharField(max_length=255)
    url_to = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)
    background = models.ImageField(upload_to="ImagesStudy/", null=True, blank=True)
    category = models.ForeignKey(PageCategory, on_delete=models.CASCADE)
    NOTHING = 'nnnttss'
    BLUE = 'gallery__item--purple'
    BLUESKY = 'gallery__item--blue'
    ORANGE = 'gallery__item--orange'
    YEAR_IN_SCHOOL_CHOICES = [
        (NOTHING, 'nnnttss'),
        (BLUE, 'gallery__item--purple'),
        (BLUESKY, 'gallery__item--blue'),
        (ORANGE, 'gallery__item--orange'),
    ]
    color = models.CharField(
        max_length=40,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=NOTHING,
    )

    def __str__(self):

        return f"{self.title}:  in {self.category} category"

class Teacher(models.Model):

    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to="teacherImages/")
    experiense = models.CharField(max_length=255)
    education = models.CharField(max_length=255)
    description = models.TextField(null=True,blank=True)
    formAction = models.TextField(null=True, blank=True)

    def __str__(self):

        return f"{self.name}"

    def get_absolute_url(self):

        return reverse('teacherUrl', args=(str(self.id)))




    


    

