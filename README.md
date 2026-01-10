# 🎬 Netflix Data Analysis & Visualization Dashboard  

Welcome to the **Netflix Data Analysis** project — an insightful data exploration of the popular *Netflix Movies and TV Shows* dataset.  
This project dives into trends, genres, and viewing patterns, and includes an **interactive Streamlit dashboard** for visual exploration.  

---

## 📊 Project Overview  

The goal of this project is to analyze Netflix content to uncover:  
- The balance between **Movies and TV Shows**  
- Most **popular genres and countries**  
- **Content trends** over the years  
- **Ratings distribution** and other insights  

 **Data Analysis**, **Visualization**, and **Streamlit App Development**.  

---

## 🧩 Dataset Description  

**Dataset Name:** [Netflix Movies and TV Shows (Kaggle)](https://www.kaggle.com/datasets/shivamb/netflix-shows)  
**File Used:** `netflix_titles.csv`  

**Key Columns:**  
| Column | Description |
|---------|--------------|
| `show_id` | Unique ID for each show |
| `type` | Movie or TV Show |
| `title` | Name of the title |
| `director` | Director’s name |
| `cast` | Main cast members |
| `country` | Country of production |
| `date_added` | Date added to Netflix |
| `release_year` | Year of release |
| `rating` | Age rating (e.g., PG, TV-MA) |
| `duration` | Duration (in minutes or seasons) |
| `listed_in` | Genre category |
| `description` | Short summary |

---

## 📓 Notebook Analysis  

The **Jupyter Notebook** (`netflix-dataset-analysis-updated.ipynb`) includes:  
- 🔹 Data Cleaning (handling null values, duplicates, etc.)  
- 🔹 Exploratory Data Analysis (EDA)  
- 🔹 Visualizations using **Matplotlib**, **Seaborn**, and **WordCloud**  
- 🔹 Insightful conclusions on Netflix content trends  

---

## 💻 Interactive Dashboard  

The **Streamlit Dashboard** (`app.py`) provides an **interactive way** to explore Netflix data.  
You can filter by **Type**, **Country**, and **Rating**, and view visual insights like:  
- 🎬 Movies vs TV Shows  
- 📆 Content Added Over the Years  
- 🌎 Top Countries with Most Content  
- ⭐ Ratings Distribution  

> 🖼️ **Dashboard Preview:**  
> Check out the `Images` folder in this repository to see screenshots of the dashboard in action.  

Example:  
![Netflix Dashboard](Images/Screenshot%202025-10-27%20115114.png)

---

## ⚙️ Technologies Used  

- 🐍 **Python 3.9+**  
- 📘 **Pandas** – Data manipulation  
- 📊 **Matplotlib / Seaborn** – Data visualization  
- 💡 **Plotly / Streamlit** – Interactive dashboard  
- ☁️ **Jupyter Notebook** – Data exploration  

---

## 🚀 How to Run the Project  

### 1️⃣ Clone the repository  
```bash
git clone https://github.com/your-username/Netflix-Data-Analysis.git
cd Netflix-Data-Analysis


2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run the Streamlit dashboard
streamlit run app.py


Then open the provided local URL (usually http://localhost:8501
) in your browser.

📈 Key Insights

📺 Netflix has more Movies than TV Shows.

🌍 The United States produces the most content.

🕰️ Content production peaked around 2018–2020.

⭐ Ratings such as TV-MA and TV-14 dominate Netflix content.

🎭 The most common genres include Dramas, Comedies, and Documentaries.

📷 Dashboard Screenshots
Movies vs TV Shows	Content by Year

	
Top Countries	Ratings Distribution

	
🏁 Conclusion

This project offers a complete data analysis and visualization pipeline, from data cleaning to dashboard creation.
It’s a great addition to your data science portfolio, showcasing your ability to turn raw data into interactive insights.
