# Käyttöohje

## Pelin asentaminen

| Toiminto                             | Komento                 |
|--------------------------------------|-------------------------|
| Asenna pygame -moduuli               | pip install pygame      |
| Asenna numpy -moduuli                | pip install numpy       |

## Komennot

| Toiminto                             | Komento                 |
|--------------------------------------|-------------------------|
| Aloita peli                          | python3 game.py         |
| Pylint -testit ui.py                 | python3 -m pylint ui.py |
| Pylint -testit helper_functions.py   | python3 -m pylint helper_functions.py |
| Yksikkötestit                        | python3 -m unittest -v unittests.py   |
| Kattavuustestit                      | python3 -m coverage run -m pytest unittests.py |
| Kattavuustestien raportti konsolissa | python3 -m coverage report -m | 
| Kattavuustestien raportti html       | python3 -m coverage html      |
| Suorituskykytestaus                  | python3 performance_tests.py  |
