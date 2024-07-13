from django.db import models

class Categoria(models.Model):
    id_cat = models.AutoField(primary_key=True)
    categoria_cat = models.CharField(max_length=255)

    def __str__(self):
        return self.categoria_cat


class Empresa(models.Model):
    id_empre = models.AutoField(primary_key=True)
    empresa_empre = models.CharField(max_length=255)

    def __str__(self):
        return self.empresa_empre


class Costo(models.Model):
    id_cos = models.AutoField(primary_key=True)
    c_costo_cos = models.CharField(max_length=255)

    def __str__(self):
        return self.c_costo_cos


class Convenio(models.Model):
    id_con = models.AutoField(primary_key=True)
    nombre_con = models.CharField(max_length=255)
    nombre_oficina_con = models.CharField(max_length=255)
    sucursal_con = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre_con


class Puesto(models.Model):
    id_pue = models.AutoField(primary_key=True)
    puesto_pue = models.CharField(max_length=255)
    calle_pue = models.CharField(max_length=255)
    ciudad_pue = models.CharField(max_length=255)
    provincia_pue = models.CharField(max_length=255)
    fec_ingreso_pue = models.DateField()
    fec_egreso_pue = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.puesto_pue


class Trabajo(models.Model):
    id_tra = models.AutoField(primary_key=True)
    sucursal_tra = models.CharField(max_length=255)
    departamento_tra = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.sucursal_tra} - {self.departamento_tra}'


class Empleado(models.Model):
    id_emp = models.AutoField(primary_key=True)
    ci_emp = models.CharField(max_length=10)
    legajo_emp = models.CharField(max_length=10)
    apellido_emp = models.CharField(max_length=255)
    nombre_emp = models.CharField(max_length=255)
    religion_emp = models.CharField(max_length=255, null=True, blank=True)
    t_doc_emp = models.CharField(max_length=255)
    estado_civil_emp = models.CharField(max_length=255)
    edad_emp = models.IntegerField()
    fecha_nacimiento_emp = models.DateField()
    nacionalidad_emp = models.CharField(max_length=255)
    pais_emp = models.CharField(max_length=255)
    provincia_emp = models.CharField(max_length=255)
    localidad_emp = models.CharField(max_length=255)
    genero_emp = models.CharField(max_length=255)
    puesto = models.ForeignKey(Puesto, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nombre_emp} {self.apellido_emp}'
