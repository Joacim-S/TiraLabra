# Käyttöohje
## Asennus
* Kloonaa repo
* Asenna riippuvuuden komennolla:
```bash
poetry install
```
## Käyttö
* Käynnistä sovellus komennolla:
```bash
poetry run invoke start
```
* testit ajetaan komennolla:
```bash
poetry run invoke test
```
* Coverage raportin saa komennolla:
```bash
poetry run invoke coverage-report
```
* Laita src/input kansioon .txt tiedostot, jotka haluat pakata
* Sovelluksen luomat tiedostot tallentuvat src/output kansioon.
* Itse sovelluksen käytössä UI ohjeistaa.
* compress_stats komennon luoma stats tiedosto löytyy kansiosta src/output/stats, jossa on valmiina testidatasta luotu tilasto.
* Ohjelma toimii utf-8 koodatuilla txt tiedostoilla.
