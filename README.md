# Italy's Economic Performance under Giorgia Meloni – Project Overview

## Project Description
This project examines how Italy's current government, led by Giorgia Meloni (since October 2022), has influenced or coincided with changes in several key economic indicators. It compares Italy's performance to previous Italian governments and to EU averages.

We rely on Eurostat (and supporting sources like UNCTAD or ISTAT) for data on:
- GDP Growth
- Inflation
- Unemployment
- Public Debt
- Foreign Direct Investment (FDI)
- Industrial Production

The `analysis.py` script merges and analyzes these datasets, producing summary tables, commentary, and plots. The textual analysis (like an article) is printed to the console and embedded in docstrings.

---

## File Structure

- **analysis.py**  
  Main analysis script containing:
  - Data loading from CSV files
  - Merging and cleaning
  - Plotting
  - Commentary and final conclusions in docstrings/print statements

- **data_sources.txt**  
  Provides relevant Eurostat (and other) URLs for each indicator.

- **README.md**  
  This file. Overview of the project, data fetching steps, and instructions to reproduce the analysis.

---

## Data Extraction Steps

1. **Identify Data from Eurostat**  
   - Visit [Eurostat Data Browser](https://ec.europa.eu/eurostat/databrowser/) or the direct links in `data_sources.txt`.
   - Search the relevant table codes:
     - GDP: `nama_10_gdp`
     - Inflation (HICP): `prc_hicp_midx`
     - Unemployment: `une_rt_m`
     - Public Debt: `gov_10dd_edpt1`
     - FDI: `bop_fdi_main` (or UNCTAD data)
     - Industrial Production: `sts_inpr_a`
   - Filter by country (Italy, EU27, or others if needed), select the desired time periods (e.g., 2018–2023).

2. **Download/Export to CSV**  
   - In the Eurostat interface, once you have the data displayed, choose “Export” → “CSV”.
   - Save files in the same directory as `analysis.py`, naming them consistently with the code (e.g., `gdp_italy.csv`).

3. **Check & Clean the Data**  
   - Verify that the CSV columns match what the script expects. For example:
     - `gdp_italy.csv` should have columns `[Year, Italy_GDP_growth]`.
   - Adjust column headers or data format if needed. For instance, you might have GDP levels that you convert to growth rates.

4. **Run the Analysis Script**  
   - Install dependencies: `pip install pandas matplotlib`
   - Run: `python analysis.py`
   - The script prints commentary and displays the plots in a window (or inline if using a Jupyter notebook).

5. **Interpret & Refine**  
   - The script prints an article-like narrative. Customize the text, commentary, or data processing steps as you refine your analysis.
   - Update placeholders with real numbers or more precise calculations as needed.

---

## How to Reproduce / Extend

- **Additional Years or Indicators**: You can add more years or new columns (e.g., quarterly data, monthly data) to the CSVs and update the script to reflect new columns or date/time formats.
- **Comparisons**: If you want to compare Italy to more countries (France, Germany, etc.), replicate the approach by adding new CSV files (e.g., `gdp_france.csv`) and merging them similarly.
- **Automation**: You can add Python code using [requests](https://docs.python-requests.org/en/master/) or [pandas’ read_csv with a URL](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html) to automate data fetching. Just ensure the Eurostat link yields a direct CSV export.

---

## Project Status
- This repo is in a demonstration phase. The numeric data in the CSV files may be sample placeholders. You are encouraged to update them with the most recent and accurate data from Eurostat or other official sources.

## License
- You are free to use or modify this code. Bear in mind that Eurostat data usage falls under [Eurostat’s reuse policy](https://ec.europa.eu/eurostat/about/policies/copyright). Check official terms if in doubt.
