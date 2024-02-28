from enum import Enum

class Type(Enum): 
    ACOUSTIC = 1 
    ELECTRIC = 2 

class Builder(Enum): 
    FENDER = 1
    MARTIN = 2
    GIBSON = 3 
    COLLINGS = 4
    OLSON = 5 
    RYAN = 6 
    PRS = 7 
    ANY = 8 


class Wood(Enum): 
    INDIAN_ROSEWOOD = 1
    BRAZILIAN_ROSEWOOD  = 2 
    MAHOGANY = 3
    MAPLE = 4 
    COCOBOLO = 5 
    CEDAR = 6 
    ADIRONDACK = 7 
    ALDER = 8 
    SITKA = 9 