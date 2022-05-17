import random, schedule, time

from twilio.rest import Client
from twilio_credentials import cellphone, twilio_account, twilio_token, twilio_number

GOOD_MORNING_QUOTES = [
    "Good Friend! Hope You Have An Amazing Day💕 ",
    "Good Morning Georgous! Hope you slept well 🤎",
    "Hope you have a great day today, remeber you're doing good 🧡",
    "Good Morning, \"Always remeber you're doing good\" - Larry June🍊 "
]

GOOD_EVENING_QUOTES = [
    "Good Evening, its time for some good ole sleep 😴",
    "Sleep Tight 💕",
    "Goodnight, dont let the bed bugs bite 🪲 haha JK",
    "Love you! I hope you dream about how cool I am 😎 JK"
]


def send_message(quotes_list=GOOD_MORNING_QUOTES):

    account = twilio_account
    token = twilio_token
    client = Client(account, token)
    quote = quotes_list[random.randint(0, len(quotes_list)-1)]

    client.messages.create(to=cellphone,
                           from_=twilio_number,
                           body=quote
                           )


# send a message in the morning
schedule.every().day.at("10:50").do(send_message, GOOD_MORNING_QUOTES)

# send a message in the evening
schedule.every().day.at("20:00").do(send_message, GOOD_EVENING_QUOTES)

# testing
schedule.every().day.at("13:50").do(send_message, GOOD_EVENING_QUOTES)

while True:
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(2)

