import re

path = '/Users/mfargas/Documents/4Ventures/00001-Atigravity/06.Andala/4venturesweb/opensalud/estrategia-seo.html'

with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# Massive map of common mojibake pairs (UTF-8 bytes misread as Windows-1252/ISO-8859-1)
fixes = {
    'Ã¡': 'á', 'Ã©': 'é', 'Ã­': 'í', 'Ã³': 'ó', 'Ãº': 'ú',
    'Ã ': 'à', 'Ã¨': 'è', 'Ã¬': 'ì', 'Ã²': 'ò', 'Ã¹': 'ù',
    'Ã±': 'ñ', 'Ã‘': 'Ñ',
    'Â¿': '¿', 'Â¡': '¡',
    'ðŸ“': '📄', 'ðŸ': '🚀',
    'â€”': '—', 'â€“': '–', 'â€œ': '"', 'â€ ': '"', 'â€™': "'",
    'â€': '—',
    'Â': '', # Extra artifacts
    'Ã': 'í', # Standalone fix for common í error
}

for k, v in fixes.items():
    text = text.replace(k, v)

# Specific words from image
text = text.replace('Artí­culo', 'Artículo')
text = text.replace('Cá³mo', 'Cómo')
text = text.replace('evaluaciá³n', 'evaluación')
text = text.replace('Á³', 'ó') # Typical break in evaluation

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)
print("Finished")
