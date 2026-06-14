"""
Variable Constraints for Society Dream Machine
Auto-generated from codes.csv + MASTER_DATASET.csv.

This file defines:
1. Data types (categorical, integer, continuous)
2. Valid ranges and values for each variable
3. Inter-variable constraints
"""

import numpy as np

# ==============================================================================
# SUBSISTENCE ECONOMY (EA001-EA005)
# ==============================================================================

SUBSISTENCE_VARS = {'EA001': {'labels': {0: 'Zero to 5 percent dependence',
                      1: '6 to 15 percent dependence',
                      2: '16 to 25 percent dependence',
                      3: '26 to 35 percent dependence',
                      4: '36 to 45 percent dependence',
                      5: '46 to 55 percent dependence',
                      6: '56 to 65 percent dependence',
                      7: '66 to 75 percent dependence',
                      8: '76 to 85 percent dependence',
                      9: '86 to 100 percent dependence'},
           'name': 'EA001',
           'type': 'categorical',
           'valid_values': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]},
 'EA002': {'labels': {0: 'Zero to 5 percent dependence',
                      1: '6 to 15 percent dependence',
                      2: '16 to 25 percent dependence',
                      3: '26 to 35 percent dependence',
                      4: '36 to 45 percent dependence',
                      5: '46 to 55 percent dependence',
                      6: '56 to 65 percent dependence',
                      7: '66 to 75 percent dependence',
                      8: '76 to 85 percent dependence',
                      9: '86 to 100 percent dependence'},
           'name': 'EA002',
           'type': 'categorical',
           'valid_values': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]},
 'EA003': {'labels': {0: 'Zero to 5 percent dependence',
                      1: '6 to 15 percent dependence',
                      2: '16 to 25 percent dependence',
                      3: '26 to 35 percent dependence',
                      4: '36 to 45 percent dependence',
                      5: '46 to 55 percent dependence',
                      6: '56 to 65 percent dependence',
                      7: '66 to 75 percent dependence',
                      8: '76 to 85 percent dependence',
                      9: '86 to 100 percent dependence'},
           'name': 'EA003',
           'type': 'categorical',
           'valid_values': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]},
 'EA004': {'labels': {0: 'Zero to 5 percent dependence',
                      1: '6 to 15 percent dependence',
                      2: '16 to 25 percent dependence',
                      3: '26 to 35 percent dependence',
                      4: '36 to 45 percent dependence',
                      5: '46 to 55 percent dependence',
                      6: '56 to 65 percent dependence',
                      7: '66 to 75 percent dependence',
                      8: '76 to 85 percent dependence',
                      9: '86 to 100 percent dependence'},
           'name': 'EA004',
           'type': 'categorical',
           'valid_values': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]},
 'EA005': {'labels': {0: 'Zero to 5 percent dependence',
                      1: '6 to 15 percent dependence',
                      2: '16 to 25 percent dependence',
                      3: '26 to 35 percent dependence',
                      4: '36 to 45 percent dependence',
                      5: '46 to 55 percent dependence',
                      6: '56 to 65 percent dependence',
                      7: '66 to 75 percent dependence',
                      8: '76 to 85 percent dependence',
                      9: '86 to 100 percent dependence'},
           'name': 'EA005',
           'type': 'categorical',
           'valid_values': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]}}

# ==============================================================================
# ALL CODED VARIABLES (from codes.csv)
# ==============================================================================

CODED_VARS = {'EA001': {'labels': {0: 'Zero to 5 percent dependence',
                      1: '6 to 15 percent dependence',
                      2: '16 to 25 percent dependence',
                      3: '26 to 35 percent dependence',
                      4: '36 to 45 percent dependence',
                      5: '46 to 55 percent dependence',
                      6: '56 to 65 percent dependence',
                      7: '66 to 75 percent dependence',
                      8: '76 to 85 percent dependence',
                      9: '86 to 100 percent dependence'},
           'name': 'EA001',
           'type': 'categorical',
           'valid_values': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]},
 'EA002': {'labels': {0: 'Zero to 5 percent dependence',
                      1: '6 to 15 percent dependence',
                      2: '16 to 25 percent dependence',
                      3: '26 to 35 percent dependence',
                      4: '36 to 45 percent dependence',
                      5: '46 to 55 percent dependence',
                      6: '56 to 65 percent dependence',
                      7: '66 to 75 percent dependence',
                      8: '76 to 85 percent dependence',
                      9: '86 to 100 percent dependence'},
           'name': 'EA002',
           'type': 'categorical',
           'valid_values': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]},
 'EA003': {'labels': {0: 'Zero to 5 percent dependence',
                      1: '6 to 15 percent dependence',
                      2: '16 to 25 percent dependence',
                      3: '26 to 35 percent dependence',
                      4: '36 to 45 percent dependence',
                      5: '46 to 55 percent dependence',
                      6: '56 to 65 percent dependence',
                      7: '66 to 75 percent dependence',
                      8: '76 to 85 percent dependence',
                      9: '86 to 100 percent dependence'},
           'name': 'EA003',
           'type': 'categorical',
           'valid_values': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]},
 'EA004': {'labels': {0: 'Zero to 5 percent dependence',
                      1: '6 to 15 percent dependence',
                      2: '16 to 25 percent dependence',
                      3: '26 to 35 percent dependence',
                      4: '36 to 45 percent dependence',
                      5: '46 to 55 percent dependence',
                      6: '56 to 65 percent dependence',
                      7: '66 to 75 percent dependence',
                      8: '76 to 85 percent dependence',
                      9: '86 to 100 percent dependence'},
           'name': 'EA004',
           'type': 'categorical',
           'valid_values': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]},
 'EA005': {'labels': {0: 'Zero to 5 percent dependence',
                      1: '6 to 15 percent dependence',
                      2: '16 to 25 percent dependence',
                      3: '26 to 35 percent dependence',
                      4: '36 to 45 percent dependence',
                      5: '46 to 55 percent dependence',
                      6: '56 to 65 percent dependence',
                      7: '66 to 75 percent dependence',
                      8: '76 to 85 percent dependence',
                      9: '86 to 100 percent dependence'},
           'name': 'EA005',
           'type': 'categorical',
           'valid_values': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]},
 'EA006': {'labels': {1: 'Bride-price or bride-wealth, i.e., transfer of a substantial '
                         'consideration in the form of livestock, goods, or money from the groom '
                         'or his relatives to the kinsmen of the bride',
                      2: 'Bride-service, i.e., a substantial material consideration in which the '
                         'principal element consists of labor or other services rendered by the '
                         "groom to the bride's kinsmen",
                      3: 'Token bride-price, i.e., a small or symbolic payment only',
                      4: 'Gift exchange, i.e., reciprocal exchange of gifts of substantial value '
                         'between the relatives of the bride and groom, or a continuing exchange '
                         'of goods and services in approximately equal amounts between the groom '
                         "or his kinsmen and the bride's relatives",
                      5: 'Exchange, i.e., transfer of a sister or other female relative of the '
                         'groom in exchange for the bride',
                      6: 'Absence of any significant consideration, or bridal gifts only',
                      7: 'Dowry, i.e., transfer of a substantial amount of property from the '
                         "bride's relatives to the bride, the groom, or the kinsmen of the latter"},
           'name': 'EA006',
           'type': 'categorical',
           'valid_values': [1, 2, 3, 4, 5, 6, 7]},
 'EA007': {'labels': {1: 'Bride-price or bride-wealth, i.e., transfer of a substantial '
                         'consideration in the form of livestock, goods, or money from the groom '
                         'or his relatives to the kinsmen of the bride',
                      2: 'Bride-service, i.e., a substantial material consideration in which the '
                         'principal element consists of labor or other services rendered by the '
                         "groom to the bride's kinsmen",
                      3: 'Token bride-price, i.e., a small or symbolic payment only',
                      4: 'Gift exchange, i.e., reciprocal exchange of gifts of substantial value '
                         'between the relatives of the bride and groom, or a continuing exchange '
                         'of goods and services in approximately equal amounts between the groom '
                         "or his kinsmen and the bride's relatives",
                      5: 'Exchange, i.e., transfer of a sister or other female relative of the '
                         'groom in exchange for the bride',
                      6: 'Absence of any significant consideration, or bridal gifts only',
                      7: 'Dowry, i.e., transfer of a substantial amount of property from the '
                         "bride's relatives to the bride, the groom, or the kinsmen of the latter",
                      8: 'No alternate mode or supplementary practices, see "Mode of marriage '
                         '(primary)"'},
           'name': 'EA007',
           'type': 'categorical',
           'valid_values': [1, 2, 3, 4, 5, 6, 7, 8]},
 'EA008': {'labels': {1: 'Independent nuclear families with monogamy',
                      2: 'Independent nuclear families with occasional or limited polygyny',
                      3: 'Independent polyandrous families',
                      4: 'Independent polygynous families, unusual co-wives pattern (either '
                         'polygyny is preferentially sororal, with cowives in separate quarters or '
                         'it is typically non-sororal, with cowives in same quarters',
                      5: 'Independent polygynous families, usual co-wives pattern (either polygyny '
                         'is preferentially sororal, with cowives in same quarters, OR typically '
                         'non-sororal, with cowives in separate quarters)',
                      6: 'Minimal extended or "stem" families, i.e., those consisting of only two '
                         'related families of procreation (disregarding polygamous unions), '
                         'particularly of adjacent generations',
                      7: 'Small extended families, i.e., those normally embracing the families of '
                         'procreation of only one individual in the senior generation but of at '
                         'least two in the next generation. Such families usually dissolve on the '
                         'death of the head',
                      8: 'Large extended families, i.e., corporate aggregations of smaller family '
                         'units occupying a single dwelling or a number of adjacent dwellings and '
                         'normally embracing the families of procreation of at least two siblings '
                         'or cousins in each of at least two adjacent generations'},
           'name': 'EA008',
           'type': 'categorical',
           'valid_values': [1, 2, 3, 4, 5, 6, 7, 8]},
 'EA009': {'labels': {1: 'Monogamous',
                      2: 'Polygynous, with polygyny occasional or limited',
                      3: 'Polygynous, with polygyny common and preferentially sororal, and '
                         'co-wives not reported to occupy separate quarters',
                      4: 'Polygynous, with polygyny common and preferentially sororal, and '
                         'co-wives typically occupying separate quarters',
                      5: 'Polygynous, with polygyny general and not reported to be preferentially '
                         'sororal, and co-wives typically occupying separate quarters',
                      6: 'Polygynous, with polygyny general and not reported to be preferentially '
                         'sororal, and co-wives not reported to occupy separate quarters',
                      7: 'Polyandrous'},
           'name': 'EA009',
           'type': 'categorical',
           'valid_values': [1, 2, 3, 4, 5, 6, 7]},
 'EA010': {'labels': {1: 'Avunculocal, i.e., normal residence with or near the maternal uncle or '
                         'other male matrilineal kinsmen of the husband',
                      2: 'Ambilocal, i.e., residence established optionally with or near the '
                         'parents of either the husband or the wife, depending upon circumstances '
                         'or personal choice, where neither alternative exceeds the other in '
                         'actual frequency by a ratio greater than two to one.',
                      3: 'Optionally uxorilocal or avunculocal. This may be the case in a '
                         'uxorilocal society where many men marry a MoBrDa and thus, in fact, live '
                         'avunculocally',
                      4: 'Optionally patrilocal (or virilocal) or avunculocal',
                      5: 'Matrilocal, i.e., normal residence with or near the female matrilineal '
                         'kinsmen of the wife. Cf. U Uxorilocal',
                      6: 'Neolocal, i.e., normal residence apart from the relatives of both '
                         'spouses or at a place not determined by the kin ties of either',
                      7: 'Nonestablishment of a common household, i.e., where both spouses remain '
                         'in their natal households, sometimes called "duolocal" or "natolocal" '
                         'residence',
                      8: 'Patrilocal, i.e., normal residence with or near the male patrilineal '
                         'kinsmen of the husband. Cf. V Virilocal',
                      9: 'Uxorilocal. Equivalent to "matrilocal" but confined to instances where '
                         "the wife's matrikin are not aggregated in matrilocal and matrilineal kin "
                         'groups',
                      10: 'Virilocal. Equivalent to "patrilocal" but confined to instances where '
                          "the husband's patrikin are not aggregated in patrilocal and patrilineal "
                          'kin groups',
                      11: 'Ambilocal, with a marked preponderance of uxorilocal practice (i.e., '
                          'uxorilocal option exceeds virilocal option in actual frequency by a '
                          'ratio greater than two to one).',
                      12: 'Ambilocal, with a marked preponderance of virilocal practice (i.e., '
                          'virilocal option exceeds uxorilocal option in actual frequency by a '
                          'ratio greater than two to one).'},
           'name': 'EA010',
           'type': 'categorical',
           'valid_values': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]},
 'EA011': {'labels': {1: "Wife to husband's group (patrilocal, virilocal) or wife to husband's "
                         "mother's brother's household (avunculocal)",
                      2: 'Couple to either group or neolocal',
                      3: "Husband to wife's group",
                      9: 'Nonestablishment of a common household, i.e., where both spouses remain '
                         'in their natal households, sometimes called "duolocal" or "natolocal" '
                         'residence'},
           'name': 'EA011',
           'type': 'categorical',
           'valid_values': [1, 2, 3, 9]},
 'EA012': {'labels': {1: 'Avunculocal, i.e., normal residence with or near the maternal uncle or '
                         'other male matrilineal kinsmen of the husband',
                      2: 'Ambilocal, i.e., residence established optionally with or near the '
                         'parents of either the husband or the wife, depending upon circumstances '
                         'or personal choice, where neither alternative exceeds the other in '
                         'actual frequency by a ratio greater than two to one.',
                      3: 'Optionally uxorilocal or avunculocal. This may be the case in a '
                         'uxorilocal society where many men marry a MoBrDa and thus, in fact, live '
                         'avunculocally',
                      4: 'Optionally patrilocal (or virilocal) or avunculocal',
                      5: 'Matrilocal, i.e., normal residence with or near the female matrilineal '
                         'kinsmen of the wife. Cf. U Uxorilocal',
                      6: 'Neolocal, i.e., normal residence apart from the relatives of both '
                         'spouses or at a place not determined by the kin ties of either',
                      7: 'Nonestablishment of a common household, i.e., where both spouses remain '
                         'in their natal households, sometimes called "duolocal" or "natolocal" '
                         'residence',
                      8: 'Patrilocal, i.e., normal residence with or near the male patrilineal '
                         'kinsmen of the husband. Cf. V Virilocal',
                      9: 'Uxorilocal. Equivalent to "matrilocal" but confined to instances where '
                         "the wife's matrikin are not aggregated in matrilocal and matrilineal kin "
                         'groups',
                      10: 'Virilocal. Equivalent to "patrilocal" but confined to instances where '
                          "the husband's patrikin are not aggregated in patrilocal and patrilineal "
                          'kin groups',
                      11: 'Ambilocal, with a marked preponderance of uxorilocal practice (i.e., '
                          'uxorilocal option exceeds virilocal option in actual frequency by a '
                          'ratio greater than two to one).',
                      12: 'Ambilocal, with a marked preponderance of virilocal practice (i.e., '
                          'virilocal option exceeds uxorilocal option in actual frequency by a '
                          'ratio greater than two to one).'},
           'name': 'EA012',
           'type': 'categorical',
           'valid_values': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]},
 'EA013': {'labels': {1: "Wife to husband's group (patrilocal, virilocal) or wife to husband's "
                         "mother's brother's household (avunculocal)",
                      2: 'Couple to either group or neolocal',
                      3: "Husband to wife's group",
                      4: 'No common residence',
                      9: 'No alternate form'},
           'name': 'EA013',
           'type': 'categorical',
           'valid_values': [1, 2, 3, 4, 9]},
 'EA014': {'labels': {1: 'Avunculocal, i.e., normal residence with or near the maternal uncle or '
                         'other male matrilineal kinsmen of the husband',
                      2: 'Ambilocal, i.e., residence established optionally with or near the '
                         'parents of either the husband or the wife, depending upon circumstances '
                         'or personal choice, where neither alternative exceeds the other in '
                         'actual frequency by a ratio greater than two to one.',
                      3: 'Optionally uxorilocal or avunculocal. This may be the case in a '
                         'uxorilocal society where many men marry a MoBrDa and thus, in fact, live '
                         'avunculocally',
                      4: 'Optionally patrilocal (or virilocal) or avunculocal',
                      5: 'Matrilocal, i.e., normal residence with or near the female matrilineal '
                         'kinsmen of the wife. Cf. U Uxorilocal',
                      6: 'Neolocal, i.e., normal residence apart from the relatives of both '
                         'spouses or at a place not determined by the kin ties of either',
                      7: 'Nonestablishment of a common household, i.e., where both spouses remain '
                         'in their natal households, sometimes called "duolocal" or "natolocal" '
                         'residence',
                      8: 'Patrilocal, i.e., normal residence with or near the male patrilineal '
                         'kinsmen of the husband. Cf. V Virilocal',
                      9: 'Uxorilocal. Equivalent to "matrilocal" but confined to instances where '
                         "the wife's matrikin are not aggregated in matrilocal and matrilineal kin "
                         'groups',
                      10: 'Virilocal. Equivalent to "patrilocal" but confined to instances where '
                          "the husband's patrikin are not aggregated in patrilocal and patrilineal "
                          'kin groups',
                      11: 'No alternate form'},
           'name': 'EA014',
           'type': 'categorical',
           'valid_values': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]},
 'EA015': {'labels': {1: 'Demes, i.e., communities revealing a marked tendency toward local '
                         'endogamy but not segmented into clan-barrios',
                      2: 'Segmented communities, i.e., those divided into barrios, wards, or '
                         'hamlets, each of which is essentially a localized kin group, a clan or '
                         'ramage, in the absence of any indication of local exogamy. Large '
                         'extended families (see "Domestic organization"), are treated as '
                         'clan-barrios if they are integrated by a rule of ambilineal, '
                         'matrilineal, or patrilineal descent.',
                      3: 'Agamous communities without localized clans or any marked tendency '
                         'toward either local exogamy or local endogamy',
                      4: 'Exogamous communities, i.e., those revealing a marked tendency toward '
                         'local exogamy without having the specific structure of clans',
                      5: 'Segmented communities where a marked tendency toward local exogamy is '
                         'also specifically reported',
                      6: 'Clan-communities, each consisting essentially of a single localized '
                         'exogamous kin group or clan (see "Organization of clan communities" for '
                         'more detail)'},
           'name': 'EA015',
           'type': 'categorical',
           'valid_values': [1, 2, 3, 4, 5, 6]},
 'EA016': {'labels': {1: 'Clan communities not segmented into clan barrios',
                      2: 'Clan communities segmented into clan barrios',
                      9: 'Communities not organized as exogamous clan communities'},
           'name': 'EA016',
           'type': 'categorical',
           'valid_values': [1, 2, 9]},
 'EA017': {'labels': {1: 'None',
                      2: 'Absence of true patrilineal kin groups, but presence of patrilineal '
                         'exogamy',
                      3: 'Lineages of modest size, i.e., patrilineal kin groups whose core '
                         'membership is normally confined to a single community or a part thereof',
                      4: 'Sibs ("clans" in British usage), i.e., lineages whose core membership '
                         'normally comprises residents of more than one community',
                      5: 'Phratries, i.e., maximal lineages when there are more than two in the '
                         'society and when sibs are also present. Segmentary lineage systems in '
                         'which segments of a lower order of magnitude are equivalent to sibs are '
                         'also included in this category.',
                      6: 'Moieties, i.e., maximal lineages when there are only two such in the '
                         'society'},
           'name': 'EA017',
           'type': 'categorical',
           'valid_values': [1, 2, 3, 4, 5, 6]},
 'EA018': {'labels': {1: 'No patrilineal exogamy',
                      2: 'Extension of incest taboos to known patrilineal kinsmen, provided such '
                         'extension does not apply generally to bilateral kinsmen of equal '
                         'remoteness',
                      3: 'Lineages of modest size, i.e., patrilineal kin groups whose core '
                         'membership is normally confined to a single community or a part thereof',
                      4: 'Sibs ("clans" in British usage), i.e., lineages whose core membership '
                         'normally comprises residents of more than one community',
                      5: 'Phratries, i.e., maximal lineages when there are more than two in the '
                         'society and when sibs are also present. Segmentary lineage systems in '
                         'which segments of a lower order of magnitude are equivalent to sibs are '
                         'also included in this category.',
                      6: 'Moieties, i.e., maximal lineages when there are only two such in the '
                         'society'},
           'name': 'EA018',
           'type': 'categorical',
           'valid_values': [1, 2, 3, 4, 5, 6]},
 'EA019': {'labels': {1: 'None',
                      2: 'Absence of true matrilineal kin groups, but presence of matrilineal '
                         'exogamy',
                      3: 'Lineages of modest size, i.e., matrilineal kin groups whose core '
                         'membership is normally confined to a single community or a part thereof',
                      4: 'Sibs ("clans" in British usage), i.e., lineages whose core membership '
                         'normally comprises residents of more than one community',
                      5: 'Phratries, i.e., maximal lineages when there are more than two in the '
                         'society and when sibs are also present. Segmentary lineage systems in '
                         'which segments of a lower order of magnitude are equivalent to sibs are '
                         'also included in this category.',
                      6: 'Moieties, i.e., maximal lineages when there are only two such in the '
                         'society'},
           'name': 'EA019',
           'type': 'categorical',
           'valid_values': [1, 2, 3, 4, 5, 6]},
 'EA020': {'labels': {1: 'No matrilineal exogamy',
                      2: 'Extension of incest taboos to known matrilineal kinsmen, provided '
                         'extension does not apply generally to bilateral kinsmen of equal '
                         'remoteness.',
                      3: 'Lineages of modest size, i.e., matrilineal kin groups whose core '
                         'membership is normally confined to a single community or a part thereof',
                      4: 'Sibs ("clans" in British usage), i.e., lineages whose core membership '
                         'normally comprises residents of more than one community',
                      5: 'Phratries, i.e., maximal lineages when there are more than two in the '
                         'society and when sibs are also present. Segmentary lineage systems in '
                         'which segments of a lower order of magnitude are equivalent to sibs are '
                         'also included in this category.',
                      6: 'Moieties, i.e., maximal lineages when there are only two such in the '
                         'society'},
           'name': 'EA020',
           'type': 'categorical',
           'valid_values': [1, 2, 3, 4, 5, 6]},
 'EA021': {'labels': {1: 'Bilateral descent as inferred from the absence of reported ambilineal, '
                         'matrilineal, or patrilineal kin groups, kindreds being absent or '
                         'unreported',
                      2: 'Kindreds: bilateral descent with specifically reported kindreds, i.e., '
                         'Ego-oriented bilateral kin groups or categories',
                      3: 'Ambilineal descent inferred from the presence of ambilocal extended '
                         'families, true ramages being absent or unreported',
                      4: 'Ramages, i.e., ancestor-oriented ambilineal kin groups, if they are '
                         'agamous, endogamous, or not specifically stated to be exogamous',
                      5: 'Exogamous ramages specifically reported',
                      6: 'Bilateral descent with reported or probable quasi-lineages, i.e., '
                         'cognatic groups approximating the structure of lineages but based on '
                         'filiation rather than on unilineal or ambilineal descent',
                      9: 'Absence of cognatic kin groups as inferred from the presence of '
                         'unilineal descent'},
           'name': 'EA021',
           'type': 'categorical',
           'valid_values': [1, 2, 3, 4, 5, 6, 9]},
 'EA022': {'labels': {2: 'Kindreds: bilateral descent with specifically reported kindreds, i.e., '
                         'Ego-oriented bilateral kin groups or categories',
                      4: 'Ramages, i.e., ancestor-oriented ambilineal kin groups, if they are '
                         'agamous, endogamous, or not specifically stated to be exogamous',
                      9: 'No secondary cognatic groups'},
           'name': 'EA022',
           'type': 'categorical',
           'valid_values': [2, 4, 9]},
 'EA023': {'labels': {1: 'Duolateral cross-cousin marriage permitted, i.e., marriage allowed with '
                         'either MoBrDa or FaSiDa but forbidden with a parallel cousin',
                      2: 'Duolateral marriage permitted with paternal cousins only (FaBrDa or '
                         'FaSiDa)',
                      3: 'Duolateral marriage permitted with maternal cousins only (MoBrDa or '
                         'MoSiDa)',
                      4: "Duolateral marriage permitted with an uncle's daughter only (FaBrDa or "
                         'MoBrDa)',
                      5: "Duolateral marriage permitted with an aunt's daughter only (FaSiDa or "
                         'MoSiDa)',
                      6: 'Unilateral: only matrilateral cross-cousin marriage permitted, i.e., '
                         'with a MoBrDa',
                      7: 'Nonlateral marriage, i.e., unions forbidden with any first or second '
                         'cousin',
                      8: 'Nonlateral marriage, evidence available only for first cousins',
                      9: 'Unilateral: only patrilateral cross-cousin marriage permitted i.e., with '
                         'a FaSiDa',
                      10: 'Quadrilateral marriage, i.e., marriage allowed with any first cousin',
                      11: 'Nonlateral marriage in which all first cousins and some but not all '
                          'second cousins are forbidden as spouses',
                      12: 'Nonlateral marriage in which unions are forbidden with any first cousin '
                          'but are permitted with any second cousin (or at least any who is not a '
                          'lineage mate)',
                      13: 'Trilateral marriage, i.e., marriage allowed with any first cousin '
                          'except an orthocousin or lineage mate'},
           'name': 'EA023',
           'type': 'categorical',
           'valid_values': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]},
 'EA024': {'labels': {1: 'Quadrilateral marriage, i.e., marriage allowed with any first cousin',
                      2: 'Trilateral marriage, i.e., marriage allowed with any first cousin except '
                         'an orthocousin or lineage mate',
                      3: 'Two of four first cousins marriageable',
                      4: 'One of four first cousins marriageable',
                      5: 'Nonlateral marriage in which unions are forbidden with any first cousin '
                         'but are permitted with any second cousin (or at least any who is not a '
                         'lineage mate)',
                      6: 'Nonlateral marriage in which all first cousins and some but not all '
                         'second cousins are forbidden as spouses',
                      7: 'Nonlateral marriage when evidence is available only for first cousins',
                      8: 'Nonlateral marriage, i.e., unions forbidden with any first or second '
                         'cousin'},
           'name': 'EA024',
           'type': 'categorical',
           'valid_values': [1, 2, 3, 4, 5, 6, 7, 8]},
 'EA025': {'labels': {1: 'Duolateral, symmetrical preference for MoBrDa or FaSiDa',
                      2: 'Duolateral, matrilateral preference (MoBrDa)',
                      3: 'Duolateral, patrilateral preference (FaSiDa)',
                      4: 'Duolateral, with maternal cousins only and MoBrDa preferred',
                      5: 'Unilateral: matrilateral cross-cousin marriage to MoBrDa preferred '
                         'rather than merely permitted',
                      6: 'Unilateral: patrilateral cross-cousin marriage to FaSiDa preferred '
                         'rather than merely permitted',
                      7: 'Quadrilateral, where FaBrDa is the preferred mate',
                      8: 'Quadrilateral, symmetrical preference (FaSiDa or MoBrDa)',
                      9: 'Quadrilateral, matrilateral preference (MoSi__ or MoBr__)',
                      10: 'Nonlateral, with preference for particular second cross-cousins only, '
                          'notably MoMoBrDaDa or FaMoBrSoDa, often reported of societies with '
                          'subsection systems',
                      11: 'Nonlateral, with second-cousin marriage preferred rather than merely '
                          'permitted',
                      12: 'Trilateral marriage, with preference for a bilateral cross-cousin '
                          '(MoBrDa = FaSiDa).',
                      13: 'Trilateral marriage, with preference for a matrilateral cross-cousin '
                          '(MoBrDa)',
                      14: 'Trilateral marriage, with preference for a patrilateral cross-cousin '
                          '(FaSiDa)',
                      15: 'No preferred cousin marriages'},
           'name': 'EA025',
           'type': 'categorical',
           'valid_values': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]},
 'EA026': {'labels': {1: 'A symmetrical cross-cousin is preferred spouse',
                      2: 'MoBrDa is preferred spouse',
                      3: 'FaSiDa is preferred spouse',
                      4: 'FaBrDa is preferred spouse',
                      5: 'A second-cousin is preferred spouse',
                      9: 'No preferred cousin marriage'},
           'name': 'EA026',
           'type': 'categorical',
           'valid_values': [1, 2, 3, 4, 5, 9]},
 'EA027': {'labels': {1: 'Crow, i.e., FaSiCh equated with Fa or FaSi and/or MoBrCh with Ch or '
                         'BrCh(ws)',
                      2: 'Descriptive or derivative, rather than elementary, terms employed for '
                         'all cousins',
                      3: 'Eskimo, i.e., FaBrCh, FaSiCh, MoBrCh, and MoSiCh equated with each other '
                         'but differentiated from siblings',
                      4: 'Hawaiian, i.e., all cousins equated with siblings or called by terms '
                         'clearly derivative from those for siblings',
                      5: 'Iroquois, i.e., FaSiCh equated with MoBrCh but differentiated from both '
                         'siblings and parallel cousins',
                      6: 'Omaha, i.e., MoBrCh equated with MoBr or Mo and/or FaSiCh with SiCh(ms) '
                         'or Ch',
                      7: 'Sudanese, i.e., FaSiCh and MoBrCh distinguished alike from siblings, '
                         'parallel cousins, and each other but without conforming to either the '
                         'Crow, the descriptive, or the Omaha patterns',
                      8: 'Mixed or variant patterns not adequately represented by any of the '
                         'foregoing symbols. The details are given under "Classification by '
                         'Clusters."'},
           'name': 'EA027',
           'type': 'categorical',
           'valid_values': [1, 2, 3, 4, 5, 6, 7, 8]},
 'EA028': {'labels': {1: 'Complete absence of agriculture',
                      2: 'Casual agriculture, i.e., the slight or sporadic cultivation of food or '
                         'other plants incidental to a primary dependence upon other subsistence '
                         'practices',
                      3: 'Extensive or shifting cultivation, as where new fields are cleared '
                         'annually, cultivated for a year or two, and then allowed to revert to '
                         'forest or brush for a long fallow period',
                      4: 'Horticulture, i.e., semi-intensive agriculture limited mainly to '
                         'vegetable gardens or groves of fruit trees rather than the cultivation '
                         'of field crops',
                      5: 'Intensive agriculture on permanent fields, utilizing fertilization by '
                         'compost or animal manure, crop rotation, or other techniques so that '
                         'fallowing is either unnecessary or is confined to relatively short '
                         'periods',
                      6: 'Intensive cultivation where it is largely dependent upon irrigation'},
           'name': 'EA028',
           'type': 'categorical',
           'valid_values': [1, 2, 3, 4, 5, 6]},
 'EA029': {'labels': {1: 'No agriculture',
                      2: 'Non-food crops only, e.g., cotton or tobacco',
                      3: 'Vegetables, e.g., cucurbits, greens, or legumes, when more important '
                         'than other crops',
                      4: 'Tree fruits, e.g., bananas, breadfruit, coconuts, or dates, when more '
                         'important than cereal grains and root crops. Sago, unless specifically '
                         'reported to be cultivated, is treated as a gathered product rather than '
                         'a cultivated one',
                      5: 'Roots or tubers, e.g., manioc, potatoes, taro, or yams, when more '
                         'important than cereal grains and at least as important as tree crops or '
                         'vegetables',
                      6: 'Cereal grains, e.g., maize, millet, rice, or wheat, when at least as '
                         'important as any other type of crop'},
           'name': 'EA029',
           'type': 'categorical',
           'valid_values': [1, 2, 3, 4, 5, 6]},
 'EA030': {'labels': {1: 'Fully migratory or nomadic bands',
                      2: 'Seminomadic communities whose members wander in bands for at least half '
                         'of the year but occupy a fixed settlement at some season or seasons, '
                         'e.g., recurrently occupied winter quarters',
                      3: 'Semisedentary communities whose members shift from one to another fixed '
                         'settlement at different seasons or who occupy more or less permanently a '
                         'single settlement from which a substantial proportion of the population '
                         'departs seasonally to occupy shifting camps, e.g., during transhumance',
                      4: 'Compact but impermanent settlements, i.e., villages whose location is '
                         'shifted every few years',
                      5: 'Neighborhoods of dispersed family homesteads',
                      6: 'Separated hamlets where several such form a more or less permanent '
                         'single community',
                      7: 'Compact and relatively permanent settlements, i.e., nucleated villages '
                         'or towns',
                      8: 'Complex settlements consisting of a nucleated village or town with '
                         'outlying homesteads or satellite hamlets. Urban aggregations of '
                         'population are not separately indicated since EA031 deals with community '
                         'size'},
           'name': 'EA030',
           'type': 'categorical',
           'valid_values': [1, 2, 3, 4, 5, 6, 7, 8]},
 'EA031': {'labels': {1: 'Fewer than 50 persons',
                      2: 'From 50 to 99 persons',
                      3: 'From 100 to 199 persons',
                      4: 'From 200 to 399 persons',
                      5: 'From 400 to 1,000 persons',
                      6: 'More than 1,000 persons in the absence of indigenous urban aggregations '
                         'of more than 5,000',
                      7: 'One or more indigenous towns of more than 5,000 inhabitants but none of '
                         'more than 50,000',
                      8: 'One or more indigenous cities with more than 50,000 inhabitants'},
           'name': 'EA031',
           'type': 'categorical',
           'valid_values': [1, 2, 3, 4, 5, 6, 7, 8]},
 'EA032': {'labels': {2: 'Independent families (may be nuclear or polygynous)',
                      3: 'Extended families',
                      4: 'Clan-barrios'},
           'name': 'EA032',
           'type': 'categorical',
           'valid_values': [2, 3, 4]},
 'EA033': {'labels': {1: 'No political authority beyond community (e.g., autonomous bands and '
                         'villages)',
                      2: 'One level (e.g., petty chiefdoms)',
                      3: 'Two levels (e.g., larger chiefdoms)',
                      4: 'Three levels (e.g., states)',
                      5: 'Four levels (e.g., large states)'},
           'name': 'EA033',
           'type': 'categorical',
           'valid_values': [1, 2, 3, 4, 5]},
 'EA034': {'labels': {1: 'A high god absent or not reported in substantial descriptions of '
                         'religious beliefs',
                      2: 'A high god present but otiose or not concerned with human affairs',
                      3: 'A high god present and active in human affairs but not offering positive '
                         'support to human morality',
                      4: 'A high god present, active, and specifically supportive of human '
                         'morality'},
           'name': 'EA034',
           'type': 'categorical',
           'valid_values': [1, 2, 3, 4]},
 'EA035': {'labels': {1: 'No games of any of the three types',
                      2: 'Games of physical skill only, whether or not they may also involve '
                         'incidental elements of chance or strategy, e.g., foot racing, wrestling, '
                         'the hoop-and-pole game',
                      3: 'Games of chance only, with no significant element of either physical '
                         'skill or strategy involved, e.g., dice games',
                      4: 'Games of physical skill and of chance both present',
                      5: 'Games of strategy only, involving no significant element of physical '
                         'skill, e.g., chess, go, poker. Whether or not an element of chance is '
                         'also involved is considered irrelevant',
                      6: 'Games of physical skill and of strategy present, but not games of chance',
                      7: 'Games of chance and of strategy present, but not games of physical skill',
                      8: 'Games of all three types present'},
           'name': 'EA035',
           'type': 'categorical',
           'valid_values': [1, 2, 3, 4, 5, 6, 7, 8]},
 'EA036': {'labels': {1: 'No taboo, especially where the husband is expected to have intercourse '
                         'with his wife as soon as possible after childbirth for the alleged '
                         'benefit of the child',
                      2: 'Short post-partum taboo, lasting not more than one month',
                      3: 'Duration of from more than a month to six months',
                      4: 'Duration of from more than six months to one year',
                      5: 'Duration of from more than one year to two years',
                      6: 'Duration of more than two years'},
           'name': 'EA036',
           'type': 'categorical',
           'valid_values': [1, 2, 3, 4, 5, 6]},
 'EA037': {'labels': {1: 'Absent or not generally practiced',
                      2: 'Performed shortly after birth, i.e., within the first two months',
                      3: 'Performed during infancy, i.e., from two months to two years of age',
                      4: 'Performed during early childhood, i.e., from two to five years of age',
                      5: 'Performed during late childhood, i.e., from six to ten years of age',
                      6: 'Performed during adolescence, i.e., from eleven to fifteen years of age',
                      7: 'Performed during early adulthood, i.e., from sixteen to 25 years of age',
                      8: 'Performed during maturity, i.e., from 25 to 50 years of age',
                      9: 'Performed in old age, i.e., after 50 years of age',
                      10: 'Circumcision customary, but the normal age is unspecified or unclear'},
           'name': 'EA037',
           'type': 'categorical',
           'valid_values': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]},
 'EA038': {'labels': {1: 'Absence of segregation, adolescent boys residing and sleeping in the '
                         'same dwelling as their mothers and sisters',
                      2: 'Partial segregation, adolescent boys residing or eating with their natal '
                         'families but sleeping apart from them, e.g., in a special hut or in a '
                         'cattle shed',
                      3: 'Complete segregation, in which adolescent boys go to live as individuals '
                         'with relatives outside the nuclear family, e.g., with grandparents or '
                         'with a maternal or paternal uncle',
                      4: 'Complete segregation, in which adolescent boys go to live as individuals '
                         'with non-relatives, e.g., as retainers to a chief or as apprentices to '
                         'specialists',
                      5: 'Complete segregation, in which boys reside with a group of their own '
                         'peers, e.g., in bachelor dormitories, military regiments, or '
                         'age-villages'},
           'name': 'EA038',
           'type': 'categorical',
           'valid_values': [1, 2, 3, 4, 5]},
 'EA039': {'labels': {1: 'Absent (no plow animals)',
                      2: 'Plow cultivation not aboriginal but well established at the period of '
                         'observation',
                      3: 'Animals employed in plow cultivation prior to the contact period'},
           'name': 'EA039',
           'type': 'categorical',
           'valid_values': [1, 2, 3]},
 'EA040': {'labels': {1: 'Absence or near absence of domestic animals other than bees, eats, dogs, '
                         'fowl, guinea pigs, or the like',
                      2: 'Pigs the only domestic animals of consequence',
                      3: 'Sheep and/or goats when larger domestic animals are absent or much less '
                         'important',
                      4: 'Equine animals, e.g., horses, donkeys',
                      5: 'Deer, e.g., reindeer',
                      6: 'Camels or other animals of related genera, e.g., alpacas, llamas',
                      7: 'Bovine animals, e.g., cattle, mithun, water buffaloes, yaks'},
           'name': 'EA040',
           'type': 'categorical',
           'valid_values': [1, 2, 3, 4, 5, 6, 7]},
 'EA041': {'labels': {1: 'Absence or near absence of milking',
                      2: 'Domestic animals milked more often than sporadically'},
           'name': 'EA041',
           'type': 'categorical',
           'valid_values': [1, 2]},
 'EA042': {'labels': {1: 'Gathering contributes most',
                      2: 'Fishing contributes most',
                      3: 'Hunting contributes most',
                      4: 'Pastoralism contributes most',
                      5: 'Casual agriculture contributes most',
                      6: 'Extensive agriculture contributes most',
                      7: 'Intensive agriculture contributes most',
                      8: 'Two or more sources contribute equally',
                      9: 'Agriculture contributes most, type unknown'},
           'name': 'EA042',
           'type': 'categorical',
           'valid_values': [1, 2, 3, 4, 5, 6, 7, 8, 9]},
 'EA043': {'labels': {1: 'Patrilineal (EA017 > 1, EA019 = 1, EA021 = 9)',
                      2: 'Duolateral (EA017 > 1, EA019 > 1, EA021 = 9 or EA021 = 0)',
                      3: 'Matrilineal (EA017 = 1, EA019 > 1, EA021 = 9)',
                      4: 'Quasi-lineages (EA017 = 1, EA019 = 1, EA021 = 6)',
                      5: 'Ambilineal (EA017 = 1, EA019 = 1, EA021 = 3 or EA021 = 4 or EA021 = 5)',
                      6: 'Bilateral (EA017 = 1, EA019 = 1, EA021 = 1 or EA021 = 2)',
                      7: 'Mixed (EA017  and/or EA019 > 1,and EA021 not equal to 9)'},
           'name': 'EA043',
           'type': 'categorical',
           'valid_values': [1, 2, 3, 4, 5, 6, 7]},
 'EA044': {'labels': {1: 'Males alone perform the activity, female participation being negligible',
                      2: 'Both sexes participate, but males do appreciably more than females',
                      3: 'Differentiation of specific tasks by sex but approximately equal '
                         'participation by both sexes in the total activity',
                      4: 'Equal participation by both sexes without marked or reported '
                         'differentiation in specific tasks',
                      5: 'Both sexes participate, but females do appreciably more than males',
                      6: 'Females alone perform the activity, male participation being negligible',
                      7: 'Sex participation irrelevant, especially where production is '
                         'industrialized',
                      8: 'The activity is present, but sex participation is unspecified in the '
                         'sources consulted',
                      9: 'The activity is absent or unimportant in the particular society'},
           'name': 'EA044',
           'type': 'categorical',
           'valid_values': [1, 2, 3, 4, 5, 6, 7, 8, 9]},
 'EA045': {'labels': {1: 'Males alone perform the activity, female participation being negligible',
                      2: 'Both sexes participate, but males do appreciably more than females',
                      3: 'Differentiation of specific tasks by sex but approximately equal '
                         'participation by both sexes in the total activity',
                      4: 'Equal participation by both sexes without marked or reported '
                         'differentiation in specific tasks',
                      5: 'Both sexes participate, but females do appreciably more than males',
                      6: 'Females alone perform the activity, male participation being negligible',
                      7: 'Sex participation irrelevant, especially where production is '
                         'industrialized',
                      8: 'The activity is present, but sex participation is unspecified in the '
                         'sources consulted',
                      9: 'The activity is absent or unimportant in the particular society'},
           'name': 'EA045',
           'type': 'categorical',
           'valid_values': [1, 2, 3, 4, 5, 6, 7, 8, 9]},
 'EA046': {'labels': {1: 'Males alone perform the activity, female participation being negligible',
                      2: 'Both sexes participate, but males do appreciably more than females',
                      3: 'Differentiation of specific tasks by sex but approximately equal '
                         'participation by both sexes in the total activity',
                      4: 'Equal participation by both sexes without marked or reported '
                         'differentiation in specific tasks',
                      5: 'Both sexes participate, but females do appreciably more than males',
                      6: 'Females alone perform the activity, male participation being negligible',
                      7: 'Sex participation irrelevant, especially where production is '
                         'industrialized',
                      8: 'The activity is present, but sex participation is unspecified in the '
                         'sources consulted',
                      9: 'The activity is absent or unimportant in the particular society'},
           'name': 'EA046',
           'type': 'categorical',
           'valid_values': [1, 2, 3, 4, 5, 6, 7, 8, 9]},
 'EA047': {'labels': {1: 'Males alone perform the activity, female participation being negligible',
                      2: 'Both sexes participate, but males do appreciably more than females',
                      3: 'Differentiation of specific tasks by sex but approximately equal '
                         'participation by both sexes in the total activity',
                      4: 'Equal participation by both sexes without marked or reported '
                         'differentiation in specific tasks',
                      5: 'Both sexes participate, but females do appreciably more than males',
                      6: 'Females alone perform the activity, male participation being negligible',
                      7: 'Sex participation irrelevant, especially where production is '
                         'industrialized',
                      8: 'The activity is present, but sex participation is unspecified in the '
                         'sources consulted',
                      9: 'The activity is absent or unimportant in the particular society'},
           'name': 'EA047',
           'type': 'categorical',
           'valid_values': [1, 2, 3, 4, 5, 6, 7, 8, 9]},
 'EA048': {'labels': {1: 'Males alone perform the activity, female participation being negligible',
                      2: 'Both sexes participate, but males do appreciably more than females',
                      3: 'Differentiation of specific tasks by sex but approximately equal '
                         'participation by both sexes in the total activity',
                      4: 'Equal participation by both sexes without marked or reported '
                         'differentiation in specific tasks',
                      5: 'Both sexes participate, but females do appreciably more than males',
                      6: 'Females alone perform the activity, male participation being negligible',
                      7: 'Sex participation irrelevant, especially where production is '
                         'industrialized',
                      8: 'The activity is present, but sex participation is unspecified in the '
                         'sources consulted',
                      9: 'The activity is absent or unimportant in the particular society'},
           'name': 'EA048',
           'type': 'categorical',
           'valid_values': [1, 2, 3, 4, 5, 6, 7, 8, 9]},
 'EA049': {'labels': {1: 'Males alone perform the activity, female participation being negligible',
                      2: 'Both sexes participate, but males do appreciably more than females',
                      3: 'Differentiation of specific tasks by sex but approximately equal '
                         'participation by both sexes in the total activity',
                      4: 'Equal participation by both sexes without marked or reported '
                         'differentiation in specific tasks',
                      5: 'Both sexes participate, but females do appreciably more than males',
                      6: 'Females alone perform the activity, male participation being negligible',
                      7: 'Sex participation irrelevant, especially where production is '
                         'industrialized',
                      8: 'The activity is present, but sex participation is unspecified in the '
                         'sources consulted',
                      9: 'The activity is absent or unimportant in the particular society'},
           'name': 'EA049',
           'type': 'categorical',
           'valid_values': [1, 2, 3, 4, 5, 6, 7, 8, 9]},
 'EA050': {'labels': {1: 'Males alone perform the activity, female participation being negligible',
                      2: 'Both sexes participate, but males do appreciably more than females',
                      3: 'Differentiation of specific tasks by sex but approximately equal '
                         'participation by both sexes in the total activity',
                      4: 'Equal participation by both sexes without marked or reported '
                         'differentiation in specific tasks',
                      5: 'Both sexes participate, but females do appreciably more than males',
                      6: 'Females alone perform the activity, male participation being negligible',
                      7: 'Sex participation irrelevant, especially where production is '
                         'industrialized',
                      8: 'The activity is present, but sex participation is unspecified in the '
                         'sources consulted',
                      9: 'The activity is absent or unimportant in the particular society'},
           'name': 'EA050',
           'type': 'categorical',
           'valid_values': [1, 2, 3, 4, 5, 6, 7, 8, 9]},
 'EA051': {'labels': {1: 'Males alone perform the activity, female participation being negligible',
                      2: 'Both sexes participate, but males do appreciably more than females',
                      3: 'Differentiation of specific tasks by sex but approximately equal '
                         'participation by both sexes in the total activity',
                      4: 'Equal participation by both sexes without marked or reported '
                         'differentiation in specific tasks',
                      5: 'Both sexes participate, but females do appreciably more than males',
                      6: 'Females alone perform the activity, male participation being negligible',
                      7: 'Sex participation irrelevant, especially where production is '
                         'industrialized',
                      8: 'The activity is present, but sex participation is unspecified in the '
                         'sources consulted',
                      9: 'The activity is absent or unimportant in the particular society'},
           'name': 'EA051',
           'type': 'categorical',
           'valid_values': [1, 2, 3, 4, 5, 6, 7, 8, 9]},
 'EA052': {'labels': {1: 'Males alone perform the activity, female participation being negligible',
                      2: 'Both sexes participate, but males do appreciably more than females',
                      3: 'Differentiation of specific tasks by sex but approximately equal '
                         'participation by both sexes in the total activity',
                      4: 'Equal participation by both sexes without marked or reported '
                         'differentiation in specific tasks',
                      5: 'Both sexes participate, but females do appreciably more than males',
                      6: 'Females alone perform the activity, male participation being negligible',
                      7: 'Sex participation irrelevant, especially where production is '
                         'industrialized',
                      8: 'The activity is present, but sex participation is unspecified in the '
                         'sources consulted',
                      9: 'The activity is absent or unimportant in the particular society'},
           'name': 'EA052',
           'type': 'categorical',
           'valid_values': [1, 2, 3, 4, 5, 6, 7, 8, 9]},
 'EA053': {'labels': {1: 'Males alone perform the activity, female participation being negligible',
                      2: 'Both sexes participate, but males do appreciably more than females',
                      3: 'Differentiation of specific tasks by sex but approximately equal '
                         'participation by both sexes in the total activity',
                      4: 'Equal participation by both sexes without marked or reported '
                         'differentiation in specific tasks',
                      5: 'Both sexes participate, but females do appreciably more than males',
                      6: 'Females alone perform the activity, male participation being negligible',
                      7: 'Sex participation irrelevant, especially where production is '
                         'industrialized',
                      8: 'The activity is present, but sex participation is unspecified in the '
                         'sources consulted',
                      9: 'The activity is absent or unimportant in the particular society'},
           'name': 'EA053',
           'type': 'categorical',
           'valid_values': [1, 2, 3, 4, 5, 6, 7, 8, 9]},
 'EA054': {'labels': {1: 'Males alone perform the activity, female participation being negligible',
                      2: 'Both sexes participate, but males do appreciably more than females',
                      3: 'Differentiation of specific tasks by sex but approximately equal '
                         'participation by both sexes in the total activity',
                      4: 'Equal participation by both sexes without marked or reported '
                         'differentiation in specific tasks',
                      5: 'Both sexes participate, but females do appreciably more than males',
                      6: 'Females alone perform the activity, male participation being negligible',
                      7: 'Sex participation irrelevant, especially where production is '
                         'industrialized',
                      8: 'The activity is present, but sex participation is unspecified in the '
                         'sources consulted',
                      9: 'The activity is absent or unimportant in the particular society'},
           'name': 'EA054',
           'type': 'categorical',
           'valid_values': [1, 2, 3, 4, 5, 6, 7, 8, 9]},
 'EA055': {'labels': {1: 'Junior age specialization, i.e., the activity is largely performed by '
                         'boys and/or girls before the age of puberty',
                      2: 'Senior age specialization, i.e., the activity is largely performed by '
                         'men and/or women beyond the prime of life',
                      3: 'Craft specialization, i.e., the activity is largely performed by a small '
                         'minority of adult males or females who possess specialized skills. '
                         'Occupational castes are treated as instances of craft specialization',
                      4: 'Industrial specialization, i.e., the activity is largely removed from '
                         'the domain of a division of labor by sex, age, or craft specialization '
                         'and is performed industrialized mainly by techniques of production',
                      9: 'Normally performed by many or most adult men, women, or both',
                      10: 'The activity is absent or unimportant in the particular society'},
           'name': 'EA055',
           'type': 'categorical',
           'valid_values': [1, 2, 3, 4, 9, 10]},
 'EA056': {'labels': {1: 'Junior age specialization, i.e., the activity is largely performed by '
                         'boys and/or girls before the age of puberty',
                      2: 'Senior age specialization, i.e., the activity is largely performed by '
                         'men and/or women beyond the prime of life',
                      3: 'Craft specialization, i.e., the activity is largely performed by a small '
                         'minority of adult males or females who possess specialized skills. '
                         'Occupational castes are treated as instances of craft specialization',
                      4: 'Industrial specialization, i.e., the activity is largely removed from '
                         'the domain of a division of labor by sex, age, or craft specialization '
                         'and is performed industrialized mainly by techniques of production',
                      9: 'Normally performed by many or most adult men, women, or both',
                      10: 'The activity is absent or unimportant in the particular society'},
           'name': 'EA056',
           'type': 'categorical',
           'valid_values': [1, 2, 3, 4, 9, 10]},
 'EA057': {'labels': {1: 'Junior age specialization, i.e., the activity is largely performed by '
                         'boys and/or girls before the age of puberty',
                      2: 'Senior age specialization, i.e., the activity is largely performed by '
                         'men and/or women beyond the prime of life',
                      3: 'Craft specialization, i.e., the activity is largely performed by a small '
                         'minority of adult males or females who possess specialized skills. '
                         'Occupational castes are treated as instances of craft specialization',
                      4: 'Industrial specialization, i.e., the activity is largely removed from '
                         'the domain of a division of labor by sex, age, or craft specialization '
                         'and is performed industrialized mainly by techniques of production',
                      9: 'Normally performed by many or most adult men, women, or both',
                      10: 'The activity is absent or unimportant in the particular society'},
           'name': 'EA057',
           'type': 'categorical',
           'valid_values': [1, 2, 3, 4, 9, 10]},
 'EA058': {'labels': {1: 'Junior age specialization, i.e., the activity is largely performed by '
                         'boys and/or girls before the age of puberty',
                      2: 'Senior age specialization, i.e., the activity is largely performed by '
                         'men and/or women beyond the prime of life',
                      3: 'Craft specialization, i.e., the activity is largely performed by a small '
                         'minority of adult males or females who possess specialized skills. '
                         'Occupational castes are treated as instances of craft specialization',
                      4: 'Industrial specialization, i.e., the activity is largely removed from '
                         'the domain of a division of labor by sex, age, or craft specialization '
                         'and is performed industrialized mainly by techniques of production',
                      9: 'Normally performed by many or most adult men, women, or both',
                      10: 'The activity is absent or unimportant in the particular society'},
           'name': 'EA058',
           'type': 'categorical',
           'valid_values': [1, 2, 3, 4, 9, 10]},
 'EA059': {'labels': {1: 'Junior age specialization, i.e., the activity is largely performed by '
                         'boys and/or girls before the age of puberty',
                      2: 'Senior age specialization, i.e., the activity is largely performed by '
                         'men and/or women beyond the prime of life',
                      3: 'Craft specialization, i.e., the activity is largely performed by a small '
                         'minority of adult males or females who possess specialized skills. '
                         'Occupational castes are treated as instances of craft specialization',
                      4: 'Industrial specialization, i.e., the activity is largely removed from '
                         'the domain of a division of labor by sex, age, or craft specialization '
                         'and is performed industrialized mainly by techniques of production',
                      9: 'Normally performed by many or most adult men, women, or both',
                      10: 'The activity is absent or unimportant in the particular society'},
           'name': 'EA059',
           'type': 'categorical',
           'valid_values': [1, 2, 3, 4, 9, 10]},
 'EA060': {'labels': {1: 'Junior age specialization, i.e., the activity is largely performed by '
                         'boys and/or girls before the age of puberty',
                      2: 'Senior age specialization, i.e., the activity is largely performed by '
                         'men and/or women beyond the prime of life',
                      3: 'Craft specialization, i.e., the activity is largely performed by a small '
                         'minority of adult males or females who possess specialized skills. '
                         'Occupational castes are treated as instances of craft specialization',
                      4: 'Industrial specialization, i.e., the activity is largely removed from '
                         'the domain of a division of labor by sex, age, or craft specialization '
                         'and is performed industrialized mainly by techniques of production',
                      9: 'Normally performed by many or most adult men, women, or both',
                      10: 'The activity is absent or unimportant in the particular society'},
           'name': 'EA060',
           'type': 'categorical',
           'valid_values': [1, 2, 3, 4, 9, 10]},
 'EA061': {'labels': {1: 'Junior age specialization, i.e., the activity is largely performed by '
                         'boys and/or girls before the age of puberty',
                      2: 'Senior age specialization, i.e., the activity is largely performed by '
                         'men and/or women beyond the prime of life',
                      3: 'Craft specialization, i.e., the activity is largely performed by a small '
                         'minority of adult males or females who possess specialized skills. '
                         'Occupational castes are treated as instances of craft specialization',
                      4: 'Industrial specialization, i.e., the activity is largely removed from '
                         'the domain of a division of labor by sex, age, or craft specialization '
                         'and is performed industrialized mainly by techniques of production',
                      9: 'Normally performed by many or most adult men, women, or both',
                      10: 'The activity is absent or unimportant in the particular society'},
           'name': 'EA061',
           'type': 'categorical',
           'valid_values': [1, 2, 3, 4, 9, 10]},
 'EA062': {'labels': {1: 'Junior age specialization, i.e., the activity is largely performed by '
                         'boys and/or girls before the age of puberty',
                      2: 'Senior age specialization, i.e., the activity is largely performed by '
                         'men and/or women beyond the prime of life',
                      3: 'Craft specialization, i.e., the activity is largely performed by a small '
                         'minority of adult males or females who possess specialized skills. '
                         'Occupational castes are treated as instances of craft specialization',
                      4: 'Industrial specialization, i.e., the activity is largely removed from '
                         'the domain of a division of labor by sex, age, or craft specialization '
                         'and is performed industrialized mainly by techniques of production',
                      9: 'Normally performed by many or most adult men, women, or both',
                      10: 'The activity is absent or unimportant in the particular society'},
           'name': 'EA062',
           'type': 'categorical',
           'valid_values': [1, 2, 3, 4, 9, 10]},
 'EA063': {'labels': {1: 'Junior age specialization, i.e., the activity is largely performed by '
                         'boys and/or girls before the age of puberty',
                      2: 'Senior age specialization, i.e., the activity is largely performed by '
                         'men and/or women beyond the prime of life',
                      3: 'Craft specialization, i.e., the activity is largely performed by a small '
                         'minority of adult males or females who possess specialized skills. '
                         'Occupational castes are treated as instances of craft specialization',
                      4: 'Industrial specialization, i.e., the activity is largely removed from '
                         'the domain of a division of labor by sex, age, or craft specialization '
                         'and is performed industrialized mainly by techniques of production',
                      9: 'Normally performed by many or most adult men, women, or both',
                      10: 'The activity is absent or unimportant in the particular society'},
           'name': 'EA063',
           'type': 'categorical',
           'valid_values': [1, 2, 3, 4, 9, 10]},
 'EA064': {'labels': {1: 'Junior age specialization, i.e., the activity is largely performed by '
                         'boys and/or girls before the age of puberty',
                      2: 'Senior age specialization, i.e., the activity is largely performed by '
                         'men and/or women beyond the prime of life',
                      3: 'Craft specialization, i.e., the activity is largely performed by a small '
                         'minority of adult males or females who possess specialized skills. '
                         'Occupational castes are treated as instances of craft specialization',
                      4: 'Industrial specialization, i.e., the activity is largely removed from '
                         'the domain of a division of labor by sex, age, or craft specialization '
                         'and is performed industrialized mainly by techniques of production',
                      9: 'Normally performed by many or most adult men, women, or both',
                      10: 'The activity is absent or unimportant in the particular society'},
           'name': 'EA064',
           'type': 'categorical',
           'valid_values': [1, 2, 3, 4, 9, 10]},
 'EA065': {'labels': {1: 'Junior age specialization, i.e., the activity is largely performed by '
                         'boys and/or girls before the age of puberty',
                      2: 'Senior age specialization, i.e., the activity is largely performed by '
                         'men and/or women beyond the prime of life',
                      3: 'Craft specialization, i.e., the activity is largely performed by a small '
                         'minority of adult males or females who possess specialized skills. '
                         'Occupational castes are treated as instances of craft specialization',
                      4: 'Industrial specialization, i.e., the activity is largely removed from '
                         'the domain of a division of labor by sex, age, or craft specialization '
                         'and is performed industrialized mainly by techniques of production',
                      9: 'Normally performed by many or most adult men, women, or both',
                      10: 'The activity is absent or unimportant in the particular society'},
           'name': 'EA065',
           'type': 'categorical',
           'valid_values': [1, 2, 3, 4, 9, 10]},
 'EA066': {'labels': {1: 'Absence of significant class distinctions among freemen (slavery is '
                         'treated in EA070), ignoring variations in individual repute achieved '
                         'through skill, valor, piety, or wisdom',
                      2: 'Wealth distinctions, based on the possession or distribution of '
                         'property, present and socially important but not crystallized into '
                         'distinct and hereditary social classes',
                      3: 'Elite stratification, in which an elite class derives its superior '
                         'status from, and perpetuates it through, control over scarce resources, '
                         'particularly land, and is thereby differentiated from a property-less '
                         'proletariat or serf class',
                      4: 'Dual stratification into a hereditary aristocracy and a lower class of '
                         'ordinary commoners or freemen, where traditionally ascribed noble status '
                         'is at least as decisive as control over scarce resources',
                      5: 'Complex stratification into social classes correlated in large measure '
                         'with extensive differentiation of occupational statuses'},
           'name': 'EA066',
           'type': 'categorical',
           'valid_values': [1, 2, 3, 4, 5]},
 'EA067': {'labels': {1: 'Absence of significant class distinctions among freemen (slavery is '
                         'treated in EA070), ignoring variations in individual repute achieved '
                         'through skill, valor, piety, or wisdom',
                      2: 'Wealth distinctions, based on the possession or distribution of '
                         'property, present and socially important but not crystallized into '
                         'distinct and hereditary social classes',
                      3: 'Elite stratification, in which an elite class derives its superior '
                         'status from, and perpetuates it through, control over scarce resources, '
                         'particularly land, and is thereby differentiated from a property-less '
                         'proletariat or serf class',
                      4: 'Dual stratification into a hereditary aristocracy and a lower class of '
                         'ordinary commoners or freemen, where traditionally ascribed noble status '
                         'is at least as decisive as control over scarce resources',
                      5: 'Complex stratification into social classes correlated in large measure '
                         'with extensive differentiation of occupational statuses',
                      9: 'No secondary type'},
           'name': 'EA067',
           'type': 'categorical',
           'valid_values': [1, 2, 3, 4, 5, 9]},
 'EA068': {'labels': {1: 'Caste distinctions absent or insignificant',
                      2: 'One or more despised occupational groups, e.g., smiths or leather '
                         'workers, distinguished from the general population, regarded as '
                         'outcastes by the latter, and characterized by strict endogamy',
                      3: 'Ethnic stratification, in which a superordinate caste withholds '
                         'privileges from and refuses to intermarry with a subordinate caste (or '
                         'castes) which it stigmatizes as ethnically alien, e.g., as descended '
                         'from a conquered and culturally inferior indigenous population, from '
                         'former slaves, or from foreign immigrants of different race and/or '
                         'culture',
                      4: 'Complex caste stratification in which occupational differentiation '
                         'emphasizes hereditary ascription and endogamy to the near exclusion of '
                         'achievable class statuses'},
           'name': 'EA068',
           'type': 'categorical',
           'valid_values': [1, 2, 3, 4]},
 'EA069': {'labels': {1: 'Caste distinctions absent or insignificant',
                      2: 'One or more despised occupational groups, e.g., smiths or leather '
                         'workers, distinguished from the general population, regarded as '
                         'outcastes by the latter, and characterized by strict endogamy',
                      3: 'Ethnic stratification, in which a superordinate caste withholds '
                         'privileges from and refuses to intermarry with a subordinate caste (or '
                         'castes) which it stigmatizes as ethnically alien, e.g., as descended '
                         'from a conquered and culturally inferior indigenous population, from '
                         'former slaves, or from foreign immigrants of different race and/or '
                         'culture',
                      4: 'Complex caste stratification in which occupational differentiation '
                         'emphasizes hereditary ascription and endogamy to the near exclusion of '
                         'achievable class statuses',
                      9: 'No secondary type'},
           'name': 'EA069',
           'type': 'categorical',
           'valid_values': [1, 2, 3, 4, 9]},
 'EA070': {'labels': {1: 'Absence or near absence of slavery',
                      2: 'Incipient or nonhereditary slavery, i.e., where slave status is '
                         'temporary and not transmitted to the children of slaves',
                      3: 'Slavery reported but not identified as hereditary or nonhereditary',
                      4: 'Hereditary slavery present and of at least modest social significance'},
           'name': 'EA070',
           'type': 'categorical',
           'valid_values': [1, 2, 3, 4]},
 'EA071': {'labels': {1: 'Slavery never practiced',
                      2: 'Slavery present in past, but not currently in existence',
                      3: 'Slavery present currently and in past'},
           'name': 'EA071',
           'type': 'categorical',
           'valid_values': [1, 2, 3]},
 'EA072': {'labels': {1: 'Patrilineal heir',
                      2: 'Matrilineal heir',
                      3: 'Nonhereditary succession through appointment by some higher authority',
                      4: 'Nonhereditary succession on the basis primarily of seniority or age',
                      5: 'Nonhereditary succession through influence, e.g., of wealth or social '
                         'status',
                      6: 'Nonhereditary succession through election or some other mode of formal '
                         'consensus',
                      7: 'Nonhereditary succession through informal consensus',
                      9: 'Absence of any office resembling that of a local headman'},
           'name': 'EA072',
           'type': 'categorical',
           'valid_values': [1, 2, 3, 4, 5, 6, 7, 9]},
 'EA073': {'labels': {1: 'Hereditary succession by a son',
                      2: 'Hereditary succession by a patrilineal heir who takes precedence over a '
                         'son',
                      3: "Hereditary succession by a sister's son",
                      4: 'Hereditary succession by a matrilineal heir who takes precedence over a '
                         "sister's son, e.g., a younger brother",
                      5: 'Nonhereditary',
                      9: 'Absence of any office resembling that of a local headman'},
           'name': 'EA073',
           'type': 'categorical',
           'valid_values': [1, 2, 3, 4, 5, 9]},
 'EA074': {'labels': {1: 'Absence of individual property rights in land or of any rule of '
                         'inheritance governing the transmission of such rights',
                      2: "Matrilineal inheritance by a sister's son or sons",
                      3: "Inheritance by matrilineal heirs who take precedence over sisters' sons",
                      4: 'Inheritance by children, but with daughters receiving less than sons',
                      5: 'Inheritance by children of either sex or both',
                      6: 'Inheritance by patrilineal heirs who take precedence over sons',
                      7: 'Patrilineal inheritance by a son or sons'},
           'name': 'EA074',
           'type': 'categorical',
           'valid_values': [1, 2, 3, 4, 5, 6, 7]},
 'EA075': {'labels': {1: 'Equal or relatively equal distribution among all members of the category',
                      2: 'Exclusive or predominant inheritance by the member of the category '
                         'adjudged best qualified, either by the deceased or by his surviving '
                         'relatives',
                      3: 'Ultimogeniture, i.e., predominant inheritance by the junior member of '
                         'the category',
                      4: 'Primogeniture, i.e., predominant inheritance by the senior member of the '
                         'category',
                      9: 'Absence of inheritance of real property'},
           'name': 'EA075',
           'type': 'categorical',
           'valid_values': [1, 2, 3, 4, 9]},
 'EA076': {'labels': {1: 'Absence of individual rights to movable property or of any rule of '
                         'inheritance governing the transmission of such rights. This includes the '
                         'destruction, burial, or giving away of movable property',
                      2: "Matrilineal inheritance by a sister's son or sons",
                      3: "Inheritance by matrilineal heirs who take precedence over sisters' sons",
                      4: 'Inheritance by children, but with daughters receiving less than sons',
                      5: 'Inheritance by children of either sex or both',
                      6: 'Inheritance by patrilineal heirs who take precedence over sons',
                      7: 'Patrilineal inheritance by a son or sons'},
           'name': 'EA076',
           'type': 'categorical',
           'valid_values': [1, 2, 3, 4, 5, 6, 7]},
 'EA077': {'labels': {1: 'Equal or relatively equal distribution among all members of the category',
                      2: 'Exclusive or predominant inheritance by the member of the category '
                         'adjudged best qualified, either by the deceased or by his surviving '
                         'relatives',
                      3: 'Ultimogeniture, i.e., predominant inheritance by the junior member of '
                         'the category',
                      4: 'Primogeniture, i.e., predominant inheritance by the senior member of the '
                         'category',
                      9: 'Absence of inheritance of movable property; includes the destruction, '
                         'burial, or giving away of movable property'},
           'name': 'EA077',
           'type': 'categorical',
           'valid_values': [1, 2, 3, 4, 9]},
 'EA078': {'labels': {1: 'Premarital sex relations precluded by a very early age of marriage for '
                         'females',
                      2: 'Insistence on virginity; premarital sex relations prohibited, strongly '
                         'sanctioned, and in fact rare',
                      3: 'Premarital sex relations prohibited but weakly sanctioned and not '
                         'infrequent in fact',
                      4: 'Premarital sex relations allowed and not sanctioned unless pregnancy '
                         'results',
                      5: 'Trial marriage; monogamous premarital sex relations permitted with the '
                         'expectation of marriage if pregnancy results, promiscuous relations '
                         'being prohibited and sanctioned',
                      6: 'Premarital sex relations freely permitted and subject to no sanctions'},
           'name': 'EA078',
           'type': 'categorical',
           'valid_values': [1, 2, 3, 4, 5, 6]},
 'EA079': {'labels': {1: 'Semicircular',
                      2: 'Circular',
                      3: 'Elliptical or elongated with rounded ends',
                      4: 'Polygonal',
                      5: 'Rectangular or square',
                      6: 'Quadrangular around (or partially around) an interior court'},
           'name': 'EA079',
           'type': 'categorical',
           'valid_values': [1, 2, 3, 4, 5, 6]},
 'EA080': {'labels': {1: 'Subterranean or semi-subterranean, ignoring cellars beneath the living '
                         'quarters',
                      2: 'Floor formed by or level with the ground itself',
                      3: 'Elevated slightly above the ground on a raised platform of earth, stone, '
                         'or wood',
                      4: 'Raised substantially above the ground on piles, posts, or piers'},
           'name': 'EA080',
           'type': 'categorical',
           'valid_values': [1, 2, 3, 4]},
 'EA081': {'labels': {1: 'Stone, stucco, concrete, or fired brick',
                      2: 'Plaster, mud and dung, or wattle and daub',
                      3: 'Wood, including logs, planks, poles, bamboo, or shingles',
                      4: 'Bark',
                      5: 'Hides or skins',
                      6: 'Felt, cloth, or other fabric',
                      7: 'Mats, latticework, or wattle',
                      8: 'Grass, leaves, or other thatch',
                      9: 'Adobe, clay, or dried brick',
                      10: 'Open walls, including cases where they can be temporarily closed by '
                          'screens',
                      11: 'Walls indistinguishable from roof or merging into the latter (see '
                          '"Roofing materials" for details)'},
           'name': 'EA081',
           'type': 'categorical',
           'valid_values': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]},
 'EA082': {'labels': {1: 'Rounded or semi-cylindrical',
                      2: 'Dome shaped or hemispherical',
                      3: 'Beehive shaped with pointed peak',
                      4: 'Conical',
                      5: 'Semi-hemispherical',
                      6: 'Shed, i.e., with one slope',
                      7: 'Flat or horizontal',
                      8: 'Gabled, i.e., with two slopes',
                      9: 'Hipped or pyramidal, i.e., with four slopes'},
           'name': 'EA082',
           'type': 'categorical',
           'valid_values': [1, 2, 3, 4, 5, 6, 7, 8, 9]},
 'EA083': {'labels': {1: 'Stone or slate',
                      2: 'Plaster, clay, mud and dung, or wattle and daub',
                      3: 'Wood, including logs, planks, poles, bamboo, or shingles',
                      4: 'Bark',
                      5: 'Hides or skins',
                      6: 'Felt, cloth, or other fabric',
                      7: 'Mats',
                      8: 'Grass, leaves, brush, or other thatch',
                      9: 'Earth or turf',
                      10: 'Ice or snow',
                      11: 'Tile or fired brick'},
           'name': 'EA083',
           'type': 'categorical',
           'valid_values': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]},
 'EA084': {'labels': {1: 'Semicircular',
                      2: 'Circular',
                      3: 'Elliptical or elongated with rounded ends',
                      4: 'Polygonal',
                      5: 'Rectangular or square',
                      6: 'Quadrangular around (or partially around) an interior court'},
           'name': 'EA084',
           'type': 'categorical',
           'valid_values': [1, 2, 3, 4, 5, 6]},
 'EA085': {'labels': {1: 'Subterranean or semi-subterranean, ignoring cellars beneath the living '
                         'quarters',
                      2: 'Floor formed by or level with the ground itself',
                      3: 'Elevated slightly above the ground on a raised platform of earth, stone, '
                         'or wood',
                      4: 'Raised substantially above the ground on piles, posts, or piers'},
           'name': 'EA085',
           'type': 'categorical',
           'valid_values': [1, 2, 3, 4]},
 'EA086': {'labels': {1: 'Stone, stucco, concrete, or fired brick',
                      2: 'Plaster, mud and dung, or wattle and daub',
                      3: 'Wood, including logs, planks, poles, bamboo, or shingles',
                      4: 'Bark',
                      5: 'Hides or skins',
                      6: 'Felt, cloth, or other fabric',
                      7: 'Mats, latticework, or wattle',
                      8: 'Grass, leaves, or other thatch',
                      9: 'Adobe, clay, or dried brick',
                      10: 'Open walls, including cases where they can be temporarily closed by '
                          'screens',
                      11: 'Walls indistinguishable from roof or merging into the latter (see '
                          '"Roofing materials" for details)'},
           'name': 'EA086',
           'type': 'categorical',
           'valid_values': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]},
 'EA087': {'labels': {1: 'Rounded or semi-cylindrical',
                      2: 'Dome shaped or hemispherical',
                      3: 'Beehive shaped with pointed peak',
                      4: 'Conical',
                      5: 'Semi-hemispherical',
                      6: 'Shed, i.e., with one slope',
                      7: 'Flat or horizontal',
                      8: 'Gabled, i.e., with two slopes',
                      9: 'Hipped or pyramidal, i.e., with four slopes'},
           'name': 'EA087',
           'type': 'categorical',
           'valid_values': [1, 2, 3, 4, 5, 6, 7, 8, 9]},
 'EA088': {'labels': {1: 'Stone or slate',
                      2: 'Plaster, clay, mud and dung, or wattle and daub',
                      3: 'Wood, including logs, planks, poles, bamboo, or shingles',
                      4: 'Bark',
                      5: 'Hides or skins',
                      6: 'Felt, cloth, or other fabric',
                      7: 'Mats',
                      8: 'Grass, leaves, brush, or other thatch',
                      9: 'Earth or turf',
                      10: 'Ice or snow',
                      11: 'Tile or fired brick'},
           'name': 'EA088',
           'type': 'categorical',
           'valid_values': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]},
 'EA090': {'labels': {1: 'Absence of any politicdal organization even at local level, e.g., where '
                         'family heads acknowledge no higher political authority',
                      2: 'Autonomous local communities, i.e., politically independent groups which '
                         'do not exceed 1500 in average population',
                      3: 'Peace groups transcending the local community where the basis of unity '
                         'is other than political, e.g., derived from reciprocal trade relations, '
                         'defensive military agreements, or a common cult or age-grade '
                         'organization',
                      4: 'Minimal states, i.e., political integration even at the local level, '
                         'e.g., where family heads acknowledge no higher political authority (1500 '
                         'ﾖ 10,000)',
                      5: 'Little states, i.e., political integration in independent units '
                         'averaging between 10,000 and 100,000 in population',
                      6: 'States, i.e., political integration in large independent units averaging '
                         'at least 100,000 in population',
                      8: 'Dependent societies lacking any political organization of their own, '
                         'e.g., those forming an integral part of some larger political system and '
                         'those governed exclusively and directly by agents of another and '
                         'politically dominant society. Colonial governments operating through '
                         'indirect rule are ignored.'},
           'name': 'EA090',
           'type': 'categorical',
           'valid_values': [1, 2, 3, 4, 5, 6, 8]},
 'EA094': {'labels': {11: 'Patrilineal succession where a son is preferred to a younger brother',
                      12: 'Patrilineal succession where a younger brother is preferred to a son',
                      13: 'Patrilineal succession other than younger brother or son, or where '
                          'preference is unspecified',
                      24: "Matrilineal succession where a sister's son is preferred to a younger "
                          'brother',
                      25: 'Matrilineal succession where a younger brother is preferred to a '
                          "sister's son",
                      26: "Matrilineal succession other than sister's son or younger brother, or "
                          'where preference is unspecified',
                      39: 'Nonhereditary succession through appointment of headmen by some higher '
                          'political authority',
                      49: 'Nonhereditary succession through election or some other method of '
                          'formal consensus',
                      59: 'Nonhereditary succession through informal consensus or personal '
                          'influence',
                      69: 'Councils, i.e., absence of true headmen, political authroity at the '
                          'local level being exercised exclusively by a council or other '
                          'collective body',
                      99: 'Absence of any indigenous political authority, as in societies lacking '
                          'political integration even at the local level and in some dependent '
                          'societies'},
           'name': 'EA094',
           'type': 'categorical',
           'valid_values': [11, 12, 13, 24, 25, 26, 39, 49, 59, 69, 99]},
 'EA112': {'labels': {1: 'Trance behavior is known to occur, but there is no belief in possession.',
                      2: 'A belief in possession exists.',
                      3: 'Trance behavior is known to occur and is explained as due to possession. '
                         'There is no possession belief referring to other experiences and there '
                         'are no trance states with other explanations.',
                      4: 'Two types of trance states are known to occur. One which is explained as '
                         'due to possession and one which is given another type of explanation. In '
                         'addition to explaining trance, possession belief also refers to one or '
                         'more other phenomena.',
                      5: 'There is both a trance state and a belief in possession, but this belief '
                         'refers to phenomena other than trance, which is explained through other '
                         'categories.',
                      6: 'Trance explained as due to possession is known to occur, and there are '
                         'no other trance states, but cases of possession outside of trance are '
                         'also believed to occur.',
                      7: 'Trance states of two kinds are known to occur, some of which are '
                         'explained by possession. No other phenomena are explained by possession.',
                      8: 'No trance states of any kind are known to occur, and there is no belief '
                         'in possession.'},
           'name': 'EA112',
           'type': 'categorical',
           'valid_values': [1, 2, 3, 4, 5, 6, 7, 8]},
 'EA113': {'labels': {1: 'Rigid, characterized as: non-egalitarian, ascriptive status '
                         'distinctions, autocratic, hierarchical political system, fixed residence '
                         'and group membership, central authority, fixed religious rites.',
                      2: 'Flexible, characterized as: egalitarian, achieved status distinctions, '
                         'autocratic, democratic, federated or stateless political system, ease in '
                         'residence and group changes, individualized or flexible religious '
                         'rites.'},
           'name': 'EA113',
           'type': 'categorical',
           'valid_values': [1, 2]},
 'EA201': {'labels': {1: 'Pattern of marital residence differs in the first years of marriage '
                         'relative to later years.',
                      2: 'Pattern of marital residence in the first years of marriage not '
                         'different from later years.'},
           'name': 'EA201',
           'type': 'categorical',
           'valid_values': [1, 2]}}

# ==============================================================================
# OTHER VARIABLES (from dataset percentiles)
# ==============================================================================

OTHER_VARS = {'AnnualMeanTemperature': {'description': 'Range derived from dataset 1st-99th percentiles',
                           'max': 27.612347117,
                           'min': -10.900893695,
                           'name': 'AnnualMeanTemperature',
                           'type': 'continuous'},
 'MonthlyMeanPrecipitation': {'description': 'Clipped to realistic 0–600 mm/month',
                              'max': 600.0,
                              'min': 0.0,
                              'name': 'MonthlyMeanPrecipitation',
                              'type': 'continuous'},
 'PrecipitationConstancy': {'description': 'Range derived from dataset 1st-99th percentiles',
                            'max': 0.692460919,
                            'min': 0.1777495284,
                            'name': 'PrecipitationConstancy',
                            'type': 'continuous'},
 'PrecipitationPredictability': {'description': 'Range derived from dataset 1st-99th percentiles',
                                 'max': 0.7948403222,
                                 'min': 0.3371611489,
                                 'name': 'PrecipitationPredictability',
                                 'type': 'continuous'},
 'TemperatureConstancy': {'description': 'Range derived from dataset 1st-99th percentiles',
                          'max': 0.8382963472999999,
                          'min': 0.1698883521,
                          'name': 'TemperatureConstancy',
                          'type': 'continuous'},
 'TemperaturePredictability': {'description': 'Range derived from dataset 1st-99th percentiles',
                               'max': 0.8562049611,
                               'min': 0.4585456686,
                               'name': 'TemperaturePredictability',
                               'type': 'continuous'}}

# ==============================================================================
# COMBINED REFERENCE
# ==============================================================================

ALL_VARIABLES = {
    **CODED_VARS,
    **OTHER_VARS,
}

# ==============================================================================
# INTER-VARIABLE CONSTRAINTS
# ==============================================================================

CONSTRAINTS = {
    'subsistence_sum': {
        'description': 'EA001-EA005 must sum to approximately 10',
        'variables': ['EA001', 'EA002', 'EA003', 'EA004', 'EA005'],
        'rule': 'sum_equals',
        'target': 10,
        'tolerance': 0
    },
    'agriculture_intensity_logic': {
        'description': 'If EA028=1 (no agriculture), then EA005 should be 0',
        'variables': ['EA028', 'EA005'],
        'rule': 'if_then',
        'condition': lambda ea028, ea005: ea028 == 1,
        'consequence': lambda ea028, ea005: ea005 == 0
    },
    'settlement_subsistence_correlation': {
        'description': 'Nomadic (EA030=1) unlikely with high agriculture (EA005>7)',
        'variables': ['EA030', 'EA005'],
        'rule': 'soft_constraint',
        'condition': lambda ea030, ea005: ea030 == 1 and ea005 > 7,
        'warning': 'Nomadic lifestyle rarely compatible with intensive agriculture'
    },
    'hierarchy_stratification_correlation': {
        'description': 'Complex stratification (EA066=5) requires political hierarchy (EA033>=3)',
        'variables': ['EA066', 'EA033'],
        'rule': 'soft_constraint',
        'condition': lambda ea066, ea033: ea066 == 5 and ea033 < 3,
        'warning': 'Complex social stratification typically requires state-level organization'
    }
}

# ==============================================================================
# HELPER FUNCTIONS
# ==============================================================================

def get_variable_type(var_name):
    if var_name in ALL_VARIABLES:
        return ALL_VARIABLES[var_name]['type']
    return None


def get_valid_range(var_name):
    if var_name not in ALL_VARIABLES:
        return None

    var_info = ALL_VARIABLES[var_name]
    var_type = var_info['type']

    if var_type == 'categorical':
        return var_info['valid_values']
    elif var_type in ['integer', 'continuous']:
        return (var_info['min'], var_info['max'])

    return None


def validate_value(var_name, value):
    if var_name not in ALL_VARIABLES:
        return False, f"Unknown variable: {var_name}"

    var_info = ALL_VARIABLES[var_name]
    var_type = var_info['type']

    if var_type == 'categorical':
        if value not in var_info['valid_values']:
            return False, f"{var_name}={value} not in valid values {var_info['valid_values']}"
        return True, "Valid"

    elif var_type == 'integer':
        if isinstance(value, (int, np.integer)):
            int_value = int(value)
        elif isinstance(value, (float, np.floating)) and abs(value - round(value)) < 1e-6:
            int_value = int(round(value))
        else:
            return False, f"{var_name}={value} must be integer"

        if int_value < var_info['min'] or int_value > var_info['max']:
            return False, f"{var_name}={int_value} outside range [{var_info['min']}, {var_info['max']}]"
        return True, "Valid"

    elif var_type == 'continuous':
        if value < var_info['min'] or value > var_info['max']:
            return False, f"{var_name}={value} outside range [{var_info['min']}, {var_info['max']}]"
        return True, "Valid"

    return False, "Unknown validation error"


def get_label(var_name, code):
    if var_name not in ALL_VARIABLES:
        return None

    var_info = ALL_VARIABLES[var_name]
    if var_info['type'] != 'categorical':
        return None

    return var_info.get('labels', {}).get(code, f"Code {code}")

# ==============================================================================
# QUICK REFERENCE
# ==============================================================================

RF_INPUT_VARS = [
    'EA001', 'EA002', 'EA003', 'EA004', 'EA005',
    'AnnualMeanTemperature', 'MonthlyMeanPrecipitation', 'TemperatureConstancy',
    'EA043', 'EA009', 'EA012',
    'EA042', 'EA070',
    'EA028', 'EA030', 'EA033'
]

COMPLEXITY_VARS = ['EA033', 'EA066', 'EA030', 'EA028', 'EA039']
