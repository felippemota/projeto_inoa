from django.db import models

# Modelo para os ativos que serão monitorados
class Asset(models.Model):
    name = models.CharField(max_length=200)  # Nome do ativo
    lower_bound = models.FloatField()  # Limite inferior do túnel de preço
    upper_bound = models.FloatField()  # Limite superior do túnel de preço
    check_frequency = models.IntegerField()  # Frequência de checagem da cotação (em minutos)

    def __str__(self):
        return self.name

# Modelo para as cotações dos ativos
class Quotation(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)  # Ativo ao qual a cotação pertence
    price = models.FloatField()  # Preço do ativo
    timestamp = models.DateTimeField(auto_now_add=True)  # Data e hora em que a cotação foi obtida

    def __str__(self):
        return f'{self.asset.name} - {self.price} - {self.timestamp}'
