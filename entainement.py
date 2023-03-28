import random

def game():
    # Génération d'un nombre aléatoire entre 1 et 100
    number = random.randint(1, 100)
    # Nombre d'essais maximum
    max_guesses = 5
    # Compteur d'essais
    guesses = 0

    # Boucle principale du jeu
    while guesses < max_guesses:
        # Demande au joueur de deviner un nombre
        guess = input("Devinez un nombre entre 1 et 100 : ")

        # Vérifie si l'entrée est un nombre
        try:
            guess = int(guess)
        except ValueError:
            print("Veuillez entrer un nombre entier.")
            continue

        # Vérifie si le nombre est dans la plage valide
        if guess < 1 or guess > 100:
            print("Veuillez entrer un nombre entre 1 et 100.")
            continue

        # Incrémente le compteur d'essais
        guesses += 1

        # Vérifie si le joueur a deviné le nombre
        if guess == number:
            print("Bravo ! Vous avez deviné le nombre en", guesses, "essais.")
            return

        # Donne un indice au joueur si le nombre deviné est plus grand ou plus petit que le nombre à deviner
        if guess < number:
            print("Le nombre est plus grand.")
        else:
            print("Le nombre est plus petit.")

    # Le joueur n'a pas réussi à deviner le nombre dans le nombre d'essais maximum
    print("Vous avez épuisé vos essais. Le nombre à deviner était", number)

# Appel de la fonction principale
game()






           


