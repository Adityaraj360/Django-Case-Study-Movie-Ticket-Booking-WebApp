from django.db import models

# Create your models here.
class shows(models.Model):
    Show_time=models.TimeField()

class Seats(models.Model):
    Status1=models.CharField(max_length=10,default="Unbooked")
    Status2=models.CharField(max_length=10,default="Unbooked")
    Status3=models.CharField(max_length=10,default="Unbooked")
    Status4=models.CharField(max_length=10,default="Unbooked")
    Status5=models.CharField(max_length=10,default="Unbooked")
    Status6=models.CharField(max_length=10,default="Unbooked")
    S_no1=models.IntegerField()
    S_no2=models.IntegerField()
    S_no3=models.IntegerField()
    S_no4=models.IntegerField()
    S_no5=models.IntegerField()
    S_no6=models.IntegerField()
    def __str__(self):
        return(str(self.S_no6))

class Bookings(models.Model):
    movie_name=models.CharField(max_length=50)
    # Show_time=models.TimeField()
    # Date=models.DateField()
    price=models.IntegerField()
    selected_seats=models.CharField(max_length=100)
    u_name=models.CharField(max_length=30,default="Nikitha")
    
    # def __str__(self):
    #     return str(self.u_name)


class Movies(models.Model):
    name = models.CharField(max_length=50)
    image=models.CharField(max_length=255)
    date = models.DateField()
    duration = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    rating = models.CharField(max_length=50)
    trailer = models.CharField(max_length=100)
    price = models.IntegerField(default=0)

    def __str__(self):
        return str(self.name)

