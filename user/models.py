from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return f"{self.name}{self.email}{self.subject}{self.message}"

class Subscribed(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()


    def __str__(self):
        return f"{self.name}{self.email}"
class Collect(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    business = models.TextField()
    feedback = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}{self.mobile}{self.location}{self.business}{self.feedback}"


class Service(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    industry = models.CharField(max_length=200)
    bn = models.CharField(max_length=200)
    wu = models.CharField(max_length=200)
    jt = models.CharField(max_length=200)
    years = models.IntegerField()
    email = models.EmailField()
    number = models.CharField(max_length=11)
    howhelp = models.CharField(max_length=200)


    def __str__(self):
        return f"{self.firstname}{self.lastname}{self.industry}{self.bn}{self.wu}{self.jt}{self.years}{self.email}{self.number}{self.howhelp}{self.file}"
