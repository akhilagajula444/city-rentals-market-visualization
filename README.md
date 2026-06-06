# City Rentals Market Visualization Report

## Project Overview

This project analyzes the New York City Airbnb market using the NYC Airbnb Open Data dataset. The objective is to transform raw listing data into a clear visual narrative that helps property investors understand pricing patterns, listing concentration, competition levels, and potential investment opportunities.

The analysis focuses on identifying:

- Which boroughs have the highest concentration of Airbnb listings
- How prices vary across boroughs and room types
- Which neighborhoods command premium pricing
- Which areas appear oversupplied
- Geographic patterns in listing distribution

---

## Business Problem

A property investment analyst wants to understand the short-term rental market in New York City and identify locations that offer attractive investment opportunities.

The analysis answers the following questions:

1. Which borough contains the highest number of Airbnb listings?
2. How do Airbnb listing prices vary across boroughs?
3. How does room type affect Airbnb pricing?
4. Which neighborhoods have the highest median Airbnb prices?
5. Which neighborhoods have the highest number of Airbnb listings?
6. How do prices vary across boroughs and room types?
7. Where are Airbnb listings geographically concentrated across New York City?

---

## Dataset

**Dataset:** NYC Airbnb Open Data

**Source:** Kaggle

Dataset Link:

https://www.kaggle.com/datasets/dgomonov/new-york-city-airbnb-open-data

The dataset includes:

- Listing Name
- Host Information
- Borough
- Neighborhood
- Room Type
- Price
- Availability
- Latitude
- Longitude

### Dataset Access

The dataset is not included in this repository according to the assessment guidelines.

Download `AB_NYC_2019.csv` and place it inside the `data/` folder before running the notebook.

---

## Technologies Used

- Python 3.10+
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Jupyter Notebook
- Streamlit

---

## Project Structure

```text
city-rentals-market-visualization/
│
├── data/
├── notebooks/
│   └── airbnb_market_analysis.ipynb
├── reports/
│   └── airbnb_market_analysis.html
├── README.md
├── requirements.txt
├── .gitignore
└── app.py
```

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

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Launch Jupyter Notebook

```bash
jupyter notebook
```

Open:

```text
notebooks/airbnb_market_analysis.ipynb
```

Run all cells from top to bottom.

---

## Data Cleaning

The following cleaning steps were performed:

- Removed listings with price = 0 because they represent invalid entries.
- Removed listings with price > 1000 to reduce the influence of extreme luxury properties.
- Created a cleaned dataset for analysis while preserving the original data.

---

## Visualizations Included

- Borough Listing Distribution
- Price Distribution by Borough
- Price Distribution by Room Type
- Top Neighborhoods by Median Price
- Neighborhood Listing Concentration Analysis
- Interactive Plotly Price Comparison
- Geospatial Distribution Map

Each visualization includes a business insight explaining the key takeaway.

---

## Key Decisions

### Why Remove Outliers?

The dataset contained listings priced as high as $10,000. These values significantly distorted the price distribution and made it difficult to analyze the broader Airbnb market.

### Why Use Median Prices?

Median prices are less sensitive to extreme values and better represent the typical listing price within a neighborhood.

### Why Use Boxplots?

Airbnb prices are highly skewed. Boxplots effectively show median values, spread, variability, and outliers.

### Why Include a Geospatial Visualization?

Location is one of the strongest factors affecting Airbnb pricing. Geographic visualizations reveal clustering patterns and location-based pricing trends.

### Why Include an Interactive Plotly Chart?

Interactive charts allow stakeholders to explore pricing relationships more effectively than static visualizations.

---

## Key Findings

- Manhattan contains the highest concentration of Airbnb listings.
- Manhattan generally commands the highest listing prices.
- Entire-home listings achieve significantly higher prices than private or shared rooms.
- A small number of neighborhoods command premium pricing.
- Listing density is concentrated within a limited set of neighborhoods.
- Location is a major factor influencing Airbnb pricing.

---

## Investor Recommendations

1. Focus on neighborhoods that balance strong pricing potential with moderate competition.
2. Entire-home listings may provide stronger revenue opportunities than private or shared accommodations.
3. Evaluate both pricing and competition before investing.
4. Use location-based analysis as a primary factor when identifying investment opportunities.

---

## Limitations

- Historical snapshot only.
- Occupancy and booking information are unavailable.
- Revenue and profitability cannot be calculated directly.
- Seasonal demand patterns are not included.
- Some luxury listings were removed during outlier treatment.

---

## Stretch Goal Implementation

A Streamlit dashboard was developed as an additional enhancement beyond the core project requirements.

### Features

- Borough filtering
- Interactive Plotly visualizations
- Market summary metrics
- Geographic listing exploration

### Run the Dashboard

```bash
streamlit run app.py
```

The dashboard provides an interactive way for users to explore Airbnb market trends across New York City boroughs.

---

## Future Improvements

- Historical trend analysis using multiple Airbnb snapshots.
- Occupancy and booking data integration.
- Revenue estimation models.
- Enhanced Streamlit dashboard with advanced filters.
- Neighborhood-level investment scoring.
- Predictive modeling for Airbnb pricing.

---

## Conclusion

The New York City Airbnb market is dominated by Manhattan and Brooklyn in terms of listing concentration. Manhattan generally commands higher prices, while entire-home listings achieve premium pricing compared with private and shared rooms. Geographic location remains the strongest factor influencing pricing and market activity.

Successful investment decisions should consider pricing potential, competition levels, and neighborhood characteristics rather than focusing solely on listing volume or premium pricing.

