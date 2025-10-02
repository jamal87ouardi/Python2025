exercice =input("enter le type des exercice :")
mois =int(input("enter le nombre des mois :"))
courscoullecife = input( "enter cour scoullectife oui ou non :")
cochingpersonnalise = input ("enter cochin gpersonnalise oui ou non")
fidelite =input("enter fidelete oui non :")
if exercice == "basique" :
     prix =200*mois
elif exercice =="standard" :
    prix = 350*mois
elif exercice =="premium" :
     prix= 500*mois

else:
    print("type de exercice incorect : ")
    exit()

if cochingpersonnalise =="oui" :
    prix+=(100*mois)
if courscoullecife =="oui":
    prix+=(200 * mois)
if fidelite =="oui":
   prix=prix - 0.2*prix
print(prix)