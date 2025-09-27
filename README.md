# 📊 CORD-19 Metadata Analysis & Streamlit Dashboard

**Author:** Charles Kinyua
**Repository:** `_Framework-assignment_`

---

## 🚀 Project Overview

This project analyzes the **CORD-19 `metadata.csv`** dataset, which contains research papers related to COVID-19.
The workflow covers **data loading, cleaning, exploration, visualization, and building an interactive dashboard** using **Streamlit**.

The work is fully implemented, from raw data exploration to a working Streamlit application.

---

## 🎯 Objectives

* Load and explore the dataset using **pandas**
* Handle missing values and prepare clean data for analysis
* Generate insights with **visualizations** (`matplotlib`, `seaborn`, `wordcloud`)
* Build and deploy an interactive **Streamlit web app**
* Demonstrate reproducible workflow using **GitHub**

---

## 📂 Repository Contents

```
_Framework-assignment_/
│
├── analysis_steps.py      # Data cleaning, exploration, and visualization script
├── app.py                 # Streamlit dashboard
├── requirements.txt       # Project dependencies
├── README.md              # Documentation
└── .gitignore             # Excludes metadata.csv, venv, and other unnecessary files
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/ChaoKinyua/_Framework-assignment_.git
cd _Framework-assignment_
```

### 2️⃣ Create and activate a virtual environment

**Windows (PowerShell):**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```


### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Add dataset

Place `metadata.csv` in the root project folder. (Download it from [Kaggle](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge)).

---

## 📊 Analyses Performed

* **Publications over time** → Trend of research growth by year
* **Top journals** → Journals with the highest number of publications
* **Word frequency in titles** → Most common keywords via WordCloud
* **Source distribution** → Breakdown of papers by source

---

## 🖥 Running the Project

### Run data analysis

```bash
python analysis_steps.py
```

### Run Streamlit dashboard

```bash
streamlit run app.py
```

The app will open in your browser (usually at `http://localhost:8501`).

---

## 📈 Visualizations Included

* Line chart: Publications trend over years
* Bar chart: Top publishing journals
* Word cloud: Most frequent title words
* Pie chart: Source distribution

---

## ✅ Evaluation Mapping

* **Implementation (40%)** → Full pipeline from raw CSV → insights → app
* **Code quality (30%)** → Clean, modular, well-commented scripts
* **Visualizations (20%)** → Clear and relevant data plots
* **Streamlit app (10%)** → Functional dashboard with year slider and data preview

---

## 📝 Reflection

Through this project, I:

* Gained hands-on experience working with a **real-world dataset**
* Learned to handle missing and messy data effectively
* Applied the complete **data science workflow** from raw CSV to interactive dashboard
* Built an **intuitive Streamlit app** for exploring COVID-19 research data
* Practiced **version control and collaboration** with Git & GitHub

---

🔥 Project successfully completed and documented.

---

