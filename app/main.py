import discord  # Pycordを読み込む(pip install py-cord)
import dotenv
import os
from server import server_thread

# .envファイルの内容を読み込む
dotenv.load_dotenv()

# TOKENの読み込み
TOKEN = os.environ.get('TOKEN')

# botの元オブジェクトを生成
bot = discord.Bot(
    intents=discord.Intents.all()   # すべてのコンテンツを利用できるように
)


"""
# 起動時に自動的に動くメソッド
@bot.event
async def on_ready():
    print("起動完了")  # 起動すると実行したターミナルに"起動完了"と表示される

# メッセージが投稿された時に動くメソッド
@bot.event
async def on_message(message: discord.Message):
    # メッセージ送信者がbotであれば無視する
    if message.author.bot:
        return
    # メッセージが"こんにちは"なら、"やぁ！"と返信する
    if message.content == "こんにちは":
        await message.reply("やぁ！")

# /コマンドを実装
@client.command(name="test", description="テスト")
async def test(ctx: discord.ApplicationContext):
    await ctx.respond("てすとてすと")


# テーマを保存するためのtheme_title変数を用意
theme_title = None
"""

# テーマを保存
@bot.command(name="post", description="ボットにテーマを保存")
async def post(ctx: discord.ApplicationContext, theme: str):
    global theme_title
    theme_title = theme
    await ctx.respond(f"テーマ`{theme}`を保存したよ！")

# テーマを取得
@bot.command(name="get", description="ボットからテーマを取得")
async def get(ctx: discord.ApplicationContext):
    global theme_title
    await ctx.respond(f"今週のテーマは`{theme_title}`だよ！")

# テーマの確認
@bot.command(name="check", description="テーマの確認")
async def check(ctx: discord.ApplicationContext):
    if theme_title is not None:
        await ctx.respond(f"今のテーマは`{theme_title}`だよ！")
    else:
        await ctx.respond("まだテーマが設定されていないよ！")

# koyeb用サーバ立ち上げ
server_thread()

# Discord botを実行
bot.run(TOKEN)
