import re
import sys

path = '/Users/mfargas/Documents/4Ventures/00001-Atigravity/06.Andala/4venturesweb/opensalud/estrategia-seo.html'

with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# Manual mapping for common broken substrings from the screenshot
# "ArtÃ­culo" -> "Artículo"
# "CÃ³mo" -> "Cómo"
# "evaluaciÃ³n" -> "evaluación"
# "ðŸ“" -> "📄"
# "â€”" -> "—"

mojibake_map = {
    'Ã¡': 'á', 'Ã©': 'é', 'Ã­': 'í', 'Ã³': 'ó', 'Ãº': 'ú',
    'Ã ': 'à', 'Ã¨': 'è', 'Ã¬': 'ì', 'Ã²': 'ò', 'Ã¹': 'ù',
    'Ã±': 'ñ', 'Ã‘': 'Ñ',
    'Â¿': '¿', 'Â¡': '¡',
    'ðŸ“': '📄',
    'â€”': '—',
    'â€“': '–',
    'â€œ': '"',
    'â€ ': '"',
    'â€™': "'",
    'â€': '—',
    'Ã ': ' ', 'Â ': ' ', 'Â': ''
}

# Apply the map
for k, v in mojibake_map.items():
    text = text.replace(k, v)

# Final cleanup for remaining "Ã "
text = text.replace('Ã ', 'á')
text = text.replace('Ã³', 'ó')
text = text.replace('Ã­', 'í')

with open(path, 'w', encoding='utf-8', errors='ignore') as f:
    f.write(text)

print("Deep cleaning successful")
