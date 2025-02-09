# Diabetes Prediction  

## Data Source  
The model was trained using a dataset containing medical records, including:  

- **Glucose Levels**  
- **Insulin Levels**  
- **Body Mass Index (BMI)**  
- **Blood Pressure**  
- **Diabetes Pedigree Function**  
- **Skin Thickness**  
- **Pregnancies**  
- **Age**  

The data was **cleaned, scaled, and used to train a Random Forest classifier** for accurate predictions.  

---

## Files  

- **Main.ipynb**: Jupyter Notebook containing the model training, data preprocessing, and performance evaluation.  
- **app.py**: Flask application that loads the trained model and serves predictions.  
- **index.html**: Frontend web page for user interaction, allowing input of health metrics.  
- **styles.css**: CSS file for styling the web page.  

---

## Key Features  

- **User-Friendly Web Interface**: Allows users to input health details easily.  
- **Machine Learning-Based Prediction**: Uses a **Random Forest model** trained on real medical data.  
- **Real-Time Processing**: Predictions are generated instantly.  
- **Data Preprocessing & Scaling**: Input features are **normalized using a pre-trained scaler**.  
- **Flask Backend**: The model is served through a simple **Flask web application**.  

---

## How to Run  

### 1. Clone the Repository  

```bash
git clone https://github.com/yourusername/diabetes-prediction.git
cd diabetes-prediction
