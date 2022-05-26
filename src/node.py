# -*- coding: utf8 -*-

# Cette classe représente le compte à trouver avec les données


class Node:
    def __init__(self, res, values, bestRes=None, bestCalcul=None):
        self.res = res
        self.values = values
        self.bestRes = bestRes
        self.bestCalcul = bestCalcul

    def getRes(self):
        return self.res

    def getValues(self):
        return self.values

    def getBestRes(self):
        return self.bestRes

    def getBestCalcul(self):
        return self.bestCalcul

    def setValues(self, newValues):
        self.values = newValues

    def setBestRes(self, newBestRes):
        self.bestRes = newBestRes

    def setBestCalcul(self, newBestCalcul):
        self.bestCalcul = newBestCalcul

    def setRes(self, newRes):
        self.res = newRes
