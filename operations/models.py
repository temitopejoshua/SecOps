from django.db import models
from django.contrib.auth.models import AbstractUser


class Elders(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    staff_id = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.IntegerField()
    image_1 = models.ImageField(upload_to="Elders/image1", null=True)
    image_2 = models.ImageField(upload_to="Elders/image2", null=True)
    image_3 = models.ImageField(upload_to="Elders/image3", null=True)
    image_4 = models.ImageField(upload_to="Elders/image4", null=True)
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('first_name',)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Natives(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    native_id = models.CharField(max_length=20)
    email = models.EmailField()
    phone_number = models.IntegerField()
    image_1 = models.ImageField(upload_to="Natives/image1", null=True)
    image_2 = models.ImageField(upload_to="Natives/image2", null=True)
    image_3 = models.ImageField(upload_to="Natives/image3", null=True)
    image_4 = models.ImageField(upload_to="Natives/image4", null=True)
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('first_name',)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Citizens(models.Model):
    full_name = models.CharField(max_length=150)
    image = models.ImageField(upload_to="citizens/image", null=True)

    class Meta:
        ordering = ('full_name',)

    def __str__(self):
        return "{}".format(self.full_name)


class Activities(models.Model):
    time_In = models.DateTimeField(auto_now_add=True)
    time_Out = models.DateTimeField(auto_now_add=True)
    elder = models.ForeignKey(Elders, on_delete=models.CASCADE)
    native = models.ForeignKey(Natives, on_delete=models.CASCADE)
    citizen = models.ForeignKey(Citizens, models.CASCADE)

    class Meta:
        ordering = ('pk',)

    def __str__(self):
        return "{}".format(self.pk)


class CustomUser(AbstractUser):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.email
