"""
Server for the emotion detector app
detects the emotion of user entered text
"""
from flask import Flask, render_template, request
# Import the EmotionDetection package
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    """
    route for the home/start page of the application
    """
    return render_template('index.html')


@app.route("/emotionDetector")
def detector_route():
    """
    analyse the user provided text
    using the emtion detector function
    """
    text = str(request.args.get('textToAnalyze'))
    result_dict = emotion_detector(text)
    if result_dict['dominant_emotion'] == "None":
        return "<strong>Invalid text! Please try again!.</strong>"
    result = "For the given statement, the system response is" \
    f"'anger' {str(result_dict['anger'])}," \
    f"‘disgust’: {str(result_dict['disgust'])}," \
    f"‘fear’: {str(result_dict['fear'])}," \
    f"‘joy’: {str(result_dict['joy'])}" \
    f"and ‘sadness’: {str(result_dict['sadness'])}." \
    f"The dominant emotion is <strong>{result_dict['dominant_emotion']}</strong>"
    return result


if __name__ == "__main__":
    # By default the Flask application is executed in
    # host = localhost
    # port = 5000
    app.run()
