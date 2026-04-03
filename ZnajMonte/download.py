import os
import urllib.request
import urllib.parse
import time

# Lista zdjęć (Nazwa pliku docelowego, URL z Wikipedii bez kodowania)
zdjecia = [
    # Polscy dowódcy i oficerowie
    ("Wladyslaw_Anders.jpg", "https://commons.wikimedia.org/wiki/Special:FilePath/Władysław_Anders_1.jpg"),
    ("Kazimierz_Sosnkowski.jpg", "https://commons.wikimedia.org/wiki/Special:FilePath/Kazimierz_Sosnkowski_1940.jpg"),
    ("Bronislaw_Duch.jpg", "https://commons.wikimedia.org/wiki/Special:FilePath/Bolesław_Bronisław_Duch.jpg"),
    ("Nikodem_Sulik.jpg", "https://commons.wikimedia.org/wiki/Special:FilePath/Nikodem_Sulik.jpg"),
    ("Bronislaw_Rakowski.jpg", "https://commons.wikimedia.org/wiki/Special:FilePath/Bronisław_Rakowski.jpg"),
    ("Klemens_Rudnicki.jpg", "https://commons.wikimedia.org/wiki/Special:FilePath/Klemens_Rudnicki.jpg"),
    ("Wladyslaw_Smrokowski.jpg", "https://commons.wikimedia.org/wiki/Special:FilePath/Władysław_Smrokowski.jpg"),
    ("Jozef_Gawlina.jpg", "https://commons.wikimedia.org/wiki/Special:FilePath/Józef_Gawlina_1940.jpg"),
    ("Bronislawa_Wyslouchowa.jpg", "https://commons.wikimedia.org/wiki/Special:FilePath/Bronisława_Wysłouchowa.jpg"),

    # Polscy żołnierze
    ("Emil_Czech.jpg", "https://commons.wikimedia.org/wiki/Special:FilePath/Emil_Czech.jpg"),
    ("Odznaka_3_DSK.jpg", "https://commons.wikimedia.org/wiki/Special:FilePath/Odznaka_Pamiątkowa_3_DSK.jpg"),
    ("Polacy_Wehrmacht_ilustracja.jpg", "https://commons.wikimedia.org/wiki/Special:FilePath/Bundesarchiv_Bild_101I-103-0025-09A,_Nordeuropa,_Soldaten_der_Wehrmacht.jpg"),
    ("Jerzy_Kluger.jpg", "https://commons.wikimedia.org/wiki/Special:FilePath/Jerzy_Kluger.jpg"),
    ("Kpr_Wojtek.jpg", "https://commons.wikimedia.org/wiki/Special:FilePath/Wojtek_soldier_bear.jpg"),

    # Dowódcy alianccy
    ("Harold_Alexander.jpg", "https://commons.wikimedia.org/wiki/Special:FilePath/Harold_Alexander_1.jpg"),
    ("Mark_Wayne_Clark.jpg", "https://commons.wikimedia.org/wiki/Special:FilePath/Mark_Clark.jpg"),
    ("Oliver_Leese.jpg", "https://commons.wikimedia.org/wiki/Special:FilePath/Oliver_Leese.jpg"),
    ("Alphonse_Juin.jpg", "https://commons.wikimedia.org/wiki/Special:FilePath/Alphonse_Juin_1952.jpg"),
    ("Eedson_Burns.jpg", "https://commons.wikimedia.org/wiki/Special:FilePath/Eedson_Louis_Millard_Burns.jpg"),
    ("Bernard_Freyberg.jpg", "https://commons.wikimedia.org/wiki/Special:FilePath/Bernard_Freyberg.jpg"),
    ("Umberto_Utili.jpg", "https://commons.wikimedia.org/wiki/Special:FilePath/Umberto_Utili.jpg"),

    # Żołnierze alianccy
    ("Kamal_Ram.jpg", "https://commons.wikimedia.org/wiki/Special:FilePath/Kamal_Ram_VC.jpg"),

    # Dowódcy niemieccy
    ("Albert_Kesselring.jpg", "https://commons.wikimedia.org/wiki/Special:FilePath/Albert_Kesselring.jpg"),
    ("Fridolin_von_Senger.jpg", "https://commons.wikimedia.org/wiki/Special:FilePath/Bundesarchiv_Bild_101I-708-0300-11,_Fridolin_von_Senger_und_Etterlin.jpg"),
    ("Wilhelm_Schmalz.jpg", "https://commons.wikimedia.org/wiki/Special:FilePath/Wilhelm_Schmalz.jpg"),
    ("Julius_Schlegel.jpg", "https://commons.wikimedia.org/wiki/Special:FilePath/Julius_Schlegel_1944.jpg"),

    # Postacie związane z klasztorem
    ("Sw_Benedykt.jpg", "https://commons.wikimedia.org/wiki/Special:FilePath/St_Benedict_of_Nursia.jpg"),
    ("Sw_Scholastyka.jpg", "https://commons.wikimedia.org/wiki/Special:FilePath/Saint_Scholastica.jpg"),
    ("Gregorio_Diamare.jpg", "https://commons.wikimedia.org/wiki/Special:FilePath/Gregorio_Diamare.jpg"),

    # Odznaczenia
    ("Krzyz_Walecznych.jpg", "https://commons.wikimedia.org/wiki/Special:FilePath/POL_Krzyż_Walecznych_1943.jpg"),
    ("Krzyz_Wiktorii.png", "https://commons.wikimedia.org/wiki/Special:FilePath/Victoria_Cross_Medal.png"),
    ("Virtuti_Militari.svg", "https://commons.wikimedia.org/wiki/Special:FilePath/POL_Order_Virtuti_Militari_V_class_BAR.svg"),
    ("Krzyz_Monte_Cassino.jpg", "https://commons.wikimedia.org/wiki/Special:FilePath/POL_Krzyż_Pamiątkowy_Monte_Cassino.jpg"),
    ("Gwiazda_Wloch.svg", "https://commons.wikimedia.org/wiki/Special:FilePath/Italy_Star_ribbon.svg"),
    ("Legia_Zaslugi.svg", "https://commons.wikimedia.org/wiki/Special:FilePath/Legion_of_Merit_Officer_ribbon.svg"),
    ("Odznaka_Luftwaffe.jpg", "https://commons.wikimedia.org/wiki/Special:FilePath/Fallschirmschützenabzeichen.jpg"),
    ("Odznaka_2_Brygady.jpg", "https://commons.wikimedia.org/wiki/Special:FilePath/POL_2_Warszawska_Brygada_Pancerna_badge.jpg"),

    # Symbole, znaki i naszywki
    ("Czerwone_Maki.jpg", "https://commons.wikimedia.org/wiki/Special:FilePath/Papaver_rhoeas_front.jpg"),
    ("Polski_Orzel.jpg", "https://commons.wikimedia.org/wiki/Special:FilePath/Orzeł_wz.43.jpg"),
    ("Krzyz_sw_Benedykta.jpg", "https://commons.wikimedia.org/wiki/Special:FilePath/Saint_Benedict_Medal_-_Front.jpg"),
    ("Naszywka_PSZ.svg", "https://commons.wikimedia.org/wiki/Special:FilePath/POL_PSZ_8_Army_patch.svg"),
    ("Naszywka_2_Brygady.svg", "https://commons.wikimedia.org/wiki/Special:FilePath/POL_2_Brygada_Pancerna_patch.svg"),
    ("Oznaka_Luftwaffe_Balkenkreuz.svg", "https://commons.wikimedia.org/wiki/Special:FilePath/Balkenkreuz.svg"),

    # Flagi
    ("Flaga_Polski.svg", "https://commons.wikimedia.org/wiki/Special:FilePath/Flag_of_Poland.svg"),
    ("Flaga_Wielkiej_Brytanii.svg", "https://commons.wikimedia.org/wiki/Special:FilePath/Flag_of_the_United_Kingdom.svg"),
    ("Flaga_USA_48.svg", "https://commons.wikimedia.org/wiki/Special:FilePath/Flag_of_the_United_States_(1912-1959).svg"),
    ("Flaga_Wolnej_Francji.svg", "https://commons.wikimedia.org/wiki/Special:FilePath/Flag_of_Free_France_(1940-1944).svg"),
    ("Flaga_Indii_Brytyjskich.svg", "https://commons.wikimedia.org/wiki/Special:FilePath/British_Raj_Red_Ensign.svg"),
    ("Flaga_Wloch_Krolestwo.svg", "https://commons.wikimedia.org/wiki/Special:FilePath/Flag_of_Italy_(1861-1946).svg"),
    ("Flaga_Kanady_1921.svg", "https://commons.wikimedia.org/wiki/Special:FilePath/Flag_of_Canada_(1921–1957).svg"),
    ("Flaga_Nowej_Zelandii.svg", "https://commons.wikimedia.org/wiki/Special:FilePath/Flag_of_New_Zealand.svg"),
    ("Flaga_III_Rzeszy.svg", "https://commons.wikimedia.org/wiki/Special:FilePath/Flag_of_the_German_Reich_(1935–1945).svg")
]

folder_docelowy = "Zdjecia_Monte_Cassino"

if not os.path.exists(folder_docelowy):
    os.makedirs(folder_docelowy)

print("Rozpoczynam pobieranie ze słownikiem polskich znaków oraz z systemem opóźnień...")
for nazwa, raw_url in zdjecia:
    sciezka = os.path.join(folder_docelowy, nazwa)
    
    # Przetwarzamy URL by uwzględnił znaki polskie i spacje, uciekając ASCII
    # "Special:FilePath/" to podział w Wiki, więc kodujemy samą nazwę pliku
    # urllib.parse.quote() przetworzy znaki diakrytyczne
    base_url = "https://commons.wikimedia.org/wiki/Special:FilePath/"
    file_name_encoded = urllib.parse.quote(raw_url.replace(base_url, ''))
    encoded_url = base_url + file_name_encoded

    if not os.path.exists(sciezka):
        print(f"Pobieranie {nazwa}...")
        try:
            req = urllib.request.Request(encoded_url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
            with urllib.request.urlopen(req) as response, open(sciezka, 'wb') as f:
                f.write(response.read())
            # Opóźnienie by serwer Wikipedii nas nie zablokował:
            time.sleep(1.5)
        except Exception as e:
            print(f"Błąd pobierania {nazwa}: {e}")
            time.sleep(2) # Kary umowne opóźnienia
    else:
        print(f"Pominięto {nazwa} - plik już jest.")

print("Zakończono poprawnie!")