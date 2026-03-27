import sys

path = '/Users/mfargas/Documents/4Ventures/00001-Atigravity/06.Andala/4venturesweb/opensalud/estrategia-seo.html'

try:
    # Try reading as Latin-1 or other potentially mismatched encoding
    # and then correcting it back to UTF-8
    with open(path, 'rb') as f:
        binary_data = f.read()
    
    # The image shows typical UTF-8 characters being interpreted as something else (mojibake)
    # Example: Artículo becoming ArtÃ­culo
    # Let's try to decode as UTF-8 and if that fails, we have a real mess.
    # If it's already written as "ArtÃ­culo" in the file, it means it was SAVED as UTF-8
    # but the source was already garbled.
    
    text = binary_data.decode('utf-8')
    
    # Common mojibake fixes
    fixes = {
        'Ã¡': 'á', 'Ã©': 'é', 'Ã­': 'í', 'Ã³': 'ó', 'Ãº': 'ú',
        'Ã‘': 'Ñ', 'Ã±': 'ñ', 'Â¿': '¿', 'Â¡': '¡',
        'Ã ': 'à', 'Ã¨': 'è', 'Ã¬': 'ì', 'Ã²': 'ò', 'Ã¹': 'ù',
        'â€': '—', # Sometimes it's part of a dash
        'Ã€': 'À', 'Â': '', # Extra artifacts
        'ðŸ“': '📄', # The document emoji
        'â€“': '—',
        'â€”': '—',
        'â€œ': '"',
        'â€': '"',
        'â€™': "'",
    }
    
    for wrong, right in fixes.items():
        text = text.replace(wrong, right)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)
    print("Success")

except Exception as e:
    print(f"Error: {e}")
