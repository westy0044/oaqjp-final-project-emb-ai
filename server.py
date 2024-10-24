from flask import Flask, render_template, request
# Import the EmotionDetection package 
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route("/emotionDetector")
def detector_route():
    text = str(request.args.get('textToAnalyze')) 
    result_dict = emotion_detector(text) 
    if result_dict['dominant_emotion'] == "None":
        return "<strong>Invalid text! Please try again!.</strong>"
    else:
        result = f"For the given statement, the system response is 'anger' {str(result_dict['anger'])}, ‘disgust’: {str(result_dict['disgust'])}, ‘fear’: {str(result_dict['fear'])}, ‘joy’: {str(result_dict['joy'])} and ‘sadness’: {str(result_dict['sadness'])}. The dominant emotion is <strong>{result_dict['dominant_emotion']}</strong>"
        return result


if __name__ == "__main__":
    # By default the Flask application is executed in
    # host = localhost
    # port = 5000 
    app.run()