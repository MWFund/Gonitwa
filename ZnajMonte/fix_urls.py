import json
import urllib.request
import urllib.parse
import sys

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

fixed_urls = []
print("Searching Wikipedia for real files...")
for search_term, out_name in zdjecia:
    query = urllib.parse.quote(search_term)
    # Search for files with this title
    api_url = f"https://commons.wikimedia.org/w/api.php?action=query&list=search&srsearch=File:{query}&utf8=&format=json"
    
    try:
        req = urllib.request.Request(api_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode('utf-8'))
            results = data.get("query", {}).get("search", [])
            if results:
                # Get the first actual File:
                file_title = None
                for res in results:
                    if res["title"].startswith("File:"):
                        file_title = res["title"].replace("File:", "")
                        break
                if file_title:
                    fixed_urls.append((out_name, file_title))
                    print(f"Found {file_title} for {search_term}")
                    continue
    except Exception as e:
        pass
    print(f"NOT FOUND: {search_term}")
    fixed_urls.append((out_name, search_term + ".jpg"))

# Write new download script
with open("download_fixed.py", "w", encoding="utf-8") as f:
    f.write("import os\nimport urllib.request\nimport urllib.parse\nimport time\n\nzdjecia = [\n")
    for out_name, file_title in fixed_urls:
        f.write(f'    ("{out_name}", "https://commons.wikimedia.org/wiki/Special:FilePath/{urllib.parse.quote(file_title)}"),\n')
    f.write("]\n")
    
    f.write("""
folder_docelowy = 'Zdjecia_Monte_Cassino'
if not os.path.exists(folder_docelowy):
    os.makedirs(folder_docelowy)

print('Rozpoczynam poprawione pobieranie...')
for nazwa, url in zdjecia:
    sciezka = os.path.join(folder_docelowy, nazwa)
    if not os.path.exists(sciezka):
        print(f'Pobieranie {nazwa}...')
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as response, open(sciezka, 'wb') as out_f:
                out_f.write(response.read())
            time.sleep(1.5)
        except Exception as e:
            print(f'Błąd dla {nazwa} z {url}: {e}')
    else:
        print(f'Pominięto {nazwa} - już istnieje.')
""")
print("Odbudowano plik jako download_fixed.py")
