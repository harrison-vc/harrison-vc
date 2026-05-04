# Design System: Vanguard Infrastructure Architecture

## 1. Visual Theme & Atmosphere
The atmosphere is "Stealth Technical" — a high-agency, institutional interface that mirrors the faceplate of a premium server rack. It balances **Cockpit Dense (9)** data modules with **Art Gallery Airy (2)** structural whitespace. Layouts are strictly **Offset Asymmetric (7)** to break the AI centering bias, supported by **Fluid (6)** micro-animations that signal a living, observable system.

## 2. Color Palette & Roles
- **Canvas Black** (#09090B) — Primary background surface (OLED depth)
- **Core Surface** (#18181B) — Secondary surface, badge backgrounds, and container fill
- **Gallery White** (#F4F4F5) — Primary typography and high-signal data
- **Muted Slate** (#71717A) — Secondary text, labels, and system metadata
- **Technical Zinc** (#27272A) — Hairline borders, structural lines, and dividers
- **Electric Emerald** (#10B981) — Singular accent for active states, system status, and technical paths (Saturation < 80%)

## 3. Typography Rules
- **Display:** Geist Sans / system-ui — Massive scale (84pt+), track-tight (-5%), heavy weight (900). Anchored to the left for asymmetric tension.
- **Body:** Geist Sans — Relaxed leading (1.6), max 60ch width, Muted Slate color.
- **Mono:** JetBrains Mono / Geist Mono — For technical labels, paths (`/ROOT/`), metadata, and high-density numbers.
- **Rules:** No Inter. No generic serif fonts. All technical labels MUST use uppercase tracking (4px).

## 4. Component Stylings
*   **Badges:** Monochromatic (Core Surface background) with Flat White icons. No rainbow colors. 22px height for technical precision.
*   **Cards (Double-Bezel):** Major modules must use a nested architecture. Outer shell (Technical Zinc border) with an inner Core Surface fill and a 1px white/5 top highlight to simulate refractive glass.
*   **Inputs:** Label above (Mono), error below. 1px Technical Zinc border. No glow effects.
*   **Loaders:** Shimmering scanning line (Electric Emerald, 5% opacity) moving vertically through the layout.

## 5. Layout Principles
- **Editorial Hierarchy:** Strict left-alignment for all primary content. Centered headers are BANNED.
- **Asymmetric Grid:** Use 3-column or 70/30 splits. Metadata blocks should be anchored to the top-right, opposite the primary title.
- **Density:** Technical "Arsenal" should be organized into high-density grids to create texture rather than a wall of logos.
- **Containment:** 1200px max-width for SVGs and primary web containers.

## 6. Motion & Interaction
- **Physics:** Spring-based transitions (`stiffness: 100, damping: 20`). No linear movement.
- **Perpetual Motion:** Active components must feature an infinite loop state (e.g., a 2s opacity pulse on status indicators or a 10s scan line).
- **Hardware Feel:** Interaction feedback should be tactile (e.g., -1px vertical translate on push).

## 7. Anti-Patterns (Banned)
- No emojis (replace with Phosphor/Radix icons).
- No "Rainbow" or "Logo-colored" badges.
- No centered layouts for Hero/Header sections.
- No AI copywriting clichés ("Elevate", "Next-Gen", "Seamless").
- No neon outer glows or oversaturated gradients.
- No fake round numbers (e.g., use 99.99% instead of 100%).
