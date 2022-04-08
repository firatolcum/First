"""
Convert the data given in the tuple into a json(javascript object notation) type document.
"""

import json
turn_to_json = {
    "eventId": 674189,
    "dateTime": "2015-02-12T09:23:17.511Z",
    "chocolate": "Semi-sweet Dark",
    "isTomatoAFruit": False
}

with open("output.json", "w") as json_file:
    json.dump(turn_to_json, json_file)
