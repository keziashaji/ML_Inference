from sklearn.tree import DecisionTreeClassifier
import joblib

X = [[40],[50],[60],[70],[80],[90]]
y = [0,0,0,1,1,1]

model = DecisionTreeClassifier()

model.fit(X,y)

joblib.dump(model,"model.pkl")

print("Model saved!")