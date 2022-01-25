from django.db import models
from datetime import date
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
# Create your models here.
class OrganismeStage (models.Model):
    nomOrganisme = models.CharField(max_length=20,null=False)
    adresse = models.CharField(max_length=40,null=False)
    email = models.CharField(max_length=20,null=False)
    def __str__(self):
        return f'{self.nomOrganisme}'

class Jury(models.Model):
    codeJ = models.CharField(max_length=15)
    dateSoutenance = models.DateField(default="01/01/2022",null= False)
    def __str__(self):
        return f'{self.codeJ}'
    
class Enseignant(models.Model):
    nomE = models.CharField(max_length=20,null=False)
    prenomE = models.CharField(max_length=20,null=False)
    class ge(models.TextChoices):
        A = 'A',_('Maître assistant A')
        B = 'B',_('Maître assistant B')
        C = 'C',_('Maître de conférence A')
        D = 'D',_('Maître de conférence B')
        E = 'E',_('Professeur')
    grade = models.CharField(max_length=20,choices=ge.choices)
    codeJ = models.ForeignKey(Jury, on_delete=models.SET_NULL, null= True, blank=True )
    def __str__(self):
        return f'{self.nomE}'

class Stage(models.Model):
    titreStage = models.CharField(max_length=40)
    class ts(models.TextChoices):
        CP1 = '1CP',_('Stage ouvrier 1CP')
        CS1 = '1CS',_('Stage technique 1CS')
        CS3 = 'PFE3CS',_('Stage technique PFE 3CS')
    typeStage = models.CharField(max_length=30, choices=ts.choices)
    enseignant = models.ForeignKey(Enseignant,on_delete=models.CASCADE)
    #stagiaire = models.ManyToManyField(stagiaire,related_name='stagiaire')
    #rapport =  models.ManyToManyField(Rapport,related_name='rapport')
    #rapport = models.ForeignKey(Rapport,on_delete=models.SET_NULL, null= False, blank=False )
    jury = models.ForeignKey(Jury,on_delete=models.SET_NULL, null= True, blank=True )
    organisme = models.ForeignKey(OrganismeStage, on_delete=models.CASCADE )
    def __str__(self):
        return f'{self.titreStage}'
         
class Rapport(models.Model):
    nbrpages = models.IntegerField()
    stage = models.ForeignKey(Stage,on_delete=models.SET_NULL, null= True, blank=False )
    #stage = models.OneToOneField(Stage, null=True, on_delete=models.CASCADE)
    #stage = models.ManyToManyField(Stage,related_name='stage')s
    def __int__(self):
        return f'{self.nbrpages}'
    def __str__(self):
        return f'{self.stage.titreStage}'

class Membre(models.Model):
    nomM = models.CharField(max_length=20)
    prenomM = models.CharField(max_length=20)
    poste = models.CharField(max_length=20)
    codeJ = models.ForeignKey(Jury, on_delete=models.SET_NULL, null= True, blank=True )
    organisme = models.ForeignKey(OrganismeStage, on_delete=models.CASCADE)
    stage = models.ForeignKey(Stage,on_delete=models.SET_NULL, null= True, blank=True )
    def __str__(self):
        return f'{self.nomM}'

class Stagiaire (models.Model):
    noms = models.CharField(max_length=40, null= False)
    prenoms = models.CharField(max_length=40, null= False)
    DateNaissance = models.DateField(default="01/01/2022",null= False)
    Email = models.EmailField(max_length = 254, null= False)
    class ad(models.TextChoices):
        CP1 = '1CPI',_('1CPI')
        CS1 = '1CS',_('1CS')
        CS3 = 'PFE3CS',_('3CS')
    annedEude = models.CharField(max_length=20, choices=ad.choices)
    stage = models.ForeignKey(Stage, on_delete=models.SET_NULL, null= True, blank=True )
    def __str__(self):
        return f'{self.noms}'
       
class Convention(models.Model):
    duree = models.CharField(max_length=2)
    stage = models.ForeignKey(Stage,on_delete=models.CASCADE )
    def __str__(self):
        return f'{self.duree}'
    def __str__(self):
        return f'{self.stage}'

class Ficheeva(models.Model):
    noteava = models.IntegerField(default=0, validators=[
            MaxValueValidator(20),
            MinValueValidator(0)])
    stage = models.ForeignKey(Stage,on_delete=models.CASCADE )

    def __float__(self):
        return f'{self.noteava}'
