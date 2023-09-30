# Viikko 4

## Mitä tehty viikolla
* Pistelaskujärjestelmää kehitetty lisää
* Minimax -algoritmi on otettu käyttöön. Se osaa laittaa neljännen pelimerkin sarakkeeseen, jos siellä on jo 3. 
Tunnistaa osan pelaajan rivissä/sarakkeessa/viistosti olevat 3 merkkiä ja osaa blokata ne.
* Testejä kirjoitettu lisää ml. Minimaxin testaaminen.
* Alpha-beta -karsinta lisätty Minimaxiin.

## Ohjelman edistyminen
* Minimax -algoritmi ja alpha-beta -karsinta on otettu käyttöön. Tekoälyn pelitaso parani.
* Pistelaskujärjestelmä ei toimi aivan kuten pitäisi mutta on selvästi havaittavissa, että se osaa muodostaa neljän rivejä 
ja myös blokata niistä osan.
* Testejä nyt yhteensä 30 kpl ja pelin testikattavuus on 97%
* Pylint score on 8,97/10

## Mitä opittu
* Minimax -algoritmin toiminta selvinnyt entistä paremmin
* Alpha-beta -karsinnan käyttö yhdessä minimaxin kanssa
* Testaamiseen tullut enemmän rutiinia

## Epäselvät asiat / vaikeudet
* Miten Minimax saadaan paremmin reagoimaan pelaajan pelimerkkeihin ja tekemään oikea arvio seuraavasta siirrosta.

## Ensi viikolla
* Pistelaskujärjestelmän parantaminen
* Aikaisemmin tällä viikolla neljän suora ei toisinaan johtanut pelin loppumiseen.
Lauantaina korjauksen jälkeen ei ole tullut näitä tilanteita vastaan mutta asiaa pitää vielä tutkia.
* Vuoronvaihtoa testaavat kaksi testiä eivät mene yhteisajossa aina läpi. Erikseen toimivat aina.
* Tekoäly ei huomaa kaikkia pelaajan kolmen suoria.
