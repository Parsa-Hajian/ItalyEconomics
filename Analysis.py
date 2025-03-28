# ------------------------------------------------------------------------------
# 1. Imports and Setup
# ------------------------------------------------------------------------------
import matplotlib.pyplot as plt

def plot_and_show(title, x, y1, y2=None, labels=('Italy','EU27'), 
                  xlabel='', ylabel='', rotation=0):
    """
    Helper function to plot data. 
    If y2 is provided, it plots a comparison line chart of y1 vs y2.
    """
    plt.figure(figsize=(6,4))
    if y2 is None:
        plt.plot(x, y1, marker='o', label=labels[0])
    else:
        plt.plot(x, y1, marker='o', label=labels[0])
        plt.plot(x, y2, marker='o', label=labels[1])
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=rotation)
    plt.legend()
    plt.tight_layout()
    plt.show()

def bar_and_show(title, x, y1, y2=None, labels=('Italy','EU27'), 
                 xlabel='', ylabel=''):
    """
    Helper function to plot bar charts.
    If y2 is provided, it does a grouped bar chart.
    """
    import numpy as np
    x_idx = np.arange(len(x))
    width = 0.35
    plt.figure(figsize=(7,4))
    if y2 is None:
        bars = plt.bar(x_idx, y1, width, label=labels[0])
        plt.xticks(x_idx, x)
    else:
        bars1 = plt.bar(x_idx - width/2, y1, width, label=labels[0])
        bars2 = plt.bar(x_idx + width/2, y2, width, label=labels[1])
        plt.xticks(x_idx, x)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.tight_layout()
    plt.show()


# ------------------------------------------------------------------------------
# 2. GDP Growth
# ------------------------------------------------------------------------------
def analyze_gdp_growth():
    """
    Compares Italy's real GDP growth with the EU average from 2018 to 2023.
    """
    years = [2018, 2019, 2020, 2021, 2022, 2023]
    italy_gdp = [0.8, 0.3, -9.0, 6.6, 3.7, 0.7]   # Italy real GDP growth (%)
    eu_gdp    = [2.1, 1.9, -5.6, 6.3, 3.5, 0.4]   # EU27 real GDP growth (%)
    
    print("\nGDP Growth Analysis")
    print("==================")
    print("Years:", years)
    print("Italy GDP Growth (%):", italy_gdp)
    print("EU27 GDP Growth (%): ", eu_gdp)
    
    # Plot
    plot_and_show(
        title='Annual GDP Growth Rate',
        x=years,
        y1=italy_gdp,
        y2=eu_gdp,
        labels=('Italy','EU27'),
        xlabel='Year',
        ylabel='Real GDP Growth (%)'
    )
    # Commentary
    print("Commentary: Italy saw a steep decline in 2020 due to the pandemic, rebounded in 2021, "
          "and has since slowed slightly in 2023, remaining comparable to EU averages.")


# ------------------------------------------------------------------------------
# 3. Inflation
# ------------------------------------------------------------------------------
def analyze_inflation():
    """
    Plots Italy's inflation vs the EU's from Jan 2022 to Dec 2023 (approx. HICP).
    """
    months = ["Jan-2022","Apr-2022","Jul-2022","Oct-2022","Jan-2023","Apr-2023","Jul-2023","Oct-2023","Dec-2023"]
    italy_inf = [5.1, 6.3, 8.4, 12.6, 10.7, 8.6, 6.3, 1.8, 0.5]  # Italy HICP YoY
    eu_inf    = [5.7, 8.7, 10.7, 12.3, 10.3, 8.0, 5.7, 3.2, 3.1]  # EU27 HICP YoY
    
    print("\nInflation Analysis")
    print("==================")
    print("Months:", months)
    print("Italy Inflation (%):", italy_inf)
    print("EU27 Inflation (%): ", eu_inf)
    
    plot_and_show(
        title='Inflation Rate (YoY %)',
        x=months,
        y1=italy_inf,
        y2=eu_inf,
        labels=('Italy','EU27'),
        xlabel='Month',
        ylabel='HICP Annual Change (%)',
        rotation=90
    )
    print("Commentary: Italy's inflation peaked around Oct 2022, then fell sharply "
          "into 2023, dipping below the EU average.")


# ------------------------------------------------------------------------------
# 4. Unemployment
# ------------------------------------------------------------------------------
def analyze_unemployment():
    """
    Analyzes Italy's unemployment rate compared to the EU average from 2018 to 2023.
    """
    years = [2018, 2019, 2020, 2021, 2022, 2023]
    italy_unemp = [10.6, 10.0, 9.3, 9.5, 8.2, 7.8]  # Italy unemployment rate (%)
    eu_unemp    = [6.8, 6.7, 7.1, 7.0, 6.2, 6.1]    # EU27 unemployment rate (%)
    
    print("\nUnemployment Analysis")
    print("=====================")
    print("Years:", years)
    print("Italy Unemployment (%):", italy_unemp)
    print("EU27 Unemployment (%): ", eu_unemp)
    
    plot_and_show(
        title='Unemployment Rate (annual average)',
        x=years,
        y1=italy_unemp,
        y2=eu_unemp,
        labels=('Italy','EU27'),
        xlabel='Year',
        ylabel='Unemployment (%)'
    )
    print("Commentary: Italy's unemployment has declined consistently; it's still above "
          "the EU average, but the gap has narrowed recently.")


# ------------------------------------------------------------------------------
# 5. Public Debt
# ------------------------------------------------------------------------------
def analyze_public_debt():
    """
    Analyzes Italy's government debt-to-GDP ratio vs EU average from 2018 to 2023.
    """
    years = [2018, 2019, 2020, 2021, 2022, 2023]
    italy_debt = [134.1, 134.4, 155.3, 150.6, 138.3, 134.8]  # Italy debt (% of GDP)
    eu_debt    = [79.0, 77.5, 90.0, 88.0, 82.5, 80.8]        # EU debt (% of GDP)
    
    print("\nPublic Debt Analysis")
    print("====================")
    print("Years:", years)
    print("Italy Debt-to-GDP (%):", italy_debt)
    print("EU27 Debt-to-GDP (%):  ", eu_debt)
    
    bar_and_show(
        title='Government Debt (% of GDP)',
        x=years,
        y1=italy_debt,
        y2=eu_debt,
        labels=('Italy','EU27'),
        xlabel='Year',
        ylabel='Debt-to-GDP (%)'
    )
    print("Commentary: Italy's debt remains one of the highest in the EU, but "
          "the ratio has inched downward from the pandemic peak.")


# ------------------------------------------------------------------------------
# 6. Foreign Investment
# ------------------------------------------------------------------------------
def analyze_foreign_investment():
    """
    Shows net FDI inflows for Italy from 2019 to 2023 (mock data). 
    """
    import numpy as np
    import matplotlib.pyplot as plt
    
    years = [2019, 2020, 2021, 2022, 2023]
    fdi_flows = [22.7, -18.6, -3.0, 32.2, 18.2]  # Italy net FDI inflows, in USD bn
    
    print("\nForeign Investment (FDI) Analysis")
    print("==================================")
    print("Years:", years)
    print("Italy Net FDI (USD bn):", fdi_flows)
    
    plt.figure(figsize=(6,4))
    bars = plt.bar(years, fdi_flows, 
                   color=['green' if v>=0 else 'red' for v in fdi_flows])
    plt.title('Italy Inward FDI Flows (USD billion)')
    plt.xlabel('Year')
    plt.ylabel('Net Inflows (BoP, USD bn)')
    plt.axhline(0, color='gray', linewidth=0.8)
    
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, 
                 height + (1 if height>=0 else -2.5),
                 f'{height:.1f}', ha='center',
                 va='bottom' if height>=0 else 'top')
    plt.tight_layout()
    plt.show()
    
    print("Commentary: Italy's FDI inflows have been volatile, with a dip in 2020–2021, "
          "a surge in 2022, and a moderation in 2023. Global economic trends and national "
          "policies both play a role.")


# ------------------------------------------------------------------------------
# 7. Industrial Production
# ------------------------------------------------------------------------------
def analyze_industrial_production():
    """
    Compares Italy's industrial production index with the EU from 2018 to 2023.
    """
    years = [2018, 2019, 2020, 2021, 2022, 2023]
    eu_index    = [100.0, 101.0, 93.3, 101.3, 101.7, 100.5]  # EU index (2018=100)
    italy_index = [100.0, 101.0, 89.9, 100.0, 100.4, 98.4]   # Italy index (2018=100)
    
    print("\nIndustrial Production Analysis")
    print("=============================")
    print("Years:", years)
    print("Italy Production Index:", italy_index)
    print("EU27 Production Index: ", eu_index)
    
    plot_and_show(
        title='Industrial Production Index (2018=100)',
        x=years,
        y1=italy_index,
        y2=eu_index,
        labels=('Italy','EU27'),
        xlabel='Year',
        ylabel='Production Volume (index)'
    )
    print("Commentary: Italy saw a deeper drop in 2020 than the EU average, a strong rebound "
          "in 2021, but recent stagnation as energy prices and supply chain issues persist.")


# ------------------------------------------------------------------------------
# 8. Conclusion
# ------------------------------------------------------------------------------
def main():
    print("=====================================================================")
    print("Italy’s Economic Performance under Meloni: A Data-Driven Analysis")
    print("=====================================================================")
    
    analyze_gdp_growth()
    analyze_inflation()
    analyze_unemployment()
    analyze_public_debt()
    analyze_foreign_investment()
    analyze_industrial_production()
    
    print("\n---Conclusion---")
    print("Overall, Italy's economy has shown mostly continuity in its major indicators "
          "under the Meloni government, with improvements in unemployment and inflation, "
          "but ongoing challenges around high public debt and industrial stagnation. "
          "Future trends will require close monitoring, particularly as global headwinds "
          "continue to shape Italy's macroeconomic environment.")

if __name__ == '__main__':
    main()
