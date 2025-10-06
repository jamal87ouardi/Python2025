while True:
    motdepasse=int(input("entrer le mot de passe: "))
    if motdepasse== 1234:
      print("correct :")
      break
    else:
      print("mot de passe incorrect")
type=input("entrer le type de velot: ")
heures=int(input("entrer les heures: "))
casque=input("voulez vous un casque ? (oui/non): ")
siegebebe=input("voulez vous un siegebebe  ? (oui/non): ")
if type=="VTT":
        prixtotale=10*heures
elif type=="VELO VILLE":
        prixtotale=7*heures
elif type=="VELO ELECTRIQUE":
       prixtotale=14*heures
else:
    print("type de velot incorrect")
    exit()
if casque=="oui":
    prixtotale+=10
if siegebebe=="oui":
    prixtotale+=15
print(prixtotale)