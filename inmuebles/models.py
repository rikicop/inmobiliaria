from django.db import models


class Inmueble(models.Model):
    #codigo = models.CharField(max_length=100)
    codigo = models.DateTimeField(auto_now_add=True)
    tipo = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=1000)
    edo = models.CharField(max_length=1000,blank=True)
    precio = models.DecimalField(max_digits=7,decimal_places=2)
    description = models.TextField()
    image = models.FileField(blank=True)

    def __str__(self):
        template = '{0.codigo} {0.tipo} {0.ubicacion} {0.edo} {0.precio}'
        return template.format(self)

class InmuebleImage(models.Model):
    inmueble = models.ForeignKey(Inmueble, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'images/')

    def __str__(self):
        template = '{0.inmueble.codigo}'
        #return self.inmueble.codigo
        return template.format(self)