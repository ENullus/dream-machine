"""
Mega description system for Society Dream Machine.

Covers all 66 VAE variables organised into 9 thematic sections.
Each section has a describe_*() function that reads its variables from the
society dict, picks from randomised template pools, and returns a short
paragraph.  Variables absent from the dict are silently skipped so the same
code works for both the full 66-variable VAE path and the 16-variable dials
path.
"""

import random

# ── helpers ──────────────────────────────────────────────────────────────────

def _get(society, key, default=None):
    """Return int-cast value if present, else *default*."""
    v = society.get(key)
    if v is None:
        return default
    try:
        return int(round(float(v)))
    except (TypeError, ValueError):
        return default


def _getf(society, key):
    """Return float value or None."""
    v = society.get(key)
    if v is None:
        return None
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def _pick(templates, code, fallback=""):
    """Pick a random template for *code* from a {code: [str, …]} dict."""
    if code is not None and code in templates:
        return random.choice(templates[code])
    return fallback

# ═══════════════════════════════════════════════════════════════════════════════
# 1. ECONOMY
# ═══════════════════════════════════════════════════════════════════════════════

INTENSITY_WORDS = {
    "none": ["virtually no", "no meaningful"],
    "low":  ["a small share of", "a minor part of", "a modest portion of"],
    "med":  ["a solid share of", "a meaningful portion of", "a balanced part of"],
    "high": ["the bulk of", "the lion's share of", "a dominant share of", "most of"],
}

RESOURCE_TYPES = {
    "gathering":   ["wild tubers", "nuts and seeds", "seasonal fruits", "edible grasses", "wild berries"],
    "hunting":     ["large game", "small mammals", "seasonal herds", "birds", "forest game"],
    "fishing":     ["river fish", "lake fish", "shellfish", "coastal fish", "seasonal runs"],
    "herding":     ["cattle", "goats", "sheep", "mixed herds", "camelids"],
    "agriculture": ["grain crops", "root crops", "mixed gardens", "irrigated fields", "terraced plots"],
}

SUB_TEMPLATES = {
    "gathering": [
        "Gathering accounts for {intensity} the food supply, with {resource} especially important.",
        "Foraging — mostly {resource} — makes up {intensity} the diet.",
        "Wild plant foods like {resource} are collected regularly, providing {intensity} what people eat.",
    ],
    "hunting": [
        "Hunting provides {intensity} the diet, with {resource} most often taken.",
        "People pursue {resource} for {intensity} their food.",
        "Wild game, especially {resource}, remains significant.",
    ],
    "fishing": [
        "Fishing contributes {intensity} the food base, focused on {resource}.",
        "Aquatic harvests of {resource} account for {intensity} the diet.",
        "People rely on {resource} from nearby waters for {intensity} their sustenance.",
    ],
    "herding": [
        "Herding supplies {intensity} the livelihood, especially {resource}.",
        "Pastoral work with {resource} accounts for {intensity} the economy.",
        "Livestock — mainly {resource} — anchor daily routines.",
    ],
    "agriculture": [
        "Agriculture provides {intensity} the food base, focused on {resource}.",
        "Farming — especially {resource} — accounts for {intensity} the diet.",
        "Cultivated {resource} form the core of the agricultural economy.",
    ],
}

SUB_KEYS = [
    ("EA001", "gathering"),
    ("EA002", "hunting"),
    ("EA003", "fishing"),
    ("EA004", "herding"),
    ("EA005", "agriculture"),
]

AG_INTENSITY = {
    1: ["There is no agriculture at all.",
        "Cultivation is entirely absent."],
    2: ["Agriculture is casual and opportunistic.",
        "Some planting occurs but it is haphazard and minor."],
    3: ["Farming follows an extensive or shifting pattern, with fields rotated over time.",
        "Cultivation is extensive, with plots cleared, used, and then left fallow."],
    4: ["Horticulture — semi-intensive garden and grove work — defines the farming system.",
        "Gardens and small groves are tended carefully in a horticultural pattern."],
    5: ["Agriculture is intensive, with permanent fields, fertilisation, and crop rotation.",
        "Permanent fields are cultivated intensively with careful land management."],
    6: ["Intensive irrigated agriculture dominates, with canal or terrace systems.",
        "Irrigation infrastructure supports a highly intensive farming system."],
}

CROP_TYPE = {
    1: ["No crops are cultivated."],
    2: ["The main crops are non-food plants like cotton or tobacco."],
    3: ["Vegetables — cucurbits, greens, legumes — are the primary crops.",
        "Garden vegetables form the main cultivated harvest."],
    4: ["Tree fruits such as bananas, breadfruit, or coconut are the staple crop.",
        "Fruit-bearing trees dominate the cultivated landscape."],
    5: ["Root crops and tubers — manioc, yams, taro, or potatoes — are the staple.",
        "The staple harvest comes from root crops like yams or manioc."],
    6: ["Cereal grains — maize, millet, rice, or wheat — are the primary crop.",
        "Grain agriculture provides the dietary foundation."],
}

PLOW = {
    1: ["The plow is unknown here; all cultivation is done by hand.",
        "No plow or draft animals are used in farming."],
    2: ["The plow was introduced externally and is now well established.",
        "Plow agriculture arrived from outside but has taken firm root."],
    3: ["Plow cultivation has deep indigenous roots.",
        "The plow has been used here since before outside contact."],
}

ANIMAL_HUSBANDRY = {
    1: ["Domestic animals are nearly absent beyond dogs or fowl.",
        "There are almost no economically significant domestic animals."],
    2: ["Pigs are the primary domestic animal.",
        "Pig-keeping is the main form of animal husbandry."],
    3: ["Sheep and goats are the most important livestock.",
        "Small ruminants — sheep or goats — dominate the herds."],
    4: ["Horses or donkeys are the primary domestic animals.",
        "Equines play a central role in animal husbandry."],
    5: ["Reindeer are the main herded animal.",
        "Reindeer herding shapes the pastoral economy."],
    6: ["Camels, llamas, or alpacas are the most important herd animals.",
        "Camelids anchor the pastoral economy."],
    7: ["Cattle, water buffalo, or yak are the dominant livestock.",
        "Bovine animals are at the centre of animal husbandry."],
}

MILKING = {
    1: ["Milking of domestic animals is absent or negligible.",
        "People do not milk their livestock in any regular way."],
    2: ["Domestic animals are milked regularly, and dairy is part of the diet.",
        "Milking is a routine practice that supplements the food supply."],
}

DOM_SUBSISTENCE = {
    1: ["Overall, gathering contributes more than any other activity.",
        "The economy is primarily a foraging one."],
    2: ["Fishing is the single most important food source.",
        "Aquatic resources dominate the subsistence economy."],
    3: ["Hunting provides the largest share of food.",
        "The economy is anchored by hunting."],
    4: ["Pastoralism is the dominant subsistence activity.",
        "Herding outweighs all other food-getting strategies."],
    5: ["Casual agriculture is the main livelihood.",
        "Light farming contributes the most to subsistence."],
    6: ["Extensive agriculture is the economic backbone.",
        "Shifting or extensive cultivation supports most of the population."],
    7: ["Intensive agriculture drives the economy.",
        "Permanent, intensive farming underpins daily life."],
    8: ["No single activity dominates; two or more contribute roughly equally.",
        "The subsistence economy is diversified, with no one activity dominant."],
    9: ["Agriculture of an unspecified type is the primary livelihood.",
        "Farming is dominant but its specific form is unclear."],
}


def _intensity_word(val):
    if val is None:
        return None
    if val <= 0:
        return "none"
    if val <= 3:
        return "low"
    if val <= 6:
        return "med"
    return "high"


def describe_economy(society):
    """Build economy paragraph with interaction-aware logic.

    EA042 (dominant subsistence) is the authority — it frames the opening.
    EA028 (ag intensity) gates all agriculture detail: if EA028 == 1 we
    suppress agriculture percentages, crop type, and plow even if EA005
    is high (the VAE sometimes produces contradictory combos).
    Only the top 2 non-zero subsistence activities are described to avoid
    a laundry-list feel.
    """
    parts = []

    # ── 1. Lead with dominant subsistence (EA042) ──
    dom = _get(society, "EA042")
    if dom is not None:
        parts.append(_pick(DOM_SUBSISTENCE, dom))

    # Map dominant subsistence code → subsistence key to avoid redundancy
    DOM_TO_KEY = {1: "gathering", 2: "fishing", 3: "hunting", 4: "herding",
                  5: "agriculture", 6: "agriculture", 7: "agriculture", 9: "agriculture"}
    dom_key = DOM_TO_KEY.get(dom)

    # ── 2. Determine whether agriculture is real ──
    ag_intensity = _get(society, "EA028")
    has_agriculture = ag_intensity is not None and ag_intensity > 1

    # ── 3. Subsistence mix — pick the top 2 activities by score ──
    scored = []
    for var, key in SUB_KEYS:
        val = _get(society, var)
        if val is None or val <= 0:
            continue
        # Suppress agriculture line if ag_intensity says "no agriculture"
        if key == "agriculture" and not has_agriculture:
            continue
        # Skip if this is the same activity already named as dominant
        if key == dom_key:
            continue
        scored.append((val, key))
    scored.sort(key=lambda x: -x[0])  # highest first

    for val, key in scored[:2]:  # top 2 only
        band = _intensity_word(val)
        if band == "none":
            continue
        tmpl = random.choice(SUB_TEMPLATES[key])
        parts.append(tmpl.format(
            intensity=random.choice(INTENSITY_WORDS[band]),
            resource=random.choice(RESOURCE_TYPES[key]),
        ))

    # ── 4. Agriculture details — only if agriculture is real ──
    if has_agriculture:
        parts.append(_pick(AG_INTENSITY, ag_intensity))

        code = _get(society, "EA029")
        if code is not None and code != 1:
            parts.append(_pick(CROP_TYPE, code))

        code = _get(society, "EA039")
        if code is not None:
            parts.append(_pick(PLOW, code))
    elif ag_intensity == 1:
        # Explicitly note absence only if nothing else was said about farming
        if dom not in (5, 6, 7, 9):
            parts.append(_pick(AG_INTENSITY, 1))

    # ── 5. Animal husbandry / milking (always relevant) ──
    code = _get(society, "EA040")
    if code is not None:
        parts.append(_pick(ANIMAL_HUSBANDRY, code))

    code = _get(society, "EA041")
    if code is not None:
        parts.append(_pick(MILKING, code))

    return " ".join(p for p in parts if p)


# ═══════════════════════════════════════════════════════════════════════════════
# 2. SETTLEMENT / HOUSING
# ═══════════════════════════════════════════════════════════════════════════════

SETTLEMENT = {
    1: ["The people are fully nomadic, moving frequently across their territory.",
        "Settlement is highly mobile, with camps lasting only days or weeks."],
    2: ["A seminomadic pattern governs residence, with seasonal relocations.",
        "Households alternate between seasonal camps at known sites."],
    3: ["Communities are semisedentary, occupying seasonal villages.",
        "Villages are semi-permanent and periodically abandoned."],
    4: ["Impermanent villages form around key resources and are periodically rebuilt.",
        "Settlement is village-based but not permanent."],
    5: ["Dispersed homesteads are scattered across the landscape.",
        "Families maintain separate farmsteads spread widely apart."],
    6: ["Small hamlets of a few households cluster together.",
        "Hamlet life centres on compact groups of neighbouring families."],
    7: ["People live in permanent villages or small towns.",
        "Stable villages serve as the main residential unit."],
    8: ["Large, complex permanent settlements anchor the region.",
        "Urbanised or near-urban centres organise regional life."],
}

JURISDICTIONAL = {
    2: ["At the local level, independent nuclear or polygynous families are the basic unit.",
        "Local jurisdiction rests with individual families."],
    3: ["Extended families form the jurisdictional base of the community.",
        "The local community is organised around extended family units."],
    4: ["Clan-barrios serve as the primary jurisdictional subdivision.",
        "Local governance operates through clan-based neighbourhood groupings."],
}

DWELLING_PLAN = {
    1: ["Dwellings have a semicircular ground plan."],
    2: ["Houses are built on a circular ground plan.",
        "Round houses define the residential architecture."],
    3: ["Dwellings are elliptical or elongated with rounded ends."],
    4: ["Houses follow a polygonal ground plan."],
    5: ["Rectangular or square houses are the norm.",
        "Dwellings are built in a rectangular layout."],
    6: ["Houses are quadrangular, arranged around an interior courtyard."],
}

FLOOR_LEVEL = {
    1: ["Floors are subterranean or semi-subterranean, dug into the earth.",
        "Houses are partially sunken below ground level."],
    2: ["Floors sit level with the surrounding ground.",
        "Dwellings rest directly on the ground surface."],
    3: ["Houses are raised slightly on low platforms.",
        "A raised platform elevates the living floor."],
    4: ["Dwellings stand on piles, posts, or piers well above ground.",
        "Stilt construction lifts houses substantially off the ground."],
}

WALL_MATERIAL = {
    1: ["Walls are built from stone, stucco, or fired brick."],
    2: ["Walls are plastered mud, dung, or wattle-and-daub."],
    3: ["Walls are made of wood — logs, planks, or bamboo."],
    4: ["Bark sheets form the walls."],
    5: ["Hides or skins cover the wall frames."],
    6: ["Felt or fabric drapes over the wall structure."],
    7: ["Woven mats or latticework form the walls."],
    8: ["Grass, leaves, or thatch make up the walls."],
    9: ["Adobe or sun-dried clay brick forms the walls."],
    10: ["Walls are open or absent."],
    11: ["Walls and roof merge into a single continuous shell."],
}

ROOF_SHAPE = {
    1: ["Roofs are rounded or semi-cylindrical."],
    2: ["Dome-shaped roofs cap the houses."],
    3: ["Beehive roofs with pointed peaks top the dwellings."],
    4: ["Conical roofs rise over the structures."],
    5: ["Semi-hemispherical roofs cover the houses."],
    6: ["Shed-style roofs with a single slope are standard."],
    7: ["Flat roofs define the architecture."],
    8: ["Gabled roofs with two slopes are typical."],
    9: ["Hipped or pyramidal roofs with four slopes cap the dwellings."],
}

ROOF_MATERIAL = {
    1: ["Roofing is stone or slate."],
    2: ["Roofs are plastered with clay, mud, or dung."],
    3: ["Wooden planks or shingles cover the roof."],
    4: ["Bark sheets serve as roofing."],
    5: ["Hides or skins are stretched over the roof frame."],
    6: ["Felt or fabric covers the roof."],
    7: ["Woven mats form the roof covering."],
    8: ["Grass, leaves, or thatch make up the roof.",
        "Thatched roofs are the norm."],
    9: ["Earth or turf covers the roof."],
    10: ["Ice or packed snow forms the roof."],
    11: ["Fired tile or brick serves as roofing material."],
}


def describe_settlement_housing(society):
    """Describe settlement pattern and housing, with cross-variable checks.

    Nomadic / seminomadic societies (EA030 <= 2) get simplified housing
    descriptions — elaborating permanent wall materials and roof shapes
    for a group that moves every few weeks is contradictory.
    """
    parts = []

    settlement = _get(society, "EA030")
    if settlement is not None:
        parts.append(_pick(SETTLEMENT, settlement))

    code = _get(society, "EA032")
    if code is not None:
        parts.append(_pick(JURISDICTIONAL, code))

    # Housing — suppress for highly mobile peoples
    is_mobile = settlement is not None and settlement <= 2
    housing_bits = []

    code = _get(society, "EA079")
    if code is not None and not is_mobile:
        housing_bits.append(_pick(DWELLING_PLAN, code))

    code = _get(society, "EA080")
    if code is not None and not is_mobile:
        housing_bits.append(_pick(FLOOR_LEVEL, code))

    code = _get(society, "EA081")
    if code is not None:
        # Portable materials (hides, felt, mats) are fine for mobile; others suppressed
        if is_mobile and code not in (5, 6, 7):
            pass  # skip permanent materials for nomads
        else:
            housing_bits.append(_pick(WALL_MATERIAL, code))

    code = _get(society, "EA082")
    if code is not None and not is_mobile:
        housing_bits.append(_pick(ROOF_SHAPE, code))

    code = _get(society, "EA083")
    if code is not None:
        if is_mobile and code not in (5, 6, 7):
            pass  # skip permanent roofing for nomads
        else:
            housing_bits.append(_pick(ROOF_MATERIAL, code))

    if housing_bits:
        parts.append(" ".join(housing_bits))

    return " ".join(p for p in parts if p)


# ═══════════════════════════════════════════════════════════════════════════════
# 3. POLITICAL / STRATIFICATION
# ═══════════════════════════════════════════════════════════════════════════════

POLITICAL = {
    1: ["There is no formal political hierarchy; leadership is informal and situational.",
        "Authority is diffuse — no one holds permanent power over others."],
    2: ["A single level of leadership — a headman or petty chief — coordinates local affairs.",
        "One tier of political authority handles community decisions."],
    3: ["Two hierarchical levels link local and regional authority.",
        "Political life operates across two administrative tiers."],
    4: ["Three levels of hierarchy reflect state-level organisation.",
        "Formal governance spans three administrative tiers."],
    5: ["Four or more hierarchical levels indicate complex state or imperial organisation.",
        "Deeply layered, centralised governance structures the polity."],
}

CLASS_STRAT = {
    1: ["Class distinctions among freemen are absent or negligible.",
        "Social equality among free people is the norm."],
    2: ["Wealth differences exist and carry social weight, though classes are not hereditary.",
        "People are distinguished by wealth but status is not fixed at birth."],
    3: ["An elite controls key resources like land, creating a clear upper stratum.",
        "Elite families monopolise scarce resources such as land."],
    4: ["A hereditary aristocracy stands apart from commoners.",
        "Dual stratification divides society into nobles and commoners."],
    5: ["Complex stratification links hereditary classes with occupational specialisation.",
        "Multiple social strata are tied to hereditary occupation and rank."],
}

CASTE_STRAT = {
    1: ["Caste distinctions are absent.",
        "There is no caste-based social division."],
    2: ["Despised occupational groups — smiths, leather-workers — form endogamous outcastes.",
        "Certain crafts carry hereditary stigma, isolating their practitioners."],
    3: ["Ethnic stratification creates a caste-like hierarchy, with a superordinate group refusing intermarriage.",
        "One ethnic group dominates and refuses to intermarry with subordinate peoples."],
    4: ["A complex caste system combines hereditary rank, occupational specialisation, and endogamy.",
        "Multiple rigid, endogamous castes structure the social order."],
}

SLAVERY_T = {
    1: ["Slavery is absent or nearly so.",
        "There is no institution of slavery."],
    2: ["Slavery exists in an incipient, nonhereditary form — captives or debtors may serve temporarily.",
        "Some people are held in bondage, but their status does not pass to their children."],
    3: ["Slavery is present, though its exact form is unclear.",
        "Enslaved people exist but the nature of their bondage is not well specified."],
    4: ["Hereditary slavery is an established institution of real social significance.",
        "Slavery is hereditary and deeply embedded in the social order.",
        "A hereditary slave class occupies the bottom of the social hierarchy."],
}

SLAVERY_TEMPORAL = {
    1: ["Slavery has never been practised here."],
    2: ["Slavery existed in the past but has since disappeared."],
    3: ["Slavery persists both historically and at present."],
}


def describe_political_stratification(society):
    parts = []

    code = _get(society, "EA033")
    if code is not None:
        parts.append(_pick(POLITICAL, code))

    # Class
    code = _get(society, "EA066")
    if code is not None:
        parts.append(_pick(CLASS_STRAT, code))

    # Secondary class (only add if different from primary)
    code2 = _get(society, "EA067")
    if code2 is not None and code2 != _get(society, "EA066") and code2 != 9:
        parts.append("A secondary pattern of " + _pick(CLASS_STRAT, code2, "class distinction also appears.").lower())

    # Caste
    code = _get(society, "EA068")
    if code is not None and code != 1:
        parts.append(_pick(CASTE_STRAT, code))

    code2 = _get(society, "EA069")
    if code2 is not None and code2 != _get(society, "EA068") and code2 != 1 and code2 != 9:
        parts.append("A secondary caste pattern also exists.")

    # Slavery
    code = _get(society, "EA070")
    if code is not None:
        parts.append(_pick(SLAVERY_T, code))

    code = _get(society, "EA071")
    if code is not None and code != 1:
        parts.append(_pick(SLAVERY_TEMPORAL, code))

    return " ".join(p for p in parts if p)


# ═══════════════════════════════════════════════════════════════════════════════
# 4. MARRIAGE / FAMILY
# ═══════════════════════════════════════════════════════════════════════════════

MARRIAGE_MODE = {
    1: ["Marriage typically involves bride-price — a transfer of goods or livestock to the bride's family.",
        "Bride-wealth is exchanged to formalise unions."],
    2: ["The groom performs bride-service, working for the bride's family.",
        "Labour owed to the bride's kin seals the marriage agreement."],
    3: ["A token bride-price — small and symbolic — accompanies marriage.",
        "Marriage involves a modest, symbolic payment."],
    4: ["Gift exchange between families accompanies marriage.",
        "Reciprocal gifts of real value are exchanged between the families."],
    5: ["Marriage involves sister exchange — a female relative given in return for the bride.",
        "Direct exchange of women between families formalises the union."],
    6: ["Marriage involves no significant economic transaction.",
        "No substantial bride-price, dowry, or exchange accompanies marriage."],
    7: ["Dowry flows from the bride's family to the groom or his kin.",
        "The bride's relatives provide substantial property at marriage."],
}

DOMESTIC_ORG = {
    1: ["Households are independent nuclear families, monogamous in structure.",
        "Each household is a self-contained nuclear family."],
    2: ["Nuclear families are independent, with occasional or limited polygyny.",
        "Households are mostly nuclear but some men have two wives."],
    3: ["Independent polyandrous families are the norm — a woman may have multiple husbands.",
        "Polyandrous households structure domestic life."],
    4: ["Independent polygynous families dominate, with co-wives in an unusual arrangement.",
        "Polygynous households are standard, with distinctive co-wife arrangements."],
    5: ["Independent polygynous families are common, with co-wives sharing a compound.",
        "Multiple wives reside together in a shared household."],
    6: ["Minimal extended or stem families — two related nuclear families under one roof.",
        "Households are small extended families spanning two generations."],
    7: ["Small extended families dissolve upon the death of the household head.",
        "Extended households form around a senior generation but are not permanent."],
    8: ["Large, corporate extended families span multiple generations and persist across lifetimes.",
        "Big extended family compounds house many related families."],
}

MARITAL_COMP = {
    1: ["Marriage is exclusively monogamous.",
        "Only monogamous unions are recognised."],
    2: ["Polygyny is occasional or limited.",
        "Most marriages are monogamous but a few men take a second wife."],
    3: ["Sororal polygyny is common, with co-wives living together.",
        "Men commonly marry sisters, who share a dwelling."],
    4: ["Sororal polygyny is preferred, with co-wives in separate quarters.",
        "Sisters are preferred as co-wives but maintain separate residences."],
    5: ["General polygyny — not restricted to sisters — is practised, with co-wives in separate quarters.",
        "Multiple wives from unrelated families each maintain their own dwelling."],
    6: ["General polygyny is the norm, with co-wives cohabiting.",
        "Multiple unrelated wives share a single compound."],
    7: ["Polyandry — a woman married to multiple husbands — is the standard.",
        "Polyandrous unions define family structure."],
}

RESIDENCE_PRIMARY = {
    1: ["Newlyweds reside with the husband's maternal uncle (avunculocal).",
        "Post-marital residence is avunculocal."],
    2: ["Couples may live with either spouse's parents (ambilocal).",
        "Residence is ambilocal, with flexibility in choice."],
    3: ["Residence is optionally uxorilocal or avunculocal."],
    4: ["Residence is optionally patrilocal or avunculocal."],
    5: ["The couple moves to the wife's mother's household (matrilocal).",
        "Matrilocal residence is the rule."],
    6: ["Newlyweds establish an independent household (neolocal).",
        "Couples set up on their own, apart from both families."],
    7: ["Spouses maintain separate households (duolocal).",
        "Husband and wife do not share a common residence."],
    8: ["The couple moves to the husband's father's household (patrilocal).",
        "Patrilocal residence is the norm."],
    9: ["Residence is uxorilocal — near the wife's kin but not in a matrilineal framework.",
        "Couples settle near the wife's family."],
    10: ["Residence is virilocal — near the husband's kin but not in a patrilineal framework.",
         "Couples settle near the husband's family."],
    11: ["Ambilocal residence leans uxorilocal (toward the wife's family)."],
    12: ["Ambilocal residence leans virilocal (toward the husband's family)."],
}

RESIDENCE_TRANSITION = {
    1: ["Residence patterns differ in the early years of marriage compared to later.",
        "Newly married couples live in one arrangement and shift after a few years."],
    2: ["Residence remains the same throughout the marriage.",
        "The post-marital living arrangement does not change over time."],
}


def describe_marriage_family(society):
    parts = []

    # Marriage mode
    code = _get(society, "EA006")
    if code is not None:
        parts.append(_pick(MARRIAGE_MODE, code))

    # Domestic organisation
    code = _get(society, "EA008")
    if code is not None:
        parts.append(_pick(DOMESTIC_ORG, code))

    # Marital composition
    code = _get(society, "EA009")
    if code is not None:
        parts.append(_pick(MARITAL_COMP, code))

    # Residence — prefer primary (EA010), fall back to EA012
    code = _get(society, "EA010")
    if code is None:
        code = _get(society, "EA012")
    if code is not None:
        parts.append(_pick(RESIDENCE_PRIMARY, code))

    # Residence transition
    code = _get(society, "EA201")
    if code is None:
        code = _get(society, "EA014")
    if code is not None:
        parts.append(_pick(RESIDENCE_TRANSITION, code))

    return " ".join(p for p in parts if p)


# ═══════════════════════════════════════════════════════════════════════════════
# 5. KINSHIP / DESCENT
# ═══════════════════════════════════════════════════════════════════════════════

DESCENT = {
    1: ["Descent is traced through the father's line (patrilineal).",
        "Patrilineal descent organises kinship and inheritance."],
    2: ["Descent is duolateral, recognising kin on both sides.",
        "Both paternal and maternal ties carry weight."],
    3: ["Descent follows the mother's line (matrilineal).",
        "Matrilineal descent structures inheritance and group membership."],
    4: ["Descent runs through quasi-lineages — flexible groupings that approximate lineage logic.",
        "Quasi-lineage descent provides loose patrilineal or matrilineal affiliation."],
    5: ["Descent is ambilineal — people choose which parent's line to affiliate with.",
        "Flexible, ambilineal descent allows choice between parental lines."],
    6: ["Descent is bilateral, with both parents' sides treated equally.",
        "Bilateral kinship means no single line dominates inheritance or identity."],
    7: ["Descent mixes multiple principles — no single rule applies uniformly.",
        "Mixed descent combines patrilineal, matrilineal, and other logics."],
}

COMMUNITY_ORG = {
    1: ["Local communities are endogamous demes — people marry within the village.",
        "Marriage is concentrated within the local community."],
    2: ["Communities are segmented into barrios or wards based on kin groups.",
        "Neighbourhoods within the settlement correspond to lineage groups."],
    3: ["Communities are agamous — neither strongly endogamous nor exogamous.",
        "Local marriage patterns are flexible and unstructured."],
    4: ["Strong local exogamy means people must marry outside their own community.",
        "Community exogamy pushes marriage alliances outward."],
    5: ["Segmented communities practice marked local exogamy.",
        "Kin-based barrios exist, and people marry outside the community."],
    6: ["The community is a single, localised exogamous clan.",
        "The entire settlement functions as one clan-community."],
}

PATRI_KIN = {
    1: ["No patrilineal kin groups exist."],
    2: ["Patrilineal exogamy is practised even without formal patrilineal groups."],
    3: ["Patrilineal lineages are confined to a single community.",
        "Localised patrilineages organise kin within the settlement."],
    4: ["Patrilineal clans span multiple communities.",
        "Patriclans link kin across different settlements."],
    5: ["Patrilineal phratries — clusters of clans — form the widest kin groupings.",
        "Segmentary patrilineal organisation extends across a broad territory."],
    6: ["Patrilineal moieties divide the society into two halves.",
        "A dual patrilineal moiety system structures social relations."],
}

MATRI_KIN = {
    1: ["No matrilineal kin groups exist."],
    2: ["Matrilineal exogamy is practised even without formal matrilineal groups."],
    3: ["Matrilineal lineages are localised within settlements.",
        "Matrilineages organise kin within the community."],
    4: ["Matrilineal clans span multiple communities.",
        "Matriclans connect kin across different settlements."],
    5: ["Matrilineal phratries group clusters of clans together.",
        "Broad matrilineal segmentary organisation extends across the region."],
    6: ["Matrilineal moieties divide the society in two.",
        "A dual matrilineal moiety system shapes social identity."],
}

COGNATIC_KIN = {
    1: ["Bilateral descent is recognised but no formal kindreds are reported."],
    2: ["Ego-centred kindreds — bilateral kin groups — organise social obligations.",
        "Kindreds connect people through both parents' sides."],
    3: ["Ambilineal descent through extended families provides flexible affiliation."],
    4: ["Ancestor-oriented ramages organise descent flexibly.",
        "Ramage groups trace descent from founding ancestors through flexible lines."],
    5: ["Exogamous ramages structure kin affiliation."],
    6: ["Bilateral descent coexists with quasi-lineage groupings."],
    9: ["Cognatic kin groups are absent; unilineal descent prevails."],
}

COUSIN_MARRIAGE_SUMMARY = {
    1: ["Any first cousin is a marriageable partner.",
        "Cousin marriage is unrestricted — all first cousins are eligible."],
    2: ["Most first cousins are marriageable except lineage-mates."],
    3: ["Two of the four types of first cousin are eligible for marriage."],
    4: ["Only one specific type of first cousin may be married."],
    5: ["First cousins are forbidden but second cousins are acceptable.",
        "Marriage with first cousins is taboo; second cousins are allowed."],
    6: ["Both first and some second cousins are forbidden as marriage partners."],
    7: ["First-cousin marriage is forbidden."],
    8: ["All first and second cousins are forbidden as spouses.",
        "Cousin marriage is broadly prohibited."],
}

KIN_TERMINOLOGY = {
    1: ["Kinship terminology follows the Crow system, reflecting matrilineal principles.",
        "Crow-type cousin terms mark matrilineal distinctions."],
    2: ["Kinship terms are descriptive or derivative.",
        "Relatives are named by specific, descriptive terms."],
    3: ["Eskimo-type kinship terminology distinguishes lineal from collateral kin.",
        "The kinship system resembles the Eskimo pattern."],
    4: ["Hawaiian-type terminology groups all cousins together with siblings.",
        "Generational (Hawaiian) kinship terms are used."],
    5: ["Iroquois-type terminology distinguishes cross-cousins from parallel-cousins.",
        "The kinship system follows the Iroquois pattern."],
    6: ["Omaha-type terminology reflects patrilineal principles.",
        "Omaha cousin terms encode patrilineal logic."],
    7: ["Sudanese-type terminology gives each relative a unique term.",
        "Highly specific Sudanese kinship terms are used."],
    8: ["Kinship terminology mixes or blends multiple patterns."],
}


def describe_kinship(society):
    parts = []

    code = _get(society, "EA043")
    if code is not None:
        parts.append(_pick(DESCENT, code))

    code = _get(society, "EA015")
    if code is not None:
        parts.append(_pick(COMMUNITY_ORG, code))

    code = _get(society, "EA017")
    if code is not None and code != 1:
        parts.append(_pick(PATRI_KIN, code))

    code = _get(society, "EA019")
    if code is not None and code != 1:
        parts.append(_pick(MATRI_KIN, code))

    code = _get(society, "EA021")
    if code is not None and code != 9:
        parts.append(_pick(COGNATIC_KIN, code))

    # Cousin marriage (use summary EA024)
    code = _get(society, "EA024")
    if code is not None:
        parts.append(_pick(COUSIN_MARRIAGE_SUMMARY, code))

    code = _get(society, "EA027")
    if code is not None:
        parts.append(_pick(KIN_TERMINOLOGY, code))

    return " ".join(p for p in parts if p)


# ═══════════════════════════════════════════════════════════════════════════════
# 6. INHERITANCE / SUCCESSION
# ═══════════════════════════════════════════════════════════════════════════════

SUCCESSION = {
    1: ["Leadership passes to a patrilineal heir.",
        "The headman's office is inherited through the male line."],
    2: ["Succession follows the matrilineal line.",
        "The next leader is chosen from the mother's kin."],
    3: ["The headman is appointed by a higher authority.",
        "Leadership is assigned from above, not inherited."],
    4: ["Seniority or age determines who leads.",
        "The oldest eligible person assumes the headman's role."],
    5: ["Influence — wealth, reputation — determines the leader.",
        "Leadership accrues to the most influential person."],
    6: ["Formal election or consensus selects the headman.",
        "The community chooses its leader through a deliberate process."],
    7: ["Informal consensus selects the leader.",
        "Leadership emerges through quiet agreement rather than formal vote."],
    9: ["There is no office resembling a local headman.",
        "Political authority is collective or absent entirely."],
}

HEIR_TYPE = {
    1: ["The son inherits leadership."],
    2: ["A patrilineal heir other than the son takes precedence."],
    3: ["The sister's son inherits the office."],
    4: ["A matrilineal heir other than the sister's son takes precedence."],
    5: ["Succession is nonhereditary."],
    9: ["No headman-like office exists to inherit."],
}

MOVABLE_INHERITANCE = {
    1: ["There are no individual property rights in movable goods, or possessions are destroyed at death.",
        "Personal property is buried, destroyed, or given away at death."],
    2: ["Movable property passes through the matrilineal line to sisters' sons.",
        "Inheritance of personal goods follows the mother's kin."],
    3: ["Matrilineal heirs take precedence over sisters' sons for movable property."],
    4: ["Children inherit movable property, with daughters receiving less than sons."],
    5: ["Children of either sex inherit movable property equally."],
    6: ["Patrilineal heirs other than sons take precedence for movable property."],
    7: ["Sons inherit movable property (patrilineal).",
        "Personal possessions pass from father to son."],
}


def describe_inheritance(society):
    parts = []

    code = _get(society, "EA072")
    if code is not None:
        parts.append(_pick(SUCCESSION, code))

    code = _get(society, "EA073")
    if code is not None and code not in (5, 9):
        parts.append(_pick(HEIR_TYPE, code))

    code = _get(society, "EA076")
    if code is not None:
        parts.append(_pick(MOVABLE_INHERITANCE, code))

    return " ".join(p for p in parts if p)


# ═══════════════════════════════════════════════════════════════════════════════
# 7. LABOR / GENDER DIVISION
# ═══════════════════════════════════════════════════════════════════════════════

SEX_DIV_LABELS = {
    1: "done exclusively by men",
    2: "done mostly by men",
    3: "shared between the sexes with differentiated tasks",
    4: "shared equally between men and women",
    5: "done mostly by women",
    6: "done exclusively by women",
    7: "not differentiated by sex (industrialised context)",
    8: "performed by unspecified participants",
    9: None,  # absent
}

AGE_SPEC_LABELS = {
    1: "with specialisation among the young",
    2: "with specialisation among elders",
    3: "with craft specialists performing the work",
    4: "industrially specialised",
    9: "performed by most adults",
    10: None,  # absent
}

LABOR_ACTIVITIES = {
    "EA044": "Metalworking",
    "EA051": "Agriculture",
    "EA054": "Trade",
}

AGE_ACTIVITIES = {
    "EA055": "metalworking",
    "EA062": "agriculture",
    "EA065": "trade",
}


def describe_labor(society):
    sex_parts = []
    for var, activity in LABOR_ACTIVITIES.items():
        code = _get(society, var)
        if code is not None and code in SEX_DIV_LABELS and SEX_DIV_LABELS[code] is not None:
            sex_parts.append(f"{activity} is {SEX_DIV_LABELS[code]}.")

    age_parts = []
    for var, activity in AGE_ACTIVITIES.items():
        code = _get(society, var)
        if code is not None and code in AGE_SPEC_LABELS and AGE_SPEC_LABELS[code] is not None:
            age_parts.append(f"In {activity}, work is {AGE_SPEC_LABELS[code]}.")

    all_parts = sex_parts + age_parts
    if not all_parts:
        return ""

    intro = random.choice([
        "The division of labour follows clear patterns.",
        "Work is organised along lines of sex and age.",
        "Labour roles are socially structured.",
    ])
    return intro + " " + " ".join(all_parts)


# ═══════════════════════════════════════════════════════════════════════════════
# 8. CULTURE / RITUAL
# ═══════════════════════════════════════════════════════════════════════════════

CIRCUMCISION = {
    1: ["Male circumcision is absent or not generally practised.",
        "Boys are not circumcised."],
    2: ["Boys are circumcised shortly after birth."],
    3: ["Circumcision is performed during infancy."],
    4: ["Circumcision takes place in early childhood."],
    5: ["Boys are circumcised in late childhood, between ages six and ten."],
    6: ["Circumcision marks adolescence, performed between ages eleven and fifteen.",
        "Adolescent circumcision serves as a rite of passage."],
    7: ["Circumcision is performed in early adulthood.",
        "Young men are circumcised as they enter adult life."],
    8: ["Circumcision occurs at maturity."],
    9: ["Circumcision is performed in old age."],
    10: ["Circumcision is customary but the usual age is unspecified."],
}


def describe_culture(society):
    parts = []
    code = _get(society, "EA037")
    if code is not None:
        parts.append(_pick(CIRCUMCISION, code))
    return " ".join(p for p in parts if p)


# ═══════════════════════════════════════════════════════════════════════════════
# 9. CLIMATE / ENVIRONMENT
# ═══════════════════════════════════════════════════════════════════════════════

TEMP_TEMPLATES = {
    "cold": [
        "The climate is cold for much of the year.",
        "Winters are long and temperatures stay low.",
        "Cold conditions dominate the seasonal cycle.",
    ],
    "temperate": [
        "The climate is temperate, with distinct seasons.",
        "Temperatures are moderate through most of the year.",
        "Seasons shift between warm and cool without extremes.",
    ],
    "warm": [
        "The climate is warm year-round.",
        "Heat and long growing seasons define the environment.",
        "Warm conditions prevail across most of the year.",
    ],
}

PRECIP_TEMPLATES = {
    "arid": [
        "Rainfall is scarce and the landscape is dry.",
        "The climate is arid, with rain arriving only in short bursts.",
        "Water is limited and droughts are a persistent concern.",
    ],
    "moderate": [
        "Rainfall is moderate and fairly dependable.",
        "Seasonal rains come regularly enough to sustain agriculture.",
        "Precipitation is balanced through the year.",
    ],
    "wet": [
        "Rain is plentiful and the landscape stays green.",
        "The climate is wet, with frequent and heavy rainfall.",
        "Abundant moisture supports dense vegetation.",
    ],
}

TEMP_CONSTANCY_T = {
    "low": [
        "Temperature swings sharply between seasons.",
        "There is wide seasonal variation in temperature.",
    ],
    "med": [
        "Temperatures are moderately consistent across the year.",
        "Seasonal temperature changes are noticeable but not extreme.",
    ],
    "high": [
        "Temperatures remain remarkably stable year-round.",
        "There is very little seasonal temperature variation.",
    ],
}

TEMP_PREDICT_T = {
    "low": [
        "Temperature patterns are hard to predict from year to year.",
        "Interannual temperature variation makes planning difficult.",
    ],
    "med": [
        "Temperature patterns are moderately predictable.",
    ],
    "high": [
        "Temperature patterns are highly predictable across years.",
        "People can count on consistent temperature cycles.",
    ],
}

PRECIP_CONSTANCY_T = {
    "low": [
        "Rainfall varies greatly from month to month.",
        "Precipitation is highly uneven across the year.",
    ],
    "med": [
        "Rainfall is moderately spread through the seasons.",
    ],
    "high": [
        "Rainfall arrives with unusual evenness across the year.",
        "Precipitation is remarkably steady month to month.",
    ],
}

PRECIP_PREDICT_T = {
    "low": [
        "Rainfall timing is unpredictable from year to year.",
        "When the rains come varies substantially between years.",
    ],
    "med": [
        "Rainfall timing is moderately predictable.",
    ],
    "high": [
        "The rainy season arrives with reliable regularity.",
        "Precipitation patterns are highly predictable year to year.",
    ],
}


def _band3(val, lo, hi):
    """Return 'low', 'med', or 'high' for a value between lo and hi."""
    if val is None:
        return None
    third = (hi - lo) / 3
    if val < lo + third:
        return "low"
    if val < lo + 2 * third:
        return "med"
    return "high"


def describe_climate_full(society):
    parts = []

    temp = _getf(society, "AnnualMeanTemperature")
    if temp is not None:
        if temp < 10:
            parts.append(random.choice(TEMP_TEMPLATES["cold"]))
        elif temp < 20:
            parts.append(random.choice(TEMP_TEMPLATES["temperate"]))
        else:
            parts.append(random.choice(TEMP_TEMPLATES["warm"]))

    precip = _getf(society, "MonthlyMeanPrecipitation")
    if precip is not None:
        if precip < 50:
            parts.append(random.choice(PRECIP_TEMPLATES["arid"]))
        elif precip < 150:
            parts.append(random.choice(PRECIP_TEMPLATES["moderate"]))
        else:
            parts.append(random.choice(PRECIP_TEMPLATES["wet"]))

    tc = _getf(society, "TemperatureConstancy")
    band = _band3(tc, 0.17, 0.84)
    if band:
        parts.append(random.choice(TEMP_CONSTANCY_T[band]))

    tp = _getf(society, "TemperaturePredictability")
    band = _band3(tp, 0.46, 0.86)
    if band:
        parts.append(random.choice(TEMP_PREDICT_T[band]))

    pc = _getf(society, "PrecipitationConstancy")
    band = _band3(pc, 0.18, 0.69)
    if band:
        parts.append(random.choice(PRECIP_CONSTANCY_T[band]))

    pp = _getf(society, "PrecipitationPredictability")
    band = _band3(pp, 0.34, 0.79)
    if band:
        parts.append(random.choice(PRECIP_PREDICT_T[band]))

    return " ".join(p for p in parts if p)


# ═══════════════════════════════════════════════════════════════════════════════
# NARRATIVE FRAMING (intros, transitions, conclusions)
# ═══════════════════════════════════════════════════════════════════════════════

INTROS = [
    "The story of this society begins with how people make a living.",
    "Life here is shaped by a familiar rhythm of work, movement, and cooperation.",
    "This community's character shows in the practical choices of livelihood and home.",
    "What defines this group is how they meet basic needs and organise daily life.",
    "Their way of life is built around a consistent blend of subsistence and social structure.",
    "You can feel the society's character in how people eat, build, and relate to one another.",
    "Daily life follows a practical logic connecting economy, kinship, and authority.",
    "The community's rhythm emerges from how food is found, shared, and turned into social life.",
]

TRANSITIONS = [
    "Beyond subsistence, the social fabric reveals its own complexity.",
    "The social order is no less distinctive than the economy.",
    "Authority and hierarchy shape daily interactions.",
    "Social structure runs deeper than economics alone.",
    "Power and status tell another part of the story.",
    "The way people relate to each other reveals a deeper structure.",
]

FAMILY_TRANSITIONS = [
    "Family life follows its own logic.",
    "Marriage and household patterns reflect the wider social order.",
    "Domestic life is tightly woven into the larger social fabric.",
    "The household is where these broader patterns play out day to day.",
]

ENVIRONMENT_TRANSITIONS = [
    "All of this unfolds within a particular landscape.",
    "The environment sets the stage for everything else.",
    "Nature shapes what is possible here.",
    "The land and climate frame all of these choices.",
]

CONCLUSIONS_STABLE_CLEAN = [
    "By most measures, this society is well-adapted to its environment and internally consistent. The pieces fit.",
    "This is a society that works. Food is secure, authority is proportionate, and people have room to live.",
    "There's a quiet stability here — not perfect, but functional and self-sustaining.",
    "Few obvious fault lines. The economy supports the social structure, and the social structure supports the economy.",
    "This looks like a society that could persist for generations without major upheaval.",
]

CONCLUSIONS_STABLE_DARK = [
    "It works — but not for everyone. The stability rests on the backs of those at the bottom.",
    "On paper, this society is functional. In practice, someone is always paying the price for that stability.",
    "There's an uncomfortable efficiency here. Everything holds together, but only because some people have no choice.",
    "Sustainable? Probably. Just? That depends on who you ask — and who is allowed to answer.",
    "The machinery runs smoothly. Whether that's admirable or horrifying depends on where you stand in the hierarchy.",
    "This is the kind of order that lasts — not because it's fair, but because those who suffer it have no alternative.",
]

CONCLUSIONS_FRAGILE = [
    "There are cracks in the foundation. This society's structure doesn't quite match its resource base.",
    "Something here doesn't add up. The social complexity may be outrunning what the land can support.",
    "This arrangement feels precarious — one bad season or one challenge to authority could unravel it.",
    "The balance is delicate. Too many demands on too few resources, or too much hierarchy for too little production.",
    "Whether this holds together long-term is an open question. The tensions are real.",
]

CONCLUSIONS_HARSH_FRAGILE = [
    "This is a society under pressure from every direction — environmentally and socially. Something has to give.",
    "Hard land, hard rules, and hard lives. The question isn't whether this is sustainable — it's how long before it breaks.",
    "The combination of environmental stress and social inequality makes this a volatile arrangement.",
    "Survival here comes at a steep cost, and the cost is not shared equally. That rarely ends well.",
]

CONCLUSIONS_SIMPLE = [
    "It's a lean way of life — not much room for excess, but not much need for it either.",
    "Simple doesn't mean easy. But this society is well-matched to its constraints.",
    "There's an elegance to the simplicity. Few layers, few contradictions.",
    "What you see is what you get. A small-scale society doing what it needs to survive.",
]

CONCLUSIONS_COLLAPSE = [
    "This society cannot sustain itself. The structure demands more than the land and economy can deliver — collapse is not a question of if, but when.",
    "The math doesn't work. You cannot run a complex state on foraging alone. This arrangement is a contradiction that will resolve itself, violently if necessary.",
    "This is a society eating itself alive. The hierarchy requires surplus that doesn't exist, and the people at the bottom are running out of reasons to stay.",
    "Nothing about this is stable. The political structure is built on a foundation that isn't there. When it falls — and it will — there won't be much left.",
    "This is a dead end. The combination of demands and resources points in only one direction: disintegration.",
    "On paper, this society exists. In practice, it's a slow-motion collapse. The centre cannot hold because there is no centre — just extraction from people who have nothing left to give.",
]

CONCLUSIONS_COLLAPSE_MILD = [
    "Something here has to break. The pieces don't fit together, and no amount of tradition or force can make them fit for long.",
    "This society is running on borrowed time. The contradictions are structural, not cosmetic.",
    "It might hold together for a generation. Maybe two. But the mismatch between what's demanded and what's produced will catch up.",
    "The warning signs are all here. Overreach, undersupply, and a social order that relies on conditions it can't guarantee.",
]


def _generate_conclusion(society):
    """Pick a conclusion that reflects the society's tensions, including collapse."""
    slavery = _get(society, "EA070", 1)
    caste = _get(society, "EA068", 1)
    hierarchy = _get(society, "EA033", 1)
    ag_intensity = _get(society, "EA028", 1)
    settlement = _get(society, "EA030", 1)
    class_strat = _get(society, "EA066", 1)
    dom_sub = _get(society, "EA042", 8)

    has_coercion = slavery >= 3 or caste >= 3 or class_strat >= 4
    has_exploitation = slavery >= 2 or caste >= 2
    is_complex = hierarchy >= 3
    is_highly_complex = hierarchy >= 4
    is_sedentary = settlement >= 5
    is_nomadic = settlement <= 2
    has_agriculture = ag_intensity >= 3
    has_intensive_ag = ag_intensity >= 5
    is_simple = hierarchy <= 2
    is_forager = dom_sub in (1, 2, 3) and not has_agriculture

    # Get climate stress signals
    temp = _getf(society, "AnnualMeanTemperature")
    precip = _getf(society, "MonthlyMeanPrecipitation")
    climate_harsh = (temp is not None and (temp < 5 or temp > 30)) or \
                    (precip is not None and precip < 30)

    # ════════════════════════════════════════════════
    # COLLAPSE TIER — hard contradictions
    # ════════════════════════════════════════════════

    collapse_signals = 0

    # Complex state (3+ tiers) running on foraging — historically near-impossible
    if is_highly_complex and is_forager:
        collapse_signals += 3

    # Complex state + nomadic — you can't administer what you can't find
    if is_complex and is_nomadic:
        collapse_signals += 2

    # Intensive agriculture + nomadic — can't farm and move
    if has_intensive_ag and is_nomadic:
        collapse_signals += 2

    # Hereditary slavery + no authority to enforce it
    if slavery >= 3 and hierarchy <= 1:
        collapse_signals += 2

    # Complex hierarchy + harsh climate + no agriculture
    if is_complex and climate_harsh and not has_agriculture:
        collapse_signals += 2

    # Large sedentary settlement + pure foraging — can't feed a town on berries
    if settlement >= 7 and is_forager:
        collapse_signals += 2

    # Coercion + nomadic + no agriculture
    if has_coercion and is_nomadic and not has_agriculture:
        collapse_signals += 1

    # Harsh climate + no food security + exploitation
    if climate_harsh and is_forager and has_exploitation:
        collapse_signals += 1

    # COLLAPSE — multiple hard contradictions
    if collapse_signals >= 3:
        return random.choice(CONCLUSIONS_COLLAPSE)

    # MILD COLLAPSE — serious but not total contradiction
    if collapse_signals >= 2:
        return random.choice(CONCLUSIONS_COLLAPSE_MILD)

    # ════════════════════════════════════════════════
    # TENSION TIERS — problems but not structural failure
    # ════════════════════════════════════════════════

    # Stable food + settlement + coercion = "works but dark"
    if has_agriculture and is_sedentary and has_coercion:
        return random.choice(CONCLUSIONS_STABLE_DARK)

    # Complex hierarchy without agriculture = fragile
    if is_complex and not has_agriculture:
        if has_coercion:
            return random.choice(CONCLUSIONS_HARSH_FRAGILE)
        return random.choice(CONCLUSIONS_FRAGILE)

    # Nomadic/mobile + complex hierarchy = fragile
    if not is_sedentary and is_complex:
        return random.choice(CONCLUSIONS_FRAGILE)

    # Coercion without stable base = harsh and fragile
    if has_coercion and not (has_agriculture and is_sedentary):
        return random.choice(CONCLUSIONS_HARSH_FRAGILE)

    # Exploitation present but mild, with stable base = stable but dark
    if has_exploitation and has_agriculture and is_sedentary:
        return random.choice(CONCLUSIONS_STABLE_DARK)

    # ════════════════════════════════════════════════
    # POSITIVE TIERS
    # ════════════════════════════════════════════════

    # Stable agriculture + sedentary + no coercion = clean and functional
    if has_agriculture and is_sedentary and not has_exploitation:
        return random.choice(CONCLUSIONS_STABLE_CLEAN)

    # Simple society, low hierarchy, no agriculture, no coercion = lean/simple
    if is_simple and not has_exploitation and not has_agriculture:
        return random.choice(CONCLUSIONS_SIMPLE)

    # Default fallback
    return random.choice(CONCLUSIONS_STABLE_CLEAN + CONCLUSIONS_SIMPLE)


# ═══════════════════════════════════════════════════════════════════════════════
# ASSEMBLY
# ═══════════════════════════════════════════════════════════════════════════════

def generate_full_description(society, complexity=None, seed=None):
    """Build a multi-paragraph narrative from the society dict.

    Works with any subset of the 66 VAE variables — missing keys are
    silently skipped.  Sections are grouped into themed paragraphs with
    transition phrases for narrative flow.
    """
    if seed is not None:
        random.seed(seed)

    # Generate all sections
    economy     = describe_economy(society)
    settlement  = describe_settlement_housing(society)
    political   = describe_political_stratification(society)
    marriage    = describe_marriage_family(society)
    kinship     = describe_kinship(society)
    inheritance = describe_inheritance(society)
    labor       = describe_labor(society)
    culture     = describe_culture(society)
    climate     = describe_climate_full(society)

    paragraphs = []

    # ── Paragraph 1: Intro + Economy + Settlement ──
    p1_parts = [random.choice(INTROS)]
    if economy:
        p1_parts.append(economy)
    if settlement:
        p1_parts.append(settlement)
    paragraphs.append(" ".join(p1_parts))

    # ── Paragraph 2: Political + Stratification ──
    if political:
        paragraphs.append(random.choice(TRANSITIONS) + " " + political)

    # ── Paragraph 3: Marriage + Kinship + Inheritance ──
    p3_parts = []
    if marriage:
        p3_parts.append(marriage)
    if kinship:
        p3_parts.append(kinship)
    if inheritance:
        p3_parts.append(inheritance)
    if p3_parts:
        paragraphs.append(random.choice(FAMILY_TRANSITIONS) + " " + " ".join(p3_parts))

    # ── Paragraph 4: Labor + Culture ──
    p4_parts = []
    if labor:
        p4_parts.append(labor)
    if culture:
        p4_parts.append(culture)
    if p4_parts:
        paragraphs.append(" ".join(p4_parts))

    # ── Paragraph 5: Climate / Environment ──
    if climate:
        paragraphs.append(random.choice(ENVIRONMENT_TRANSITIONS) + " " + climate)

    # ── Conclusion — context-aware ──
    if len(paragraphs) > 1:
        paragraphs.append(_generate_conclusion(society))

    if not paragraphs or (len(paragraphs) == 1 and paragraphs[0].strip() in INTROS):
        return "Not enough information to describe this society."

    return "\n\n".join(paragraphs)


# ═══════════════════════════════════════════════════════════════════════════════
# CLI TEST
# ═══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    sample = {
        "EA001": 2, "EA002": 1, "EA003": 0, "EA004": 1, "EA005": 6,
        "EA006": 1, "EA007": 8, "EA008": 6, "EA009": 2, "EA010": 8,
        "EA011": 1, "EA012": 8, "EA013": 9, "EA014": 11, "EA015": 3,
        "EA016": 9, "EA017": 3, "EA018": 3, "EA019": 1, "EA020": 1,
        "EA021": 9, "EA022": 9, "EA023": 7, "EA024": 7, "EA025": 15,
        "EA026": 9, "EA027": 5, "EA028": 5, "EA029": 6, "EA030": 7,
        "EA032": 3, "EA033": 2, "EA037": 6, "EA039": 3, "EA040": 7,
        "EA041": 2, "EA042": 7, "EA043": 1, "EA044": 1, "EA051": 4,
        "EA054": 2, "EA055": 9, "EA062": 9, "EA065": 9, "EA066": 2,
        "EA067": 9, "EA068": 1, "EA069": 9, "EA070": 4, "EA071": 3,
        "EA072": 1, "EA073": 1, "EA076": 7, "EA079": 5, "EA080": 2,
        "EA081": 9, "EA082": 7, "EA083": 8, "EA201": 2,
        "AnnualMeanTemperature": 21.2,
        "MonthlyMeanPrecipitation": 120.0,
        "TemperatureConstancy": 0.55,
        "TemperaturePredictability": 0.70,
        "PrecipitationConstancy": 0.40,
        "PrecipitationPredictability": 0.60,
    }
    print(generate_full_description(sample, seed=42))
