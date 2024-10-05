from django.db import models

# Modelo que representa um paciente
class Paciente(models.Model):
    nome = models.CharField(max_length=100)  # Nome do paciente
    contato = models.CharField(max_length=15)  # Contato do paciente

    def __str__(self):
        return self.nome

# Modelo que representa uma consulta
class Consulta(models.Model):
    STATUS_CHOICES = [
        ('AGENDADO', 'Agendado'),
        ('CANCELADO', 'Cancelado'),
        ('REAGENDADO', 'Reagendado'),
    ]

    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)  # Relacionamento com o paciente
    data = models.DateField()  # Data da consulta
    hora = models.TimeField()  # Hora da consulta
    motivo = models.TextField()  # Motivo da consulta
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='AGENDADO')  # Status da consulta

    def __str__(self):
        return f'{self.paciente.nome} - {self.data} {self.hora}'
