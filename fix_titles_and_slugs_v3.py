import re

path = '/Users/mfargas/Documents/4Ventures/00001-Atigravity/06.Andala/4venturesweb/opensalud/estrategia-seo.html'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

article_titles = {
    1: "Cómo realizar la evaluación de riesgos psicosociales (ley 31/1995)",
    2: "El coste real del absentismo laboral por estrés en españa (datos 2026)",
    3: "Estrategias de retención de talento en 2026: el rol de la salud mental",
    4: "Diferencia entre vigilancia médica física y vigilancia de salud mental",
    5: "Guía para medir el clima laboral y el enps en recursos humanos",
    6: "Burnout en equipos de alto rendimiento: señales y protocolos",
    7: "Programas de bienestar corporativo: 5 ejemplos y cómo medir su roi",
    8: "Plataformas de psicología b2b: ¿qué exigir a tu proveedor?",
    9: "Liderazgo empático: claves para reducir la rotación de personal",
    10: "Síndrome del impostor y productividad: cómo afecta a la rentabilidad"
}

# Corrected regex with exact match including spaces
for i in range(10, 0, -1): # Backward order to avoid Artículo 1 matching Artículo 10
    pattern = rf'Artículo {i} — slug:'
    replacement = rf'Artículo {i}: {article_titles[i]} — slug:'
    text = text.replace(pattern, replacement)

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Update attempt v3 complete")
