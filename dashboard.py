import streamlit as st
import pandas as pd

# Load data set -----
@st.cache_data
def load_data(path: str):
    data = pd.read_excel(path)
    return data
df = load_data('feedbackInfoSessionClean.xlsx')

# Page config
st.set_page_config(layout="wide")

# Title
st.title("Info Session Dashboard")

# Layout
choose, mOne, mTwo = st.columns(3, border=True)
keyw, skill, conclusion = st.columns(3, border=True)

# Select Box
option_course = choose.selectbox(
    'Pilih Bidang',
    df['Which area are you MOST interested in exploring within GDG On Campus?'].unique()
)

# Keyword Insight -----
keyword = [
    {
        "course": "Web Development",
        "keywords": ["UI/UX", "Frontend", "Backend", "Database", "Deployment & Hosting", "Full-Stack Development"],
        "conclusion": f"""
        Banyak member yang tertarik pada skill technical mengenai cara pembuatan web baik dari sisi Front End, Back End, dan Deployment. 
        Pada sisi Back End terdapat beberapa member yang ingin tahu beberapa hal seperti mengelola server, database, dan logika dibalik website dan dari sisi Front End 
        banyak keyword yang menyangkut pada tampilan atau UI/UX.
        """,
    },
    {
        "course": "Machine Learning",
        "keywords": ["AI (Artificial Intelligence)", "ML (Machine Learning)", "DL (Deep Learning)", "NLP (Natural Language Processing)", "LLM (Large Language Model)", "Ai Agents", "Data Analyst"],
        "conclusion": f"""
        Dari keyword yang muncul, minat member yang memilih Machine Learning memiliki semangat untuk belajar yang sangat tinggi ke arah fundamental dan teknikalnya

        """
    },
    {
        "course": "Product Management",
        "keywords": ["Product Management / PM Skills", "Manage Product", "Attract People", "Lead Skill"],
        "conclusion": f"""
        Keyword yang muncul dari member yang memilih PM tidak hanya ke arah ke hal yang bersifat fundamental dari PM itu sendiri, tetapi juga ke arah soft skill yang diperlukan sebagai seorang PM
        """
    },
    {
        "course": "UI/UX",
        "keywords": ["UI/UX", "Design/Desain", "Membuat Desain"],
        "conclusion": f"""
        Member ingin memahami mengenai proses mendesain secara menyeluruh dan dasar-dasar dari UI/UX dari nol dan memperdalamnya. Selain itu member juga ingin menguasai beberapa tools yang digunakan dalam pembuatan UI/UX
        """
    },
    {
        "course": "Mobile Development",
        "keywords": ["Mobile Development", "App Development", "APK Development", "React Native", "API Implementation", "ML Algorithm Integration", "Data Management", "Debuggin", "Backend in Mobile Development"],
        "conclusion": f"""
        Keyword yang muncul cukup bervariasi tidak hanya spesifik pada mobil dev tetapi juga muncul keyword yang sifatnya meluas seperti ML Integration, Caching, React Native, bahkan sampai Game Development
        """
    },
]

filtered_data_course = df[df['Which area are you MOST interested in exploring within GDG On Campus?'] == option_course] 

for key in keyword:
    if key["course"] == option_course:
        keyword_list = key["keywords"]
        break

with keyw.container():
    st.subheader("Keywords Insight")
    markdown_output = ""
    for kw in keyword_list:
        markdown_output += f"* {kw}\n"

    st.markdown(markdown_output)

# Display Banyak Memilih -----
count_data_first = df[df['Which area are you MOST interested in exploring within GDG On Campus?'] == option_course]['Which area are you MOST interested in exploring within GDG On Campus?'].count()
count_data_sec = df[df['Which area are you second MOST interested in exploring within GDG On Campus?'] == option_course]['Which area are you second MOST interested in exploring within GDG On Campus?'].count()

mOne.metric(
    label="Banyak memilih di bidang pertama",
    value=count_data_first,
    # border=True
)
mTwo.metric(
    label="Banyak memilih di bidang kedua",
    value=count_data_sec,
    # border=True
)

# Display Skill User -----
filtered_data_skill = df[df['Which area are you MOST interested in exploring within GDG On Campus?'] == option_course]['Rate your current skill level in your chosen field.'].value_counts().reset_index()
filtered_data_skill.columns = ['Skill Level', 'Count']

with skill.container():
    st.subheader(f"Member Skill Level at {option_course}")
    st.text("1 = Beginner, 5 = Expert")
    st.bar_chart(filtered_data_skill, x='Skill Level', y='Count')

with conclusion.container():
    st.subheader(f"Conclusion for {option_course}")
    for key in keyword:
        if key["course"] == option_course:
            st.text(key["conclusion"])