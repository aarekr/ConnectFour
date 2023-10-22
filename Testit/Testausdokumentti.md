# Testausdokumentti

## Yksikkötestaus
Testauksessa on käytetty Pythonin unittest -työkalua.

## Mitä testattu ja miten
* Pelin alussa oikeanmuotoinen (6*7) pelimatriisi muodostuu
* Pelin alussa alarivin tulisi olla tyhjä ts. kaikissa soluissa on 0
* Pelin alussa pelaajalle ilmoitetaan kumpi aloittaa
* Pelin alussa kaikkien sarakkeiden tulisi olla pelattavissa
* Jokaisen siirron jälkeen, konsoliin tulisi tulostua pelimatriisi
* Neljä pelaajan peräkkäistä pelimerkkiä rivissä johtaa pelin loppumiseen
* Neljä pelaajan peräkkäistä pelimerkkiä sarakkeessa johtaa pelin loppumiseen
* Neljä pelaajan merkkiä viistosti (molemmat suunnat) johtaa pelin loppumiseen
* Neljä molempien pelaajien pelimerkkiä samassa rivissä eivät lopeta peliä
* Vuoro vaihtuu pelaajalta tekoälylle
* Vuoro vaihtuu tekoälyltä pelaajalle
* Rivi 4 on vapaa kun sarakkeeseen on tiputettu 3 pelimerkkiä
* Kun sarake on täynnä pelimerkkejä, siihen ei voi enää tiputtaa uusia merkkejä
* Kun sarake on täynnä pelimerkkejä, sarake ei ole vapaiden sarakkeiden listalla
* Kun rivi 0 on täynnä, kaikki sarakkeet ovat edelleen pelattavissa
* Kun pelaajalla on neljän pelimerkin suora, kyseessä on terminal node
* Kun tekoälyllä on neljän pelimerkin suora, kyseessä on terminal node
* Kun molemman pelaajan merkkejä on 4 peräkkäin, kyseessä ei ole terminal node
* Minimax: kun päätöspuun syvyys on 0, minimax palauttaa peliposition arvon
* Minimax: kun ihminen voittaa (terminal node), minimax palauttaa heuristisen arvon
* Minimax: kun tekoäly voittaa (terminal node), minimax palauttaa heuristisen arvon
* Tekoälyn kolmen ja kahden pelimerkin suorat saavat pelipositioina arvot
* Ihmispelaajan kolmen ja kahden merkin suorat huonontavat tekoälyn peliposition arvoa
* Tekoäly pyrkii laittamaan pelimerkkejä keskimmäisiin sarakkeisiin
* Tekoäly voittaa yhdellä siirrolla kun sillä on 3 peräkkäistä merkkiä sarakkeessa ja 1 tyhjä
* Tekoäly voittaa yhdellä siirrolla kun sillä on 3 peräkkäistä merkkiä rivissä ja 1 tyhjä
* Testataan pelin lopussa, että pelaajan voitto ilmoitetaan konsolissa
* Testataan pelin lopussa, että tekoälyn voitto ilmoitetaan konsolissa

## Testauksessa käytetyt syötteet
* Testauksessa luodaan aina uusi peli. Pelin alkutilannetta testaavissa testeissä merkkejä ei ole tiputettu. 
Muissa testeissä on sarakkeisiin tiputettu tarvittava määrä merkkejä ja testattu peliä tämän jälkeen.

## Testien toistettavuus

## Empiirisen testauksen visuaalinen/graafinen muoto
* Raportti (23.9.) löytyy [täältä](https://github.com/aarekr/ConnectFour/blob/main/Testit/Testikattavuus_2023-09-23.JPG)
* Raportti (30.9.) löytyy [täältä](https://github.com/aarekr/ConnectFour/blob/main/Testit/Testikattavuus_2023-09-30.JPG)
* Raportti (7.10.) löytyy [täältä](https://github.com/aarekr/ConnectFour/blob/main/Testit/Testikattavuus_2023-10-07.JPG)
* Raportti (14.10.) löytyy [täältä](https://github.com/aarekr/ConnectFour/blob/main/Testit/Testikattavuus_2023-10-14.JPG)
* Raportti (22.10.) löytyy [täältä](https://github.com/aarekr/ConnectFour/blob/main/Testit/Testikattavuus_2023-10-22.JPG)
