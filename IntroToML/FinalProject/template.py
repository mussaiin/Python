import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
from flask import Flask, render_template,request,url_for
from flask_bootstrap import Bootstrap

from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd


# train = pd.read_csv('train0.csv', encoding='utf-8')
app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def index():
    imagefile = request.files.get('imagefile', '')
    print(imagefile)
    return render_template('index1.html')


@app.route('/analyse', methods=['POST'])
def analyse():
    return render_template('index1.html', received_text=received, blob_sentiment=result, summary=result)


if __name__ == '__main__':
    app.run(debug=True)