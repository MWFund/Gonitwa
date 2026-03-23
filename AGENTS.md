# Gonitwa - Dokumentacja Architektury i Standardów

Ten dokument opisuje architekturę, standardy kodowania oraz używane biblioteki w projekcie **Gonitwa** (Chess Pursuit). Został stworzony, aby pomóc agentom AI oraz programistom w zrozumieniu struktury i konwencji tego projektu.

## 🎮 Opis Gry, Zasady i Cel

**Gonitwa (Chess Pursuit)** to zręcznościowa minigra przeglądarkowa oparta na klasycznej mechanice szachowej. Głównym celem gracza jest przetrwanie w obliczu nieustającego pościgu ze strony nacierających figur przeciwnika, przy jednoczesnym zdobywaniu jak najwyższego wyniku.

**Kluczowe założenia i zasady:**
1. **Wybór figury:** Gracz na początku wybiera, w jaką figurę chce się wcielić (Król, Hetman, Wieża, Goniec, Skoczek, Pion). Postać porusza się zgodnie z tradycyjnymi zasadami gry w szachy. Z tego powodu może bić pionki, które uniemożliwiają ucieczkę lub "wejdą" na jej drogę.
2. **Cel główny:** 
   - Ciągła ucieczka przed ścigającym wrogiem i unikanie własnego "szach mata", który kończy grę.
   - Pomyślne docieranie do kolejnych, wyższych punktów kontrolnych — tzw. "linii obrony" (łącznie ukryte w środowisku gry są poziomy od 1 do 6). Niesie to ze sobą pokaźny zastrzyk w postaci bonusu do punktów.
   - Zbijanie (w miarę możliwości na szachownicy) pionków z ramienia przeciwnego władcy.
3. **Punktacja w grze:**
   - Zbicie Piona: 1 pkt
   - Zbicie Gońca lub Skoczka: 3 pkt
   - Zbicie Wieży: 5 pkt
   - Zbicie Hetmana: 9 pkt
   - Szczęśliwe ukończenie Poziomu `N`: Otrzymanie bonusowo `N × 100 pkt`
4. **Rozgrywka i Mechaniki Czasowe:** W grę wbudowane jest tempo "Szybka" lub "Wolna". Akcja odbywa się dynamicznie w czasie rzeczywistym. Gra kończy się definitywnie w momencie, gdy zdeterminowana armia złapie naszego gracza.

## 🏛 Architektura Projektu

Projekt *Gonitwa* to minigra przeglądarkowa typu "przetrwanie" (survival/chase) osadzona na motywach szachowych. Architektura opiera się o tradycyjne środowisko **Vanilla Web** uruchamiane całkowicie po stronie klienta (Client-Side). 

Kluczowe aspekty architektury to:
1. **Single Page Application (SPA) bez frameworka**: Cały interfejs znajduje się w pliku `index.html`. Główne menu oraz nakładki HUD ukrywane/odsłaniane są za pomocą manipulacji klasą CSS (np. `.hidden`). Główne okno gry montowane jest dynamicznie w elemencie `#root`.
2. **Pętla Gry (Game Loop) & Renderowanie**: Silnik gry działa na podstawie własnej pętli wykorzystującej `window.requestAnimationFrame` (np. funkcja `tic` w `game.js`). Wykorzystuje architekturę oknu (DOM/SVG) z domieszką HTML5 Canvas:
   - *Canvas*: Do dynamicznego generowania teł (np. *bgCanvas*, *shadowCanvas*, domyślnie także *skyCanvas*).
   - *Elementy DOM*: Figury szachowe i plansza zarządzane są natywnymi elementami SVG lub DIV modyfikowanymi z poziomu `game.js`.
3. **Zarządzanie Stanem / Zapis Danych (Local Storage)**: Najlepsze wyniki i checkpointy gracza (Leaderboard) są asynchronicznie zapisywane bezpośrednio w przeglądarce za pomocą interfejsu API lokalnego magazynu: domyślny klucz to `LEADERBOARD_KEY = 'gonitwa_scores_v2'`.
4. **Rescaling / Responsywność Globalna**: Aplikacja nie posługuje się układami flex/grid do skalowania właściwej zawartości gry, ale wykorzystuje funkcję adaptacyjną `applyResponsiveScale`, wyliczającą zoom planszy w odniesieniu do zmiennej `SIZE` (bazowo 400px * 1.8) dodając odpowiednią regułę z `transform: scale()`, idealnie wypełniając aktualny viewport urządzenia.

## 📚 Biblioteki i Zależności

Aplikacja opiera z założenia na kodzie modułowym bez wielkich frameworków interfejsu użytkownika (np. bez Reacta, czy Vue.js), a jedynie z drobną warstwą toolingową. Główne narzędzia i zależności to:

1. **jsfxr (ArcadeAudio)**
   - Wbudowana bezpośrednio w `game.js` biblioteka będąca natywnym javascriptowym portem narzędzia generującego retrodźwięki (sfxr). Dzięki algorytmicznej generacji projekt nie wymaga ładowania osobnych assetów audio (.mp3 / .ogg). Zaimplementowano wrappera `ArcadeAudio` zarządzającego buforami.
2. **Google Fonts**
   - Importowane nowoczesne fonty `Outfit` (dla nagłówków, liczb i tytułów) oraz `Plus Jakarta Sans` (do bloków tekstowych).
3. **Grunt (`package.json`)**
   - System zarządzania zadaniami w Node.js, używany w trybie deweloperskim m.in. do kompilacji, minifikacji (plugin `grunt-contrib-uglify`), sprawdzania jakości kodu (`grunt-contrib-jshint`) oraz testów jednostkowych (`nodeunit`, `qunit`). 

## 🛠 Standardy Kodowania

Aby zachować spójność z istniejącym ekosystemem, należy trzymać się poniższych pryncypiów:

### ✨ Interfejsy i Design (HTML & CSS)
* **Zmienne CSS (Custom Properties)**: W całym pliku `styles.css` lub tagu `<style>` głównym rdzeniem spójności są tokeny zapisane w zmiennej pseudo-klasie `:root`. Używaj koncepcji `oklch` przy deklaracjach kolorów (np. `--c-accent-gold: oklch(0.85 0.16 85)`).
* **Fluid Typography**: Nie używaj sztywno ustalonej wielkości fontów `px`. Kod interfejsu używa zmiennych opartych o funkcję `clamp()` (np. `--text-xl: clamp(1.5rem, 2vw + 1.25rem, 2rem);`) by płynnie dostosować tekst do każdego wyświetlacza.
* **Klasy niemutowalne**: Unikaj nadpisywania stylów poszczególnym atrybutom ID (`#`), promuj wykorzystywanie klas. 

### 💻 Logika (JavaScript)
* **Konfiguracja Tekstowa**: Nigdy nie umieszczaj ("hardcode") tekstów na "sztywno" w logice. Elementy stałe tekstu oraz dialogi umieszczaj w centralnym obiekcie rejestru `TEXT_CONFIG` znajdującym się na szczycie pliku `game.js`. Dodawaj i używaj funkcji zwracających dany szablon komunikatu z tego obiektu.
* **Hermetyzacja Logiki**: Podstawowy kod używa starego/klasycznego standardu ES5 (globalne zmienne konfiguracyjne, definicje `var`, `function() {}`). Do modyfikacji nowych mechanizmów można stosować elementy ES6+ (`const`, `let`), jeśli nie łamią domknięć logicznych wewnątrz `game.js`. 
* **Bezpieczny DOM**: Preferuj Vanilla DOM API (np. `document.getElementById`, `element.classList`). Wrzucając nowy fragment do DOM, zachowaj nadane mu atrybuty bezwzględne ARIA (`aria-live`, `aria-label`) dla dostępności projektu.
