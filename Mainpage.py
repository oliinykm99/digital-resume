import streamlit as st
import streamlit_analytics2 as streamlit_analytics
import os
from PIL import Image
from config import * 
from dotenv import load_dotenv

load_dotenv(dotenv_path='.env')
password = os.getenv("password")

streamlit_analytics.start_tracking()
st.set_page_config(page_title=PAGE_TITLE,
                   page_icon=PAGE_ICON,
                   initial_sidebar_state='collapsed')


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.write("📫", EMAIL)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file,
        mime="application/octet-stream",
    )
    


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 2 Years expereince extracting actionable insights from data
- ✔️ Strong hands on experience and knowledge in Python
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: `Python (Scikit-learn, Pandas)`, `SQL`, `MS Excel`
- 📊 Data Visulization: `MS Excel`, `Matplotlib`, `Plotly`
- 📚 Modeling: `Logistic Regression`, `Linear Regression`, `Decision Trees`
- 🗄️ Databases: `GraphQL`, `Db2 SQL`, `MySQL`
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Quantitative Analyst | Pragma**")
st.write("11/2023 - Present")
st.write(
    """
- ► Developed algorithms for data analysis and predictive modeling using statistical methods, reducing analysis time by 30% with high accuracy
- ► Collaborated with 2 cross-functional teams on 3 research initiatives
- ► Communicated findings to stakeholders via comprehensive reports, facilitating informed decision-making
- ► Conducted backtesting, improving trading algorithm performance by 25%
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Data Analyst | Pragma**")
st.write("11/2022 - 11/2023")
st.write(
    """
- ► Participated in writing and reviewing 3 white papers for projects, showcasing the underlying technology and value proposition
- ► Implemented and applied advanced mathematical models and algorithms for decentralized financial operations, resulting in a 10% improvement in financial analysis accuracy
- ► Leveraged a comprehensive computing stack to model, analyze, and validate various financial models and strategies, contributing to data-driven decision-making
- ► Prepared detailed research reports and delivered internal teams and stakeholders, communicating complex findings and actionable insights
- ► Expanded expertise by actively researching emerging blockchain and web3 technologies and integrating new insights into project strategies
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Consulting Intern | Deloitte**")
st.write("06/2019 - 08/2019")
st.write(
    """
- ► Supported the consulting team by conducting over 10 in-depth economic and market quantitative analyses, delivering key insights that informed strategic recommendations and drove impactful business decisions
- ► Prepared comprehensive business analysis reports for senior managers, synthesizing research findings and actionable insights
- ► Streamlined data gathering and analysis processes, reducing report preparation time by 10% through efficient data management techniques
- ► Managed and prioritized multiple high-impact projects, consistently delivering key deliverables ahead of deadlines, leading to a 20% improvement in project efficiency and increased client satisfaction.
"""
)

# --- Licenses & certifications ---
st.write('\n')
st.subheader("Licenses & certifications")
st.write("---")
for (project, link), (key, icon) in zip(CERTIFICATIONS.items(), ICONS.items()):
        st.markdown(f'<img src="{icon}" width="20"/> [{project}]({link})', unsafe_allow_html=True)
streamlit_analytics.stop_tracking(save_to_json='mainpage.json', unsafe_password=password)

# --- Projects ---
st.write('\n')
st.subheader("Projects")
st.write("---")
if st.button("Projects"):
    st.switch_page("pages/Projects.py")