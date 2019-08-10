import os
from flask import Flask, request, Response
import requests
import json

app = Flask(__name__)

@app.route('/', methods=['POST'])
def verify():
	data = request.json
	if data['event']['type'] == "app_mention":
		user_text = data['event']['text']
		user = data['event']['user']
		remove_from = user_text.index('>')
		text = user_text[remove_from+2::]
		print(text)
		webhook_url = 'https://hooks.slack.com/services/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'
		slack_data = {
	    "text": "Would you like to play a game?",
    	"attachments": [
      {
        "text": "Choose a game to play",
        "fallback": "You are unable to choose a game",
        "callback_id": "wopr_game",
        "color": "#3AA3E3",
        "attachment_type": "default",
        "actions": [
          {
            "name": "game",
            "text": "Chess",
            "type": "button",
            "value": "chess"
          },
          {
            "name": "game",
            "text": "Falken's Maze",
            "type": "button",
            "value": "maze"
          },
          {
            "name": "game",
            "text": "Thermonuclear War",
            "style": "danger",
            "type": "button",
            "value": "war",
            "confirm": {
              "title": "Are you sure?",
              "text": "Wouldn't you prefer a good game of chess?",
              "ok_text": "Yes",
              "dismiss_text": "No"
            }
          }
        ]
      }
    ]
	}
		response = requests.post(
	    webhook_url, data=json.dumps(slack_data),
	    headers={'Content-Type': 'application/json'}
		)
	return('', 204)

if __name__ == "__main__":
  app.run(debug=True)	