# n-gram-finder-
Program that finds commont parts of 2 words and calculates jaccards corelation. 

Example: 
    elemelek
{el le em me ek}
{ele lem eme mel lek}
{elem leme emel mele elek}

kundelek
{ku un nd de el le ek}
{kun und nde del ele lek}
{kund unde ndel dele elek}

AuB = {el le em me ek ku un nd de}

|AuB|=9

AnB = {el le ek}
|AnB|=3

J=3/9

3gram
AuB = {ele lem eme mel kun und nde del lek}
|AuB|=9

AnB = {ele  lek}
|AnB|=2

J=2/9

4gram
AuB = {elem leme emel mele elek kund unde ndel dele}
|AuB|= 9 
AnB = {elek}
|AnB|=1

J=1/9
