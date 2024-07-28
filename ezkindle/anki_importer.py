""" anki_importer make use of AnkiConnect addon https://foosoft.net/projects/anki-connect/index.html#deck-actions"""
import json
import urllib.request

def request(action, **params):
    return {'action': action, 'params': params, 'version': 6}

def invoke(action, **params):
    requestJson = json.dumps(request(action, **params)).encode('utf-8')
    response = json.load(urllib.request.urlopen(urllib.request.Request('http://127.0.0.1:8765', requestJson)))
    if len(response) != 2:
        raise Exception('response has an unexpected number of fields')
    if 'error' not in response:
        raise Exception('response is missing required error field')
    if 'result' not in response:
        raise Exception('response is missing required result field')
    if response['error'] is not None:
        raise Exception(response['error'])
    return response['result']

def addNote(frontc, backc):
    """add card to your anki deck"""
    with open("note.template.json") as file:
        note = json.load(file)
        note["fields"]["表面"] = frontc
        note["fields"]["裏面"] = backc
        note["fields"]["Audio"] = f"[sound:{frontc}.wav]"

        try:
            invoke('addNote', note=note)
            invoke('sync')
        except Exception as err:
            print(f"Can not create {frontc} note - {err}")
