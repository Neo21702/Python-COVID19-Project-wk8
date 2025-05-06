# COVID-19 Global Data Tracker

## Project Overview

This project is a Jupyter Notebook that analyzes and visualizes global COVID-19 trends using the [Our World in Data COVID-19 dataset](https://ourworldindata.org/covid-cases). The notebook demonstrates data loading, cleaning, exploratory data analysis (EDA), and visualization for cases, deaths, and vaccinations across selected countries.

## Objectives

- Import and clean COVID-19 global data
- Analyze time trends (cases, deaths, vaccinations)
- Compare metrics across countries/regions
- Visualize trends with charts and summary tables
- Communicate findings in a Jupyter Notebook

## Data Source

- [Our World in Data COVID-19 Dataset](https://ourworldindata.org/covid-cases)
- File used: `owid-covid-data.csv`

## Tools Used

- Python (pandas, matplotlib, seaborn, plotly)
- Jupyter Notebook (or VS Code with Jupyter extension)

## Project Workflow

1. **Data Loading & Exploration**
   - Load the dataset, display columns, preview data, and check for missing values.

2. **Data Cleaning**
   - Filter for countries of interest (e.g., Kenya, USA, India)
   - Drop rows with missing critical values
   - Convert date columns to datetime format
   - Fill or interpolate missing numeric values

3. **Exploratory Data Analysis (EDA)**
   - Plot total cases and deaths over time for selected countries
   - Compare daily new cases between countries
   - Calculate and visualize death rates

4. **Vaccination Analysis**
   - Plot cumulative vaccinations over time
   - Compare percentage of population vaccinated

5. **(Optional) Choropleth Map**
   - Visualize global case density or vaccination rates on a world map

6. **Insights & Reporting**
   - Summarize key findings and patterns using Markdown cells

## How to Run

1. Place `owid-covid-data.csv` in the project directory.
2. Open `JupyterNotebook.ipynb` in VS Code or Jupyter.
3. Run each cell in order to reproduce the analysis and visualizations.
4. Review the outputs, charts, and summary tables.

## Example Insights

- The USA had the highest total cases and deaths among the selected countries.
- India experienced a sharp rise in cases during mid-2021.
- Kenya's vaccination rollout lagged behind the USA and India.
- Death rates were highest in the early stages of the pandemic for all countries.
- Vaccination rates increased significantly in the USA compared to Kenya and India.

## License

This project is for educational purposes only.