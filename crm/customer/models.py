from django.db import models

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
    
    class Meta:
        db_table = "customer"
    