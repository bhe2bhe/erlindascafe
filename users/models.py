from django.db import models
# Create your models here.
class Menu(models.Model):
    item = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(default='default-pic.jpg', upload_to='menu_pictures')
    CATEGORIES = [
        ('beverages','Beverages'),
        ('meals','Meals'),
        ('snacks','Snacks')
    ]
    
    DEFAULT_CATEGORY = 'meals'
    category = models.CharField(max_length=20, choices=CATEGORIES, default='meals')
    
    def __str__(self):
        return f"{self.item} -- {self.price}" 
    
    
class Employee(models.Model):
    name = models.CharField(max_length=100)
    caption = models.TextField(max_length=600)
    employee_message = models.TextField(max_length=500)
    image = models.ImageField(default='waiter.png', upload_to='employee_pictures')
    
    def __str__(self):
        return f'{self.name}'
    
    
class Quote(models.Model):
    quote = models.TextField(max_length=1000)
    quote_by = models.CharField(max_length=100)
    image = models.ImageField(default='erlinda-crew.jpg', upload_to='quote_pictures')
    
    def __str__(self):
        return f"{self.quote} -- {self.quote_by}"