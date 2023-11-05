# Toteutusdokumentti
## Ohjelman yleisrakenne
Varsinainen ohjelma koostuu kuudesta moduulista. [index](https://github.com/Joacim-S/TiraLabra/blob/main/src/index.py) käynnistää ohjelman pääloopin, joka löytyy [ui](https://github.com/Joacim-S/TiraLabra/blob/main/src/ui.py) moduulista.

Ui moduuli välittää käyttäjän antamat komennot [commands](https://github.com/Joacim-S/TiraLabra/blob/main/src/commands.py) moduulille, joka käsittelee komennot.

Commands moduuli lukee ja kirjoittaa tiedostot, sekä kutsuu pakkausalgoritmeja.

Pakkausalgoritmeilla on omat moduulinsa: [lz78](https://github.com/Joacim-S/TiraLabra/blob/main/src/lz78.py) ja [huffman](https://github.com/Joacim-S/TiraLabra/blob/main/src/huffman.py). Algoritmit ovat moduuleissaan luokkina. Huffman moduulista löytyy myös Node luokka puita varten.
Pakkausalgoritmit käyttävät [tools](https://github.com/Joacim-S/TiraLabra/blob/main/src/tools.py) moduulia, josta löytyy molempien algoritmien tarvitsemat funktiot.

Tekstitiedostot luetaan input kansiosta, ja pakatut sekä puretut tiedostot tallennetaan output kansioon.

## Suorituskyky
Kummmallakin algoritmilla päästiin halutun 50% pakkaussuhteen tienoille, kun syötteet ovat tarpeeksi pitkiä. Liian lyhyt syöte johtaa huonoimmillaan alkuperäistä suurempaan tiedostokokoon.
![image](https://github.com/Joacim-S/TiraLabra/assets/45919018/561ea9e3-0d55-4e19-9dcd-8773b130d3ec)
Taulukossa tekstitiedostoja, niiden alkuperäiset koot ja saavutetut pakkaussuhteet kummallakin algoritmilla, sekä tieto, pakkasiko LZ78 paremmin. [Täällä ohjelman tuottama csv tiedosto](https://github.com/Joacim-S/TiraLabra/blob/main/src/output/stats/stats_0.csv). Data on kuvassa järjestetty nousevasti tiedostokoon mukaan, jotta tulee esiin havaittu trendi. 
Huffmanin koodaus on yleensä tehokkaampi lyhyemmmillä syötteillä, kun taas LZ78 vie selkeästi voiton pidemmillä syötteillä, mikä selittyy hyvin algoritmien toimintaperiaatteilla. Huffmanin koodauksessa pakkausteho perustuu yksittäisten merkkien koodaamiseen optimaalisesti. 
Tämä on tehokas tapa pakata melko lyhyttäkin tekstiä, kunhan Huffman puu on tarpeeksi pieni tekstiin verrattuna. Lempel Ziv algoritmit taas perustuvat siihen, että aiemmin nähtyyn osamerkkijonoon voidaaan viitata indeksillä.
Tekstin pituuden kasvaessa todennäköisyys löytää pidempiä jo nähtyjä osamerkkijonoja kasvaa, mutta merkkien suhteellinen esiintymismäärä ei välttämättä juuri muutu. Siksi LZ78:n pakkausteho nousee syötteen pituuden myötä selvästi enemmän kuin Huffmanin koodauksen.
Kaaviossa on 3 erikoista datapistettä. 69.txt, 3210.txt ja 10.txt. 69.txt sisältää 32. Mersennen alkuluvun. Se on siis pitkä jono numeroita, joiden toisteisuus on vähäistä. LZ78 ei siis suoriudu pakkauksesta yhtä hyvin kuin yleensä. 
Huffmanin koodaus taas suoriutuu poikkeuksellisen hyvin, kun merkistö on pieni. 3210.txt pakkautuu molemmilla algoritmeilla hyvin, koska kyseessä on sanakirja, joka sisältää hyvin paljon välilyöntejä. Eli tiedostossa on paljon yhtä merkkiä monta kertaa peräkkäin, joten kumpikin agoritmi loistaa.
10.txt on Raamattu, jossa jokaisen jakeen edessä on kirjan lyhenne ja jakeen numero. Osamerkkijonojen toisteisuutta on siis poikkeuksellisen paljon, joten LZ78:n ja Huffmanin koodauksen ero on poikkeuksellisen suuri.

## Puutteet ja mahdolliset parannukset
Tiedostojen käsittelyn olisi voinut eriyttää omaaan moduuliin. Tämä olisi erityisesti helpottanut commnands moduulin testausta, jonka nyt jätin tekemättä. Useamman tiedoston pakkauksesta tai putkamisesta voisi tehdä monin kerroin nopeampaa, jos tiedostoille olisi omat säikeet. Ohjelman käytön kannalta olisi kätevää valita itse, minne tiedostot tallennetaan ja mistä ne luetaan.
Nyt tiedostopolut on kovakoodattu.

## Laajojen kielimallien käyttö
En käyttänyt laajoja kielimalleja lainkaaan.

## Lähteet
* https://fi.wikipedia.org/wiki/Huffmanin_koodaus
* https://en.wikipedia.org/wiki/Huffman_coding
* https://en.wikipedia.org/wiki/LZ77_and_LZ78
* https://math.mit.edu/~goemans/18310S15/lempel-ziv-notes.pdf
