import time
from Packages.RNDCommands import CommandList
from Packages.LabDevice import DeviceLimitList

class LabDeviceBase:

    def __init__(self, serial):
        self.com = serial
        self.id = self.IDN()
        self.port = self.com.port
        # self.get_commands()
        # self.get_device_limits()

        # Read device id
        # Set device id as name
        # Fetch instructions available for device
        # Add those instructions as functions in this class
        return
    
    # def add_instruction(self, instr_name, method):
    #     setattr(self, instr_name, method)
        # self.instr_name = method
    def get_commands(self):
        for key in CommandList.DEVICE_CMD_SETS:
            if key in self.id:
                self.commands = list(CommandList.DEVICE_CMD_SETS[key])
                break
            
    def get_device_limits(self):
        for key in CommandList.DEVICE_CMD_SETS:
            if key in self.id:
                self.limits = list(DeviceLimitList.DEVICE_LIMITS_LIST[key])
                break
            
    
    def write_and_read(self, data, delay=0.1):
        out = ""
        self.com.write(data.encode())

        time.sleep(delay)

        while self.com.in_waiting > 0:
            out += self.com.read(1).decode("latin-1")
        
        if out != "":
            return out
        return None
    
    def write_and_check(self, data, check, delay=0.1):
        out = ""
        self.com.write(data.encode())
        
        time.sleep(delay)
        
        self.com.write(check.encode())
        
        time.sleep(delay)
        while self.com.in_waiting > 0:
            out += self.com.read(1).decode("latin-1")
        
        if out != "":
            return out
        return None
