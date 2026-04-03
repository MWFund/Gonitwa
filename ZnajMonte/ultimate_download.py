import json
import urllib.request
import urllib.parse
import sys
import time
import os

zdjecia = [
    # Polscy dowódcy i oficerowie
    ("Wladyslaw_Anders", "Wladyslaw_Anders.jpg"),
    ("Kazimierz_Sosnkowski", "Kazimierz_Sosnkowski.jpg"),
    ("Bolesław_Bronisław_Duch", "Bronislaw_Duch.jpg"),
    ("Nikodem_Sulik", "Nikodem_Sulik.jpg"),
    ("Bronisław_Rakowski", "Bronislaw_Rakowski.jpg"),
    ("Klemens_Rudnicki", "Klemens_Rudnicki.jpg"),
    ("Władysław_Smrokowski", "Wladyslaw_Smrokowski.jpg"),
    ("Józef_Gawlina", "Jozef_Gawlina.jpg"),
    ("Bronisława_Wysłouchowa", "Bronislawa_Wyslouchowa.jpg"),

    # Polscy żołnierze
    ("Emil_Czech", "Emil_Czech.jpg"),
    ("Odznaka_Pamiątkowa_3_DSK", "Odznaka_3_DSK.jpg"),
    ("Polacy_Wehrmacht", "Polacy_Wehrmacht_ilustracja.jpg"),
    ("Jerzy_Kluger", "Jerzy_Kluger.jpg"),
    ("Wojtek_bear", "Kpr_Wojtek.jpg"),

    # Dowódcy alianccy
    ("Harold_Alexander", "Harold_Alexander.jpg"),
    ("Mark_Clark", "Mark_Wayne_Clark.jpg"),
    ("Oliver_Leese", "Oliver_Leese.jpg"),
    ("Alphonse_Juin", "Alphonse_Juin.jpg"),
    ("Eedson_Burns", "Eedson_Burns.jpg"),
    ("Bernard_Freyberg", "Bernard_Freyberg.jpg"),
    ("Umberto_Utili", "Umberto_Utili.jpg"),

    # Żołnierze alianccy
    ("Kamal_Ram", "Kamal_Ram.jpg"),

    # Dowódcy niemieccy
    ("Albert_Kesselring", "Albert_Kesselring.jpg"),
    ("Fridolin_von_Senger", "Fridolin_von_Senger.jpg"),
    ("Wilhelm_Schmalz", "Wilhelm_Schmalz.jpg"),
    ("Julius_Schlegel", "Julius_Schlegel.jpg"),

    # Postacie związane z klasztorem
    ("Benedict_of_Nursia", "Sw_Benedykt.jpg"),
    ("Saint_Scholastica", "Sw_Scholastyka.jpg"),
    ("Gregorio_Diamare", "Gregorio_Diamare.jpg"),

    # Odznaczenia
    ("Krzyż_Walecznych", "Krzyz_Walecznych.jpg"),
    ("Victoria_Cross", "Krzyz_Wiktorii.png"),
    ("Virtuti_Militari", "Virtuti_Militari.svg"),
    ("Krzyż_Pamiątkowy_Monte_Cassino", "Krzyz_Monte_Cassino.jpg"),
    ("Italy_Star", "Gwiazda_Wloch.svg"),
    ("Legion_of_Merit", "Legia_Zaslugi.svg"),
    ("Fallschirmschützenabzeichen", "Odznaka_Luftwaffe.jpg"),
    ("2_Warszawska_Brygada_Pancerna_badge", "Odznaka_2_Brygady.jpg"),

    # Symbole, znaki i naszywki
    ("Papaver_rhoeas", "Czerwone_Maki.jpg"),
    ("Orzeł_wz.43", "Polski_Orzel.jpg"),
    ("Saint_Benedict_Medal", "Krzyz_sw_Benedykta.jpg"),
    ("8_Army_patch", "Naszywka_PSZ.svg"),
    ("2_Brygada_Pancerna_patch", "Naszywka_2_Brygady.svg"),
    ("Balkenkreuz", "Oznaka_Luftwaffe_Balkenkreuz.svg"),

    # Flagi
    ("Flag_of_Poland", "Flaga_Polski.svg"),
    ("Flag_of_the_United_Kingdom", "Flaga_Wielkiej_Brytanii.svg"),
    ("Flag_of_the_United_States", "Flaga_USA_48.svg"),
    ("Flag_of_Free_France", "Flaga_Wolnej_Francji.svg"),
    ("British_Raj_Red_Ensign", "Flaga_Indii_Brytyjskich.svg"),
    ("Flag_of_Italy", "Flaga_Wloch_Krolestwo.svg"),
    ("Flag_of_Canada", "Flaga_Kanady_1921.svg"),
    ("Flag_of_New_Zealand", "Flaga_Nowej_Zelandii.svg"),
    ("Flag_of_the_German_Reich", "Flaga_III_Rzeszy.svg")
]

folder_docelowy = 'Zdjecia_Monte_Cassino'
if not os.path.exists(folder_docelowy):
    os.makedirs(folder_docelowy)

print("Fetching direct upload.wikimedia.org URLs to avoid rate limiting...")
for search_term, out_name in zdjecia:
    if os.path.exists(os.path.join(folder_docelowy, out_name)):
        continue
        
    query = urllib.parse.quote(search_term)
    
    # Krok 1: Wyszukaj prawidłową nazwę pliku
    search_api = f"https://commons.wikimedia.org/w/api.php?action=query&list=search&srsearch=File:{query}&utf8=&format=json"
    actual_file = ""
    try:
        req = urllib.request.Request(search_api, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode('utf-8'))
            results = data.get("query", {}).get("search", [])
            for res in results:
                if res["title"].startswith("File:"):
                    actual_file = res["title"] # "File:Nazwa.jpg"
                    break
    except Exception as e:
        print(f"Błąd wyszukiwania dla {search_term}")
        
    if not actual_file:
        actual_file = "File:" + search_term + ".jpg"

    # Krok 2: Pobierz BARDZO BEZPOŚREDNI adres do CDN-a (upload.wikimedia.org)
    info_api = f"https://commons.wikimedia.org/w/api.php?action=query&titles={urllib.parse.quote(actual_file)}&prop=imageinfo&iiprop=url&format=json"
    direct_url = ""
    try:
        req2 = urllib.request.Request(info_api, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req2) as response:
            data2 = json.loads(response.read().decode('utf-8'))
            pages = data2.get("query", {}).get("pages", {})
            for page_id, page_info in pages.items():
                if "imageinfo" in page_info and len(page_info["imageinfo"]) > 0:
                    direct_url = page_info["imageinfo"][0]["url"]
    except Exception as e:
        pass
        
    if not direct_url:
        print(f"[{out_name}] Nie znaleziono adresu bezpośredniego dla: {actual_file}")
        continue
        
    # Krok 3: Pobieranie BEZ LIMITÓW przez CND \o/
    sciezka = os.path.join(folder_docelowy, out_name)
    print(f"Pobieranie: {out_name} z {direct_url}")
    try:
        req_dl = urllib.request.Request(direct_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req_dl) as res, open(sciezka, 'wb') as f:
            f.write(res.read())
            time.sleep(3.0) # Zwiększono karę czasową by IP nie łapało Error 429 (zbyt częste żądania do Wikipedii)
    except Exception as e:
        print(f"Błąd pobierania CDN {out_name}: {e}")
        time.sleep(5.0)
        
    time.sleep(3.0)

print("Zakończono pobieranie wszystkich plików :)")
