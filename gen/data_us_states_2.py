# -*- coding: utf-8 -*-
"""US state water-quality profiles, Montana through Wyoming.
System counts are approximate EPA SDWIS community water system figures; contaminant
notes reflect publicly documented EPA/EWG/state agency reporting as of 2026."""

STATES_2 = [
    dict(slug="montana", name="Montana", abbr="MT",
        overview=[
            "Montana's cities drink well: Bozeman and Missoula use mountain snowmelt and clean valley aquifers, Billings treats Yellowstone River water, and the major systems meet all federal standards. Missoula's aquifer is among the most productive and pristine urban sources in the West.",
            "The state's mining century left its mark: Butte's Berkeley Pit is America's most infamous acid-mine lake (isolated from drinking supplies, but emblematic), and legacy metals affect some streams and private wells near historic districts. Naturally occurring arsenic tracks the Madison and Missouri River systems downstream of Yellowstone's geothermal basins.",
        ],
        n_systems="about 730",
        contaminants=[
            ("Arsenic", "Geothermally sourced arsenic in the Madison/Missouri drainage affects some systems and wells; treated where needed"),
            ("Mining-legacy metals", "Copper, zinc, and arsenic near historic districts (Butte, Anaconda) affect surface water and some private wells, not compliant public systems"),
            ("Nitrate and bacteria in wells", "Rural private wells, common across the state, need routine testing"),
        ],
        violations="Public-system compliance is solid; most violations are monitoring lapses in very small systems. Superfund work around Butte and Anaconda addresses the mining legacy separately from drinking-water systems.",
        faqs=[
            ("Is tap water safe to drink in Montana?", "Yes: Billings, Missoula, Bozeman, and the major systems meet all EPA standards, and several draw exceptionally clean mountain sources."),
            ("Does the Berkeley Pit threaten drinking water?", "The pit's acidic water is contained and pumped/treated under Superfund management; Butte's drinking water comes from separate protected sources and meets standards."),
            ("Why does the Madison River carry arsenic?", "Yellowstone's geothermal features feed naturally arsenic-rich water into the drainage; downstream systems account for it in treatment and monitoring."),
        ],
        meta_description="Montana tap water: pristine mountain city supplies, Butte's mining legacy, and geothermal arsenic. Look up your water system by ZIP."),

    dict(slug="nebraska", name="Nebraska", abbr="NE",
        overview=[
            "Omaha (Metropolitan Utilities District) and Lincoln both deliver fully compliant water, drawing on the Missouri and Platte River alluvial systems. Nebraska sits atop the High Plains aquifer, and most of the state drinks groundwater.",
            "Agriculture defines the risk map: nitrate is the state's chief contaminant, with dozens of small towns treating or drilling new wells, and research linking high-nitrate regions to health concerns keeps it politically live. Naturally occurring uranium co-occurs with nitrate in some aquifers, an increasingly documented pairing.",
        ],
        n_systems="about 590",
        contaminants=[
            ("Nitrate", "The state's dominant violation; irrigated corn country loads the aquifer, hitting small systems and private wells hardest"),
            ("Uranium", "Naturally occurring and mobilized by nitrate chemistry in some groundwater; several small systems have installed removal"),
            ("Atrazine", "Seasonal pulses in Platte-influenced supplies, generally within limits"),
        ],
        violations="Omaha and Lincoln are consistently compliant. Nitrate exceedances in small systems account for most enforcement, with state programs funding treatment, blending, and well relocation.",
        faqs=[
            ("Is tap water safe to drink in Nebraska?", "Yes in Omaha, Lincoln, and the larger systems. In farm country, small systems and private wells warrant regular nitrate testing, which the state subsidizes."),
            ("Why is nitrate rising in Nebraska groundwater?", "A century of irrigated, fertilized corn production over permeable soils feeds nitrogen steadily into the High Plains aquifer; trends move slowly and will persist for decades."),
            ("Is Nebraska water hard?", "Yes, moderately to very hard in most of the state: a taste and appliance matter, not a safety one."),
        ],
        meta_description="Nebraska tap water: compliant metro systems over the High Plains aquifer, farm-driven nitrate, and uranium pockets. Check your ZIP code."),

    dict(slug="nevada", name="Nevada", abbr="NV",
        overview=[
            "Nine in ten Nevadans drink Colorado River water from Lake Mead, treated by the Southern Nevada Water Authority for the Las Vegas Valley, or Truckee River water treated by TMWA in Reno. Both operations are heavily monitored and fully compliant, with SNWA's drought engineering (including the 'third straw' intake) nationally known.",
            "The water is very hard and mineral-rich, the state's top consumer complaint but not a safety issue. Outside the metros, some rural basins carry naturally occurring arsenic (the Fallon area is well documented) and uranium, and small systems treat or blend accordingly.",
        ],
        n_systems="about 180",
        contaminants=[
            ("Hardness and TDS", "Lake Mead water runs 250-300 mg/L hardness: softeners are common, safety is unaffected"),
            ("Arsenic", "Naturally elevated in several rural basins (Fallon, Fernley historically); affected systems installed treatment after the 2006 arsenic rule"),
            ("Perchlorate legacy", "The Henderson industrial site once fed perchlorate into Lake Mead; remediation cut levels dramatically and current water meets all standards"),
        ],
        violations="The metro systems are consistently compliant. Rural arsenic drove a wave of small-system treatment installs; monitoring violations in tiny systems remain the most common enforcement item.",
        faqs=[
            ("Is tap water safe to drink in Nevada?", "Yes: Las Vegas and Reno meet all EPA standards. The hardness that fuels complaints is cosmetic, and rural arsenic systems have largely installed treatment."),
            ("Is Las Vegas running out of water?", "Lake Mead's decline is a supply-planning crisis, not a quality one: SNWA's deep intake and aggressive recycling keep delivery secure, and the tap water remains fully treated and monitored."),
            ("What was the Henderson perchlorate problem?", "Cold War-era rocket-fuel manufacturing leached perchlorate into groundwater reaching Lake Mead. Remediation since the early 2000s reduced river loading by over 90%, and current levels are well within safety benchmarks."),
        ],
        meta_description="Nevada tap water: Lake Mead supply, very hard water, rural arsenic, and the perchlorate cleanup. Look up your ZIP code here."),

    dict(slug="new-hampshire", name="New Hampshire", abbr="NH",
        overview=[
            "New Hampshire's public systems, Manchester's Lake Massabesic supply chief among them, are clean and compliant. But nearly half the state drinks from private bedrock wells, and that is where New Hampshire's two signature contaminants live: arsenic and PFAS.",
            "The state's granite bedrock naturally yields arsenic (New Hampshire adopted a 5 ppb standard, twice as strict as EPA's), and the Saint-Gobain plastics plant in Merrimack created one of New England's major PFAS plumes, extending bottled water and treatment to thousands of properties. New Hampshire was among the first states to set enforceable PFAS limits.",
        ],
        n_systems="about 690",
        contaminants=[
            ("Arsenic in bedrock wells", "Roughly one in five private wells exceeds the state's strict 5 ppb standard; testing rates remain the public-health gap"),
            ("PFAS", "The Merrimack Saint-Gobain plume plus scattered military/industrial sites; state limits among the nation's first, treatment ongoing"),
            ("Radon and uranium", "Granite geology yields radionuclides in some wells; mitigation is well established"),
        ],
        violations="Public systems show strong compliance, with PFAS remediation the active front. The state's focus is private wells, which serve almost half of residents outside any federal rule.",
        faqs=[
            ("Is tap water safe to drink in New Hampshire?", "On public systems, yes: Manchester, Nashua, and Concord all comply fully. On private wells, test for arsenic, PFAS, and radon: the state's geology and industrial history make all three realistic."),
            ("What did Saint-Gobain do in Merrimack?", "Air emissions from its plastics plant deposited PFOA across the area, contaminating public wells and hundreds of private ones. Consent decrees funded waterline extensions, treatment, and monitoring across several towns."),
            ("Why is New Hampshire's arsenic standard stricter than EPA's?", "State studies tied low-level arsenic in wells to health risks, prompting a 5 ppb standard (half the federal 10 ppb) for public systems, with private-well testing campaigns alongside."),
        ],
        meta_description="New Hampshire tap water: granite-state arsenic, the Merrimack PFAS plume, and clean public systems. Check your town or ZIP code."),

    dict(slug="new-jersey", name="New Jersey", abbr="NJ",
        overview=[
            "New Jersey packs dense population, heavy industrial legacy, and some of the nation's most protective water rules into one small state: it set the first enforceable PFAS standards in the country and runs aggressive lead-line replacement mandates. Big systems (Newark, Jersey City, NJ American Water, Passaic Valley) meet federal and state standards.",
            "Newark's 2019 lead crisis became a national story and then a national model: the city replaced over 23,000 lead service lines in under three years, faster than any comparable program. PFAS detections remain widespread given the industrial footprint, with treatment installs rolling across the state.",
        ],
        n_systems="about 580",
        contaminants=[
            ("PFAS", "Among the most widespread detections in the nation due to industry density; New Jersey's early standards forced treatment years before federal rules"),
            ("Lead from service lines", "Statewide replacement mandate (10-year deadline) following Newark's crisis and turnaround"),
            ("Disinfection byproducts and legacy VOCs", "Managed within limits; legacy solvent plumes affect some wellfields with air-stripping treatment in place"),
        ],
        violations="Compliance among major systems is solid and state oversight is unusually strict. Newark's water now meets lead standards after full replacement; PFAS treatment construction is the state's biggest active compliance program.",
        faqs=[
            ("Is tap water safe to drink in New Jersey?", "Yes: the major systems meet all federal and stricter state standards. Newark's lead levels dropped below action thresholds after its record-speed pipe replacement."),
            ("Is Newark's water safe now?", "Yes. After the 2019 crisis, Newark replaced 23,000+ lead lines by 2022 and lead readings fell well below the federal action level: now cited as the national template for rapid replacement."),
            ("Why does New Jersey lead on PFAS rules?", "Its chemical-industry legacy made contamination widespread and visible early; the state's scientists recommended strict limits (13-14 ppt) adopted in 2018-2020, first in the nation and a model for the federal standard."),
        ],
        meta_description="New Jersey tap water: first-in-nation PFAS rules, Newark's lead-pipe turnaround, and industrial-legacy cleanup. Look up your ZIP."),

    dict(slug="new-mexico", name="New Mexico", abbr="NM",
        overview=[
            "Albuquerque secured its water future with the San Juan-Chama project, importing Colorado River basin water to rest its aquifer, and the city's supply meets all federal standards. Santa Fe blends reservoirs, wells, and the same imported water.",
            "New Mexico's risks are rural and mineral: naturally occurring arsenic and uranium in groundwater (the uranium-mining legacy on and near Navajo lands left hundreds of unremediated sites and contaminated wells), plus PFAS plumes at Cannon and Holloman Air Force bases that rank among the nation's worst.",
        ],
        n_systems="about 560",
        contaminants=[
            ("Arsenic", "Naturally elevated across Rio Grande rift groundwater; Albuquerque treats and blends, and small systems account for most exceedances"),
            ("Uranium", "Mining legacy plus natural occurrence affects wells in the Grants belt and Navajo Nation communities, many outside public-system regulation"),
            ("PFAS", "Cannon AFB's plume contaminated dairy wells near Clovis in one of the country's starkest agricultural PFAS cases; Holloman's lakebed levels are among the highest recorded"),
        ],
        violations="Albuquerque, Las Cruces, and Santa Fe comply fully. Small-system arsenic exceedances are the routine violation; uranium-legacy and base-plume cleanups run as long-term federal projects.",
        faqs=[
            ("Is tap water safe to drink in New Mexico?", "Yes in Albuquerque, Santa Fe, and Las Cruces, all EPA-compliant. Rural wells, especially in the uranium belt and near air bases, need testing through state and IHS programs."),
            ("What is the uranium legacy on Navajo lands?", "Cold War mining left 500+ abandoned mines; some communities' unregulated wells show uranium and arsenic, and federal cleanup plus water-hauling alternatives progress slowly: a major environmental-justice case."),
            ("How bad is the PFAS contamination at Cannon AFB?", "Firefighting foam contaminated groundwater used by nearby dairies, forcing milk destruction and herd culls near Clovis: one of the first cases of PFAS entering the food chain via agriculture. Remediation and litigation continue."),
        ],
        meta_description="New Mexico tap water: compliant cities, uranium-belt wells, and severe base PFAS plumes. Search your water system by ZIP code."),

    dict(slug="new-york", name="New York", abbr="NY",
        overview=[
            "New York City's Catskill/Delaware supply is the largest unfiltered system on earth, protected by a watershed program so effective the EPA waives filtration for 8.5 million people, and the water routinely wins taste awards. Upstate cities run conventional systems on lakes and rivers.",
            "Outside the city, the record is more mixed: Hoosick Falls' PFOA crisis (2014-2016) made the state an early PFAS regulator, Newburgh's supply was contaminated by Stewart Air Base foam, and Long Island's sole-source aquifer carries 1,4-dioxane and PFAS from decades of industry, driving the nation's most extensive treatment build-out there.",
        ],
        n_systems="about 2,300",
        contaminants=[
            ("PFAS", "Hoosick Falls and Newburgh became national cases; state limits (10 ppt) preceded federal rules and Long Island systems installed dozens of treatment units"),
            ("1,4-Dioxane", "Long Island's signature contaminant from industrial solvents; New York set the nation's first enforceable limit and AOP treatment is being installed across Nassau/Suffolk"),
            ("Lead from plumbing", "Older upstate cities (Buffalo, Syracuse, Albany) carry legacy service lines with replacement programs accelerating"),
        ],
        violations="NYC's system is consistently compliant with a filtration waiver held since 1993 (UV disinfection added). Long Island's treatment retrofit and small upstate systems account for most active compliance work.",
        faqs=[
            ("Is tap water safe to drink in New York State?", "Yes: NYC's protected mountain supply is world-famous, and the major upstate systems comply fully. Long Island's water meets standards via heavy treatment investment against legacy industrial contaminants."),
            ("Why doesn't New York City filter its water?", "Decades of watershed land protection in the Catskills keep source water clean enough for an EPA filtration avoidance waiver: the largest in the world, maintained by a billion-dollar protection program that is cheaper than a filtration plant."),
            ("What happened in Hoosick Falls?", "PFOA from plastics manufacturing contaminated the village wells, discovered in 2014-2015. The fallout produced medical monitoring settlements, New York's strict PFAS limits, and treatment for the village supply."),
        ],
        meta_description="New York tap water: NYC's unfiltered mountain supply, Long Island's treatment build-out, and Hoosick Falls' legacy. Check your ZIP code."),

    dict(slug="north-carolina", name="North Carolina", abbr="NC",
        overview=[
            "North Carolina's Piedmont cities (Charlotte, Raleigh, Durham, Greensboro, Winston-Salem) run modern reservoir-fed systems that meet all federal standards. The coastal plain leans on groundwater and smaller systems.",
            "The Cape Fear River made the state a PFAS epicenter: Chemours' Fayetteville Works discharged GenX and related compounds for decades, contaminating Wilmington's supply downstream and thousands of private wells nearby. A consent order forced emissions cuts, well remediation, and advanced treatment (Wilmington's granular activated carbon plant is among the nation's largest responses). Coal-ash pond seepage into groundwater has been the other long-running fight.",
        ],
        n_systems="about 2,000",
        contaminants=[
            ("PFAS / GenX", "The Cape Fear basin case is nationally defining: downstream utilities installed major treatment and Chemours operates under a consent order with ongoing well testing"),
            ("Coal-ash constituents", "Groundwater near legacy ash ponds showed boron, cobalt, and arsenic; excavation settlements are removing ash statewide"),
            ("Lead from plumbing", "Older urban housing carries typical legacy-plumbing risk; utilities run corrosion control"),
        ],
        violations="The big Piedmont utilities are consistently compliant. GenX-era scrutiny made North Carolina's PFAS monitoring among the most intensive anywhere; small coastal and mountain systems account for routine violations.",
        faqs=[
            ("Is tap water safe to drink in North Carolina?", "Yes across the major metros, and Wilmington's water now passes through one of the country's largest carbon treatment plants specifically to remove PFAS. Private wells near Fayetteville Works should be in Chemours' testing program."),
            ("What is GenX and why is it tied to North Carolina?", "GenX is a PFAS compound Chemours used and discharged into the Cape Fear River, contaminating downstream drinking supplies: discovered publicly in 2017, it triggered a consent order, health studies, and the treatment build-out."),
            ("Did coal ash contaminate North Carolina drinking water?", "Groundwater near several Duke Energy ash ponds exceeded standards for ash-related constituents, prompting bottled-water programs, waterline extensions, and court-ordered excavation of the ponds."),
        ],
        meta_description="North Carolina tap water: GenX and the Cape Fear PFAS fight, coal ash cleanup, and compliant Piedmont metros. Look up your ZIP."),

    dict(slug="north-dakota", name="North Dakota", abbr="ND",
        overview=[
            "Fargo and Grand Forks treat Red River water, Bismarck sits on excellent Missouri River supply, and the major systems comply fully. The signature achievement is rural: pipeline networks like the Southwest Pipeline and Northwest Area Water Supply now deliver treated Missouri River water across enormous thinly populated areas, replacing poor-quality local wells.",
            "Natural groundwater quality is the historic weakness: high sulfates, sodium, and total dissolved solids made many prairie wells barely drinkable, which is why the state built its pipeline systems. Oil-patch activity in the Bakken adds localized spill and brine-disposal concerns for shallow aquifers.",
        ],
        n_systems="about 320",
        contaminants=[
            ("Sulfates and TDS", "Naturally high in prairie groundwater; the driver behind regional pipeline systems rather than a violation issue in treated supplies"),
            ("Nitrate and bacteria in wells", "Standard rural private-well risks, with state testing programs available"),
            ("Bakken brine spills", "Localized saltwater-disposal and pipeline incidents affect some shallow aquifers and streams; monitored by state regulators"),
        ],
        violations="Compliance is strong and improving as regional systems replace marginal wells; remaining violations are mostly monitoring lapses in very small systems.",
        faqs=[
            ("Is tap water safe to drink in North Dakota?", "Yes: Fargo, Bismarck, and the regional pipeline systems deliver fully compliant water, and rural quality has improved dramatically as pipelines replaced mineral-heavy wells."),
            ("Why did North Dakota build rural water pipelines?", "Prairie groundwater is often high in sulfates and dissolved solids: legal to drink but unpleasant and hard on plumbing: so the state pipes treated Missouri River water hundreds of miles to farms and small towns."),
            ("Does oil development threaten drinking water?", "Bakken brine spills have damaged localized shallow groundwater and streams; public systems drawing deep or surface sources are unaffected, and the state tracks incidents publicly."),
        ],
        meta_description="North Dakota tap water: regional pipelines replacing sulfate-heavy wells, compliant cities, and Bakken caveats. Check your ZIP code."),

    dict(slug="ohio", name="Ohio", abbr="OH",
        overview=[
            "Ohio's three C's are well served: Columbus runs reservoir and aquifer plants, Cincinnati's Ohio River plant pioneered granular activated carbon treatment (a national reference facility), and Cleveland treats Lake Erie water at four large plants. All meet federal standards.",
            "Toledo's 2014 'do not drink' weekend, when a Lake Erie algal bloom's microcystin toxin overwhelmed the plant, reshaped harmful-algal-bloom monitoring nationwide; Toledo has since invested heavily in ozone and monitoring. Legacy lead lines across old industrial cities and East Palestine's 2023 derailment (which spared the municipal supply but scarred trust) round out the picture.",
        ],
        n_systems="about 1,200",
        contaminants=[
            ("Algal toxins (microcystin)", "Western Lake Erie blooms recur each summer, fed by farm runoff; plants now carry ozone/carbon defenses and real-time monitoring"),
            ("Lead from service lines", "Cleveland, Cincinnati, and the industrial belt carry large legacy inventories under replacement mandates"),
            ("PFAS", "Statewide sampling found scattered detections; treatment planning proceeds under federal limits"),
        ],
        violations="Metro systems comply consistently; the compliance frontier is bloom-season vigilance on Lake Erie and lead-line replacement. Small-system violations follow the usual rural pattern.",
        faqs=[
            ("Is tap water safe to drink in Ohio?", "Yes: Columbus, Cleveland, Cincinnati, and Toledo all meet EPA standards, with Toledo now running some of the nation's most advanced bloom monitoring after 2014."),
            ("Could the Toledo water crisis happen again?", "The risk is managed rather than gone: blooms still form most summers, but ozone treatment, early-warning buoys, and revised protocols mean detection and response now happen before toxins reach taps."),
            ("Did the East Palestine derailment contaminate drinking water?", "Municipal supplies tested safe throughout; monitoring focused on private wells near the site and on the Ohio River plume, which downstream utilities tracked and dodged with intake closures."),
        ],
        meta_description="Ohio tap water: Lake Erie bloom defenses after Toledo 2014, Cincinnati's carbon pioneering, and lead-line work. Check your ZIP."),

    dict(slug="oklahoma", name="Oklahoma", abbr="OK",
        overview=[
            "Oklahoma City pipes water from reservoirs across the state (including Canton Lake and southeast Oklahoma's Atoka pipeline) and Tulsa draws Spavinaw and Oologah lakes; both metros meet all federal standards.",
            "Rural Oklahoma shows the strain: many small systems face disinfection byproduct exceedances and aging plants, southeastern karst and old zinc-mining land (the Tar Creek Superfund site at Picher) left localized metals contamination, and naturally occurring arsenic, selenium, and chromium appear in western groundwater pockets.",
        ],
        n_systems="about 1,300",
        contaminants=[
            ("Disinfection byproducts", "The most common exceedance across small reservoir-fed systems with long distribution runs"),
            ("Mining-legacy metals", "Tar Creek's lead and zinc contaminated Ottawa County groundwater; affected communities were relocated or connected to alternate supplies"),
            ("Arsenic and selenium", "Natural pockets in western Oklahoma groundwater trigger occasional small-system violations"),
        ],
        violations="The metros are reliably compliant; Oklahoma's violation counts concentrate in its very large roster of small rural systems, and consolidation moves slowly. Tar Creek remains one of the nation's oldest active Superfund sites.",
        faqs=[
            ("Is tap water safe to drink in Oklahoma?", "Yes in Oklahoma City, Tulsa, and Norman, which meet all EPA standards. Small-town systems carry more frequent DBP notices: check your annual report."),
            ("What is Tar Creek?", "A former lead-zinc mining district around Picher where acid mine water and chat piles contaminated groundwater and soil so thoroughly the federal government bought out and relocated the towns: Oklahoma's starkest water legacy."),
            ("Where does Oklahoma City get its water?", "From a portfolio of reservoirs including Hefner and Overholser locally, Canton Lake to the northwest, and McGee Creek/Atoka in the southeast, moved by one of the longer municipal pipeline networks in the country."),
        ],
        meta_description="Oklahoma tap water: compliant metros, small-system DBP notices, and the Tar Creek mining legacy. Look up your water by ZIP code."),

    dict(slug="oregon", name="Oregon", abbr="OR",
        overview=[
            "Portland drinks from the Bull Run watershed, a federally protected forest reserve closed to the public since 1904, one of America's premier municipal sources. A 2017 cryptosporidium detection ended its filtration waiver, and the city's new filtration plant (due 2027) is its largest-ever infrastructure project; water remains safe and compliant meanwhile.",
            "Salem's 2018 algal-toxin advisory from Detroit Lake pushed bloom monitoring statewide, and Eugene's McKenzie River supply is among the cleanest anywhere. East of the Cascades, agricultural nitrate in the Lower Umatilla Basin has left rural well users with the state's most serious ongoing contamination problem.",
        ],
        n_systems="about 900",
        contaminants=[
            ("Cryptosporidium risk", "Low-level Bull Run detections triggered Portland's filtration mandate; UV and the new plant close the gap"),
            ("Algal toxins", "Cascade reservoir blooms (Detroit Lake) require seasonal monitoring for Salem and neighbors"),
            ("Nitrate", "The Lower Umatilla Basin's groundwater exceeds limits under decades of farm and food-processing load; a declared emergency for private well users"),
        ],
        violations="The big western systems comply fully. The state's hardest problem is the Umatilla Basin nitrate emergency affecting rural wells, where bottled water and treatment programs are still scaling.",
        faqs=[
            ("Is tap water safe to drink in Oregon?", "Yes: Portland, Eugene, Salem, and Bend all meet federal standards, with Portland's protected Bull Run source famously pure while its filtration plant is completed."),
            ("Why is Portland building a filtration plant?", "Cryptosporidium detections in 2017 ended the city's filtration waiver; regulators mandated filtration by 2027, and the plant also adds wildfire-ash and turbidity resilience for the century ahead."),
            ("What is the Umatilla Basin nitrate problem?", "Decades of irrigation, food processing, and dairy operations pushed nitrate above safe limits in the shallow aquifer serving rural wells near Boardman and Hermiston: Oregon's most urgent drinking-water inequity, now under state emergency response."),
        ],
        meta_description="Oregon tap water: Bull Run's protected purity, Portland's new filtration plant, and the Umatilla nitrate emergency. Check your ZIP."),

    dict(slug="pennsylvania", name="Pennsylvania", abbr="PA",
        overview=[
            "Philadelphia treats Delaware and Schuylkill river water at three plants with a solid compliance record; Pittsburgh's PWSA emerged from its 2016-2019 lead crisis with replaced lines, orthophosphate treatment, and readings now well below action levels. Pennsylvania American Water and hundreds of authorities cover the rest.",
            "The state carries heavy legacies: among the nation's largest lead service line inventories, PFAS clusters in the Philadelphia suburbs (Willow Grove and Warminster military sites drove some of the country's earliest municipal PFAS responses), abandoned-mine drainage staining thousands of stream miles, and private-well country with no statewide construction standards.",
        ],
        n_systems="about 1,900",
        contaminants=[
            ("Lead from service lines", "Pittsburgh's turnaround is the model case; Philadelphia and the older boroughs continue large replacement programs"),
            ("PFAS", "Bucks/Montgomery county plumes from military foam made Horsham, Warminster, and Warrington early adopters of zero-tolerance treatment; state limits adopted 2023"),
            ("Abandoned-mine drainage", "Acidic, metal-laden drainage affects streams and some small-source watersheds in coal country"),
        ],
        violations="The major systems comply; Pittsburgh's lead exceedances ended after treatment and replacement. Pennsylvania's long tail of small systems and its million-plus unregulated private wells shape most remaining risk.",
        faqs=[
            ("Is tap water safe to drink in Pennsylvania?", "Yes: Philadelphia and Pittsburgh both meet all federal standards, Pittsburgh having driven lead well below action levels since 2020 after its replacement program."),
            ("What happened with Pittsburgh's lead crisis?", "A 2014 corrosion-control change (made without approval) preceded rising lead readings; after enforcement and public pressure, PWSA replaced 10,000+ lines, restored orthophosphate, and now posts some of its best-ever results."),
            ("Which Pennsylvania areas dealt with PFAS first?", "The Willow Grove/Warminster area north of Philadelphia, where Navy and Air Guard foam contaminated public wells: local utilities set zero-detection goals and installed treatment nearly a decade before federal limits."),
        ],
        meta_description="Pennsylvania tap water: Pittsburgh's lead recovery, Philly-suburb PFAS pioneers, and mine-drainage legacies. Look up your ZIP code."),

    dict(slug="rhode-island", name="Rhode Island", abbr="RI",
        overview=[
            "Providence Water's Scituate Reservoir supplies about 60% of Rhode Islanders with well-protected, consistently compliant water, and the state's compact geography keeps most residents on a handful of professional systems.",
            "The live issue is lead: Providence's old housing stock sits on one of New England's larger lead-line inventories, and the utility has cycled above the federal action level in past sampling rounds, driving an accelerating replacement program (with free replacements funded since 2023). PFAS detections in a few wells led to state limits and treatment.",
        ],
        n_systems="about 480",
        contaminants=[
            ("Lead from service lines", "Providence's legacy inventory produced past action-level exceedances; free full-replacement programs and corrosion control are cutting readings"),
            ("PFAS", "Scattered well detections (Oakland/Burrillville among the first) brought state limits and treatment or interconnections"),
            ("Sodium from road salt", "Rising in some wellfields, flagged for restricted diets"),
        ],
        violations="The Scituate supply itself is excellent; compliance attention centers on Providence's lead plumbing rather than source or treatment failures. Small systems show typical monitoring-violation patterns.",
        faqs=[
            ("Is tap water safe to drink in Rhode Island?", "Yes: the Scituate Reservoir supply meets all standards. In pre-1950 Providence housing, use a lead-rated filter until your service line is replaced: the city offers free replacements."),
            ("Why does Providence have lead issues if its reservoir is clean?", "The water leaves treatment lead-free but passes through tens of thousands of old lead service lines; corrosion control reduces leaching while replacement, now free to homeowners, removes the source."),
            ("Does Rhode Island regulate PFAS?", "Yes: enforceable interim limits took effect in 2022-2023, with statewide testing and treatment where wells exceeded them."),
        ],
        meta_description="Rhode Island tap water: Scituate Reservoir quality, Providence's lead-line push, and PFAS limits. Check your city or ZIP code."),

    dict(slug="south-carolina", name="South Carolina", abbr="SC",
        overview=[
            "South Carolina's major systems (Charleston Water, Columbia, Greenville Water's protected mountain reservoirs) meet all federal standards, with Greenville's supply regarded as one of the Southeast's best.",
            "The cautionary tale is Denmark, the small town whose decade-long use of an unapproved well additive (HaloSan) and discolored water became a national environmental-justice story. More broadly the state faces PFAS in the rivers that supply the Midlands and Pee Dee, radium in some coastal-plain aquifers, and struggling small systems that the state has pushed to consolidate.",
        ],
        n_systems="about 660",
        contaminants=[
            ("PFAS", "River detections above new federal limits affect several Midlands and Pee Dee systems now planning treatment; textile-industry legacy contributes"),
            ("Radium", "Naturally occurring exceedances in a band of coastal-plain groundwater systems"),
            ("Disinfection byproducts", "The routine small-system exceedance, especially in warm months"),
        ],
        violations="Metro systems comply consistently. Denmark's saga drove reforms in state oversight of small systems; radium and DBP violations in small systems remain the routine enforcement load.",
        faqs=[
            ("Is tap water safe to drink in South Carolina?", "Yes in Charleston, Columbia, Greenville, and the major systems. Small-town systems have a weaker record: check local reports, and note several utilities are adding PFAS treatment under the new federal rule."),
            ("What happened in Denmark, SC?", "For a decade the town dosed one well with HaloSan, a disinfectant not approved for drinking water, while residents complained of discolored water: exposed by researchers in 2018, it forced the well's closure and became a symbol of small-system neglect."),
            ("Which South Carolina rivers carry PFAS?", "Sampling found elevated PFAS in stretches of the Congaree, Saluda, and Pee Dee basins serving downstream utilities, several of which now plan carbon or ion-exchange treatment."),
        ],
        meta_description="South Carolina tap water: Greenville's mountain supply, the Denmark scandal, and river PFAS. Look up your water system by ZIP."),

    dict(slug="south-dakota", name="South Dakota", abbr="SD",
        overview=[
            "Sioux Falls blends Big Sioux aquifer wells with Missouri River water from the Lewis & Clark regional pipeline, a multi-state project that has transformed supply reliability across the region; Rapid City draws clean Black Hills sources. Both comply fully.",
            "Rural South Dakota mirrors its neighbors: naturally mineral-heavy prairie groundwater (iron, sulfates, TDS) pushed the state into regional rural water systems, agricultural nitrate pressures shallow wells, and scattered arsenic and uranium occurrences track Black Hills geology and legacy mining at Edgemont.",
        ],
        n_systems="about 470",
        contaminants=[
            ("Nitrate", "Shallow ag-area wells and a few small systems exceed limits after wet cycles"),
            ("Sulfates, iron, TDS", "Natural prairie groundwater character: the driver for regional pipeline supply rather than a health violation"),
            ("Arsenic and uranium", "Localized Black Hills-area occurrences in wells; testing recommended"),
        ],
        violations="Compliance is solid, strengthened as Lewis & Clark pipeline water replaces marginal local wells; remaining violations are small-system nitrate and monitoring lapses.",
        faqs=[
            ("Is tap water safe to drink in South Dakota?", "Yes: Sioux Falls and Rapid City meet all EPA standards, and the regional pipelines have upgraded rural supply quality substantially."),
            ("What is the Lewis & Clark Regional Water System?", "A pipeline network treating Missouri River water near Vermillion and delivering it to member cities across South Dakota, Iowa, and Minnesota: the fix for a region of poor natural groundwater."),
            ("Should rural well owners test their water?", "Yes: nitrate after wet years and naturally occurring minerals (plus arsenic near the Black Hills) make periodic testing the state-recommended practice."),
        ],
        meta_description="South Dakota tap water: Lewis & Clark pipeline supply, prairie groundwater minerals, and rural well testing. Check your ZIP code."),

    dict(slug="tennessee", name="Tennessee", abbr="TN",
        overview=[
            "Memphis drinks from the Memphis Sand aquifer: ancient, naturally filtered artesian water widely called some of the best-tasting municipal supply in America. Nashville, Knoxville, and Chattanooga treat river water to full compliance.",
            "The watchpoints: TVA's Allen plant wells near Memphis raised (contained) concerns about pulling shallow contaminated groundwater toward the drinking aquifer, coal-ash legacy at Kingston (site of the 2008 spill) still shadows the state's utility politics, and Appalachian small systems carry the usual DBP and infrastructure strain.",
        ],
        n_systems="about 460",
        contaminants=[
            ("Disinfection byproducts", "Routine exceedances in small upland surface-water systems"),
            ("Lead from plumbing", "Older Memphis and Nashville housing carries standard legacy-plumbing risk; utilities run corrosion control"),
            ("Coal-ash constituents", "Kingston's 2008 spill and ash-pond groundwater seepage remain monitored legacies near TVA sites, separate from compliant public supplies"),
        ],
        violations="The four metro systems are consistently compliant, and Memphis' aquifer needs minimal treatment. Small-system DBPs in the mountains generate most violations.",
        faqs=[
            ("Is tap water safe to drink in Tennessee?", "Yes: Memphis' aquifer water and the treated river supplies of Nashville, Knoxville, and Chattanooga all meet EPA standards."),
            ("Why is Memphis water considered special?", "It rises from the Memphis Sand aquifer, rainwater filtered through sand for centuries, so it arrives naturally clean, soft-tasting, and needing little treatment: the largest US city relying solely on artesian groundwater."),
            ("Is the Memphis aquifer threatened?", "Studies found leaks in the protective clay layer that could let shallow contaminated water migrate downward near heavy pumping; TVA switched its Allen plant off aquifer wells, and monitoring guards the resource."),
        ],
        meta_description="Tennessee tap water: the Memphis Sand aquifer's famous purity, compliant river metros, and coal-ash legacies. Check your ZIP."),

    dict(slug="texas", name="Texas", abbr="TX",
        overview=[
            "Texas runs the nation's largest water-system roster, roughly 4,600 community systems, from Dallas, Houston, and San Antonio's fully compliant metro giants (San Antonio's Edwards Aquifer supply needs little more than disinfection) down to thousands of small rural utilities where most problems live.",
            "The 2021 winter storm exposed the grid-water nexus (14 million Texans under boil notices), and the state leads the country in boil-water advisories most years. Naturally occurring arsenic and radium in West Texas and Hill Country groundwater, nitrate in the Panhandle, and colonias along the border still lacking full service round out a state of extremes.",
        ],
        n_systems="about 4,600",
        contaminants=[
            ("Radium and radionuclides", "Hill Country and West Texas granite-belt groundwater produces the nation's largest cluster of small-system radium violations"),
            ("Arsenic", "Naturally elevated across West Texas basins; dozens of small systems run treatment or variances"),
            ("Nitrate", "Panhandle and agricultural-belt groundwater exceedances in small systems and private wells"),
            ("Boil-water advisories", "Pressure-loss advisories after storms, freezes, and main breaks are the state's most common consumer-facing event"),
        ],
        violations="Metro systems are reliably compliant; Texas' violation totals lead the nation mostly because its small-system count does. Radionuclides and arsenic dominate health-based exceedances, and hardening systems against freeze events is the post-2021 priority.",
        faqs=[
            ("Is tap water safe to drink in Texas?", "Yes in the major cities: Houston, Dallas, San Antonio, Austin, and Fort Worth all meet EPA standards. Small rural systems carry most of the state's violations, and boil notices after freezes or breaks should always be followed."),
            ("Why does Texas issue so many boil-water notices?", "Any pressure loss triggers a precautionary notice, and with 4,600+ systems, aging rural infrastructure, hurricanes, and freeze events, Texas simply has more trigger events than anywhere else."),
            ("What is special about San Antonio's water?", "It flows from the Edwards Aquifer, a karst limestone system so clean the city historically needed only disinfection: now supplemented by desalination and storage projects to reduce drought dependence on the aquifer."),
        ],
        meta_description="Texas tap water: compliant metro giants, 4,600 systems, radium belts, and the boil-notice capital. Look up your water by ZIP code."),

    dict(slug="utah", name="Utah", abbr="UT",
        overview=[
            "Salt Lake City pipes snowmelt straight from protected Wasatch canyons, some of the youngest, cleanest municipal water in the country, and the Wasatch Front districts meet all federal standards. Rapid growth, not quality, is the defining pressure.",
            "Southern and rural Utah rely on groundwater with localized arsenic (notably around Hinckley and parts of the west desert) and legacy uranium-mill sites along the Colorado Plateau; the shrinking Great Salt Lake raises dust and water-supply questions rather than direct tap-quality ones.",
        ],
        n_systems="about 480",
        contaminants=[
            ("Arsenic", "Naturally occurring in west-desert and some southern groundwater; small systems treat, blend, or truck water"),
            ("Uranium-mill legacy", "Plateau-country sites (Moab's tailings removal, nearly complete) affected localized groundwater, managed under federal cleanup"),
            ("Hardness", "Valley groundwater runs hard; canyon surface water is soft: hence noticeable neighborhood variation along the Wasatch Front"),
        ],
        violations="Wasatch Front systems are consistently compliant. Small desert systems account for arsenic and radionuclide exceedances; the Moab tailings project has removed the great bulk of the state's most-watched legacy risk.",
        faqs=[
            ("Is tap water safe to drink in Utah?", "Yes: Salt Lake City, Provo, and the Wasatch Front districts deliver protected snowmelt meeting every standard. Check small west-desert systems for arsenic notices."),
            ("Why does Salt Lake City water taste so fresh?", "Much of it is that season's snowmelt from protected canyons, in some cases hours-to-days from mountain stream to tap, with watershed rules (no dogs, no swimming) guarding the source."),
            ("Does the shrinking Great Salt Lake affect drinking water?", "Not directly: the lake is terminal and not a drinking source. The concerns are upstream diversions, dust from exposed lakebed, and long-term supply planning for a fast-growing region."),
        ],
        meta_description="Utah tap water: Wasatch canyon snowmelt, desert arsenic pockets, and the Moab cleanup. Look up water quality by ZIP code."),

    dict(slug="vermont", name="Vermont", abbr="VT",
        overview=[
            "Burlington and the Champlain Valley systems treat Lake Champlain water to full compliance, and Vermont's small mountain systems are generally well run under close state oversight.",
            "Vermont's PFAS moment came in Bennington, where decades of Teflon-coating emissions from ChemFab contaminated hundreds of private wells with PFOA, producing a landmark settlement with Saint-Gobain and waterline extensions across the area. Naturally occurring arsenic, radon, and uranium appear in bedrock wells, and blue-green algae blooms on shallow Champlain bays require seasonal vigilance.",
        ],
        n_systems="about 410",
        contaminants=[
            ("PFOA (Bennington plume)", "Air-deposited PFOA contaminated wells across Bennington/North Bennington; settlements funded municipal hookups and long-term monitoring"),
            ("Arsenic and radon in wells", "Bedrock geology yields both in scattered private wells; state testing campaigns target the gap"),
            ("Algal toxins", "Summer blooms on Lake Champlain's shallow bays are monitored by lakeside systems"),
        ],
        violations="Public-system compliance is strong. The Bennington PFOA case, one of New England's defining PFAS battles, was driven by private-well contamination now remedied through waterline extensions.",
        faqs=[
            ("Is tap water safe to drink in Vermont?", "Yes: Burlington and the public systems meet all standards. Private bedrock wells warrant testing for arsenic and radon, and Bennington-area properties are covered by the PFOA response program."),
            ("What happened in Bennington?", "ChemFab's fabric-coating plants emitted PFOA that settled over the area for decades, contaminating private wells: discovered in 2016, it led to Vermont's strict PFAS rules and a Saint-Gobain-funded expansion of municipal water."),
            ("Are Lake Champlain blooms a tap water risk?", "Utilities on vulnerable bays monitor toxins in season and treat accordingly; no Vermont system has had a Toledo-style advisory, and beach closures are the more common bloom impact."),
        ],
        meta_description="Vermont tap water: compliant Champlain systems, Bennington's PFOA settlement, and bedrock well testing. Check your town or ZIP."),

    dict(slug="virginia", name="Virginia", abbr="VA",
        overview=[
            "Northern Virginia's Fairfax Water and the Washington Aqueduct deliver top-tier Potomac and Occoquan supply; Virginia Beach and Norfolk manage sophisticated reservoir networks. Richmond's 2025 treatment-plant failure, which left the capital region under a days-long boil advisory, exposed how much rides on aging plants even in compliant systems.",
            "Occoquan's system is a national landmark in planned water reuse (highly treated wastewater sustains the reservoir), coalfield counties in the southwest wrestle with failing small systems and mining-legacy wells, and kepone's long shadow still keeps James River fish advisories alive without affecting treated drinking water.",
        ],
        n_systems="about 1,100",
        contaminants=[
            ("Lead from plumbing", "Richmond and older Tidewater housing carry legacy lines; utilities run corrosion control and replacement"),
            ("Disinfection byproducts", "Warm reservoir systems manage seasonal THMs; small southwest systems record most exceedances"),
            ("PFAS", "Detections near defense installations (Oceana, Langley area) and scattered industrial sites; treatment planning proceeds under federal limits"),
        ],
        violations="The large systems comply consistently; Richmond's 2025 outage was an infrastructure failure rather than a standards violation and accelerated state scrutiny of plant resilience. Coalfield small systems remain the chronic weak point.",
        faqs=[
            ("Is tap water safe to drink in Virginia?", "Yes: Northern Virginia, Richmond, and Hampton Roads all meet EPA standards. Richmond's 2025 boil advisory stemmed from a plant power failure, since remediated with state-mandated upgrades."),
            ("What happened to Richmond's water in 2025?", "A winter power failure flooded the city's main treatment plant, collapsing pressure across the region and triggering a multi-day boil advisory: a wake-up call about backup power and maintenance that produced state enforcement and investment."),
            ("Is the Occoquan Reservoir really recycled water?", "Partly, by design: an advanced reclamation plant has discharged highly treated water into the reservoir since 1978, one of the nation's oldest indirect potable reuse systems, and Fairfax Water's treatment finishes the job to full standards."),
        ],
        meta_description="Virginia tap water: Fairfax quality, Richmond's 2025 plant failure, Occoquan reuse pioneering, and coalfield gaps. Check your ZIP."),

    dict(slug="washington", name="Washington", abbr="WA",
        overview=[
            "Seattle's Cedar and Tolt watersheds and Tacoma's Green River supply are protected mountain sources delivering some of the country's best big-city water; Spokane pumps the prolific Spokane Valley-Rathdrum Prairie aquifer. All major systems comply fully.",
            "Washington's watchpoints: PFAS plumes on the West Plains around Fairchild AFB and Airway Heights (which flushed its system and drilled new wells), legacy agricultural nitrate in the Lower Yakima Valley affecting private wells, and the enormous but tightly monitored Hanford cleanup, whose groundwater plumes are kept from the Columbia and from drinking supplies.",
        ],
        n_systems="about 2,200",
        contaminants=[
            ("PFAS", "Fairchild AFB-area contamination hit Airway Heights' wells in 2017; state action levels and new federal rules drive testing statewide"),
            ("Nitrate", "Lower Yakima Valley dairy-belt groundwater exceeds limits in many private wells, under a long-running EPA-supervised response"),
            ("Cryptosporidium/turbidity management", "Unfiltered Cedar/Tolt supplies rely on watershed protection, ozone, and UV: monitored intensively"),
        ],
        violations="Metro compliance is excellent, and Seattle holds filtration avoidance for the Cedar supply. Violations concentrate among the state's many small systems; Yakima Valley nitrate is the standing private-well inequity.",
        faqs=[
            ("Is tap water safe to drink in Washington?", "Yes: Seattle, Tacoma, and Spokane deliver protected-source or pristine-aquifer water meeting every standard."),
            ("What happened in Airway Heights?", "Firefighting foam from Fairchild AFB contaminated the city's wells with PFAS in 2017; the city flushed its system, secured replacement supply, and the Air Force funds treatment and monitoring."),
            ("Does Hanford affect drinking water?", "Hanford's radioactive and chemical groundwater plumes are contained and monitored under the nation's largest environmental cleanup; they do not reach public drinking systems, and Richland's Columbia River intake tests clean."),
        ],
        meta_description="Washington State tap water: Seattle's protected watersheds, Spokane's aquifer, Airway Heights PFAS, and Yakima nitrate. Check your ZIP."),

    dict(slug="west-virginia", name="West Virginia", abbr="WV",
        overview=[
            "West Virginia American Water serves Charleston and much of the state from the Elk and Kanawha rivers: the same Elk River where the 2014 Freedom Industries MCHM spill contaminated the supply for 300,000 people, the largest do-not-use order in modern US history and the trigger for federal chemical-storage reforms.",
            "The chemical-industry corridor still shapes risk perception, PFAS from the Parkersburg-area DuPont/Chemours Washington Works plant produced the C8 health studies and the litigation dramatized in 'Dark Waters,' while coalfield counties deal with failing small systems, mine-influenced wells, and some of the nation's oldest infrastructure.",
        ],
        n_systems="about 450",
        contaminants=[
            ("PFAS (C8 legacy)", "The Mid-Ohio Valley's PFOA contamination from Washington Works defined the science and litigation of PFAS nationally; affected systems run carbon treatment"),
            ("Chemical-corridor spill risk", "The 2014 MCHM spill exposed source-water vulnerability; storage-tank laws and intake protections followed"),
            ("Mine-influenced water", "Iron, manganese, sulfates, and occasional metals in coalfield wells and small systems"),
        ],
        violations="The large WVAW systems meet standards; small coalfield systems generate chronic violations and outages, and several have been taken over or regionalized. Infrastructure funding is the state's central water issue.",
        faqs=[
            ("Is tap water safe to drink in West Virginia?", "In the main systems, yes: Charleston's supply meets all standards under post-2014 safeguards. Small coalfield systems are less reliable: follow local advisories."),
            ("What was the Elk River chemical spill?", "In January 2014, MCHM (a coal-washing chemical) leaked from Freedom Industries' tanks just upstream of Charleston's intake, leaving 300,000 people unable to use tap water for days-to-weeks and prompting national storage-tank legislation."),
            ("What is C8?", "PFOA, the Teflon-related chemical DuPont's Washington Works released for decades near Parkersburg: the resulting class-action science panel linked it to six diseases and effectively launched the national PFAS reckoning."),
        ],
        meta_description="West Virginia tap water: the Elk River spill's legacy, C8 and Dark Waters country, and coalfield system struggles. Check your ZIP."),

    dict(slug="wisconsin", name="Wisconsin", abbr="WI",
        overview=[
            "Milwaukee treats Lake Michigan water with ozone and rigorous monitoring, lessons from its 1993 cryptosporidiosis outbreak, the largest waterborne-disease event in US history, and Madison pumps deep, naturally clean aquifer wells. Both comply fully.",
            "Wisconsin's fights are well mapped: lead service lines in Milwaukee and the old industrial cities (a decades-long replacement program), nitrate and bacteria in the karst country of Kewaunee and Door counties where manure reaches wells fast, PFAS in Marinette/Peshtigo (Tyco foam) and La Crosse-area wells, and radium in deep-aquifer systems around Waukesha, which won a precedent-setting Great Lakes diversion to solve it.",
        ],
        n_systems="about 1,050",
        contaminants=[
            ("Nitrate and bacteria in karst wells", "Kewaunee-area fractured bedrock lets manure reach wells rapidly: the state's flagship rural water-justice issue with targeted spreading rules"),
            ("Lead from service lines", "Milwaukee's ~65,000-line inventory anchors a statewide replacement push"),
            ("PFAS", "Marinette/Peshtigo's Tyco foam plume and other sites drove state standards and litigation"),
            ("Radium", "Deep sandstone aquifer systems (Waukesha historically) exceed limits; fixed by treatment or the Lake Michigan diversion"),
        ],
        violations="Milwaukee and Madison hold strong records; violations concentrate in karst-country wells (largely private, outside SDWA), small-system radium, and PFAS-affected wells. Waukesha's 2023 switch to lake water resolved the state's most prominent radium case.",
        faqs=[
            ("Is tap water safe to drink in Wisconsin?", "Yes: Milwaukee, Madison, and the major systems meet all standards, with Milwaukee's post-1993 treatment among the most conservative anywhere. Karst-country private wells need frequent testing."),
            ("What was the 1993 Milwaukee outbreak?", "Cryptosporidium passed through treatment and sickened an estimated 400,000 people: the event that rewrote US surface-water treatment rules and led Milwaukee to add ozone and best-in-class monitoring."),
            ("Why did Waukesha switch to Lake Michigan water?", "Its deep aquifer wells exceeded radium limits; after a first-of-its-kind approval under the Great Lakes Compact, the city began receiving lake water via Milwaukee in 2023, returning treated wastewater to the basin."),
        ],
        meta_description="Wisconsin tap water: Milwaukee's post-1993 rigor, karst nitrate country, Marinette PFAS, and Waukesha's radium fix. Check your ZIP."),

    dict(slug="wyoming", name="Wyoming", abbr="WY",
        overview=[
            "Cheyenne pipes mountain water from the Laramie Range and Colorado's Little Snake headwaters, Casper treats North Platte alluvial wells, and the state's small population rides on generally clean high-plains and mountain sources. Major systems comply fully.",
            "With the nation's smallest population spread across hundreds of tiny systems, Wyoming's issues are scale and geology: naturally occurring uranium, radium, and fluoride in scattered groundwater, legacy uranium-district wells in the Gas Hills and Shirley Basin, and produced-water questions in oil-and-gas country (the Pavillion groundwater investigation remains the reference case).",
        ],
        n_systems="about 250",
        contaminants=[
            ("Uranium and radium", "Natural occurrences plus mining-district legacy affect scattered wells and a few small systems"),
            ("Fluoride", "Naturally high in some basins, occasionally above the secondary standard"),
            ("Oil-and-gas constituents", "The Pavillion investigation examined methane and organics in domestic wells near gas fields; monitoring and cistern programs followed"),
        ],
        violations="Large-system compliance is solid; the state's violation profile is dominated by monitoring lapses and radionuclide exceedances in very small systems, often resolved by new wells or hookups to regional supply.",
        faqs=[
            ("Is tap water safe to drink in Wyoming?", "Yes: Cheyenne, Casper, and the major systems meet all EPA standards, drawing largely clean mountain and alluvial sources."),
            ("What was the Pavillion water investigation?", "EPA and state studies examined whether gas development contaminated domestic wells near Pavillion; findings were contested, some residents received cisterns, and the case remains the touchstone for produced-water debates in the state."),
            ("Should rural Wyoming well owners test for uranium?", "In known uranium districts (Gas Hills, Shirley Basin) and granite-belt areas, yes: naturally occurring radionuclides are the state's most common well-water surprise."),
        ],
        meta_description="Wyoming tap water: clean mountain city supplies, uranium-district wells, and the Pavillion case. Look up your water system by ZIP."),
]
