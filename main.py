# coding:utf-8
import os  # プロキシ設定用の環境変数を設定するためにosモジュールをインポート
from openai import OpenAI  # openaiモジュールを読み込む
from local import OPENAI_API_KEY, KIT_PROXY  # 同階層にlocal.pyを作成し、その中の変数をインポート

# プロキシ設定、openaiはプロキシ用の環境変数を読み込む 
# -> 学内では必要,家でやるときは不要
os.environ['http_proxy'] = KIT_PROXY
os.environ['https_proxy'] = KIT_PROXY

# openaiにAPIキーを設定する
client = OpenAI(
    api_key=OPENAI_API_KEY
)

# ここにAIに演じてほしい役をプロンプトで設定する。
# > ここでは統計学のスペシャリストとして設定している
sysemRole_setting = """
あなたは統計学のスペシャリストです。
"""

# ここに、AIに聞きたいことや、やってほしいことを書く
request_script = """
有意水準とは何か、200文字程度で説明しなさい。
"""

# 学習モデルの設定
model = "gpt-4"

# 設定の読み込み
completion = client.chat.completions.create(
    model=model,  # 学習モデルを設定する
    messages=[
        # GPT-4がどんな役回りか設定できる ->  例:"あなたは統計学のスペシャリストです！"
        {"role": "system", "content": sysemRole_setting},
        # GPT-4に投げかける質問を設定する -> 例:"優位水準とはなんですか？"
        {"role": "user", "content": request_script}
    ]
)

response_script = completion.choices[0].message.content

# 同階層の'resulet.txt'ファイルに結果を出力
with open('./result.txt', encoding="UTF-8", mode="w") as f:
    f.write(response_script)
