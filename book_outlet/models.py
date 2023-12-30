from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from django.urls import reverse
from django.utils.text import slugify



class Address (models.Model):
    street = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=10)


class Author(models.Model):
    first_name = models.CharField(max_length=100) 
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(Address,on_delete = models.CASCADE,null=True)
    
    
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    author = models.ForeignKey(Author,on_delete=models.CASCADE,null=True)
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="",null=False, db_index=True)

    def absolute_url(self):
        return reverse("book-detail" ,args=[self.slug])
    


    def __str__(self):
        return f"{ self.title } ({ self.rating })"