# Auto-école en ligne · Bénin

Projet de plateforme d'auto-école en ligne pour le Bénin : révision du code de la route sur téléphone, examens blancs, réservation des leçons de conduite et paiement Mobile Money.

## Contenu

- `index.html` : le site publié (Vercel), généré par `python3 scripts/build.py`.
- `maquette/index.html` : la source de la page (sans `<head>`), à modifier.
- `manifest.webmanifest`, `sw.js`, `icons/` : installation sur téléphone et fonctionnement hors connexion.

## Mettre en ligne sur Vercel

1. Sur https://vercel.com/new, choisir « Import Git Repository » et sélectionner ce dépôt.
2. Framework : « Other ». Ne rien remplir pour la commande de build ni le dossier de sortie.
3. Cliquer sur « Deploy ». Chaque push sur `main` met le site à jour.

## Feuille de route

1. Site vitrine et inscriptions en ligne
2. Code en ligne : séries, examens blancs, espace candidat, paiement Mobile Money
3. Application mobile : réservation des leçons, tableau de bord des moniteurs

Le nom « Volant Bénin », les prix et le contenu du code sont provisoires et à valider avec l'auto-école.

## Skills de design utilisés

La maquette suit les règles de ces skills Claude Code :

- [pbakaus/impeccable](https://github.com/pbakaus/impeccable)
- [emilkowalski/skills](https://github.com/emilkowalski/skills)
- [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)

Pour les installer sur ton ordinateur :

```bash
npx skills@latest add pbakaus/impeccable
npx skills@latest add emilkowalski/skills
npx skills@latest add Leonxlnx/taste-skill
```
