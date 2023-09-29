# Viikko 4

## Mitä tehty viikolla
* Pistelaskujärjestelmää kehitetty lisää
* Minimax -algoritmi on otettu käyttöön. Se on saa laittaa neljännen pelimerkin sarakkeeseen, jos siellä on jo 3. 
Tunnistaa osan pelaajan pysty- ja vaakariveissä olevat 3 merkkiä ja osaa blokata ne.
* Testejä kirjoitettu lisää ml. Minimaxin testaaminen.

## Ohjelman edistyminen
* Minimax -algoritmi on otettu käyttöön ja se osaa pelata vaaka- ja pystyrivejä.
* Pistelaskujärjestelmä ei toimi aivan kuten pitäisi mutta on selvästi havaittavissa, että se osaa muodostaa neljän rivejä 
ja myös blokata niistä osan. Vaikuttaa siltä, että depth 3 pelaa paremmin kuin depth 4. Depth 5 on hidas mutta pelaa hyvin.
* Testejä nyt yhteensä 21 kpl ja pelin testikattavuus on 96%
* Pylint score on 8,68/10

## Mitä opittu
* Minimax -algoritmin toiminta selvinnyt entistä paremmin.

## Epäselvät asiat / vaikeudet
* Miten minimax saadaan paremmin reagoimaan pelaajan pelimerkkeihin ja tekemään oikea arvio seuraavasta siirrosta.

## Ensi viikolla
* Pistelaskujärjestelmän parantaminen
* Toisinaan neljän suora ei johda pelin loppumiseen ja tämä on korjattava
* Vuoronvaihtoa testaavat kaksi testiä eivät mene yhteisajossa aina läpi. Erikseen toimivat aina.