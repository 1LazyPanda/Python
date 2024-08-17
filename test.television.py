import pytest
from television import *

class Test:
    def setup_method(self):
        self.television = Television()

    def teardown_method(self):
        del self.television

    def test_init(self):
        # Check initial values
        assert str(self.television) == "Power = False, Channel = 0, Volume = 0"

    def test_power(self):
        # Check the TV details when it is turned on
        self.television.power()
        assert str(self.television) == "Power = True, Channel = 0, Volume = 0"

        # Check the TV details when it is turned off
        self.television.power()
        assert str(self.television) == "Power = False, Channel = 0, Volume = 0"

    def test_mute(self):
        # Test mute when TV is off (should have no effect)
        self.television.mute()
        assert str(self.television) == "Power = False, Channel = 0, Volume = 0"

        # Power on, increase volume, mute
        self.television.power()
        self.television.volume_up()
        self.television.mute()
        assert str(self.television) == "Power = True, Channel = 0, Volume = 1 (Muted)"

        # Unmute
        self.television.mute()
        assert str(self.television) == "Power = True, Channel = 0, Volume = 1"

    def test_channel_up(self):
        # Test channel up when TV is off (should have no effect)
        self.television.channel_up()
        assert str(self.television) == "Power = False, Channel = 0, Volume = 0"

        # Power on and increase channel
        self.television.power()
        self.television.channel_up()
        assert str(self.television) == "Power = True, Channel = 1, Volume = 0"

        # Test channel wrapping around the maximum value
        # Assuming the maximum channel is 10 for example
        for _ in range(10):
            self.television.channel_up()
        assert str(self.television) == "Power = True, Channel = 0, Volume = 0"

    def test_channel_down(self):
        # Test channel down when TV is off (should have no effect)
        self.television.channel_down()
        assert str(self.television) == "Power = False, Channel = 0, Volume = 0"

        # Power on and decrease channel
        self.television.power()
        self.television.channel_down()
        assert str(self.television) == "Power = True, Channel = 9, Volume = 0"  # Assuming 0 wraps to max

        # Test channel wrapping around the minimum value
        for volume in range(0, 3):
            self.television.channel_down()
        assert str(self.television) == "Power = True, Channel = 9, Volume = 0"

    def test_volume_up(self):
        # Test volume up when TV is off (should have no effect)
        self.television.volume_up()
        assert str(self.television) == "Power = False, Channel = 0, Volume = 0"

        # Power on and increase volume
        self.television.power()
        self.television.volume_up()
        assert str(self.television) == "Power = True, Channel = 0, Volume = 1"

        # Test volume at maximum (assuming max is 10)
        for volume in range(3):
            self.television.volume_up()
        self.television.volume_up()
        assert str(self.television) == "Power = True, Channel = 0, Volume = 10"

    def test_volume_down(self):
        # Test volume down when TV is off (should have no effect)
        self.television.volume_down()
        assert str(self.television) == "Power = False, Channel = 0, Volume = 0"

        # Power on and decrease volume
        self.television.power()
        self.television.volume_down()
        assert str(self.television) == "Power = True, Channel = 0, Volume = 0"

        # Test volume at minimum
        self.television.volume_up()
        self.television.volume_down()
        assert str(self.television) == "Power = True, Channel = 0, Volume = 0"
