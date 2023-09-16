# Viikko 2

## Mitä tehty viikolla
* Toteutan pelimerkkien ja vapaiden paikkojen hallinnan numpy -moduulilla. 0 tarkoittaa 
vapaata paikkaa. Numerot 1 j 2 osoittavat pelaajien pelimerkkejä.
* Toteutan pelin graafisen osuuden pygame -moduulilla.

## Ohjelman edistyminen
* Pelin grafiikka on luotu ja koodattu. Kehikko on sininen ja tyhjät paikat valkoisia. 
Pelaajat voivat pudottaa pelimerkkejä vapaisiin paikkoihin.
* Pelimerkkien ja vapaiden paikkojen hallinnasta vastaava rakenne on koodattu.
* Kirjoitin testimielessä (tyhmän) tekoälyn joka arpoo pelimerkkien sarakkeet eikä ota 
huomioon vastustajan liikkeitä. Pelaajan pelatessa tarkoituksella huonosti, tekoäly 
voittaa.
* Kolme yksikkötestiä kirjoitettu. Yksi testaa, että pelin alussa rivi 0 on tyhjä. 
Kaksi muuta testaavat, että samalla rivillä olevat merkit vaikuttavat oikein pelin 
loppumiseen ja jatkumiseen.

## Mitä opittu
* Testaamisen perusteet
* Minimax -algoritmin perusteet ja miten alpha-beta käytetään sen kanssa

## Epäselvät asiat / vaikeudet
* Ei epäselvyyksiä tai vaikeuksia. Tämän viikon alussa uudet ja vaikealta tuntuvat 
asiat selvisivät viikon aikana työtä tehdessä.

## Ensi viikolla
* Kirjoittaa random AI:n tilalle Minimax -algoritmi ja ymmärtää sen toiminta pelissä.
* Lisätä testejä.
* Saada testikattavuus mukaan koodiin ja visuaaliseen muotoon.

