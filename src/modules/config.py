import os

class Config:
    BUTTON_WIDTH = 25
    BUTTON_HEIGHT = 1
    BUTTON_SIZE = (int(BUTTON_WIDTH), int(BUTTON_HEIGHT))
    PNL_MAIN_HEIGHT = 8 
    PNL_BORDER_HEIGHT = 2
    PNL_BORDER_WIDTH = 2
    Size = os.get_terminal_size()
    APP_NAME = "Talkye"
    APP_VERSION = "0.1"
    APP_RELEASE_DATE = "2023-12-31"

    RECEIVER_HEIGHT = Size.lines - PNL_BORDER_HEIGHT - PNL_MAIN_HEIGHT - 1
    SIDEBAR_WIDTH = 20