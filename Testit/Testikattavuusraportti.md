# Testikattavuusraportti

## Yksikkötestaus
Testauksessa on käytetty Pythonin unittest -työkalua.

## Mitä testattu ja miten
* Pelin alkaessa alarivin tulisi olla tyhjä ts. kaikissa soluissa on 0
* Vuoro vaihtuu pelaajalta tekoälylle
* Vuoro vaihtuu tekoälyltä pelaajalle
* Neljä pelaajan pelimerkkiä rivissä johtaa pelin loppumiseen
* Neljä molempien pelaajien pelimerkkiä samassa rivissä eivät lopeta peliä
* Neljä pelaajan merkkiä viistosti (molemmat suunnat) johtaa pelin loppumiseen
* Pelin alkaessa kaikkiin sarakkeisiin voi tiputtaa pelimerkkejä
* Kun sarake on täynnä pelimerkkejä, siihen ei voi enää tiputtaa uusia merkkejä.

## Testauksessa käytetyt syötteet
* Testauksessa luodaan aina uusi peli. Pelin alkutilannetta testaavissa testeissä merkkejä ei ole tiputettu. 
Muissa testeissä on sarakkeisiin tiputettu tarvittava määrä merkkejä ja testattu peliä tämän jälkeen.

## Testien toistettavuus

## Empiirisen testauksen visuaalinen/graafinen muoto
Raportti (23.9.) löytyy [täältä](https://github.com/aarekr/ConnectFour/blob/main/Testit/Testikattavuus_2023-09-23.JPG)
