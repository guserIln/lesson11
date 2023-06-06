from django.db import models

# Create your models here.
GENDER_CHOICE = (
   ('М', 'Мужской'),
   ('Ж', 'Женский')
)

class Group(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Patient(models.Model):
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    second_name = models.CharField('Фамилия', max_length=255)
    gender = models.CharField('Пол', max_length=255, choices=GENDER_CHOICE, default=GENDER_CHOICE[0])
    birthDate = models.DateField(default='2000-01-01')

    def __str__(self):
      return self.first_name
class Visit(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    patient_id = models.ForeignKey(Patient,  on_delete=models.CASCADE)
    visitDate = models.DateField(default='2000-01-01')
    def __str__(self):
      return self.name

class User(models.Model):
    name = models.CharField(max_length=40)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name='Группа')
    visit = models.ManyToManyField(Visit, verbose_name='Посещения')
