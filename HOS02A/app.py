from flask import Flask, render_template
import os

app = Flask(__name__)
#load model once used by all prediction calls
import joblib
clf = joblib.load("binary_clf.joblib")

@app.route('/')
def home():
    return render_template('index.html')

@app.get('/predict/<int:input_data>')
def converter_with_type(input_data):
    # make train data look alike predict data 
    pred_data = [[input_data]]
    predict_result = clf.predict(pred_data)
    return ("Prediction result: " + str(predict_result))

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 2791 ))
    app.run(debug=True, host='0.0.0.0', port=port)

