"""Module providing a function emotion detection python version."""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    """Sent analyser method"""
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

     # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract the label and score from the response
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']

    scores = {}
    scores['anger'] = anger
    scores['disgust'] = disgust
    scores['fear'] = fear
    scores['joy'] = joy
    scores['sadness'] = sadness

    if anger is None:
        return "Invalid input! Try again."

    dominant_emotion = max(scores, key=scores.get)
    # Return a formatted string with the sentiment label and score
    return f"For the given statement, the system response is {scores}. The dominant emotion is {dominant_emotion} ¤"

@app.route("/")
def render_index_page():
    """render index page method"""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="localhost", port=5000)
