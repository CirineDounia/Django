"""gestStage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Gestion.views import indexstatEns, indexstat, index, Organisme, Org_delete, org_edit, jury, jury_edit, jury_delete ,enseignant, fiche_edit, ens_delete, ens_edit, stage, stage_edit, stage_delete, rapport, rapport_edit,rapport_delete, membre, membre_edit, membre_delete, stagiaire, stagiaire_delete, stagiaire_edit, convention, convention_edit,convention_delete, ficheEva, fiche_delete


urlpatterns = [
    path('admin/', admin.site.urls),
    path('HomePage/', index, name="HomePage"),
    path('statistiques/', indexstat, name="statistiques"),
    path('statEns/', indexstatEns, name="statEns"),
    path('Organisme/', Organisme, name="Organisme"),
    path('Stage/', stage, name="Stage"),
    path('Jury/', jury, name="Jury"),
    path('Enseignant/', enseignant, name="Enseignant"),
    path('Rapport/', rapport, name="Rapport"),
    path('membre/', membre, name="Membre"),
    path('Stagiaire/', stagiaire, name="Stagiaire"),
    path('Convention/', convention, name="Convention"),
    path('ficheEva/', ficheEva, name="ficheEva"),
    path('Organisme/delete/<int:pk>/', Org_delete, name='dashboard-Org-delete'),
    path('membre/delete/<int:pk>/', membre_delete, name='dashboard-M-delete'),
    path('Jury/delete/<int:pk>/', jury_delete, name='dashboard-jury-delete'),
    path('Enseignant/delete/<int:pk>/', ens_delete, name='dashboard-ens-delete'),
    path('Stage/delete/<int:pk>/', stage_delete, name='dashboard-stage-delete'),
    path('Rapport/delete/<int:pk>/', rapport_delete, name='dashboard-rapp-delete'),
    path('Stagiaire/delete/<int:pk>/', stagiaire_delete, name='dashboard-stag-delete'),
    path('Convention/delete/<int:pk>/', convention_delete, name='dashboard-conv-delete'),
    path('ficheEva/delete/<int:pk>/', fiche_delete, name='dashboard-fiche-delete'),
    path('Organisme/edit/<int:pk>/', org_edit, name='dashboard-Org-edit'),
    path('Enseignant/edit/<int:pk>/', ens_edit, name='dashboard-ens-edit'),
    path('Jury/edit/<int:pk>/', jury_edit, name='dashboard-jury-edit'),
    path('Stage/edit/<int:pk>/', stage_edit, name='dashboard-stage-edit'),
    path('Rapport/edit/<int:pk>/', rapport_edit, name='dashboard-rapp-edit'),
    path('membre/edit/<int:pk>/', membre_edit, name='dashboard-M-edit'),
    path('Stagiaire/edit/<int:pk>/', stagiaire_edit, name='dashboard-stag-edit'),
    path('Convention/edit/<int:pk>/', convention_edit, name='dashboard-conv-edit'),
    path('ficheEva/edit/<int:pk>/', fiche_edit, name='dashboard-fiche-edit'),
]
