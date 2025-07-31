# Heart_Disease_Prediction_System
## ❤️ Heart Disease Prediction Web App

A machine learning-based web application developed using **Flask** that predicts the likelihood of a person having heart disease based on several medical inputs.

---

## 🧠 About the Project

This project uses a pre-trained machine learning model to evaluate patient data and predict heart disease risk. The application features a clean, responsive front-end built with HTML and CSS, and a backend served by Flask.

---

## Accuracy of the Models and Algorithms Used

| Sr No | Algorithm Used                   | Accuracy   |
|-------|----------------------------------|------------|
| 1     | K - Nearest Neighbor             | 97.82%     |
| 2     | Random Forest                    | 86.95%     |
| 3     | Ada Boost With Random Forest     | 93.47%     |
| 4     | Gradient Boosting                | 89.91%     |

---


## 📁 Project Structure

```
Heart_Disease_Prediction_System
│
├── static/
│   ├── Heart.gif
│   ├── heartbeat.png
│   ├── heartcp.png
│   ├── heartp.png
│   ├── icons8-heart.gif
│   └── new.gif
│
├── templates/
│   ├── detail.html
│   ├── index.html
│   └── predict.html
│
├── .gitattributes
├── .gitignore
├── app.py
├── hdp_data.csv
├── hdp_model.pkl
├── heart_disease.ipynb
├── LICENSE
├── model_jlib
├── README.md
└── requirements.txt
```

---

## ⚙️ Prerequisites

Make sure you have **Python 3.9+** installed on your system.

---

## 🛠️ Setup Instructions

### 🐚 Bash Setup

Run the following commands in your terminal:

Clone the repository

```bash
git clone https://github.com/your-username/heart-disease-prediction.git
```

Create virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

For **Windows**:

```bash
venv\Scripts\activate
```

For **Unix** or **MacOS**:

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🧠 Model File

Make sure to place the trained model `hdp_model.pkl` in the correct path:
```plaintext
C:\Users\hasit\OneDrive\Desktop\Heart_Disease_prediction-WebApp\Heart-Disease-Prediction-main\hdp_model.pkl
```

> You can modify the path in `app.py` to match your own model file location:
```python
fullpath = 'path/to/your/hdp_model.pkl'
```

---

## 🚀 Running the App

Once everything is set up, run the Flask application:

```bash
python app.py
```

Go to your browser and visit:  
👉 [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 💡 Features

- User-friendly web interface
- Collects medical input like age, sex, blood pressure, etc.
- Predicts likelihood of heart disease using ML model
- Personalized result view with animations and styling
- Fully responsive and themed with modern design

---

## 📸 Screenshots

![Home Page](Screenshots/Screenshot_1.png)
![Details Form](Screenshots/Screenshot_2.png)
![Prediction Result](Screenshots/result_with_heart_disease.png)

---

## 👨‍💻 Author

- **Hasitha Reddy Eppalapalli**  
  - [GitHub](https://github.com/hasithaa02)  
  - [LinkedIn](https://www.linkedin.com/in/hasitha-reddy-eppalapalli-ab290a230/)

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### ❤️ Made with care for early diagnosis and better health outcomes!
### If you like the project, please ⭐ this repository!
