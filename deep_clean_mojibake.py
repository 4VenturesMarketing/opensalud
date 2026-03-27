import sys

path = '/Users/mfargas/Documents/4Ventures/00001-Atigravity/06.Andala/4venturesweb/opensalud/estrategia-seo.html'

with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# Comprehensive list of UTF-8 mojibake commonly seen
fixes = {
    'Ã¡': 'á', 'Ã©': 'é', 'Ã­': 'í', 'Ã³': 'ó', 'Ãº': 'ú',
    'Ã': 'é', # Often standalone if the following byte was different
    'Ã±': 'ñ', 'Ã‘': 'Ñ',
    'â€”': '—', 'â€“': '–', 'â€': '—',
    'Â ': ' ', 'Â': '',
    'Â¿': '¿', 'Â¡': '¡',
    'ðŸ“': '��', 'ðŸ': '🚀', # Some emojis might be split
    'â€œ': '"', 'â€ ': '"', 'â€™': "'",
    'â‚¬': '€',
    'CÃ³mo': 'Cómo', 'evaluaciÃ³n': 'evaluación', 'artÃ­culo': 'artículo', 'ArtÃ­culo': 'Artículo'
}

for wrong, right in fixes.items():
    text = text.replace(wrong, right)

# Second pass for remaining standalone patterns
text = re.sub(r'Ã³', 'ó', text)
text = re.sub(r'Ã­', 'í', text)
text = re.sub(r'Ã©', 'é', text)
text = re.sub(r'Ã¡', 'á', text)
text = re.sub(r'Ãº', 'ú', text)

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)
print("Cleaned")
