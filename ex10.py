destination=input("entrer la distination: ")
nbpersonne=int(input("entrer le nombre de personne:"))
if destination== "caire":
    if nbpersonne==1:
        prixtotal=8000
    elif nbpersonne== 2:
        prixtotal =1500
    else:
        print("nbpersonne non disponible ")
elif destination== "istanbul":
    if nbpersonne== 1:
       prixtotal =11000
    elif nbpersonne== 2:
       prixtotal =22000
    else:
        print("nbpersonne non disponible ")
        exit()
elif destination== "paris":
    if nbpersonne==1:
        prixtotal=6000
    elif nbpersonne== 2:
         prixtotal =11000
    else:
        print("nbpersonne non disponible ")
        exit()
else:
    print("destination non disponible ")
    exit()
print(prixtotal)