import asyncio
import guilded

async def send_messages():
    email = input("Enter your Guilded email: ")
    password = input("Enter your Guilded password: ")
    team_name = input("Enter the name of your team: ")
    channel_name = input("Enter the name of the channel: ")
    message_content = input("Enter the message content: ")
    num_messages = int(input("Enter the number of messages to send: "))
    delay_seconds = float(input("Enter the delay in seconds between each message: "))

    client = guilded.Client()
    await client.login(email, password)

    team = client.teams.find(team_name)
    channel = team.channels.find(channel_name)

    for _ in range(num_messages):
        message = await channel.send(message_content)
        print(f"Message sent: {message.content}")
        await asyncio.sleep(delay_seconds)

    await client.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(send_messages())
