from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.title

class Reference(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.title

class ContactInfo(models.Model):
    company_name = models.CharField(max_length=100, default='Tlaki Pikelj')
    address = models.CharField(max_length=200, default='Gradišče pri Trebnjem 94A')
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.company_name
    
class CustomerDetails(models.Model):
    ime = models.CharField(max_length=100)
    email = models.EmailField()
    telefonska_stevilka = models.CharField(max_length=15)
    sporocilo = models.TextField()
    
