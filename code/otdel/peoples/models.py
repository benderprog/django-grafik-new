from django.db import models


# Create your models here.
class Rank(models.Model):
    # Звания
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Duty(models.Model):
    name = models.CharField(max_length=10)
    description = models.TextField(max_length=100)

    def __str__(self):
        return self.name


class Person(models.Model):
    surname = models.CharField(max_length=32)
    name = models.CharField(max_length=32)
    otch = models.CharField(max_length=32)
    rank = models.ForeignKey(
        Rank,
        default=1,
        on_delete=models.PROTECT,  # Защита от удаления, если уже есть такой элемент
    )
    age = models.PositiveIntegerField(null=True, blank=True)
    utk = models.BooleanField(default=True)
    duty = models.ForeignKey(
        Duty,
        default=1,
        on_delete=models.PROTECT,  # Защита от удаления, если уже есть такой элемент
    )
    job_title = models.CharField(max_length=100, blank=True)

    def full_name(self):
        return self.surname + ' ' + self.name[0] + '.' + self.otch[0] + '.'

    def __str__(self):
        return self.surname + ' ' + self.name[0] + '.' + self.otch[0] + '.'
