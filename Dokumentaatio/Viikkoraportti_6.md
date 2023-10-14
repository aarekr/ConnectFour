# Viikko 6

## Mitä tehty viikolla
* Käyttöliittymällä on nyt vihdoinkin oma luokka. Pylint -tulos romahti ja vaati koodiin melkoisesti muutoksia.
* 12 apufunktiota siirretty erilliseen moduuliin (helper_functions.py) ja tämä importoidaan ui.py:ssä
* 7 muuttujaa siirretty käyttöliittymän ulkopuolelle
* 2 testiä testaavat nyt osaako Minimax täyttää neljännen pelimerkin kun 3 jo sarakkeessa / rivissä
* Apufunktioiden siirtäminen ui.py:stä helper_functions -moduuliin alentaa pylint ratingia
* Zoom-tapaaminen ohjaajan kanssa
* Minimaxin syvyysvirhe korjattu
* Sarakkeiden läpikäyntijärjestys muutettu optimaaliseksi ts. aloitetaan keskeltä ja edetään reunoihin
* Testit siirretty Testit-hakemistoon
* Käyttöliittymä ja Tekoäly-luokat ja niihin liittyvät toiminnot erotettu tiedostoihin ui.py ja ai.py
* Pylint ai.py on 9.86/10
* ai.py:n testikattavuus on 100% mutta lisää Minimaxin peliälyä testaavia testejä tarvitaan

## Ohjelman edistyminen
* Käyttöliittymä erotettu main -funktiosta
* Apufunktiot siirretty pois Käyttöliittymä-luokasta
* Lisää muuttujia siirretty käyttöliittymästä ulos
* Testejä kirjoitettu lisää, nyt 40
* Luotu Tekoäly-luokka ja tekoälytoiminnallisuudet erotettu Käyttöliittymä-luokasta. Tiedosto helper_functions.py poistettu.

## Mitä opittu
* 

## Epäselvät asiat / vaikeudet
* 

## Ensi viikolla
* Pitäisi lukea pelin strategioista
* Kirjoittaa Minimaxille lisää pelistrategiatestejä
* Optimoida pistelaskujärjestelmää pelistrategiatestien perusteella
