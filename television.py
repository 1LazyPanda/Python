class Television:
    Min_Volume = 0
    Max_Volume = 2
    Min_Channel = 0
    Max_Channel = 3

    def __init__(self):
        self.__muted = False
        self.__volume = Television.Min_Volume
        self.__channel = Television.Min_Channel
        self.__status = False
        self.previous_volume = 0

    def power(self):
        self.__status = not self.__status

    def mute(self):
        self.__muted = not self.__muted

    def volume_up(self):
        if self.__status and not self.__muted:
            if self.__volume < Television.Max_Volume:
                self.__volume += 1

    def volume_down(self):
        if self.__status and not self.__muted:
            if self.__volume > Television.Min_Volume:
                self.__volume -= 1

    def channel_up(self):
        if self.__status:
            if self.__channel < Television.Max_Channel:
                self.__channel += 1
            else:
                self.__channel = Television.Min_Channel

    def channel_down(self):
        if self.__status:
            if self.__channel > Television.Min_Channel:
                self.__channel -= 1
            else:
                self.__channel = Television.Max_Channel

    def __str__(self):
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"

