import os
import tensorflow as tf
from flask import Flask, request, jsonify, render_template, redirect, url_for
from PIL import Image
import numpy as np
from werkzeug.utils import secure_filename

# Carregar o modelo salvo
model = tf.keras.models.load_model('model.keras')

# Definir o nome das classes
class_names = ['cavalo', 'humano']

# Definir o tamanho da imagem que o modelo espera
image_size = (160, 160)

# Inicializar a aplicação Flask
app = Flask(__name__)

# Rota principal para upload de imagem
@app.route('/')
def upload_file():
    return render_template('upload.html')

# Rota para processar o upload e fazer a predição
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return redirect(url_for('error_page'))

    file = request.files['file']
    
    if file.filename == '':
        return redirect(url_for('error_page'))

    if file:
        try:
            # Abrir a imagem com o Pillow (PIL) e redimensionar
            image = Image.open(file)
            image = image.resize(image_size)
            image = np.array(image) / 255.0  # Normalizar os valores entre 0 e 1
            image = np.expand_dims(image, axis=0)  # Adicionar dimensão para batch
            
            # Fazer a predição
            prediction = model.predict(image)
            prediction_class = class_names[int(prediction[0] > 0.5)]
            
            # Redirecionar para a página de resultado e passar a classificação
            return redirect(url_for('result', prediction=prediction_class))
        
        except Exception as e:
            print(f"Erro ao processar a imagem: {e}")
            return redirect(url_for('error_page'))

# Rota para exibir apenas o resultado da classificação
@app.route('/result')
def result():
    prediction = request.args.get('prediction')
    return render_template('result.html', prediction=prediction)

# Rota para a página de erro
@app.route('/error')
def error_page():
    return render_template('error.html')

# Rodar a aplicação Flask
if __name__ == '__main__':
    app.run(debug=True)
