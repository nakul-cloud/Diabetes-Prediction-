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

# Diabetes Prediction  

## How the Prediction Works  

### **Steps**  

1. **User Input**:  
   - The user enters their **Glucose, Insulin, BMI, Age, Blood Pressure, and other health data** in the web form.  

2. **Data Preprocessing**:  
   - Input features are **scaled using a pre-trained `scaler.pkl`** to match the training data distribution.  

3. **Model Prediction**:  
   - The **Random Forest model (`rf_model.pkl`)** predicts the probability of having diabetes.  

4. **Result Display**:  
   - The webpage displays one of the following results:  
     - **"You may have diabetes."** (Positive Prediction)  
     - **"You are not likely to have diabetes."** (Negative Prediction)  

---

## Exploratory Data Analysis (EDA)  

The **Jupyter Notebook (`Main.ipynb`)** contains a detailed **Exploratory Data Analysis (EDA)**, including:  

### **Data Preprocessing**  

- **Convert date columns** (if applicable) to `datetime` format.  
- **Handle missing values** and remove irrelevant or inconsistent data.  
- **Remove duplicate entries** for cleaner analysis.  

### **Feature Engineering**  

- Normalize numerical values for **consistent model performance**.  

### **Data Visualization**  

- **Histograms**: Show distributions of **glucose levels, BMI, and other health metrics**.  
- **Box Plots**: Identify **outliers** in the dataset.  
- **Correlation Heatmaps**: Identify relationships between variables.  

### **Outlier Detection and Handling**  

- Identify and **remove extreme values** in the dataset.  

---

## Visualizations & Model Performance  

- The **Jupyter Notebook (`Main.ipynb`)** includes:  
  - **Histograms for input feature distributions**.  
  - **Feature importance analysis** (which variables contribute most to predictions).  
  - **Performance metrics** like **accuracy, precision, recall, and F1-score**.  

- The **Random Forest model** achieved **high accuracy**, making it a reliable choice for diabetes prediction.  

---

## Key Findings  

### **Feature Importance**  

- **Glucose levels and BMI** were found to be the **most important** factors in predicting diabetes.  
- **Diabetes Pedigree Function** had a moderate effect, indicating genetic influence.  

### **Prediction Accuracy**  

- The model performs **better than traditional statistical methods** in early diabetes detection.  

### **Outliers and Data Cleaning**  

- Certain data points (e.g., **negative values for insulin levels**) were removed for accuracy.  

---

## Conclusion  

- **Machine learning can effectively predict diabetes** using common health indicators.  
- **Feature scaling improves prediction accuracy**, ensuring better generalization on new data.  
- **Random Forest was a suitable model**, but further improvements can be made with deep learning approaches.  

---

## Future Improvements  

- **Deploy the model using Flask + Docker** for scalability.  
- **Integrate additional medical features** for even better accuracy.  
- **Create a mobile-friendly UI** for easier accessibility.  

---

## Acknowledgements  

This project was developed using publicly available **medical datasets** and **machine learning frameworks**.  
Thanks to the open-source community for maintaining useful libraries like **Flask, NumPy, and Scikit-learn**.  

---

## Contact  

For any questions, issues, or suggestions, feel free to contact: [jadhavnakul456@gmail.com](mailto:jadhavnakul456@gmail.com)  


---

## License  

This project is licensed under the **MIT License**. Feel free to use and modify it for educational and research purposes.  



