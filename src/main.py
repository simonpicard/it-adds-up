# -*- coding: utf8 -*-

from node import *


class compteEstBon:
    def __init__(self, res, values):
        self.node = Node(res, values)
        # création d'un noeud représentant le compte à trouver avec les données
        self.res = self.node.getRes()
        # récupération du resultat a trouver
        self.operation = ["+", "-", "*", "/"]
        # création d'une liste comprenant les différentes opérations
        self.maxBT = len(self.node.getValues()) - 1
        # création de l'indice de récurcivité maximale, il s'agit du nombre de chiffres donnés moins un
        # à chaque récursivité on suprime 2 éléments pour en ajouter un
        bestCalcul, bestResult, end = self.compter(
            0, self.node.getValues(), [], [], None, False
        )
        # appel de la fonction qui calcule le resultat
        self.node.setBestRes(bestResult)
        self.node.setBestCalcul(bestCalcul)
        # ajout des resultats dans le noeud

    def compter(self, z, values, calcul, bestCalcul, bestResult, end):
        """Calcul le résultat le plus proche du résultat demandé avec le détail du calcul"""
        if z == self.maxBT:
            # si on a atteint la récursivité maximale
            if bestResult == None or abs(bestResult - self.res) > abs(
                int(values[0]) - self.res
            ):
                # s'il n'y a pas encore de meilleur résultat définis ou que le résultat actuel est plus proche du résultat
                # demandé que le meilleur résultat actuel
                bestResult = int(values[0])
                bestCalcul = list(calcul)
                # on sauvegarde ce resultat
            if bestResult == self.res:
                # si le résultat actuel vaut le résultat demandé
                end = True
                # l'algorithme est fini
        else:
            for i in range(len(values)):
                # pour chacune des valeurs
                for j in range(i + 1, len(values)):
                    # pour chaque valeurs après la valeur précédemment sélectionnée
                    # il est inutile de calculer 3+5 et 5+3 par exemple
                    # donc on ne prend que les valeurs suivantes
                    for o in self.operation:
                        # pour chaque opération
                        if not end:
                            # si l'algorithme n'est pas finis
                            v0 = values[i]
                            v1 = values[j]
                            # on prend les deux valeurs sélectionnées
                            resultatNaturel = True
                            # on initialise une boolean qui garantira que le résultat est un naturel
                            if o == "*":
                                resultat = v0 * v1
                            elif o == "-":
                                resultat = v0 - v1
                                strRes = (
                                    str(v0)
                                    + o
                                    + str(v1)
                                    + " = "
                                    + str(resultat)
                                )
                                if resultat == 0:
                                    # si le résultat est nul
                                    resultatNaturel = False
                                elif resultat < 0:
                                    # si le résultat est négatif, on inverse la soustraction
                                    # le résultat sera forcément positif
                                    resultat = v1 - v0
                                    strRes = (
                                        str(v1)
                                        + o
                                        + str(v0)
                                        + " = "
                                        + str(resultat)
                                    )
                            elif o == "+":
                                resultat = v0 + v1
                            else:
                                resultat = v0 * 1.0 / v1
                                if int(resultat) != resultat:
                                    # si le résultat n'est pas un entier, on inverse la soustraction
                                    resultatNaturel = False
                                else:
                                    resultat = int(resultat)
                            if resultatNaturel:
                                if o != "-":
                                    strRes = (
                                        str(v0)
                                        + o
                                        + str(v1)
                                        + " = "
                                        + str(resultat)
                                    )
                                    # création d'une chaine de caractère qui représante l'opération effectuée
                                    # sauf pour la soustraction où la chaine de caractère est faite dans la condition précédante
                                    # car les valeurs peuvent être inversée
                                newValues = list(values)
                                del newValues[j]
                                del newValues[i]
                                newValues.append(resultat)
                                # on crée une nouvelle liste sans les deux valeurs utilisée et avec le resultat de l'opération
                                calcul.append(strRes)
                                # on ajoute l'opération dans le calcul
                                bestCalcul, bestResult, end = self.compter(
                                    z + 1,
                                    newValues,
                                    calcul,
                                    bestCalcul,
                                    bestResult,
                                    end,
                                )
                                # on rappel la fonction avec les nouvelles valeurs
                                calcul.pop()
                                # on supprime la dernière opération de la liste et on refait un tour de boucle
        # on retourne les valeurs qui permette d'obtenir le calcul pour arriver au résultat
        # et l'état de l'algorithme
        return bestCalcul, bestResult, end

    def affiche(self):
        """Affiche le calcul ayant mené au résultat"""
        bestCalcul = self.node.getBestCalcul()
        bestResult = self.node.getBestRes()
        res = self.res
        # on récupère le résultat demandé, le résultat se raprochant le plus du résultat demandé et le calcul
        if res == bestResult:
            # si le résultat demandé vaut le résultat se raprochant le plus du résultat demandé
            print("Le compte est bon !")
        else:
            print(
                "Le compte est approché de " + str(abs(res - bestResult)) + "."
            )
        for i in range(len(bestCalcul)):
            print(bestCalcul[i])
            # on affiche le calcul

    def getMax(self):
        """Retourne le résultat se raprochant le plus du résultat demandé"""
        return self.node.getBestRes()


if __name__ == "__main__":
    values = []
    for i in range(7):
        donneeNotOk = True
        while donneeNotOk:
            donneeNotOk = False
            try:
                if i == 6:
                    res = int(
                        input(
                            "\nVeuillez entrer un nombre entre 1 et 999\nqui"
                            " sera le resultat a trouver. "
                        )
                    )
                    if not 0 < res < 1000:
                        # si la valeur n'est pas comprise entre 1 et 999
                        donneeNotOk = True
                else:
                    value = int(
                        input(
                            "\nVeuillez entrer un nombre entre 1 et 999\nqui"
                            " sera un des nombres utilisable pour trouver le"
                            " nombre ("
                            + str(i)
                            + "/6). "
                        )
                    )
                    if 0 < value < 1000:
                        values.append(value)
                    else:
                        donneeNotOk = True
            except ValueError:
                # si la valeur n'est pas un nombre
                donneeNotOk = True
    CEB = compteEstBon(res, values)
    CEB.affiche()
