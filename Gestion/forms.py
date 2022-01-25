from django.db.models import fields
from django import forms
from .models import OrganismeStage, Jury,Enseignant, Stage, Rapport, Membre, Stagiaire, Convention, Ficheeva
class organismeForm(forms.ModelForm):
    
    class Meta:
        model = OrganismeStage
        fields = "__all__"
        labels ={
            'nomOrganisme': 'Nom Organisme'
        }

class juryForm(forms.ModelForm):
    class Meta:
        model = Jury
        fields = "__all__"
        labels ={
            'codeJ': 'Code Jury',
            'dateSoutenance': 'Date Soutenance'
        }
        widgets={
       'dateSoutenance' : forms.DateInput(attrs={
            'data-target': '#datetimepicker1',
            'placeholder': 'mm/dd/yyyy'
            }),
        }

class EnseignantForm(forms.ModelForm):
    
    class Meta:
        model = Enseignant
        fields = "__all__"
        labels ={
                'nomE': 'Nom Enseignant',
                'prenomE': 'Préom Enseignant',
                'CodeJ': 'Code jury',

            }
class stageForm(forms.ModelForm):
    
    class Meta:
        model = Stage
        fields = "__all__"
        labels ={
                'titrestage': 'Titre de Stage',
                'typestage': 'Type stage',
                'enseignant': 'Nom Enseignant',
                'jury': 'Code jury',
                'organisme': 'Nom Organisme',


            }

class rapportForm(forms.ModelForm):
    
    class Meta:
        model = Rapport
        fields = "__all__"
        labels ={
                'nbrpages': 'Nombre de page',
                'typestage': 'Type stage',
                'stage': 'Titre de Stage'

            }

class membreForm(forms.ModelForm):
    
    class Meta:
        model = Membre
        fields = "__all__"
        labels ={
                'nomM': 'Nom Membre',
                'prenomM': 'Prénom Membre',
                'poste': 'Poste',
                'codeJ': 'Code Jury',
                'organisme': 'Nom Organisme',
                'stage': 'Titre de Stage'

            }
class stagiaireForm(forms.ModelForm):
    
    class Meta:
        model = Stagiaire
        fields = "__all__"
        labels ={
                    'noms': 'Nom Stagiaire',
                    'prenoms': 'Prénom Stagiaire',
                    'DateNaissance': 'Date de naissance',
                    'Email': 'Email',
                    'annedEude': "Année d'étude",
                    'stage': 'Titre de Stage'

            }
        widgets = {
            'noms': forms.TextInput(attrs={'placeholder': 'Nom stagiare','class':"form-control"}),
            'prenoms': forms.TextInput(attrs={'placeholder': 'Prénom(s) stagiare','class':"form-control"}),
            'DateNaissance' : forms.DateInput(attrs={
            'class': 'form-control datepicker-input',
            'data-target': '#datetimepicker1',
            'placeholder': 'mm/dd/yyyy'
            }),
            'Email':forms.TextInput(attrs={'class':'form-control','placeholder': 'name@example.com'}),
            'annedEude':forms.Select(attrs={'class':'form-control','placeholder': "Année d'étude"})
            
        }
        
class conventionForm(forms.ModelForm):
    
    class Meta:
        model = Convention
        fields = "__all__"
        labels ={
                'duree': 'Durée',
                'stage': 'Titre de Stage'

            }

class ficheEvaForm(forms.ModelForm):
    
    class Meta:
        model = Ficheeva
        fields = "__all__"
        labels ={
                'noteava': 'Note Evaluation',
                'stage': 'Titre de Stage'
            }