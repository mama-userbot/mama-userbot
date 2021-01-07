from telethon.sessions import StringSession
from telethon.sync import TelegramClient

print("")
print("""Welcome To mama-userbot String Generator By @mama_bad_op""")
print("""Kindly Enter Your Details To Continue ! """)

API_KEY = input("API_KEY: ")
API_HASH = input("API_HASH: ")

while True:
    try:
        with TelegramClient(StringSession(), API_KEY, API_HASH) as client:
            print("String Sent To Your Saved Message, Store It To A Safe Place!! ")
            print("")
            session = client.session.save()
            client.send_message(
                "me",
                f"Here is your TELEGRAM STRING SESSION\n(Tap to copy it)👇 \n\n `{session}` \n\n And Visit @HellBot_Official For Any Help !",
            )

            print(
                "Thanks for Choosing mama-userbot Have A Good Time....Note That When You Terminate the Old Session ComeBack And Genrate A New String Session Old One Wont Work"
            )
    except:
        print("")
        print(
            "Wrong phone number \n make sure its with correct country code (international format). Example : +919966778833 ! Kindly Retry"
        )
        print("")
        continue
    break
