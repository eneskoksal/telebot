import subprocess
import time
import telepot

def wake(pswd):
    subprocess.call(f'echo {pswd} | sudo etherwake 4C:CC:6A:68:3E:BA')
    
def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print('Got command: %s' % command)

    if command == 'awake':
       bot.sendMessage(chat_id, wake)

bot = telepot.Bot('5244902840:AAFt5PuKEDiubfANH56IOIwZzSIvrmeU9kI')
bot.message_loop(handle)
print('I am listening...')

while 1:
    try:
        time.sleep(10)
    
    except KeyboardInterrupt:
        print('\n Program interrupted')
        exit()
        
    except:
        print('Other error or exception occured!')