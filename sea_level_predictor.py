# sea_level_predictor.py

import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# 1. Import the data
df = pd.read_csv('epa-sea-level.csv')

# 2. Create the scatter plot
def draw_plot():
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='b', label='Original Data')

    # 3. Create first line of best fit using the entire dataset
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = pd.Series(range(1880, 2051))  # Extend years to 2050
    sea_level_pred = res.intercept + res.slope * years_extended
    ax.plot(years_extended, sea_level_pred, 'r', label='Best Fit Line (1880-2050)')

    # 4. Create second line of best fit using data from year 2000 onward
    df_recent = df[df['Year'] >= 2000]
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent = pd.Series(range(2000, 2051))  # Extend years to 2050
    sea_level_pred_recent = res_recent.intercept + res_recent.slope * years_recent
    ax.plot(years_recent, sea_level_pred_recent, 'g', label='Best Fit Line (2000-2050)')

    # 5. Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    ax.legend()

    # 6. Save and return the plot
    fig.savefig('sea_level_plot.png')
    return fig
