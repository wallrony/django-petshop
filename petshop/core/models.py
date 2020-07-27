from django.db import models

# Create your models here.

class Pet(models.Model):
  LABRADOR = 'LAB'
  BULDOGUE = 'BUL'
  POODLE = 'POO'
  PASTOR_ALEMAO = 'PAS'
  BEAGLE = 'BEA'
  GOLDEN_RETRIEVER = 'GOL'
  CHIHUAHUA = 'CHI'
  HUSKY_SIBERIANO = 'HUS'

  RACA_CHOICES = (
    (LABRADOR, 'Labrador'),
    (BULDOGUE, 'Buldogue'),
    (POODLE, 'Poodle'),
    (PASTOR_ALEMAO, 'Pastor Alemão'),
    (BEAGLE, 'Beagle'),
    (GOLDEN_RETRIEVER, 'Golden Retriever'),
    (CHIHUAHUA, 'Chihuahua'),
    (HUSKY_SIBERIANO, 'Husky Siberiano')
  )

  nome = models.CharField(max_length=30, blank=True)
  raca = models.CharField(max_length=3, choices=RACA_CHOICES)
  idade = models.IntegerField(default=0)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def get_raca_choice(self, choice):
    raca = ''

    for i in range(self.RACA_CHOICES.__len__()):
      if self.RACA_CHOICES.__getitem__(i).__getitem__(0) == choice:
        raca = self.RACA_CHOICES.__getitem__(i).__getitem__(1)
    return raca

  def __str__(self):
    return "{} - {} - {} anos".format(self.nome, self.get_raca_choice(self.raca), self.idade)