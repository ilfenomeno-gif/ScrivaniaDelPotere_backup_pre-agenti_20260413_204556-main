from pathlib import Path

root = Path(r"c:/Users/PC/Downloads/bellius-libro-main/bellius-libro-main")
base = root / "bellius-libro-structure" / "5-Personaggi" / "secondari"

TEMPLATE = """# {name}

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

profiles = {
    "druso.md": dict(
        name="Druso",
        definizione="Campione d'arena nel volume 1, usato per mostrare la soglia di potenza di Spazio.",
        identita="Druso; gladiatore veterano; corpo segnato da cicatrici.",
        ruolo="Antagonista episodico di prova.",
        obiettivi="Vincere nell'arena e mantenere il proprio dominio.",
        conflitti="Scontro diretto con Spazio, che lo supera in lettura e precisione.",
        psicologia="Feroce e abituato al controllo del combattimento fino alla rottura del proprio schema.",
        backstory="Presentato come figura amata dalla folla e temprata da anni di arena.",
        relazioni="Spazio (avversario); folla dell'arena.",
        evoluzione="Arco breve e chiuso: da predatore del ring a segnale del cambio di scala.",
        voce="Non emergono battute dominanti; la caratterizzazione e soprattutto fisica.",
        capacita="Forza e impatto; limite: prevedibilita tecnica contro un avversario adattivo.",
        simboli="Violenza ritualizzata dell'arena; fine del paradigma umano puro.",
        lore="Evidenze: bellius-libro-1.md:583, bellius-libro-1.md:587, bellius-libro-1.md:609.",
        stato="Canonico",
        aspetto="Largo, cicatrici diffuse, presenza intimidatoria.",
        abbigliamento="Da arena.",
        oggetti="Armi da arena.",
        origine="Da verificare.",
        fazione="Circuito arena.",
        momenti="Ingresso in arena; perdita del controllo tecnico; decapitazione.",
        frasi="Nessuna frase cardine conservata.",
        contraddizioni="Nessuna rilevante: personaggio funzionale e coerente.",
        alternative="Riusi solo in flashback o parallelismi simbolici.",
    ),
    "lucas.md": dict(
        name="Lucas",
        definizione="Contatto del passato di Bellius e Tebris, nodo di memoria e protezione.",
        identita="Lucas; uomo; legato a Giulia.",
        ruolo="Secondario di raccordo nel primo volume.",
        obiettivi="Aiutare Bellius e Tebris nonostante il rischio.",
        conflitti="Rischio personale dovuto al supporto fornito ai protagonisti.",
        psicologia="Stanco ma capace di riaccendersi nel riconoscimento.",
        backstory="Conosce i protagonisti da prima degli eventi correnti.",
        relazioni="Bellius, Tebris, Giulia.",
        evoluzione="Non ha arco autonomo lungo; resta presidio umano del passato.",
        voce="Essenziale e pragmatica.",
        capacita="Memoria della rete locale e supporto logistico; limite: esposizione al pericolo.",
        simboli="Casa, fiducia, continuita tra trauma e presente.",
        lore="Evidenze: bellius-libro-1.md:157, bellius-libro-1.md:159, bellius-libro-1.md:177.",
        stato="Canonico",
        aspetto="Più vecchio e consumato dal tempo.",
        abbigliamento="Da contesto urbano domestico.",
        oggetti="Non rilevati.",
        origine="Pompei/area rete locale, da confermare.",
        fazione="Rete contatti umani di Bellius e Tebris.",
        momenti="Riconoscimento all'ingresso; ospitalita condivisa con Giulia.",
        frasi='"Lucas. Siamo Bellius e Tebris. Ricordi?"',
        contraddizioni="Nessuna maggiore; ruolo episodico ma chiaro.",
        alternative="Espansione in dossier rete contatti del volume 1.",
    ),
    "marcus.md": dict(
        name="Marcus",
        definizione="Leader pragmatico dei ribelli, interpreta Bellius e Tebris come catalizzatori.",
        identita="Marcus; uomo; legato alla linea di Ostia/ribelli.",
        ruolo="Secondario politico-strategico nel volume 1.",
        obiettivi="Usare ogni risorsa utile alla rivolta senza romanticismo.",
        conflitti="Tensione tra fiducia e strumentalita verso i protagonisti.",
        psicologia="Analitico, prudente, orientato al risultato.",
        backstory="Appare come guida locale capace di leggere rapidamente il valore delle persone.",
        relazioni="Bellius, Tebris, rete ribelle.",
        evoluzione="Da incontro a riferimento ricorrente nei passaggi cruciali.",
        voce="Misurata e selettiva.",
        capacita="Leadership pragmatica, lettura del rischio; limiti non ancora espansi.",
        simboli="Politica concreta della rivolta.",
        lore="Evidenze: bellius-libro-1.md:197, bellius-libro-1.md:201, bellius-libro-1.md:207, bellius-libro-1.md:295.",
        stato="Canonico",
        aspetto="Non dettagliato in modo completo.",
        abbigliamento="Da contesto clandestino/ribelle.",
        oggetti="Non rilevati.",
        origine="Da verificare.",
        fazione="Ribelli.",
        momenti="Presentazione; valutazione dei protagonisti; ricomparse operative.",
        frasi='"Mi chiamo Marcus. E voi?"',
        contraddizioni="Da chiarire estensione del suo ruolo oltre il volume 1.",
        alternative="Nodo centrale nella mappa politico-terrestre pre-divina.",
    ),
    "elara.md": dict(
        name="Elara",
        definizione="Figura di prossimita affettiva e intellettuale che interrompe l'isolamento di Spazio.",
        identita="Elara; traduttrice dei mercanti del porto; lettrice poliglotta.",
        ruolo="Secondario emotivo ad alto impatto.",
        obiettivi="Vivere e lavorare mantenendo autonomia e lucidita.",
        conflitti="Diventa vulnerabile al contesto violento che circonda Spazio.",
        psicologia="Diretta senza crudelta, gentile senza debolezza.",
        backstory="Incontro a Parma; costruisce fiducia senza forzare confessioni.",
        relazioni="Spazio; cacciatori di taglie (evento traumatico).",
        evoluzione="Da spazio di cura a perdita che segna l'identita di Spazio.",
        voce="Calma, non invasiva, precisa.",
        capacita="Linguistica, osservazione, stabilita relazionale; limite: esposizione al conflitto armato.",
        simboli="Sguardo non giudicante, umanita, perdita.",
        lore="Evidenze: bellius-libro-1.md:815, bellius-libro-1.md:821, bellius-libro-1.md:849, bellius-libro-3.md:101.",
        stato="Canonico",
        aspetto="Non fissato in dettagli rigidi.",
        abbigliamento="Da vita urbana/portuale.",
        oggetti="Libro personale ricorrente.",
        origine="Parma come luogo cardine di apparizione.",
        fazione="Indipendente.",
        momenti="Presentazione al fuoco; scena della maschera; aggressione dei cacciatori.",
        frasi="Nessuna formula unica canonizzata nei dossier.",
        contraddizioni="Da fissare esattamente il suo destino finale nel canone di lavoro.",
        alternative="Riapparizione memoriale o archivio testuale indiretto.",
    ),
    "theron.md": dict(
        name="Theron",
        definizione="Identita usata come copertura operativa; nel volume 2 si chiarisce che e legata all'azione di Magnus.",
        identita="Theron; figura informativa/operativa; status reale ambiguo dopo la rivelazione su Magnus.",
        ruolo="Snodo di transizione tra indagine urbana e arco superiore.",
        obiettivi="Fornire accessi, piste e movimentazione tattica (copertura).",
        conflitti="Conflitto principale: ambiguita identitaria tra persona reale e impersonificazione.",
        psicologia="Nel volume 1 appare efficiente e misurato; nel volume 2 il ruolo viene riframmato.",
        backstory="Spazio lo aggancia in taverna; nel volume 2 emerge che Magnus si e fatto passare per Theron in varie fasi.",
        relazioni="Spazio, Magnus, Castore, Polluce.",
        evoluzione="Da contatto credibile a elemento di twist identitario.",
        voce="Poche parole, taglio professionale.",
        capacita="Rete contatti e operazioni; limite: affidabilita dipendente dall'identita effettiva in scena.",
        simboli="Maschera sociale, depistaggio, funzionalita.",
        lore="Evidenze: bellius-libro-1.md:907, bellius-libro-1.md:925, bellius-libro-2.md:717, bellius-libro-2.md:809.",
        stato="Canonico con verifica in corso",
        aspetto="Varia per natura della copertura.",
        abbigliamento="Da strada/operativo.",
        oggetti="Pergamene e dati di posizione.",
        origine="Da verificare.",
        fazione="Copertura mobile.",
        momenti="Arruolamento in taverna; supporto operativo; rivelazione legata a Magnus.",
        frasi='"I segreti sono sempre piu redditizi."',
        contraddizioni="Va deciso nel canone se Theron esiste come personaggio autonomo o quasi solo come identita coperta.",
        alternative="Scissione in due schede: Theron reale e Theron-copertura.",
    ),
    "magnus.md": dict(
        name="Magnus",
        definizione="Figura cardine della linea conoscitiva: scrittore, cartografo umano e poi anomalia non classificabile.",
        identita="Magnus; inizialmente scrittore anziano; successivamente entita trasformata dal Libro dei Morti.",
        ruolo="Alleato strategico e intellettuale di Spazio.",
        obiettivi="Decifrare sistemi, mappe e registri; rendere attaccabile il cuore del sistema di Andoi.",
        conflitti="Mutazione progressiva, status ontologico incerto, pressione del regno divino.",
        psicologia="Freddo, preciso, capace di pianificazione lunga.",
        backstory="Viene cercato come scrittore derubato; legge la pietra a Tignes; apre il Libro dei Morti e cambia natura.",
        relazioni="Spazio, Honos, Ignis, Andoi; contatto con Castore/Polluce in volume 3.",
        evoluzione="Da vecchio scrittore a variabile fuori categoria (neppure Andoi lo classifica pienamente).",
        voce="Didattica, asciutta, spesso un passo avanti nella lettura dei fatti.",
        capacita="Lettura di sistemi non ordinari, pianificazione, metamorfosi parziale; limite: costo fisico e instabilita.",
        simboli="Conoscenza come arma, mappa, forma che cambia.",
        lore="Evidenze: bellius-libro-1.md:967, bellius-libro-1.md:987, bellius-libro-1.md:1279, bellius-libro-1.md:1773, bellius-libro-3.md:137.",
        stato="Canonico",
        aspetto="Da anziano scrittore a figura in tuta scura con occhi bianchi e maschera blu.",
        abbigliamento="Prima da scrittore/viaggio, poi equipaggiamento scuro.",
        oggetti="Mappe, pergamene, registri, strumenti di scrittura.",
        origine="Torino come nodo iniziale di aggancio.",
        fazione="Asse Spazio; poi indipendente ma convergente.",
        momenti="Scoperta cripta; apertura Libro; contenimento nel regno; piano sul registro; mappa nel volume 3.",
        frasi='"Io sono il piano. Tu sei l\'esecuzione."',
        contraddizioni="Da pulire il confine tra Magnus-persona, Magnus-trasformato e i suoi alias operativi.",
        alternative="Diventare archivista permanente del nuovo ordine post-Andoi.",
    ),
    "honos.md": dict(
        name="Honos",
        definizione="Entita guerriera del regno divino: da antagonista formativo a alleato contro Andoi.",
        identita="Honos; dio/entita legata alla disciplina del combattimento e alla struttura del sistema.",
        ruolo="Secondario maggiore con impatto su climax.",
        obiettivi="Prima: contenere e giudicare Spazio. Poi: rompere il sistema che lo ha usato.",
        conflitti="Lealta storica al sistema contro verita del tradimento di Andoi.",
        psicologia="Controllato, rigoroso, capace di revisione quando la prova e incontrovertibile.",
        backstory="Si presenta in duello a Siena; scopre di essere stato strumentalizzato nella macchina di Andoi.",
        relazioni="Spazio, Ignis, Andoi, Magnus.",
        evoluzione="Da avversario superiore a co-combattente nel confronto finale.",
        voce="Piana, non teatrale, fortemente assertiva.",
        capacita="Tecnica millenaria, pressione divina, lettura tattica; limite: vincoli del sistema e feribilita.",
        simboli="Disciplina, onore, scelta morale tardiva ma decisiva.",
        lore="Evidenze: bellius-libro-1.md:671, bellius-libro-1.md:1487, bellius-libro-1.md:1765, bellius-libro-3.md:269, bellius-libro-3.md:609.",
        stato="Canonico",
        aspetto="Presenza solida; nel volume 3 ricorrono cicatrice al sopracciglio e postura di attesa.",
        abbigliamento="Da entita guerriera del regno.",
        oggetti="Arsenale non sempre esplicitato; combatte anche a mani/forza di principio.",
        origine="Regno divino.",
        fazione="Prima sistema Andoi, poi asse anti-Andoi.",
        momenti="Duello con Spazio; confessione del tradimento sistemico; alleanza nel finale.",
        frasi='"Sei potente, Spazio. Ma sei un\'arma grezza."',
        contraddizioni="Da fissare con precisione il perimetro della sua responsabilita nelle azioni passate.",
        alternative="Custode del nuovo equilibrio o autoesilio punitivo.",
    ),
    "ignis.md": dict(
        name="Ignis",
        definizione="Entita di fuoco: in conflitto con Honos, poi variabile critica nella rottura del sistema.",
        identita="Ignis; entita ignea del regno divino.",
        ruolo="Secondario maggiore, snodo del conflitto tra ordine e impulso.",
        obiettivi="Difendere un ordine comprensibile, poi ridefinire il proprio ruolo dopo la caduta di Andoi.",
        conflitti="Conflitto con Honos; manipolazione da parte di Andoi; paura del caos.",
        psicologia="Reattivo, ardente, ma capace di disciplina in punti decisivi.",
        backstory="Emerge dalla cripta legata al Libro; viene richiamato da Honos; coinvolto nella sentenza di Andoi.",
        relazioni="Honos, Spazio, Magnus, Andoi.",
        evoluzione="Da forza imprevedibile a presenza che apre un varco (volume 3) e poi cambia direzione.",
        voce="Tagliente, breve, ironia secca.",
        capacita="Potenza ignea elevata; limite: oscillazione tra istinto e controllo.",
        simboli="Fuoco, reazione, rischio di distruzione senza direzione.",
        lore="Evidenze: bellius-libro-1.md:1019, bellius-libro-1.md:1769, bellius-libro-3.md:333, bellius-libro-3.md:349, bellius-libro-3.md:383.",
        stato="Canonico",
        aspetto="Occhi fiammeggianti; presenza luminosa e instabile.",
        abbigliamento="Non descritto in modo stabile.",
        oggetti="Nessuno rilevante; il fuoco e gia arma/funzione.",
        origine="Regno divino.",
        fazione="Asse Honos-Ignis, poi biforcazione nelle scelte.",
        momenti="Risveglio in cripta; sentenza alla Terra; confronto con Honos nel volume 3.",
        frasi='"Stavo dormendo abbastanza bene..."',
        contraddizioni="Da consolidare la sequenza precisa dei passaggi tra opposizione e apertura.",
        alternative="Custode del fuoco non punitivo nel nuovo ordine.",
    ),
    "guardiano.md": dict(
        name="Guardiano",
        definizione="Custode delle chiavi e della soglia, inizialmente voce senza forma poi presenza quasi completa.",
        identita="Guardiano; entita liminale legata al confine tra piani.",
        ruolo="Secondario strutturale di altissimo peso.",
        obiettivi="Tenere le chiavi fuori dal controllo di Andoi e consegnare conoscenza selettiva.",
        conflitti="Presenza parziale, manifestazione progressiva, intervento indiretto.",
        psicologia="Misurato, stanco, selettivo.",
        backstory="Nel volume 2 parla prima di avere forma, poi guida alla logica delle sette chiavi.",
        relazioni="Spazio, Magnus, Andoi, sistema delle Casate.",
        evoluzione="Da eco liminale a figura quasi completa, poi assenza operativa lasciando biblioteca/testamento.",
        voce="Didascalica ma non onnisciente; interroga prima di concedere.",
        capacita="Accesso ai luoghi non posizionali, custodia chiavi, mediazione di soglia; limite: non puo (o non vuole) risolvere al posto degli altri.",
        simboli="Soglia, custodia, memoria del sistema.",
        lore="Evidenze: bellius-libro-2.md:801, bellius-libro-2.md:1271, bellius-libro-2.md:1575, bellius-libro-3.md:29, bellius-libro-3.md:397.",
        stato="Canonico",
        aspetto="Da assente a forma quasi completa.",
        abbigliamento="Non applicabile.",
        oggetti="Chiavi (in custodia logica, non proprieta personale classica).",
        origine="Zona liminale tra piano terrestre e regno divino.",
        fazione="Custodia indipendente.",
        momenti="Capitoli centrali volume 2; trasmissione sulle chiavi; testamento bibliotecario in volume 3.",
        frasi='"Le sette."',
        contraddizioni="Da definire in canone se sia singola entita o funzione ereditabile.",
        alternative="Scomparsa definitiva dopo compimento della soglia.",
    ),
    "castore.md": dict(
        name="Castore",
        definizione="Membro della coppia Castore-Polluce: pratico, rumoroso, ma con fratture intime decisive.",
        identita="Castore; fratello/partner operativo di Polluce; profilo da strada e scasso.",
        ruolo="Secondario dinamico nel volume 2 e ponte in volume 3.",
        obiettivi="Trovare Orun, estinguere debiti, uscire dal ciclo di rischi.",
        conflitti="Debito/opacita verso il gruppo; conflitto tra sopravvivenza e lealta.",
        psicologia="Verbale, ironico, nervoso; nasconde dolore e memoria personale (Aria, giardino).",
        backstory="Recluta Spazio per Orun; si rivela implicato in accordi antecedenti all'incontro.",
        relazioni="Polluce, Spazio, Magnus/Theron.",
        evoluzione="Da opportunista a figura stanca che collabora nel passaggio finale (foglio rubato in volume 3).",
        voce="Sarcastica, rapida, difensiva.",
        capacita="Lockpicking, adattamento urbano, negoziazione sporca; limite: pressione emotiva e fiducia instabile.",
        simboli="Sopravvivenza, debito, fragilita sotto rumorosita.",
        lore="Evidenze: bellius-libro-2.md:627, bellius-libro-2.md:947, bellius-libro-2.md:1375, bellius-libro-3.md:157.",
        stato="Canonico",
        aspetto="Profilo fisico agile da strada, dettagli completi non fissati.",
        abbigliamento="Pratico, urbano.",
        oggetti="Attrezzi da scasso; foglio rubato (volume 3).",
        origine="Da verificare.",
        fazione="Coppia Castore-Polluce, poi convergenza con asse Spazio.",
        momenti="Caccia a Luccio; crepa personale; rivelazione dell'accordo; consegna foglio rubato.",
        frasi='"Speriamo che Orun valga il rischio."',
        contraddizioni="Da chiarire se il tradimento iniziale sia solo costrizione da debito o scelta piena.",
        alternative="Redenzione completa o caduta tardiva per vecchi debiti.",
    ),
    "polluce.md": dict(
        name="Polluce",
        definizione="Compagno di Castore, silenzioso e calcolatore, con un passato di debito che guida molte scelte.",
        identita="Polluce; partner di Castore; profilo basso e osservativo.",
        ruolo="Secondario tattico e portatore di segreto.",
        obiettivi="Estinguere un debito pregresso e sopravvivere.",
        conflitti="Lealta verso Castore/gruppo contro vincolo verso forze esterne.",
        psicologia="Misurato, trattenuto, ipervigile; paura specifica dei luoghi bui dopo Milano.",
        backstory="Ha una storia precedente a Castore non condivisa interamente.",
        relazioni="Castore, Spazio, Magnus, figura-creditore anonima.",
        evoluzione="Da ombra tattica a nodo di verita quando emerge il debito.",
        voce="Poche parole, ad alta densita informativa.",
        capacita="Valutazione del rischio e invisibilita pratica; limite: ricattabilita storica.",
        simboli="Debito, silenzio, paura non nominata.",
        lore="Evidenze: bellius-libro-2.md:633, bellius-libro-2.md:1025, bellius-libro-2.md:1059, bellius-libro-2.md:1377.",
        stato="Canonico",
        aspetto="Basso profilo; segni da rissa nel volume 2.",
        abbigliamento="Da strada.",
        oggetti="Non stabilizzati.",
        origine="Da verificare.",
        fazione="Coppia Castore-Polluce.",
        momenti="Rissa da Luccio; incontro a Milano; rivelazione del debito.",
        frasi='"Forse esca..."',
        contraddizioni="Da definire quanto abbia agito per costrizione rispetto a volonta autonoma.",
        alternative="Riparazione piena o uscita laterale dal conflitto principale.",
    ),
    "luccio.md": dict(
        name="Luccio",
        definizione="Contatto criminale del volume 2, nodo episodico per recupero frammenti/libri.",
        identita="Luccio; figura di sottobosco urbano.",
        ruolo="Secondario episodico funzionale.",
        obiettivi="Evitare cattura e difendere il proprio bottino informativo/materiale.",
        conflitti="Braccato da Spazio, Castore e Polluce.",
        psicologia="Pauroso sotto pressione diretta.",
        backstory="Si nasconde in locale opaco; viene raggiunto nella sequenza 'Caccia a Luccio'.",
        relazioni="Castore, Polluce, Spazio.",
        evoluzione="Chiude la sua funzione con la consegna forzata del materiale.",
        voce="Balbetta in condizioni di minaccia.",
        capacita="Reti minori e occultamento; limite: crollo sotto forza immediata.",
        simboli="Sottobosco informativo del volume 2.",
        lore="Evidenze: bellius-libro-2.md:639, bellius-libro-2.md:645, bellius-libro-2.md:659, bellius-libro-2.md:663.",
        stato="Canonico",
        aspetto="Viso alterato dalla paura nel confronto.",
        abbigliamento="Da strada.",
        oggetti="Bagaglio con frammento e libri.",
        origine="Da verificare.",
        fazione="Reti criminali locali.",
        momenti="Localizzazione, rissa, cattura, recupero materiale.",
        frasi="Nessuna formula iconica stabile.",
        contraddizioni="Nessuna rilevante.",
        alternative="Rientro come contatto minore o nota di dossier.",
    ),
}

for filename, data in profiles.items():
    path = base / filename
    path.write_text(TEMPLATE.format(**data).strip() + "\n", encoding="utf-8")

print(f"Updated {len(profiles)} secondary character files.")
