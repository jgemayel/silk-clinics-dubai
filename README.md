# Silk Clinics Dubai

Multi-page static website for **Silk Clinics**, a multi-specialty aesthetic, skin and dental clinic inside Dubai Healthcare City.

Live reference site: https://silkclinicsdubai.com

## Pages

| File | Purpose |
| --- | --- |
| `index.html` | Home with hero, specialties, featured treatments, offer banner, testimonial, CTA |
| `treatments.html` | Full catalogue of 7 treatment categories (Aesthetic, Skin & Laser, Injectables, Hair, Dental, Wellness, Diagnostics) |
| `popular-treatments.html` | Three signature treatments (Scarlet S, Skin Boosters, Biostimulators) |
| `offers.html` | Seasonal 15% off promo on select skin treatments |
| `blog.html` | Blog index with one featured post and six additional articles |
| `contact.html` | Clinic details, contact form, embedded map |
| `treatment-botox.html` | Template for individual treatment detail pages |
| `styles.css` | Shared design system |

## Design system

- **Brand accent** Silk green `#B2D234` (extracted from the live site)
- **Background** warm off-white `#FAF9F5`
- **Ink** `#141413`
- **Typography** Cormorant Garamond serif paired with Inter sans
- Sticky blurred header, WhatsApp float, responsive at 980px and 600px

## SEO

Every page ships with a unique title, meta description, canonical URL, Open Graph and Twitter card tags. Structured data includes:

- `MedicalBusiness` JSON-LD on the homepage
- `BreadcrumbList` on treatments
- `MedicalProcedure` on treatment detail pages
- Google Analytics tag `G-4FVXC5ELPM`

## Local preview

```bash
cd silk-clinics-dubai
python3 -m http.server 8000
# open http://localhost:8000
```

## Deploy

Drop the directory into any static host (GitHub Pages, Netlify, Vercel, Cloudflare Pages). No build step required.

For GitHub Pages: Settings → Pages → Branch `main` → Root `/`.

## Clinic details

Clinic 304, Building 24, Dubai Healthcare City, Umm Hurair 2, Dubai
Phone `+971 52 188 1437` · Email `info@silkclinicsdubai.com`
