# COVID-19 Global Data Tracker

## Project Overview

This project is a comprehensive data analysis notebook that tracks global COVID-19 trends using the [Our World in Data COVID-19 dataset](https://ourworldindata.org/covid-cases). The notebook demonstrates data cleaning, exploratory data analysis (EDA), visualization, and insight generation for cases, deaths, and vaccinations across countries and continents.

## Objectives

- Import and clean COVID-19 global data
- Analyze time trends (cases, deaths, vaccinations)
- Compare metrics across countries and continents
- Visualize trends with charts and summary tables
- Communicate findings in a Jupyter Notebook

## Data Source

- [Our World in Data COVID-19 Dataset](https://ourworldindata.org/covid-cases)
- File used: `owid-covid-data.csv`

## Tools Used

- Python (pandas, matplotlib, seaborn)
- Jupyter Notebook (or VS Code with Jupyter extension)

## Project Workflow

1. **Data Loading & Exploration**
   - Load the dataset and display columns, preview data, and check for missing values.

2. **Data Cleaning**
   - Handle missing values by filling with zeros or dropping as appropriate.
   - Filter for countries or continents of interest.
   - Convert date columns to datetime format.

3. **Exploratory Data Analysis (EDA)**
   - Calculate and visualize total cases and deaths by continent.
   - Compute and display case fatality rates (CFR) for countries and continents.
   - Analyze trends in cases and deaths over time for selected countries (e.g., United States, India, Kenya).
   - Generate summary reports and statistics.

4. **Visualization**
   - Bar plots for total cases and deaths by continent.
   - Line plots for total cases and deaths over time by country.
   - Boxplots and other charts for comparing new cases and fatality rates.

5. **Advanced Analysis**
   - Calculate average case fatality rates by continent.
   - Clean and handle infinite or missing values in calculated metrics.
   - Optionally, provide interactive dashboards (e.g., with Streamlit).

6. **Reporting**
   - Print and display summary tables and key findings.
   - Save cleaned and processed datasets for further use.

## How to Run

1. Ensure `owid-covid-data.csv` is in the project directory.
2. Open `JupyterNotebook.ipynb` in VS Code or Jupyter.
3. Run each cell in order to reproduce the analysis and visualizations.
4. Review the outputs, charts, and summary tables.

## Example Insights

- The USA, India, and Kenya show distinct trends in total cases and deaths over time.
- Europe has a notably high average case fatality rate compared to other continents.
- Data cleaning is essential due to missing and infinite values in real-world datasets.
- Visualizations help reveal differences in pandemic impact across regions.

## License

This project is for educational purposes only.