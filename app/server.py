# Fast-API立ち上げ

from threading import Thread   # スレッド作成のための標準ライブラリ
from fastapi import FastAPI   # APIサーバを作成するためのフレームワーク
import uvicorn   # FastAPIアプリケーションを実行するために使用


# FastAPIアプリケーションの設定
app = FastAPI() # アプリケーションインスタンスを作成

@app.get("/")   # ルートエンドポイントの定義
async def root():
    return {"message": "The server is up!"}

# サーバの起動
def start():
    uvicorn.run(app, host="0.0.0.0", port=8080)

# サーバを別スレッドで実行
def server_thread():
    t = Thread(target=start)
    t.start()