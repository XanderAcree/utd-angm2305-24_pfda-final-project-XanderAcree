import pygame
from pygame.locals import *
import random

class EldenRandom():
    def eldenAttribute(self, numRange = 255):
        self.numRange = numRange
        randAttribute = random.randrange(numRange)
        return randAttribute
    
    def set_r(self, r = random.randrange(255)):
            self.r = r
            return r

    def set_g(self, g = random.randrange(255)):
            self.g = g
            return g

    def set_r(self, b = random.randrange(255)):
            self.b = b
            return b

    def eldenColor(self, returnValues = False):

        r = EldenRandom.set_r
        g = random.randrange(255)
        b = random.randrange(255)

        self.returnValues = returnValues

        randColor = pygame.Color(r,g,b)

        colorReturnList = [r,g,b]
        if returnValues == True:
            return colorReturnList
        else:
            return randColor

    def __init__(self, _numRange = 255, isAttribute = True, isColor = False, isBool = False):
        
        _randAttribute = EldenRandom.eldenAttribute(_numRange)
        self._randAttribute = _randAttribute

        _randColor = EldenRandom.eldenColor()
        self._randColor = _randColor

        _randCol_r = EldenRandom.eldenColor(True)

        randCol_g = random.randrange(255)

        randCol_b = random.randrange(255)

        #__init__ Boolean Variables
        self.isAttribute = isAttribute
        self.isColor = isColor
        self.isBool = isBool
    
    def randBase(self):
        randAttribute