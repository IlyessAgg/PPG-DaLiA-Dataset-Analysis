from django.db import models

# Create your models here.
class Patient(models.Model):
    chest_ACC_x        = models.FloatField()
    chest_ACC_y        = models.FloatField()
    chest_ACC_z        = models.FloatField()
    chest_Resp         = models.FloatField()
    chest_ECG          = models.FloatField()
    wrist_ACC_x        = models.FloatField()
    wrist_ACC_y        = models.FloatField()
    wrist_ACC_z        = models.FloatField()
    wrist_BVP          = models.FloatField()
    wrist_TEMP         = models.FloatField()
    WEIGHT             = models.FloatField(default=60.0)
    Gender             = models.FloatField()
    AGE                = models.FloatField()
    HEIGHT             = models.FloatField()
    SKIN               = models.FloatField()
    SPORT              = models.FloatField()
    Rpeaks             = models.FloatField()
    Label              = models.FloatField(default=79.8)
    # The dependent variable: y
    Activity           = models.FloatField(null=True)
    # Just to give a date to the creation of the object instance
    created       = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Un patient avec {self.AGE}'
    # We don't have to...
    #class Meta:
    #    ordering = ['created']