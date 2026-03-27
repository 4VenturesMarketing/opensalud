path = '/Users/mfargas/Documents/4Ventures/00001-Atigravity/06.Andala/4venturesweb/opensalud/estrategia-seo.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace H2 title
content = content.replace('9. Roadmap ejecutivo: ejecución técnica paso a paso', '9. Roadmap ejecutivo paso a paso')

# No menu change needed since it already says "9. Roadmap" in shorter version, 
# but making sure for full-text consistency

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
