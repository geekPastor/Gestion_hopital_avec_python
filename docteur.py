import os
from clear_consol import clear_consol


"""définition de fonction Enregistrer un docteur : nom, prenom, postnom, téléphone
, matricule, spécialisation (ex: pédiatre, gynecologue, etc.)"""
docteurs = []

def enregistre_docteur(prenom, nom, postnom, tel, specialisation, genre):
    clear_consol()
    print("################################################################")
    print("##                                                            ##")
    print("##                    ENREGISTRER UN DOCTEURS                 ##")
    print("##                                                            ##")
    print("################################################################")
    identites_docteur= []
    matricule = nom[0]+postnom[0]+prenom[0:4]+tel[-1:-4:-1]
    identites_docteur.append(prenom.upper())
    identites_docteur.append(nom.upper())
    identites_docteur.append(postnom.upper())
    identites_docteur.append(specialisation.upper())
    identites_docteur.append(tel)
    identites_docteur.append(matricule.upper())
    identites_docteur.append(genre.upper())
    docteurs.append(identites_docteur)


"""Afficher tous les docteurs"""
def afficher_docteur():
    clear_consol()
    print("################################################################")
    print("##                                                            ##")
    print("##        VOICI LA LISTE DE TOUS LES DOCTEURS                ##")
    print("##                                                            ##")
    print("################################################################")
    if len(docteurs) > 0:
        for i in range(len(docteurs)):
            print(f'\nPrénom : {docteurs[i][0]}\nNom: {docteurs[i][1]}\nPostnom: {docteurs[i][2]}\nSpécialité : {docteurs[i][3]}\nNuméro de téléphone : {docteurs[i][4]}\nMatricule : {docteurs[i][5]}\nGenre : {docteurs[i][6]}\n')
    else :
        print("La liste est encore vide !")


def afficher_horaire(prenom, nom, postnom):
    clear_consol()
    chercher_docteur = []
    for i in range(len(docteurs)):
        if len(docteurs[i]) >= 8:
            chercher_docteur.append(prenom.upper())
            chercher_docteur.append(nom.upper())
            chercher_docteur.append(postnom.upper())
            for chercher_docteur in docteurs[i]:
                if chercher_docteur in docteurs[i]:
                    print(f'Prénom : {docteurs[i][0]}\nNom: {docteurs[i][1]}\nPostnom : {docteurs[i][2]}\nVoici son horaire :\n     Lundi :{docteurs[i][7]}\n       Mardi :{docteurs[i][8]}\n       Mercredi :{docteurs[i][9]}\n        Jeudi :{docteurs[i][10]}\n      Vendredi :{docteurs[i][11]}\n       Samedi{docteurs[i][12]}\n       Dimanche :{docteurs[i][13]}')
                    break
                else :
                    print("Ses identifiants ne sont pas dans la liste des docteurs")
                    break
        else:
            print("Pour ce médecin l'horaire n'est pas encore enregistre")




def enregistrer_horaire(prenom, postnom, nom):
    clear_consol()
    print("################################################################")
    print("##                                                            ##")
    print("##             ENREGISTRER L'HORAIRE D'UN DOCTEUR               ##")
    print("##                                                            ##")
    print("################################################################")
    horaire = []
    identifiants = []
    identifiants.append(prenom.upper())
    identifiants.append(nom.upper())
    identifiants.append(postnom.upper())
    for i in range(len(docteurs)):
        for identifiants in docteurs[i]:
            if identifiants in docteurs[i]:
                jour1 = input("Entrez son horaire du lundi: ")
                jour2 = input("Entrez son horaire du mardi: ")
                jour3 = input("Entrez son horaire du mercredi: ")
                jour4 = input("Entrez son horaire du jeudi: ")
                jour5 = input("Entrez son horaire du vendredi: ")
                jour6 = input("Entrez son horaire du samedi: ")
                jour7 = input("Entrez son horaire du dimanche: ")
                horaire.append(jour1)
                horaire.append(jour2)
                horaire.append(jour3)
                horaire.append(jour4)
                horaire.append(jour5)
                horaire.append(jour6)
                horaire.append(jour7)
                docteurs[i].append(horaire)
                break
            else:
                print("Ses identifiants ne sont pas dans la liste des Docteurs")
                break

#CHRINOVIC MUKEBA



def ajouter_horaire(jour, nomDocteur):
    clear_consol()
    for i in range(len(docteurs)):
        if len(docteurs[i]) >= 8:
            for j in range(len(docteurs[i])):
                if nomDocteur in docteurs[i]:
                    
                    if jour.lower() == "lundi":
                        action = input("Entrez la tâche à ajouter du lundi: ")
                        docteurs[i][7].append(action)
                                    
                    elif jour.lower() == "mardi":
                        action = input("Entrez la tâche à ajouter du mardi: ")
                        docteurs[i][8].append(action)
                                    
                    elif jour.lower() == "mercredi":
                        action = input("Entrez la tâche à ajouter du mercredi: ")
                        docteurs[i][9].append(action)
                                    
                    elif jour.lower() == "jeudi":
                        action = input("Entrez la tâche à ajouter à celle du jeudi: ")
                        docteurs[i][10].append(action)
                                    
                    elif jour.lower() == "vendredi":
                        action = input("Entrez la tâche à ajouter à celle du vendredi: ")
                        docteurs[i][11].append(action)
                                    
                    elif jour.lower() == "samedi":
                        action = input("Entrez la tâche à ajouter à celle du samedi: ")
                        docteurs[i][12].append(action)
                                    
                    elif jour.lower() == "dimanche":
                        action = input("Entrez la tâche à ajouter à celle du dimanche: ")
                        docteurs[i][13].append(action)
                                    
                    else:
                        print("Le jour que vous avez saisi n'existe pas !!")
            else:
                print("Ce nom n'est pas dans notre liste")




def changer_horaire(jour, nomDocteur):
    clear_consol()
    for i in range(len(docteurs)):
        if len(docteurs[i]) >= 8:
            for j in range(len(docteurs[i])):
                if nomDocteur in docteurs[i]:
                    if jour.lower() == "lundi":
                        action = input("Entrez la nouvelle tâche du lundi: ")
                        docteurs[i][7] = action
                                    
                    elif jour.lower() == "mardi":
                        action = input("Entrez la nouvelle tâche du mardi: ")
                        docteurs[i][8] = action
                                    
                    elif jour.lower() == "mercredi":
                        action = input("Entrez la nouvelle tâche du mercredi: ")
                        docteurs[i][9] = action
                                    
                    elif jour.lower() == "jeudi":
                        action = input("Entrez la nouvelle tâche du jeudi: ")
                        docteurs[i][10] = action
                                    
                    elif jour.lower() == "vendredi":
                        action = input("Entrez la nouvelle tâche du vendredi: ")
                        docteurs[i][11] = action
                                    
                    elif jour.lower() == "samedi":
                        action = input("Entrez la nouvelle tâche du samedi: ")
                        docteurs[i][12] = action
                                    
                    elif jour.lower() == "dimanche":
                        action = input("Entrez la nouvelle tâche du dimanche: ")
                        docteurs[i][13] = action
                                    
                    else:
                        print("Le jour que vous avez saisi n'existe pas !!")
