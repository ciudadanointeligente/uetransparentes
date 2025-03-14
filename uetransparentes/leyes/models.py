from django.db import models


class Anexo(models.Model):
    texto = models.CharField(max_length=255)
    url = models.URLField()

    def __str__(self):
        return self.texto


class Area(models.Model):
    area = models.CharField(max_length=255)

    def __str__(self):
        return self.area


class Tipo(models.Model):
    tipo = models.CharField(max_length=255)

    def __str__(self):
        return self.tipo


class Avance(models.Model):
    avance = models.TextField()

    def __str__(self):
        return self.avance


class Ley(models.Model):
    ley = models.CharField(max_length=255)
    boletin = models.ManyToManyField(Anexo)
    enlace = models.URLField()
    autores = models.TextField()
    descripcion = models.TextField()
    fecha = models.DateField()
    minuta = models.ManyToManyField(Anexo)

    def __str__(self):
        return self.ley
