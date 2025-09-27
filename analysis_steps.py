# Part 1: Load & basic exploration
import pandas as pd
pd.options.display.max_columns = 80
pd.options.display.max_colwidth = 300

CSV = 'metadata.csv'   # ensure file is in project folder

# If the file is very large use nrows to test:
# df = pd.read_csv(CSV, nrows=10000, low_memory=False)
df = pd.read_csv(CSV, low_memory=False)

print("Loaded:", CSV)
print("Shape:", df.shape)
display(df.head(5))
print("\nDtypes:\n", df.dtypes)
print("\nMissing values (top 40):")
print(df.isnull().sum().sort_values(ascending=False).head(40))

# Part 2: cleaning & preparation
import numpy as np

# Convert publish_time to datetime safely
if 'publish_time' in df.columns:
    df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
    df['year'] = df['publish_time'].dt.year

# Ensure title & abstract are strings and compute word counts
df['title'] = df['title'].fillna('').astype(str)
df['abstract'] = df.get('abstract', '').fillna('').astype(str)  # use get to avoid keyerror
df['title_word_count'] = df['title'].str.split().apply(len)
df['abstract_word_count'] = df['abstract'].str.split().apply(len)

# Columns with high missingness
missing_pct = (df.isnull().sum() / len(df)).sort_values(ascending=False)
display(missing_pct.head(50))

# Rule example: drop columns with > 80% missing (optional)
cols_to_consider_drop = missing_pct[missing_pct > 0.8].index.tolist()
print("Columns with >80% missing:", cols_to_consider_drop)

# Create cleaned copy: drop rows that lack both title and abstract
cleaned = df[~((df['title'].str.strip()=='') & (df['abstract'].str.strip()==''))].reset_index(drop=True)
print("Cleaned shape:", cleaned.shape)

import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
from wordcloud import WordCloud, STOPWORDS
import re
from nltk.corpus import stopwords

sns.set(style='whitegrid', context='talk')

# Publications by year
if 'year' in cleaned.columns:
    counts = cleaned['year'].dropna().astype(int).value_counts().sort_index()
    plt.figure(figsize=(10,5))
    plt.plot(counts.index, counts.values, marker='o')
    plt.title('Publications by Year')
    plt.xlabel('Year'); plt.ylabel('Number of Papers')
    plt.show()

# Top journals
journal_col = None
for c in ['journal', 'journal_title', 'venue']:
    if c in cleaned.columns:
        journal_col = c
        break

if journal_col:
    top = cleaned[journal_col].fillna('Unknown').value_counts().head(20)
    plt.figure(figsize=(10,8))
    sns.barplot(x=top.values, y=top.index)
    plt.title('Top 20 Journals by Paper Count')
    plt.xlabel('Count')
    plt.tight_layout()
    plt.show()

# Frequent words in titles (simple)
titles_text = ' '.join(cleaned['title'].astype(str).values).lower()
words = re.findall(r'\b[a-z]{3,}\b', titles_text)
stop = set(stopwords.words('english'))
words = [w for w in words if w not in stop]
freq = Counter(words)
print("Top 30 title words:", freq.most_common(30))

# Wordcloud
wc_stop = set(STOPWORDS).union(stop)
wc = WordCloud(width=1200, height=600, stopwords=wc_stop, background_color='white', max_words=200).generate(titles_text)
plt.figure(figsize=(14,7))
plt.imshow(wc, interpolation='bilinear'); plt.axis('off'); plt.show()

# Distribution by source
source_col = None
for c in ['source_x','source','corpus']:
    if c in cleaned.columns:
        source_col = c
        break
if source_col:
    s = cleaned[source_col].fillna('Unknown').value_counts().head(15)
    plt.figure(figsize=(10,6))
    sns.barplot(x=s.values, y=s.index)
    plt.title('Top Sources / Corpora')
    plt.xlabel('Count')
    plt.tight_layout(); plt.show()

