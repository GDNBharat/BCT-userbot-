import os

os.system("pip3 install tgcrypto pyrogram")
os.system("clear")
from pyrogram import Client

# guide them

intro = """
@sinnalu Corporation
Get the following values by logging to,

https://my.telegram.org

Required:
  
  1. API_ID
  2. API_HASH
  3. PHONE NUMBER (WITH COUNTRY CODE)
  
"""


print(intro)


API_ID = input("\nEnter your API_ID: ")

while not (API_ID.isdigit() and len(API_ID) == 7):
    print("\n\nPlease enter a 7 digit API_ID.\n\n")
    API_ID = input("Enter your API_ID (1234567): ")


# hexadecimal number
API_HASH = input("\nEnter API HASH: ")


# create a new pyrogram session
with Client("in_memory=True", api_id=int(API_ID), api_hash=API_HASH) as app:
    app.send_message(
        "me",
        f"This Is Your Chinnaop Userbot • [ `SESSION` ]\n\n```{app.export_session_string()}```\n\n⚠️• Don't share this with anyone !!\n\nCreate Again •)",
        disable_web_page_preview=True,
    )
    print(
        "Your String Session Is Successfully Saved In Telegram Saved (Cloud) Messages !! Don't Share It With Anyone!! Anyone having your session can use (hack) your telegram account !"
    )
