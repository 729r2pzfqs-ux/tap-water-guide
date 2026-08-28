# -*- coding: utf-8 -*-
"""US water quality lookup data: state profiles, ZIP-prefix geography, and
city-to-utility mapping for the /us-water-quality/ tool.

ZIP mapping uses 3-digit ZIP prefixes (USPS sectional center facility areas).
Prefix-to-state assignment is stable USPS allocation; prefix-to-city mapping is
approximate (a prefix can span multiple utilities), which the UI discloses."""

from data_us_states_1 import STATES_1
from data_us_states_2 import STATES_2

US_STATES = STATES_1 + STATES_2

STATE_BY_SLUG = {s["slug"]: s for s in US_STATES}
STATE_BY_ABBR = {s["abbr"]: s for s in US_STATES}
STATE_BY_NAME = {s["name"]: s for s in US_STATES}

# 3-digit ZIP prefix ranges -> state abbreviation (inclusive).
# Unused prefixes inside a state's range map to that state harmlessly.
# Military (090-098, 340, 962-966) and territories (006-009, 969) are omitted:
# the lookup reports "no data" for those.
ZIP_RANGES = [
    (5, 5, "NY"),
    (10, 27, "MA"),
    (28, 29, "RI"),
    (30, 38, "NH"),
    (39, 49, "ME"),
    (50, 59, "VT"),
    (60, 69, "CT"),
    (70, 89, "NJ"),
    (100, 149, "NY"),
    (150, 196, "PA"),
    (197, 199, "DE"),
    (200, 200, "DC"),
    (201, 201, "VA"),
    (202, 205, "DC"),
    (206, 212, "MD"),
    (214, 219, "MD"),
    (220, 246, "VA"),
    (247, 268, "WV"),
    (270, 289, "NC"),
    (290, 299, "SC"),
    (300, 319, "GA"),
    (320, 339, "FL"),
    (341, 342, "FL"),
    (344, 349, "FL"),
    (350, 369, "AL"),
    (370, 385, "TN"),
    (386, 397, "MS"),
    (398, 399, "GA"),
    (400, 427, "KY"),
    (430, 459, "OH"),
    (460, 479, "IN"),
    (480, 499, "MI"),
    (500, 528, "IA"),
    (530, 549, "WI"),
    (550, 567, "MN"),
    (570, 577, "SD"),
    (580, 588, "ND"),
    (590, 599, "MT"),
    (600, 629, "IL"),
    (630, 658, "MO"),
    (660, 679, "KS"),
    (680, 693, "NE"),
    (700, 714, "LA"),
    (716, 729, "AR"),
    (730, 732, "OK"),
    (733, 733, "TX"),
    (734, 749, "OK"),
    (750, 799, "TX"),
    (800, 816, "CO"),
    (820, 831, "WY"),
    (832, 838, "ID"),
    (840, 847, "UT"),
    (850, 865, "AZ"),
    (870, 884, "NM"),
    (885, 885, "TX"),
    (889, 898, "NV"),
    (900, 961, "CA"),
    (967, 968, "HI"),
    (970, 979, "OR"),
    (980, 994, "WA"),
    (995, 999, "AK"),
]


def zip_prefix_to_state():
    """Expand ZIP_RANGES into a {'606': 'IL', ...} dict."""
    out = {}
    for lo, hi, abbr in ZIP_RANGES:
        for p in range(lo, hi + 1):
            out["%03d" % p] = abbr
    return out


# City slug (matching data_us_cities.py) -> (utility name, [3-digit ZIP prefixes]).
# Prefixes listed are the core urban prefixes for that utility's service area;
# cities without a clean dominant prefix are name-searchable only.
CITY_UTILITIES = {
    # Alabama
    "birmingham": ("Birmingham Water Works Board", ["352"]),
    "huntsville": ("Huntsville Utilities", ["358"]),
    # Alaska
    "anchorage": ("Anchorage Water & Wastewater Utility (AWWU)", ["995"]),
    # Arizona
    "phoenix": ("City of Phoenix Water Services", ["850", "851"]),
    "tucson": ("Tucson Water", ["856", "857"]),
    "mesa": ("City of Mesa Water Resources", ["852"]),
    "chandler": ("City of Chandler Water Division", []),
    "glendale-az": ("City of Glendale Water Services", ["853"]),
    # California
    "los-angeles": ("Los Angeles Department of Water and Power (LADWP)", ["900", "913", "914", "916"]),
    "san-diego": ("City of San Diego Public Utilities", ["920", "921"]),
    "san-francisco": ("San Francisco Public Utilities Commission (SFPUC)", ["941"]),
    "sacramento": ("City of Sacramento Department of Utilities", ["958"]),
    "fresno": ("City of Fresno Water Division", ["937"]),
    "long-beach": ("Long Beach Utilities", ["908"]),
    "oakland": ("East Bay Municipal Utility District (EBMUD)", ["946"]),
    "bakersfield": ("City of Bakersfield / California Water Service", ["933"]),
    "anaheim": ("Anaheim Public Utilities", ["928"]),
    "santa-ana": ("City of Santa Ana Water Resources", ["927"]),
    "riverside": ("Riverside Public Utilities", ["925"]),
    "stockton": ("City of Stockton Municipal Utilities", ["952"]),
    "chula-vista": ("Sweetwater Authority / Otay Water District", ["919"]),
    "irvine": ("Irvine Ranch Water District", ["926"]),
    "fontana": ("Fontana Water Company", ["923"]),
    "moreno-valley": ("Eastern Municipal Water District", []),
    "oxnard": ("City of Oxnard Public Works", ["930"]),
    "modesto": ("City of Modesto Utilities", ["953"]),
    "san-bernardino": ("San Bernardino Municipal Water Department", ["924"]),
    "santa-clarita": ("SCV Water (Santa Clarita Valley Water Agency)", []),
    # Colorado
    "denver": ("Denver Water", ["802"]),
    "colorado-springs": ("Colorado Springs Utilities", ["809"]),
    "aurora-co": ("Aurora Water", ["800", "801"]),
    # Florida
    "miami": ("Miami-Dade Water and Sewer Department", ["331", "332"]),
    "hialeah": ("Miami-Dade Water and Sewer Department", ["330"]),
    "jacksonville": ("JEA (Jacksonville)", ["322"]),
    "orlando": ("Orlando Utilities Commission (OUC)", ["328"]),
    "tampa": ("Tampa Water Department", ["336"]),
    "port-st-lucie": ("Port St. Lucie Utility Systems", ["349"]),
    # Georgia
    "atlanta": ("Atlanta Department of Watershed Management", ["303", "311"]),
    # Hawaii
    "honolulu": ("Honolulu Board of Water Supply", ["967", "968"]),
    # Idaho
    "boise": ("Veolia Water Idaho (Boise)", ["837"]),
    # Illinois
    "chicago": ("Chicago Department of Water Management", ["606", "607", "608"]),
    # Indiana
    "indianapolis": ("Citizens Energy Group (Indianapolis)", ["462"]),
    # Iowa
    "des-moines": ("Des Moines Water Works", ["503"]),
    # Kansas
    "wichita": ("City of Wichita Public Works & Utilities", ["672"]),
    # Kentucky
    "louisville": ("Louisville Water Company", ["402"]),
    "lexington": ("Kentucky American Water (Lexington)", ["405"]),
    # Louisiana
    "new-orleans": ("Sewerage & Water Board of New Orleans", ["701"]),
    "baton-rouge": ("Baton Rouge Water Company", ["708"]),
    # Maryland
    "baltimore": ("Baltimore City Department of Public Works", ["212"]),
    # Massachusetts
    "boston": ("MWRA / Boston Water and Sewer Commission", ["021", "022"]),
    # Michigan
    "detroit": ("Great Lakes Water Authority / DWSD", ["482"]),
    "grand-rapids": ("Grand Rapids Water System", ["495"]),
    # Minnesota
    "minneapolis": ("Minneapolis Water Works", ["554"]),
    "st-paul": ("Saint Paul Regional Water Services", ["551"]),
    # Missouri
    "st-louis": ("City of St. Louis Water Division", ["631"]),
    "kansas-city": ("KC Water (Kansas City, MO)", ["641"]),
    # Nebraska
    "omaha": ("Metropolitan Utilities District (Omaha)", ["681"]),
    "lincoln": ("Lincoln Water System", ["685"]),
    # Nevada
    "las-vegas": ("Las Vegas Valley Water District (SNWA)", ["891"]),
    "henderson": ("City of Henderson Water Utility", ["890"]),
    "reno": ("Truckee Meadows Water Authority (TMWA)", ["895"]),
    # New Jersey
    "newark": ("Newark Department of Water & Sewer Utilities", ["071"]),
    "jersey-city": ("Jersey City MUA / Veolia", ["073"]),
    # New Mexico
    "albuquerque": ("Albuquerque Bernalillo County Water Utility Authority", ["871"]),
    # New York
    "new-york-city": ("New York City DEP", ["100", "101", "102", "103", "104", "111", "112", "113", "114", "116"]),
    "buffalo": ("Buffalo Water", ["142"]),
    "rochester-ny": ("City of Rochester Water Bureau", ["146"]),
    # North Carolina
    "charlotte": ("Charlotte Water", ["282"]),
    "raleigh": ("Raleigh Water", ["276"]),
    "durham": ("City of Durham Water Management", ["277"]),
    "greensboro": ("City of Greensboro Water Resources", ["274"]),
    "winston-salem": ("Winston-Salem/Forsyth County Utilities", ["271"]),
    "fayetteville-nc": ("Fayetteville Public Works Commission (PWC)", ["283"]),
    # Ohio
    "columbus": ("Columbus Department of Public Utilities", ["432"]),
    "cincinnati": ("Greater Cincinnati Water Works", ["452"]),
    "toledo": ("Toledo Department of Public Utilities", ["436"]),
    # Oklahoma
    "oklahoma-city": ("Oklahoma City Utilities Department", ["731"]),
    # Oregon
    "portland": ("Portland Water Bureau", ["972"]),
    # Pennsylvania
    "philadelphia": ("Philadelphia Water Department", ["191"]),
    "pittsburgh": ("Pittsburgh Water (PWSA)", ["152"]),
    # Tennessee
    "memphis": ("Memphis Light, Gas and Water (MLGW)", ["381"]),
    "nashville": ("Metro Water Services (Nashville)", ["372"]),
    # Texas
    "houston": ("Houston Public Works", ["770", "772"]),
    "austin": ("Austin Water", ["733", "787"]),
    "dallas": ("Dallas Water Utilities", ["752", "753"]),
    "fort-worth": ("Fort Worth Water", ["761"]),
    "san-antonio": ("San Antonio Water System (SAWS)", ["782"]),
    "arlington-tx": ("Arlington Water Utilities", ["760"]),
    "corpus-christi": ("Corpus Christi Water", ["784"]),
    "plano": ("City of Plano Utilities", ["750"]),
    "garland": ("Garland Water Utilities", []),
    "lubbock": ("City of Lubbock Water Utilities", ["794"]),
    # Utah
    "salt-lake-city": ("Salt Lake City Department of Public Utilities", ["841"]),
    # Virginia
    "virginia-beach": ("Virginia Beach Public Utilities", ["234"]),
    "richmond": ("Richmond Department of Public Utilities", ["232"]),
    # Washington
    "seattle": ("Seattle Public Utilities", ["981"]),
    "spokane": ("City of Spokane Water Department", ["992"]),
    "tacoma": ("Tacoma Water", ["984"]),
    # Wisconsin
    "milwaukee": ("Milwaukee Water Works", ["532"]),
    "madison": ("Madison Water Utility", ["537"]),
}
