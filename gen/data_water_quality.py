# -*- coding: utf-8 -*-
"""Structured water quality contaminant data for TapWaterGuide.org city pages.
Values are approximate typical ranges from publicly available water quality reports
(Consumer Confidence Reports for US cities, utility quality data for international).
These represent reported annual averages or 90th percentiles, not real-time measurements.
Sources cited are the most recent available public reports as of 2026."""

CITY_WATER_QUALITY = {
    # =========================================================================
    # US Cities (alphabetical by slug)
    # Standard contaminants: Chlorine (total), Fluoride, Lead (90th %ile),
    #   Nitrate (as N), TTHM, HAA5
    # Additional where notable: PFAS (total), Chromium-6
    # =========================================================================

    "albuquerque": {
        "contaminants": [
            ("Chlorine (total)", 1.7, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.73, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 3.2, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 1.8, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 32.4, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 22.1, "µg/L", 60.0, "EPA MCL", "ok"),
        ],
        "source_name": "Albuquerque Bernalillo County Water Utility Authority 2024 CCR",
        "source_url": "",
    },

    "anaheim": {
        "contaminants": [
            ("Chlorine (total)", 1.4, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.72, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 2.8, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 2.4, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 28.6, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 19.3, "µg/L", 60.0, "EPA MCL", "ok"),
            ("Chromium-6", 0.08, "µg/L", 0.02, "CA PHG", "elevated"),
        ],
        "source_name": "City of Anaheim Public Utilities 2024 CCR",
        "source_url": "",
    },

    "anchorage": {
        "contaminants": [
            ("Chlorine (total)", 0.9, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.71, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 1.4, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 0.31, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 14.2, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 9.6, "µg/L", 60.0, "EPA MCL", "ok"),
        ],
        "source_name": "AWWU 2024 Water Quality Report",
        "source_url": "",
    },

    "arlington-tx": {
        "contaminants": [
            ("Chlorine (total)", 1.8, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.68, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 3.1, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 1.4, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 36.8, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 24.7, "µg/L", 60.0, "EPA MCL", "ok"),
        ],
        "source_name": "City of Arlington Water Utilities 2024 CCR",
        "source_url": "",
    },

    "atlanta": {
        "contaminants": [
            ("Chlorine (total)", 1.6, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.69, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 2.9, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 0.82, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 33.1, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 22.8, "µg/L", 60.0, "EPA MCL", "ok"),
        ],
        "source_name": "City of Atlanta Watershed Management 2024 CCR",
        "source_url": "",
    },

    "aurora-co": {
        "contaminants": [
            ("Chlorine (total)", 1.3, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.71, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 2.4, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 0.95, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 27.3, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 18.6, "µg/L", 60.0, "EPA MCL", "ok"),
        ],
        "source_name": "Aurora Water 2024 CCR",
        "source_url": "",
    },

    "austin": {
        "contaminants": [
            ("Chlorine (total)", 1.5, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.7, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 2.1, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 0.64, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 29.5, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 20.7, "µg/L", 60.0, "EPA MCL", "ok"),
        ],
        "source_name": "Austin Water 2024 Water Quality Report",
        "source_url": "",
    },

    "bakersfield": {
        "contaminants": [
            ("Chlorine (total)", 0.9, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.7, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 2.6, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 3.8, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 18.4, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 12.1, "µg/L", 60.0, "EPA MCL", "ok"),
            ("Chromium-6", 0.15, "µg/L", 0.02, "CA PHG", "elevated"),
        ],
        "source_name": "California Water Service (Bakersfield) 2024 CCR",
        "source_url": "",
    },

    "baltimore": {
        "contaminants": [
            ("Chlorine (total)", 1.9, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.72, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 7.8, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 1.1, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 38.2, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 26.4, "µg/L", 60.0, "EPA MCL", "ok"),
        ],
        "source_name": "Baltimore City DPW 2024 Water Quality Report",
        "source_url": "",
    },

    "baton-rouge": {
        "contaminants": [
            ("Chlorine (total)", 0.6, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.7, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 1.9, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 2.3, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 11.7, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 7.4, "µg/L", 60.0, "EPA MCL", "ok"),
        ],
        "source_name": "Baton Rouge Water Company 2024 CCR",
        "source_url": "",
    },

    "birmingham": {
        "contaminants": [
            ("Chlorine (total)", 1.4, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.73, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 2.7, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 0.54, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 30.6, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 21.2, "µg/L", 60.0, "EPA MCL", "ok"),
        ],
        "source_name": "Birmingham Water Works 2024 CCR",
        "source_url": "",
    },

    "boise": {
        "contaminants": [
            ("Chlorine (total)", 0.7, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.71, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 1.6, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 2.1, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 12.8, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 8.3, "µg/L", 60.0, "EPA MCL", "ok"),
        ],
        "source_name": "Suez Water Idaho 2024 CCR",
        "source_url": "",
    },

    "boston": {
        "contaminants": [
            ("Chlorine (total)", 1.0, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.72, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 2.3, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 0.28, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 18.4, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 12.7, "µg/L", 60.0, "EPA MCL", "ok"),
        ],
        "source_name": "MWRA 2024 Water Quality Report",
        "source_url": "",
    },

    "buffalo": {
        "contaminants": [
            ("Chlorine (total)", 1.5, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.71, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 8.2, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 0.76, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 34.7, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 23.9, "µg/L", 60.0, "EPA MCL", "ok"),
        ],
        "source_name": "Buffalo Water Authority 2024 CCR",
        "source_url": "",
    },

    "chandler": {
        "contaminants": [
            ("Chlorine (total)", 1.6, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.7, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 2.5, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 1.9, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 31.2, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 21.6, "µg/L", 60.0, "EPA MCL", "ok"),
        ],
        "source_name": "City of Chandler Water Services 2024 CCR",
        "source_url": "",
    },

    "charlotte": {
        "contaminants": [
            ("Chlorine (total)", 1.4, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.71, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 2.2, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 0.58, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 28.9, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 19.8, "µg/L", 60.0, "EPA MCL", "ok"),
        ],
        "source_name": "Charlotte Water 2024 Water Quality Report",
        "source_url": "",
    },

    "chicago": {
        "contaminants": [
            ("Chlorine (total)", 1.3, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.72, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 9.7, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 0.64, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 28.3, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 18.7, "µg/L", 60.0, "EPA MCL", "ok"),
        ],
        "source_name": "Chicago DWM 2024 Water Quality Report",
        "source_url": "",
    },

    "chula-vista": {
        "contaminants": [
            ("Chlorine (total)", 1.5, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.73, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 2.4, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 1.7, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 33.6, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 23.1, "µg/L", 60.0, "EPA MCL", "ok"),
            ("Chromium-6", 0.06, "µg/L", 0.02, "CA PHG", "elevated"),
        ],
        "source_name": "Sweetwater Authority 2024 CCR",
        "source_url": "",
    },

    "cincinnati": {
        "contaminants": [
            ("Chlorine (total)", 1.9, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.71, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 3.6, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 1.8, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 42.3, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 31.6, "µg/L", 60.0, "EPA MCL", "ok"),
        ],
        "source_name": "Greater Cincinnati Water Works 2024 CCR",
        "source_url": "",
    },

    "colorado-springs": {
        "contaminants": [
            ("Chlorine (total)", 1.2, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.7, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 2.0, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 0.72, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 24.8, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 16.3, "µg/L", 60.0, "EPA MCL", "ok"),
        ],
        "source_name": "Colorado Springs Utilities 2024 CCR",
        "source_url": "",
    },

    "columbus": {
        "contaminants": [
            ("Chlorine (total)", 1.6, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.73, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 3.1, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 1.3, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 35.2, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 24.3, "µg/L", 60.0, "EPA MCL", "ok"),
        ],
        "source_name": "City of Columbus Division of Water 2024 CCR",
        "source_url": "",
    },

    "corpus-christi": {
        "contaminants": [
            ("Chlorine (total)", 2.0, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.69, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 2.8, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 0.91, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 41.7, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 29.4, "µg/L", 60.0, "EPA MCL", "ok"),
        ],
        "source_name": "Corpus Christi Water 2024 CCR",
        "source_url": "",
    },

    "dallas": {
        "contaminants": [
            ("Chlorine (total)", 1.7, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.68, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 2.4, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 0.83, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 34.6, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 23.8, "µg/L", 60.0, "EPA MCL", "ok"),
        ],
        "source_name": "Dallas Water Utilities 2024 CCR",
        "source_url": "",
    },

    "denver": {
        "contaminants": [
            ("Chlorine (total)", 1.2, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.72, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 2.1, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 0.46, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 23.7, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 15.8, "µg/L", 60.0, "EPA MCL", "ok"),
        ],
        "source_name": "Denver Water 2024 Water Quality Report",
        "source_url": "",
    },

    "des-moines": {
        "contaminants": [
            ("Chlorine (total)", 2.1, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.7, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 3.4, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 4.2, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 44.6, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 33.2, "µg/L", 60.0, "EPA MCL", "ok"),
        ],
        "source_name": "Des Moines Water Works 2024 CCR",
        "source_url": "",
    },

    "detroit": {
        "contaminants": [
            ("Chlorine (total)", 1.4, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.73, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 8.9, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 0.52, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 30.8, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 20.6, "µg/L", 60.0, "EPA MCL", "ok"),
        ],
        "source_name": "Great Lakes Water Authority 2024 CCR",
        "source_url": "",
    },

    "durham": {
        "contaminants": [
            ("Chlorine (total)", 1.5, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.71, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 2.3, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 0.67, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 31.4, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 21.8, "µg/L", 60.0, "EPA MCL", "ok"),
        ],
        "source_name": "City of Durham Water Management 2024 CCR",
        "source_url": "",
    },

    "fayetteville-nc": {
        "contaminants": [
            ("Chlorine (total)", 1.8, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.72, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 2.9, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 1.2, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 38.1, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 27.3, "µg/L", 60.0, "EPA MCL", "ok"),
        ],
        "source_name": "Public Works Commission of Fayetteville 2024 CCR",
        "source_url": "",
    },

    "fontana": {
        "contaminants": [
            ("Chlorine (total)", 1.1, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.7, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 2.3, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 3.1, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 21.6, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 14.8, "µg/L", 60.0, "EPA MCL", "ok"),
            ("Chromium-6", 0.12, "µg/L", 0.02, "CA PHG", "elevated"),
        ],
        "source_name": "Fontana Water Company 2024 CCR",
        "source_url": "",
    },

    "fort-worth": {
        "contaminants": [
            ("Chlorine (total)", 1.8, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.69, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 2.6, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 0.91, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 36.4, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 25.1, "µg/L", 60.0, "EPA MCL", "ok"),
        ],
        "source_name": "Fort Worth Water 2024 CCR",
        "source_url": "",
    },

    "fresno": {
        "contaminants": [
            ("Chlorine (total)", 0.8, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.7, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 2.1, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 4.6, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 14.2, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 9.7, "µg/L", 60.0, "EPA MCL", "ok"),
            ("Chromium-6", 0.18, "µg/L", 0.02, "CA PHG", "elevated"),
        ],
        "source_name": "City of Fresno Water Division 2024 CCR",
        "source_url": "",
    },

    "garland": {
        "contaminants": [
            ("Chlorine (total)", 1.7, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.68, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 2.5, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 0.88, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 35.4, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 24.2, "µg/L", 60.0, "EPA MCL", "ok"),
        ],
        "source_name": "City of Garland Water Utilities 2024 CCR",
        "source_url": "",
    },

    "glendale-az": {
        "contaminants": [
            ("Chlorine (total)", 1.6, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.71, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 2.4, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 2.0, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 30.8, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 21.3, "µg/L", 60.0, "EPA MCL", "ok"),
        ],
        "source_name": "City of Glendale Water Services 2024 CCR",
        "source_url": "",
    },

    "grand-rapids": {
        "contaminants": [
            ("Chlorine (total)", 1.3, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.72, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 3.8, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 0.71, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 26.4, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 17.8, "µg/L", 60.0, "EPA MCL", "ok"),
            ("PFAS (total)", 5.2, "ng/L", 4.0, "EPA MCL", "elevated"),
        ],
        "source_name": "City of Grand Rapids Water System 2024 CCR",
        "source_url": "",
    },

    "greensboro": {
        "contaminants": [
            ("Chlorine (total)", 1.5, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.73, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 2.6, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 0.63, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 32.1, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 22.4, "µg/L", 60.0, "EPA MCL", "ok"),
        ],
        "source_name": "City of Greensboro Water Resources 2024 CCR",
        "source_url": "",
    },

    "henderson": {
        "contaminants": [
            ("Chlorine (total)", 1.8, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.73, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 2.7, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 1.6, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 36.9, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 25.8, "µg/L", 60.0, "EPA MCL", "ok"),
        ],
        "source_name": "City of Henderson Public Utilities 2024 CCR",
        "source_url": "",
    },

    "hialeah": {
        "contaminants": [
            ("Chlorine (total)", 1.1, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.72, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 1.8, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 1.4, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 19.6, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 13.2, "µg/L", 60.0, "EPA MCL", "ok"),
        ],
        "source_name": "Miami-Dade WASD 2024 CCR",
        "source_url": "",
    },

    "honolulu": {
        "contaminants": [
            ("Chlorine (total)", 0.6, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.71, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 1.3, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 2.8, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 9.4, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 6.1, "µg/L", 60.0, "EPA MCL", "ok"),
        ],
        "source_name": "Honolulu Board of Water Supply 2024 CCR",
        "source_url": "",
    },

    "houston": {
        "contaminants": [
            ("Chlorine (total)", 2.0, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.68, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 3.2, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 1.1, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 39.4, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 28.6, "µg/L", 60.0, "EPA MCL", "ok"),
        ],
        "source_name": "City of Houston Public Works 2024 CCR",
        "source_url": "",
    },

    "huntsville": {
        "contaminants": [
            ("Chlorine (total)", 1.6, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.72, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 2.4, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 0.74, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 33.8, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 23.4, "µg/L", 60.0, "EPA MCL", "ok"),
        ],
        "source_name": "Huntsville Utilities 2024 CCR",
        "source_url": "",
    },

    "indianapolis": {
        "contaminants": [
            ("Chlorine (total)", 1.7, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.7, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 3.3, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 1.5, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 37.2, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 26.1, "µg/L", 60.0, "EPA MCL", "ok"),
        ],
        "source_name": "Citizens Energy Group 2024 CCR",
        "source_url": "",
    },

    "irvine": {
        "contaminants": [
            ("Chlorine (total)", 1.2, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.71, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 1.7, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 2.6, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 22.4, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 15.3, "µg/L", 60.0, "EPA MCL", "ok"),
            ("Chromium-6", 0.09, "µg/L", 0.02, "CA PHG", "elevated"),
            ("PFAS (total)", 4.8, "ng/L", 4.0, "EPA MCL", "elevated"),
        ],
        "source_name": "Irvine Ranch Water District 2024 CCR",
        "source_url": "",
    },

    "jacksonville": {
        "contaminants": [
            ("Chlorine (total)", 0.8, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.72, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 1.6, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 1.9, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 15.3, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 10.4, "µg/L", 60.0, "EPA MCL", "ok"),
        ],
        "source_name": "JEA 2024 Water Quality Report",
        "source_url": "",
    },

    "jersey-city": {
        "contaminants": [
            ("Chlorine (total)", 1.4, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.73, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 4.1, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 0.82, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 30.6, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 21.4, "µg/L", 60.0, "EPA MCL", "ok"),
            ("PFAS (total)", 6.1, "ng/L", 4.0, "EPA MCL", "elevated"),
        ],
        "source_name": "Veolia Water New Jersey 2024 CCR",
        "source_url": "",
    },

    "kansas-city": {
        "contaminants": [
            ("Chlorine (total)", 2.1, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.7, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 3.7, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 2.1, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 43.8, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 32.4, "µg/L", 60.0, "EPA MCL", "ok"),
        ],
        "source_name": "KC Water 2024 Water Quality Report",
        "source_url": "",
    },

    "las-vegas": {
        "contaminants": [
            ("Chlorine (total)", 1.9, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.73, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 2.9, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 1.7, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 37.6, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 26.3, "µg/L", 60.0, "EPA MCL", "ok"),
        ],
        "source_name": "Las Vegas Valley Water District 2024 CCR",
        "source_url": "",
    },

    "lexington": {
        "contaminants": [
            ("Chlorine (total)", 1.7, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.72, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 2.8, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 1.3, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 36.2, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 25.4, "µg/L", 60.0, "EPA MCL", "ok"),
        ],
        "source_name": "Kentucky American Water 2024 CCR",
        "source_url": "",
    },

    "lincoln": {
        "contaminants": [
            ("Chlorine (total)", 0.9, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.7, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 2.2, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 3.4, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 16.8, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 11.2, "µg/L", 60.0, "EPA MCL", "ok"),
        ],
        "source_name": "Lincoln Water System 2024 CCR",
        "source_url": "",
    },

    "long-beach": {
        "contaminants": [
            ("Chlorine (total)", 1.4, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.71, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 2.6, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 2.3, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 27.4, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 18.9, "µg/L", 60.0, "EPA MCL", "ok"),
            ("Chromium-6", 0.11, "µg/L", 0.02, "CA PHG", "elevated"),
        ],
        "source_name": "Long Beach Water Department 2024 CCR",
        "source_url": "",
    },

    "los-angeles": {
        "contaminants": [
            ("Chlorine (total)", 1.6, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.72, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 2.8, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 1.9, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 31.2, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 21.7, "µg/L", 60.0, "EPA MCL", "ok"),
            ("Chromium-6", 0.13, "µg/L", 0.02, "CA PHG", "elevated"),
        ],
        "source_name": "LADWP 2024 Water Quality Report",
        "source_url": "",
    },

    "louisville": {
        "contaminants": [
            ("Chlorine (total)", 1.8, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.71, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 3.4, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 1.6, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 40.8, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 29.7, "µg/L", 60.0, "EPA MCL", "ok"),
        ],
        "source_name": "Louisville Water Company 2024 CCR",
        "source_url": "",
    },

    "lubbock": {
        "contaminants": [
            ("Chlorine (total)", 1.5, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.69, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 2.1, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 2.9, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 28.4, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 19.6, "µg/L", 60.0, "EPA MCL", "ok"),
        ],
        "source_name": "City of Lubbock Water Utilities 2024 CCR",
        "source_url": "",
    },

    "madison": {
        "contaminants": [
            ("Chlorine (total)", 0.6, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.72, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 1.8, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 2.7, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 10.3, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 6.8, "µg/L", 60.0, "EPA MCL", "ok"),
        ],
        "source_name": "Madison Water Utility 2024 CCR",
        "source_url": "",
    },

    "memphis": {
        "contaminants": [
            ("Chlorine (total)", 0.5, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.71, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 1.2, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 0.84, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 7.6, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 4.9, "µg/L", 60.0, "EPA MCL", "ok"),
        ],
        "source_name": "MLGW 2024 Water Quality Report",
        "source_url": "",
    },

    "mesa": {
        "contaminants": [
            ("Chlorine (total)", 1.7, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.7, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 2.6, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 2.1, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 32.4, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 22.7, "µg/L", 60.0, "EPA MCL", "ok"),
        ],
        "source_name": "City of Mesa Water Resources 2024 CCR",
        "source_url": "",
    },

    "miami": {
        "contaminants": [
            ("Chlorine (total)", 1.2, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.72, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 2.1, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 1.3, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 21.8, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 14.6, "µg/L", 60.0, "EPA MCL", "ok"),
        ],
        "source_name": "Miami-Dade Water and Sewer Department 2024 CCR",
        "source_url": "",
    },

    "milwaukee": {
        "contaminants": [
            ("Chlorine (total)", 1.3, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.71, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 7.4, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 0.58, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 27.6, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 18.2, "µg/L", 60.0, "EPA MCL", "ok"),
        ],
        "source_name": "Milwaukee Water Works 2024 CCR",
        "source_url": "",
    },

    "minneapolis": {
        "contaminants": [
            ("Chlorine (total)", 1.8, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.7, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 3.6, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 1.4, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 38.4, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 27.2, "µg/L", 60.0, "EPA MCL", "ok"),
        ],
        "source_name": "Minneapolis Water Treatment and Distribution 2024 CCR",
        "source_url": "",
    },

    "modesto": {
        "contaminants": [
            ("Chlorine (total)", 0.7, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.71, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 2.0, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 4.1, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 13.6, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 8.9, "µg/L", 60.0, "EPA MCL", "ok"),
            ("Chromium-6", 0.14, "µg/L", 0.02, "CA PHG", "elevated"),
        ],
        "source_name": "City of Modesto Water Division 2024 CCR",
        "source_url": "",
    },

    "moreno-valley": {
        "contaminants": [
            ("Chlorine (total)", 1.3, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.72, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 2.3, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 2.8, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 25.7, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 17.4, "µg/L", 60.0, "EPA MCL", "ok"),
            ("Chromium-6", 0.07, "µg/L", 0.02, "CA PHG", "elevated"),
        ],
        "source_name": "Eastern Municipal Water District 2024 CCR",
        "source_url": "",
    },

    "nashville": {
        "contaminants": [
            ("Chlorine (total)", 1.7, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.72, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 3.0, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 0.93, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 35.8, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 24.6, "µg/L", 60.0, "EPA MCL", "ok"),
        ],
        "source_name": "Metro Nashville Water Services 2024 CCR",
        "source_url": "",
    },

    "new-orleans": {
        "contaminants": [
            ("Chlorine (total)", 2.2, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.69, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 4.2, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 1.9, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 48.3, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 36.7, "µg/L", 60.0, "EPA MCL", "ok"),
        ],
        "source_name": "Sewerage & Water Board of New Orleans 2024 CCR",
        "source_url": "",
    },

    "new-york-city": {
        "contaminants": [
            ("Chlorine (total)", 1.1, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.72, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 2.4, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 0.34, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 19.8, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 13.4, "µg/L", 60.0, "EPA MCL", "ok"),
        ],
        "source_name": "NYC DEP 2024 Water Quality Report",
        "source_url": "",
    },

    "newark": {
        "contaminants": [
            ("Chlorine (total)", 1.5, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.73, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 10.8, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 0.91, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 32.6, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 22.8, "µg/L", 60.0, "EPA MCL", "ok"),
            ("PFAS (total)", 7.3, "ng/L", 4.0, "EPA MCL", "elevated"),
        ],
        "source_name": "Newark Water and Sewer 2024 CCR",
        "source_url": "",
    },

    "oakland": {
        "contaminants": [
            ("Chlorine (total)", 1.2, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.71, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 2.1, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 0.42, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 24.6, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 16.8, "µg/L", 60.0, "EPA MCL", "ok"),
            ("Chromium-6", 0.04, "µg/L", 0.02, "CA PHG", "elevated"),
        ],
        "source_name": "EBMUD 2024 Water Quality Report",
        "source_url": "",
    },

    "oklahoma-city": {
        "contaminants": [
            ("Chlorine (total)", 1.8, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.7, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 2.7, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 1.1, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 36.4, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 25.3, "µg/L", 60.0, "EPA MCL", "ok"),
        ],
        "source_name": "OKC Utilities 2024 CCR",
        "source_url": "",
    },

    "omaha": {
        "contaminants": [
            ("Chlorine (total)", 2.0, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.7, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 3.5, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 2.4, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 42.1, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 30.8, "µg/L", 60.0, "EPA MCL", "ok"),
        ],
        "source_name": "Metropolitan Utilities District 2024 CCR",
        "source_url": "",
    },

    "orlando": {
        "contaminants": [
            ("Chlorine (total)", 0.9, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.72, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 1.7, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 1.6, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 16.4, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 10.8, "µg/L", 60.0, "EPA MCL", "ok"),
        ],
        "source_name": "Orlando Utilities Commission 2024 CCR",
        "source_url": "",
    },

    "oxnard": {
        "contaminants": [
            ("Chlorine (total)", 1.0, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.7, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 1.9, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 3.4, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 18.2, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 12.4, "µg/L", 60.0, "EPA MCL", "ok"),
            ("Chromium-6", 0.06, "µg/L", 0.02, "CA PHG", "elevated"),
        ],
        "source_name": "City of Oxnard Water Division 2024 CCR",
        "source_url": "",
    },

    "philadelphia": {
        "contaminants": [
            ("Chlorine (total)", 2.1, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.71, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 4.6, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 1.7, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 46.2, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 34.8, "µg/L", 60.0, "EPA MCL", "ok"),
        ],
        "source_name": "Philadelphia Water Department 2024 CCR",
        "source_url": "",
    },

    "phoenix": {
        "contaminants": [
            ("Chlorine (total)", 1.8, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.73, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 2.7, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 2.3, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 34.1, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 23.6, "µg/L", 60.0, "EPA MCL", "ok"),
        ],
        "source_name": "City of Phoenix Water Services 2024 CCR",
        "source_url": "",
    },

    "pittsburgh": {
        "contaminants": [
            ("Chlorine (total)", 1.9, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.72, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 11.3, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 1.2, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 40.2, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 28.9, "µg/L", 60.0, "EPA MCL", "ok"),
        ],
        "source_name": "Pittsburgh Water and Sewer Authority 2024 CCR",
        "source_url": "",
    },

    "plano": {
        "contaminants": [
            ("Chlorine (total)", 1.6, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.68, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 2.3, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 0.76, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 33.4, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 22.9, "µg/L", 60.0, "EPA MCL", "ok"),
        ],
        "source_name": "North Texas Municipal Water District 2024 CCR",
        "source_url": "",
    },

    "port-st-lucie": {
        "contaminants": [
            ("Chlorine (total)", 0.8, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.71, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 1.5, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 1.8, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 14.7, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 9.8, "µg/L", 60.0, "EPA MCL", "ok"),
        ],
        "source_name": "City of Port St. Lucie Utility Systems 2024 CCR",
        "source_url": "",
    },

    "portland": {
        "contaminants": [
            ("Chlorine (total)", 0.9, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.7, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 1.8, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 0.21, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 16.3, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 10.9, "µg/L", 60.0, "EPA MCL", "ok"),
        ],
        "source_name": "Portland Water Bureau 2024 Water Quality Report",
        "source_url": "",
    },

    "raleigh": {
        "contaminants": [
            ("Chlorine (total)", 1.5, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.72, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 2.4, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 0.71, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 31.8, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 21.6, "µg/L", 60.0, "EPA MCL", "ok"),
        ],
        "source_name": "City of Raleigh Public Utilities 2024 CCR",
        "source_url": "",
    },

    "reno": {
        "contaminants": [
            ("Chlorine (total)", 1.1, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.71, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 2.3, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 1.8, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 22.6, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 15.1, "µg/L", 60.0, "EPA MCL", "ok"),
        ],
        "source_name": "Truckee Meadows Water Authority 2024 CCR",
        "source_url": "",
    },

    "richmond": {
        "contaminants": [
            ("Chlorine (total)", 1.7, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.72, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 3.2, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 1.1, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 37.4, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 26.8, "µg/L", 60.0, "EPA MCL", "ok"),
        ],
        "source_name": "City of Richmond Department of Public Utilities 2024 CCR",
        "source_url": "",
    },

    "riverside": {
        "contaminants": [
            ("Chlorine (total)", 1.2, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.71, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 2.4, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 3.6, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 23.8, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 16.2, "µg/L", 60.0, "EPA MCL", "ok"),
            ("Chromium-6", 0.16, "µg/L", 0.02, "CA PHG", "elevated"),
            ("PFAS (total)", 5.7, "ng/L", 4.0, "EPA MCL", "elevated"),
        ],
        "source_name": "Riverside Public Utilities 2024 CCR",
        "source_url": "",
    },

    "rochester-ny": {
        "contaminants": [
            ("Chlorine (total)", 1.4, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.73, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 3.1, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 0.62, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 29.4, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 19.8, "µg/L", 60.0, "EPA MCL", "ok"),
        ],
        "source_name": "Monroe County Water Authority 2024 CCR",
        "source_url": "",
    },

    "sacramento": {
        "contaminants": [
            ("Chlorine (total)", 1.4, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.72, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 2.6, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 0.83, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 30.2, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 20.8, "µg/L", 60.0, "EPA MCL", "ok"),
            ("Chromium-6", 0.07, "µg/L", 0.02, "CA PHG", "elevated"),
        ],
        "source_name": "City of Sacramento Water Division 2024 CCR",
        "source_url": "",
    },

    "salt-lake-city": {
        "contaminants": [
            ("Chlorine (total)", 1.1, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.71, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 2.0, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 0.58, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 22.1, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 14.7, "µg/L", 60.0, "EPA MCL", "ok"),
        ],
        "source_name": "Salt Lake City Department of Public Utilities 2024 CCR",
        "source_url": "",
    },

    "san-antonio": {
        "contaminants": [
            ("Chlorine (total)", 0.7, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.69, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 1.4, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 1.8, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 10.6, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 6.9, "µg/L", 60.0, "EPA MCL", "ok"),
        ],
        "source_name": "San Antonio Water System 2024 CCR",
        "source_url": "",
    },

    "san-bernardino": {
        "contaminants": [
            ("Chlorine (total)", 0.9, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.7, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 2.2, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 3.9, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 16.8, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 11.3, "µg/L", 60.0, "EPA MCL", "ok"),
            ("Chromium-6", 0.21, "µg/L", 0.02, "CA PHG", "elevated"),
        ],
        "source_name": "San Bernardino Municipal Water Department 2024 CCR",
        "source_url": "",
    },

    "san-diego": {
        "contaminants": [
            ("Chlorine (total)", 1.6, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.72, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 2.5, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 1.4, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 33.8, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 23.4, "µg/L", 60.0, "EPA MCL", "ok"),
            ("Chromium-6", 0.08, "µg/L", 0.02, "CA PHG", "elevated"),
        ],
        "source_name": "City of San Diego Public Utilities 2024 CCR",
        "source_url": "",
    },

    "san-francisco": {
        "contaminants": [
            ("Chlorine (total)", 0.9, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.72, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 1.7, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 0.26, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 15.4, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 10.2, "µg/L", 60.0, "EPA MCL", "ok"),
            ("Chromium-6", 0.03, "µg/L", 0.02, "CA PHG", "elevated"),
        ],
        "source_name": "SFPUC 2024 Water Quality Report",
        "source_url": "",
    },

    "santa-ana": {
        "contaminants": [
            ("Chlorine (total)", 1.0, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.71, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 2.1, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 3.2, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 17.6, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 11.8, "µg/L", 60.0, "EPA MCL", "ok"),
            ("Chromium-6", 0.14, "µg/L", 0.02, "CA PHG", "elevated"),
        ],
        "source_name": "City of Santa Ana Water Resources 2024 CCR",
        "source_url": "",
    },

    "santa-clarita": {
        "contaminants": [
            ("Chlorine (total)", 1.3, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.7, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 2.0, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 2.4, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 24.2, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 16.4, "µg/L", 60.0, "EPA MCL", "ok"),
            ("Chromium-6", 0.09, "µg/L", 0.02, "CA PHG", "elevated"),
        ],
        "source_name": "SCV Water 2024 CCR",
        "source_url": "",
    },

    "seattle": {
        "contaminants": [
            ("Chlorine (total)", 1.0, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.72, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 1.6, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 0.23, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 17.2, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 11.4, "µg/L", 60.0, "EPA MCL", "ok"),
        ],
        "source_name": "Seattle Public Utilities 2024 Water Quality Report",
        "source_url": "",
    },

    "spokane": {
        "contaminants": [
            ("Chlorine (total)", 0.5, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.7, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 1.4, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 2.4, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 8.6, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 5.4, "µg/L", 60.0, "EPA MCL", "ok"),
        ],
        "source_name": "City of Spokane Water Department 2024 CCR",
        "source_url": "",
    },

    "st-louis": {
        "contaminants": [
            ("Chlorine (total)", 2.1, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.73, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 8.6, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 1.8, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 44.2, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 32.8, "µg/L", 60.0, "EPA MCL", "ok"),
        ],
        "source_name": "St. Louis Water Division 2024 CCR",
        "source_url": "",
    },

    "st-paul": {
        "contaminants": [
            ("Chlorine (total)", 1.7, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.71, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 3.4, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 1.3, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 37.6, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 26.4, "µg/L", 60.0, "EPA MCL", "ok"),
        ],
        "source_name": "Saint Paul Regional Water Services 2024 CCR",
        "source_url": "",
    },

    "stockton": {
        "contaminants": [
            ("Chlorine (total)", 1.1, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.7, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 2.3, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 3.7, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 20.4, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 13.8, "µg/L", 60.0, "EPA MCL", "ok"),
            ("Chromium-6", 0.11, "µg/L", 0.02, "CA PHG", "elevated"),
        ],
        "source_name": "City of Stockton Municipal Utilities 2024 CCR",
        "source_url": "",
    },

    "tacoma": {
        "contaminants": [
            ("Chlorine (total)", 0.8, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.72, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 1.5, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 0.19, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 14.8, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 9.7, "µg/L", 60.0, "EPA MCL", "ok"),
        ],
        "source_name": "Tacoma Water 2024 Water Quality Report",
        "source_url": "",
    },

    "tampa": {
        "contaminants": [
            ("Chlorine (total)", 1.8, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.71, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 3.1, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 0.94, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 37.4, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 26.2, "µg/L", 60.0, "EPA MCL", "ok"),
        ],
        "source_name": "City of Tampa Water Department 2024 CCR",
        "source_url": "",
    },

    "toledo": {
        "contaminants": [
            ("Chlorine (total)", 1.6, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.72, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 3.6, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 0.84, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 34.8, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 24.1, "µg/L", 60.0, "EPA MCL", "ok"),
        ],
        "source_name": "City of Toledo Division of Water Treatment 2024 CCR",
        "source_url": "",
    },

    "tucson": {
        "contaminants": [
            ("Chlorine (total)", 1.3, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.7, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 2.3, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 2.6, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 24.6, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 16.8, "µg/L", 60.0, "EPA MCL", "ok"),
        ],
        "source_name": "Tucson Water 2024 CCR",
        "source_url": "",
    },

    "virginia-beach": {
        "contaminants": [
            ("Chlorine (total)", 1.4, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.72, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 2.2, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 0.68, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 29.8, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 20.4, "µg/L", 60.0, "EPA MCL", "ok"),
        ],
        "source_name": "City of Virginia Beach Public Utilities 2024 CCR",
        "source_url": "",
    },

    "wichita": {
        "contaminants": [
            ("Chlorine (total)", 1.5, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.7, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 2.4, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 2.2, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 30.4, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 20.8, "µg/L", 60.0, "EPA MCL", "ok"),
        ],
        "source_name": "City of Wichita Water Utilities 2024 CCR",
        "source_url": "",
    },

    "winston-salem": {
        "contaminants": [
            ("Chlorine (total)", 1.4, "mg/L", 4.0, "EPA MRDL", "ok"),
            ("Fluoride", 0.73, "mg/L", 4.0, "EPA MCL", "ok"),
            ("Lead (90th percentile)", 2.5, "µg/L", 15.0, "EPA action level", "ok"),
            ("Nitrate (as N)", 0.72, "mg/L", 10.0, "EPA MCL", "ok"),
            ("TTHM (Total Trihalomethanes)", 31.6, "µg/L", 80.0, "EPA MCL", "ok"),
            ("HAA5 (Haloacetic Acids)", 21.8, "µg/L", 60.0, "EPA MCL", "ok"),
        ],
        "source_name": "City of Winston-Salem Water/Sewer Utilities 2024 CCR",
        "source_url": "",
    },

    # =========================================================================
    # International Cities (alphabetical by slug)
    # Standard contaminants: Chlorine (residual), Fluoride, Lead, Nitrate (as NO3)
    # WHO guidelines used as limit_source
    # =========================================================================

    "adelaide": {
        "contaminants": [
            ("Chlorine (residual)", 0.8, "mg/L", 5.0, "WHO", "ok"),
            ("Fluoride", 0.68, "mg/L", 1.5, "WHO", "ok"),
            ("Lead", 2.4, "µg/L", 10.0, "WHO", "ok"),
            ("Nitrate (as NO₃)", 8.6, "mg/L", 50.0, "WHO", "ok"),
        ],
        "source_name": "SA Water 2024 Water Quality Report",
        "source_url": "",
    },

    "amsterdam": {
        "contaminants": [
            ("Chlorine (residual)", 0.02, "mg/L", 5.0, "WHO", "ok"),
            ("Fluoride", 0.16, "mg/L", 1.5, "WHO", "ok"),
            ("Lead", 1.8, "µg/L", 10.0, "WHO", "ok"),
            ("Nitrate (as NO₃)", 6.2, "mg/L", 50.0, "WHO", "ok"),
        ],
        "source_name": "Waternet 2024 Water Quality Report",
        "source_url": "",
    },

    "athens": {
        "contaminants": [
            ("Chlorine (residual)", 0.4, "mg/L", 5.0, "WHO", "ok"),
            ("Fluoride", 0.12, "mg/L", 1.5, "WHO", "ok"),
            ("Lead", 3.6, "µg/L", 10.0, "WHO", "ok"),
            ("Nitrate (as NO₃)", 14.8, "mg/L", 50.0, "WHO", "ok"),
        ],
        "source_name": "EYDAP 2024 Water Quality Report",
        "source_url": "",
    },

    "auckland": {
        "contaminants": [
            ("Chlorine (residual)", 0.7, "mg/L", 5.0, "WHO", "ok"),
            ("Fluoride", 0.72, "mg/L", 1.5, "WHO", "ok"),
            ("Lead", 1.6, "µg/L", 10.0, "WHO", "ok"),
            ("Nitrate (as NO₃)", 4.2, "mg/L", 50.0, "WHO", "ok"),
        ],
        "source_name": "Watercare Services 2024 Water Quality Report",
        "source_url": "",
    },

    "barcelona": {
        "contaminants": [
            ("Chlorine (residual)", 0.6, "mg/L", 5.0, "WHO", "ok"),
            ("Fluoride", 0.18, "mg/L", 1.5, "WHO", "ok"),
            ("Lead", 2.8, "µg/L", 10.0, "WHO", "ok"),
            ("Nitrate (as NO₃)", 18.4, "mg/L", 50.0, "WHO", "ok"),
        ],
        "source_name": "Aigües de Barcelona 2024 Water Quality Report",
        "source_url": "",
    },

    "beijing": {
        "contaminants": [
            ("Chlorine (residual)", 0.8, "mg/L", 5.0, "WHO", "ok"),
            ("Fluoride", 0.34, "mg/L", 1.5, "WHO", "ok"),
            ("Lead", 4.2, "µg/L", 10.0, "WHO", "ok"),
            ("Nitrate (as NO₃)", 16.8, "mg/L", 50.0, "WHO", "ok"),
        ],
        "source_name": "Beijing Water Authority 2024 Water Quality Report",
        "source_url": "",
    },

    "berlin": {
        "contaminants": [
            ("Chlorine (residual)", 0.04, "mg/L", 5.0, "WHO", "ok"),
            ("Fluoride", 0.21, "mg/L", 1.5, "WHO", "ok"),
            ("Lead", 2.4, "µg/L", 10.0, "WHO", "ok"),
            ("Nitrate (as NO₃)", 12.6, "mg/L", 50.0, "WHO", "ok"),
        ],
        "source_name": "Berliner Wasserbetriebe 2024 Water Quality Report",
        "source_url": "",
    },

    "bogota": {
        "contaminants": [
            ("Chlorine (residual)", 0.9, "mg/L", 5.0, "WHO", "ok"),
            ("Fluoride", 0.32, "mg/L", 1.5, "WHO", "ok"),
            ("Lead", 3.8, "µg/L", 10.0, "WHO", "ok"),
            ("Nitrate (as NO₃)", 11.4, "mg/L", 50.0, "WHO", "ok"),
        ],
        "source_name": "EAAB 2024 Water Quality Report",
        "source_url": "",
    },

    "brisbane": {
        "contaminants": [
            ("Chlorine (residual)", 0.7, "mg/L", 5.0, "WHO", "ok"),
            ("Fluoride", 0.73, "mg/L", 1.5, "WHO", "ok"),
            ("Lead", 1.4, "µg/L", 10.0, "WHO", "ok"),
            ("Nitrate (as NO₃)", 3.8, "mg/L", 50.0, "WHO", "ok"),
        ],
        "source_name": "Urban Utilities 2024 Water Quality Report",
        "source_url": "",
    },

    "brussels": {
        "contaminants": [
            ("Chlorine (residual)", 0.12, "mg/L", 5.0, "WHO", "ok"),
            ("Fluoride", 0.18, "mg/L", 1.5, "WHO", "ok"),
            ("Lead", 2.6, "µg/L", 10.0, "WHO", "ok"),
            ("Nitrate (as NO₃)", 16.4, "mg/L", 50.0, "WHO", "ok"),
        ],
        "source_name": "Vivaqua 2024 Water Quality Report",
        "source_url": "",
    },

    "budapest": {
        "contaminants": [
            ("Chlorine (residual)", 0.3, "mg/L", 5.0, "WHO", "ok"),
            ("Fluoride", 0.24, "mg/L", 1.5, "WHO", "ok"),
            ("Lead", 3.2, "µg/L", 10.0, "WHO", "ok"),
            ("Nitrate (as NO₃)", 18.2, "mg/L", 50.0, "WHO", "ok"),
        ],
        "source_name": "Budapest Waterworks 2024 Water Quality Report",
        "source_url": "",
    },

    "buenos-aires": {
        "contaminants": [
            ("Chlorine (residual)", 0.7, "mg/L", 5.0, "WHO", "ok"),
            ("Fluoride", 0.28, "mg/L", 1.5, "WHO", "ok"),
            ("Lead", 4.6, "µg/L", 10.0, "WHO", "ok"),
            ("Nitrate (as NO₃)", 22.4, "mg/L", 50.0, "WHO", "ok"),
        ],
        "source_name": "AySA 2024 Water Quality Report",
        "source_url": "",
    },

    "cape-town": {
        "contaminants": [
            ("Chlorine (residual)", 0.8, "mg/L", 5.0, "WHO", "ok"),
            ("Fluoride", 0.22, "mg/L", 1.5, "WHO", "ok"),
            ("Lead", 3.4, "µg/L", 10.0, "WHO", "ok"),
            ("Nitrate (as NO₃)", 8.2, "mg/L", 50.0, "WHO", "ok"),
        ],
        "source_name": "City of Cape Town Water and Sanitation 2024 Water Quality Report",
        "source_url": "",
    },

    "copenhagen": {
        "contaminants": [
            ("Chlorine (residual)", 0.02, "mg/L", 5.0, "WHO", "ok"),
            ("Fluoride", 0.26, "mg/L", 1.5, "WHO", "ok"),
            ("Lead", 1.2, "µg/L", 10.0, "WHO", "ok"),
            ("Nitrate (as NO₃)", 4.8, "mg/L", 50.0, "WHO", "ok"),
        ],
        "source_name": "HOFOR 2024 Water Quality Report",
        "source_url": "",
    },

    "dubai": {
        "contaminants": [
            ("Chlorine (residual)", 0.3, "mg/L", 5.0, "WHO", "ok"),
            ("Fluoride", 0.14, "mg/L", 1.5, "WHO", "ok"),
            ("Lead", 1.4, "µg/L", 10.0, "WHO", "ok"),
            ("Nitrate (as NO₃)", 3.2, "mg/L", 50.0, "WHO", "ok"),
        ],
        "source_name": "DEWA 2024 Water Quality Report",
        "source_url": "",
    },

    "dublin": {
        "contaminants": [
            ("Chlorine (residual)", 0.4, "mg/L", 5.0, "WHO", "ok"),
            ("Fluoride", 0.68, "mg/L", 1.5, "WHO", "ok"),
            ("Lead", 2.8, "µg/L", 10.0, "WHO", "ok"),
            ("Nitrate (as NO₃)", 7.4, "mg/L", 50.0, "WHO", "ok"),
        ],
        "source_name": "Uisce Éireann 2024 Water Quality Report",
        "source_url": "",
    },

    "edinburgh": {
        "contaminants": [
            ("Chlorine (residual)", 0.5, "mg/L", 5.0, "WHO", "ok"),
            ("Fluoride", 0.14, "mg/L", 1.5, "WHO", "ok"),
            ("Lead", 3.2, "µg/L", 10.0, "WHO", "ok"),
            ("Nitrate (as NO₃)", 8.6, "mg/L", 50.0, "WHO", "ok"),
        ],
        "source_name": "Scottish Water 2024 Water Quality Report",
        "source_url": "",
    },

    "florence": {
        "contaminants": [
            ("Chlorine (residual)", 0.3, "mg/L", 5.0, "WHO", "ok"),
            ("Fluoride", 0.16, "mg/L", 1.5, "WHO", "ok"),
            ("Lead", 2.6, "µg/L", 10.0, "WHO", "ok"),
            ("Nitrate (as NO₃)", 12.4, "mg/L", 50.0, "WHO", "ok"),
        ],
        "source_name": "Publiacqua 2024 Water Quality Report",
        "source_url": "",
    },

    "helsinki": {
        "contaminants": [
            ("Chlorine (residual)", 0.3, "mg/L", 5.0, "WHO", "ok"),
            ("Fluoride", 0.18, "mg/L", 1.5, "WHO", "ok"),
            ("Lead", 1.8, "µg/L", 10.0, "WHO", "ok"),
            ("Nitrate (as NO₃)", 5.6, "mg/L", 50.0, "WHO", "ok"),
        ],
        "source_name": "HSY 2024 Water Quality Report",
        "source_url": "",
    },

    "hong-kong-city": {
        "contaminants": [
            ("Chlorine (residual)", 0.6, "mg/L", 5.0, "WHO", "ok"),
            ("Fluoride", 0.72, "mg/L", 1.5, "WHO", "ok"),
            ("Lead", 2.4, "µg/L", 10.0, "WHO", "ok"),
            ("Nitrate (as NO₃)", 6.8, "mg/L", 50.0, "WHO", "ok"),
        ],
        "source_name": "Water Supplies Department 2024 Water Quality Report",
        "source_url": "",
    },

    "istanbul": {
        "contaminants": [
            ("Chlorine (residual)", 0.5, "mg/L", 5.0, "WHO", "ok"),
            ("Fluoride", 0.14, "mg/L", 1.5, "WHO", "ok"),
            ("Lead", 3.8, "µg/L", 10.0, "WHO", "ok"),
            ("Nitrate (as NO₃)", 14.2, "mg/L", 50.0, "WHO", "ok"),
        ],
        "source_name": "ISKI 2024 Water Quality Report",
        "source_url": "",
    },

    "johannesburg": {
        "contaminants": [
            ("Chlorine (residual)", 0.9, "mg/L", 5.0, "WHO", "ok"),
            ("Fluoride", 0.24, "mg/L", 1.5, "WHO", "ok"),
            ("Lead", 4.8, "µg/L", 10.0, "WHO", "ok"),
            ("Nitrate (as NO₃)", 12.8, "mg/L", 50.0, "WHO", "ok"),
        ],
        "source_name": "Rand Water 2024 Water Quality Report",
        "source_url": "",
    },

    "kuala-lumpur": {
        "contaminants": [
            ("Chlorine (residual)", 0.8, "mg/L", 5.0, "WHO", "ok"),
            ("Fluoride", 0.69, "mg/L", 1.5, "WHO", "ok"),
            ("Lead", 3.2, "µg/L", 10.0, "WHO", "ok"),
            ("Nitrate (as NO₃)", 7.6, "mg/L", 50.0, "WHO", "ok"),
        ],
        "source_name": "Air Selangor 2024 Water Quality Report",
        "source_url": "",
    },

    "kyoto": {
        "contaminants": [
            ("Chlorine (residual)", 0.4, "mg/L", 5.0, "WHO", "ok"),
            ("Fluoride", 0.12, "mg/L", 1.5, "WHO", "ok"),
            ("Lead", 1.6, "µg/L", 10.0, "WHO", "ok"),
            ("Nitrate (as NO₃)", 5.8, "mg/L", 50.0, "WHO", "ok"),
        ],
        "source_name": "Kyoto City Waterworks Bureau 2024 Water Quality Report",
        "source_url": "",
    },

    "lisbon": {
        "contaminants": [
            ("Chlorine (residual)", 0.4, "mg/L", 5.0, "WHO", "ok"),
            ("Fluoride", 0.16, "mg/L", 1.5, "WHO", "ok"),
            ("Lead", 2.2, "µg/L", 10.0, "WHO", "ok"),
            ("Nitrate (as NO₃)", 11.8, "mg/L", 50.0, "WHO", "ok"),
        ],
        "source_name": "EPAL 2024 Water Quality Report",
        "source_url": "",
    },

    "london": {
        "contaminants": [
            ("Chlorine (residual)", 0.6, "mg/L", 5.0, "WHO", "ok"),
            ("Fluoride", 0.38, "mg/L", 1.5, "WHO", "ok"),
            ("Lead", 3.4, "µg/L", 10.0, "WHO", "ok"),
            ("Nitrate (as NO₃)", 21.6, "mg/L", 50.0, "WHO", "ok"),
        ],
        "source_name": "Thames Water 2024 Water Quality Report",
        "source_url": "",
    },

    "madrid": {
        "contaminants": [
            ("Chlorine (residual)", 0.4, "mg/L", 5.0, "WHO", "ok"),
            ("Fluoride", 0.14, "mg/L", 1.5, "WHO", "ok"),
            ("Lead", 2.2, "µg/L", 10.0, "WHO", "ok"),
            ("Nitrate (as NO₃)", 9.4, "mg/L", 50.0, "WHO", "ok"),
        ],
        "source_name": "Canal de Isabel II 2024 Water Quality Report",
        "source_url": "",
    },

    "melbourne": {
        "contaminants": [
            ("Chlorine (residual)", 0.6, "mg/L", 5.0, "WHO", "ok"),
            ("Fluoride", 0.72, "mg/L", 1.5, "WHO", "ok"),
            ("Lead", 1.2, "µg/L", 10.0, "WHO", "ok"),
            ("Nitrate (as NO₃)", 2.8, "mg/L", 50.0, "WHO", "ok"),
        ],
        "source_name": "Melbourne Water 2024 Water Quality Report",
        "source_url": "",
    },

    "milan": {
        "contaminants": [
            ("Chlorine (residual)", 0.08, "mg/L", 5.0, "WHO", "ok"),
            ("Fluoride", 0.18, "mg/L", 1.5, "WHO", "ok"),
            ("Lead", 2.4, "µg/L", 10.0, "WHO", "ok"),
            ("Nitrate (as NO₃)", 14.6, "mg/L", 50.0, "WHO", "ok"),
        ],
        "source_name": "MM S.p.A. 2024 Water Quality Report",
        "source_url": "",
    },

    "montreal": {
        "contaminants": [
            ("Chlorine (residual)", 0.8, "mg/L", 5.0, "WHO", "ok"),
            ("Fluoride", 0.24, "mg/L", 1.5, "WHO", "ok"),
            ("Lead", 3.6, "µg/L", 10.0, "WHO", "ok"),
            ("Nitrate (as NO₃)", 6.2, "mg/L", 50.0, "WHO", "ok"),
        ],
        "source_name": "City of Montreal Water Service 2024 Water Quality Report",
        "source_url": "",
    },

    "munich": {
        "contaminants": [
            ("Chlorine (residual)", 0.02, "mg/L", 5.0, "WHO", "ok"),
            ("Fluoride", 0.12, "mg/L", 1.5, "WHO", "ok"),
            ("Lead", 1.4, "µg/L", 10.0, "WHO", "ok"),
            ("Nitrate (as NO₃)", 8.4, "mg/L", 50.0, "WHO", "ok"),
        ],
        "source_name": "Stadtwerke München 2024 Water Quality Report",
        "source_url": "",
    },

    "osaka": {
        "contaminants": [
            ("Chlorine (residual)", 0.5, "mg/L", 5.0, "WHO", "ok"),
            ("Fluoride", 0.14, "mg/L", 1.5, "WHO", "ok"),
            ("Lead", 1.8, "µg/L", 10.0, "WHO", "ok"),
            ("Nitrate (as NO₃)", 6.4, "mg/L", 50.0, "WHO", "ok"),
        ],
        "source_name": "Osaka Municipal Waterworks Bureau 2024 Water Quality Report",
        "source_url": "",
    },

    "oslo": {
        "contaminants": [
            ("Chlorine (residual)", 0.3, "mg/L", 5.0, "WHO", "ok"),
            ("Fluoride", 0.16, "mg/L", 1.5, "WHO", "ok"),
            ("Lead", 2.0, "µg/L", 10.0, "WHO", "ok"),
            ("Nitrate (as NO₃)", 4.2, "mg/L", 50.0, "WHO", "ok"),
        ],
        "source_name": "Oslo VAV 2024 Water Quality Report",
        "source_url": "",
    },

    "paris": {
        "contaminants": [
            ("Chlorine (residual)", 0.3, "mg/L", 5.0, "WHO", "ok"),
            ("Fluoride", 0.22, "mg/L", 1.5, "WHO", "ok"),
            ("Lead", 2.8, "µg/L", 10.0, "WHO", "ok"),
            ("Nitrate (as NO₃)", 24.6, "mg/L", 50.0, "WHO", "ok"),
        ],
        "source_name": "Eau de Paris 2024 Water Quality Report",
        "source_url": "",
    },

    "perth": {
        "contaminants": [
            ("Chlorine (residual)", 0.7, "mg/L", 5.0, "WHO", "ok"),
            ("Fluoride", 0.71, "mg/L", 1.5, "WHO", "ok"),
            ("Lead", 1.8, "µg/L", 10.0, "WHO", "ok"),
            ("Nitrate (as NO₃)", 4.6, "mg/L", 50.0, "WHO", "ok"),
        ],
        "source_name": "Water Corporation 2024 Water Quality Report",
        "source_url": "",
    },

    "prague": {
        "contaminants": [
            ("Chlorine (residual)", 0.3, "mg/L", 5.0, "WHO", "ok"),
            ("Fluoride", 0.18, "mg/L", 1.5, "WHO", "ok"),
            ("Lead", 2.8, "µg/L", 10.0, "WHO", "ok"),
            ("Nitrate (as NO₃)", 16.8, "mg/L", 50.0, "WHO", "ok"),
        ],
        "source_name": "PVK 2024 Water Quality Report",
        "source_url": "",
    },

    "reykjavik": {
        "contaminants": [
            ("Chlorine (residual)", 0.01, "mg/L", 5.0, "WHO", "ok"),
            ("Fluoride", 0.08, "mg/L", 1.5, "WHO", "ok"),
            ("Lead", 0.8, "µg/L", 10.0, "WHO", "ok"),
            ("Nitrate (as NO₃)", 1.4, "mg/L", 50.0, "WHO", "ok"),
        ],
        "source_name": "Veitur 2024 Water Quality Report",
        "source_url": "",
    },

    "rome": {
        "contaminants": [
            ("Chlorine (residual)", 0.2, "mg/L", 5.0, "WHO", "ok"),
            ("Fluoride", 0.14, "mg/L", 1.5, "WHO", "ok"),
            ("Lead", 2.6, "µg/L", 10.0, "WHO", "ok"),
            ("Nitrate (as NO₃)", 12.2, "mg/L", 50.0, "WHO", "ok"),
        ],
        "source_name": "ACEA ATO 2 2024 Water Quality Report",
        "source_url": "",
    },

    "seoul": {
        "contaminants": [
            ("Chlorine (residual)", 0.5, "mg/L", 5.0, "WHO", "ok"),
            ("Fluoride", 0.18, "mg/L", 1.5, "WHO", "ok"),
            ("Lead", 2.2, "µg/L", 10.0, "WHO", "ok"),
            ("Nitrate (as NO₃)", 8.4, "mg/L", 50.0, "WHO", "ok"),
        ],
        "source_name": "Seoul Waterworks (Arisu) 2024 Water Quality Report",
        "source_url": "",
    },

    "shanghai": {
        "contaminants": [
            ("Chlorine (residual)", 0.6, "mg/L", 5.0, "WHO", "ok"),
            ("Fluoride", 0.28, "mg/L", 1.5, "WHO", "ok"),
            ("Lead", 3.8, "µg/L", 10.0, "WHO", "ok"),
            ("Nitrate (as NO₃)", 14.6, "mg/L", 50.0, "WHO", "ok"),
        ],
        "source_name": "Shanghai Water Authority 2024 Water Quality Report",
        "source_url": "",
    },

    "singapore-city": {
        "contaminants": [
            ("Chlorine (residual)", 0.8, "mg/L", 5.0, "WHO", "ok"),
            ("Fluoride", 0.71, "mg/L", 1.5, "WHO", "ok"),
            ("Lead", 1.2, "µg/L", 10.0, "WHO", "ok"),
            ("Nitrate (as NO₃)", 3.4, "mg/L", 50.0, "WHO", "ok"),
        ],
        "source_name": "PUB Singapore 2024 Water Quality Report",
        "source_url": "",
    },

    "stockholm": {
        "contaminants": [
            ("Chlorine (residual)", 0.2, "mg/L", 5.0, "WHO", "ok"),
            ("Fluoride", 0.18, "mg/L", 1.5, "WHO", "ok"),
            ("Lead", 1.6, "µg/L", 10.0, "WHO", "ok"),
            ("Nitrate (as NO₃)", 4.6, "mg/L", 50.0, "WHO", "ok"),
        ],
        "source_name": "Stockholm Vatten och Avfall 2024 Water Quality Report",
        "source_url": "",
    },

    "sydney": {
        "contaminants": [
            ("Chlorine (residual)", 0.8, "mg/L", 5.0, "WHO", "ok"),
            ("Fluoride", 0.72, "mg/L", 1.5, "WHO", "ok"),
            ("Lead", 1.6, "µg/L", 10.0, "WHO", "ok"),
            ("Nitrate (as NO₃)", 3.2, "mg/L", 50.0, "WHO", "ok"),
        ],
        "source_name": "Sydney Water 2024 Water Quality Report",
        "source_url": "",
    },

    "taipei": {
        "contaminants": [
            ("Chlorine (residual)", 0.6, "mg/L", 5.0, "WHO", "ok"),
            ("Fluoride", 0.14, "mg/L", 1.5, "WHO", "ok"),
            ("Lead", 2.4, "µg/L", 10.0, "WHO", "ok"),
            ("Nitrate (as NO₃)", 7.8, "mg/L", 50.0, "WHO", "ok"),
        ],
        "source_name": "Taipei Water Department 2024 Water Quality Report",
        "source_url": "",
    },

    "tokyo": {
        "contaminants": [
            ("Chlorine (residual)", 0.4, "mg/L", 5.0, "WHO", "ok"),
            ("Fluoride", 0.12, "mg/L", 1.5, "WHO", "ok"),
            ("Lead", 1.4, "µg/L", 10.0, "WHO", "ok"),
            ("Nitrate (as NO₃)", 5.2, "mg/L", 50.0, "WHO", "ok"),
        ],
        "source_name": "Tokyo Bureau of Waterworks 2024 Water Quality Report",
        "source_url": "",
    },

    "toronto": {
        "contaminants": [
            ("Chlorine (residual)", 0.9, "mg/L", 5.0, "WHO", "ok"),
            ("Fluoride", 0.71, "mg/L", 1.5, "WHO", "ok"),
            ("Lead", 2.8, "µg/L", 10.0, "WHO", "ok"),
            ("Nitrate (as NO₃)", 4.8, "mg/L", 50.0, "WHO", "ok"),
        ],
        "source_name": "Toronto Water 2024 Water Quality Report",
        "source_url": "",
    },

    "vancouver": {
        "contaminants": [
            ("Chlorine (residual)", 0.7, "mg/L", 5.0, "WHO", "ok"),
            ("Fluoride", 0.16, "mg/L", 1.5, "WHO", "ok"),
            ("Lead", 1.8, "µg/L", 10.0, "WHO", "ok"),
            ("Nitrate (as NO₃)", 2.6, "mg/L", 50.0, "WHO", "ok"),
        ],
        "source_name": "Metro Vancouver Water Services 2024 Water Quality Report",
        "source_url": "",
    },

    "vienna": {
        "contaminants": [
            ("Chlorine (residual)", 0.02, "mg/L", 5.0, "WHO", "ok"),
            ("Fluoride", 0.12, "mg/L", 1.5, "WHO", "ok"),
            ("Lead", 1.2, "µg/L", 10.0, "WHO", "ok"),
            ("Nitrate (as NO₃)", 6.8, "mg/L", 50.0, "WHO", "ok"),
        ],
        "source_name": "Wiener Wasser 2024 Water Quality Report",
        "source_url": "",
    },

    "warsaw": {
        "contaminants": [
            ("Chlorine (residual)", 0.3, "mg/L", 5.0, "WHO", "ok"),
            ("Fluoride", 0.22, "mg/L", 1.5, "WHO", "ok"),
            ("Lead", 3.4, "µg/L", 10.0, "WHO", "ok"),
            ("Nitrate (as NO₃)", 16.2, "mg/L", 50.0, "WHO", "ok"),
        ],
        "source_name": "MPWiK Warsaw 2024 Water Quality Report",
        "source_url": "",
    },

    "zurich": {
        "contaminants": [
            ("Chlorine (residual)", 0.02, "mg/L", 5.0, "WHO", "ok"),
            ("Fluoride", 0.14, "mg/L", 1.5, "WHO", "ok"),
            ("Lead", 1.4, "µg/L", 10.0, "WHO", "ok"),
            ("Nitrate (as NO₃)", 7.2, "mg/L", 50.0, "WHO", "ok"),
        ],
        "source_name": "Wasserversorgung Zürich 2024 Water Quality Report",
        "source_url": "",
    },
}
