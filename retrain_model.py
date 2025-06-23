import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

df = pd.read_csv("data/academic_cleaned.csv")

if 'performance_category' not in df.columns:
    df['performance_category'] = pd.cut(
        df['exam_score'],
        bins=[-1, 50, 75, 100],
        labels=['Low', 'Medium', 'High']
    )

df_model = df.drop(['student_id', 'exam_score'], axis=1)
y = df_model['performance_category']
X = df_model.drop('performance_category', axis=1)

X_encoded = pd.get_dummies(X, drop_first=True)
joblib.dump(X_encoded.columns.tolist(), "model/feature_names.pkl")

X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
joblib.dump(model, "model/model.pkl")
print("✅ Model and feature names saved")