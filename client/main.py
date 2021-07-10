import paho.mqtt.client as mqtt

BROKER = "127.0.0.1"
PORT = 1883

user = input("Username: ")

# Create client object
client = mqtt.Client(user, False)


def on_connect(client, userdata, flags, rc):
    # print('Conectado!')
    pass


def on_disconnect(client, userdata, rc=0):
    pass


def on_subscribe(client, userdata, mid, granted_qos):
    pass


def on_publish(client, userdata, mid):
    pass


def on_message(client, userdata, message):
    topics = (message.topic).split('/')
    if topics[1] != user:
        print(f'{topics[1]}: {str(message.payload.decode("utf-8"))}')


client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_publish = on_publish
client.on_subscribe = on_subscribe
client.on_message = on_message

client.connect(BROKER, PORT)
client.loop_start()
client.subscribe('chat/#')


while True:
    client.publish(f'chat/{user}', input())
