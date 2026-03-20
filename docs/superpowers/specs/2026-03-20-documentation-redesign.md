# eYssen Documentation Redesign

## Summary

Modernize the Sphinx-based documentation theme to match eyssen.com's design language.
Style: "Red Line" (V5) — dark header/hero with red vertical line guiding content flow.

## Design Decisions

- **Color palette**: eyssen.com exact colors — `#C8102E` (red), `#1A1A2E` (dark), `#FAFAF8` (bg), `#F7F5F2` (warm bg)
- **Typography**: Playfair Display (headings) + DM Sans (body) + JetBrains Mono (code)
- **Layout**: Red vertical line connects hero to content sections, dot markers at section labels
- **Cards**: 20px radius, top-border red animation on hover, translateY(-4px) lift
- **Header**: Glassmorphism (blur 20px, transparent bg), pill version badge with pulse dot
- **Footer**: Dark (#0F0F1A) 4-column footer matching eyssen.com
- **Buttons**: Pill-shaped (100px radius), red CTA style from eyssen.com
- **What's New**: Git-based auto-generation via custom Sphinx extension

## Files to Modify

1. `extensions/odoo_theme/static/scss/bootstrap_overridden.scss` — colors, fonts, radius
2. `extensions/odoo_theme/static/scss/_variables.scss` — new font families
3. `extensions/odoo_theme/static/scss/style.scss` — new component styles
4. `extensions/odoo_theme/layout_templates/homepage.html` — complete redesign
5. `extensions/odoo_theme/layout_templates/header.html` — glassmorphism nav
6. `extensions/odoo_theme/layout_templates/footer.html` — dark 4-column footer
7. `extensions/odoo_theme/layout_templates/layout.html` — font imports
8. `extensions/changelog/` — new git-based changelog extension
9. `conf.py` — register changelog extension

## Reference Mockup

`/docs/superpowers/brainstorm/.../homepage-v5-eyssen.html`
