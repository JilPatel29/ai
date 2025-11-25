import matplotlib.pyplot as plt

models = ['Logistic Regression', 'SVM', 'Decision Tree', 'ANN', 'Random Forest']
accuracy = [0.83, 0.86, 0.88, 0.91, 0.95] 

plt.figure(figsize=(10,6))             
plt.bar(models, accuracy)
plt.xlabel("Models", fontsize=12)
plt.ylabel("Accuracy", fontsize=12)
plt.title("Model Comparison for DDoS Detection", fontsize=14)

plt.ylim(0.7, 1.0)                     
plt.xticks(rotation=30, fontsize=11)   
plt.tight_layout()                    
plt.show()
