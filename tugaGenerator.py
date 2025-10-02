# BairroPump XL
> 200+ multilingual bars of dark sarcasm.  
> Offline. Mobile-ready. Potato-proof.  
> If you wanted kindness, try yoga. If you wanted results, press run.
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#version: '3'

tasks:
  default:
    desc: Run all languages, 240 quotes
    cmds:
      - python bairro_pump_xl.py --lang all --count 240

  lisbon-night:
    desc: Pure Portuguese bairro energy
    cmds:
      - python bairro_pump_xl.py --lang pt-PT --count 220 --seed 7

  london-rain:
    desc: Cold Cockney grind
    cmds:
      - python bairro_pump_xl.py --lang en --count 220 --seed 21

  berlin-steel:
    desc: German precision, no excuses
    cmds:
      - python bairro_pump_xl.py --lang de --count 220 --seed 99

  manila-heat:
    desc: Tagalog fire, playful but sharp
    cmds:
      - python bairro_pump_xl.py --lang tl --count 220 --seed 42

  arabian-dunes:
    desc: Arabic discipline, desert-dry sarcasm
    cmds:
      - python bairro_pump_xl.py --lang ar --count 220 --seed 77

  paris-smoke:
    desc: French cynicism with trap swagger
    cmds:
      - python bairro_pump_xl.py --lang fr --count 220 --seed 55

  madrid-grit:
    desc: Spanish hustle, barrio sarcasm
    cmds:
      - python bairro_pump_xl.py --lang es --count 220 --seed 88

  milano-drip:
    desc: Italian flex, dark sarcasm
    cmds:
      - python bairro_pump_xl.py --lang it --count 220 --seed 66

  moscow-frost:
    desc: Russian cold grind
    cmds:
      - python bairro_pump_xl.py --lang ru --count 220 --seed 33

# BairroPump XL: Offline Dark Sarcasm Motivation Generator
# Languages: pt-PT, es, it, ru, de, en, fr, ar, tl
# Vibe: Cockney London + Angolan trap swagger, dark sarcasm, status-first, no slurs, no targets.
# Usage:
#   python bairro_pump_xl.py --lang all --count 240
#   python bairro_pump_xl.py --lang pt-PT --count 220 --seed 7 --out quotes_pt.txt
#Q: Why is it so mean? A: Because your excuses don’t deserve kindness.

Q: Can it run on my old Android? A: If it can run Snake, it can run this.

Q: Will it make me rich? A: No. But it’ll make you allergic to mediocrity.

# License: MIT

import argparse
import random
import sys

ADLIBS = {
    "en": ["skrrt", "innit", "bruv", "oi", "yeah-yeah", "sheesh", "ayy", "safe"],
    "pt-PT": ["ya", "bro", "wou", "tss", "ya-ya", "ok", "seguro", "calma"],
    "es": ["bro", "vale", "ey", "ok", "wacho", "ayy", "tss"],
    "it": ["oh", "bro", "bella", "vai", "ay", "ok", "tss"],
    "ru": ["эй", "бро", "окей", "ай", "да", "тсс"],
    "de": ["ey", "digga", "jo", "okay", "ayy", "skrrt"],
    "fr": ["wesh", "frérot", "ouais", "hein", "ok", "ayy"],
    "ar": ["يلا", "أيوه", "تمام", "ها", "آي", "أيوووه"],
    "tl": ["oy", "grabe", "ayos", "sige", "tara", "skrrt"]
}

CORE = {
    "en": {
        "nouns": ["discipline", "focus", "hunger", "vision", "patience", "consistency", "momentum", "silence"],
        "verbs": ["stack", "build", "scale", "grind", "execute", "deliver", "commit", "level up"],
        "flex": ["time", "skill", "respect", "results", "reputation", "leverage", "cashflow"]
    },
    "pt-PT": {
        "nouns": ["disciplina", "foco", "fome", "visão", "paciência", "consistência", "ritmo", "silêncio"],
        "verbs": ["empilhar", "construir", "escalar", "moer", "executar", "entregar", "cumprir", "subir de nível"],
        "flex": ["tempo", "skill", "respeito", "resultados", "reputação", "alavanca", "cashflow"]
    },
    "es": {
        "nouns": ["disciplina", "enfoque", "hambre", "visión", "paciencia", "constancia", "ritmo", "silencio"],
        "verbs": ["apilar", "construir", "escalar", "moler", "ejecutar", "entregar", "cumplir", "subir de nivel"],
        "flex": ["tiempo", "habilidad", "respeto", "resultados", "reputación", "apalancamiento", "flujo"]
    },
    "it": {
        "nouns": ["disciplina", "focus", "fame", "visione", "pazienza", "costanza", "slancio", "silenzio"],
        "verbs": ["impilare", "costruire", "scalare", "macinare", "eseguire", "consegnare", "impegnarsi", "livellare"],
        "flex": ["tempo", "skill", "rispetto", "risultati", "reputazione", "leva", "flusso"]
    },
    "ru": {
        "nouns": ["дисциплина", "фокус", "голод", "видение", "терпение", "постоянство", "моментум", "тишина"],
        "verbs": ["накладывать", "строить", "масштабировать", "пахать", "исполнять", "доставлять", "держать слово", "повышать уровень"],
        "flex": ["время", "скилл", "уважение", "результаты", "репутация", "рычаг", "поток"]
    },
    "de": {
        "nouns": ["Disziplin", "Fokus", "Hunger", "Vision", "Geduld", "Konstanz", "Momentum", "Stille"],
        "verbs": ["stapeln", "bauen", "skalieren", "ackern", "liefern", "durchziehen", "committen", "aufsteigen"],
        "flex": ["Zeit", "Skill", "Respekt", "Resultate", "Ruf", "Hebel", "Cashflow"]
    },
    "fr": {
        "nouns": ["discipline", "focus", "faim", "vision", "patience", "constance", "élan", "silence"],
        "verbs": ["empiler", "bâtir", "scaler", "grinder", "exécuter", "livrer", "tenir", "monter de niveau"],
        "flex": ["temps", "skill", "respect", "résultats", "réputation", "levier", "flux"]
    },
    "ar": {
        "nouns": ["انضباط", "تركيز", "جوع", "رؤية", "صبر", "ثبات", "زخم", "صمت"],
        "verbs": ["راكِم", "ابنِ", "وسّع", "اطحن", "نفّذ", "سلّم", "التزم", "ارتقِ"],
        "flex": ["وقت", "مهارة", "احترام", "نتائج", "سمعة", "رافعة", "تدفق"]
    },
    "tl": {
        "nouns": ["disiplina", "pokus", "gana", "bisyon", "tyaga", "konsistensi", "momentum", "katahimikan"],
        "verbs": ["ipon", "tayo", "angat", "giling", "execute", "deliver", "commit", "level up"],
        "flex": ["oras", "skill", "respeto", "bunga", "reputasyon", "leverage", "daloy"]
    }
}

LINES = {
    "en": [
        "Dreams are cute—deadlines pay. {adlib}.",
        "Motivation fades; systems eat. {adlib}.",
        "You don’t need hype; you need reps. {adlib}.",
        "If it’s not scheduled, it’s fiction. {adlib}.",
        "Luxury is a side effect of discipline. {adlib}.",
        "Results > excuses. {adlib}.",
        "Be allergic to average. {adlib}.",
        "Plan like a cynic, execute like a machine. {adlib}.",
        "If it’s easy, it’s crowded. {adlib}.",
        "Your future self is watching—don’t be mid. {adlib}."
    ],
    "pt-PT": [
        "Sonhos são giros—prazos é que pagam. {adlib}.",
        "A motivação passa; o sistema manda. {adlib}.",
        "Não precisas de hype; precisas de reps. {adlib}.",
        "Se não está na agenda, é ficção. {adlib}.",
        "Luxo é efeito da disciplina. {adlib}.",
        "Resultados > desculpas. {adlib}.",
        "Sê alérgico ao mediano. {adlib}.",
        "Planeia como cínico, executa como máquina. {adlib}.",
        "Se é fácil, está lotado. {adlib}.",
        "O teu eu futuro está a ver—não sejas fraquinho. {adlib}."
    ],
    "es": [
        "Los sueños son bonitos—las fechas pagan. {adlib}.",
        "La motivación se va; el sistema manda. {adlib}.",
        "No necesitas hype; necesitas repeticiones. {adlib}.",
        "Si no está agendado, es ficción. {adlib}.",
        "El lujo es efecto de la disciplina. {adlib}.",
        "Resultados > excusas. {adlib}.",
        "Sé alérgico a lo mediocre. {adlib}.",
        "Plan cínico, ejecución máquina. {adlib}.",
        "Si es fácil, está lleno. {adlib}.",
        "Tu futuro te mira—no seas tibio. {adlib}."
    ],
    "it": [
        "I sogni sono carini—le scadenze pagano. {adlib}.",
        "La motivazione svanisce; il sistema regna. {adlib}.",
        "Non ti serve hype; ti servono ripetizioni. {adlib}.",
        "Se non è in agenda, è finzione. {adlib}.",
        "Il lusso è effetto della disciplina. {adlib}.",
        "Risultati > scuse. {adlib}.",
        "Sii allergico al medio. {adlib}.",
        "Pianifica cinico, esegui macchina. {adlib}.",
        "Se è facile, è affollato. {adlib}.",
        "Il tuo futuro ti osserva—non essere tiepido. {adlib}."
    ],
    "ru": [
        "Мечты милые—дедлайны платят. {adlib}.",
        "Мотивация уходит; система ест. {adlib}.",
        "Не нужен хайп; нужны повторы. {adlib}.",
        "Если не в расписании — это фантазия. {adlib}.",
        "Роскошь — побочный эффект дисциплины. {adlib}.",
        "Результаты > оправдания. {adlib}.",
        "Будь аллергичен к среднему. {adlib}.",
        "Планируй цинично, исполняй как машина. {adlib}.",
        "Если легко — там толпа. {adlib}.",
        "Твой будущий ты смотрит — не будь посредственным. {adlib}."
    ],
    "de": [
        "Träume sind nett—Deadlines zahlen. {adlib}.",
        "Motivation vergeht; Systeme fressen. {adlib}.",
        "Kein Hype—Wiederholungen zählen. {adlib}.",
        "Ohne Kalender ist es Fiktion. {adlib}.",
        "Luxus ist Nebenwirkung von Disziplin. {adlib}.",
        "Resultate > Ausreden. {adlib}.",
        "Allergisch gegen Durchschnitt. {adlib}.",
        "Zynisch planen, maschinell liefern. {adlib}.",
        "Wenn’s leicht ist, ist’s voll. {adlib}.",
        "Dein Zukunfts-Ich schaut zu—sei nicht mittelmäßig. {adlib}."
    ],
    "fr": [
        "Les rêves c’est mignon—les deadlines payent. {adlib}.",
        "La motivation passe; le système régit. {adlib}.",
        "Pas besoin de hype; besoin de répétitions. {adlib}.",
        "Si c’est pas planifié, c’est fiction. {adlib}.",
        "Le luxe est un effet de la discipline. {adlib}.",
        "Résultats > excuses. {adlib}.",
        "Allergique au moyen. {adlib}.",
        "Plan cynique, exécution machine. {adlib}.",
        "Si c’est facile, c’est bondé. {adlib}.",
        "Ton futur te regarde—ne sois pas tiède. {adlib}."
    ],
    "ar": [
        "الأحلام لطيفة—المواعيد النهائية هي اللي تدفع. {adlib}.",
        "الحافز يروح؛ النظام يظل. {adlib}.",
        "ما تحتاج ضجيج؛ تحتاج تكرار. {adlib}.",
        "إذا مش مجدول، فهي خيال. {adlib}.",
        "الفخامة أثر الانضباط. {adlib}.",
        "نتائج > أعذار. {adlib}.",
        "كن حساسًا ضد العادي. {adlib}.",
        "خطّط بسخرية، نفّذ كآلة. {adlib}.",
        "لو سهل، المكان مليان. {adlib}.",
        "ذاتك المستقبلية تشاهد—لا تكن متوسطًا. {adlib}."
    ],
    "tl": [
        "Cute ang pangarap—deadline ang nagbabayad. {adlib}.",
        "Nawawala ang motivation; sistema ang matibay. {adlib}.",
        "Di mo kailangan ng hype; kailangan mo ng reps. {adlib}.",
        "Kung wala sa iskedyul, kwento lang. {adlib}.",
        "Luho ay epekto ng disiplina. {adlib}.",
        "Resulta > dahilan. {adlib}.",
        "Allergic sa average. {adlib}.",
        "Planong may duda, execution na makina. {adlib}.",
        "Kung madali, siksikan ‘yan. {adlib}.",
        "Pinapanood ka ng future mo—huwag pa‑easy. {adlib}."
    ]
}

TEMPLATES = {
    "en": [
        "{adlib}. {verb} {flex}, marry {nouns}.",
        "Cold {nouns}, warm wallet. {adlib}.",
        "Respect follows {nouns}, not noise. {adlib}.",
        "No shortcuts, only {nouns} + {verbs}. {adlib}.",
        "Silence the feed, amplify {nouns}. {adlib}."
    ],
    "pt-PT": [
        "{adlib}. {verb} {flex}, casa com {nouns}.",
        "Frio no {nouns}, carteira quente. {adlib}.",
        "O respeito segue {nouns}, não barulho. {adlib}.",
        "Sem atalhos, só {nouns} + {verbs}. {adlib}.",
        "Desliga o feed, amplifica {nouns}. {adlib}."
    ],
    "es": [
        "{adlib}. {verb} {flex}, cásate con {nouns}.",
        "{nouns} frío, cartera caliente. {adlib}.",
        "El respeto sigue a {nouns}, no al ruido. {adlib}.",
        "Sin atajos, solo {nouns} + {verbs}. {adlib}.",
        "Silencia el feed, amplifica {nouns}. {adlib}."
    ],
    "it": [
        "{adlib}. {verb} {flex}, sposa {nouns}.",
        "{nouns} freddo, portafoglio caldo. {adlib}.",
        "Il rispetto segue {nouns}, non il rumore. {adlib}.",
        "Niente scorciatoie, solo {nouns} + {verbs}. {adlib}.",
        "Silenzia il feed, amplifica {nouns}. {adlib}."
    ],
    "ru": [
        "{adlib}. {verb} {flex}, женись на {nouns}.",
        "Холодная {nouns}, горячий кошелек. {adlib}.",
        "Уважение следует за {nouns}, а не за шумом. {adlib}.",
        "Без сокращений, только {nouns} + {verbs}. {adlib}.",
        "Выключи ленту, усиливай {nouns}. {adlib}."
    ],
    "de": [
        "{adlib}. {verb} {flex}, heirate {nouns}.",
        "Kaltes {nouns}, warme Brieftasche. {adlib}.",
        "Respekt folgt {nouns}, nicht Lärm. {adlib}.",
        "Keine Abkürzungen, nur {nouns} + {verbs}. {adlib}.",
        "Feed aus, {nouns} an. {adlib}."
    ],
    "fr": [
        "{adlib}. {verb} {flex}, épouse {nouns}.",
        "{nouns} glacé, portefeuille chaud. {adlib}.",
        "Le respect suit {nouns}, pas le bruit. {adlib}.",
        "Pas de raccourcis, juste {nouns} + {verbs}. {adlib}.",
        "Coupe le feed, booste {nouns}. {adlib}."
    ],
    "ar": [
        "{adlib}. {verb} الـ{flex}، تزوّج الـ{nouns}.",
        "{nouns} بارد، المحفظة حامية. {adlib}.",
        "الاحترام يتبع الـ{nouns}، مش الضوضاء. {adlib}.",
        "لا طرق مختصرة، فقط {nouns} + {verbs}. {adlib}.",
        "اسكت الخلاصة، كبّر الـ{nouns}. {adlib}."
    ],
    "tl": [
        "{adlib}. {verb} ang {flex}, pakasalan ang {nouns}.",
        "Malamig ang {nouns}, mainit ang bulsa. {adlib}.",
        "Respeto ay sumusunod sa {nouns}, hindi sa ingay. {adlib}.",
        "Walang shortcut, puro {nouns} + {verbs}. {adlib}.",
        "Mute ang feed, boost ang {nouns}. {adlib}."
    ]
}

def gen_quote(lang: str, rng: random.Random) -> str:
    adlib = rng.choice(ADLIBS[lang])
    # 60/40 split between written lines and templates
    if rng.random() < 0.6:
        base = rng.choice(LINES[lang])
        return base.format(adlib=adlib)
    core = CORE[lang]
    base = rng.choice(TEMPLATES[lang])
    return base.format(
        adlib=adlib,
        nouns=rng.choice(core["nouns"]),
        verbs=rng.choice(core["verbs"]),
        verb=rng.choice(core["verbs"]),
        flex=rng.choice(core["flex"])
    )

def gen_many(lang: str, count: int, seed: int | None = None):
    rng = random.Random(seed)
    quotes = []
    langs = ["pt-PT", "es", "it", "ru", "de", "en", "fr", "ar", "tl"] if lang == "all" else [lang]
    for _ in range(count):
        L = rng.choice(langs)
        quotes.append((L, gen_quote(L, rng)))
    return quotes

def print_quotes(quotes, out_file=None):
    tagmap = {"pt-PT": "[PT]", "es": "[ES]", "it": "[IT]", "ru": "[RU]", "de": "[DE]", "en": "[EN]", "fr": "[FR]", "ar": "[AR]", "tl": "[TL]"}
    lines = []
    for i, (lang, q) in enumerate(quotes, 1):
        tag = tagmap[lang]
        lines.append(f"{i:03d} {tag} {q}")
    data = "\n".join(lines)
    if out_file:
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(data + "\n")
    else:
        print(data)

def parse_args(argv):
    p = argparse.ArgumentParser(description="BairroPump XL: Offline Dark Sarcasm Motivation Generator")
    p.add_argument("--lang", default="all",
                   choices=["pt-PT", "es", "it", "ru", "de", "en", "fr", "ar", "tl", "all"],
                   help="Language or 'all'")
    p.add_argument("--count", type=int, default=240, help="Number of quotes to generate (>= 200)")
    p.add_argument("--seed", type=int, default=None, help="Random seed for reproducibility")
    p.add_argument("--out", type=str, default=None, help="Optional output file path")
    return p.parse_args(argv)

def main():
    args = parse_args(sys.argv[1:])
    if args.count < 1:
        print("Count must be >= 1", file=sys.stderr)
        sys.exit(1)
    quotes = gen_many(args.lang, args.count, args.seed)
    print_quotes(quotes, args.out)

if __name__ == "__main__":
    main()
