# Farveeksperten

Landingsside for Farveeksperten – maling, gulve, gardiner og markiser.

## Struktur
- `index.html` – selve landingssiden (self-contained, responsiv)
- `assets/fonts/` – self-hostede fonte (Poppins, Roboto)

## Preview
Åbn `index.html` i en browser, eller se det via GitHub Pages.

## Opsætning der mangler

### 1. Kontaktformular (Web3Forms) — nøgle er sat ✅
Formularen sender til **marianne@farvexperten.dk** via Web3Forms.
Access key ligger i `index.html` (den er ikke hemmelig og må gerne stå offentligt).

Gratisplanen dækker 250 henvendelser/måned og gemmer indsendelser i 30 dage i Web3Forms-dashboardet.

**Ved flytning til GoHighLevel (GHL):** hvis der er sat en domænebegrænsning på
access key'en i Web3Forms, skal det nye domæne tilføjes der, ellers afvises
indsendelser. Alternativt kan formularen sendes direkte til GHL i stedet — i så
fald udskiftes kun `fetch(...)`-endpointet i `index.html`.

### 2. Meta Pixel
Erstat `INDSAET_META_PIXEL_ID` i `index.html` med jeres Pixel-ID.
Pixel og Google Maps indlæses først, når brugeren accepterer cookies.
