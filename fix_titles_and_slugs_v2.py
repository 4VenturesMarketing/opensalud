import re

path = '/Users/mfargas/Documents/4Ventures/00001-Atigravity/06.Andala/4venturesweb/opensalud/estrategia-seo.html'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# Define the dictionary of titles (from meta titles)
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

# We'll use a regex to find each Article X card and replace its H3.
for i in range(1, 11):
    # Pattern to match: <h3 style="margin-top:0; color:var(--blue)">Artículo X — slug: <code>...</code></h3>
    pattern = rf'<h3 style="margin-top:0; color:var(--blue)">Artículo {i} — slug: (<code>.*?</code>)</h3>'
    replacement = rf'<h3 style="margin-top:0; color:var(--blue)">Artículo {i}: {article_titles[i]} — slug: \1</h3>'
    text = re.sub(pattern, replacement, text)

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Finished update")
