from django.shortcuts import render, redirect
from .models import OrganismeStage, Jury, Enseignant,Stage, Rapport, Membre, Stagiaire, Convention, Ficheeva
from .forms import organismeForm, juryForm, EnseignantForm,stageForm,rapportForm, membreForm, stagiaireForm, conventionForm, ficheEvaForm
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,'fenetre/HomePage.html')

def indexstat(request):
    stagiaires= Stagiaire.objects.all()
    stagiaire_count= stagiaires.count()
    stagiaire1= Stagiaire.objects.filter(annedEude='1CPI')
    stagiaire1_count= stagiaire1.count()
    stagiaire2= Stagiaire.objects.filter(annedEude='1CS')
    stagiaire2_count= stagiaire2.count()
    stagiaire3= Stagiaire.objects.filter(annedEude='PFE3CS')
    stagiaire3_count= stagiaire3.count()
    org= OrganismeStage.objects.filter(nomOrganisme='')
    orga = org.count()
    context ={
            'stagiaires': stagiaires,
            'stagiaire_count': stagiaire_count,
            'stagiaire1_count': stagiaire1_count,
            'stagiaire2_count': stagiaire2_count,
            'stagiaire3_count': stagiaire3_count,
            'orga': orga
        }
    return render(request,'fenetre/statistiques.html', context)

def indexstatEns(request):
    enseignants= Enseignant.objects.all()
    enseignant_count= enseignants.count()
    enseignant1= Enseignant.objects.filter(grade='A')
    enseignant1_count= enseignant1.count()
    enseignant2= Enseignant.objects.filter(grade='B')
    enseignant2_count= enseignant2.count()
    enseignant3= Enseignant.objects.filter(grade='C')
    enseignant3_count= enseignant3.count()
    enseignant4= Enseignant.objects.filter(grade='D')
    enseignant4_count= enseignant4.count()
    enseignant5= Enseignant.objects.filter(grade='E')
    enseignant5_count= enseignant5.count()
    context ={
            'enseignants': enseignants,
            'enseignant_count': enseignant_count,
            'enseignant1_count': enseignant1_count,
            'enseignant2_count': enseignant2_count,
            'enseignant3_count': enseignant3_count,
            'enseignant4_count': enseignant4_count,
            'enseignant5_count': enseignant5_count,
        }
    return render(request,'fenetre/statEns.html', context)


def Organisme(request):
    Organismes= OrganismeStage.objects.all()
    organisme_count= Organismes.count()
    if request.method == 'POST':
        form= organismeForm(data=request.POST)
        if form.is_valid():
            form.save()
            organisme_name = form.cleaned_data.get('nomOrganisme')
            messages.success(request, f'{organisme_name} est bien ajouté')
            return redirect('Organisme')
            
        return render(request,'fenetre/Organisme.html', {'form':form})
    else:
        form= organismeForm()
        context ={
            'organismes': Organismes,
            'organisme_count': organisme_count,
            'form':form
        }
        return render(request,'fenetre/Organisme.html', context)
    

def Org_delete(request, pk):
        item = OrganismeStage.objects.get(id=pk)
        if request.method == 'POST':
            item.delete()
            return redirect('Organisme')
        context = {
        'item': item
        }
        return render(request, 'fenetre/deleteOrg.html', context)

def org_edit(request, pk):
    item = OrganismeStage.objects.get(id=pk)
    if request.method == 'POST':
        form = organismeForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('Organisme')
    else:
        form = organismeForm(instance=item)
    context = {
        'form': form,
    }
    return render(request, 'fenetre/EditOrg.html', context)

def jury(request):
    juries= Jury.objects.all()
    jury_count= juries.count()
    if request.method == 'POST':
        form= juryForm(data=request.POST)
        if form.is_valid():
            form.save()
            jury_code = form.cleaned_data.get('codeJ')
            messages.success(request, f'{jury_code } est bien ajouté')
            return redirect('Jury')
            
        return render(request,'fenetre/Jury.html', {'form':form})
    else:
        form= juryForm()
        context ={
            'juries': juries,
            'jury_count': jury_count,
            'form':form
        }
        return render(request,'fenetre/Jury.html', context)
    
def jury_edit(request, pk):
    item = Jury.objects.get(id=pk)
    if request.method == 'POST':
        form = juryForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('Jury')
    else:
        form = juryForm(instance=item)
    context = {
        'form': form,
    }
    return render(request, 'fenetre/EditJury.html', context)
def jury_delete(request, pk):
        item = Jury.objects.get(id=pk)
        if request.method == 'POST':
            item.delete()
            return redirect('Jury')
        context = {
        'item': item
        }
        return render(request, 'fenetre/deleteJury.html', context)

def enseignant(request):
    enseignants= Enseignant.objects.all()
    enseignant_count= enseignants.count()
    if request.method == 'POST':
        form= EnseignantForm(data=request.POST)
        if form.is_valid():
            form.save()
            Enseignant_name = form.cleaned_data.get('nomE')
            messages.success(request, f'{Enseignant_name } est bien ajouté')
            return redirect('Enseignant')
            
        return render(request,'fenetre/Enseignant.html', {'form':form})
    else:
        form= EnseignantForm()
        context ={
            'enseignants': enseignants,
            'enseignant_count': enseignant_count,
            'form':form
        }
        return render(request,'fenetre/Enseignant.html', context)

def ens_delete(request, pk):
        item = Enseignant.objects.get(id=pk)
        if request.method == 'POST':
            item.delete()
            return redirect('Enseignant')
        context = {
        'item': item
        }
        return render(request, 'fenetre/deleteEnseignant.html', context)

def ens_edit(request, pk):
    item = Enseignant.objects.get(id=pk)
    if request.method == 'POST':
        form = EnseignantForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('Enseignant')
    else:
        form = EnseignantForm(instance=item)
    context = {
        'form': form,
    }
    return render(request, 'fenetre/editEnseignant.html', context)

def stage(request):
    stages= Stage.objects.all()
    stage_count= stages.count()
    if request.method == 'POST':
        form= stageForm(data=request.POST)
        if form.is_valid():
            form.save()
            Stage_name = form.cleaned_data.get('titreStage')
            messages.success(request, f'{Stage_name } est bien ajouté')
            return redirect('Stage')
            
        return render(request,'fenetre/Stage.html', {'form':form})
    else:
        form= stageForm()
        context ={
            'stages': stages,
            'stage_count': stage_count,
            'form':form
        }
        return render(request,'fenetre/Stage.html', context)
def stage_edit(request, pk):
    item = Stage.objects.get(id=pk)
    if request.method == 'POST':
        form = stageForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('Stage')
    else:
        form = stageForm(instance=item)
    context = {
        'form': form,
    }
    return render(request, 'fenetre/editstage.html', context)

def stage_delete(request, pk):
        item = Stage.objects.get(id=pk)
        if request.method == 'POST':
            item.delete()
            return redirect('Stage')
        context = {
        'item': item
        }
        return render(request, 'fenetre/deleteStage.html', context)

def rapport(request):
    rapports= Rapport.objects.all()
    rapport_count= rapports.count()
    if request.method == 'POST':
        form= rapportForm(data=request.POST)
        if form.is_valid():
            form.save()
            rapport_id = form.cleaned_data.get('id')
            messages.success(request, f'{rapport_id } est bien ajouté')
            return redirect('Rapport')
            
        return render(request,'fenetre/Rapport.html', {'form':form})
    else:
        form= rapportForm()
        context ={
            'rapports': rapports,
            'rapport_count': rapport_count,
            'form':form
        }
        return render(request,'fenetre/Rapport.html', context)

def rapport_edit(request, pk):
    item = Rapport.objects.get(id=pk)
    if request.method == 'POST':
        form = rapportForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('Rapport')
    else:
        form = rapportForm(instance=item)
    context = {
        'form': form,
    }
    return render(request, 'fenetre/editrapp.html', context)
def rapport_delete(request, pk):
        item = Rapport.objects.get(id=pk)
        if request.method == 'POST':
            item.delete()
            return redirect('Rapport')
        context = {
        'item': item
        }
        return render(request, 'fenetre/deleterapp.html', context)

def membre(request):
    membres= Membre.objects.all()
    membre_count= membres.count()
    if request.method == 'POST':
        form= membreForm(data=request.POST)
        if form.is_valid():
            form.save()
            membre_name = form.cleaned_data.get('nomM')
            messages.success(request, f'{membre_name} est bien ajouté')
            return redirect('Membre')
            
        return render(request,'fenetre/membre.html', {'form':form})
    else:
        form= membreForm()
        context ={
            'membres': membres,
            'membre_count': membre_count,
            'form':form
        }
        return render(request,'fenetre/membre.html', context)
    
def membre_delete(request, pk):
        item = Membre.objects.get(id=pk)
        if request.method == 'POST':
            item.delete()
            return redirect('Membre')
        context = {
        'item': item
        }
        return render(request, 'fenetre/deletemem.html', context)

def  membre_edit(request, pk):
    item = Membre.objects.get(id=pk)
    if request.method == 'POST':
        form = membreForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('Membre')
    else:
        form = membreForm(instance=item)
    context = {
        'form': form,
    }
    return render(request, 'fenetre/editmem.html', context)

def stagiaire(request):
    stagiaires= Stagiaire.objects.all()
    stagiaire_count= stagiaires.count()
    stagiaire1= Stagiaire.objects.filter(annedEude='1CPI')
    stagiaire1_count= stagiaire1.count()
    stagiaire2= Stagiaire.objects.filter(annedEude='1CS')
    stagiaire2_count= stagiaire2.count()
    stagiaire3= Stagiaire.objects.filter(annedEude='PFE3CS')
    stagiaire3_count= stagiaire3.count()
    if request.method == 'POST':
        form= stagiaireForm(data=request.POST)
        if form.is_valid():
            form.save()
            stagiaire_name = form.cleaned_data.get('noms')
            messages.success(request, f'{stagiaire_name} est bien ajouté')
            return redirect('Stagiaire')
            
        return render(request,'fenetre/Stagiaire.html', {'form':form})
    else:
        form= stagiaireForm()
        context ={
            'stagiaires': stagiaires,
            'stagiaire_count': stagiaire_count,
            'stagiaire1_count': stagiaire1_count,
            'stagiaire2_count': stagiaire2_count,
            'stagiaire3_count': stagiaire3_count,
            'form':form
        }
        return render(request,'fenetre/Stagiaire.html', context)
    
def stagiaire_delete(request, pk):
        item = Stagiaire.objects.get(id=pk)
        if request.method == 'POST':
            item.delete()
            return redirect('Stagiaire')
        context = {
        'item': item
        }
        return render(request, 'fenetre/deleteStagiaire.html', context)

def  stagiaire_edit(request, pk):
    item = Stagiaire.objects.get(id=pk)
    if request.method == 'POST':
        form = stagiaireForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('Stagiaire')
    else:
        form = stagiaireForm(instance=item)
    context = {
        'form': form,
    }
    return render(request, 'fenetre/editStagiaire.html', context)
def convention(request):
    conventions= Convention.objects.all()
    convention_count= conventions.count()
    if request.method == 'POST':
        form= conventionForm(data=request.POST)
        if form.is_valid():
            form.save()
            stagiaire_name = form.cleaned_data.get('noms')
            messages.success(request, f'{stagiaire_name} est bien ajouté')
            return redirect('Convention')
            
        return render(request,'fenetre/Convention.html', {'form':form})
    else:
        form= conventionForm()
        context ={
            'conventions': conventions,
            'convention_count': convention_count,
            'form':form
        }
        return render(request,'fenetre/Convention.html', context)
    
def  convention_edit(request, pk):
    item = Convention.objects.get(id=pk)
    if request.method == 'POST':
        form = conventionForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('Convention')
    else:
        form = conventionForm(instance=item)
    context = {
        'form': form,
    }
    return render(request, 'fenetre/editconv.html', context)

def convention_delete(request, pk):
        item = Convention.objects.get(id=pk)
        if request.method == 'POST':
            item.delete()
            return redirect('Convention')
        context = {
        'item': item
        }
        return render(request, 'fenetre/deleteconv.html', context)

def ficheEva(request):
    fiches= Ficheeva.objects.all()
    fiche_count= fiches.count()
    if request.method == 'POST':
        form= ficheEvaForm(data=request.POST)
        if form.is_valid():
            form.save()
            fiche_name = form.cleaned_data.get('id')
            messages.success(request, f' la fiche N° {fiche_name} est bien ajouté')
            return redirect('Convention')
            
        return render(request,'fenetre/ficheEva.html', {'form':form})
    else:
        form= ficheEvaForm()
        context ={
            'fiches': fiches,
            'fiche_count': fiche_count,
            'form':form
        }
        return render(request,'fenetre/ficheEva.html', context)
    
def  fiche_edit(request, pk):
    item = Ficheeva.objects.get(id=pk)
    if request.method == 'POST':
        form = ficheEvaForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('ficheEva')
    else:
        form = ficheEvaForm(instance=item)
    context = {
        'form': form,
    }
    return render(request, 'fenetre/EditFiche.html', context)

def fiche_delete(request, pk):
        item = Ficheeva.objects.get(id=pk)
        if request.method == 'POST':
            item.delete()
            return redirect('ficheEva')
        context = {
        'item': item
        }
        return render(request, 'fenetre/deleteFICHE.html', context)
