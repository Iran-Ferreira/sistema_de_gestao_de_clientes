from django.db import models
from django.urls import reverse

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    birth_date = models.DateField()
    area_code = models.CharField(max_length=3) #DDD do Número
    phone_number = models.CharField(max_length=9)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    create_date = models.DateTimeField(auto_now_add=True) #Data de quando o cliente for criado
    update_date = models.DateTimeField(auto_now=True) #Data de atualização dos dados dos clientes
    active = models.BooleanField(default=True) # Ativar ou desativar o cliente, não precisa apagar todo o histórico do cliente
    
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_full_phone_number(self):
        return f"({self.area_code}) {self.phone_number}"
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_full_city(self):
        return f"{self.city} - {self.state}"
    
    def get_absolute_url(self):
        return reverse("customer:customer-update", kwargs={"id": self.id})
    
    def get_delete_url(self):
        return reverse("customer:customer-delete", kwargs={"id": self.id})
    
    class Meta:
        db_table = "customer"
    