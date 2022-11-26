from django.db import models

# Create your models here.
class Grandeur(models.Model):
    nom=models.CharField(max_length=60)
    unit=models.CharField(max_length=30)
    valMin=models.FloatField()
    valMax=models.FloatField()

    def __str__(self):
        return f"Grandeur: {self.nom} Unité: {self.unit} valeurs entre {self.valMin} et {self.valMax}"

class Mesure(models.Model):
    valeur=models.FloatField()
    datetime=models.DateTimeField()
    grandeur=models.ForeignKey(Grandeur,on_delete=models.CASCADE)

    # Create your models here.
    class Grandeur(models.Model):
        nom = models.CharField(max_length=60)
        age = models.IntegerField()
        unit = models.CharField(max_length=30)
        VaMin = models.FloatField()
        valMax = models.FloatField()
        def __str__(self):
            return f"Mesure: {self.valeur} at {self.datePrise}"


