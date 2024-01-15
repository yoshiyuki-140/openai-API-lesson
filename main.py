# coding:utf-8
import os  # プロキシ設定用の環境変数を設定するためにosモジュールをインポート
from openai import OpenAI  # openaiモジュールを読み込む
from local import OPENAI_API_KEY, KIT_PROXY  # 同階層にlocal.pyを作成し、その中の変数をインポート

# プロキシ設定、openaiはプロキシ用の環境変数を読み込む 
# -> 学内では必要,家でやるときは不要
# os.environ['http_proxy'] = KIT_PROXY
# os.environ['https_proxy'] = KIT_PROXY

# openaiにAPIキーを設定する
client = OpenAI(
    api_key=OPENAI_API_KEY
)

# ここにAIに演じてほしい役をプロンプトで設定する。
# > ここでは統計学のスペシャリストとして設定している
systemRole_setting = """
"""

# ここに、AIに聞きたいことや、やってほしいことを書く
request_script = """
MAX SAT問題に対する局所探索を行います。

"""

# 学習モデルの設定
model = "gpt-3.5-turbo-16k"

# 設定の読み込み
completion = client.chat.completions.create(
    model=model,  # 学習モデルを設定する
    messages=[
        {"role": "system", "content": systemRole_setting},
        {"role": "user", "content": request_script},
    ]
)

# レスポンスを格納
response_script = completion.choices[0].message.content

# 同階層の'resulet.txt'ファイルに結果を出力
with open('./result.txt', encoding="UTF-8", mode="w") as f:
    f.write(response_script)
