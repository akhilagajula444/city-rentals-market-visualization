# City Rentals Market Visualization Report

## Project Overview

This project analyzes the New York City Airbnb market using the NYC Airbnb Open Data dataset and transforms raw listing data into a visual investment report.

The goal is to help property investors understand:

- Listing concentration across boroughs
- Pricing patterns by borough and room type
- High-value neighborhoods
- Market competition levels
- Geographic distribution of listings

The final deliverables include:

- Jupyter Notebook analysis
- Professional HTML business report
- Interactive Plotly visualizations
- Interactive geospatial map
- Streamlit dashboard (Stretch Goal)

---

## Business Problem

A property-investment analyst wants to understand the short-term rental market in New York City and identify attractive investment opportunities.

This project answers:

1. Which borough contains the highest number of Airbnb listings?
2. How do Airbnb listing prices vary across boroughs?
3. How does room type affect Airbnb pricing?
4. Which neighborhoods command premium prices?
5. Which neighborhoods have the highest listing concentration?
6. How do prices vary across boroughs and room types?
7. Where are Airbnb listings geographically concentrated?

---

## Dataset

**Dataset:** NYC Airbnb Open Data

**Source:** Kaggle

Dataset Link:

https://www.kaggle.com/datasets/dgomonov/new-york-city-airbnb-open-data

The dataset contains:

- Listing information
- Host information
- Borough and neighborhood
- Room type
- Price
- Availability
- Latitude and longitude

### Dataset Access

The dataset is not committed to the repository.

Download:

```
AB_NYC_2019.csv
```

Place it in:

```
data/
```

before running the project.

---

## Technologies Used

### Core Analysis

- Python 3.10+
- Pandas
- NumPy
- Matplotlib
- Seaborn

### Interactive Visualizations

- Plotly

### Reporting

- HTML
- CSS

### Dashboard

- Streamlit

### Development Environment

- Jupyter Notebook
- Virtual Environment (venv)

---

## Project Structure

```text
city-rentals-market-visualization/

│
├── data/
│
├── images/
│   ├── question1.png
│   ├── question2.png
│   ├── question3.png
│   ├── question4.png
│   └── question5.png
│
├── notebooks/
│   └── airbnb_market_analysis.ipynb
│
├── reports/
│   ├── airbnb_market_analysis.html
│   ├── geospatial_map.html
│   └── price_analysis.html
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Setup Instructions

### Clone Repository

```bash
git clone https://github.com/akhilagajula444/city-rentals-market-visualization.git

cd city-rentals-market-visualization
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Mac/Linux

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Launch Notebook

```bash
jupyter notebook
```

Open:

```text
notebooks/airbnb_market_analysis.ipynb
```

Run all cells.

---

## Data Cleaning

The following preprocessing steps were applied:

### Invalid Prices Removed

Removed listings with:

```text
price = 0
```

These entries represent invalid or incomplete listings.

### Outlier Treatment

Removed listings with:

```text
price > 1000
```

to reduce the impact of extreme luxury properties on the analysis.

### Clean Dataset Creation

A cleaned analytical dataset was created while preserving the original source data.

---

## Visualizations Included

### Question 1

**Listing Distribution by Borough**

**Insight**

Manhattan and Brooklyn contain the highest concentration of Airbnb listings.

---

### Question 2

**Price Distribution by Borough**

**Insight**

Manhattan commands the highest median Airbnb prices.

---

### Question 3

**Price Distribution by Room Type**

**Insight**

Entire-home listings achieve substantially higher prices than private or shared rooms.

---

### Question 4

**Top Neighborhoods by Median Price**

**Insight**

A small number of neighborhoods dominate premium pricing.

---

### Question 5

**Neighborhood Listing Concentration**

**Insight**

Certain neighborhoods show signs of stronger market competition.

---

### Question 6

**Interactive Price Analysis Dashboard**

File:

```text
reports/price_analysis_dashboard.html
```

**Insight**

Pricing varies significantly across both boroughs and room types.

Interactive Plotly visualizations allow stakeholders to explore pricing patterns dynamically.

---

### Question 7

**Interactive Geospatial Analysis**

File:

```text
reports/airbnb_geospatial_analysis.html
```

**Insight**

Listings are heavily concentrated in Manhattan and Brooklyn.

The interactive map reveals geographic pricing clusters and market hotspots.

---

## Professional HTML Report

A business-focused HTML report was developed to communicate findings to non-technical stakeholders.

Report:

```text
reports/Airbnb_Report.html
```

The report includes:

- Executive Summary
- Data Cleaning
- Visual Analysis
- Interactive Visualizations
- Investor Recommendations
- Limitations
- Conclusion

---

## Key Decisions

### Why Remove Outliers?

Some listings exceeded $10,000 per night.

These values distorted price distributions and reduced analytical clarity.

### Why Use Median Prices?

Median values provide a more representative measure of typical Airbnb pricing.

### Why Use Boxplots?

Airbnb prices are heavily skewed.

Boxplots effectively show:

- Median
- Spread
- Variability
- Outliers

### Why Use Interactive Visualizations?

Interactive charts provide deeper exploration capabilities than static charts.

Stakeholders can examine patterns without modifying the code.

### Why Use a Geospatial Visualization?

Location strongly influences Airbnb pricing and demand.

Mapping listings helps identify premium investment zones and market concentration.

---

## Key Findings

- Manhattan contains the largest number of Airbnb listings.
- Manhattan generally commands the highest listing prices.
- Entire-home listings achieve premium pricing.
- Premium pricing is concentrated within a limited set of neighborhoods.
- Competition is concentrated in specific areas.
- Geographic location remains a primary driver of Airbnb pricing.

---

## Investor Recommendations

1. Focus on neighborhoods balancing pricing potential and competition.
2. Prioritize entire-home listings where feasible.
3. Consider both location and competition before investing.
4. Use geographic analysis alongside pricing analysis when evaluating opportunities.

---

## Limitations

- Single historical dataset snapshot
- No occupancy information
- No booking information
- Revenue cannot be calculated directly
- Seasonal effects are not included
- Luxury outliers were intentionally removed

---

## Stretch Goal Implementation

A Streamlit dashboard was developed beyond the project requirements.

### Dashboard Features

- Borough filtering
- Interactive Plotly charts
- Market summary metrics
- Geographic exploration

### Run Dashboard

```bash
streamlit run app.py
```

---

## Future Improvements

- Historical trend analysis
- Occupancy integration
- Revenue forecasting
- Enhanced dashboard filtering
- Neighborhood investment scoring
- Airbnb price prediction models

---

## Conclusion

The New York City Airbnb market is heavily concentrated in Manhattan and Brooklyn. Pricing varies significantly by location and room type, with entire-home listings commanding premium rates. Combining pricing analysis, competition assessment, and geographic insights provides a strong foundation for investment decision-making.

---
