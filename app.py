from flask import Flask, request
from youtube_transcript_api import YouTubeTranscriptApi
from transformers import pipeline
import requests
app = Flask(__name__)

@app.get('/summary')
def summary_api():
    url = request.args.get('url', '')
    video_id = url.split('=')[1]
    summary = get_summary(get_transcript(video_id))
    return summary, 200

def get_transcript(video_id):
    transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
    transcript = ' '.join([d['text'] for d in transcript_list])
    return transcript

def get_summary(transcript):
    api_url = "https://article-extractor-and-summarizer.p.rapidapi.com/summarize-text"
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "4fbc267b64mshe1cfa51cc191b8ep119d63jsnac8c1dac640f",
        "X-RapidAPI-Host": "article-extractor-and-summarizer.p.rapidapi.com"
    }
    payload = {
        "text": transcript
    }
    response = requests.post(api_url, json=payload, headers=headers).json()
    summary = response["summary"]
    return summary
    

if __name__ == '__main__':
    app.run()