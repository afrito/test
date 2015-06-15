from django.db import models

# Create your models here.

class Tipo_Producto(models.Model):
    id_tipo_producto = models.AutoField(primary_key=True)
    nb_tipo_producto = models.CharField(max_length=50)
    
    
class Impuestos(models.Model):
    id_impuestos = models.AutoField(primary_key=True)
    iva = models.FloatField()
    flete = models.FloatField() #cargo por transporte#
    
    
class Producto(models.Model):
    id_prod = models.AutoField(primary_key=True)
    cod_prod =models.CharField(max_length=10)
    nb_prod = models.CharField(max_length=100)
    id_tipo_prod = models.ForeignKey(Tipo_Producto)
    desc_prod = models.TextField()
    precio_prod = models.FloatField()
    status = models.BooleanField(default=True)
    iva = models.ForeignKey(Impuestos)
    

class Inventario(models.Model):
    id_inv = models.AutoField(primary_key=True)
    id_prod = models.IntegerField(unique=True)
    cant_prod = models.IntegerField()
    

class Detalle_Inventario(models.Model): #tabla para indicar el ingreso de productos (detalles)
    id = models.AutoField(primary_key=True)
    id_prod = models.ForeignKey(Producto)
    cant_prod = models.ForeignKey(Inventario)
    id_oper = models.IntegerField()
    fe_oper = models.DateTimeField(auto_now_add=True)
    

class Compras(models.Model):
    id_compras = models.AutoField(primary_key=True)
    id_prod = models.ForeignKey(Producto)
    cant_prod = models.IntegerField()
    fe_compra = models.DateTimeField(auto_now_add=True)
    

class Ventas(models.Model):
    id_venta = models.AutoField(primary_key=True)
    id_prod = models.ForeignKey(Producto)
    cant_prod = models.IntegerField()
    fe_venta = models.DateTimeField(auto_now_add=True)
    

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    rif = models.CharField(max_length=10, unique=True)
    nb_cliente = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    tlf1 = models.CharField(max_length=13)
    tlf2 = models.CharField(max_length=13)
    cel = models.CharField(max_length=13)
    mail = models.CharField(max_length=50)
    status = models.BooleanField(default=True)
    
    
class Cargo(models.Model):
    id_cargo = models.AutoField(primary_key=True)
    nb_cargo = models.CharField(max_length=50)
    desc_cargo = models.CharField(max_length=100)
    
    
class Empleado(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    ci = models.CharField(max_length=50)
    nb_1 = models.CharField(max_length=50)
    nb_2 = models.CharField(max_length=50)
    ap_1 = models.CharField(max_length=50)
    ap_2 = models.CharField(max_length=50)
    tlf1 = models.CharField(max_length=13)
    tlf2 = models.CharField(max_length=13)
    cel = models.CharField(max_length=13) 
    fe_nac = models.DateField()
    mail = models.EmailField()
    direccion = models.CharField(max_length=200)
    sueldo = models.FloatField()
    id_cargo = models.ForeignKey(Cargo) 
    fe_ingreso = models.DateField()
    fe_egreso = models.DateField()
    status = models.BooleanField(default=True)
    

class Rol_Usuario(models.Model):
    id_rol = models.AutoField(primary_key=True)
    nb_rol = models.CharField(max_length=50)
    desc_rol = models.CharField(max_length=100)
    
    
class Pregunta_Usuario(models.Model):
    id_pregunta = models.AutoField(primary_key=True)
    nb_pregunta = (
        ('1', 'Nombre de su Padre'),
        ('2', 'Nombre de su Madre'),
        ('3', 'Nombre de su Mascota'),
        ('4', 'Cual fue su primer Carro'),
    )
    pregunta = models.CharField(max_length=1, choices=nb_pregunta)
    
       
class Usuario(models.Model):
    id_user = models.AutoField(primary_key=True)
    id_rol = models.ForeignKey(Rol_Usuario)
    user = models.CharField(max_length=20)
    clave = models.CharField(max_length=255)
    nb_usuario = models.CharField(max_length=50)
    ap_usuario = models.CharField(max_length=50)
    mail = models.EmailField()
    nb_pregunta = models.ForeignKey(Pregunta_Usuario)
    nb_respuesta = models.CharField(max_length=50)
    fe_create =  models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    
  
class Operacion_Inventario(models.Model):
    id_operacion_inventario = models.AutoField(primary_key=True)
    nb_operacion_inventario = models.CharField(max_length=50)
    
