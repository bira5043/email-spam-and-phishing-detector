import tkinter as tk
from tkinter import filedialog, messagebox
import joblib
import os

# Load the model and vectorizer
model = joblib.load("spam_phishing_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Predict function
def predict_email(text):
    vect_text = vectorizer.transform([text])
    prediction = model.predict(vect_text)[0]
    return prediction

# Browse file and scan
def scan_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if not file_path:
        return
    with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
        content = file.read()

    result = predict_email(content)

    if result == "spam":
        result_label.config(text="🚫 Spam Email Detected", fg="red")
    elif result == "phishing":
        result_label.config(text="⚠️ Phishing Email Detected", fg="orange")
    else:
        result_label.config(text="✅ Email is Safe", fg="green")

# GUI
root = tk.Tk()
root.title("Email Spam & Phishing Detector")
root.geometry("400x200")

tk.Label(root, text="Scan Email File (.txt)", font=("Arial", 14)).pack(pady=10)

tk.Button(root, text="Browse & Scan", command=scan_file, bg="#4caf50", fg="white", padx=20, pady=5).pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=20)

root.mainloop()
