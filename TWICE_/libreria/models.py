from django.db import models


# Create your models here.
class Libro(models.Model):
    id=models.AutoField(primary_key=True)
    titulo=models.CharField(max_length=100, verbose_name='Nombre')
    imagen=models.ImageField(upload_to='imagenes/',verbose_name='Portada', null=True)
    descripcion=models.TextField(verbose_name='Lanzamiento/Version',null=True)

    def __str__(self):
        fila="Nombre: " + self.titulo + "-" + "Lanzamiento/Version: " + self.descripcion
        return fila

    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()