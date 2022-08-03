import preprocess
from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

model = joblib.load('Models/model.h5')
scaler = joblib.load('Models/scaler.h5')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def get_prediction():


    if request.method == 'POST':
        year = request.form['year']
        mileage = request.form['mileage']
        tax = request.form['tax']
        mpg = request.form['mpg']
        engineSize = request.form['engineSize']
        model = request.form['model']
        transmission = request.form['transmission']
        fuelType = request.form['fuelType']

    data =  {'year':year, 'mileage':mileage, 'tax':tax, 'mpg':mpg, 'engineSize':engineSize, 'model':model,
            'transmission':transmission, 'fuelType':fuelType}
            
    model = joblib.load('Models/model.h5')
    scaler = joblib.load('Models/scaler.h5')

    Final_data = preprocess.User(data)
    scaled_data = scaler.transform([Final_data])
    predict = model.predict(scaled_data)[0]
    # print(predict)
 
    return render_template('prediction.html', prediction=(predict))

if __name__ == "__main__":
    app.run(debug=True)
