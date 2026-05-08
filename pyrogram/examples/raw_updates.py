from pyrogram import Client

app = Client("my_account")


@app.on_raw_update()
async def raw(client, update, users, chats):
    print(update)


app.run()
