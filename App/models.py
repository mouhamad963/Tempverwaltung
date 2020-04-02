from django.db import models


# Create your models here.
class Benutzer(models.Model):

    benutzer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256, blank=True, null=False, default='')
    anmeldename = models.CharField(max_length=256, blank=True, null=False, default='')
    telefonnr = models.IntegerField(default=1)


    def __str__(self):
        return self.anmeldename
        
        
    class Meta:
        managed = True
        db_table = 'benutzer'
        
class Hersteller(models.Model):

    hersteller_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256, blank=True, null=False, default='')
  
    def __str__(self):
        return self.name
        
    class Meta:
        managed = True
        db_table = 'hersteller'

class Logs(models.Model):
    log_id = models.AutoField(primary_key=True)

    datum = models.DateTimeField(auto_now=True, blank=True, editable=False, help_text='Update Date')
    nachricht = models.CharField(max_length=256, blank=True, null=False, default='')
    sensor = models.ForeignKey("Sensors", models.DO_NOTHING)
    benutzer = models.ForeignKey("Benutzer", models.DO_NOTHING)

    def __str__(self):
        return self.log_id + " " + self.datum
    
    class Meta:
        
        managed = True
        db_table = 'logs'

class Sensors(models.Model):
    sensor_id = models.AutoField(primary_key=True)

    adresse = models.CharField(max_length=256, blank=True, null=False, default='')
    serverschrank = models.PositiveIntegerField(default=1)
    max_temp = models.PositiveIntegerField(default=1)
    hersteller = models.ForeignKey("Hersteller", models.DO_NOTHING)
    
    
    def __str__(self):
        return self.hersteller.name + " " + self.adresse
    
    class Meta:
        unique_together = ('adresse', 'serverschrank',)
        managed = True
        db_table = 'sensors'


class Temperaturen(models.Model):
    temperatur_id = models.AutoField(primary_key=True)
    datum = models.DateTimeField(auto_now=True, blank=True, editable=False, help_text='Update Date')
    temperatur = models.IntegerField(default=1)
    sensor = models.ForeignKey("Sensors", models.DO_NOTHING)
    
    
    def __str__(self):
        return self.temperatur 
    class Meta:
        managed = True
        db_table = 'temperaturen'

 