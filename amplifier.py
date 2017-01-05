import urllib
import requests
import settings


# AMPLIFIER INPUTS
SOURCE = "SOURCE"
TUNER = "TUNER"
PHONO = "PHONO"
CD = "CD"  #Alexa
DVD = "DVD"  #XBOX
HDP = "HDP"  #PS3
TV_CBL = "TV/CBL"  #Summer
SAT = "SAT"  #SAT
VCR = "VCR"  #VCR/iPod
DVR = "DVR"
AUX = "V.AUX"
NET_USB = "NET/USB"
XM = "XM"


def get_url(url, mute=False, volume=-30, source=CD, power=True, surround_mode="5/7Ch_Stereo"):
    params = {
        "setAuto": "Manual",
        "radioPower": "ON" if power else "OFF",
        "listInputFunction": source,
        "listSurrMode": surround_mode,  # this is best for
        "checkMmute": "on" if mute else "off",
        "textMas": str(volume),
        "setMas": "on",  # if you change vol, this needs to be "on" other "off"
        "checkVolLimit": "on",
        "radioVolStep": "1dB"
    }

    formatted_url = url.format(
        settings.username,
        settings.password,
        urllib.urlencode(params)
    )
    print formatted_url
    return formatted_url


def _update_room(url, source, volume, surround_mode):
    response = requests.get(get_url(
        url=url,
        source=source,
        volume=volume,
        surround_mode=surround_mode
    ))
    print response.content
    return response.status_code == 200


def update_livingroom(source, volume):
    return _update_room(
        url=settings.living_room_url,
        surround_mode="5/7Ch_Stereo",
        source=source,
        volume=volume
    )


def update_kitchen(source, volume):
    # TODO: actually has different params
    # setAuto = Manual
    # radioPower2 = ON
    # listInputFunction2 = SOURCE
    # checkMmute = off
    # textVolume2 = -26
    # setVolume2 = off
    # checkVolLimitZone2 = on

    return _update_room(
        url=settings.kitchen_url,
        surround_mode="Stereo",
        source=source,
        volume=volume
    )

# print update_livingroom(TV_CBL, -30.5)
print update_kitchen(SOURCE, -30.5)