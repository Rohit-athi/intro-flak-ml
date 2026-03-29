from flask import Flask,render_template,request
import pickle

app = Flask(__name__)

model = pickle.load(open("model1.pkl","rb"))

@app.route("/")
def home():
    return render_template("index.html")


@app.route('/predict')
def predict():
    data = request.args
    
    # Use .get() with a default value to prevent errors if a field is missing
    size = int(data.get("size", 0))
    age = int(data.get("age", 0))
    
    # Replace 'arg' with 'age' and ensure the order matches your training data
    # Standard format: [[feature1, feature2]]
    predicts = model.predict([[age, size]])

    # predicts[0] is often an array or a single value; 
    # ensure your template can handle the returned type.
    return render_template("index.html", val=predicts[0])



if __name__ == "__main__":
    app.run(debug=True)