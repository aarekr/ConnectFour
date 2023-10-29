# Testausdokumentti

## Yksikkötestaus
* Testauksessa on käytetty Pythonin unittest -työkalua. Testejä yhteensä 68 kpl.

## Testauksessa käytetyt syötteet
* Testauksessa luodaan aina uusi peli. Pelin alkutilannetta testaavissa testeissä pelimerkkejä ei ole tiputettu. 
Muissa testeissä on sarakkeisiin tiputetaan tarvittava määrä pelimerkkejä ja testataan peliä tämän jälkeen.
* Minimaxin syvyyden 3, 5 ja 7 testien kirjoittamisessa käytetty apuna https://connect4.gamesolver.org -sivua.

## Mitä testattu ja miten
#### Pelin aloittamiseen liittyvät perustoiminnot (TestGameStart)
* Pelin alussa muodostetaan oikeanmuotoinen (6*7) pelimatriisi
* Pelin alussa alarivin tulisi olla tyhjä ts. merkkejä ei ole tiputettu
* Pelin alussa kaikkien sarakkeiden tulisi olla pelattavissa
* Tarkistetaan, että pelilaudan konsoliin tulostava funktio olemassa
* Tarkistetaan, että pelilaudan peli-ikkunaan tulostava funktio olemassa
* Pelin alussa pelaajalle ilmoitetaan, että hän aloittaa
* Pelin alussa pelaajalle ilmoitetaan, että tekoäly aloittaa

#### Neljän peräkkäisen pelimerkin suora käsitellään oikein (TestFourInRow)
* Neljä pelaajan/tekoälyn peräkkäistä pelimerkkiä rivissä johtaa pelin loppumiseen
* Neljä pelaajan/tekoälyn peräkkäistä pelimerkkiä sarakkeessa johtaa pelin loppumiseen
* Neljä pelaajan/tekoälyn peräkkäistä merkkiä viistosti ylöspäin johtaa pelin loppumiseen
* Neljä pelaajan/tekoälyn peräkkäistä merkkiä viistosti alaspäin johtaa pelin loppumiseen
* Neljä molempien pelaajien peräkkäistä pelimerkkiä samassa rivissä eivät lopeta peliä

#### Vuoron vaihtuminen ja arpominen (TestTurnChanges)
* Vuoro vaihtuu pelaajalta tekoälylle kun pelimerkki tiputettu
* Vuoro vaihtuu tekoälyltä pelaajalle kun pelimerkki tiputettu
* Pelin aloittajaksi arvotaan joko pelaaja tai tekoäly

#### Pelimerkkien määrä pelikehikossa on oikea (TestChipCount)
* Pelin alussa pelimerkkien määrä pelikehikossa on 0
* Pelimerkkien määrä on 4 kun molemmat pelaajat ovat tiputtaneet 2
* Pelimerkkien määrä on 7 kun pelaajat ovat tiputtaneet 3 ja 4
* Pelimerkkien määrä on 42 kun kaikki pelimerkit on tiputettu

#### Alin vapaa (ts. pelattavissa oleva) rivi sarakkeessa on oikein (TestFreeRows)
* Rivi 1 on vapaa, jos sarakkeeseen ei ole tiputettu pelimerkkejä
* Rivi 4 on vapaa kun sarakkeessa on 3 pelimerkkiä
* Sarakkeessa ei ole vapaita rivejä, jos 6 pelimerkkiä tiputettu

#### Vapaat sarakkeet ilmoitetaan oikein (TestFreeColumns)
* Kun sarake on täynnä pelimerkkejä, siihen ei voi enää tiputtaa uusia merkkejä
* Kun kaikki 42 pelimerkkiä on tiputettu, vapaita sarakkeita ei enää ole
* Kun rivi 1 on täynnä, kaikki sarakkeet ovat edelleen pelattavissa

#### Uusien siirtojen mahdollisuus ja pelin loppuminen (TestTerminalNode)
* Kun kaikki 42 pelimerkkiä on tiputettu, peli on loppunut
* Kun pelaajalla on neljän pelimerkin suora, peli on loppunut
* Kun tekoälyllä on neljän pelimerkin suora, peli on loppunut
* Kun molemmat pelaajat ovat tiputtaneet 4 pelimerkkiä eikä kummallakaan suoraa, peli jatkuu
* Kun molemman pelaajan merkkejä on 4 peräkkäin, peli jatkuu

#### Minimax -algoritmin perustoiminnot (TestMinimaxBasicFunctionalities)
* Kun päätöspuun syvyys on 0 ja pelimerkkejä ei tiputettu, Minimax palauttaa peliposition arvon 0
* Kun pelaaja voittaa tarkasteltavassa pelitilanteessa, Minimax palauttaa heuristisen arvon miinus ääretön
* Kun tekoäly voittaa tarkasteltavassa pelitilanteessa, Minimax palauttaa heuristisen arvon ääretön
* Sarakkeiden käsittelyjärjestys on optimaalinen (keskeltä reunoihin) kun kaikki sarakkeet ovat vapaita
* Optimaalisesta sarakkeiden käsittelyjärjestyksestä puuttuvat 2 täynnä olevaa saraketta
* Sarakkeita ei käsitellä kun kaikki sarakkeet ovat täynnä

#### Minimax -algoritmin yhden siirron pelistrategian testaaminen (syvyys 1) (TestMinimaxStrategiesDepthOne)
* Kun sarakkeessa on 3 tekoälyn merkkiä peräkkäin ja yksi tyhjä, tekoäly voittaa yhdellä siirrolla
* Kun rivissä on 3 tekoälyn merkkiä peräkkäin ja yksi tyhjä, tekoäly voittaa yhdellä siirrolla

#### Minimax -algoritmin kahden siirron pelistrategian testaaminen (syvyys 3) (TestMinimaxStrategiesDepthThree)
* Tilanteessa 0002200 (rivi 1), tekoäly tiputtaa pelimerkin sarakkeeseen 3 ja voittaa seuraavalla siirrolla
* Tilanteessa 0011000 (rivi 1), tekoäly tiputtaa pelimerkin sarakkeeseen 5 ja estää pelaajan varman voiton
* Minimax rakentaa risteävät diagonaalit ja voittaa varmasti seuraavalla siirrolla
* Tilanteessa 1011000 (rivi 1), tekoäly blokkaa (2), pelaaja (5) ja tekoäly blokkaa (6)

#### Minimax -algoritmin kolmen siirron pelistrategioita (syvyys 5) (TestMinimaxStrategiesDepthFive)
* Pelitilanteet ovat monimutkaisempia ja esitelty testitiedostossa. Testejä on 5 kpl.

#### Minimax -algoritmin neljän siirron pelistrategioita (syvyys 7) (TestMinimaxStrategiesDepthSeven)
* Pelitilanteet ovat monimutkaisempia ja esitelty testitiedostossa. Testejä on 5 kpl.

#### Tekoälyn peliposition arvon testaaminen (TestAIPositionValue)
* Pelitilanne 3 rivissä 2220 antaa tekoälylle pistemäärän 50
* Pelitilanne 3 rivissä 2221 antaa tekoälylle pistemäärän 0
* Pelitilanteet 0220 ja 2020 antavat molemmat tekoälylle pistemäärän 20
* Pelitilanne 1220 antaa tekoälylle pistemäärän 0
* Pelitilanne 0020 antaa tekoälylle pistemäärän 0

#### Pelaajan peliposition arvon testaaminen (TestHumanPositionValue)
* Pelitilanne 1110 antaa tekoälylle pistemäärän -50
* Pelitilanne 1112 antaa tekoälylle pistemäärän 0
* Pelitilanteet 0110 ja 1010 antavat molemmat tekoälylle pistemäärän -20
* Pelitilanne 2110 antaa tekoälylle pistemäärän 0
* Pelitilanne 0010 antaa tekoälylle pistemäärän 0

#### Pelin loppu konsolissa ja peli-ikkunassa (TestGameEnd)
* Pelin lopussa konsolissa ilmoitetaan tasapeli
* Pelin lopussa konsolissa ilmoitetaan pelaajan voitto
* Pelin lopussa konsolissa ilmoitetaan tekoälyn voitto
* Pelin lopussa peli-ikkunassa ilmoitetaan tasapeli
* Pelin lopussa peli-ikkunassa ilmoitetaan pelaajan voitto
* Pelin lopussa peli-ikkunassa ilmoitetaan tekoälyn voitto

## Testausraportit
* Raportti (23.9.) löytyy [täältä](https://github.com/aarekr/ConnectFour/blob/main/Testit/Testikattavuus_2023-09-23.JPG)
* Raportti (30.9.) löytyy [täältä](https://github.com/aarekr/ConnectFour/blob/main/Testit/Testikattavuus_2023-09-30.JPG)
* Raportti (7.10.) löytyy [täältä](https://github.com/aarekr/ConnectFour/blob/main/Testit/Testikattavuus_2023-10-07.JPG)
* Raportti (14.10.) löytyy [täältä](https://github.com/aarekr/ConnectFour/blob/main/Testit/Testikattavuus_2023-10-14.JPG)
* Raportti (22.10.) löytyy [täältä](https://github.com/aarekr/ConnectFour/blob/main/Testit/Testikattavuus_2023-10-22.JPG)
* Raportti (26.10.) löytyy [täältä](https://github.com/aarekr/ConnectFour/blob/main/Testit/Testikattavuus_2023-10-26.JPG)
* Raportti (29.10.) löytyy [täältä](https://github.com/aarekr/ConnectFour/blob/main/Testit/Testikattavuus_2023-10-29.JPG)
