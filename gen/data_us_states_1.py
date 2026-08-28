# -*- coding: utf-8 -*-
"""US state water-quality profiles, Alabama through Missouri.
System counts are approximate EPA SDWIS community water system figures; contaminant
notes reflect publicly documented EPA/EWG/state agency reporting as of 2026."""

STATES_1 = [
    dict(slug="alabama", name="Alabama", abbr="AL",
        overview=[
            "Most Alabamians drink surface water drawn from the Tennessee, Coosa, Cahaba, and Black Warrior river systems, treated by large regional utilities such as Birmingham Water Works and Huntsville Utilities. The big urban systems have strong compliance records and meet all federal Safe Drinking Water Act standards.",
            "The state's defining water story is PFAS: decades of discharges from the 3M plant in Decatur contaminated the Tennessee River and forced downstream utilities in the West Morgan-East Lawrence area onto advanced filtration. Smaller rural systems in the Black Belt region also struggle with aging infrastructure and occasional monitoring lapses.",
        ],
        n_systems="about 570",
        contaminants=[
            ("PFAS (forever chemicals)", "Tennessee River systems downstream of Decatur carry a well-documented legacy of 3M-related PFAS contamination; affected utilities have added reverse osmosis or carbon treatment"),
            ("Disinfection byproducts", "River-sourced systems across the state chlorinate heavily in warm months; trihalomethane levels run closer to the federal limit in some small systems"),
            ("Lead from plumbing", "Older housing in Birmingham, Mobile, and Montgomery can leach lead from private-side pipes and fixtures, as in most older US cities"),
        ],
        violations="Alabama's large metro systems rarely record health-based violations. Enforcement actions concentrate in small rural systems, particularly in the Black Belt counties, where aging plants and thin budgets produce monitoring and reporting violations more often than actual contaminant exceedances.",
        faqs=[
            ("Is tap water safe to drink in Alabama?", "Yes, in the large city systems: Birmingham, Huntsville, Montgomery, and Mobile all meet federal standards. The main caveats are PFAS in some Tennessee River systems near Decatur and spotty compliance in very small rural systems."),
            ("What is the PFAS situation in Alabama?", "Discharges from the 3M plant in Decatur contaminated the Tennessee River for decades. Downstream utilities such as West Morgan-East Lawrence installed advanced filtration, and 3M has funded settlements. Huntsville's intakes sit upstream and were not affected."),
            ("How do I check my Alabama utility's record?", "Look up your ZIP code above, then confirm details in your utility's annual Consumer Confidence Report or ADEM's drinking water database."),
        ],
        meta_description="Alabama tap water quality by city and ZIP code: PFAS on the Tennessee River, strong metro compliance, and rural system gaps. Look up your utility."),

    dict(slug="alaska", name="Alaska", abbr="AK",
        overview=[
            "Anchorage, Fairbanks, and Juneau enjoy some of the cleanest municipal water in the country, drawn from glacier-fed and protected mountain sources like Anchorage's Eklutna Lake. The urban systems are modern and consistently meet all EPA standards.",
            "Outside the cities, Alaska has the nation's starkest water-access gap: dozens of remote villages, mainly in the Yukon-Kuskokwim Delta and Arctic coast, still lack piped water entirely and rely on hauled or treated river water. Where systems exist, extreme cold, permafrost damage, and shipping costs make maintenance hard.",
        ],
        n_systems="about 400",
        contaminants=[
            ("Arsenic in private wells", "Interior Alaska and Fairbanks-area groundwater carries naturally occurring arsenic; private wells need testing since they are unregulated"),
            ("Iron and manganese", "Common in village groundwater systems; mostly an aesthetic issue but a sign of limited treatment capacity"),
            ("Disinfection byproducts", "Small surface-water systems with basic chlorination occasionally exceed trihalomethane limits"),
        ],
        violations="Urban Alaska systems are consistently compliant. Violations cluster in small rural systems facing frozen distribution lines, power interruptions, and operator shortages; monitoring violations are far more common than health-based exceedances.",
        faqs=[
            ("Is tap water safe to drink in Alaska?", "In cities, yes: Anchorage's Eklutna Lake supply is among the best in the US. In remote villages, infrastructure varies enormously and some communities still lack piped water."),
            ("Should Alaskans on private wells test their water?", "Yes. Interior groundwater can carry naturally occurring arsenic, and private wells fall outside EPA regulation, so annual testing is the state-recommended practice."),
            ("Why do some Alaska villages lack running water?", "Permafrost, extreme cost, and logistics have left dozens of communities without piped systems; state and federal programs are working through a long construction backlog."),
        ],
        meta_description="Alaska tap water quality: excellent glacier-fed city systems, arsenic in Interior wells, and rural village gaps. Check your ZIP code or utility here."),

    dict(slug="arizona", name="Arizona", abbr="AZ",
        overview=[
            "Arizona's big cities blend Colorado River water delivered by the Central Arizona Project canal with Salt and Verde River supplies and local groundwater. Phoenix, Mesa, Chandler, Glendale, and Tucson all meet federal standards, and utilities here run some of the country's most sophisticated drought and recharge management.",
            "The desert geology gives Arizona water its character: it is among the hardest in the nation, and naturally occurring arsenic in groundwater is the state's most persistent compliance challenge, especially for small systems that rely on wells. PFAS plumes near military bases and airports have also forced well shutdowns around Tucson and Luke Air Force Base.",
        ],
        n_systems="about 780",
        contaminants=[
            ("Arsenic", "Naturally occurring in Basin and Range groundwater; the most common health-based violation among small Arizona well systems"),
            ("PFAS", "Firefighting-foam plumes near Tucson's south side, Luke AFB, and Davis-Monthan AFB have shut down municipal wells; affected utilities blend or treat"),
            ("Hardness and TDS", "Colorado River and local groundwater are very hard, roughly 200-350 mg/L in metro Phoenix; a taste and appliance issue, not a safety one"),
            ("Chromium-6", "Detected at low levels in some Phoenix-area and Yuma groundwater, below federal limits but above health-advocacy benchmarks"),
        ],
        violations="Metro utilities are reliably compliant; arsenic exceedances in small groundwater systems account for most of Arizona's health-based violations. The state runs assistance programs to help small systems install arsenic treatment.",
        faqs=[
            ("Is tap water safe to drink in Arizona?", "Yes in the metro systems: Phoenix, Tucson, Mesa, and their neighbors meet all EPA standards. Small rural well systems carry more arsenic risk and are worth checking individually."),
            ("Why is Arizona water so hard?", "It travels through mineral-rich desert basins and the Colorado River system, picking up calcium and magnesium. Hardness of 200-350 mg/L is normal in Phoenix; softeners are common but not needed for safety."),
            ("Does Arizona tap water have PFAS?", "Some wells near military installations and Tucson International Airport showed PFAS and were taken offline or treated. Utilities publish PFAS sampling in annual reports, and federal limits now force treatment where levels are elevated."),
        ],
        meta_description="Arizona tap water quality by ZIP: hard Colorado River water, arsenic in desert wells, PFAS near bases. Phoenix and Tucson details plus a ZIP lookup."),

    dict(slug="arkansas", name="Arkansas", abbr="AR",
        overview=[
            "Arkansas draws most of its drinking water from lakes and reservoirs: Little Rock's Lake Maumelle watershed is actively protected, and Central Arkansas Water is regarded as one of the better-run utilities in the region. Beaver Lake serves the fast-growing northwest corridor around Fayetteville and Bentonville.",
            "Compliance in the large systems is strong. The challenges sit with the hundreds of small rural systems, where disinfection byproducts and aging distribution lines generate most violations, and with private wells in the Ouachitas and Delta that go untested.",
        ],
        n_systems="about 680",
        contaminants=[
            ("Disinfection byproducts", "The most common exceedance in small surface-water systems, especially in warm months when organic matter is high"),
            ("Manganese and iron", "Common in Delta groundwater; aesthetic at typical levels"),
            ("Lead from plumbing", "Pre-1986 housing in Little Rock and older Delta towns can contribute lead from service lines and fixtures"),
        ],
        violations="Central Arkansas Water and the other metro systems rarely record health-based violations. Small systems account for nearly all exceedances, most often trihalomethanes, and consolidation of struggling systems into regional utilities has been the state's main fix.",
        faqs=[
            ("Is tap water safe to drink in Arkansas?", "Yes in the metro systems. Little Rock's protected Lake Maumelle supply meets all EPA standards, and northwest Arkansas systems on Beaver Lake are similarly reliable. Small rural systems are less consistent."),
            ("Where does Little Rock's water come from?", "Lake Maumelle and Lake Winona, protected reservoirs west of the city managed by Central Arkansas Water, which restricts development in the watershed."),
            ("What is the most common water violation in Arkansas?", "Disinfection byproducts (trihalomethanes) in small surface-water systems: a treatment-optimization problem rather than industrial contamination."),
        ],
        meta_description="Arkansas tap water quality: protected reservoirs serve Little Rock and NW Arkansas, while small systems battle disinfection byproducts. ZIP lookup inside."),

    dict(slug="california", name="California", abbr="CA",
        overview=[
            "California operates the largest and most scrutinized drinking water program in the country, with roughly 2,900 community systems and state standards stricter than federal minimums for several contaminants. The big city systems: LADWP, SFPUC's Hetch Hetchy supply, EBMUD, and San Diego's blended portfolio, all meet every federal and state standard.",
            "The gap is between those systems and the small ones. Hundreds of small Central Valley communities sit on groundwater contaminated with nitrate from agriculture, arsenic, uranium, or 1,2,3-TCP, and the state's SAFER program spends hundreds of millions annually consolidating failing systems. California also pioneered regulation of chromium-6 and PFAS ahead of federal rules.",
        ],
        n_systems="about 2,900",
        contaminants=[
            ("Nitrate", "The Central Valley's signature problem: fertilizer and dairy legacy in groundwater pushes some small-system wells over the 10 mg/L limit"),
            ("Arsenic", "Naturally occurring in Central Valley and desert groundwater; a leading cause of small-system violations"),
            ("1,2,3-TCP", "A legacy fumigant contaminant regulated by California but not federally; detected in dozens of Valley systems, driving treatment installs and lawsuits against manufacturers"),
            ("Chromium-6", "California set the nation's first chromium-6 limit; some inland systems blend or treat to comply"),
            ("PFAS", "Plumes near airports, bases, and industrial areas affect wells in Orange County, the Inland Empire, and elsewhere; large-scale treatment is being built"),
        ],
        violations="Roughly 300 mostly small systems appear on California's Human Right to Water failing-systems list at any time, serving under 2% of the population. The metro systems that serve most Californians are consistently compliant, and the state aggressively consolidates failing systems into larger neighbors.",
        faqs=[
            ("Is tap water safe to drink in California?", "For the vast majority, yes: Los Angeles, San Francisco, San Diego, Sacramento, and the other large systems meet all federal and stricter state standards. The exceptions are small Central Valley and rural systems on contaminated groundwater, which the state tracks publicly."),
            ("Why do small Central Valley towns have unsafe water?", "Decades of fertilizer, dairy, and fumigant use contaminated shallow groundwater with nitrate and 1,2,3-TCP, and many tiny systems cannot afford treatment. The state's SAFER program funds fixes and consolidations."),
            ("Is California tap water more regulated than other states?", "Yes. California enforces its own stricter limits for contaminants like chromium-6, 1,2,3-TCP, and perchlorate, and adopted PFAS response levels ahead of federal rules."),
        ],
        meta_description="California tap water by city and ZIP: strict state standards, clean metro systems, and Central Valley nitrate and arsenic problems. Look up your utility."),

    dict(slug="colorado", name="Colorado", abbr="CO",
        overview=[
            "Colorado's Front Range cities drink high-mountain snowmelt collected close to the source: Denver Water's Rocky Mountain reservoirs, Colorado Springs' Pikes Peak system, and Aurora's Prairie Waters reuse project. Source quality is excellent and all major systems meet federal standards.",
            "The state's issues are legacy and local: PFAS from firefighting foam contaminated groundwater in the Widefield aquifer south of Colorado Springs and near several bases, forcing new treatment; mountain mining legacy leaves metals in some watersheds; and a handful of small plains systems exceed limits for naturally occurring radium or uranium.",
        ],
        n_systems="about 880",
        contaminants=[
            ("PFAS", "The Widefield aquifer contamination from Peterson SFB foam is one of the nation's best-documented PFAS cases; affected districts installed ion-exchange treatment"),
            ("Uranium and radium", "Naturally occurring in some eastern plains groundwater; a recurring small-system violation"),
            ("Lead from plumbing", "Denver Water runs a nationally watched lead service line replacement program, using pH adjustment while lines are removed"),
            ("Mining-legacy metals", "Historic mine drainage affects some mountain source waters; treatment removes it in compliant systems"),
        ],
        violations="Front Range metro systems are consistently compliant. Violations concentrate in small eastern-plains groundwater systems (radionuclides, nitrate) and a few mountain systems with disinfection challenges.",
        faqs=[
            ("Is tap water safe to drink in Colorado?", "Yes: Denver, Colorado Springs, Aurora, and Fort Collins all deliver snowmelt-sourced water that meets every federal standard. Check small plains systems individually for radionuclide notices."),
            ("What happened with PFAS in Fountain and Widefield?", "Firefighting foam from Peterson Space Force Base contaminated the Widefield aquifer serving Fountain, Security, and Widefield. The districts switched sources and installed treatment, and the sites remain part of federal PFAS cleanup programs."),
            ("Why is Denver replacing lead service lines?", "Denver Water chose a 15-year accelerated replacement of roughly 64,000 lead lines with pH-adjusted corrosion control in the meantime: a program regulators cite as a national model."),
        ],
        meta_description="Colorado tap water: snowmelt-fed Front Range systems, the Widefield PFAS cleanup, and Denver's lead line program. Check water quality by ZIP code."),

    dict(slug="connecticut", name="Connecticut", abbr="CT",
        overview=[
            "Connecticut drinks from well-protected reservoirs run by large regional utilities: Aquarion and the South Central Connecticut Regional Water Authority among them. State law here is unusually protective, banning wastewater discharges into drinking-water watersheds, so source quality is among the best in the Northeast.",
            "Compliance is correspondingly strong: health-based violations are rare even among small systems. The live issues are PFAS detections in scattered wells, sodium from decades of road salt creeping into groundwater, and lead plumbing in the state's old housing stock.",
        ],
        n_systems="about 500",
        contaminants=[
            ("Lead from plumbing", "Pre-1950 housing in New Haven, Bridgeport, and Hartford can leach lead from service lines and solder; utilities run corrosion control"),
            ("Sodium and chloride", "Road salt has raised sodium in some wells and small systems, a concern for restricted-sodium diets"),
            ("PFAS", "Detected in scattered public and private wells; the state set action levels and funds treatment where needed"),
        ],
        violations="Connecticut consistently ranks among the states with the fewest health-based violations, helped by watershed-protection laws and consolidation into large professional utilities.",
        faqs=[
            ("Is tap water safe to drink in Connecticut?", "Yes: Connecticut's reservoir systems are among the cleanest in the country, protected by some of the strictest watershed laws in the US."),
            ("Why is Connecticut water quality so consistently good?", "State law prohibits sewage discharge into public drinking-water watersheds and most residents are served by large, well-funded regional utilities rather than tiny systems."),
            ("Should I worry about lead in Connecticut homes?", "In pre-1950 housing, have your water tested or use an NSF-53 filter; the water leaving treatment plants is compliant, and risk comes from building plumbing."),
        ],
        meta_description="Connecticut tap water: protected reservoirs, top-tier compliance, and old-housing lead caveats. Look up water quality by ZIP code or city."),

    dict(slug="delaware", name="Delaware", abbr="DE",
        overview=[
            "Northern Delaware drinks a mix of Brandywine and White Clay Creek surface water and Potomac aquifer groundwater, served by Veolia Delaware, Wilmington's city system, and Artesian Water. All the major systems meet federal standards.",
            "Delaware sits in the mid-Atlantic PFAS belt: detections near the New Castle Air National Guard Base and in scattered wells pushed the state to set its own PFAS limits ahead of federal rules and fund treatment. Nitrate in southern Sussex County groundwater, driven by intensive poultry agriculture, is the other recurring concern.",
        ],
        n_systems="about 200",
        contaminants=[
            ("PFAS", "Groundwater near New Castle ANG Base and several industrial sites shows PFAS; affected wells are treated or offline and statewide sampling is ongoing"),
            ("Nitrate", "Poultry-farming regions of Sussex County show elevated nitrate in shallow groundwater and private wells"),
            ("Disinfection byproducts", "Surface-water systems in the north manage seasonal trihalomethane levels within limits"),
        ],
        violations="Health-based violations are uncommon; Delaware's small size and consolidation into three main utilities keeps oversight tight. PFAS remediation and private-well nitrate are managed as state programs rather than as system violations.",
        faqs=[
            ("Is tap water safe to drink in Delaware?", "Yes: Wilmington, Dover, and the Artesian and Veolia service areas all meet federal standards, and the state adopted PFAS limits early."),
            ("Does Delaware water contain PFAS?", "Some wells near the New Castle Air National Guard Base and industrial sites showed contamination and were treated or removed from service. Utilities now report PFAS results in annual reports."),
            ("Is private well water safe in southern Delaware?", "Test it: shallow Sussex County groundwater can carry nitrate from intensive agriculture, and private wells are not covered by EPA rules."),
        ],
        meta_description="Delaware tap water quality: compliant utilities, early PFAS action near New Castle, and Sussex County nitrate. Check your ZIP code here."),

    dict(slug="washington-dc", name="Washington, DC", abbr="DC",
        overview=[
            "The District's water comes from the Potomac River, treated by the Washington Aqueduct (run by the Army Corps of Engineers) and distributed by DC Water. The system meets all federal standards today, but DC carries the legacy of the early-2000s lead crisis, one of the worst in US history, when a disinfectant switch spiked lead citywide.",
            "Since then, orthophosphate corrosion control has kept lead levels low and DC Water is replacing all remaining lead service lines, with a legal mandate to finish by 2030. Disinfection byproducts from the river supply are monitored and within limits.",
        ],
        n_systems="1 major system (DC Water)",
        contaminants=[
            ("Lead from service lines", "Tens of thousands of lead lines remain mid-replacement; corrosion control keeps measured levels compliant, and free testing is offered"),
            ("Disinfection byproducts", "Chloraminated Potomac water produces DBPs that are monitored and kept within EPA limits"),
            ("Seasonal taste changes", "A spring chlorine switch causes a temporary taste change each year; it is routine maintenance, not a safety issue"),
        ],
        violations="DC Water currently meets all federal health-based standards. The 2001-2004 lead crisis reshaped national lead rules; today's compliance rests on orthophosphate treatment and an accelerating line-replacement program.",
        faqs=[
            ("Is tap water safe to drink in Washington, DC?", "Yes, it meets all EPA standards. In pre-1986 buildings, use a lead-rated filter or request DC Water's free lead test, since service line replacement is still in progress."),
            ("What happened in the DC lead crisis?", "A 2001 switch to chloramine disinfection made the water more corrosive, leaching lead from service lines at levels far above the federal action limit until orthophosphate treatment began in 2004. It became the case study behind modern federal lead rules."),
            ("When will DC's lead pipes be gone?", "DC law requires all lead service lines replaced by 2030, one of the most aggressive deadlines in the country."),
        ],
        meta_description="Washington DC tap water: Potomac-sourced, EPA-compliant, with lead service line replacement due by 2030. History of the lead crisis and current data."),

    dict(slug="florida", name="Florida", abbr="FL",
        overview=[
            "Florida is groundwater country: the Floridan and Biscayne aquifers supply most of the state's roughly 1,600 community systems, including Miami-Dade, Orlando, and Jacksonville. Aquifer water is naturally filtered through limestone, and the big utilities meet all federal standards.",
            "The limestone geology also defines the problems: hydrogen sulfide taste and odor, hardness, and disinfection byproducts formed when organic-rich groundwater is chlorinated (Jacksonville and Tampa manage the state's most watched trihalomethane levels). Saltwater intrusion pushes coastal utilities to deepen or relocate wells, and PFAS shows up near bases and airports.",
        ],
        n_systems="about 1,600",
        contaminants=[
            ("Disinfection byproducts", "The most common Florida exceedance; organic-rich source water plus warm temperatures push trihalomethanes near limits in some systems"),
            ("Hydrogen sulfide taste", "The classic Florida 'rotten egg' or 'swampy' taste from sulfur in aquifer water; harmless but widely noticed"),
            ("PFAS", "Detections near military installations (Pensacola, Jacksonville, Patrick SFB) and some airports; treatment and well shutdowns underway"),
            ("Saltwater intrusion", "Coastal wellfields in South Florida and Tampa Bay face rising chloride, a supply issue driving reuse and desalination investment"),
        ],
        violations="Large Florida utilities are broadly compliant; disinfection byproduct exceedances in mid-size and small systems account for most health-based violations. State revolving funds are financing treatment upgrades across the Panhandle and rural interior.",
        faqs=[
            ("Is tap water safe to drink in Florida?", "Yes across the major metros: Miami, Orlando, Tampa, and Jacksonville all meet EPA standards. The frequent complaints are taste-related, sulfur and chlorine, rather than safety issues."),
            ("Why does Florida tap water taste different?", "Most of it is aquifer water rich in dissolved minerals and traces of sulfur, then chlorinated in a hot climate. A carbon filter fixes taste; the water itself is compliant."),
            ("Is saltwater intrusion making Florida water unsafe?", "No: utilities monitor chloride and retire wells before water becomes unsafe. It is a long-term supply and cost problem, which is why South Florida invests heavily in alternative supplies."),
        ],
        meta_description="Florida tap water by ZIP: aquifer-sourced and EPA-compliant, with sulfur taste, DBP hotspots, and saltwater intrusion pressures. Look up your utility."),

    dict(slug="georgia", name="Georgia", abbr="GA",
        overview=[
            "Metro Atlanta drinks the Chattahoochee River and Lake Lanier, the most fought-over water in the Southeast, treated by Atlanta's Department of Watershed Management and a ring of county utilities that all meet federal standards. South Georgia relies on the Floridan aquifer.",
            "Atlanta's aging pipes generate frequent main breaks and boil-water advisories (a distribution problem more than a treatment one), and the city is investing billions, including the massive Bellwood Quarry reserve, in reliability. Rural systems deal with disinfection byproducts, and private wells in south Georgia with nitrate and bacteria.",
        ],
        n_systems="about 1,800",
        contaminants=[
            ("Lead from plumbing", "Older intown Atlanta housing can contribute lead; the city offers free testing and runs corrosion control"),
            ("Disinfection byproducts", "Small surface-water systems in middle and south Georgia record most of the state's THM exceedances"),
            ("PFAS", "Carpet-industry legacy around Dalton and Calhoun contaminated the Conasauga watershed; affected utilities have added treatment and litigation continues"),
        ],
        violations="Metro utilities meet health-based standards; north Georgia's carpet-belt PFAS and small-system DBPs drive most enforcement attention. Watch for boil-water advisories after Atlanta main breaks: a recurring infrastructure symptom.",
        faqs=[
            ("Is tap water safe to drink in Georgia?", "Yes across metro Atlanta and the major cities, all EPA-compliant. Heed temporary boil-water advisories after main breaks, and check small-system reports in rural areas."),
            ("Why does Atlanta have so many boil-water advisories?", "Century-old distribution mains break regularly, dropping pressure and triggering precautionary advisories. The water leaving the plants meets standards; the pipes are the weak link, and replacement programs are underway."),
            ("What is the PFAS problem in north Georgia?", "Decades of carpet manufacturing around Dalton released PFAS into the Conasauga River basin, affecting downstream systems into Alabama. Utilities installed treatment and manufacturers face ongoing litigation."),
        ],
        meta_description="Georgia tap water quality: EPA-compliant metros, Atlanta's aging mains, and carpet-belt PFAS near Dalton. Search water data by ZIP code."),

    dict(slug="hawaii", name="Hawaii", abbr="HI",
        overview=[
            "Hawaii's municipal water is naturally exceptional: rain filtered through volcanic rock into basal aquifers, so pure that Honolulu's Board of Water Supply delivers it with disinfection alone, no filtration needed. Neighbor-island county systems are similarly clean.",
            "That purity made the 2021 Red Hill crisis a statewide shock: jet fuel from the Navy's underground storage tanks contaminated the base's Pearl Harbor-area system and threatened Oahu's primary aquifer, forcing well shutdowns that still constrain supply. The tanks have since been defueled and closure is underway; municipal wells are monitored and remain unaffected.",
        ],
        n_systems="about 130",
        contaminants=[
            ("Petroleum (Red Hill legacy)", "The 2021 fuel release contaminated the Navy's own system, not BWS municipal wells; ongoing monitoring guards the aquifer and shut wells reduce supply flexibility"),
            ("Legacy pesticides", "Traces of historic plantation fumigants (TCP, EDB) appear in some central Oahu and Maui wells, treated with carbon where present"),
            ("Chloride and hardness", "Some coastal wells trend brackish; managed through blending"),
        ],
        violations="County water systems consistently meet all federal standards. The Red Hill contamination occurred on the Navy's separate system; its aftermath is managed as a federal cleanup with independent aquifer monitoring.",
        faqs=[
            ("Is tap water safe to drink in Hawaii?", "Yes: volcanic aquifer water is among the purest municipal supply in the US, and Honolulu's needs no filtration, only disinfection."),
            ("Did Red Hill contaminate Honolulu's drinking water?", "The 2021 fuel release contaminated the Navy's own water system serving base housing. Honolulu Board of Water Supply wells were not contaminated, though BWS shut its Halawa shaft as a precaution and monitoring continues while the tanks are decommissioned."),
            ("Do I need a filter in Hawaii?", "Not for safety on county systems. Residents near legacy plantation areas can check their annual report for pesticide-trace results if curious."),
        ],
        meta_description="Hawaii tap water: pristine volcanic aquifers, the Red Hill fuel crisis explained, and current safety by island. Look up your ZIP code."),

    dict(slug="idaho", name="Idaho", abbr="ID",
        overview=[
            "Idaho drinks almost entirely from groundwater, including the vast Snake River Plain aquifer, one of the most productive in the world. Boise's system (run by Veolia) blends aquifer wells with treated Boise River water and meets all federal standards.",
            "Water quality is generally very good. The persistent issues are nitrate from irrigated agriculture and dairies in the Magic Valley and eastern Snake Plain, naturally occurring arsenic and uranium in some southern wells, and the usual small-system capacity gaps in a largely rural state.",
        ],
        n_systems="about 790",
        contaminants=[
            ("Nitrate", "Idaho's most tracked contaminant; agricultural regions show rising trends and some small systems and private wells exceed the limit"),
            ("Arsenic", "Naturally occurring in southwest and south-central Idaho groundwater; a recurring small-system violation"),
            ("Uranium", "Detected above limits in a handful of southern Idaho wells; treated or blended where found"),
        ],
        violations="Boise and the larger cities are consistently compliant. Violations concentrate in small agricultural-area systems for nitrate and arsenic, and the state maintains nitrate priority areas where groundwater degradation is documented.",
        faqs=[
            ("Is tap water safe to drink in Idaho?", "Yes in Boise and the major cities, which meet all EPA standards. In agricultural areas, small systems and private wells should be checked for nitrate."),
            ("Why is nitrate a concern in Idaho?", "Irrigated farming and large dairies load nitrogen into the Snake River Plain aquifer. Levels rise slowly and persistently, making nitrate the state's top groundwater priority."),
            ("Where does Boise's water come from?", "A mix of aquifer wells and treated Boise River water managed by Veolia Water Idaho, all meeting federal standards."),
        ],
        meta_description="Idaho tap water quality: Snake Plain aquifer supply, rising nitrate in farm country, and compliant city systems. Check your ZIP code lookup."),

    dict(slug="illinois", name="Illinois", abbr="IL",
        overview=[
            "Northeastern Illinois drinks Lake Michigan water treated at Chicago's enormous filtration plants and piped to more than 100 suburbs; the lake supply is excellent and consistently compliant. Downstate cities rely on rivers and wells of varying character.",
            "Illinois' defining issue is lead: the state has more lead service lines than any other, roughly 1 million, with Chicago alone holding about 400,000. Statute now requires full replacement over the coming decades. Radium in deep-aquifer groundwater has long affected some collar-county and downstate systems, and PFAS sampling has flagged sites near industry and bases.",
        ],
        n_systems="about 1,730",
        contaminants=[
            ("Lead from service lines", "The nation's largest lead-line inventory; corrosion control keeps water compliant while a decades-long replacement mandate proceeds"),
            ("Radium", "Naturally occurring in the deep sandstone aquifer; several small systems treat or blend to comply"),
            ("Nitrate", "Agricultural runoff seasonally pressures river-sourced downstate systems like Decatur"),
            ("PFAS", "Statewide sampling found detections near industrial corridors; Illinois has proposed enforceable limits"),
        ],
        violations="Lake Michigan systems rarely violate standards. Downstate, radium and occasional nitrate exceedances in small systems make up most health-based violations, and lead-line replacement dominates the compliance agenda statewide.",
        faqs=[
            ("Is tap water safe to drink in Illinois?", "Yes: Chicago and the Lake Michigan suburbs meet all EPA standards, as do the major downstate systems. The main risk is lead from legacy service lines in older housing, addressed by filters and line replacement."),
            ("Why does Illinois have so many lead pipes?", "Chicago's plumbing code required lead service lines until the 1986 federal ban, and older towns statewide followed similar practice, leaving roughly a million lines now mandated for replacement."),
            ("Is radium in Illinois water dangerous?", "Some deep wells naturally exceed radium limits and affected systems must treat, blend, or switch sources. Compliant systems' annual reports show current levels."),
        ],
        meta_description="Illinois tap water: Lake Michigan quality, a million lead service lines, and downstate radium. Search water quality by ZIP code or city."),

    dict(slug="indiana", name="Indiana", abbr="IN",
        overview=[
            "Indianapolis draws from the White River and reservoirs through Citizens Energy Group, while northern cities like Fort Wayne and South Bend mix river and groundwater. The major systems meet all federal standards.",
            "Indiana's industrial legacy shows at the edges: East Chicago's lead-contaminated soil crisis put its water system under scrutiny, PFAS detections track the steel and manufacturing corridor near Lake Michigan, and agricultural nitrate pressures small groundwater systems across the corn belt.",
        ],
        n_systems="about 780",
        contaminants=[
            ("Lead from plumbing", "Older industrial cities (East Chicago, Gary, Indianapolis's old neighborhoods) carry legacy service lines; utilities run corrosion control and replacement programs"),
            ("Nitrate", "Corn-belt groundwater systems see seasonal exceedances after wet springs"),
            ("PFAS", "Detections near the northwest industrial corridor and several bases; statewide monitoring is expanding under federal rules"),
        ],
        violations="Large systems are consistently compliant; violations skew to small rural systems (nitrate, occasional bacteria) and aging industrial-city distribution. East Chicago remains the cautionary tale that accelerated the state's lead programs.",
        faqs=[
            ("Is tap water safe to drink in Indiana?", "Yes in Indianapolis, Fort Wayne, and the major systems, which meet all EPA standards. Older industrial-city housing warrants lead-aware precautions like flushing or filters."),
            ("What happened in East Chicago?", "A lead-contaminated Superfund site under a housing complex exposed residents through soil and raised scrutiny of water lead levels, prompting federal intervention and accelerated line replacement in the region."),
            ("Does Indiana water have PFAS?", "Sampling found detections concentrated near northwest Indiana industry and military sites; affected utilities are planning treatment under the new federal PFAS limits."),
        ],
        meta_description="Indiana tap water quality: compliant metros, East Chicago's lead legacy, and corn-belt nitrate. Look up your water system by ZIP code."),

    dict(slug="iowa", name="Iowa", abbr="IA",
        overview=[
            "Iowa's water story is agriculture. Des Moines Water Works runs one of the world's largest nitrate-removal facilities because the Raccoon and Des Moines Rivers drain some of the most intensively farmed land on earth, and it still delivers fully compliant water to half a million people.",
            "Statewide, nitrate and its treatment costs dominate: dozens of small systems have installed removal equipment or drilled new wells, and the state's private wells show frequent nitrate and bacteria exceedances. Atrazine and other herbicides appear seasonally in surface water at levels below federal limits.",
        ],
        n_systems="about 1,070",
        contaminants=[
            ("Nitrate", "The state's defining contaminant, from fertilizer and drained cropland; utilities treat or blend, and private wells are at highest risk"),
            ("Herbicides (atrazine)", "Spring runoff pulses appear in river-sourced systems, monitored and typically below limits"),
            ("Bacteria in private wells", "Shallow rural wells frequently test positive for coliform; state programs offer free testing"),
        ],
        violations="Public systems mostly comply because they invest in treatment: the cost of nitrate removal is the real burden. Small systems account for periodic nitrate exceedances, and Iowa's water-quality debate centers on upstream farm-practice policy.",
        faqs=[
            ("Is tap water safe to drink in Iowa?", "Yes on public systems: Des Moines and the major utilities treat aggressively and meet federal standards. Private wells in farm country need regular nitrate and bacteria testing."),
            ("Why is nitrate such a problem in Iowa?", "Tile-drained, heavily fertilized cropland delivers nitrogen straight to rivers and shallow aquifers. Removing it is expensive, which is why Des Moines built the world's largest nitrate facility."),
            ("Is Iowa doing anything about the source problem?", "The state funds voluntary conservation (cover crops, buffers, bioreactors), a perennially debated approach since compliance costs fall on drinking-water utilities downstream."),
        ],
        meta_description="Iowa tap water: the nitrate capital of US drinking water, how Des Moines treats it, and private-well risks. Check your ZIP code for details."),

    dict(slug="kansas", name="Kansas", abbr="KS",
        overview=[
            "Eastern Kansas cities drink treated river and reservoir water (Wichita blends Cheney Reservoir with Equus Beds aquifer wells; Kansas City-area systems use the Missouri and Kansas Rivers), and all the large systems meet federal standards. Western Kansas depends on the declining Ogallala aquifer.",
            "Recurring issues are agricultural: nitrate exceedances in small groundwater systems, atrazine pulses in reservoirs after spring planting, and naturally occurring uranium and selenium in pockets of western groundwater. Wichita's aquifer storage project also guards against a legacy industrial plume east of the wellfield.",
        ],
        n_systems="about 860",
        contaminants=[
            ("Nitrate", "The most common health-based violation, concentrated in small ag-area groundwater systems"),
            ("Atrazine", "Spring runoff peaks in some reservoir systems; annual averages stay within limits"),
            ("Uranium", "Naturally occurring in parts of western Kansas groundwater; affected systems blend or treat"),
        ],
        violations="Wichita, Topeka, and the Johnson County systems are consistently compliant. Violations cluster in small western and central systems for nitrate and radionuclides, with consolidation and new wells the usual fixes.",
        faqs=[
            ("Is tap water safe to drink in Kansas?", "Yes in the cities: Wichita, Topeka, and the Kansas City suburbs meet all EPA standards. Small farm-country systems and private wells warrant nitrate testing."),
            ("Where does Wichita's water come from?", "A blend of Cheney Reservoir and the Equus Beds aquifer, with a managed recharge project that stores treated river water underground for drought years."),
            ("Is the Ogallala aquifer decline a safety issue?", "It is a supply problem, not a contamination one: western Kansas towns face wells running dry and costly deepening, while the water itself generally meets standards."),
        ],
        meta_description="Kansas tap water quality: compliant city systems, farm-belt nitrate, and Ogallala supply pressures. Look up water data for your ZIP code."),

    dict(slug="kentucky", name="Kentucky", abbr="KY",
        overview=[
            "Louisville Water is one of the most technically respected utilities in the country: its Ohio River supply is polished through natural riverbank filtration at the Payne plant, and the company literally trademarked its tap water's taste. Lexington's Kentucky American system is similarly reliable.",
            "Beyond the big systems, Kentucky wrestles with aging coal-country infrastructure: Martin County's failing system became a national symbol of rural water neglect, with chronic outages and disinfection byproduct violations. Karst geology makes springs and shallow wells vulnerable to rapid contamination.",
        ],
        n_systems="about 390",
        contaminants=[
            ("Disinfection byproducts", "The characteristic violation in small eastern-Kentucky systems with long pipe runs and surface sources"),
            ("Lead from plumbing", "Louisville and Lexington's older neighborhoods carry legacy lines; both utilities run replacement and corrosion-control programs"),
            ("Bacteria in karst wells", "Sinkhole-fed groundwater can transmit surface contamination quickly; private springs and wells need treatment"),
        ],
        violations="Kentucky consolidated aggressively (fewer than 400 community systems remain), lifting most of the state to solid compliance. Distressed Appalachian systems like Martin County account for the persistent violations, drawing state takeovers and federal infrastructure money.",
        faqs=[
            ("Is tap water safe to drink in Kentucky?", "Yes in Louisville, Lexington, and most consolidated regional systems. A handful of eastern-Kentucky systems have documented reliability problems; local advisories apply there."),
            ("What makes Louisville's water notable?", "Riverbank filtration: wells beside the Ohio River draw water naturally pre-filtered through sand and gravel, yielding award-winning quality the utility markets as 'Louisville pure tap'."),
            ("What happened in Martin County?", "Decades of underinvestment left the county's system losing most of its water to leaks, with frequent outages and quality violations: now a national case study in rural infrastructure failure and the subject of state intervention."),
        ],
        meta_description="Kentucky tap water: Louisville's award-winning riverbank filtration, Appalachian system struggles, and karst risks. Search by ZIP code."),

    dict(slug="louisiana", name="Louisiana", abbr="LA",
        overview=[
            "New Orleans and Baton Rouge sit on very different supplies: the Sewerage & Water Board treats Mississippi River water in aging plants, while Baton Rouge pumps pristine groundwater from the Southern Hills aquifer. Both meet federal standards, but the state's infrastructure is among the country's most stressed.",
            "Louisiana's recurring problems include boil-water advisories from pressure losses and storm damage, saltwater wedges creeping up the Mississippi in drought years (threatening Plaquemines and New Orleans intakes in 2023), disinfection byproducts in small systems, and the nation's most publicized brain-eating amoeba detections, which forced chlorine burns in several parish systems.",
        ],
        n_systems="about 950",
        contaminants=[
            ("Disinfection byproducts", "Warm, organic-rich water makes THM control a constant battle in small surface-water systems"),
            ("Lead from plumbing", "New Orleans' old housing stock carries legacy lines; corrosion control and replacement programs are underway"),
            ("Naegleria fowleri detections", "Rare amoeba findings in a few parish distribution systems prompted precautionary chlorine burns; tap water remains safe to drink (the risk pathway is nasal, not ingestion)"),
            ("Saltwater intrusion", "Drought-year wedges up the Mississippi threaten downriver intakes, managed with barriers and barged water in 2023"),
        ],
        violations="Compliance is solid in the metros but fragile in small systems, which lead the nation in boil-water advisories per capita. Federal infrastructure funds are rebuilding storm-damaged and deferred systems across the state.",
        faqs=[
            ("Is tap water safe to drink in New Orleans and Louisiana?", "Yes: New Orleans and Baton Rouge meet all EPA standards. Expect occasional precautionary boil-water advisories after pressure drops, and follow them when issued."),
            ("What about the brain-eating amoeba in Louisiana water?", "Naegleria fowleri was detected in a few parish systems' pipes in past years. Drinking the water is safe; the organism infects through the nose, so avoid getting untreated tap water deep into nasal passages during advisories. Affected systems ran chlorine burns."),
            ("Did saltwater reach New Orleans' drinking water?", "The 2023 drought pushed a saltwater wedge far upriver, prompting sill construction and emergency planning; it was halted before affecting the city's intakes, though smaller downriver systems needed barged water."),
        ],
        meta_description="Louisiana tap water: Mississippi River treatment, boil-water advisories, saltwater wedges, and amoeba facts. Check your parish by ZIP code."),

    dict(slug="maine", name="Maine", abbr="ME",
        overview=[
            "Portland's Sebago Lake supply is so clean it holds one of the EPA's rare filtration waivers: the protected watershed delivers water needing only disinfection. Maine's other surface-water systems are similarly well-sourced for the most part.",
            "Maine's real water issue is underground: it has among the nation's highest rates of arsenic in private wells, with roughly half the state on unregulated wells drilled into arsenic-bearing bedrock. PFAS from decades of sludge-spreading on farmland has also emerged as a statewide crisis, with Maine setting some of the country's strictest standards and testing programs.",
        ],
        n_systems="about 380",
        contaminants=[
            ("Arsenic in private wells", "Bedrock wells across large swaths of Maine exceed the arsenic limit; an estimated one in ten wells is affected and testing rates remain low"),
            ("PFAS from sludge-spreading", "Land-applied biosolids contaminated farms and wells statewide; Maine banned sludge spreading and funds well testing and treatment"),
            ("Disinfection byproducts", "Occasional exceedances in small systems with organic-rich sources"),
        ],
        violations="Public systems have strong compliance, anchored by Sebago Lake's waiver-grade quality. The state's attention is on private wells (arsenic, PFAS), which fall outside federal regulation and depend on homeowner testing.",
        faqs=[
            ("Is tap water safe to drink in Maine?", "On public systems, yes: Portland's Sebago Lake water is among the best in the country. On private wells, test for arsenic and PFAS: Maine's bedrock and sludge-spreading history make both meaningfully common."),
            ("Why does Portland's water skip filtration?", "Sebago Lake's protected watershed qualifies for an EPA filtration avoidance waiver, held by only a handful of US systems: the water is disinfected with UV and chloramine and piped to the metro area."),
            ("What is Maine's PFAS farm crisis?", "Sludge spread as fertilizer for decades carried PFAS into soil and groundwater, contaminating wells and some farm products. Maine banned the practice first in the nation and runs statewide testing and remediation programs."),
        ],
        meta_description="Maine tap water: Sebago Lake's filtration-waiver purity, arsenic in bedrock wells, and the PFAS sludge legacy. Look up your ZIP code."),

    dict(slug="maryland", name="Maryland", abbr="MD",
        overview=[
            "Baltimore's reservoir system and the Washington suburbs' Potomac/Patuxent supply (WSSC Water) serve most Marylanders, and both large systems meet all federal standards. WSSC has never recorded a health-based violation in over a century of operation, a record it advertises.",
            "Baltimore's aging distribution has produced high-profile incidents: the 2022 E. coli detection in West Baltimore triggered a boil-water advisory, and main breaks are chronic. On the Eastern Shore, poultry-belt groundwater carries nitrate, and scattered PFAS detections track bases and industry.",
        ],
        n_systems="about 450",
        contaminants=[
            ("Lead from plumbing", "Baltimore's older rowhouse stock contributes lead from private-side plumbing; the city offers testing and filter programs"),
            ("Nitrate", "Eastern Shore shallow groundwater near intensive poultry operations shows elevated levels, mainly affecting private wells"),
            ("Disinfection byproducts", "Managed within limits in the big surface-water systems; occasional small-system exceedances"),
        ],
        violations="The two dominant utilities are strongly compliant; Baltimore's issues are distribution-side (breaks, pressure, aging valves) rather than treatment failures. Small Eastern Shore and western Maryland systems account for most formal violations.",
        faqs=[
            ("Is tap water safe to drink in Maryland?", "Yes: Baltimore and the WSSC service area meet all EPA standards. Follow any temporary advisories after main breaks, and test private wells on the Eastern Shore for nitrate."),
            ("What caused Baltimore's 2022 E. coli advisory?", "Routine sampling found E. coli in a West Baltimore section, likely from distribution-system intrusion. Flushing and chlorination cleared it within days; it spotlighted the city's aging mains."),
            ("Is WSSC water really violation-free?", "WSSC Water reports it has never exceeded a federal health-based standard since operations began in 1918, one of the longest clean records among major US utilities."),
        ],
        meta_description="Maryland tap water: WSSC's century-clean record, Baltimore's aging mains, Eastern Shore nitrate. Search water quality by ZIP code."),

    dict(slug="massachusetts", name="Massachusetts", abbr="MA",
        overview=[
            "The MWRA delivers Quabbin and Wachusett reservoir water to Boston and 50+ communities: protected-watershed supply so clean it earned an EPA filtration waiver, consistently rated among the best big-city water in America. Central and western systems draw local reservoirs and wells.",
            "The state's compliance record is excellent. Attention now centers on PFAS, where Massachusetts set an early, strict standard covering six compounds and found exceedances in dozens of systems (notably on Cape Cod, where firefighting-foam plumes and septic-dense geology combine), and on lead in the state's very old housing stock.",
        ],
        n_systems="about 530",
        contaminants=[
            ("PFAS", "The state's PFAS6 standard flagged dozens of systems, concentrated on Cape Cod and near training sites; treatment installs are well underway"),
            ("Lead from plumbing", "Pre-war housing across Boston, Worcester, and the mill cities carries legacy service lines and solder; MWRA's corrosion control keeps levels low"),
            ("Sodium from road salt", "Rising in some suburban wellfields; flagged for sodium-restricted diets"),
        ],
        violations="Health-based violations are rare and mostly PFAS-related as the strict state standard came into force. The MWRA core system has a decades-long clean record with soft, low-mineral water.",
        faqs=[
            ("Is tap water safe to drink in Massachusetts?", "Yes: MWRA's reservoir water is among the best in the nation, and most other systems comply fully. Cape Cod residents should check their utility's PFAS results, which the state publishes."),
            ("Why is Boston's water so highly rated?", "It comes from the protected Quabbin and Wachusett watersheds, needs no filtration, is naturally soft, and wins national taste tests: infrastructure spending since the 1990s Boston Harbor cleanup rebuilt the whole system."),
            ("What is the PFAS situation on Cape Cod?", "Firefighting foam at Joint Base Cape Cod and the region's sandy, septic-heavy geology created PFAS plumes affecting several town systems; treatment and new wells are being installed with state funds."),
        ],
        meta_description="Massachusetts tap water: MWRA's nation-leading reservoirs, Cape Cod PFAS plumes, and old-housing lead. Look up your city or ZIP."),

    dict(slug="michigan", name="Michigan", abbr="MI",
        overview=[
            "Surrounded by 20% of the world's surface freshwater, Michigan's big systems (the Great Lakes Water Authority serving metro Detroit, Grand Rapids' Lake Michigan plant) deliver excellent, fully compliant water. Then there is Flint: the 2014-2019 crisis that redefined American water policy.",
            "Flint's fallout made Michigan's rules the strictest in the nation: the state's Lead and Copper Rule exceeds federal requirements, mandating full service-line replacement and tighter action levels. Michigan also leads on PFAS, having tested every public system and set enforceable limits after discovering plumes in Rockford, Oscoda, Parchment, and elsewhere.",
        ],
        n_systems="about 1,390",
        contaminants=[
            ("Lead from service lines", "Post-Flint rules require utilities to inventory and replace all lead lines; Flint itself completed replacement and Benton Harbor followed after its own exceedances"),
            ("PFAS", "Michigan's statewide testing found 100+ sites; Wolverine Worldwide (Rockford), Wurtsmith AFB (Oscoda), and Parchment became national case studies, with limits now enforced"),
            ("Disinfection byproducts", "Occasional exceedances in small inland surface-water systems"),
        ],
        violations="The Great Lakes metro systems are consistently compliant. Benton Harbor's lead exceedances (2018-2021) and legacy PFAS sites drive most enforcement; Michigan now arguably runs the most aggressive testing regime in the country.",
        faqs=[
            ("Is tap water safe to drink in Michigan?", "Yes in Detroit, Grand Rapids, and the Great Lakes systems, which meet every standard. Flint's water now tests below action levels after full pipe replacement, and the state's post-crisis rules are the nation's strictest."),
            ("Is Flint's water safe now?", "Flint reconnected to the Detroit/GLWA supply in 2015 and finished replacing lead service lines; sampling has shown lead below the federal action level since 2016-2017. Many residents still filter by choice, and free filters remain available."),
            ("Why does Michigan lead on PFAS?", "After discovering severe plumes (Oscoda's Wurtsmith base, Rockford's tannery waste), Michigan tested all public systems, set enforceable limits for seven PFAS compounds in 2020, and built the PFAS response team other states copy."),
        ],
        meta_description="Michigan tap water: Great Lakes quality, Flint's recovery, Benton Harbor, and the nation's strictest lead and PFAS rules. Check your ZIP."),

    dict(slug="minnesota", name="Minnesota", abbr="MN",
        overview=[
            "Minneapolis and St. Paul both treat Mississippi River water with modern multi-barrier plants (softening included), and the Twin Cities supply meets all federal standards. Outstate systems split between groundwater and surface sources.",
            "Minnesota's east-metro PFAS story is foundational: 3M's disposal sites contaminated groundwater under Oakdale, Woodbury, Cottage Grove, and neighboring suburbs, producing an $850 million settlement now funding treatment plants across the area. Farm-country nitrate in the karst southeast and central sands is the other standing concern.",
        ],
        n_systems="about 960",
        contaminants=[
            ("PFAS", "The east-metro 3M plume is among the world's most studied; settlement-funded treatment now covers affected suburbs, and statewide monitoring continues"),
            ("Nitrate", "Karst southeast Minnesota and the central sands show rising nitrate in wells; the state faces EPA pressure over the karst region's private wells"),
            ("Manganese", "Naturally elevated in some groundwater systems; Minnesota issues health-based guidance for infants"),
        ],
        violations="Twin Cities systems hold strong compliance records. Violations cluster in small groundwater systems (nitrate, occasional radium), and the karst region's private wells are a recognized public-health gap outside federal jurisdiction.",
        faqs=[
            ("Is tap water safe to drink in Minnesota?", "Yes: Minneapolis, St. Paul, and the large systems meet all EPA standards. In the karst southeast, private wells need regular nitrate testing."),
            ("What did 3M do to Minnesota's water?", "Decades of PFAS disposal in east-metro landfills contaminated a large aquifer area. Minnesota's 2018 settlement with 3M ($850 million) funds new treatment plants and alternative supplies for affected communities."),
            ("Why is southeast Minnesota's groundwater vulnerable?", "Karst limestone lets surface water and farm runoff reach aquifers quickly, so nitrate and bacteria appear in wells faster than in most geology; the region is a state testing priority."),
        ],
        meta_description="Minnesota tap water: Twin Cities river treatment, the 3M PFAS settlement suburbs, and karst nitrate. Look up your system by ZIP code."),

    dict(slug="mississippi", name="Mississippi", abbr="MS",
        overview=[
            "Jackson's 2022 collapse, when flooding knocked out the O.B. Curtis plant and left the capital without safe water for weeks, made Mississippi the national emblem of water-infrastructure failure. A federal receiver now runs JXN Water, and service has stabilized with major EPA funding, though rebuilding continues.",
            "Most of the rest of the state drinks groundwater from prolific aquifers, and typical quality is decent where systems are maintained. The state has many small, thinly funded rural systems with recurring boil-water notices, and private wells in the Delta go largely untested.",
        ],
        n_systems="about 1,180",
        contaminants=[
            ("Infrastructure-driven bacteria risk", "Pressure losses and line breaks in distressed systems (Jackson historically, small rural systems today) trigger frequent precautionary boil-water notices"),
            ("Disinfection byproducts", "A recurring exceedance in small surface-water systems"),
            ("Naturally soft, corrosive groundwater", "Some aquifer water is aggressive toward plumbing, raising lead/copper leaching risk where corrosion control lapses, a factor in Jackson's earlier lead exceedances"),
        ],
        violations="Mississippi consistently ranks near the top for boil-water advisories and small-system violations per capita. Jackson operates under federal oversight with roughly $800 million in committed rebuild funds; its water currently meets standards, while trust rebuilds more slowly.",
        faqs=[
            ("Is tap water safe to drink in Mississippi?", "In most systems, yes, and Jackson's water now meets federal standards under its court-appointed operator. Rural systems issue frequent precautionary advisories: always follow current local notices."),
            ("What happened to Jackson's water?", "Decades of deferred maintenance, staffing gaps, and a shrinking rate base culminated in the 2022 flood knocking out the main plant. A federal receiver took over, stabilized treatment, and is spending federal funds on the rebuild."),
            ("Is Jackson's water safe today?", "Sampling under the federal receivership shows compliance with health standards, including lead below action levels. Advisories still occur during main breaks, and the distribution overhaul is a multi-year project."),
        ],
        meta_description="Mississippi tap water: Jackson's crisis and federal rebuild, rural boil-water notices, and aquifer basics. Check your water system by ZIP."),

    dict(slug="missouri", name="Missouri", abbr="MO",
        overview=[
            "St. Louis and Kansas City both treat Missouri/Mississippi River water at scale and hold strong compliance records; Missouri American Water's St. Louis County operation is one of the largest investor-owned systems in the country. Springfield and the Ozarks lean on wells and reservoirs.",
            "Missouri's mining legacy (the Old Lead Belt) left elevated lead in some southeast groundwater and soils, karst geology makes Ozark springs quick to contaminate, and small-system violations (bacteria, DBPs, occasional radium) track the state's large rural footprint.",
        ],
        n_systems="about 1,390",
        contaminants=[
            ("Lead", "Legacy from both mining districts and old urban service lines; St. Louis and KC run corrosion control and replacement programs"),
            ("Bacteria in karst systems", "Ozark springs and shallow wells are vulnerable to rapid surface intrusion after storms"),
            ("Radium", "Naturally occurring exceedances in scattered small groundwater systems"),
        ],
        violations="The metro systems are reliably compliant; most violations occur in small rural systems. The state uses regionalization grants to fold struggling systems into stronger neighbors.",
        faqs=[
            ("Is tap water safe to drink in Missouri?", "Yes in St. Louis, Kansas City, Springfield, and the major systems, all EPA-compliant. Small Ozark and Bootheel systems account for most advisories."),
            ("Does the Old Lead Belt affect drinking water?", "Mining-district soils and some groundwater in southeast Missouri carry elevated lead, affecting private wells and a few small systems; public systems there treat and monitor accordingly."),
            ("Why do Ozark wells need extra care?", "Karst limestone funnels surface water (and contamination) into aquifers within hours; spring-fed and shallow-well supplies need disinfection and post-storm caution."),
        ],
        meta_description="Missouri tap water: big-river metro treatment, Old Lead Belt legacy, and karst spring risks. Search water quality for your ZIP code."),
]
