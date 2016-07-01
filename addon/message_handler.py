class MessageHandler(object):

    def __init__(self, filter):
        self.filter = filter

    def handle(self, message):
        print("Received message: " + str(message))

class PrettyMessagePrint(MessageHandler):

    def handle(self, message):
        for i in range(len(message)):
            if 'data' in message[i] and \
                    'subject' in message[i]['data']:
                if 'name' in message[i]['data']['subject'] and \
                        'text' in message[i]['data']['subject']:
                    sender = message[i]['data']['subject']['name']
                    text = message[0]['data']['subject']['text']
                    print(sender + ": " + text)

class Echo(MessageHandler):

    def __init__(self, bot):
        self.last_sent = 0
        self.bot = bot

    def handle(self, message):
        for i in range(len(message)):
            if 'data' in message[i] and \
                            'subject' in message[i]['data']:
                if 'name' in message[i]['data']['subject'] and \
                                'text' in message[i]['data']['subject']:
                    sender = message[i]['data']['subject']['name']
                    if not sender == self.bot.name:
                        text = message[0]['data']['subject']['text']
                        self.bot.say(text)