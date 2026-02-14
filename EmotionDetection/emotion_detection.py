import requests # Import the requests library to handle HTTP requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, json = myobj, headers=header)

    # If the response status code is 200, extract the label and score from the response
    if response.status_code == 200:

        formatted_response = json.loads(response.text)
        
        anger = formatted_response['emotionPredictions'][0]['emotion']['anger']
        disgust = formatted_response['emotionPredictions'][0]['emotion']['disgust']
        fear = formatted_response['emotionPredictions'][0]['emotion']['fear']
        joy = formatted_response['emotionPredictions'][0]['emotion']['joy']
        sadness = formatted_response['emotionPredictions'][0]['emotion']['sadness']

        scores = {}
        scores['anger'] = anger
        scores['disgust'] = disgust
        scores['fear'] = fear
        scores['joy'] = joy
        scores['sadness'] = sadness
        dominant_emotion = max(scores, key=scores.get)	
    # If the response status code is 400, set label and score to None
    elif response.status_code == 400:
        anger = None
        disgust = None
        fear = None
        joy = None
        sadness = None
        dominant_emotion = None

    return {'anger': anger, 'disgust': disgust, 'fear': fear, 'joy': joy, 'sadness': sadness, 'dominant_emotion': dominant_emotion}
