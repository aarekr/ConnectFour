# Toteutusdokumentti

## Ohjelman yleisrakenne
Pelin alkaessa luodaan kuuden rivin ja seitsemän sarakkeen pelipöytä (game board). Alussa pelaaja näkee tyhjän pelipöydän ja 
samalla yläreunassa oleva teksti ilmoittaa kumpi pelaajista tekee ensimmäisen siirron. Tämän jälkeen pelaajat tiputtavat 
vuorotellen pelimerkkejä sarakkeisiin ja tätä toimintoa ylläpidetään while -silmukassa (game_active:n arvo on True).
Pelaajan ollessa vuorossa, Pythonin pygame -moduulin toiminnoilla seurataan hiiren liikettä ja otetaan vastaan 
sarakevalinta (syöte) kun pelaaja klikkaa hiiren nappia. Tekoäly valitsee oman sarakkeen käyttämällä Minimax -algoritmin 
ja pelin pistelaskujärjestelmän laskemaa optimaalista tulosta. Pelitilanne näkyy sekä peli-ikkunassa että konsoliin 
tulostettavassa matriisissa. Molempien pelaajien tapauksessa tarkistetaan, että valitussa sarakkeessa on vielä tilaa. 
Jokaisen siirron jälkeen tarkistetaan onko jompikumpi pelaajista voittanut tai kaikki pelimerkit käytetty. Jos peli 
loppuu, game_active muuttujan tila vaihdetaan True:sta False:ksi.

## Aikavaativuudet
Koodin aikavaativuudeltaan suurimmat osat ovat kaksi sisäkkäistä for-silmukkaa, joten O(n^2). 
Käsiteltävä tietomäärä on kuitenkin pieni - 6 toisessa silmukassa ja 7 toisessa eli n*m = 42.

## Puutteet ja parannusehdotukset
* Pistelaskujärjestelmä ei toimi kuten pitäisi ja tämä johtaa toisinaan väärään sarakevalintaan - 
tekoäly ei osaa blokata joitakin pelaajan kolmen pelimerkin suoria.

## Laajat kielimallit
* Työssä ei ole käytetty laajoja kielimalleja.

## Lähteet
* Siddhi Sawant. Ask Python. Connect Four Game in Python. https://www.askpython.com/python/examples/connect-four-game
* Minimax. Wikipedia. https://en.wikipedia.org/wiki/Minimax
* Alpha–beta pruning. Wikipedia. https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning
* Heuristic (computer science). Wikipedia. https://en.wikipedia.org/wiki/Heuristic_(computer_science)
* Python.org. Unit testing framework. https://docs.python.org/3/library/unittest.html
* Anthony Shaw. Getting Started With Testing in Python. Real Python. https://realpython.com/python-testing/
* Pylint 2.17.5. pypi.org. https://pypi.org/project/pylint/
* PEP 257 – Docstring Conventions. python.org. https://peps.python.org/pep-0257/
* Coverage.py. https://coverage.readthedocs.io/en/7.3.1/
* Muhammed Ali. Code coverage vs. test coverage in Python. Honeybadger. https://www.honeybadger.io/blog/code-test-coverage-python/
* numpy.zeros. Numpy.org. https://numpy.org/doc/stable/reference/generated/numpy.zeros.html
* Defining Main Functions in Python. RealPython. https://realpython.com/python-main-function/
* Ofer Dekel. Python Performance Testing: Quick Tutorial and Best Practices. granulate.io. (Luettu 7.10.2023) https://granulate.io/blog/python-performance-testing-quick-tutorial-and-best-practices/
* Eric Goebelbecker. blog.sentry.io. (Luettu 7.10.2023) https://blog.sentry.io/python-performance-testing-a-comprehensive-guide/
* Importing files from different folder. stackoverflow.com.  https://stackoverflow.com/questions/4383571/importing-files-from-different-folder
