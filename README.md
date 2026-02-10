# Test Umiejętności Szachowych - ADEPT Magii Szachowej

Interaktywna aplikacja webowa do testowania umiejętności szachowych uczniów na poziomie ADEPT (poziomy 1-9).

## 📋 Opis

Aplikacja pozwala na kompleksową ocenę umiejętności szachowych w 9 kategoriach:
- Szachownica i jej właściwości
- Goniec
- Wieża
- Hetman
- Skoczek
- Król i Pion
- Wartość materialna figur
- Szach, Mat i Pat
- Roszada

## ✨ Funkcje

- **Interaktywny formularz** z pytaniami testowymi
- **Animowana odznaka** z wizualizacją osiągniętego poziomu
- **Szczegółowe wyniki** z analizą mocnych i słabych stron
- **Rekomendacje rozwoju** - sugestie, które umiejętności poprawić dla awansu
- **Eksport do PDF** - możliwość zapisania wyników
- **Responsywny design** - działa na różnych urządzeniach

## 🚀 Jak używać

1. Otwórz plik `egzamin1.html` w przeglądarce
2. Wpisz imię ucznia
3. Wypełnij formularz testowy, wybierając odpowiednie poziomy umiejętności
4. Kliknij "Sprawdź mój poziom!"
5. Przejrzyj wyniki i opcjonalnie zapisz je do PDF

## 📁 Struktura projektu

```
kilo-api/
├── egzamin1.html          # Główny plik aplikacji
├── przypinka_clear.png    # Grafika odznaki
└── README.md             # Ten plik
```

## 🎨 Technologie

- HTML5
- CSS3 (z animacjami i gradientami)
- Vanilla JavaScript
- Responsywny design

## 📊 System oceniania

Aplikacja oblicza:
- **Aktualny poziom** - najniższy wynik ze wszystkich kategorii
- **Średnią** - średni wynik z wszystkich kategorii
- **Obszary do poprawy** - kategorie na najniższym poziomie
- **Możliwości awansu** - ile kategorii trzeba poprawić dla awansu

## 🖨️ Funkcja PDF

Przycisk "Zapisz wynik" otwiera okno druku przeglądarki z automatycznie:
- Ukrytym formularzem testowym
- Ukrytymi przyciskami akcji
- Zoptymalizowanym układem do druku
- Nazwą pliku zawierającą imię ucznia i datę

## 📝 Licencja

Projekt edukacyjny - Chess School Magic Academy

## 👨‍💻 Autor

Projekt stworzony dla szkół szachowych do oceny postępów uczniów.
