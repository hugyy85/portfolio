from django.db import models
from django.conf import settings


class UploadFile(models.Model):
    file = models.FileField(upload_to='app/')


#############################
# One - to - many structure
class Names(models.Model):
    number = models.CharField(primary_key=True, unique=False, max_length=11)
    name = models.CharField(max_length=128)

    # def __str__(self):
    #     return self.name

    class Meta:
        verbose_name = 'Номер'
        verbose_name_plural = 'Номера'


class Numbers(models.Model):
    # столбец для разделения загрузки данных
    id_process = models.IntegerField(null=False, default=1)
    number = models.ForeignKey(Names, to_field='number', on_delete=models.CASCADE)
    date = models.CharField(max_length=64)
    time = models.TimeField()
    who_call = models.CharField(max_length=64)
    how_long = models.CharField(max_length=128, default=1)

    def __str__(self):
        return str(self.number)

    class Meta:
        verbose_name = 'Звонок'
        verbose_name_plural = 'Звонки'


class User:
    # class for save data, to check numbers
    def __init__(self, number, id_process=1):
        self.number = number
        self.id_process = id_process
        # data[0] - date, data[1] - time, data[2] = who_call, data[3] - how_long
        self.data = []




