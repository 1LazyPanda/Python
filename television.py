class Television:
    Min_Volume = 0
    Max_Volume = 2
    Min_Channel = 0
    Max_Channel = 3

    def __init__(self) -> None:
        """
        Initializes a new instance of the Television class.

        This method initializes the private instance variables:
            - __muted: a boolean that tracks if the TV is muted
            - __volume: an integer that tracks the current volume level
            - __channel: an integer that tracks the current channel
            - __status: a boolean that tracks if the TV is on or off
            - previous_volume: an integer that tracks the previous volume level

        Args:
            None

        Returns:
            None
        """
        self.__muted: bool = False  # tracks if the TV is muted
        self.__volume: int = Television.Min_Volume  # tracks the current volume level
        self.__channel: int = Television.Min_Channel  # tracks the current channel
        self.__status: bool = False  # tracks if the TV is on or off
        self.previous_volume: int = 0  # tracks the previous volume level

    def power(self) -> None:
        """
        Toggles the power status of the Television.

        This method toggles the value of the private instance variable __status,
        which tracks if the TV is on or off. If the TV is turned off, it will be
        turned on. If the TV is turned on, it will be turned off.

        Args:
            None

        Returns:
            None
        """
        # Toggles the power status of the Television.
        # If the TV is turned off, it will be turned on.
        # If the TV is turned on, it will be turned off.
        #
        # Args:
        #     None
        #
        # Returns:
        #     None
        self.__status = not self.__status

    def mute(self) -> None:
        """
        Toggles the muted status of the Television.

        This method toggles the value of the private instance variable __muted,
        which tracks if the TV is muted. If the TV is not muted, it will be
        muted. If the TV is muted, it will be unmuted.

        Args:
            None

        Returns:
            None
        """
        # Toggles the muted status of the Television.
        # If the TV is not muted, it will be muted.
        # If the TV is muted, it will be unmuted.
        self.__muted = not self.__muted  # Toggle the muted status of the Television

    def volume_up(self) -> None:
        """
        Increases the volume of the Television.

        This method checks if the TV is on and not muted. If both conditions are true,
        it checks if the volume is not at the maximum level. If all conditions are met,
        it increases the volume by 1.

        Args:
            None

        Returns:
            None
        """
        # Increase the volume of the Television if TV is on and not muted
        # and volume is not at the maximum level
        #
        # Args:
        #     None
        #
        # Returns:
        #     None
        if self.__status and not self.__muted:  # Check if TV is on and not muted
            if self.__volume < Television.Max_Volume:  # Check if volume is not at the maximum level
                self.__volume += 1  # Increase the volume by 1

    def volume_down(self) -> None:
        """
        Decreases the volume of the Television.

        If the TV is on and not muted, it checks if the volume is not at the minimum level.
        If all conditions are met, it decreases the volume by 1.

        Args:
            None

        Returns:
            None
        """
        # Check if TV is on and not muted
        if self.__status:
            self.__muted
            # Check if volume is not at the minimum level
            if self.__volume > Television.Min_Volume:
                # Decrease the volume by 1
                self.__volume -= 1

    def channel_up(self) -> None:
        """
        Increases the channel of the Television.

        If the TV is on, it checks if the channel is not at the maximum level.
        If all conditions are met, it increases the channel by 1.

        Args:
            self: The Television object.

        Returns:
            None
        """
        # Check if the TV is on
        if self.__status:
            # Check if the channel is not at the maximum level
            if self.__channel < Television.Max_Channel:
                # Increase the channel by 1
                self.__channel += 1

    def channel_down(self) -> None:
        """
        Decreases the channel of the Television.

        If the TV is on, it checks if the channel is not at the minimum level.
        If all conditions are met, it decreases the channel by 1. If the channel
        is at the minimum level, it sets the channel to the maximum level.

        Args:
            self (Television): The Television object.

        Returns:
            None
        """
        # Check if the TV is on
        if self.__status:
            # Check if the channel is not at the minimum level
            if self.__channel > Television.Min_Channel:
                # Decrease the channel by 1
                self.__channel -= 1
            else:
                # If at the minimum level, set channel to the maximum level
                self.__channel = Television.Max_Channel

    def __str__(self) -> str:
        if self.__muted:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.Min_Volume}"
        else:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"

