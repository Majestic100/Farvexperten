# Farveeksperten

Landingsside for Farveeksperten – maling, gulve, gardiner og markiser.

## Struktur
- `index.html` – selve landingssiden (self-contained, responsiv)
- `assets/fonts/` – self-hostede fonte (Poppins, Roboto)

## Preview
Åbn `index.html` i en browser, eller se det via GitHub Pages.

## Opsætning der mangler

### 1. Kontaktformular (Web3Forms)
Formularen sender til **marianne@farvexperten.dk** via Web3Forms.

1. Gå til [web3forms.com](https://web3forms.com), indtast `marianne@farvexperten.dk`, og få en gratis access key på mail.
2. Erstat `INDSAET_WEB3FORMS_ACCESS_KEY` i `index.html` med nøglen.
3. Send en testbesked og bekræft, at mailen ankommer.

Gratisplanen dækker 250 henvendelser/måned og gemmer indsendelser i 30 dage i Web3Forms-dashboardet.

### 2. Meta Pixel
Erstat `INDSAET_META_PIXEL_ID` i `index.html` med jeres Pixel-ID.
Pixel og Google Maps indlæses først, når brugeren accepterer cookies.
