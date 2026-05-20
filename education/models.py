from django.db import models

# Modelo para almacenar las curiosidades sobre la Inteligencia Artificial (Landing Page)
class Curiosity(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título de la Curiosidad")
    text = models.TextField(verbose_name="Contenido de la Curiosidad")
    order = models.IntegerField(default=0, verbose_name="Orden de visualización")

    class Meta:
        verbose_name = "Curiosidad"
        verbose_name_plural = "Curiosidades"
        ordering = ['order', 'id']

    def __str__(self):
        return self.title


# Modelo para almacenar las definiciones de Inteligencia Artificial por diferentes autores (Contenido Protegido)
class AIDefinition(models.Model):
    author = models.CharField(max_length=200, verbose_name="Autor de la Definición")
    definition = models.TextField(verbose_name="Definición")
    image_path = models.CharField(max_length=300, blank=True, null=True, verbose_name="Ruta de la Imagen Estática")
    order = models.IntegerField(default=0, verbose_name="Orden de visualización")

    class Meta:
        verbose_name = "Definición de IA"
        verbose_name_plural = "Definiciones de IA"
        ordering = ['order', 'id']

    def __str__(self):
        return f"Definición por {self.author}"


# Modelo para conceptos educativos globales (por ejemplo, "Redes neuronales artificiales")
class Concept(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre del Concepto")
    description = models.TextField(verbose_name="Descripción del Concepto")
    image_path = models.CharField(max_length=300, blank=True, null=True, verbose_name="Ruta de la Imagen Estática")

    class Meta:
        verbose_name = "Concepto General"
        verbose_name_plural = "Conceptos Generales"

    def __str__(self):
        return self.name


# Modelo para los tipos específicos de Redes Neuronales Artificiales (Contenido Protegido)
class NeuralNetworkType(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre de la Red Neuronal")
    description = models.TextField(verbose_name="Qué es")
    how_it_works = models.TextField(verbose_name="Cómo funciona")
    image_path = models.CharField(max_length=300, blank=True, null=True, verbose_name="Ruta de la Imagen Estática")
    order = models.IntegerField(default=0, verbose_name="Orden de visualización")

    class Meta:
        verbose_name = "Tipo de Red Neuronal"
        verbose_name_plural = "Tipos de Redes Neuronales"
        ordering = ['order', 'id']

    def __str__(self):
        return self.name
