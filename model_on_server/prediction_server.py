from flask import Flask, request
import pickle
import numpy as np
app = Flask(__name__)


with open('cancer_predictor.pkl', 'rb') as input:
    cancer_predictor = pickle.load(input)
    
@app.route('/cancer')    
def predict_func():
    value = request.args.get('value')
    try:
        x = float(value)
    
        if (x > 29) or (x < 6):
            return f'enter value between 29 and 6'
        else:
            x = np.array(x).reshape(-1, 1)
            prediction = cancer_predictor.predict(x)
            return f'Вероятность рака груди: {prediction}'
    except ValueError:
        return f'enter value between 29 and 6'
        
    
if __name__ == '__main__':
    app.run('localhost', 5000)