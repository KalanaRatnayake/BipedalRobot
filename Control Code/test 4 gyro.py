import smbus
import math

# Power management registers
power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c

bus = smbus.SMBus(0) # or bus = smbus.SMBus(1) for Revision 2 boards

def read_byte(adr):
    return bus.read_byte_data(address, adr)

def read_word(adr):
    high = bus.read_byte_data(address, adr)
    low = bus.read_byte_data(address, adr+1)
    val = (high << 8) + low
    return val

def read_word_2c(adr):
    val = read_word(adr)
    if (val >= 0x8000):
        return -((65535 - val) + 1)
    else:
        return val

def dist(a,b):
    return math.sqrt((a*a)+(b*b))

def get_y_rotation(x,y,z):
    radians = math.atan2(x, dist(y,z))
    return -math.degrees(radians)

def get_x_rotation(x,y,z):
    radians = math.atan2(y, dist(x,z))
    return math.degrees(radians)

def leftFoot_Y_Angle():
    bus.write_byte_data(0x68, power_mgmt_1, 0)
    return read_word_2c(0x45) #returns the angle of rotation around y axiss of ankle

def rightFoot_Y_Angle():
    bus.write_byte_data(0x69, power_mgmt_1, 0)
    return read_word_2c(0x45) #returns the angle of rotation around y axiss of ankle


print leftFoot_Y_Angle
