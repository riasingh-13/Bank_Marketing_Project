# 🏦 MLOps Bank Marketing Project

This project implements an **end-to-end MLOps pipeline** to predict whether a customer will subscribe to a term deposit based on **bank marketing campaign data**.  
It includes **data preprocessing, model training, deployment, UI development, and model monitoring** using **FastAPI, Streamlit, and Weights & Biases (W&B).**

## 🚀 **Project Workflow**
1️⃣ **Data Preparation**: Load, clean, and preprocess the dataset.  
2️⃣ **Data Profiling**: Generate insights using Pandas Profiling.  
3️⃣ **Dataset Splitting**: Train, Test, and Production dataset creation.  
4️⃣ **Data Version Control**: Track dataset changes with GitHub.  
5️⃣ **ML Pipeline**: Build a Scikit-Learn pipeline for model training.  
6️⃣ **ML Experimentation**: Run experiments & log results with W&B.  
7️⃣ **Model Deployment**: Deploy the trained model as a REST API using FastAPI.  
8️⃣ **User Interface**: Build a UI using Streamlit to interact with the model.  
9️⃣ **Model Monitoring**: Detect data drift between Train and Production datasets.  

---

## 📺 **Project Structure**
```
MLOps_BankMarketing_Project/
│── .ipynb_checkpoints/               # Jupyter Notebook checkpoints
│── artifacts/                        # Model artifacts stored in W&B
│   ├── best_model-v0/                # Best trained model version 0
│
│── datasets/                         # Dataset Storage
│   ├── bank-additional-full.parquet   # Original dataset in Parquet format
│
│── wandb/                            # Weights & Biases tracking logs
│── wandb_models/                     # Model versions stored from W&B
│
│── Gr-02_Notebook-1.ipynb            # Data Preparation & Experiments Notebook
│── Gr-02_Notebook-2.ipynb            # FastAPI Deployment Notebook
│── Gr-02_Notebook-3.ipynb            # Streamlit UI Notebook
│── Gr-02_Notebook-3.py               # Streamlit UI Script
│── Gr-02_Notebook-4.ipynb            # Model Monitoring Notebook
```

---

## 🛠 **Setup Instructions**
Follow these steps to run the project locally.

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/riasingh-13/MLOps_BankMarketing_Project.git
cd MLOps_BankMarketing_Project
```

### **2️⃣ Run the Jupyter Notebooks**
- **Data Preprocessing & Experimentation**
```bash
jupyter notebook Gr-02_Notebook-1.ipynb
```
- **Model Deployment (FastAPI)**
```bash
jupyter notebook Gr-02_Notebook-2.ipynb
```
- **UI Development (Streamlit)**
```bash
jupyter notebook Gr-02_Notebook-3.ipynb
```
- **Model Monitoring**
```bash
jupyter notebook Gr-02_Notebook-4.ipynb
```

---

## 🚀 **Run the FastAPI Model Deployment**
1. **Navigate to the project directory**
```bash
cd MLOps_BankMarketing_Project
```
2. **Run the FastAPI server**
```bash
uvicorn deploy_fastapi:app --reload
```
3. **Test API Using Swagger UI**  
   Open your browser and go to:  
   🔍 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  

---

## 🎨 **Run the Streamlit UI**
1. **Navigate to the project directory**
```bash
cd MLOps_BankMarketing_Project
```
2. **Run Streamlit UI**
```bash
streamlit run Gr-02_Notebook-3.py
```
3. **Open UI in Browser**  
   🔍 [http://localhost:8501](http://localhost:8501)  

---

## 📊 **Model Monitoring: Detecting Data Drift**
We use **Alibi-Detect** to check if the production data is different from the training data.

1. **Run the Model Monitoring Notebook**
```bash
jupyter notebook Gr-02_Notebook-4.ipynb
```
2. **Check the Data Drift Results in Tabular Format.**

---

## 📀 **Key Technologies Used**
- **🔰 Python** → Core Language  
- **📈 Pandas, NumPy** → Data Processing  
- **🔬 Scikit-Learn** → ML Pipeline & Experimentation  
- **🏢 FastAPI** → Model Deployment  
- **🎩 Streamlit** → User Interface  
- **📊 Weights & Biases (W&B)** → Experiment Tracking & Model Registry  
- **🚨 Alibi-Detect** → Data Drift Detection  

---

## 🔥 **Project Highlights**
✅ **Fully Automated MLOps Workflow**  
✅ **Version Control for Dataset & Model**  
✅ **Experiment Tracking with W&B**  
✅ **FastAPI Endpoint for Predictions**  
✅ **Interactive UI for User Input**  
✅ **Model Monitoring for Data Drift**  

---

## 📉 **Next Steps**
- 🚀 **Improve Model Performance with Feature Engineering.**  
- 📊 **Deploy on Cloud (AWS/GCP/Azure) for Real-World Use.**  
- 🔍 **Automate Model Retraining on Data Drift Detection.**  

---

## 🤝 **Contributing**
Contributions are welcome! If you’d like to improve this project:
1. **Fork the repository.**
2. **Create a new branch.**
3. **Make your changes and commit them.**
4. **Push to your fork and submit a Pull Request.**

---

## 📄 **License**
This project is **open-source** under the **MIT License**.

---

## ⭐ **If you found this project useful, don't forget to star the repository!** ⭐

