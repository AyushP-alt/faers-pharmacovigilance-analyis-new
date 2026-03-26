# faers-pharmacovigilance-analyis-new
Analysis of FDA FAERS Q4 2025 adverse event reports using Python and pandas
# FDA FAERS Q4 2025 Analysis
This project analyses adverse drug event reports submitted to the FDA 
Adverse Event Reporting System (FAERS) for Q4 2025.

The dataset includes reports from patients, healthcare professionals 
and manufacturers covering drug reactions, outcomes and patient demographics.

Two scripts are included:

faers_analysis.py analyses the complete dataset and identifies the most 
frequently reported drugs and adverse reactions overall in Q4 2025.

faers_outc_analysis.py further analyzes a subset of it, by separating serious 
and non-serious cases using the OUTC outcome codes. Serious cases are 
defined as those flagged with death, hospitalisation, life-threatening, 
disability, congenital anomaly or required intervention codes.

## Scripts
- `faers_analysis.py` — top drugs and reactions across all reports
- `faers_outc_analysis.py` — comparison of serious vs non-serious 
   reaction profiles using outcome codes

## Data
Downloaded from the FDA FAERS public dashboard. Files not included 
due to size — available at https://fis.fda.gov/extensions/FPD-QDE-FAERS/FPD-QDE-FAERS.html

## Requirements
pandas, matplotlib
