# Testaus
## Automaattiset testit
![image](https://github.com/Joacim-S/TiraLabra/assets/45919018/f8555225-8a18-4546-9ae6-86497bdee895)
Ohjelman yksikkötestit on tehty pythonin unittest kirjastolla, ja testien ajoon on luotu task moduulilla tehtävä.
Käyttöliittymää, index tiedostoa, eikä käyttäjän tekemiä komentoja käsittelevää commands moduulia testata.
Muiden moduulien helposti yksittäin testattavat funktiot on testattu täysin muista erillään syötteillä, joilla saadaan kaikki haarat katettua.
Itse pakkaus- ja purkufunktioita ei testata erikseen. Testissä ensin pakataan syöte, ja sitten puretaan se, ja tarkistetaan, saatiinko alkuperäistä vastaava tulos.
Huffmanin koodauksen puun uudelleenrakennustakaan ei testata erikseen.
## Manuaalinen testaus
Pakkaustehoa testattiin ajamalla sovelluksen käyttöliittymän kautta komento "compress_stats" input kansion koostuessa [Toteutusdokumentin](https://github.com/Joacim-S/TiraLabra/blob/main/dokumentaatio/toteutusdokumentti.md) kaaviossa listatuista tiedostoista.
Kaikki tiedostot ovat kirjoja jotka on ladattu [Project Gutenberg](https://www.gutenberg.org/) kirjastosta.
Kirjat löytää tämän muotoisella osoitteella: https://www.gutenberg.org/ebooks/1.txt.utf-8
Numeron paikalle vain sijoitetaan tiedostonimestä löytyvä numero. Poikkeuksena tiedosto [Frankenstein](https://www.gutenberg.org/cache/epub/84/pg84.txt)
Mukaan on otettu muutama id järjestyksessä, ja loput on valittu pääosin länttäämällä sormet numpadille.
Kuten jo mainittu, empiirisen testauksen tulokset löytyvät toteutusdokumentista. Itse testitekstejä en repoon laittanut, koska koin tarpeettomaksi videä githubista tilaa ilmaiseksi tarjolla olevilla tiedostoilla.
unittestit voi ajaa komennolla poetry run invoke test.
