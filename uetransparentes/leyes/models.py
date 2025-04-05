from django.db import models


class Anexo(models.Model):
    texto = models.CharField("Texto", max_length=255, null=True, blank=True)
    url = models.URLField("URL", null=True, blank=True)

    def __str__(self):
        return self.texto


class Area(models.Model):
    area = models.CharField("Área", max_length=255, unique=True)

    class Meta:
        verbose_name = "Área"
        verbose_name_plural = "Áreas"

    def __str__(self):
        return self.area


class Tipo(models.Model):
    tipo = models.CharField("Tipo", max_length=255, unique=True)

    def __str__(self):
        return self.tipo


class Avance(models.Model):
    avance = models.CharField("Avance", max_length=255, unique=True)

    def __str__(self):
        return self.avance


class Estado(models.Model):
    estado = models.CharField("Estado", max_length=255, unique=True)

    def __str__(self):
        return self.estado


class Ley(models.Model):
    ley = models.CharField(
        "Texto de Ley",
        max_length=255,
        null=True,
        blank=True,
        help_text="Texto/Título de la ley",
    )
    boletin = models.ManyToManyField(
        Anexo,
        related_name="boletin",
        verbose_name="Boletín",
        help_text="Escoja un anexo",
    )
    avanceley = models.ForeignKey(
        Avance,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Avance de la Ley",
    )
    enlace = models.URLField(
        "Enlace", null=True, blank=True, help_text="Link directo a la ley (https://...)"
    )
    impactoavance = models.TextField("Posibilidad de avance", null=True, blank=True)
    impactociudadano = models.TextField(
        "Impacto en la ciudadanía", null=True, blank=True
    )
    impactocivilong = models.TextField(
        "Impacto en orgs sociedad civil", null=True, blank=True
    )
    estado = models.ForeignKey(Estado, null=True, blank=True, on_delete=models.CASCADE)
    autores = models.TextField("Autores", null=True, blank=True)
    descripcion = models.TextField("Descripción", null=True, blank=True)
    tipo = models.ForeignKey(Tipo, null=True, blank=True, on_delete=models.CASCADE)
    fecha = models.DateField("Fecha", null=True, blank=True)
    minuta = models.ManyToManyField(Anexo, related_name="minuta")

    class Meta:
        verbose_name = "Ley"
        verbose_name_plural = "Leyes"

    def __str__(self):
        return self.ley
