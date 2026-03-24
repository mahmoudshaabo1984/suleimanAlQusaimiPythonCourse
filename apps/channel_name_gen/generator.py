import random
from typing import List, Tuple


def default_wordlists(lang: str = "ar") -> Tuple[List[str], List[str], List[str]]:
    if lang == "ar":
        adjectives = [
            "مبدع",
            "سريع",
            "ذهبي",
            "رائع",
            "عملاق",
            "مثير",
            "ذكي",
            "نقي",
            "عالي",
            "فريد",
        ]
        nouns = [
            "تقنية",
            "ميديا",
            "ألعاب",
            "علوم",
            "طبخ",
            "سفر",
            "رياضة",
            "تعليم",
            "ترفيه",
            "فن",
        ]
        themes = [
            "ستوديو",
            "عالم",
            "محطة",
            "تيڤي",
            "لايف",
            "هاوس",
            "سنتر",
            "بود",
        ]
    else:
        adjectives = [
            "smart",
            "rapid",
            "golden",
            "epic",
            "mega",
            "prime",
            "vivid",
            "nova",
            "alpha",
            "urban",
        ]
        nouns = [
            "tech",
            "media",
            "games",
            "science",
            "cooking",
            "travel",
            "sports",
            "learning",
            "entertainment",
            "art",
        ]
        themes = [
            "studio",
            "world",
            "station",
            "tv",
            "live",
            "house",
            "center",
            "pod",
        ]
    return adjectives, nouns, themes


def apply_style(words: List[str], style: str) -> str:
    clean = [w.replace(" ", "") for w in words if w]
    if style == "kebab":
        return "-".join(clean).lower()
    if style == "snake":
        return "_".join(clean).lower()
    if style == "camel":
        first = clean[0].lower() if clean else ""
        rest = "".join(w.capitalize() for w in clean[1:])
        return first + rest
    return " ".join(words)


def generate_name(
    lang: str = "ar",
    style: str = "kebab",
    include_number: bool = False,
    rng: random.Random | None = None,
) -> str:
    if rng is None:
        rng = random
    adjectives, nouns, themes = default_wordlists(lang)
    a = rng.choice(adjectives)
    n = rng.choice(nouns)
    use_theme = rng.random() < 0.7
    t = rng.choice(themes) if use_theme else ""
    words = [a, n, t] if t else [a, n]
    name = apply_style(words, style)
    if include_number:
        num = rng.randint(1, 999)
        if style in ("kebab", "snake"):
            sep = "-" if style == "kebab" else "_"
            name = f"{name}{sep}{num}"
        elif style == "camel":
            name = f"{name}{num}"
        else:
            name = f"{name} {num}"
    return name


def generate_batch(count: int = 10, **kwargs) -> List[str]:
    seen: set[str] = set()
    out: List[str] = []
    attempts = 0
    while len(out) < count and attempts < count * 20:
        attempts += 1
        name = generate_name(**kwargs)
        if name not in seen:
            seen.add(name)
            out.append(name)
    return out

