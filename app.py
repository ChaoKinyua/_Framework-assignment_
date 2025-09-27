# app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud, STOPWORDS
import os
import re

st.set_page_config(layout='wide', page_title='CORD-19 Explorer')
sns.set(style='whitegrid')

@st.cache_data
def load_data(path='metadata.csv', nrows=None):
    return pd.read_csv(path, low_memory=False, nrows=nrows)

def ensure_dates(df):
    if 'publish_time' in df.columns:
        df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
        df['year'] = df['publish_time'].dt.year
    return df

st.title("CORD-19 Metadata Explorer")
st.markdown("Author: **Charles Kinyua** — simplified assignment version")

uploaded = st.file_uploader("Upload metadata.csv (optional)", type=['csv'])
if uploaded is not None:
    df = load_data(uploaded)
else:
    if os.path.exists('metadata.csv'):
        df = load_data('metadata.csv', nrows=50000)  # limit default for speed
    else:
        st.error("metadata.csv not found. Upload it or place it in the app folder.")
        st.stop()

df = ensure_dates(df)
st.sidebar.header("Filters")

# Year slider
if 'year' in df.columns:
    min_year = int(df['year'].min())
    max_year = int(df['year'].max())
    year_range = st.sidebar.slider("Select year range", min_year, max_year, (min_year, max_year))
    df = df[df['year'].between(year_range[0], year_range[1])]

# Journal filter
journal_col = 'journal' if 'journal' in df.columns else ('journal_title' if 'journal_title' in df.columns else None)
if journal_col:
    top_j = df[journal_col].fillna('Unknown').value_counts().head(50).index.tolist()
    selected_j = st.sidebar.multiselect("Filter by journal (top 50)", ['All'] + top_j, ['All'])
    if selected_j and 'All' not in selected_j:
        df = df[df[journal_col].isin(selected_j)]

# KPIs
c1, c2, c3 = st.columns(3)
c1.metric("Papers", len(df))
c2.metric("Unique Journals", df[journal_col].nunique() if journal_col else 'N/A')
c3.metric("Years", f"{year_range[0]}-{year_range[1]}" if 'year' in df.columns else 'N/A')

st.header("Publications over time")
if 'year' in df.columns:
    counts = df['year'].value_counts().sort_index()
    fig, ax = plt.subplots(figsize=(8,4))
    ax.plot(counts.index, counts.values, marker='o')
    ax.set_xlabel('Year'); ax.set_ylabel('Count'); ax.set_title('Publications by Year')
    st.pyplot(fig)
else:
    st.info("No publish_time/year column available.")

if journal_col:
    st.header("Top Journals")
    top = df[journal_col].fillna('Unknown').value_counts().head(20)
    fig2, ax2 = plt.subplots(figsize=(8,6))
    sns.barplot(x=top.values, y=top.index, ax=ax2)
    ax2.set_xlabel('Count'); ax2.set_ylabel('Journal')
    st.pyplot(fig2)

st.header("Word Cloud (titles)")
titles_text = ' '.join(df['title'].fillna('').astype(str).values).lower()
stop = set(STOPWORDS)
try:
    import nltk
    from nltk.corpus import stopwords
    stop = stop.union(set(stopwords.words('english')))
except Exception:
    pass

wc = WordCloud(width=900, height=400, background_color='white', stopwords=stop, max_words=200).generate(titles_text)
fig3, ax3 = plt.subplots(figsize=(12,6))
ax3.imshow(wc, interpolation='bilinear'); ax3.axis('off')
st.pyplot(fig3)

st.header("Sample data")
st.dataframe(df.head(200))
