import os
from clear_consol import clear_consol

""" Enregistrer un patient : nom, prenom, postnom, téléphone
, poids, taille, genre, age, numero de dossier (un code unique que vous allez généré)"""


patients = []
def enregistre_patient(prenom_patient, nom_patient, postnom_patient, tel_patient, poids_patient, taille_patient, genre_patient, age_patient, plaintes_patient, date):
    clear_consol()
    print("###################################################################")
    print("##                                                               ##")
    print("##                    ENREGISTREMENT UN PATIENT                  ##")
    print("##                                                               ##")
    print("###################################################################")
    identites_patient= []
    imc = ""
    
    indice_de_masse_corporel_patient = poids_patient / taille_patient**2
    if indice_de_masse_corporel_patient < 18.5:
        imc = "Insuffisance pondérale (maigreur)"
    elif indice_de_masse_corporel_patient >= 18.5 and indice_de_masse_corporel_patient < 25:
        imc = "Corpulence normale"
    elif indice_de_masse_corporel_patient >= 25 and indice_de_masse_corporel_patient < 30:
        imc = "Surpoids"
    elif indice_de_masse_corporel_patient >= 30 and indice_de_masse_corporel_patient < 35:
        imc = "Obésité modérée"
    elif indice_de_masse_corporel_patient >= 35 and indice_de_masse_corporel_patient < 40:
        imc = "Obésité sévère"
    elif indice_de_masse_corporel_patient > 40:
        imc = "Obésité morbide ou massive"
    numero_dossier_patient = (date[0:2])+str(nom_patient[0].upper())+str(date[3:5])+str(postnom_patient[0].upper())+str(date[7::])
    identites_patient.append(prenom_patient.upper())
    identites_patient.append(nom_patient.upper())
    identites_patient.append(postnom_patient.upper())
    identites_patient.append(poids_patient)
    identites_patient.append(taille_patient)
    identites_patient.append(genre_patient.upper())
    identites_patient.append(age_patient)
    identites_patient.append(imc.upper())
    identites_patient.append(plaintes_patient.upper())
    identites_patient.append(numero_dossier_patient)
    identites_patient.append(date)
    identites_patient.append(tel_patient)
    patients.append(identites_patient)


    
"""Chercher un patient par le numero de dossier
et on retourne le seul patient ayant ce numero """

def chercher_patient_avec_numero_dossier(numero_dossier):
    print("#############################################")
    print("##           Traitement en cours veillez patientez              ##")
    print("#############################################")
    os.system('pause')
    clear_consol()
    for i in range(len(patients)):
        for j in patients[i]:
            if numero_dossier == patients[i][-3]:
                print(f'Prénom : {patients[i][0]}\nNom: {patients[i][1]}\n Postnom: {patients[i][2]}\nNuméro de téléphone du patient :{patients[i][-1]}\nPoids : {patients[i][3]}\nTaille : {patients[i][4]}\nGenre : {patients[i][5]}\nAge : {patients[i][6]}\nIMC : {patients[i][7]}\nPlaintes : {patients[i][8]}\nNuméro du dossier :{patients[i][9]}\nDate : {patients[i][10]}')
                break
            else :
                print("Aucun patuient n'a ce numéro dans la liste")
                break



"""Afficher tous les patients"""
def afficher_patient():
    print("#############################################")
    print("##           Traitement en cours veillez patientez              ##")
    print("#############################################")
    os.system('pause')
    clear_consol()
    if len(patients) > 0:
        for i in range(len(patients)):
            print(f'Prénom : {patients[i][0]}\nNom: {patients[i][1]}\n Postnom: {patients[i][2]}\nNuméro de téléphone du patient :{patients[i][-1]}\nPoids : {patients[i][3]}\nTaille : {patients[i][4]}\nGenre : {patients[i][5]}\nAge : {patients[i][6]}\nIMC : {patients[i][7]}\nPlaintes : {patients[i][8]}\nNuméro du dossier :{patients[i][9]}\nDate : {patients[i][10]}')
    else :
        print("La liste est encore vide !")


"""Afficher les plaintes d'un patient à partir de son numero unique"""

def afficher_les_plaintes_patient(numero_dossier):
    print("#############################################")
    print("##           Traitement en cours veillez patientez              ##")
    print("#############################################")
    os.system('pause')
    clear_consol()
    for i in range(len(patients)):
        for j in patients[i]:
            if numero_dossier == patients[i][-3]:
                print(f'Prénom : {patients[i][0]}\nNom: {patients[i][1]}\nPostnom: {patients[i][2]}\nPlainte :{patients[i][-4]}')
                break
            else :
                print("Aucun patuient n'a ce numéro dans la liste")
                break

                
def afficher_imc_patient(numero_dossier):
    print("#############################################")
    print("##           Traitement en cours veillez patientez              ##")
    print("#############################################")
    os.system('pause')
    clear_consol()
    for i in range(len(patients)):
        for j in patients[i]:
            if numero_dossier == patients[i][-3]:
                print(f'Prénom : {patients[i][0]}\nNom: {patients[i][1]}\nPostnom: {patients[i][2]}\nIndice de masse corporel :{patients[i][-5]}')
                break
            else :
                print("Aucun patuient n'a ce numéro dans la liste")
                break



"""Chercher un patient par ses identités (nom, postnom ou prénom)
et on nous retourne la liste des utilisateurs ayants ces informations """

def chercher_patient_avec_ses_identifiants(prenom, nom, postnom):
    print("#############################################")
    print("##           Traitement en cours veillez patientez              ##")
    print("#############################################")
    os.system('pause')
    clear_consol()
    chercher_patient = []
    chercher_patient.append(prenom)
    chercher_patient.append(nom)
    chercher_patient.append(postnom)
    for i in range(len(patients)):
        for j in patients[i]:
            if chercher_patient[0] == patients [i][0] and  chercher_patient[1] ==patients [i][1] and  chercher_patient[2] ==patients [i][2]:
                print(f'Prénom : {patients[i][0]}\nNom: {patients[i][1]}\n Postnom: {patients[i][2]}\nPoids : {patients[i][3]}\nTaille : {patients[i][4]}\nGenre : {patients[i][5]}\nAge : {patients[i][6]}\nIMC : {patients[i][7]}\nPlaintes : {patients[i][8]}\nNuméro du dossier :{patients[i][9]}\nDate : {patients[i][10]}')
                break
            else :
                print("Ses identifiants ne sont pas dans la liste des patients")
                break
