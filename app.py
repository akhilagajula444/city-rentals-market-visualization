import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="NYC Airbnb Dashboard",
    page_icon="🏙️",
    layout="wide"
)

# Load Data
df = pd.read_csv("data/AB_NYC_2019.csv")

# Clean Data
df = df[(df["price"] > 0) & (df["price"] <= 1000)]

# Title
st.title("🏙️ NYC Airbnb Market Dashboard")
st.markdown("Explore Airbnb listings across New York City boroughs.")

# Sidebar Filter
st.sidebar.header("Filters")

borough = st.sidebar.selectbox(
    "Select Borough",
    sorted(df["neighbourhood_group"].unique())
)

filtered_df = df[df["neighbourhood_group"] == borough]

# Metrics
st.subheader(f"{borough} Overview")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Listings",
    f"{len(filtered_df):,}"
)

col2.metric(
    "Average Price",
    f"${filtered_df['price'].mean():.0f}"
)

col3.metric(
    "Median Price",
    f"${filtered_df['price'].median():.0f}"
)

# Price Distribution
st.subheader("Price Distribution")

fig_price = px.histogram(
    filtered_df,
    x="price",
    nbins=40,
    title=f"Price Distribution in {borough}"
)

st.plotly_chart(fig_price, use_container_width=True)

# Room Type Distribution
st.subheader("Room Type Distribution")

room_counts = (
    filtered_df["room_type"]
    .value_counts()
    .reset_index()
)

room_counts.columns = ["Room Type", "Count"]

fig_room = px.bar(
    room_counts,
    x="Room Type",
    y="Count",
    title=f"Room Types in {borough}"
)

st.plotly_chart(fig_room, use_container_width=True)

# Map
st.subheader("Listing Locations")

fig_map = px.scatter_map(
    filtered_df,
    lat="latitude",
    lon="longitude",
    color="price",
    hover_name="name",
    zoom=10,
    height=600
)

st.plotly_chart(fig_map, use_container_width=True)