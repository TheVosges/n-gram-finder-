# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 14:01:38 2021
@pytest.fixture 
@author: arkad
"""
import ngramy
import numpy as np
import pytest

def test_info_input():
    "Test sprawdzenia poprawnych danych"
    slowo = ngramy.info_check('acgt')
    assert  slowo=='ACGT'
   
def test_info_input_zle_dane():
    "Test sprawdzenia niepoprawnych danych"
    with pytest.raises(ValueError):
        ngramy.info_check('qwerty')

def test_info_input_puste():
    "Test sprawdzenia pustych danych"
    with pytest.raises(TypeError):
        ngramy.info_check('')
        
def test_info_input_zly_typ_danych():
    "Test sprawdzenia złego typu danych"
    with pytest.raises(TypeError):
        ngramy.info_check(32)
        
def test_ngramy_zla_kolejnosc_parametrow():
    "Test sprawdzenia złych parametrów podziału ngramów (min>max)"
    with pytest.raises(ValueError):
        ngramy.ngramy("ACGT","TGCA",4,2)

def test_ngramy_zla_dlugosc_parametrow():
    "Test sprawdzenia złych parametrów podziału ngramów (zbyt duże ngramy)"
    with pytest.raises(IndexError):
        ngramy.ngramy("ACGT","TGCA",2,6)

def test_ngramy_zly_typ_parametrow():
    "Test sprawdzenia złego typu danych wejsciowych"
    with pytest.raises(TypeError):
        ngramy.ngramy(32,"TGCA",2,6)    

def test_aub_zly_typ_danych():
    "Test sprawdzenia złego typu danych"
    with pytest.raises(TypeError):
        ngramy.aub(32, ["el", "le", "me"])

def test_aub_puste_tablice():
    "Test sprawdzenia sumy pustych danych"
    tablica = ngramy.ngramy("","",0,0)
    suma = ngramy.aub(tablica[0],tablica[1])
    assert np.array_equal(suma, [[]])

def test_anb_zly_typ_danych():
    "Test sprawdzenia złego typu danych"
    with pytest.raises(TypeError):
        ngramy.anb(["el", "le", "me"], 13)

def test_anb_pusta_tablica():
    "Test sprawdzenia dla braku częsci wspólnej danych"
    tablica = ngramy.ngramy("QWERTY","ACGTCGA",2,2)
    suma = ngramy.anb(tablica[0],tablica[1])
    assert np.array_equal(suma, [[]])
           
def test_elemelek_kundelek():
    "Test poprawnego podziału słów elemelek i kundelek"
    tablica = ngramy.ngramy("elemelek","kundelek",2,4)
    assert np.array_equal(tablica, [[['el', 'le', 'em', 'me', 'ek'], ['ele', 'lem', 'eme', 'mel', 'lek'], ['elem', 'leme', 'emel', 'mele', 'elek']], [['ku', 'un', 'nd', 'de', 'el', 'le', 'ek'], ['kun', 'und', 'nde', 'del', 'ele', 'lek'], ['kund', 'unde', 'ndel', 'dele', 'elek']]])

def test_aub_elemelek():
    "Test poprawnego sprawdzenia sumy ngramow slów elemelek i kundelek"
    tablica = ngramy.ngramy("elemelek","kundelek",2,4)
    suma = ngramy.aub(tablica[0],tablica[1])
    assert np.array_equal(suma, [['el', 'le', 'em', 'me', 'ek', 'ku', 'un', 'nd', 'de'], ['ele', 'lem', 'eme', 'mel', 'lek', 'kun', 'und', 'nde', 'del'], ['elem', 'leme', 'emel', 'mele', 'elek', 'kund', 'unde', 'ndel', 'dele']])
 
def test_anb_elemelek():
    "Test poprawnego sprawdzenia częsci wspólnej ngramow slów elemelek i kundelek"
    tablica = ngramy.ngramy("elemelek","kundelek",2,4)
    wspolne = ngramy.anb(tablica[0],tablica[1])
    assert np.array_equal(wspolne, [['el', 'le', 'ek'], ['ele', 'lek'], ['elek']])

def test_jaccard_elemelek():
    "Test sprawdzenia współczynnika podobieństwa dla slów elemelek i kundelek dla 2,3,4-ngramow"
    tablica = ngramy.ngramy("elemelek","kundelek",2,4)
    suma = ngramy.aub(tablica[0],tablica[1])
    wspolne = ngramy.anb(tablica[0],tablica[1])
    j = ngramy.jaccard(suma, wspolne)
    assert np.array_equal(j,[0.7777777777777778, 0.6666666666666666, 0.5555555555555556])

    
    