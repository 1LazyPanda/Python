import pytest
from television import *

class Test:
    def setup_method(self):
        self.television = Television()

    def teardown_method(self):
        del self.television

    def test_init(self):
        # Check the TV details when it is turned off
        assert self.television.__str__() == "Power = False, Channel = 0, Volume = 0"

    def test_power(self):
        # Check the TV details when it is turned on
        self.television.power()
        assert self.television.__str__() == "Power = True, Channel = 0, Volume = 0"

        # Check the TV details when it is turned off
        self.television.power()
        assert self.television.__str__() == "Power = False, Channel = 0, Volume = 0"

    def test_mute(self):
        # Power on, increase volume, mute
        self.television.power()
        self.television.volume_up()
        self.television.mute()
        assert self.television.__str__() == "Power = True, Channel = 0, Volume = 0"

        # Power on, unmute
        self.television.mute()
        assert self.television.__str__() == "Power = True, Channel = 0, Volume = 1"

        #Test when TV is off and muted (should have no effect)
        self.television.power()
        self.television.mute()
        assert self.television.__str__() == "Power = False, Channel = 0, Volume = 0"

        #Test when TV is off and unmuted (should have no effect)
        self.television.mute()
        assert self.television.__str__() == "Power = False, Channel = 0, Volume = 1"

    def test_channel_up(self):
    # Test channel up when TV is off (should have no effect)
        self.television.channel_up()
        assert self.television.__str__() == "Power = False, Channel = 0, Volume = 0"

        # Power on and increase channel
        self.television.power()
        self.television.channel_up()
        assert self.television.__str__() == "Power = True, Channel = 1, Volume = 0"

        self.television.channel_up()
        self.television.channel_up()
        assert self.television.__str__() == "Power = True, Channel = 3, Volume = 0"

        # Test channel wrapping around
        self.television.channel_up()
        assert self.television.__str__() == "Power = True, Channel = 0, Volume = 0"  # Should wrap around to 0

    def test_channel_down(self):
        # Test channel down when TV is off (should have no effect)
        self.television.channel_down()
        assert self.television.__str__() == "Power = False, Channel = 0, Volume = 0"

        # Power on and decrease channel
        self.television.power()
        self.television.channel_down()
        assert self.television.__str__() == "Power = True, Channel = 3, Volume = 0"  # Should wrap around to max channel

        self.television.channel_down()
        assert self.television.__str__() == "Power = True, Channel = 2, Volume = 0"

        self.television.channel_down()
        self.television.channel_down()
        assert self.television.__str__() == "Power = True, Channel = 0, Volume = 0"

    def test_volume_up(self):
        # Test volume up when TV is off (should have no effect)
        self.television.volume_up()
        assert self.television.__str__() == "Power = False, Channel = 0, Volume = 0"

        # Power on and increase volume
        self.television.power()
        self.television.volume_up()
        assert self.television.__str__() == "Power = True, Channel = 0, Volume = 1"

        self.television.mute()
        self.television.volume_up()
        assert self.television.__str__() == "Power = True, Channel = 0, Volume = 2"

        # Test volume at maximum (assuming max is 2)
        self.television.volume_up()
        assert self.television.__str__() == "Power = True, Channel = 0, Volume = 2"

    def test_volume_down(self):
        # Test volume down when TV is off (should have no effect)
        self.television.volume_down()
        assert self.television.__str__() == "Power = False, Channel = 0, Volume = 0"

        # Power on and decrease volume
        self.television.power()
        self.television.volume_down()
        assert self.television.__str__() == "Power = True, Channel = 0, Volume = 0"

        self.television.mute()
        self.television.volume_down()
        assert self.television.__str__() == "Power = True, Channel = 0, Volume = 0"

        # Test volume at minimum (assuming min is 0)
        self.television.volume_down()
        assert self.television.__str__() == "Power = True, Channel = 0, Volume = 0"


