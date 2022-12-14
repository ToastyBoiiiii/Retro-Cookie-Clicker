import threading
from utils import resource_path
from sounds.soundManager import playSound


class CookieHandler:
    def __init__(self):
        self.cookies = 0
        self.cps = 0  # Cookie Per Second
        self.tempCps = 0
        self.cpc = 1  # Cookie Per Click

        self.active = False
        self.cookieEffect = 0

        self.pressed = False
        self.running = True

    def update(self, cps, cpp, cookiePressed, active, cookieEffect):

        # Set cps and cpc variables

        self.cps = cps
        self.cpc = cpp

        # Update Golden Cookie Effects

        self.active = active
        self.cookieEffect = cookieEffect

        # Check if first Golden Cookie Effect is active

        tempCookies = self.cpc

        if self.active and self.cookieEffect == 1:
            tempCookies = self.cpc * 5

        # Add CPC to Cookies when Cookie is pressed

        if cookiePressed and not self.pressed:
            playSound(resource_path("sounds/click.wav"))
            self.pressed = True
            self.cookies += tempCookies
            self.cookies = round(self.cookies, 1)
        elif not cookiePressed:
            if self.pressed:
                playSound(resource_path("sounds/unclick.wav"))
            self.pressed = False

        # Check if first Golden Cookie Effect is active

        if self.active and self.cookieEffect == 0:
            self.tempCps = self.cps * 8
        else:
            self.tempCps = self.cps

    def updateCookies(self):

        # Add Cps Variable every Second

        if self.running:
            self.cookies += self.tempCps
            self.cookies = round(self.cookies, 1)

            threading.Timer(1.0, self.updateCookies).start()

    def quit(self):

        # Stop Thread

        self.running = False
