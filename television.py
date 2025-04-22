class Television:
    """
    A class representing a Television remote control
    """
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        """
        Initialize the Television object with TV off,
        not muted and min volume and channel
        """
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL

    def power(self) -> None:
        """
        Turns the television on and off using __status
        variable to store bool
        :return: None
        """
        if self.__status:
            self.__status = False
        else:
            self.__status = True

    def mute(self) -> None:
        """
        Mutes and unmutes the television using __muted variable to store bool
        :return: None
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            else:
                self.__muted = True

    def channel_up(self) -> None:
        """
        Raises the channel up using __channel variable to store channel number
        :return: None
        """
        if self.__status:
            if self.__channel != self.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = self.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        Lowers the channel down using __channel variable to store channel number
        :return: None
        """
        if self.__status:
            if self.__channel != self.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = self.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Raises the volume up using __volume variable to store volume number
        :return: None
        """
        if self.__status:
            if self.__volume != self.MAX_VOLUME:
                self.__muted = False
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Lowers the volume down using __volume to store volume number
        :return: None
        """
        if self.__status:
            if self.__volume != self.MIN_VOLUME:
                self.__muted = False
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Overloads Print function for printing status of Television
        :return: Power(T/F), Channel(int), Volume(int)
        """
        if self.__muted:
            return f'Power - {self.__status}, Channel - {self.__channel}, Volume - 0'
        else:
            return f'Power - {self.__status}, Channel - {self.__channel}, Volume - {self.__volume}'