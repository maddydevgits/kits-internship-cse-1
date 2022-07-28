import paho.mqtt.client as mqtt

client=mqtt.Client()
client.connect('broker.hivemq.com',1883)
print('Broker Connected')
client.publish('kits/cse1','hi')
