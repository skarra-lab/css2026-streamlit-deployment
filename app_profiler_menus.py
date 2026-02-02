import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

# Set page title
st.set_page_config(page_title="Sikhangele Nogcinisa Data Science Projects", layout="wide")

# Sidebar Menu
st.sidebar.title("Navigation")
menu = st.sidebar.radio(
    "Find:",
    ["Profile", "Publications", "Data Science Projects", "About Me"],
)

# Dummy STEM data
project_data = pd.DataFrame({
    "Project": ["End-to-end Mushroom Classifier API", 
                   "Object Detection with Faster R-CNN", 
                   "House Price Prediction with XGBOOST", 
                   "Cancer Cell Classification", 
                   "Bitcoin Linear Regression Prediction"],
    "Github url": ["https://github.com/skarra-lab/End-to-end-Mushroom-dataset-project-with-FastAPI.git", 
                   "https://github.com/skarra-lab/Object-detection-FasterR-CNN.git", 
                   "https://github.com/skarra-lab/XGBOOST.git", 
                   "https://github.com/skarra-lab/Logistic-datasets.git", 
                   "https://github.com/skarra-lab/machine-learning-projects.git"],
    "Date": pd.date_range(start="2024-01-01", periods=5),
})

data_certification = pd.DataFrame({
    "Cognitive class": ["Python for Data Analysis", 
                        "Python for Data Science101", 
                        "Data visualisation with Python", 
                        "Machine Learning with Python", 
                        "Machine Learning with PyTorch"],
    "Cisco": ["Python Essentials 1", "Python essentials 2", "Cisco Introduction to Data Science", "Cisco Data Analytics Essentials", "Javascripts essentials 1"],
    "Observation Date": pd.date_range(start="2024-01-01", periods=5),
})

job_simulations = pd.DataFrame({
    "Job Simulation": ["British Airways Data Science", "BCG Data Science", "AWS Machine Learning Foundations", "Introducing GenAI with AWS", "Aerobotics Machine Learning Data Associate"],
    "Results (Pass,Fail,In progess)": ["Pass", "Pass", "Pass", "Pass", "In progress"],
    "Year": [2024, 2024, 2025, 2025, 2026],
    "Recorded Date": pd.date_range(start="2024-01-01", periods=5),
})

# Sections based on menu selection
if menu == "Profile":
    st.title("Junior Data Scientist")
    st.sidebar.header("Profile Options")

    # Collect basic information
    name = "Sikhangele Nogcinisa"
    field = "Data Science & Finance"
    institution = "University of the Western Cape"

    # Display basic profile information
    st.write(f"**Name:** {name}")
    st.write(f"**Field:** {field}")
    st.write(f"**Institution:** {institution}")
    
    image = Image.open("streamlit_files/Income_conf_matrix.png")
    st.image(image, caption="Confusion Matrix", use_container_width=True)

elif menu == "Publications":
    st.title("Publications")
    st.sidebar.header("Upload and Filter")

    # Upload publications file
    uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv")
    if uploaded_file:
        publications = pd.read_csv(uploaded_file)
        st.dataframe(publications)

        # Add filtering for year or keyword
        keyword = st.text_input("Filter by keyword", "")
        if keyword:
            filtered = publications[
                publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
            ]
            st.write(f"Filtered Results for '{keyword}':")
            st.dataframe(filtered)
        else:
            st.write("Showing all publications")

        # Publication trends
        if "Year" in publications.columns:
            st.subheader("Publication Trends")
            year_counts = publications["Year"].value_counts().sort_index()
            st.bar_chart(year_counts)
        else:
            st.write("The CSV does not have a 'Year' column to visualize trends.")

elif menu == "Data Science Projects":
    st.title("Explore Data Projects")
    st.sidebar.header("Data Selection")
    
    # Tabbed view for STEM data
    data_option = st.sidebar.selectbox(
        "Choose a project to explore", 
        ["Data Science Projects", "Certifications", "Job Simulations"]
    )

    if data_option == "Data Science Projects":
        st.write("### Data Projects")
        st.dataframe(project_data)

    elif data_option == "Certifications":
        st.write("### Data Certification")
        st.dataframe(data_certification)

    elif data_option == "Job Simulations":
        st.write("### Weather Data")
        st.dataframe(job_simulations)
        
elif menu == "About Me":
    # Add a contact section
    st.header("Contact Information")
    email = "sikhangelenogcinisa93@gmail.com"
    st.write(f"You can reach me at {email}.")
    cont_number = "+27 79 611 5477"
    st.write(f"You can contact me at {cont_number}")
    



#https://scs2026-app-deploy.streamlit.app/