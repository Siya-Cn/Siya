from pathlib import Path
import json

favorite_numbers = {}

prompt = '请输入您喜欢的数：'
message = input(prompt)
favorite_numbers['value'] = message
print(favorite_numbers)

path = Path('numbers.json')
contents = json.dumps(favorite_numbers)
path.write_text(contents)