import pickle,numpy as np
from flask import Flask, redirect, url_for, request, jsonify, render_template
from tensorflow import keras
import requests
import json
app = Flask(__name__)
api = Api(app)
class farm_md(Resource):
    def post(self):
        f = request.files['image']
        f.save(secure_filename('test.jpg'))
        im = Image.open('test.jpg')
        im = im.resize((224, 224))
        image = np.array(im)
        image = image*(1.0/255)
        image = image.reshape(1, 224, 224, 3)
        model = pickle.load(open('modelv6.pkl', 'rb'))
        prediction = model.predict(image)
        head = ['Apple Cedar apple rust','Apple healthy','Corn common rust','Corn healthy']
        correct = max(prediction[0])
        cor_class = ""
        temp = ""
        for i in range(4):
            if prediction[0][i] == correct:
                cor_class = head[i]
                break
        json = { "class" : cor_class, "temp": response['main']['temp'],"humidity":response['main']['humidity'], "pressure":response['main']['pressure'], "address": x['results'][0]['address_components'][4]['short_name']+" "+x['results'][0]['address_components'][5]['short_name']}
        
        return jsonify(json)