
Netflix Movies and TV Shows Dashboard 


import streamlit as st
import pandas as pd
import plotly.express as px


# App Setup

st.set_page_config(page_title="Netflix Dashboard", page_icon="", layout="wide")
st.title("Netflix Movies and TV Shows Dashboard")
st.markdown("Explore Netflix's catalog using interactive visualizations — by type, year, genre, rating, and more.")

# ----------------------------------------------------------
# Load Dataset
# ----------------------------------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("netflix_titles.csv")

    # Clean the country column
    df['country'] = (
        df['country']
        .fillna('Unknown')
        .astype(str)
        .apply(lambda x: x.split(',')[0].strip())
    )

    df['rating'] = df['rating'].fillna('Not Rated')
    df['duration'] = df['duration'].fillna('Unknown')
    df['release_year'] = df['release_year'].fillna(0).astype(int)
    return df


df = load_data()

# ----------------------------------------------------------
# Sidebar Filters
# ----------------------------------------------------------
st.sidebar.header("Filter Options")

type_filter = st.sidebar.multiselect(
    "Select Type:",
    options=df['type'].dropna().unique(),
    default=df['type'].dropna().unique()
)

country_filter = st.sidebar.multiselect(
    "Select Country:",
    options=sorted(df['country'].dropna().unique().tolist())[:50],
    default=[]
)

rating_filter = st.sidebar.multiselect(
    "Select Rating:",
    options=sorted(df['rating'].dropna().unique().tolist()),
    default=[]
)

# Apply filters
filtered_df = df[df['type'].isin(type_filter)]

if country_filter:
    filtered_df = filtered_df[filtered_df['country'].isin(country_filter)]
if rating_filter:
    filtered_df = filtered_df[filtered_df['rating'].isin(rating_filter)]

st.write(f"### Showing {len(filtered_df)} titles after filtering")

# ----------------------------------------------------------
# Visualization 1: Movies vs TV Shows
# ----------------------------------------------------------
st.subheader("Movies vs TV Shows")

type_count = filtered_df['type'].value_counts().reset_index()
type_count.columns = ['Type', 'Count']

if not type_count.empty:
    fig1 = px.bar(
        type_count,
        x='Type',
        y='Count',
        color='Type',
        text='Count',
        title="Movies vs TV Shows"
    )
    st.plotly_chart(fig1, use_container_width=True, key="type_chart")
else:
    st.warning("⚠️ No data available for the selected filters.")

# ----------------------------------------------------------
# Visualization 2: Content Released Over the Years
# ----------------------------------------------------------
st.subheader("Content Released Over the Years")

year_df = filtered_df['release_year'].value_counts().sort_index().reset_index()
year_df.columns = ['Year', 'Count']

if not year_df.empty:
    fig2 = px.line(
        year_df,
        x='Year',
        y='Count',
        markers=True,
        title="Content Released Per Year"
    )
    st.plotly_chart(fig2, use_container_width=True, key="year_chart")
else:
    st.warning("No data available for the selected filters.")

# ----------------------------------------------------------
# Visualization 3: Top 10 Countries
# ----------------------------------------------------------
st.subheader("Top 10 Countries with Most Content")

country_df = filtered_df['country'].value_counts().head(10).reset_index()
country_df.columns = ['Country', 'Count']

if not country_df.empty:
    fig3 = px.bar(
        country_df,
        x='Count',
        y='Country',
        orientation='h',
        color='Country',
        title="Top 10 Countries by Content"
    )
    st.plotly_chart(fig3, use_container_width=True, key="country_chart")
else:
    st.warning("No data available for the selected filters.")

# ----------------------------------------------------------
# Visualization 4: Ratings Distribution
# ----------------------------------------------------------
st.subheader("Ratings Distribution")

rating_df = filtered_df['rating'].value_counts().reset_index()
rating_df.columns = ['Rating', 'Count']

if not rating_df.empty:
    fig4 = px.pie(
        rating_df,
        names='Rating',
        values='Count',
        title="Ratings Distribution"
    )
    st.plotly_chart(fig4, use_container_width=True, key="rating_chart")
else:
    st.warning("No data available for the selected filters.")

# ----------------------------------------------------------
# Visualization 5: Top 10 Genres / Categories
# ----------------------------------------------------------
st.subheader("Top 10 Genres / Categories")

genres = filtered_df['listed_in'].dropna().str.split(',').explode().str.strip()
top_genres = genres.value_counts().head(10).reset_index()
top_genres.columns = ['Genre', 'Count']

if not top_genres.empty:
    fig5 = px.bar(
        top_genres,
        x='Count',
        y='Genre',
        orientation='h',
        color='Genre',
        title="Top 10 Genres / Categories"
    )
    st.plotly_chart(fig5, use_container_width=True, key="genre_chart")
else:
    st.warning("No data available for the selected filters.")

# ----------------------------------------------------------
# Visualization 6: Top 10 Directors
# ----------------------------------------------------------
st.subheader("Top 10 Directors by Number of Titles")

directors = filtered_df['director'].dropna().value_counts().head(10).reset_index()
directors.columns = ['Director', 'Count']

if not directors.empty:
    fig6 = px.bar(
        directors,
        x='Count',
        y='Director',
        orientation='h',
        color='Director',
        title="Top 10 Directors"
    )
    st.plotly_chart(fig6, use_container_width=True, key="director_chart")
else:
    st.warning("No data available for the selected filters.")

# ----------------------------------------------------------
# Visualization 7: Duration Distribution
# ----------------------------------------------------------
st.subheader("Duration Distribution (Movies / TV Shows)")

duration_df = filtered_df['duration'].dropna().value_counts().head(10).reset_index()
duration_df.columns = ['Duration', 'Count']

if not duration_df.empty:
    fig7 = px.bar(
        duration_df,
        x='Count',
        y='Duration',
        orientation='h',
        color='Duration',
        title="Most Common Durations"
    )
    st.plotly_chart(fig7, use_container_width=True, key="duration_chart")
else:
    st.warning("No data available for the selected filters.")

# ----------------------------------------------------------
# Footer
# ----------------------------------------------------------
st.markdown("---")
st.caption(" Built with using Streamlit & Plotly | Dataset: Netflix Movies and TV Shows (Kaggle)")
