from django.db import models

# Create your models here.


class People(models.Model): 
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self) -> str:
        return self.firstname + ' ' + self.lastname + ' ' + self.age.__str__()
