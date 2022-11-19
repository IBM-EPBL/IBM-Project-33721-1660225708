import json
import wiotp.sdk.device
import time


myConfig={
    "identity":{
        "orgId":"h2xjhq",
        "typeId":"NodeMCU",
        "deviceId":"12345"
    },
    "auth":{
        "token":"12345678"
    }
}
client = wiotp.sdk.device.DeviceClient(config=myConfig,logHandlers=None)
client.connect()

while True:
    name="Child"
    #in area location
    # latitude=17.4225176
    # longitude=78.5458842

    #out area location -- TCE LOCATION
    latitude= 9.882190226007319
    longitude= 78.08165482089441

    
    myData={'name':name,'lat':latitude,'lon':longitude}
    client.publishEvent(eventId="status",msgFormat="json",data=myData,qos=0,onPublish=None)
    print("Data published to IBM IoT platform",myData)
    time.sleep(5)
    
client.disconnect()
