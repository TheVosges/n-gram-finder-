# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 19:41:28 2020

@author: arkad
"""
from copy import deepcopy
    
def info_check(info):
    """ Funkcja do wprowadzenia danych rna/dna/bialek
            
            Args:
                response (str) : "dna"/"rna"/"bialko"
                info (str) : ciag znaków 
            Returns:
                info (str): ciag dna/rna/bialek
    """ 
    if not isinstance(info, str):
        raise TypeError("Błędny typ danych")
    if info is None or info is '':
        raise TypeError("Brak danych do sprawdzenia")
    info = info.upper()
    z=0
    while z < (len(info)):
        if info[z].upper() not in ['A', 'C', 'G', 'T']: # sprawdzenie czy znaki są poprawne
            raise ValueError("Błędnie podana sekwencja DNA")
        else:
            z+=1
    return info
    
    
            
def aub(tab_napis1,tab_napis2):
    """ Funkcja znajdująca częsc wszystkie mozliwe n-gramy tablic n-gramow
            
            Args:
                tab_napis1 (list): tablica n-gramow pierwszego wyrazu
                tab_napis2 (list): tablica n-gramow drugiego wyrazu
            Returns:
                anb (list): tablica wszyskich mozliwych ngramow wyrazow dla kolejno (2-gramów, 3-gramów i 4-gramów)
    """ 

    if not isinstance(tab_napis1, list) or not isinstance(tab_napis2, list):
        raise TypeError("Błędny typ danych")
    for i in tab_napis1:
        for z in i:
            if not isinstance(z, str):
                raise ValueError("Błędny typ danych")
    for i in tab_napis2:
        for z in i:
            if not isinstance(z, str):
                raise ValueError("Błędny typ danych")
            
    aub = []
    i_napis1 = 0
    while i_napis1 <= (len(tab_napis1)-1):
        if tab_napis1[i_napis1] not in aub:
            aub.append(tab_napis1[i_napis1]) #napierw dodajemy wszystkie wyrazy pierwszego napisu
        i_napis1+=1
         
    i_aub = 0
    i_napis2 = 0
    while i_aub <= (len(aub)-1): 
        while i_napis2 <= (len(tab_napis2)-1):
            tab_pomoc = deepcopy(tab_napis2[i_napis2]) #tworzę nową tablice z tymi samymi wartosciami
            i_pomoc = 0
            while i_pomoc <= (len(tab_pomoc)-1): 
                if tab_pomoc[i_pomoc] not in aub[i_aub]:
                    aub[i_aub].append(tab_pomoc[i_pomoc]) #dopisuję do tablicy aub wartosci z tablicy tab_napis2 ktorych nie ma w tab_napis1 
                i_pomoc+=1
            i_aub+=1
            i_napis2+=1
    return aub    

def anb(tab_napis1,tab_napis2):
    """ Funkcja znajdująca częsc wspolna tablic n-gramow
            
            Args:
                tab_napis1 (list): tablica n-gramow pierwszego wyrazu
                tab_napis2 (list): tablica n-gramow drugiego wyrazu
            Returns:
                aub (list): tablica czesci wspolnej ngramow wyrazow dla kolejno (2-gramów, 3-gramów i 4-gramów)
    """ 
    if not isinstance(tab_napis1, list) or not isinstance(tab_napis2, list):
        raise TypeError("Błędny typ danych")
    for i in tab_napis1:
        for z in i:
            if not isinstance(z, str):
                raise ValueError("Błędny typ danych")
    for i in tab_napis2:
        for z in i:
            if not isinstance(z, str):
                raise ValueError("Błędny typ danych")
    anb = []
    anb_pomoc = []
    i_anb=0
    while i_anb<=(len(tab_napis1)-1):
        tab_pomoc1 = deepcopy(tab_napis1[i_anb])
        tab_pomoc2 = deepcopy(tab_napis2[i_anb])
        i_pomoc1 = 0
        i_pomoc2 = 0
        while i_pomoc1 <= (len(tab_pomoc1)-1):
            while i_pomoc2 <= (len(tab_pomoc2)-1):
                if tab_pomoc2[i_pomoc2] == tab_pomoc1[i_pomoc1]:
                    if tab_pomoc2[i_pomoc2] not in anb_pomoc:
                        anb_pomoc.append(tab_pomoc2[i_pomoc2]) #dopisywane do tablicy anb_pomoc sa wartosci ktore znajduja sie w obu tablicach poczatkowych i nie sa juz w tablicy anb
                i_pomoc2+=1
            i_pomoc2=0
            i_pomoc1+=1
        anb.append(anb_pomoc) #anb_pomoc do anb
        anb_pomoc = []
        i_anb+=1
    return anb        

def jaccard(aub, anb):
    """ Funkcja obliczajaca prawdopodobienstwo jaccarda 
            
            Args:
                aub (list): tablica wszyskich mozliwych n-gramow obu wyrazow
                anb (list): tablica wspolnych n-gramow obu wyrazow
            Returns:
                J (list): tablica podobieństw jaccarda dla kolejno (2-gramów, 3-gramów i 4-gramów)
    """ 
    J = []
    i = 0
    while i<=(len(aub)-1):
        jac = len(anb[i])/len(aub[i]) #proste obliczenie 
        J.append(jac)
        i+=1
    return J
        
def ngramy(napis1,napis2,min_dlugosc_wyrazow,max_dlugosc_wyrazow):
    """ Funkcja dzieląca wyrazy na n-gramy, znajdująca ich częsc wspólną oraz 
        wszyskie możliwe n-gramy a następnie obliczajaca prawdopodobienstwo jaccarda
            
            Args:
                napis1 (str): dowolny ciąg zanków
                napis2 (str): dowolny ciag znaków
                min_dlogosc_wyrazow (int) : dlugosc najmniejszego ngramu
                max_dlugosc_wyrazow (int) : maksymalna dlugosc ngramow
            Returns:
                ngramy (list): tablica ngramow o podanych dlugosciach (np. 2-gramów, 3-gramów i 4-gramów)
    """ 
    if not isinstance(napis1, str) or not isinstance(napis2, str):
        raise TypeError("Błędny typ danych")
    if min_dlugosc_wyrazow>max_dlugosc_wyrazow:
        raise ValueError("Błąd podczas podawania parametrów")
    if len(napis1)<max_dlugosc_wyrazow or len(napis2)<max_dlugosc_wyrazow:
        raise IndexError("Zbyt krótka długosc słowa na podany podział")


    temp_min = min_dlugosc_wyrazow
    temp_max = max_dlugosc_wyrazow
     
    
    #podzial napisu1 na n-gramy i dopisanie ich do tablicy tab_napis1
    tab_napis1 = []
    while min_dlugosc_wyrazow<=max_dlugosc_wyrazow: #do n-rgamow o dlugosci 4
        tab1=[]
        i=0
        while i<=(len(napis1)-1):
            if len(napis1[i:(i+min_dlugosc_wyrazow)])> (min_dlugosc_wyrazow-1):
                if napis1[i:(i+min_dlugosc_wyrazow)] not in tab1:
                    tab1.append(napis1[i:(i+min_dlugosc_wyrazow)]) #dodanie do tablicy n-gramow
            i+=1
        tab_napis1.append(tab1)
        min_dlugosc_wyrazow+=1
    
    #podzial napisu2 na n-gramy i dopisanie ich do tablicy tab_napis2
    min_dlugosc_wyrazow =  temp_min
    max_dlugosc_wyrazow = temp_max
    tab_napis2 = []
    while min_dlugosc_wyrazow<=max_dlugosc_wyrazow:
        tab2=[]
        i=0
        while i<=(len(napis2)-1):
            if len(napis2[i:(i+min_dlugosc_wyrazow)])> (min_dlugosc_wyrazow-1):
                if napis2[i:(i+min_dlugosc_wyrazow)] not in tab2:
                    tab2.append(napis2[i:(i+min_dlugosc_wyrazow)])
            i+=1
        tab_napis2.append(tab2)
        min_dlugosc_wyrazow+=1    
    ngramy = [tab_napis1, tab_napis2] 
    return ngramy

