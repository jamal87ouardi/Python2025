type= input("entrer le type de sport: ")
mois= int(input("entrer les mois: "))
if type == "cardio":
    if mois == 1:
       prixtotal= 200
    elif mois == 3:
       prixtotal= 500
    elif mois == 6:
       prixtotal= 600
    else:
        print("mois incorecct")
        exit()
elif type == "musculation":
    if mois == 1:
        prixtotal= 300
    elif mois == 3:
        prixtotal= 700
    elif mois == 6:
        prixtotal= 1300
    else:
        print("mois incorrect")
        exit()
else:
    print("type de sport incorrect")
    exit()
sauna= input("entrer oui pour sona: ")
if sauna == "oui":
    prixtotal += 50*mois
print(prixtotal)