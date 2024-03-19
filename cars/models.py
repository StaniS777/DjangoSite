from django.db import models

class Car(models.Model):
    brand = models.CharField(max_length=255)
    model_auto = models.CharField(max_length=255)
    body = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    instructions = models.TextField(blank=True)
    date = models.DateTimeField(null=True, blank=True)

    def __str__(self) -> str:
        return self.brand + " " + self.model_auto + " Кузов (" + self.body + ")" + " Цвет (" + self.color + ")"
