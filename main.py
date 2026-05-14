from openai import OpenAI
import os
from pathlib import Path
from datetime import datetime
import csv
import json

if not Path('logs').is_dir():
    Path.mkdir('logs', exist_ok=True, parents=True)

logs = sorted([i.name for i in Path('logs').glob('*.log')], key=lambda x: int(x[:-4]))
ind = int(logs[-1][:-4])+1 if logs != [] else 0

client = OpenAI(
    api_key=os.environ.get("API_KEY"),
    base_url="https://api.xiaomimimo.com/v1"
)

with open('prompt_struct.json', encoding='utf-8') as file:
    structure = file.read()

output = {"answers": []}
def pipe_to_model(input : str):
    with open(f'logs/{ind}.log', 'a', encoding='utf-8') as log:
        time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log.write(f'{time} > {input}\n')

        response = client.chat.completions.create(
            model="mimo-v2-flash",
            messages=[
                {
                'role': 'system',
                'content': f'Твоя задача проанализировать отзыв и выдать основную информацию согласно структуре json: {structure}'
                },
                {
                'role': 'user',
                'content': input
                }
            ],
            max_completion_tokens=1024,
            response_format={ "type": "json_object" }
        )

        time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log.write(f'{time} < {response}\n')

        content = response.choices[0].message.content
        print(json.loads(content))
        output["answers"].append( json.loads(content) )


if __name__ == '__main__':
    with open('input.csv', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            pipe_to_model(row['review'])
    
    json.dump(output, open('output.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

    