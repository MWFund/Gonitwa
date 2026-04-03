import os
import urllib.request
import urllib.parse
import time

zdjecia = [
    ("Wladyslaw_Anders.jpg", "https://commons.wikimedia.org/wiki/Special:FilePath/Wladyslaw%20Anders.jpg"),
    ("Kazimierz_Sosnkowski.jpg", "https://commons.wikimedia.org/wiki/Special:FilePath/Sosnkowski%20Kazimierz.jpg"),
    ("Bronislaw_Duch.jpg", "https://commons.wikimedia.org/wiki/Special:FilePath/GeneralDuch.jpg"),
    ("Nikodem_Sulik.jpg", "https://commons.wikimedia.org/wiki/Special:FilePath/Nikodem%20sulik.jpg"),
    ("Bronislaw_Rakowski.jpg", "https://commons.wikimedia.org/wiki/Special:FilePath/Bronis%C5%82aw%20Rakowski.jpg"),
    ("Klemens_Rudnicki.jpg", "https://commons.wikimedia.org/wiki/Special:FilePath/Rudnicki.jpg"),
    ("Wladyslaw_Smrokowski.jpg", "https://commons.wikimedia.org/wiki/Special:FilePath/W%C5%82adys%C5%82aw_Smrokowski.jpg"),
    ("Jozef_Gawlina.jpg", "https://commons.wikimedia.org/wiki/Special:FilePath/J%C3%B3zef%20Gawlina.png"),
    ("Bronislawa_Wyslouchowa.jpg", "https://commons.wikimedia.org/wiki/Special:FilePath/Bronis%C5%82awa%20Wys%C5%82ouchowa%20pp%C5%82k%20NAC%2024-319.jpg"),
    ("Emil_Czech.jpg", "https://commons.wikimedia.org/wiki/Special:FilePath/2023%20Medal%20pami%C4%99ci%20Emila%20Czecha%20%284%29.jpg"),
    ("Odznaka_3_DSK.jpg", "https://commons.wikimedia.org/wiki/Special:FilePath/Odznaka%203%20DSK.jpg"),
    ("Polacy_Wehrmacht_ilustracja.jpg", "https://commons.wikimedia.org/wiki/Special:FilePath/Exhumation%20of%20Poles%20executed%20by%20Wehrmacht%20in%20Raci%C4%85%C5%BC.jpg"),
    ("Jerzy_Kluger.jpg", "https://commons.wikimedia.org/wiki/Special:FilePath/Jerzy%20Kluger%202.jpg"),
    ("Kpr_Wojtek.jpg", "https://commons.wikimedia.org/wiki/Special:FilePath/Wojtek%20the%20bear.jpg"),
    ("Harold_Alexander.jpg", "https://commons.wikimedia.org/wiki/Special:FilePath/Sir%20Harold%20Alexander%20026065.jpg"),
    ("Mark_Wayne_Clark.jpg", "https://commons.wikimedia.org/wiki/Special:FilePath/Mark-Clark-public-domain-scaled.jpg"),
    ("Oliver_Leese.jpg", "https://commons.wikimedia.org/wiki/Special:FilePath/Lieutenant%20General%20Sir%20Oliver%20Leese%2C%20commander%20of%20the%20British%20Eighth%20Army%20in%20Italy%2C%2030%20April%201944.%20TR1759.jpg"),
    ("Alphonse_Juin.jpg", "https://commons.wikimedia.org/wiki/Special:FilePath/USA-MTO-NWA-p651%20Alphonse%20Juin.jpg"),
    ("Eedson_Burns.jpg", "https://commons.wikimedia.org/wiki/Special:FilePath/General%20E.%20L.%20M.%20Burns%20%28cropped%29.jpg"),
    ("Bernard_Freyberg.jpg", "https://commons.wikimedia.org/wiki/Special:FilePath/Bernard%20Freyberg.jpg"),
    ("Umberto_Utili.jpg", "https://commons.wikimedia.org/wiki/Special:FilePath/Incontro%20De%20Gaulle-Utili%20a%20Colli%20a%20Volturno.jpg"),
    ("Kamal_Ram.jpg", "https://commons.wikimedia.org/wiki/Special:FilePath/The%20Union%20Minister%20for%20Commerce%20and%20Industry%20Shri%20Kamal%20Nath%20meets%20the%20Union%20Minister%20for%20Steel%2C%20Chemicals%20and%20Fertilizers%20Shri%20Ram%20Vilas%20Paswan%20on%20WTO%20issues%20in%20New%20Delhi%20on%20July%2020%2C%202004.jpg"),
    ("Albert_Kesselring.jpg", "https://commons.wikimedia.org/wiki/Special:FilePath/Bundesarchiv%20Bild%20183-R93434%2C%20Albert%20Kesselring.jpg"),
    ("Fridolin_von_Senger.jpg", "https://commons.wikimedia.org/wiki/Special:FilePath/Bundesarchiv%20Bild%20101I-311-0914-10A%2C%20General%20Fridolin%20v.%20Senger%20und%20Etterlin.jpg"),
    ("Wilhelm_Schmalz.jpg", "https://commons.wikimedia.org/wiki/Special:FilePath/Wilhelm%20Schmalz.jpg"),
    ("Julius_Schlegel.jpg", "https://commons.wikimedia.org/wiki/Special:FilePath/Julius%20Schlegel.jpg"),
    ("Sw_Benedykt.jpg", "https://commons.wikimedia.org/wiki/Special:FilePath/Frari%20%28Venice%29%20-%20Sacristy%20-%20triptych%20by%20Giovanni%20Bellini%20-%20Saint%20Benedict%20of%20Nursia%20and%20Saint%20Mark.jpg"),
    ("Sw_Scholastyka.jpg", "https://commons.wikimedia.org/wiki/Special:FilePath/SantaScolastica%20Montecassino.jpg"),
    ("Gregorio_Diamare.jpg", "https://commons.wikimedia.org/wiki/Special:FilePath/Gregorio%20Vito%20Diamare.jpg"),
    ("Krzyz_Walecznych.jpg", "https://commons.wikimedia.org/wiki/Special:FilePath/Cross%20of%20Valour%20%28Poland%29%201944.jpg"),
    ("Krzyz_Wiktorii.png", "https://commons.wikimedia.org/wiki/Special:FilePath/Victoria%20Cross%20Medal%20without%20Bar.png"),
    ("Virtuti_Militari.svg", "https://commons.wikimedia.org/wiki/Special:FilePath/Virtuti%20Militari%20Grand%20Cross.jpg"),
    ("Krzyz_Monte_Cassino.jpg", "https://commons.wikimedia.org/wiki/Special:FilePath/Krzyz%20MonteCassino%20Polska.jpg"),
    ("Gwiazda_Wloch.svg", "https://commons.wikimedia.org/wiki/Special:FilePath/WW2%20Italy%20Star.jpg"),
    ("Legia_Zaslugi.svg", "https://commons.wikimedia.org/wiki/Special:FilePath/Legionnaire%20of%20the%20Legion%20of%20Merit.jpg"),
    ("Odznaka_Luftwaffe.jpg", "https://commons.wikimedia.org/wiki/Special:FilePath/Fallschirmsch%C3%BCtzenabzeichen%20der%20Luftwaffe.png"),
    ("Odznaka_2_Brygady.jpg", "https://commons.wikimedia.org/wiki/Special:FilePath/2_Warszawska_Brygada_Pancerna_badge.jpg"),
    ("Czerwone_Maki.jpg", "https://commons.wikimedia.org/wiki/Special:FilePath/Czech%20Republic%20-%20landscape%20near%20Kory%C4%8Dany.jpg"),
    ("Polski_Orzel.jpg", "https://commons.wikimedia.org/wiki/Special:FilePath/KURICA.png"),
    ("Krzyz_sw_Benedykta.jpg", "https://commons.wikimedia.org/wiki/Special:FilePath/Saint%20Benedict%20Medal%20icon.svg"),
    ("Naszywka_PSZ.svg", "https://commons.wikimedia.org/wiki/Special:FilePath/Royal%20Romanian%20Army%20collar%20patches%20-%20Reg%208.%20Ro%C5%9Fiori%20%281912-1918%29.png"),
    ("Naszywka_2_Brygady.svg", "https://commons.wikimedia.org/wiki/Special:FilePath/2_Brygada_Pancerna_patch.jpg"),
    ("Oznaka_Luftwaffe_Balkenkreuz.svg", "https://commons.wikimedia.org/wiki/Special:FilePath/Balkenkreuz%20fuselage%20underwing.svg"),
    ("Flaga_Polski.svg", "https://commons.wikimedia.org/wiki/Special:FilePath/Flag%20of%20Poland.svg"),
    ("Flaga_Wielkiej_Brytanii.svg", "https://commons.wikimedia.org/wiki/Special:FilePath/Church%20of%20All%20Saints%2C%20Odiham%201.JPG"),
    ("Flaga_USA_48.svg", "https://commons.wikimedia.org/wiki/Special:FilePath/Apollo%2015%20flag%2C%20rover%2C%20LM%2C%20Irwin.jpg"),
    ("Flaga_Wolnej_Francji.svg", "https://commons.wikimedia.org/wiki/Special:FilePath/Flag%20of%20Free%20France%20%281940-1944%29.svg"),
    ("Flaga_Indii_Brytyjskich.svg", "https://commons.wikimedia.org/wiki/Special:FilePath/British%20Raj%20Red%20Ensign.svg"),
    ("Flaga_Wloch_Krolestwo.svg", "https://commons.wikimedia.org/wiki/Special:FilePath/Flag%20of%20Italy.svg"),
    ("Flaga_Kanady_1921.svg", "https://commons.wikimedia.org/wiki/Special:FilePath/Your%20motherland%20will%20never%20forget%20-%20restoration.jpg"),
    ("Flaga_Nowej_Zelandii.svg", "https://commons.wikimedia.org/wiki/Special:FilePath/Flag%20of%20New%20Zealand.svg"),
    ("Flaga_III_Rzeszy.svg", "https://commons.wikimedia.org/wiki/Special:FilePath/Flag%20of%20Germany%20%281935%E2%80%931945%29.svg"),
]

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
