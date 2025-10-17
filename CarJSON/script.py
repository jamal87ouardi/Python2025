import json

def charger_menu():
    with open("data.json","r",encoding="utf-8") as f:
        return json.load(f)
    
def sauvegarder_menu(voitures):
    with open("data.json","w",encoding="utf-8") as f:
        json.dump(voitures,f,ensure_ascii=False,indent=4)
 

def afficher_menu_client():
    print("\n=== Menu client===")
    print("1.voir les voitures disponibles")
    print("2.louer une voiture")
def afficher_menu_admin(): 
        print("\n=== Menu administrateur===")   
        print("1.ajouter une voiture")
        print("2.modifier une voiture") 
voitures=charger_menu()
  
choix = input("vous etes un administrateur ou un client? (a/c):")


if choix.lower() == "c":
    afficher_menu_client()
    menu = input("votre choix:")
    if menu == "1":
        print("\n---cars disponibles---")
        if voitures:
            print(voitures)
        else:
            print("aucun voiture disponible.")    

    elif menu == "2":
        choix = input("entrer votre choix :")
        if choix in voitures:
            jours = int(input("entrer la duree :"))
            prixtotal = voitures[choix] * jours
            print(f"total a payer pour:{prixtotal}DH")
        else:
            print(f"la voiture '{choix}'n'existe pas.")

elif choix.lower() == "a":
           
    afficher_menu_admin()
    
    choix=input("votre choix :") 


    if choix=="1":
        nom=input("nom du nouvelle voiture:").lower()
        if nom in voitures:
            print(f"voiture '{nom}'existe deja.")
        else:


            prix=int(input("prix de l'inscription:"))
            voitures[nom]=prix
            sauvegarder_menu(voitures)
            print(f" voiture'{nom}'ajoute avec succes.") 


    elif choix=="2":
        nom=input("nom du voiture a modifier:").lower()
        if nom in voitures:
            prix=int(input("nouveau prix de louer:"))
            voitures[nom]=prix
            sauvegarder_menu(voitures)
        else:
            print(f" voiture'{nom}' n esiste pas.")

