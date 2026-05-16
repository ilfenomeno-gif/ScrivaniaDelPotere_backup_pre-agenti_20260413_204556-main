from pathlib import Path
from zipfile import ZipFile
from xml.etree import ElementTree as ET
from pypdf import PdfReader
import re

root = Path(r"c:/Users/PC/Downloads/bellius-libro-main/bellius-libro-main")
structure = root / "bellius-libro-structure"
ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}


def docx_paragraphs(path: Path):
    with ZipFile(path) as zf:
        xml = zf.read("word/document.xml")
    tree = ET.fromstring(xml)
    paras = []
    for p in tree.findall(".//w:p", ns):
        texts = [t.text for t in p.findall(".//w:t", ns) if t.text]
        line = "".join(texts).strip()
        if line:
            paras.append(re.sub(r"\s+", " ", line))
    return paras


def to_markdown(lines, source_name):
    out = [
        f"# Conversione Markdown - {source_name}",
        "",
        f"Fonte: `{source_name}`",
        "",
        "> Conversione automatica da DOCX a Markdown. La struttura del testo e stata preservata in forma lineare per consultazione e controllo di coerenza.",
        "",
    ]
    title_done = False
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        if not title_done and stripped.isupper() and len(stripped) < 80:
            out.append(f"# {stripped.title()}")
            out.append("")
            title_done = True
            continue
        if stripped == "PROLOGO":
            out.append("## Prologo")
            out.append("")
            continue
        if re.match(r"^(CAPITOLO|Capitolo)\s+\d+", stripped):
            out.append(f"## {stripped.title()}")
            out.append("")
            continue
        if stripped in {"* * *", "♦ ♦ ♦"}:
            out.append("---")
            out.append("")
            continue
        if stripped.isupper() and len(stripped) < 120:
            out.append(f"### {stripped.title()}")
            out.append("")
            continue
        out.append(stripped)
        out.append("")
    return "\n".join(out).strip() + "\n"


books = {
    "bellius_libro1_corretto.docx": "bellius-libro-1.md",
    "bellius_libro2_corretto.docx": "bellius-libro-2.md",
    "bellius_libro3_corretto.docx": "bellius-libro-3.md",
}

for source, target in books.items():
    lines = docx_paragraphs(root / source)
    md = to_markdown(lines, source)
    (structure / "9-manoscritto" / target).write_text(md, encoding="utf-8")

pdf_reader = PdfReader(str(root / "protagonista_zen (1).pdf"))
pdf_text = []
for page in pdf_reader.pages:
    pdf_text.append(page.extract_text() or "")
pdf_md = (
    "# Conversione Markdown - protagonista_zen (1).pdf\n\n"
    "Fonte: `protagonista_zen (1).pdf`\n\n"
    "> Conversione automatica da PDF a Markdown per consultazione lore.\n\n"
    + "\n\n".join(t.strip() for t in pdf_text if t.strip())
    + "\n"
)
(structure / "9-manoscritto" / "protagonista-zen.md").write_text(pdf_md, encoding="utf-8")

character_template = """# {name}

## Definizione
{definizione}

## Identita
{identita}

## Ruolo narrativo
{ruolo}

## Obiettivi
{obiettivi}

## Conflitti
{conflitti}

## Psicologia
{psicologia}

## Backstory
{backstory}

## Relazioni
{relazioni}

## Evoluzione
{evoluzione}

## Voce e comportamento
{voce}

## Capacita e limiti
{capacita}

## Simboli e temi
{simboli}

## Note di lore
{lore}

## Stato attuale
{stato}

## Aspetto fisico
{aspetto}

## Abbigliamento
{abbigliamento}

## Oggetti personali
{oggetti}

## Luogo d'origine
{origine}

## Fazione o gruppo
{fazione}

## Momenti chiave
{momenti}

## Frasi caratteristiche
{frasi}

## Contraddizioni narrative
{contraddizioni}

## Possibili evoluzioni alternative
{alternative}
"""

characters = {
    "protagonisti/bellius.md": dict(
        name="Bellius",
        definizione="Protagonista originario della saga, motore del primo volume e figura attraverso cui la vendetta personale apre il conflitto piu ampio.",
        identita="Bellius; uomo; fratello di Tebris; origine legata al trauma di un villaggio distrutto e alla caccia contro Nerone.",
        ruolo="Protagonista del primo volume e presenza simbolica nei successivi.",
        obiettivi="Obiettivo esterno: raggiungere e uccidere Nerone. Obiettivo interno: dare forma al dolore e ritrovare un senso dopo la perdita. Bisogno profondo: capire se la vendetta puo davvero colmare il vuoto.",
        conflitti="Conflitto esterno: viaggio, nemici, distanza, instabilita del mondo mortale e irruzione del divino. Conflitto interiore: rabbia che consuma e rende ciechi.",
        psicologia="Duro, diretto, ostinato, orientato all'azione. Porta il lutto come una brace costante.",
        backstory="Ha perso la madre e il villaggio in un evento traumatico condiviso con Tebris.",
        relazioni="Tebris: fratello e ancora di umanita. Nerone: bersaglio della vendetta. Spazio: figura collegata all'espansione del conflitto.",
        evoluzione="Parte come uomo guidato dalla vendetta. Il suo arco mette in crisi l'idea che eliminare il colpevole basti a guarire.",
        voce="Voce asciutta, scelte rapide, pochi giri di parole.",
        capacita="Tenacia, combattivita, resistenza al freddo e alla fatica. Limite principale: ossessione.",
        simboli="Vendetta, fratellanza, ferita originaria, insufficienza della violenza come cura.",
        lore="Fondamentale per il baricentro umano della saga.",
        stato="Canonico",
        aspetto="Segnato dal viaggio e dalla tensione continua.",
        abbigliamento="Vesti di lana ruvida da viaggio nel primo volume.",
        oggetti="Armi da viaggio.",
        origine="Da verificare con precisione.",
        fazione="Asse Bellius-Tebris.",
        momenti="Partenza verso Nerone; confronto col vuoto dopo la vendetta.",
        frasi='"Finche non avremo la testa di Nerone."',
        contraddizioni="Da chiarire il peso operativo nei volumi 2 e 3.",
        alternative="Ritorno come memoria attiva o testimone del conflitto finale.",
    ),
    "protagonisti/spazio.md": dict(
        name="Spazio",
        definizione="Figura centrale e trasversale della trilogia, ponte tra asse umano, combattimento, identita liminale e conflitto divino.",
        identita="Spazio; nome assunto come marchio di destino; associato alla maschera bianca.",
        ruolo="Protagonista trasversale, soprattutto nei volumi Evesor.",
        obiettivi="Obiettivo esterno: cercare libro, chiavi e soglia. Obiettivo interno: capire cosa e diventato.",
        conflitti="Conflitto esterno: scontri mortali, cacce, figure divine, sistema di Andoi. Conflitto interiore: identita fratturata.",
        psicologia="Osservatore, strategico, essenziale, adattivo.",
        backstory="Riceve il nome Spazio e attraversa arene, viaggi, alleanze e rivelazioni.",
        relazioni="Magnus, Honos, Ignis, Elara, Andoi, Bellius, Tebris.",
        evoluzione="Da combattente mascherato a figura capace di muoversi tra piani e soglie.",
        voce="Parla poco, parole nette, osserva prima di agire.",
        capacita="Apprendimento del combattimento, resistenza, lettura pattern. Limiti: isolamento e ossessione.",
        simboli="Maschera, presenza, vuoto, adattamento.",
        lore="Personaggio-cerniera tra piano mortale e regno divino.",
        stato="Canonico",
        aspetto="Associato a una maschera bianca.",
        abbigliamento="Da viaggio e combattimento.",
        oggetti="Maschera bianca, poi chiavi.",
        origine="Da verificare.",
        fazione="Variabile, spesso nucleo mobile.",
        momenti="Assegnazione del nome; arene; incontro con Magnus; confronto con Honos; arco delle chiavi.",
        frasi='"Spazio." come autoaffermazione identitaria.',
        contraddizioni="Da chiarire il rapporto preciso con Evesor.",
        alternative="Figura di passaggio stabile tra umano e divino.",
    ),
    "protagonisti/tebris.md": dict(
        name="Tebris",
        definizione="Fratello di Bellius e contrappeso umano del primo volume.",
        identita="Tebris; uomo; fratello di Bellius.",
        ruolo="Co-protagonista del primo volume.",
        obiettivi="Aiutare Bellius a raggiungere Nerone e conservare umanita.",
        conflitti="Dubita che la vendetta valga il costo.",
        psicologia="Riflessivo, sensibile, capace di guardare oltre la battaglia.",
        backstory="Condivide con Bellius la perdita del villaggio e della madre.",
        relazioni="Bellius: legame fraterno centrale.",
        evoluzione="Coscienza critica dell'asse vendetta.",
        voce="Misurata, problematizzante.",
        capacita="Tenuta nel viaggio e nel conflitto; limite: vulnerabilita emotiva.",
        simboli="Fratellanza, umanita residua, dubbio etico.",
        lore="Impedisce che Bellius diventi solo una lama.",
        stato="Canonico",
        aspetto="Occhi scuri, stanchezza e tensione.",
        abbigliamento="Vesti di viaggio.",
        oggetti="Pugnale.",
        origine="Da verificare.",
        fazione="Asse Bellius-Tebris.",
        momenti="Dialoghi sul senso della vendetta.",
        frasi='"A volte mi chiedo se ne varra la pena."',
        contraddizioni="Da chiarire cronologia e destino nei richiami successivi.",
        alternative="Presenza memoriale piu estesa.",
    ),
    "protagonisti/zen.md": dict(
        name="Zen",
        definizione="Protagonista del materiale prequel e cardine della cosmologia della morte.",
        identita="Zen; dio anziano; mutaforma.",
        ruolo="Protagonista del concept PDF, fondazione potenziale di prequel.",
        obiettivi="Realizzare un sistema di pace per anime divine e non divine.",
        conflitti="Tradimento di Andoi; caccia divina; costo della perdita dell'anima.",
        psicologia="Idealista all'origine, poi sempre piu duro e scisso.",
        backstory="Ultimo degli dei anziani; propone Pax; viene incastrato sul bastone.",
        relazioni="Andoi, Morte, Verdetto, Nyx, JC.",
        evoluzione="Da architetto della pace a figura rossa oscura.",
        voce="Da definire in prosa futura.",
        capacita="Mutaforma e accesso al bastone; limite massimo: perdita del filtro morale.",
        simboli="Pace fallita, tradimento, bastone, Uomo in Rosso.",
        lore="Cruciale per Pax, Tax e morte divina.",
        stato="Da verificare contro trilogia principale",
        aspetto="Occhi bianchi poi neri-rossi nella trasformazione finale.",
        abbigliamento="Tunica rossa nella forma finale.",
        oggetti="Bastone della Morte.",
        origine="Regno divino.",
        fazione="Dei anziani.",
        momenti="Proposta Pax; tradimento; fuga; presa del bastone.",
        frasi="Da estrarre in stesura prequel.",
        contraddizioni="Legame con Uomo in Rosso da fissare nei romanzi principali.",
        alternative="Romanzo prequel autonomo.",
    ),
}

secondary_names = [
    "Andoi","Nerone","Nyx","Magnus","Honos","Ignis","Guardiano","Theron","Elara","Castore","Polluce","Luccio","Lucas","Marcus","Druso","Verdetto","Morte","JC",
]

secondary_dir_map = {
    "Andoi":"antagonisti/andoi.md",
    "Nerone":"antagonisti/nerone.md",
    "Nyx":"antagonisti/nyx.md",
    "Magnus":"secondari/magnus.md",
    "Honos":"secondari/honos.md",
    "Ignis":"secondari/ignis.md",
    "Guardiano":"secondari/guardiano.md",
    "Theron":"secondari/theron.md",
    "Elara":"secondari/elara.md",
    "Castore":"secondari/castore.md",
    "Polluce":"secondari/polluce.md",
    "Luccio":"secondari/luccio.md",
    "Lucas":"secondari/lucas.md",
    "Marcus":"secondari/marcus.md",
    "Druso":"secondari/druso.md",
    "Verdetto":"secondari/verdetto.md",
    "Morte":"secondari/morte.md",
    "JC":"secondari/jc.md",
}

def minimal_secondary(name: str) -> str:
    return character_template.format(
        name=name,
        definizione="Personaggio secondario rilevato nei manoscritti o nel concept lore.",
        identita=f"{name}; dettagli da consolidare.",
        ruolo="Secondario",
        obiettivi="Da verificare sui testi convertiti.",
        conflitti="Da verificare.",
        psicologia="Da verificare.",
        backstory="Da estrarre dai manoscritti.",
        relazioni="Da verificare.",
        evoluzione="Da verificare.",
        voce="Da verificare.",
        capacita="Da verificare.",
        simboli="Da verificare.",
        lore="Voce placeholder per tracciamento canone.",
        stato="Bozza, da verificare",
        aspetto="Da verificare.",
        abbigliamento="Da verificare.",
        oggetti="Da verificare.",
        origine="Da verificare.",
        fazione="Da verificare.",
        momenti="Da verificare.",
        frasi="Da verificare.",
        contraddizioni="Da verificare.",
        alternative="Da definire.",
    )

base = structure / "5-Personaggi"
for rel_path, data in characters.items():
    path = base / rel_path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(character_template.format(**data).strip() + "\n", encoding="utf-8")

for name in secondary_names:
    rel_path = secondary_dir_map[name]
    path = base / rel_path
    if not path.exists():
        path.write_text(minimal_secondary(name), encoding="utf-8")

(base / "relazioni" / "README.md").write_text(
    """# Relazioni Personaggi

## Assi principali
- Bellius <-> Tebris: fratellanza, trauma condiviso, vendetta.
- Spazio <-> Magnus: alleanza tra forza e conoscenza.
- Spazio <-> Honos: scontro tra arma grezza e disciplina superiore.
- Spazio <-> Elara: fiducia rara e prossimita umana.
- Spazio <-> Andoi: anomalia contro sistema.
- Zen <-> Andoi: amicizia tradita e guerra cosmologica.

## Relazioni da verificare
- Spazio <-> Evesor
- Zen <-> Uomo in Rosso
- Guardiano <-> sistema delle Casate
- Morte <-> bastone nella trilogia principale
""",
    encoding="utf-8",
)

(base / "README.md").write_text(
    """# Personaggi

## Struttura
- `protagonisti/` contiene i personaggi portanti della saga e del prequel Zen.
- `antagonisti/` contiene i principali poli di opposizione.
- `secondari/` contiene alleati, entita, nodi episodici e schede preliminari da completare.
- `relazioni/` contiene mappe sintetiche dei legami.

## Nota d'uso
Le schede sono state generate incrociando i tre manoscritti convertiti e il PDF su Zen. Alcuni personaggi minori sono marcati `da verificare` quando le occorrenze non bastano ancora per fissare un profilo canonico pieno.
""",
    encoding="utf-8",
)

coherence = """# Coerenza Lore e Personaggi

## Punti coerenti verificati
- La saga cresce in modo coerente dalla vendetta umana di Bellius e Tebris al conflitto metafisico centrato su Spazio, chiavi, soglia e Andoi.
- Spazio e il perno di continuita piu forte tra i tre manoscritti.
- Andoi e coerente come antagonista sistemico sia nei romanzi sia nel concept su Zen.
- Il Guardiano, le chiavi e la soglia costruiscono una progressione leggibile tra volume 2 e volume 3.

## Ambiguita aperte
- Il legame esplicito tra Zen e l'Uomo in Rosso e dichiarato nel PDF ma non ancora fissato in modo testuale nei tre romanzi convertiti.
- Evesor appare come titolo e come possibile nome/condizione; serve verifica lessicale nei manoscritti per evitare sovrapposizioni improprie.
- Diversi nomi minori del volume 1 richiedono estrazione puntuale prima di essere marcati come pienamente canonici.

## Decisioni operative adottate
- I tre DOCX sono stati convertiti in Markdown per consentire controllo diffuso e citazione interna al workspace.
- Le schede personaggio usano una struttura uniforme e marcano come `da verificare` i casi con evidenza insufficiente.
- Orun va trattato come oggetto piu che come personaggio.

## Prossimi controlli consigliati
- Verifica mirata dei personaggi minori nel volume 1 a partire dal Markdown convertito.
- Creazione delle schede lore e oggetti per bastone della Morte, chiavi, Pax, Tax e soglia.
- Mappa relazionale piu dettagliata tra Bellius, Spazio, Andoi, Zen e Guardiano.
"""
(structure / "3-Progetto" / "coerenza-lore-personaggi.md").write_text(coherence, encoding="utf-8")

print("Done: manuscripts converted and character files generated.")
