# Käyttöohje

## Pelaaminen
Käynnistä peli konsolissa komennolla python3 game.py
Pelinäytössä voi pelin alussa valita kumpi aloittaa. Vaihtoehtoina ovat R = aloittaja arvotaan, 
Y = sinä aloitat, A = tietokone aloittaa. Jos haluat lopettaa pelin, valitse E.
Tiputa pelimerkkejä sarakkeisiin ja pyri luomaan neljän peräkkäisen pelimerkin suora joko 
vaakasuunnassa, pystysuunnassa tai vinoittain. Pyri samalla estämään vastustajaa saamasta neljä 
pelimerkkiä peräkkäin. Ensimmäiseksi neljän suoran saanut voittaa pelin. Jos kaikki 42 
pelimerkkiä on tiputettu eikä kumpikaan voita, on peli päättynyt tasapeliin. Pelin loppuessa, 
voita pelata uudestaan tai lopettaa pelaamisen.

## Pelin asentaminen

| Toiminto                             | Komento                 |
|--------------------------------------|-------------------------|
| Asenna pygame -moduuli               | pip install pygame      |
| Asenna numpy -moduuli                | pip install numpy       |

## Komennot

| Toiminto                             | Komento                 |
|--------------------------------------|-------------------------|
| Aloita peli                          | python3 game.py         |
| Pylint score ai.py                   | python3 -m pylint ai.py |
| Yksikkötestit                        | python3 -m unittest -v unittests.py   |
| Kattavuustestit                      | python3 -m coverage run -m pytest unittests.py |
| Kattavuustestien raportti konsolissa | python3 -m coverage report -m | 
| Kattavuustestien raportti html       | python3 -m coverage html      |
| Suorituskykytestaus                  | python3 performance_tests.py  |
