from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return "{f} {l}".format(f=self.first_name, l=self.last_name)


class Email(models.Model):
    address = models.CharField(max_length=100)
    verified = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.address
