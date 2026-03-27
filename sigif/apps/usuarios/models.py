from django.db import models

class Usuarios (models.Model):
    nombre = models.CharField(max_length=100)
    contra = models.CharField(max_length=15)
    telefono = models.CharField(max_length=12)
    activo = models.BooleanField(default=True)
    fecha_inicio = models.DateField(help_text="YYYY-MM-DD")
    CARGOS = (
        ("Admin", "ADMIN"),
        ("Empleado", "EMPLEADO"),
    )
    cargo = models.CharField(max_length=15, choices=CARGOS, default = "Empleado")