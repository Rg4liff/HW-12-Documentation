import pytest
from television import *

def test_init_state():
    tv = Television()
    assert str(tv) == "Power - False, Channel - 0, Volume - 0"

def test_power_switch():
    tv = Television()
    tv.power()
    assert str(tv) == "Power - True, Channel - 0, Volume - 0"
    tv.power()
    assert str(tv) == "Power - False, Channel - 0, Volume - 0"


def test_set_volume():
    tv = Television()

    # checks that volume does not go up when power is false
    tv.volume_up()
    assert str(tv) == "Power - False, Channel - 0, Volume - 0"
    tv.volume_down()
    assert str(tv) == "Power - False, Channel - 0, Volume - 0"

    # Checks volume goes up and stays at 2
    tv.power()
    tv.volume_up()
    assert str(tv) == "Power - True, Channel - 0, Volume - 1"
    tv.volume_up()
    assert str(tv) == "Power - True, Channel - 0, Volume - 2"
    tv.volume_up()
    assert str(tv) == "Power - True, Channel - 0, Volume - 2"

    # Checks if volume down works and stays at 0
    tv.volume_down()
    assert str(tv) == "Power - True, Channel - 0, Volume - 1"
    tv.volume_down()
    assert str(tv) == "Power - True, Channel - 0, Volume - 0"
    tv.volume_down()
    assert str(tv) == "Power - True, Channel - 0, Volume - 0"

def test_set_channel():
    tv = Television()

    # checks that channel does not go up when power is false
    tv.channel_up()
    assert str(tv) == "Power - False, Channel - 0, Volume - 0"
    tv.channel_down()
    assert str(tv) == "Power - False, Channel - 0, Volume - 0"

    # Checks channel goes up and resets to 0
    tv.power()
    tv.channel_up()
    assert str(tv) == "Power - True, Channel - 1, Volume - 0"
    tv.channel_up()
    assert str(tv) == "Power - True, Channel - 2, Volume - 0"
    tv.channel_up()
    assert str(tv) == "Power - True, Channel - 3, Volume - 0"
    tv.channel_up()
    assert str(tv) == "Power - True, Channel - 0, Volume - 0"

    # Checks if volume down works and resets to 3
    tv.channel_down()
    assert str(tv) == "Power - True, Channel - 3, Volume - 0"
    tv.channel_down()
    assert str(tv) == "Power - True, Channel - 2, Volume - 0"
    tv.channel_down()
    assert str(tv) == "Power - True, Channel - 1, Volume - 0"
    tv.channel_down()
    assert str(tv) == "Power - True, Channel - 0, Volume - 0"


def test_mute():
    tv = Television()
    # Checks if mute is ignored when powere is off
    tv.mute()
    assert str(tv) == "Power - False, Channel - 0, Volume - 0"

    # Checks mute on and off function, setting volume to 0 and back to pre mute settings
    tv.power()
    tv.volume_up()
    assert str(tv) == "Power - True, Channel - 0, Volume - 1"
    tv.mute()
    assert str(tv) == "Power - True, Channel - 0, Volume - 0"
    tv.mute()
    assert str(tv) == "Power - True, Channel - 0, Volume - 1"

    # Checks if mute is on, then volume is called, is unmuted and volume changes
    assert str(tv) == "Power - True, Channel - 0, Volume - 1"
    tv.mute()
    tv.volume_up()
    assert str(tv) == "Power - True, Channel - 0, Volume - 2"
    tv.mute()
    tv.volume_down()
    assert str(tv) == "Power - True, Channel - 0, Volume - 1"



