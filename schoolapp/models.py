from django.db import models

class Material(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Course(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Student(models.Model):
    age = models.PositiveIntegerField(null=True, blank=True)
    address = models.TextField(blank=True)
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15, blank=True)
    dob = models.DateField(null=True, blank=True)
    mail_id = models.EmailField(blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    PURPOSE_CHOICES = [
        ('enquiry', 'For Enquiry'),
        ('order', 'Place Order'),
        ('return', 'Return'),
    ]
    purpose = models.CharField(max_length=255, choices=PURPOSE_CHOICES)
    materials = models.ManyToManyField(Material, blank=True)

    def __str__(self):
        return self.name
