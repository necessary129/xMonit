import json
bb = open('approved.json')
dd = json.load(bb)
approved = set(dd.approved)
