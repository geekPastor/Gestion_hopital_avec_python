 #le début du programme
import os
from clear_consol import clear_consol
from patients import enregistre_patient, chercher_patient_avec_numero_dossier, afficher_patient, afficher_les_plaintes_patient, afficher_imc_patient, chercher_patient_avec_ses_identifiants
from docteur import enregistre_docteur,  afficher_docteur, ajouter_horaire,  afficher_horaire,  enregistrer_horaire, changer_horaire
print("################################################################")
print("##                                                            ##")
print("##         PROGRAMME DE GESTION D'UN HOPITAL EN PYTHON        ##")
print("##                                                            ##")
print("################################################################")

#La déclaration des variables globales




def fonction_principale():
    os.system('pause')
    clear_consol()
    print("################################################################")
    print("##                                                            ##")
    print("##                       MENU PRINCIPALE                      ##")
    print("##                                                            ##")
    print("################################################################")
    print(f'Voici les actions que vous pouvez réaliser dans ce programme\n0: Pour quitter le programme\n1: Pour Enregistrer un docteur\n2: Pour Enregistrer un patient\n3: Chercher un patient par ses identités\n4: Chercher un patient par le numero de dossier\n5: Afficher tous les patients\n6: Afficher tous les docteurs\n7: Enregistrer l\'horaire de chaque medecin\n8: Afficher les plaintes d\'un patient à partir de son numero unique\n9: Afficher l\'IMC (indice de masse corporel) d\'un patient\n10: Pour Afficher l\'horaire d\'un médecin\n11: Pour ajouter à l\'horaire d\'un docteur\n12: Pour changer l\'horaire d\'un docteur')
    choix = input ("\n>>>>")
    if choix.lower() == "0":
        exit()
        
    elif choix.lower() == "1":
        prenom = input("Entrez le prenom du nouveau docteur: ")
        nom = input("Entrez le nom du nouveau docteur: ")
        postnom = input("Entrez le postenom du nouveau docteur: ")
        tel = input("Entrez le numéro de téléphone du nouveau docteur: ")
        specialisation = input("Quel est la spécialisattion du nouveau docteur: ")
        genre= input("Entrez le genre du nouveau docteur (M ou F): ")
        enregistre_docteur(prenom, nom, postnom, tel, specialisation, genre)
        os.system('pause')
        clear_consol()
        fonction_principale()
        
    elif choix.lower() == "2":
        prenom_patient = input("Entrez le prenom du patient: ")
        nom_patient = input("Entrez le nom du patient: ")
        postnom_patient = input("Entrez le postenom du patient: ")
        tel_patient = input("Entrez le numéro de téléphone du patient: ")
        poids_patient = float(input("Entrez le poids du patient"))
        taille_patient = float(input("Entrez la taille du patient: "))
        genre_patient = input("Entrez le genre du nouveau patient M ou F: ")
        age_patient = int(input("Entrez l'âge du patient: "))
        plaintes_patient = input("De quoi souffre le patient: ")
        date = input("Entrez la date de l'enregistrement avec cette anneautation 22-06-2022: ")
        enregistre_patient(prenom_patient, nom_patient, postnom_patient, tel_patient, poids_patient, taille_patient, genre_patient, age_patient, plaintes_patient, date)
        os.system('pause')
        clear_consol()
        fonction_principale()
        
    elif choix.lower() == "3":
        prenom = input("Entrez le prenom du patient que vous voulez chercher: ")
        nom = input("Entrez le nom du patient que vous voulez chercher: ")
        postnom = input("Entrez le postnom du patient que vous voulez chercher: ")
        chercher_patient_avec_ses_identifiants(prenom, nom, postnom)
        os.system('pause')
        clear_consol()
        fonction_principale()
        
    elif choix.lower() == "4":
        numero_dossier = input("Entrez le numéro du dossier du patient: ")
        print(chercher_patient_avec_numero_dossier(numero_dossier))
        os.system('pause')
        clear_consol()
        fonction_principale()
        
    elif choix.lower() == "5":
        print(afficher_patient())
        os.system('pause')
        clear_consol()
        fonction_principale()
        
    elif choix.lower() == "6":
        print(afficher_docteur())
        os.system('pause')
        clear_consol()
        fonction_principale()
        
    elif choix.lower() == "7":
        prenom = input("Entrez le prenom du docteur pour leque vous voulez Enregistrer l'horaire: ")
        nom = input("Entrez le nom du docteur pour leque vous voulez Enregistrer l'horaire: ")
        postnom = input("Entrez le postnom du docteur pour leque vous voulez Enregistrer l'horaire: ")
        print(enregistrer_horaire(prenom, nom, postnom))
        os.system('pause')
        clear_consol()
        fonction_principale()
        
    elif choix.lower() == "8":
        numero_dossier = input("Entrez le numéro du dossier du patient: ")
        afficher_les_plaintes_patient(numero_dossier)
        os.system('pause')
        clear_consol()
        fonction_principale()
        
    elif choix.lower() == "9":
        numero_dossier = input("Entrez le numéro du dossier du patient: ")
        print(afficher_imc_patient(numero_dossier))
        os.system('pause')
        clear_consol()
        fonction_principale()
        
    elif choix.lower() == "10":
        prenom = input("Entrez le prenom du Docteur pour lequel vous voulez voir l'horaire: ")
        nom = input("Entrez le nom du Docteur pour lequel vous voulez voir l'horaire: ")
        postnom = input("Entrez le postnom du Docteur pour lequel vous voulez voir l'horaire: ")
        print(afficher_horaire(prenom, nom, postnom))
        os.system('pause')
        clear_consol()
        fonction_principale()
        
    elif choix.lower() == "11":
        jour = input("Pour quel jour vous voulez ajouter la tâche: ")
        nomDocteur = input("Entrez le nom du docteur pour lequel vous voulez ajouter une tâche à l'horaire: ")
        print(ajouter_horaire(jour, nomDocteur))
        os.system('pause')
        clear_consol()
        fonction_principale()
        
    elif choix.lower() == "12":
        jour = input("Pour quel jour vous voulez changer la tâche: ")
        nomDocteur = input("Entrez le nom du docteur pour lequel vous voulez ajouter une tâche à l'horaire: ")
        print(changer_horaire(jour, nomDocteur))
        os.system('pause')
        clear_consol()
        fonction_principale()
        
    else :
        print("Cette fonction n'est pas reconnu !\n\n")
        os.system('pause')
        clear_consol()
        fonction_principale()
fonction_principale()
