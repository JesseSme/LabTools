from .LabDeviceBase import LabDeviceBase

class RND320KA3005P(LabDeviceBase):
    def __init__(self, serial):
        super().__init__(serial)
        return


    def IDN(self):
        idn = None
        tries = 0
        while idn is None and tries < 10:
            idn = self.write_and_read("*IDN?")
            tries = tries + 1
            
        return idn