"""Genera los gráficos animados del perfil de GitHub (SVG) a partir de las capturas.
Uso: python generar.py <carpeta de capturas> <carpeta de salida (assets)>
Todo el texto va en UTF-8 y las fuentes son del sistema, para que GitHub lo pinte igual en cualquier equipo.
"""
import base64, io, os, sys
from xml.sax.saxutils import escape
from PIL import Image

cap, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)

FONT = "'Segoe UI', 'Helvetica Neue', Helvetica, Arial, sans-serif"
MONO = "'Cascadia Code', 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace"
BG = "#0a0a12"
GRAD = """<linearGradient id="g" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#22d3ee"/><stop offset=".35" stop-color="#a855f7"/>
      <stop offset=".7" stop-color="#ec4899"/><stop offset="1" stop-color="#fb923c"/>
      <animateTransform attributeName="gradientTransform" type="rotate" from="0 .5 .5" to="360 .5 .5" dur="9s" repeatCount="indefinite"/>
    </linearGradient>"""


def save(name, svg):
    with open(os.path.join(out, name), "w", encoding="utf-8", newline="\n") as f:
        f.write(svg)
    print(f"{name}: {len(svg.encode('utf-8')) // 1024} KB")


# ---------------------------------------------------------------- cabecera
def header():
    particles = "".join(
        f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}" opacity="0">'
        f'<animate attributeName="cy" values="{y};{y - 70}" dur="{d}s" begin="{b}s" repeatCount="indefinite"/>'
        f'<animate attributeName="opacity" values="0;.9;0" dur="{d}s" begin="{b}s" repeatCount="indefinite"/></circle>'
        for x, y, r, c, d, b in [
            (90, 330, 2.2, "#22d3ee", 6, 0), (210, 380, 1.6, "#a855f7", 7, 1.2), (350, 350, 2, "#ec4899", 5.5, 2.1),
            (520, 390, 1.5, "#22d3ee", 8, 0.6), (700, 360, 2.2, "#fb923c", 6.5, 3), (860, 385, 1.7, "#a855f7", 7.5, 1.8),
            (1010, 340, 2, "#22d3ee", 6, 2.6), (1120, 380, 1.6, "#ec4899", 8, 0.9), (1160, 300, 1.4, "#fb923c", 7, 3.6),
            (40, 250, 1.4, "#a855f7", 9, 4.2), (610, 320, 1.3, "#ec4899", 6.8, 4.8), (960, 280, 1.5, "#22d3ee", 7.2, 5.1),
        ]
    )
    typed = "AI Developer &amp; SaaS Builder"
    chips = [("6 productos en producción", 150), ("20+ webs a medida", 400), ("vídeo · voz · avatares con IA", 610)]
    chip_svg = ""
    for i, (t, x) in enumerate(chips):
        w = 30 + len(t) * 8.6
        chip_svg += (
            f'<g opacity="0"><animate attributeName="opacity" values="0;1" dur=".6s" begin="{3.4 + i * .35}s" fill="freeze"/>'
            f'<rect x="{x}" y="318" width="{w:.0f}" height="34" rx="17" fill="#ffffff" fill-opacity=".06" stroke="url(#g)" stroke-width="1.2"/>'
            f'<circle cx="{x + 17}" cy="335" r="4" fill="#34d399"><animate attributeName="opacity" values="1;.25;1" dur="1.6s" repeatCount="indefinite"/></circle>'
            f'<text x="{x + 30}" y="340" font-family="{FONT}" font-size="14.5" font-weight="600" fill="#e4e4e7">{escape(t)}</text></g>'
        )
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 400" width="1200" height="400" role="img" aria-label="Jose Bustos, AI Developer y SaaS Builder">
  <defs>
    {GRAD}
    <filter id="blur" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="70"/></filter>
    <filter id="glow" x="-20%" y="-50%" width="140%" height="200%"><feGaussianBlur stdDeviation="9" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
    <pattern id="grid" width="44" height="44" patternUnits="userSpaceOnUse"><path d="M44 0H0V44" fill="none" stroke="#ffffff" stroke-opacity=".045"/></pattern>
    <clipPath id="frame"><rect width="1200" height="400" rx="26"/></clipPath>
    <clipPath id="type"><rect x="150" y="226" height="50" width="0"><animate attributeName="width" from="0" to="470" dur="2.2s" begin="1s" fill="freeze"/></rect></clipPath>
  </defs>
  <g clip-path="url(#frame)">
    <rect width="1200" height="400" fill="{BG}"/>
    <g filter="url(#blur)" opacity=".75">
      <circle cx="180" cy="90" r="170" fill="#7c3aed"><animate attributeName="cx" values="180;420;180" dur="16s" repeatCount="indefinite"/><animate attributeName="cy" values="90;200;90" dur="13s" repeatCount="indefinite"/></circle>
      <circle cx="1000" cy="320" r="190" fill="#0891b2"><animate attributeName="cx" values="1000;760;1000" dur="18s" repeatCount="indefinite"/><animate attributeName="cy" values="320;150;320" dur="15s" repeatCount="indefinite"/></circle>
      <circle cx="640" cy="420" r="150" fill="#db2777" opacity=".8"><animate attributeName="cx" values="640;880;440;640" dur="22s" repeatCount="indefinite"/></circle>
    </g>
    <rect width="1200" height="400" fill="url(#grid)"/>
    <rect width="1200" height="400" fill="{BG}" opacity=".35"/>
    {particles}
    <g opacity="0"><animate attributeName="opacity" values="0;1" dur=".8s" begin=".1s" fill="freeze"/>
      <text x="150" y="112" font-family="{MONO}" font-size="17" fill="#a1a1aa" letter-spacing="3">&lt;hola mundo /&gt;</text>
    </g>
    <g filter="url(#glow)" opacity="0"><animate attributeName="opacity" values="0;1" dur="1s" begin=".3s" fill="freeze"/>
      <text x="146" y="200" font-family="{FONT}" font-size="96" font-weight="800" letter-spacing="-2" fill="url(#g)">Jose Bustos</text>
    </g>
    <g clip-path="url(#type)"><text x="150" y="262" font-family="{MONO}" font-size="30" font-weight="600" fill="#f4f4f5">{typed}</text></g>
    <rect x="150" y="232" width="3" height="36" fill="#22d3ee">
      <animate attributeName="x" from="150" to="622" dur="2.2s" begin="1s" fill="freeze"/>
      <animate attributeName="opacity" values="1;0;1" dur=".9s" repeatCount="indefinite"/>
    </rect>
    <g opacity="0"><animate attributeName="opacity" values="0;1" dur=".8s" begin="3s" fill="freeze"/>
      <text x="150" y="298" font-family="{FONT}" font-size="19" fill="#d4d4d8">Convierto ideas en productos con IA que funcionan en producción.</text>
    </g>
    {chip_svg}
    <g transform="translate(960 96)" opacity=".95">
      <g fill="none" stroke="url(#g)" stroke-width="2.2">
        <circle r="78" stroke-dasharray="12 10"><animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="22s" repeatCount="indefinite"/></circle>
        <circle r="54" stroke-dasharray="4 9" opacity=".8"><animateTransform attributeName="transform" type="rotate" from="360" to="0" dur="14s" repeatCount="indefinite"/></circle>
        <circle r="30" opacity=".9"><animate attributeName="r" values="30;35;30" dur="3s" repeatCount="indefinite"/></circle>
      </g>
      <text y="9" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="800" fill="#f4f4f5">IA</text>
    </g>
    <rect x="1" y="1" width="1198" height="398" rx="25" fill="none" stroke="url(#g)" stroke-width="2" opacity=".7"/>
  </g>
</svg>"""


# ---------------------------------------------------------------- títulos de sección
def section(title, subtitle):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 96" width="1200" height="96" role="img" aria-label="{escape(title)}">
  <defs>{GRAD}</defs>
  <text x="4" y="46" font-family="{FONT}" font-size="40" font-weight="800" letter-spacing="-.5" fill="url(#g)">{escape(title)}</text>
  <text x="6" y="76" font-family="{FONT}" font-size="17" fill="#8b8b99">{escape(subtitle)}</text>
  <rect x="4" y="88" height="4" rx="2" width="0" fill="url(#g)">
    <animate attributeName="width" values="0;1192" dur="1.6s" begin=".2s" fill="freeze" calcMode="spline" keyTimes="0;1" keySplines=".2 .8 .2 1"/>
  </rect>
  <circle cy="90" r="5" fill="#ffffff"><animate attributeName="cx" values="4;1196;4" dur="7s" repeatCount="indefinite"/><animate attributeName="opacity" values=".9;.2;.9" dur="7s" repeatCount="indefinite"/></circle>
</svg>"""


# ---------------------------------------------------------------- cifras
def numbers():
    items = [("6", "productos en producción"), ("20+", "webs a medida"), ("5", "backends propios en mi servidor"), ("6", "motores de IA en RunPod")]
    cells = ""
    for i, (n, t) in enumerate(items):
        x = 6 + i * 299
        cells += (
            f'<g opacity="0" transform="translate(0 14)"><animate attributeName="opacity" values="0;1" dur=".7s" begin="{.15 + i * .2}s" fill="freeze"/>'
            f'<animateTransform attributeName="transform" type="translate" from="0 14" to="0 0" dur=".7s" begin="{.15 + i * .2}s" fill="freeze"/>'
            f'<rect x="{x}" y="6" width="287" height="118" rx="18" fill="#12121c" stroke="url(#g)" stroke-width="1.5" stroke-opacity=".8"/>'
            f'<text x="{x + 143}" y="70" text-anchor="middle" font-family="{FONT}" font-size="52" font-weight="800" fill="url(#g)">{n}</text>'
            f'<text x="{x + 143}" y="102" text-anchor="middle" font-family="{FONT}" font-size="15.5" fill="#c4c4cf">{escape(t)}</text></g>'
        )
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 130" width="1200" height="130" role="img" aria-label="Cifras">
  <defs>{GRAD}</defs>{cells}
</svg>"""


# ---------------------------------------------------------------- tarjetas con captura
def card(key, title, tagline, url, live, crop_h=690):
    im = Image.open(os.path.join(cap, key)).convert("RGB")
    w, _ = im.size
    im = im.crop((0, 0, w, int(crop_h * w / 1280))).resize((600, int(600 * crop_h / 1280)), Image.LANCZOS)
    ih = im.size[1]
    buf = io.BytesIO(); im.save(buf, "JPEG", quality=80, optimize=True, progressive=True)
    b64 = base64.b64encode(buf.getvalue()).decode()
    H = 36 + ih + 74
    host = url.replace("https://", "").replace("www.", "").rstrip("/")
    badge = ""
    if live:
        badge = (f'<g transform="translate(486 48)"><rect width="102" height="26" rx="13" fill="#052e16" fill-opacity=".9" stroke="#34d399" stroke-opacity=".7"/>'
                 f'<circle cx="16" cy="13" r="4.5" fill="#34d399"><animate attributeName="opacity" values="1;.2;1" dur="1.4s" repeatCount="indefinite"/></circle>'
                 f'<text x="28" y="17.5" font-family="{FONT}" font-size="12.5" font-weight="700" fill="#bbf7d0" letter-spacing=".6">EN VIVO</text></g>')
    return f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 608 {H + 8}" width="608" height="{H + 8}" role="img" aria-label="{escape(title)}: {escape(tagline)}">
  <defs>
    {GRAD}
    <clipPath id="c"><rect x="4" y="4" width="600" height="{H}" rx="18"/></clipPath>
    <linearGradient id="shine" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".5" stop-color="#fff" stop-opacity=".16"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
  </defs>
  <g clip-path="url(#c)">
    <rect x="4" y="4" width="600" height="{H}" fill="#11111b"/>
    <rect x="4" y="4" width="600" height="36" fill="#1a1a27"/>
    <circle cx="26" cy="22" r="5.5" fill="#ff5f57"/><circle cx="44" cy="22" r="5.5" fill="#febc2e"/><circle cx="62" cy="22" r="5.5" fill="#28c840"/>
    <rect x="150" y="11" width="308" height="22" rx="11" fill="#0a0a12"/>
    <text x="304" y="26.5" text-anchor="middle" font-family="{MONO}" font-size="12.5" fill="#a1a1aa">{escape(host)}</text>
    <image x="4" y="40" width="600" height="{ih}" href="data:image/jpeg;base64,{b64}"/>
    <rect x="-260" y="40" width="220" height="{ih}" fill="url(#shine)" transform="skewX(-18)">
      <animate attributeName="x" values="-260;900" dur="1.5s" begin="1.2s;6.2s;12.2s;18.2s;24.2s;30.2s;36.2s;42.2s;48.2s;54.2s" fill="freeze"/>
    </rect>
    {badge}
    <rect x="4" y="{40 + ih}" width="600" height="74" fill="#11111b"/>
    <rect x="4" y="{40 + ih}" width="600" height="2" fill="url(#g)"/>
    <text x="24" y="{40 + ih + 31}" font-family="{FONT}" font-size="21" font-weight="800" fill="#fafafa">{escape(title)}</text>
    <text x="24" y="{40 + ih + 55}" font-family="{FONT}" font-size="14" fill="#a1a1aa">{escape(tagline)}</text>
    <g transform="translate(560 {40 + ih + 37})"><circle r="15" fill="none" stroke="url(#g)" stroke-width="1.6"/><path d="M-5 5 L5 -5 M-2 -5 H5 V2" fill="none" stroke="#fafafa" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></g>
  </g>
  <rect x="4" y="4" width="600" height="{H}" rx="18" fill="none" stroke="url(#g)" stroke-width="2.2"/>
</svg>"""


# ---------------------------------------------------------------- pie
def footer():
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 150" width="1200" height="150" role="img" aria-label="Hablemos">
  <defs>{GRAD}<clipPath id="f"><rect width="1200" height="150" rx="22"/></clipPath></defs>
  <g clip-path="url(#f)">
    <rect width="1200" height="150" fill="{BG}"/>
    <path fill="url(#g)" opacity=".35"><animate attributeName="d" dur="9s" repeatCount="indefinite" values="M0 100 Q300 60 600 100 T1200 100 V150 H0Z;M0 100 Q300 140 600 100 T1200 100 V150 H0Z;M0 100 Q300 60 600 100 T1200 100 V150 H0Z"/></path>
    <path fill="url(#g)" opacity=".55"><animate attributeName="d" dur="6s" repeatCount="indefinite" values="M0 118 Q300 138 600 118 T1200 118 V150 H0Z;M0 118 Q300 96 600 118 T1200 118 V150 H0Z;M0 118 Q300 138 600 118 T1200 118 V150 H0Z"/></path>
    <text x="600" y="58" text-anchor="middle" font-family="{FONT}" font-size="30" font-weight="800" fill="#fafafa">¿Tienes una idea? La pongo en producción.</text>
    <text x="600" y="86" text-anchor="middle" font-family="{FONT}" font-size="16" fill="#a1a1aa">Apps con IA · webs a medida · automatización para empresas y pymes</text>
  </g>
</svg>"""


save("cabecera.svg", header())
save("cifras.svg", numbers())
save("pie.svg", footer())
save("sec-apps.svg", section("Aplicaciones", "Productos propios, en producción y con su backend"))
save("sec-webs.svg", section("Webs a medida", "Diseño, efectos y piezas interactivas hechas para cada negocio"))
save("sec-motores.svg", section("Motores de IA", "Lo que hay debajo: generación de imagen, vídeo y voz"))
save("sec-stack.svg", section("Con qué trabajo", "Del diseño al servidor"))
save("sec-actividad.svg", section("Actividad", "Código casi todos los días"))

CARDS = [
    ("app-aihumanslab", "ahl.jpg", "AI Humans Lab", "Avatares digitales, vídeo y contenido UGC con IA", "https://www.aihumanslab.com", True),
    ("app-click2model", "c2m.jpg", "Click2Model", "De la prenda a fotos y Reels con modelos de IA", "https://www.click2model.es", True),
    ("app-innovagastro", "gastro.jpg", "InnovaGastro", "Carta digital, asistente con IA y reservas para restaurantes", "https://www.innovagastro.es", True),
    ("app-lumiere", "lumiere.jpg", "Lumière", "Reservas, bonos y cambio de look con IA para salones", "https://lumiere.innovapymes.ai", True),
    ("app-companions", "companions2.jpg", "Companions", "Avatares 3D con los que hablas en tiempo real", "https://companions.innovapymes.ai", True),
    ("app-ofertaalavista", "ofertas.jpg", "Oferta a la Vista", "Comparador de ofertas verificadas, con miles de productos", "https://ofertaalavista.com", True),
    ("web-dania360", "dania.jpg", "Dania 360", "Gestión de redes sociales y web con bot de IA", "https://dania360.com", False),
    ("web-tunel", "tunel.jpg", "Webs en túnel 3D", "Una web inmersiva a partir de la web de una empresa", "https://dania-tunel.vercel.app", False),
    ("web-nordauto", "nordauto.jpg", "Nordauto", "Taller de chapa y pintura con parte de daños interactivo", "https://nordauto-markina.vercel.app", False),
    ("web-ambinature", "ambinature.jpg", "AmbiNature Andorra", "Web corporativa con efectos de humo y color", "https://ambinature-andorra.vercel.app", False),
    ("web-glousie", "glousie.jpg", "Glousie", "Peluquería con horario en vivo y cartas de servicios", "https://web-demo-glousie-murcia.vercel.app", False),
    ("web-reformas", "reformas.jpg", "María Cándida Alemán", "Reformas con plano interactivo para dibujar la obra", "https://web-demo-maria-candida-aleman-hita.vercel.app", False),
    ("web-estefania", "estefania.jpg", "Estefanía Plaza", "Centro de estética con test de piel", "https://estefania-plaza-demo.vercel.app", False),
    ("web-mariamartin", "mariamartin.jpg", "María Martín", "Estética avanzada con calculadora de láser", "https://maria-martin-demo.vercel.app", False),
    ("web-barbara", "barbara.jpg", "Bárbara Marrero", "Consulta de psicología, serena y cuidada", "https://barbara-marrero-psicologia.vercel.app", False),
]
for name, img, title, tag, url, live in CARDS:
    save(name + ".svg", card(img, title, tag, url, live))
