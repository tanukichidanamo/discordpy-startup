# インストールした discord.py を読み込む
import discord

# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'NzEzMzM5OTAwMjgzMzIyNDU4.Xsj5Ug.fzF-rDMAmDe-dH6R29394CDA65Q'

# 接続に必要なオブジェクトを生成
client = discord.Client()

CHANNEL_ID =711234511710715924

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしただなも')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == 'たぬきち':
        await message.channel.send('テスト中だなも～')
		
# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)