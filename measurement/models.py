from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=70)

    def __str__(self):
        return f'{self.name} - {self.description}'


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, related_name='measurement', on_delete=models.CASCADE)
    temperature = models.FloatField()
    at_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Датчик {self.sensor.name} - {self.temperature} - {self.at_date}'

