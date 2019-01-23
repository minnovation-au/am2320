#### Example Usage of AM2320 Library for AlphaX X1 TM #####
#### Note: Can be modified for usage in AlphaX Machine Health Monitor ####

def readSensor():
    sensorOn = machine.Pin('P11', mode=machine.Pin.OUT)
    sensorOn(1)

    i2c = I2C(0, I2C.MASTER)
    i2c = I2C(0, pins=('P10','P9'))
    am = am2320.AM2320(i2c)

    while True:
        try:
            temp = am.temperature
            hum = am.relative_humidity        
            break
        except Exception as e:
            # These sensors are a bit flakey, its ok if the readings fail
            pass

    sensorOn.value(0)

    return([temp,hum])
