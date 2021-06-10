import wiotp.sdk.device
import time
import random
myConfig = { 
    "identity": {
        "orgId": "9jqvyj",
        "typeId": "ESP32",
        "deviceId":"12345"
    },
    "auth": {
        "token": "98765432"
    }
}

def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    m=cmd.data['command']

client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

while True:
   
    air=random.randint(0,50)
    myData={'air_quality':air}
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
    print("Published data Successfully: %s", myData)
    client.commandCallback = myCommandCallback
    time.sleep(2)
client.disconnect()

