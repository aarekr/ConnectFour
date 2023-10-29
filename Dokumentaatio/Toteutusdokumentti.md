# Toteutusdokumentti

## Ohjelman yleisrakenne
Pelin koodi on jaettu kolmeen tiedostoon: pelin aloittamisesta vastaavaan game.py, grafiikasta vastaavaan ui.py ja 
tekoälystä sekä Minimax -algoritmista vastaavaan ai.py. Peli alkaa game.py -tiedostosta, joka kutsuu ui.py:n who_starts 
-funktiota.
Pelin alkaessa luodaan kuuden rivin ja seitsemän sarakkeen pelipöytä (game board).
Pelin alussa pelaaja näkee tyhjän pelipöydän ja yläreunassa pyydetään valitsemaan pelin aloittajan tai lopetus.
Valinnan jälkeen peli-ikkunan yläreunassa oleva teksti ilmoittaa kumpi pelaajista tekee ensimmäisen siirron. 
Tämän jälkeen pelaajat tiputtavat 
vuorotellen pelimerkkejä sarakkeisiin ja tätä toimintoa ylläpidetään while -silmukassa (game_active:n arvo on True).
Pelaajan ollessa vuorossa, Pythonin pygame -moduulin toiminnoilla seurataan hiiren liikettä ja otetaan vastaan 
sarakevalinta (syöte) kun pelaaja klikkaa hiiren nappia. Tekoäly valitsee oman sarakkeensa käyttämällä Minimax -algoritmin 
ja pelin pistelaskujärjestelmän laskemaa optimaalista tulosta. Pelitilanne näkyy sekä peli-ikkunassa että konsoliin 
tulostettavassa matriisissa. Molempien pelaajien tapauksessa tarkistetaan, että valitussa sarakkeessa on vielä tilaa. 
Jokaisen siirron jälkeen tarkistetaan onko jompikumpi pelaajista voittanut tai kaikki pelimerkit käytetty. Jos peli 
loppuu, game_active muuttujan tila vaihdetaan True:sta False:ksi.
Pelin aikana pelikehikko tulostetaan konsoliin jokaisen siirron jälkeen. Tämän lisäksi tulostetaan pelin alkamiseen ja 
loppumiseen liittyvää tietoa. Tulostaminen konsoliin ei vaikuta pelin kulkuun vaan on tarkoitettu kehittäjän aputyökaluksi.
Koodissa pelaajaa merkataan arvolla 1 ja tekoälyä arvolla 2 vaikkakin ns. "magic number" -muttujia tulisi välttää.

## Pistelaskujärjestelmä
Pistelaskujärjestelmä laskee halutuille pelipositioille arvot, jotka kuvaavat positioiden hyvyyttä ja näitä arvoja verrataan 
keskenään parhaan siirron valitsemiseksi. Tarkasteltavana on kerrallaan aina neljä peräkkäistä paikkaa esim. alarivin (rivi 0)
sarakkeet 2,3,4,5. Pisteitä annetaan kahdessa tilanteessa: 1. pelaajalla on kolme pelimerkkiä ja yksi tyhjä paikka (50 pistettä) 
ja 2. pelaajalla on kaksi pelimerkkiä ja kaksi tyhjää paikkaa (20 pistettä). Muilla pelipositioilla on myös arvot mutta ne on 
jätetty pois, jotta laskenta olisi yksinkertaisempaa. Tekoälyn yllämainituista pelipositioista annetaan positiiviset arvot 
ja pelaajan positioista negatiiviset.

## Pelin heuristiikka
Minimax -algoritmi palauttaa arvon, joka ilmoittaa pelitilanteen hyvyyden tekoälyn kannalta. Kun tekoälyn pelipositio on parempi 
kuin vastustajan, on peliposition arvo positiivinen ja vastaavasti kun pelaajan pelipositio on parempi kuin tekoälyn, on 
peliposition arvo negatiivinen. Lisäksi on kaksi ääriarvoa, jotka kuvaavat toisen varmaa voittoa - tekoälyn varma voitto on 
ääretön (math.inf) ja pelaajan miinus ääretön (-math.inf). Heurististen arvojen paremmusjärjestys on math.inf, -math.inf ja väli
[pistelaskujärjestelmän antama korkein positiivinen arvo, ..., alhaisin negatiivinen arvo]. Tekoäly pyrkii toisin sanoen aina 
ensisijaisesti voittamaan (valitsemalla math.inf), toissijaisesti estämään häviön (valitsemalla -math.inf) ja mikäli 
edellä olevia tilanteita ei ole, maksimoimaan oman peliposition arvon (mahdollisimman korkea peliposition arvo). Esim. jos 
ollaan tilanteessa, jossa molemmilla on kolmen suora, tekoäly pyrkii voittamaan koska vastustajan blokkaaminen on 
toissijainen.

## Aikavaativuudet
Koodin (Minimaxin) aikavaativuus on O(s^n), missä s on siirtojen määrä (1-7) ja n on Minimaxille annettava puun syvyys (esim. 7).

## Puutteet ja parannusehdotukset
* Pistelaskujärjestelmään voi lisätä muiden pelipositioiden arvoja ottaen huomioon laskennan hidastuminen.
* Minimaxista on kutsuja muihin funktioiden, joiden käsittelyaikoja voi supistaa.
* Voittosuorien ja pelitilanteiden tarkistuksissa käydään toisinaan läpi tyhjiä rivejä ja/tai sarakkeita. Esim. jos pelimerkkejä 
on vain kahdessa reunasarakkeessa, toisen reunan sarakkeiden tarkistaminen ei ole kaikissa tilanteissa tarpeellinen.
* Minimaxin tehostamiselle on olemassa työkaluja, joilla läpikäyntiaikoja voidaan lyhentää.

## Laajat kielimallit
* Työssä ei ole käytetty laajoja kielimalleja.

## Lähteet
* Siddhi Sawant. Ask Python. Connect Four Game in Python. https://www.askpython.com/python/examples/connect-four-game
* Python crash course. Eric Matthes. No Starch Press (2019).
* Minimax. Wikipedia. https://en.wikipedia.org/wiki/Minimax
* Alpha–beta pruning. Wikipedia. https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning
* Heuristic (computer science). Wikipedia. https://en.wikipedia.org/wiki/Heuristic_(computer_science)
* Keith Galli. GitHub. https://github.com/KeithGalli/Connect4-Python/blob/master/connect4_with_ai.py
* Jonathan DeLeon. GitHub. https://github.com/JonathanDeLeon/connect-four-ai
* Python.org. Unit testing framework. https://docs.python.org/3/library/unittest.html
* Anthony Shaw. Getting Started With Testing in Python. Real Python. https://realpython.com/python-testing/
* pytest-cov 4.1.0. pypi.org. https://pypi.org/project/pytest-cov/
* Pylint 2.17.5. pypi.org. https://pypi.org/project/pylint/
* PEP 257 – Docstring Conventions. python.org. https://peps.python.org/pep-0257/
* Coverage.py. https://coverage.readthedocs.io/en/7.3.1/
* Muhammed Ali. Code coverage vs. test coverage in Python. Honeybadger. https://www.honeybadger.io/blog/code-test-coverage-python/
* numpy.zeros. Numpy.org. https://numpy.org/doc/stable/reference/generated/numpy.zeros.html
* Defining Main Functions in Python. RealPython. https://realpython.com/python-main-function/
* Ofer Dekel. Python Performance Testing: Quick Tutorial and Best Practices. granulate.io. (Luettu 7.10.2023) https://granulate.io/blog/python-performance-testing-quick-tutorial-and-best-practices/
* Eric Goebelbecker. blog.sentry.io. (Luettu 7.10.2023) https://blog.sentry.io/python-performance-testing-a-comprehensive-guide/
* Importing files from different folder. stackoverflow.com.  https://stackoverflow.com/questions/4383571/importing-files-from-different-folder
* connect4.gamesolver.org. https://connect4.gamesolver.org
