import usb.core
from time import sleep

DELAY = 0.01

class rocket:
    def __init__(self):
        self.connect()

    def connect(self):
        self.r = usb.core.find(idVendor=0x2123, idProduct=0x1010)
        self.r.set_configuration()

    def up(self, seconds=DELAY):
        self.r.ctrl_transfer(0x21,0x09,0,0,[0x02,0x02,0x00,0x00,0x00,0x00,0x00,0x00]) 
        if seconds > 0: 
            sleep(seconds)
            self.stop()

    def down(self, seconds=DELAY):
        self.r.ctrl_transfer(0x21,0x09,0,0,[0x02,0x01,0x00,0x00,0x00,0x00,0x00,0x00])
        if seconds > 0:
            sleep(seconds)
            self.stop()

    def left(self, seconds=DELAY):
        self.r.ctrl_transfer(0x21,0x09,0,0,[0x02,0x04,0x00,0x00,0x00,0x00,0x00,0x00])
        if seconds > 0:
            sleep(seconds)
            self.stop()

    def right(self, seconds=DELAY):
        self.r.ctrl_transfer(0x21,0x09,0,0,[0x02,0x08,0x00,0x00,0x00,0x00,0x00,0x00])
        if seconds > 0:
            sleep(seconds)
            self.stop()

    def stop(self):
        self.r.ctrl_transfer(0x21,0x09,0,0,[0x02,0x20,0x00,0x00,0x00,0x00,0x00,0x00])

    def fire(self):
        self.r.ctrl_transfer(0x21,0x09,0,0,[0x02,0x10,0x00,0x00,0x00,0x00,0x00,0x00])
        sleep(4)

    @staticmethod
    def demo():
        r = rocket()
        r.connect()
        r.up(2)
        r.fire()
        r.left(2)
        r.fire()
        r.right(2)
        r.fire()
        r.down(2)
        r.fire()
        r.up(2)

rocket.demo()
