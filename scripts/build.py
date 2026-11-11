"""Construit index.html (le site publié sur Vercel) à partir de maquette/index.html.

maquette/index.html est le contenu de la page sans <html>/<head>/<body> ; ce script
ajoute l'en-tête complet, le manifeste et le service worker.
Usage : python3 scripts/build.py
"""
import pathlib, re

root = pathlib.Path(__file__).resolve().parent.parent
src = (root / 'maquette' / 'index.html').read_text(encoding='utf-8')

head_end = src.index('</style>') + len('</style>')
head, body = src[:head_end], src[head_end:]
head = head.replace('<meta name="claude:viewport-fit-sides" content="cover">\n', '')

extra_head = '''<meta name="theme-color" content="#0b6b46">
<link rel="manifest" href="/manifest.webmanifest">
<link rel="icon" href="/icons/icon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/icons/icon-192.png">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="Volant Bénin">
<meta property="og:title" content="Volant Bénin">
<meta property="og:description" content="Auto-école à Cotonou : le code de la route sur ton téléphone, avec les questions lues à voix haute.">
<meta property="og:type" content="website">
'''
sw = '''<script>
if ('serviceWorker' in navigator) { addEventListener('load', () => navigator.serviceWorker.register('/sw.js').catch(() => {})); }
</script>
'''
html = ('<!doctype html>\n<html lang="fr">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        + extra_head + head + '\n</head>\n<body>\n' + body.strip() + '\n' + sw + '</body>\n</html>\n')
(root / 'index.html').write_text(html, encoding='utf-8')
print('index.html :', len(html), 'octets')
