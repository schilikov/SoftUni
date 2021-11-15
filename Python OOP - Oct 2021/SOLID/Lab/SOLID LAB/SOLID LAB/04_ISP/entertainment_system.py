class HDMIConnectable:
    def connect_to_device_via_hdmi_cable(self, device):
        return f"Connected {self} to {device} with HDMI"


class RCAConnectable:
    def connect_to_device_via_rca_cable(self, device):
        return f"Connected {self} to {device} with RCA"


class EthernetConnectable:
    def connect_to_device_via_ethernet_cable(self, device):
        return f"Connected {self} to {device} with Ethernet"


class PowerOutletConnectable:
    def connect_device_to_power_outlet(self, device):
        return f"Connected {device} to POWER_OUTLET"


class EntertainmentDevice(PowerOutletConnectable):
    pass


class Television(EntertainmentDevice, RCAConnectable, HDMIConnectable):
    def connect_to_dvd(self, dvd_player):
        self.connect_to_device_via_rca_cable(dvd_player)

    def connect_to_game_console(self, game_console):
        self.connect_to_device_via_hdmi_cable(game_console)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)


class DVDPlayer(EntertainmentDevice, HDMIConnectable):
    def connect_to_tv(self, television):
        self.connect_to_device_via_hdmi_cable(television)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)


class GameConsole(EntertainmentDevice, HDMIConnectable, EthernetConnectable):
    def connect_to_tv(self, television):
        self.connect_to_device_via_hdmi_cable(television)

    def connect_to_router(self, router):
        self.connect_to_device_via_ethernet_cable(router)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)


class Router(EntertainmentDevice, EthernetConnectable):
    def connect_to_tv(self, television):
        self.connect_to_device_via_ethernet_cable(television)

    def connect_to_game_console(self, game_console):
        self.connect_to_device_via_ethernet_cable(game_console)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)
