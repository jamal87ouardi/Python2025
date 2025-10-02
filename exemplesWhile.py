
while True:
    n = int(input("Ex4 - Entrez un nombre entre 1 et 10 : "))
    if 1 <= n <= 10:
        print("Correct :", n)
        break
    else:
        print("Nombre invalide ❌")


while True:
    mot = input("Ex6 - Entrez un mot (min 5 caractères) : ")
    if len(mot) >= 5:
        print("Mot valide :", mot)
        break
    else:
        print("Trop court ❌")

# -----------------------------
# Exemple 7 : Calculer la somme jusqu’à un nombre positif
# -----------------------------
while True:
    n = int(input("Ex7 - Entrez un nombre positif : "))
    if n > 0:
        # Calculer la somme de 1 à n
        somme = sum(range(1, n+1))
        print(f"Somme de 1 à {n} = {somme}")
        break
    else:
        print("Nombre non valide ❌")

# -----------------------------
# Exemple 8 : Vérifier une confirmation (O/N)
# -----------------------------
while True:
    rep = input("Ex8 - Voulez-vous continuer ? (O/N) : ").upper()
    if rep in ["O", "N"]:
        print("Votre réponse :", rep)
        break
    else:
        print("Réponse invalide ❌")

# -----------------------------
# Exemple 9 : Diviser deux nombres (éviter division par zéro)
# -----------------------------
while True:
    a = int(input("Ex9 - Entrez un nombre : "))
    b = int(input("Entrez un diviseur : "))
    if b != 0:
        print(f"{a} / {b} = {a/b}")
        break
    else:
        print("Division par zéro interdite ❌")

# -----------------------------
# Exemple 10 : Jeu "pile ou face"
# -----------------------------
import random
while True:
    choix = input("Ex10 - Pile ou Face ? : ").lower()
    if choix in ["pile", "face"]:
        tirage = random.choice(["pile", "face"])
        print("Résultat :", tirage)
        if choix == tirage:
            print("Gagné 🎉")
        else:
            print("Perdu ❌")
        break
    else:
        print("Choix invalide ❌")


