# Promethee II Algorithm - Python
Final project for Programming Languages (Academic subject)

#POLISH VERSION\n
Przed uruchomieniem programu upewnij się, że pobrałeś wersję odpowiednią dla twojego język.
Plik wykorzystywany do programu powinien być wykonany według poniższego szablonu:

#ATRYBUT nr_atrybutu; nazwa_atrybutu; waga; typ; typ_funkcji_preferencji; parametry_funkcji
#ROZWIĄZANIE nazwa_rozwiazania
wartosc_pierwszego_atrubutu; wartość_drugiego atrybutu; ...; wartosc_n-tego_atryvutu
#END

OZNACZENIA:
nr_atrybutu - wartości całkowite od 1 do n gdzie n jest liczbą atrybutów
nazwa - nazwa atrybutu - łańcuch znaków
waga - liczba rzeczywista, wartość atrybutu określa jego ważność, przedział (0, 1>
typ - znak K lub Z, gdzie K - charakter kosztowy to znaczy im większa wartość atrybutu tym gorzej, Z - charakter korzyści czyli im większa wartość tym lepiej
typ_funkcji_preferencji - liczba całkowita ze zbioru {1, 2, 3, 4, 5} oznaczająca formę funkcji preferencji (zdjęcia poniżej)
parametry_funkcji - dwie liczby rzeczywiste oddzielone spacją określające wartości parametrów q i p (odpowiednio próg równoważności i silnej preferencji - zdjęcia poniżej). Jeżeli dany parametr nie dotyczy danej formy funkcji preferencji to w jego miejscu należy wpisać wartość 0 i parametr ten jest ignorowany.

Funkcje preferencji i zasada ich działania (zdjęcia z prezentacji otrzymanej od dr hab. inż. Maciej Tabaszewski):
![image](https://user-images.githubusercontent.com/34101300/173627518-0bf9d003-e4fa-42c7-87cb-52fb72e51943.png)
![image](https://user-images.githubusercontent.com/34101300/173627775-1a185cb3-ad6b-4023-847d-b67b98d41872.png)
![image](https://user-images.githubusercontent.com/34101300/173627802-aea11634-6917-4293-831a-f9e816cb70da.png)


Przykładowa zawartość pliku (text.txt):
#ATRYBUT  1; koszt; 0.5; K; 1; 0 0
#ATRYBUT  2; wydajność; 0.3; Z; 2; 10.0 0  
#ATRYBUT  4; termin dostawy; 0.1; K; 3; 0 12.0
#ATRYBUT  5; ocena jakości serwisu; 0.05; Z; 4; 10.0 15.0
#ATRYBUT  3; ocena elastyczności; 0.05; Z; 5; 8 10.0
#ROZWIĄZANIE	Frezarka FFMOT 102 
130.0; 50.0; 3.0; 25; 4.0
#ROZWIĄZANIE	Frezarka FFMOT 106 
150.0; 60.0; 4.0; 40; 4.0
#ROZWIĄZANIE	Frezarka K56 
120.0; 45.0; 5.0; 20; 1.0
#ROZWIĄZANIE	Frezarka M04 
145.0; 55.0; 2.0; 30; 5.0
#END

Rozwiązanie dla pliku text.txt
![image](https://user-images.githubusercontent.com/34101300/173623873-914198b4-4c32-472d-8c6d-45ac7271d654.png)


#ENGLISH VERSION
SOON....


