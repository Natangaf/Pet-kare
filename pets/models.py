from django.db import models

class Category_Sex(models.TextChoices):
    Male = "Male"
    Female = "Female"
    Not_Informed= "Not Informed"



class Pet(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    weight = models.FloatField()
    sex = models.CharField(
        max_length=20,
        choices=Category_Sex.choices,
        default=Category_Sex.Not_Informed
    )
    group = models.ForeignKey(
        "groups.Group", on_delete=models.PROTECT ,related_name="pets"
    )
    traits = models.ManyToManyField('traits.Trait')
    def __str__(self):
        return self.name