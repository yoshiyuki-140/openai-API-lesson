import os
import openai
from openai import OpenAI
from local import OPENAI_API_KEY


# proxy setting
os.environ['http_proxy'] = 'http://wwwproxy.kanazawa-it.ac.jp:8080'
os.environ['https_proxy'] = 'http://wwwproxy.kanazawa-it.ac.jp:8080'

client = OpenAI(
    api_key=OPENAI_API_KEY
)

sysem_setting_prompt = """
あなたは統計学のスペシャリストです。
"""

user_prompt = """
有意水準とは何か、200文字程度で説明しなさい。
"""

completion = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": sysem_setting_prompt},
        {"role": "user", "content": user_prompt}
    ]
)

print(completion.choices[0].message)

# with open('./result_gpt4_001.txt', mode='w', encoding="utf-8") as f:
    # f.write(completion.choices[0].message)
