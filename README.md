# Academic Performance Predictor

This project analyzes how lifestyle and study habits affect academic performance using a machine learning model.

## Features
- View and explore a cleaned academic dataset
- Visualize trends in study, sleep, social media usage, and performance
- Predict academic performance based on lifestyle inputs

## Run the App
1. Install required packages:
```
pip install -r requirements.txt
```

2. Run Streamlit:
```
streamlit run app/Home.py
```

## Folder Structure
```
project/
│
├── app/
│   ├── Home.py
│   ├── Data_Overview.py
│   └── Academic_Prediction.py
│
├── data/
│   └── academic_cleaned.csv
│
├── model/
│   └── model.pkl
│
├── requirements.txt
└── README.md
```