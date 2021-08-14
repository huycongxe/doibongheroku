from django.db import models

# Create your models here.
class Doibong(models.Model):
    AREA = (
        ('Asia', 'Asia'),
        ('Africa', 'Africa'),
        ('Europe', 'Europe'),
        ('North America', 'North America'),
        ('South America', 'South America'),
        ('Australia', 'Australia')
    )

    name = models.CharField(max_length=200, null=True)
    short_name = models.CharField(max_length=200, null=True)
    area = models.CharField(max_length=200, null=True, choices=AREA)

    def __str__(self):
        return self.name

    def get_key(self):
        return self.id


class Cauthu(models.Model):
    name = models.CharField(max_length=200, null=True)
    age = models.IntegerField(null=True)
    number = models.CharField(max_length=200,null=True)
    height = models.CharField(max_length=200,null=True)
    weight = models.CharField(max_length=200,null=True)
    avatar = models.CharField(max_length=500, null=True)
    doibong = models.ForeignKey(Doibong, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

