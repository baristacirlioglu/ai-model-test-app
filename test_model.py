from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import json

# 1. Veri setini yükle
X, y = load_iris(return_X_y=True)

# 2. Eğitim ve test verisine böl (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 3. Modeli oluştur ve eğit
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# 4. Tahmin yap
y_pred = model.predict(X_test)

# 5. Accuracy ve confusion matrix hesapla
acc = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)

# 6. Sonuçları JSON formatında kaydet
results = {
    "accuracy": acc,
    "confusion_matrix": cm.tolist()
}

with open("results.json", "w") as f:
    json.dump(results, f, indent=2)

print("Model test edildi ve sonuçlar results.json dosyasına kaydedildi.")