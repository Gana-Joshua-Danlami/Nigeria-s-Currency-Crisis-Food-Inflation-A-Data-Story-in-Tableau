import streamlit as st
import pandas as pd
import altair as alt

# --- Page Config ---
st.set_page_config(page_title="🇳🇬 Nigeria's Food Inflation Crisis", layout="wide")

# --- Load Data ---
@st.cache_data
def load_data():
   df = pd.read_csv("combined_food_inflation_csv.csv", parse_dates=["Date"])
    return df

df = load_data()

# --- Sidebar Filters ---
st.sidebar.header("🔎 Filter")
df["Year"] = df["Year"].astype("Int64")
years = df["Year"].dropna().astype(int).unique()
years = sorted(years)
selected_years = st.sidebar.multiselect("Select Year(s)", years, default=years)

filtered_df = df[df["Year"].isin(selected_years)]

# --- Title & Description ---
st.title("🇳🇬 Nigeria's Currency Crisis & Food Inflation")
st.markdown("### An Interactive Data Story")

# --- Line Chart ---
st.subheader("📈 Food Inflation vs Exchange Rate (₦/USD)")

melted = pd.melt(
    filtered_df,
    id_vars=["Date"],
    value_vars=["Food_Inflation (%)", "Exchange_Rate (₦/USD)"],
    var_name="Indicator",
    value_name="Value"
)

line_chart = alt.Chart(melted).mark_line().encode(
    x="Date:T",
    y="Value:Q",
    color="Indicator:N",
    tooltip=["Date:T", "Indicator:N", "Value:Q"]
).properties(
    width=900,
    height=400
).interactive()

st.altair_chart(line_chart)

# --- Highlight Key Events ---
st.subheader("📌 Economic Events")
events = filtered_df[filtered_df["Comment"].notna() & (filtered_df["Comment"].str.strip() != "")]
if not events.empty:
    st.write("Here are significant notes from key months in the data:")
    for _, row in events.iterrows():
        st.markdown(f"- **{row['Date'].strftime('%b %Y')}**: {row['Comment']}")
else:
    st.write("No key economic events for the selected years.")

# --- Data Preview & Statistics ---
st.subheader("🔍 Data Preview & Statistics")
st.write(df[["Date", "Food_Inflation (%)"]].head(20))
st.write(df["Food_Inflation (%)"].describe())
