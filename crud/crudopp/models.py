from django.db import models


# Create your models here.
class CRUD(models.Model):
    name = models.CharField(max_length=30)
    cat = models.CharField(max_length=30)
    email = models.EmailField()
    image = models.ImageField(upload_to='crudopp')

    def __str__(self):
        return self.name
