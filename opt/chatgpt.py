improt openai
import json

f_in = open("./setting.json", "r")
settings = json.load(f_in)
KEY = settings.get("KEY")
print(KEY)