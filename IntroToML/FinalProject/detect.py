import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
from flask import Flask, render_template,request,url_for
from flask_bootstrap import Bootstrap

from keras.preprocessing import image
from keras.models import model_from_json
import numpy as np

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/analyse', methods=['POST'])
def analyse():
    if request.method == 'POST':
        filename = request.form['filename']
        sfname = 'images/' + filename
        json_file = open('./model/facial_expression_model_structure.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        model = model_from_json(loaded_model_json)
        model.load_weights("./model/facial_expression_model_weights.h5")
        print("Loaded model from disk")

        emotion_dict = {
            0: 'Angry',
            1: 'Disgust',
            2: 'Fear',
            3: 'Happy',
            4: 'Sad',
            5: 'Surprised',
            6: 'Neutral'
        }

        img = image.load_img(sfname, grayscale=True, target_size=(48, 48))

        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x /= 255

        custom = model.predict(x)
        index_max = np.argmax(custom[0])

        predicted = emotion_dict[index_max]
        # print("Emotion :", predicted)

    return render_template('index.html', blob_sentiment=predicted, summary=str(predicted))

if __name__ == '__main__':
    app.run(debug=True, threaded=False)