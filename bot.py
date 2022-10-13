import discord
import responses

async def send_message(message, user_message, is_private):

    try:
        if user_message[0] == '!':
            response = '```' + responses.handle_response(user_message)  +'```'
        elif user_message[0] == '$':
            response = '```' + responses.handle_response2(user_message)  +'```'
        elif user_message[0] == '#':
            response = '```' + responses.handle_response3(user_message)  +'```'
        elif user_message[0] == '^':
            response = '```' + responses.handle_response4(user_message)  +'```'

        await message.author.send(response) if is_private else await message.channel.send(response)
    
    except Exception as e:
        print(e)

def run_discord_bot():
    TOKEN = 'MTAyOTYxMTY5NDE4NTUzMzQ2MQ.Gds49X.oJZBks1Rl8VGDtisbGWguqf2DUHVwqaNJxSW0M'
    intents = discord.Intents.default()
    intents.message_content = True

    client = discord.Client(intents=intents)


    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):


        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: {user_message} ({channel})')

        if user_message[0] == '!':
            await send_message(message, user_message, is_private=False)
        elif user_message[0] == '$':
            await send_message(message, user_message, is_private=False)
        elif user_message[0] == '#':
            await send_message(message, user_message, is_private=False)
        elif user_message[0] == '^':
            await send_message(message, user_message, is_private=False)



    
    client.run(TOKEN)