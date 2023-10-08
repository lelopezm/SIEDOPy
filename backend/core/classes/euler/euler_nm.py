from django.db import models


class Euler_nm(models.Model):
    ''' Class Euler_nm is used to approximate. '''
    name: str = models.CharField(max_length=63)
    result: float = models.FloatField()
    # error: float = models.FloatField()
    # time: float = models.FloatField()
    # date: str = models.DateField(auto_now_add=True)
    # graphic: str = models.ImageField(upload_to='euler_nm/graphics')

    def __str__(self):
        return self.name
