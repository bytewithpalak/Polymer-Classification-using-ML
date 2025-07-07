# Polymer Classification Using Machine Learning

## 🔍 Overview

This project builds a multi-model machine learning pipeline to classify polymers based on their molecular fingerprints. The dataset includes over 20,000 polymer samples, each represented by a 2048-bit binary fingerprint vector.

We trained and evaluated multiple models to determine the most accurate approach for polymer type prediction.

---

## 📁 Dataset

* **Source**: Provided dataset (CSV format)
* **Samples**: 20,609 polymer molecules
* **Features**: 2048 binary molecular fingerprint bits (indicating substructure presence)
* **Target**: Polymer class (e.g., plastic, peptide, oligosaccharide)

### 🧠 What Are Fingerprint Features?

Molecular fingerprints are binary vectors representing the presence or absence of certain chemical substructures in a molecule. Each bit position refers to a specific structural pattern. This makes them ideal for machine learning input.

---

## ⚙️ Machine Learning Models Used

1. **Random Forest**
2. **K-Nearest Neighbors (KNN)**
3. **Support Vector Machine (SVM)**
4. **XGBoost**

All models were evaluated using:

* Accuracy
* Confusion Matrix
* Classification Report

---

## 📊 Model Performance Summary

| Model         | Accuracy | Notes                           |
| ------------- | -------- | ------------------------------- |
| Random Forest | 1.00     | Perfect classification          |
| KNN           | 0.975    | Slightly lower, distance-based  |
| SVM           | 1.00     | Clean margin, excellent results |
| XGBoost       | 1.00     | Fast, scalable, accurate        |

---

## 🏆 Best Model Selected

XGBoost was chosen for deployment due to its balance of speed, scalability, and high accuracy.

---

## 💾 Model Saving

The selected model and LabelEncoder were saved using `joblib` for use in the app:

```python
joblib.dump(xgb_model, 'best_model.pkl')
joblib.dump(encoder, 'label_encoder.pkl')
```


## 📌 Final Thoughts

This project demonstrates how machine learning can effectively classify polymers using structural fingerprint features.

> "From atoms to accuracy — polymers classified using machine learning."


