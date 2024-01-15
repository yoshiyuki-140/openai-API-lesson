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
systemRole_setting = """
"""

# ここに、AIに聞きたいことや、やってほしいことを書く
# request_script = """
# MAX SAT問題に対する局所探索を行います。
# 局所探索のアルゴリズムは、
# 「
# 1. 変数割り当てを一つランダムに選び、それにより充足される節の数を計算する。
# 2. 次にそのランダムに選ばれた数の近傍の割り当てについても、充足される府指数を計算する。
#     - ここでいう近傍とは、現在の割り当てから一つの変数の値だけを0から1へ、もしくは1から0へ反転させた割り当てで、ある.
# 3. その割りその中で現在の値よりも充足される節の数が多ければ、その中で最良の割り当てに移動する
# 4. なお今の値よりも近傍が充足する節の数が少ない場合は停止し、今の値を出力する
# 」
# です。
# これを実行して

# """

request_script = """
あなたの学習モデルのもとになったデータはいつ作られましたか？
"""

# 学習モデルの設定
model = "gpt-4"

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
