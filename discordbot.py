from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('非公式botがログインしました joined bot by system')    
    
    
# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 返る処理
    if message.content == '!p kosikisaba ip':
        await message.channel.send('・専用サバイバルサーバー
IP　　　　　 ：sugi-pellets-mc.tk
version　　　：JE1.16.1
whitelist　　  ：適用
ログイン人数：～10人
稼動　　　　：24時間')

# 返信する非同期関数を定義
async def reply(message):
    reply = f'{message.author.mention} 呼んだ？' # 返信メッセージの作成
    await message.channel.send(reply) # 返信メッセージを送信

"""メッセージ受信時に実行されるイベントハンドラ"""
@client.event # イベントを受信するための構文（デコレータ）
async def on_message(message): # イベントに対応する関数と受け取る引数
    ... # 処理いろいろ                                   
                                   
"""Bot起動時に実行されるイベントハンドラ"""
@client.event
async def on_ready():
    ...                                   
                                  
"""リアクション追加時に実行されるイベントハンドラ"""
@client.event
async def on_reaction_add(reaction, user):
    ...    
    
"""新規メンバー参加時に実行されるイベントハンドラ"""
@client.event
async def on_member_join(member):
    ...    

 """メンバーのボイスチャンネル出入り時に実行されるイベントハンドラ"""
@client.event
async def on_voice_state_update(member, before, after):
    ...                                  
                                   
                                   
                                   
 CHANNEL_ID = 711360614005473331 # 任意のチャンネルID(int)

# 任意のチャンネルで挨拶する非同期関数を定義
async def greet():
    channel = client.get_channel(CHANNEL_ID)
    await channel.send('おはよう！')

# bot起動時に実行されるイベントハンドラを定義
@client.event
async def on_ready():
    await greet() # 挨拶する非同期関数を実行
                                   
# コマンドに対応するリストデータを取得する関数を定義
def get_data(message):
    command = message.content
    data_table = {
        '!members': message.guild.members, # メンバーのリスト
        '!roles': message.guild.roles, # 役職のリスト
        '!text_channels': message.guild.text_channels, # テキストチャンネルのリスト
        '!voice_channels': message.guild.voice_channels, # ボイスチャンネルのリスト
        '!category_channels': message.guild.categories, # カテゴリチャンネルのリスト
    }
    return data_table.get(command, '無効なコマンドです')

# 発言時に実行されるイベントハンドラを定義
@client.event
async def on_message(message):
    # コマンドに対応するデータを取得して表示
    print(get_data(message))                                   
                                   
# 発言したチャンネルのカテゴリ内にチャンネルを作成する非同期関数
async def create_channel(message, channel_name):
    category_id = message.channel.category_id
    category = message.guild.get_channel(category_id)
    new_channel = await category.create_text_channel(name=channel_name)
    return new_channel

# 発言時に実行されるイベントハンドラを定義
@client.event
async def on_message(message):
    if message.content.startswith('!p tyanneru'):
        # チャンネルを作成する非同期関数を実行して Channel オブジェクトを取得
        new_channel = await create_channel(message, channel_name='new')

        # チャンネルのリンクと作成メッセージを送信
        text = f'{new_channel.mention} を作成しました'
        await message.channel.send(text)                                   
                                   
# 発言時に実行されるイベントハンドラを定義
@client.event
async def on_message(message):
    if message.content == '!p clean':
        if message.author.guild_permissions.administrator:
            await message.channel.purge()
            await message.channel.send('塵一つ残らないね！')
        else:
            await message.channel.send('何様のつもり？')   
                                   
@client.event
async def on_message(message):
    # 「おはよう」で始まるか調べる
    if message.content.startswith("おはよう"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            # メッセージを書きます
            m = "おはようございます" + message.author.name + "さん！"
            # メッセージが送られてきたチャンネルへメッセージを送ります
            await message.channel.send(m)
                                  
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
@bot.command()
async def ping(ctx):
    await ctx.send('pong')


bot.run(token)
