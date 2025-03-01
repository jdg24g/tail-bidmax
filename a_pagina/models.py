from django.db import models

tipo = [
    ('DELIVERY', 'DELIVERY'),
    ('MESA', 'MESA'),
    ('RECOGER', 'RECOGER'),
]

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    precio = models.PositiveIntegerField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=255)
    celular = models.CharField(max_length=255,blank=True, null=True)
    coordenadas = models.CharField(max_length=255,blank=True, null=True)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.nombre
    
class Ticket(models.Model):
    tipo = models.CharField(max_length=255, choices=tipo)
    cliente = models.CharField(max_length=255,blank=True, null=True)
    celular = models.CharField(max_length=255,blank=True, null=True)
    mesa = models.PositiveIntegerField(blank=True, null=True)
    add_time = models.DateTimeField(auto_now=True)
    productos = models.ManyToManyField(Producto,through='ItemPedido', blank=True)
    observacion = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Ticket'
        verbose_name_plural = 'Tickets'
    def get_total(self):
        return sum(item.cantidad * item.producto.precio for item in self.itempedido_set.all())
    
    def __str__(self):
        return f'{self.cliente} - {self.add_time}'
class ItemPedido(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre}"