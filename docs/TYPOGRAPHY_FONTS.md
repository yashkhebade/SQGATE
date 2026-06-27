# Typography & Fonts

## 1. Primary Font Families
- **Inter** (sans-serif): Used for all body text, paragraphs, UI buttons, and technical data. Selected for maximum legibility at small sizes.
- **Outfit** (sans-serif): Used for major headers (H1, H2), hero sections, and marketing copy to provide a premium, modern feel.

## 2. Weights & Usage
- **Body Text:** Inter 400 (Regular)
- **Small UI Elements (Meta/Tags):** Inter 500 (Medium), `11px`-`12px`
- **Buttons / Actions:** Inter 600 (Semi-Bold), `13px`-`15px`
- **Hero Headers:** Outfit 800 (Extra Bold), tightly tracked (`letter-spacing: -1px`)

## 3. Implementation
Fonts are loaded via Google Fonts. No local font hosting is necessary to ensure fast load times utilizing global CDN caching.
```html
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Outfit:wght@400;600;800&display=swap" rel="stylesheet">
```
