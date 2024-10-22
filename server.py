from flask import Flask, render_template, request
# Import the EmotionDetection package 
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route("/emotionDetector")
def RunSentimentAnalysis():
    text = str(request.args.get('textToAnalyze'))  

    result = emotion_detector(text)


if __name__ == "__main__":
    # By default the Flask application is executed in
    # host = localhost
    # port = 5000 
    app.run()