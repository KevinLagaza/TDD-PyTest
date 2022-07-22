# -*- coding: utf-8 -*-
"""
Created on Wed July 21 2022

@author: Kevin
"""

"""
LeJustePrix !

But de l'exercice :
    
Le programme demande à l'utilisateur de saisir un nombre de tentatives
pour simuler les "30 secondes". Ce nombre de tentatives représentera 
le nombre d'echecs possible.

"""

# importation de la methode random
import random

class LeJustePrix():
    """
        Classe utilitaire qui permet de determiner 
        le juste prix apres un certain nombre de tentatives
    """   

    def __init__(self):

        pass

    def input_Nbre_Tentatives(self)->int:
        """
            Fonction demande a l'utilisateur de saisir le 
            nombre de tentatives qui simulera les 30s

            params : Aucun

            return : Nombre
        """
        try:

            nb_Tentatives = int(input("Entrez le nombre de tentatives : "))
        except ValueError as e:

            print(" il faut saisir un nombre !!! ")
            LeJustePrix.input_Nbre_Tentatives()
                    
        return nb_Tentatives
    
    def nombreAleatoire(self)->int:
        """
            Fonction demande a l'utilisateur de saisir
            la borne superieure de l'intervalle qui 
            contiendra le nombre aleatoire a generer

            params : Aucun

            return : Nombre aleatoire 
        """
        
        try:

            borne_sup = int(input("Entrez la borne sup : "))
        except ValueError as e:

            print(" il faut saisir un nombre !!! ")
            LeJustePrix.nombreAleatoire()

        # création d'un nombre aleatoire 
        nombreAleatoire = random.randint(1, borne_sup)
                    
        return nombreAleatoire
    
    def deviner_le_resultat(self)->int:
        """
            Fonction demande a l'utilisateur de deviner 
            le resultat attendu pour gagner le jeu

            params : Aucun

            return : Nombre
        """
        try:

            nbre_devine = int(input("Deviner le resultat : "))
        except ValueError as e:

            print(" il faut saisir un nombre !!! ")
            LeJustePrix.deviner_le_resultat()
                    
        return nbre_devine

    def comparaison(self, num1:int, num2:int)->str:
        """
            Fonction qui compare deux nombres

            params : 
                num1 : nombre devine
                num2 : nombre aleatoire

            return : Nombre
        """

        if num1 < num2:

            res = "PLUS"
            print("c'est plus!!")
        # cas si c'est moins
        elif num1 > num2:

            res = "MOINS"
            print("c'est moins!!")
        # cas si c'est ni plus ni moins donc gagné
        else:

            res = "GAGNÉ"
        
        return str(res)
    
    def retirer_nbre_vies(self, nbre_de_chances:int)->int:
        """
            Fonction qui diminue le nombre de 
            tentatives de l'utilisateur lorsque 
            le resultat attendu n'est pas trouve

            params : Nombre de chances restantes

            return : Nombre
        """

        nbre_de_chances -= 1

        return nbre_de_chances
            

    def monJustePrix(self):
        """
            Fonction qui determine le juste prix

            params : Aucun

            Return : Aucun
        """

        # saisir le nombre de chances
        nbre_de_chances = LeJustePrix().input_Nbre_Tentatives()       
        # generer le nombre aleatoire correspondant au résultat attendu 
        nombreAleatoire = LeJustePrix().nombreAleatoire()
        # petit message de bienvenue pour commencer le jeu
        print("Bienvenue dans le Juste Prix !!")

        while (True): 

            # demande un nombre et l'enregistre dans une variable
            nbre_devine = LeJustePrix().deviner_le_resultat()
            res = LeJustePrix().comparaison(nbre_devine, nombreAleatoire)
            if res == "PLUS" or res == "MOINS":

                # diminuer le nombre de vies
                nbre_de_chances = LeJustePrix().retirer_nbre_vies(nbre_de_chances)
            else:

                # resultat trouvé, donc fin du jeu
                print("BINGO!! Vous êtes l'heureux gagnant de ce jeu")
                print("Le nombre était :", nombreAleatoire)
                break

            # si le maximum de chances est atteint
            if nbre_de_chances == 0:

                print("C'est PERDU ! Le nombre était :", nombreAleatoire)
                break
            # sinon on enleve un essai et on continue la boucle
            else:
                print("Il vous reste",nbre_de_chances,"essais.")
