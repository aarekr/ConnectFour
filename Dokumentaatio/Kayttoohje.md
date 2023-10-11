# Käyttöohje

## Pelin asentaminen
* Asenna pygame -moduuli: pip install pygame
* Asenna numpy -moduuli: pip install numpy

## Komennot
* Aloita peli: python3 game.py
* Pylint -testit: python3 -m pylint ui.py
* Yksikkötestit: python3 -m unittest -v unittests.py
* Kattavuustestit: python3 -m coverage run -m pytest unittests.py
* Kattavuustestien raportti konsolissa: python3 -m coverage report -m
* Kattavuustestien raportti html: python3 -m coverage html
* Suorituskykytestaus: python3 performance_tests.py

## Komennot taulukkoformaatissa

| Toiminto                             | Komento                 |
|--------------------------------------|-------------------------|
| Aloita peli                          | python3 game.py         |
| Pylint -testit                       | python3 -m pylint ui.py |
| Yksikkötestit                        | python3 -m unittest -v unittests.py |
| Kattavuustestit                      | python3 -m coverage run -m pytest unittests.py |
| Kattavuustestien raportti konsolissa | python3 -m coverage report -m | 
| Kattavuustestien raportti html       | python3 -m coverage html      |
| Suorituskykytestaus                  | python3 performance_tests.py  |
