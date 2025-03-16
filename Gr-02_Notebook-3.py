#!/usr/bin/env python
# coding: utf-8

# # Step 9: User Interface Development with Streamlit
# 
# ### Objectives:
# - Set up Streamlit UI for input fields.
# - Call the FastAPI prediction endpoint (http://127.0.0.1:8000/predict).
# - Display the prediction result dynamically.
# - Show appropriate messages based on input.

# ### 1. Install & Import Required Libraries

# In[21]:


# get_ipython().system('pip install streamlit requests')


# In[22]:


import streamlit as st
import requests
import json


# ### 2. Define the Streamlit UI Layout

# In[23]:


# Streamlit UI title
st.title("📊 Bank Marketing Prediction App")

st.write("""
### 📌 Enter Customer Details to Get a Prediction:
Fill in the required details and click **'Predict'** to check if the customer will subscribe to a term deposit.
""")


# ### 3. Create Input Fields for User Data

# In[24]:


# Define user input fields
age = st.number_input("Age", min_value=18, max_value=100, value=30)
job = st.selectbox("Job", ["admin.", "blue-collar", "entrepreneur", "housemaid", "management",
                           "retired", "self-employed", "services", "student", "technician", "unemployed", "unknown"])
marital = st.selectbox("Marital Status", ["married", "single", "divorced"])
education = st.selectbox("Education", ["primary", "secondary", "tertiary", "unknown"])
default = st.selectbox("Has Credit in Default?", ["yes", "no"])
balance = st.number_input("Balance", min_value=-10000, max_value=100000, value=1000)
housing = st.selectbox("Has Housing Loan?", ["yes", "no"])
loan = st.selectbox("Has Personal Loan?", ["yes", "no"])
contact = st.selectbox("Contact Type", ["cellular", "telephone"])
day = st.number_input("Last Contact Day", min_value=1, max_value=31, value=15)
month = st.selectbox("Last Contact Month", ["jan", "feb", "mar", "apr", "may", "jun",
                                            "jul", "aug", "sep", "oct", "nov", "dec"])
duration = st.number_input("Last Contact Duration (seconds)", min_value=0, value=180)
campaign = st.number_input("Number of Contacts During Campaign", min_value=1, value=2)
pdays = st.number_input("Days Passed Since Last Contact (-1 if never contacted)", min_value=-1, value=-1)
previous = st.number_input("Number of Previous Contacts", min_value=0, value=0)
poutcome = st.selectbox("Previous Campaign Outcome", ["failure", "nonexistent", "success"])

# Additional Features
emp_var_rate = st.number_input("Employment Variation Rate", value=-1.8)
cons_price_idx = st.number_input("Consumer Price Index", value=92.893)
cons_conf_idx = st.number_input("Consumer Confidence Index", value=-46.2)
euribor3m = st.number_input("Euribor 3-month Rate", value=1.313)
nr_employed = st.number_input("Number of Employees", value=5099.1)
day_of_week = st.selectbox("Day of the Week", ["mon", "tue", "wed", "thu", "fri"])


# ### 4. Send Input Data to FastAPI for Prediction

# In[25]:


# Prepare input data
input_data = {
    "age": age,
    "job": job,
    "marital": marital,
    "education": education,
    "default": default,
    "balance": balance,
    "housing": housing,
    "loan": loan,
    "contact": contact,
    "day": day,
    "month": month,
    "duration": duration,
    "campaign": campaign,
    "pdays": pdays,
    "previous": previous,
    "poutcome": poutcome,
    "emp_var_rate": emp_var_rate,
    "cons_price_idx": cons_price_idx,
    "cons_conf_idx": cons_conf_idx,
    "euribor3m": euribor3m,
    "nr_employed": nr_employed,
    "day_of_week": day_of_week
}

# API URL
API_URL = "http://127.0.0.1:8000/predict"

# Submit button
if st.button("🔍 Predict"):
    try:
        # Send request to FastAPI
        response = requests.post(API_URL, json=input_data)
        result = response.json()

        # Display prediction
        if "error" in result:
            st.error(f"❌ Error: {result['error']}")
        else:
            st.success(f"✅ Prediction: {result['prediction']}")
            st.write(f"📊 Probability of No: {result['probability_no']:.4f}")
            st.write(f"📊 Probability of Yes: {result['probability_yes']:.4f}")

    except Exception as e:
        st.error(f"❌ API Request Failed: {str(e)}")


# ### 5. Running the Streamlit UI

# In[26]:


# get_ipython().system('jupyter nbconvert --to script Gr-02_Notebook-3.ipynb')


# In[ ]:




