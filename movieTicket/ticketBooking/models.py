from django.db import models

# Create your models here.
# class shows():
#     Show_time=models.TimeField()

# class Seats():
#     S_No=models.IntegerField()
#     Status=models.CharField(default="Unbooked")
#     def __str__(self):
#         return str(self.Status)

# class Bookings(models.Model):
#     movie_name=models.CharField(max_length=50)
#     # Show_time=models.TimeField()
#     # Date=models.DateField()
#     prize=models.IntegerField()
#     selected_seats=models.CharField(max_length=100)
#     u_name=models.CharField(max_length=30,default="Nikitha")
    
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
# class movies(models.Model):
#     name = models.CharField(max_length=100)
#     image = models.ImageField(upload_to="pics", default='default.png')
#     date = models.DateField()
#     duration = 
