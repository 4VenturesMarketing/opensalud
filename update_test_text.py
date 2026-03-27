path = '/Users/mfargas/Documents/4Ventures/00001-Atigravity/06.Andala/4venturesweb/opensalud/estrategia-seo.html'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

old = 'el testador algorítmico certificado por expertos'
new = 'nuestro test de madurez en Bienestar Corporativo'

# Check for both cases (upper/lowercase start if it varies)
text = text.replace(old, new)
text = text.replace(old[:1].upper() + old[1:], new[:1].upper() + new[1:])

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)
