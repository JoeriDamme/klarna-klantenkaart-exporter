import csv
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://app.klarna.com/wallet-home-v2')

    input("Druk op Enter na inloggen...")

    access_token = page.evaluate("window.localStorage.getItem('@KLAPP:signIn:accessToken')")

    if not access_token:
        print("❌ Geen access token gevonden. Controleer of je correct bent ingelogd.")
        browser.close()
        exit(1)

    cards_url = "https://app.klarna.com/nl/api/consumer_wallet_bff/v4/wallet-content?is_migrated_from_stocard=true"
    
    cards_headers = {
        "Authorization": f"Bearer {access_token}",
        "Accept": "application/json",
        "User-Agent": "Mozilla/5.0"
    }

    cards_res = page.request.get(cards_url, headers=cards_headers)

    if not cards_res.ok:
        print("❌ Fout bij ophalen van klantenkaarten.")
        print(cards_res.status_code, cards_res.text)
        browser.close()
        exit(1)

    cards_data = cards_res.json()

    with open("klantenkaarten.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["name", "barcode_raw", "barcode_formatted", "format"])

        for card in cards_data["loyalty_identifiers"]:
            processed_data = card.get("processed", {})
            barcode = processed_data.get("barcode", {})
            
            writer.writerow([
                processed_data.get("name"),
                barcode.get("id", {}).get("raw"),
                barcode.get("id", {}).get("formatted"),
                barcode.get("format")
            ])

    print("✅ Klantenkaarten geëxporteerd naar klantenkaarten.csv")

    browser.close()