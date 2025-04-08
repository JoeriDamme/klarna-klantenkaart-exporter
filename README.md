# Klarna Klantenkaart Exporter

Helaas is Stocard overgenomen door Klarna. Hierdoor ben je nu verplicht om de Klarna app te installeren.
De Klarna app is echter veel meer dan een app die klantenkaarten bewaard en komt met allemaal features waar je niet op zit te wachten.
Ik heb daarom een export functie gemaakt die de klantenkaarten die dus nu uit Klarna trekt.
Ik ben nog aan het onderzoeken de export weer misschien in een andere app geimporteerd kan worden.

Wordt vervolgd.

RIP Stocard.

## Wie kan dit gebruiken?
Op dit moment moet je wat ervaring hebben met het werken in een terminal en zorgen dat je Python3 geïnstalleerd hebt.

## Hoe werkt het?

Dit is alleen getest op een mac. Geen idee of dit op Windows werkt.
Zorg ervoor dat de `Playwright` package is geinstalleerd:

```bash
python3 -m pip install playwright
python3 -m playwright install
```

Vervolgens start je het Python script:
```bash
python3 export_klantenkaarten.py
```

Dat opent een Chromium browser. Sluit de terminal niet af. Hierin staat de melding: `Druk op Enter na inloggen...`
Dus log nu eerst in bij Klarna via de Chromium browser. Als je eenmaal bent ingelogd, ga je terug naar de terminal
en druk je op enter.
Er wordt nu automatisch een CSV bestand voor je aangemaakt met:

- naam (albert heijn)
- barcode_raw (123456789)
- bardcode_formatted (123 456 789)
- format (CODE_128, EAN_13, QR_CODE etc.)