import os
import openai
from local import OPENAI_API_KEY, OPENAI_ORGANIZATION

openai.organization = OPENAI_ORGANIZATION
openai.api_key = OPENAI_API_KEY


# プロンプトの設定
prompt = "Please change sky color!"

# settings of API request 
response = openai.Completion.create(
    model="text-davinci-002",  # GPTのエンジン名を指定します
    prompt=prompt,
    max_tokens=100,  # 生成するトークンの最大数
    n=5,  # 生成するレスポンスの数
    stop=None,  # 停止トークンの設定
    temperature=0.7,  # 生成時のランダム性の制御
    top_p=1,  # トークン選択時の確率閾値
)

# 生成されたテキストの取得
for i, choice in enumerate(response.choices):
    print(f"\nresult {i}:")
    print(choice.text.strip())