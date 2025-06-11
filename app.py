from flask import flask,render_template,request
import pickle
import numpy as np 

app = Flask(__name__)

with open('house_price_prediction.pkl','rb') as f:
    model.pickle.load(f)