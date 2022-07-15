
from django.db import models



# Create your models here.


    
        
    

class MyUser(models.Model):
    
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    message = models.CharField(max_length=500)
   

    
    
    def __str__(self):
        if self.name is None:
            return "Name cannot be empty"
        
        else:
            
            return self.name
