from django.db import models

# Create your models here.
class Tasks(models.Model):
    name = models.CharField(max_length=255, verbose_name="Tarea", null=True)
    description = models.CharField(max_length=255, verbose_name="Descripción")
    options = [
        ('to_do', 'Sin avance'),
        ('in_progress', 'En proceso'),
        ('done', 'Hecho')
    ]
    status = models.CharField(choices=options, max_length=50, verbose_name="Opciones")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de actualización")

    status_delete = models.BooleanField(default=False)


    class Meta:
        db_table = 'tasks'
