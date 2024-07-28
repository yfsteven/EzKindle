# simple_anki.py
""" list of useful functions """
import requests
import bs4
import sys
from anki_importer import addNote
from elevenlabs import Voice, VoiceSettings, save
from elevenlabs.client import ElevenLabs
from dotenv import load_dotenv
from os import getenv

def fetch_meaning(word_list: list):
    for word in word_list:
        try:
            url = f'https://dictionary.goo.ne.jp/word/{word}/'
            res = requests.get(url)
            res.raise_for_status()
            word_soup = bs4.BeautifulSoup(res.text, 'html.parser')
            jp_text = word_soup.select('.text')
            full_sentence = ''.join(s.text for s in jp_text)
            transcribe_word(word)

            addNote(word, full_sentence)
        except requests.exceptions.HTTPError:
            print(f"Skipping {word}: It won't be added")
            pass

def transcribe_word(word: str):

    client = ElevenLabs(
      api_key=getenv('API_KEY'), # insert api key
    )

    audio = client.generate(
        text = word,
        model="eleven_multilingual_v2",
        voice=Voice(
            voice_id="j210dv0vWm7fCknyQpbA", #Japanese Voice ID
            settings=VoiceSettings(stability=0.50, similarity_boost=0.65, style=0, use_speaker_boost=True),
        )
    )

    save(audio, f"/home/vboxuser/.local/share/Anki2/ユーザー 1/collection.media/{word}.wav") #May be different from yours, but this saves audio to Anki's media collection folder. Must do this or else not able to get media files
