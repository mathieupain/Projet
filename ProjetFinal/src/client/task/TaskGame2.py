# coding=utf-8
'''
Created on 5 févr. 2017

@author: mathi
'''
import threading
import time
from tkinter import *


class TaskGame2(threading.Thread):
    # ~ Initialisation
    def __init__(self, threadID, name, main, PacketWin):
        threading.Thread.__init__(self)
        self.PacketWin = PacketWin
        self.main = main
        self.threadID = threadID
        self.name = name
        self.personne = None
        self.count = 0
        self.timer = 0

    # ~ Fonction run de la thread
    def run(self):
        time.sleep(1)
        while (self.main.running and self.main.ingame):
            time.sleep(0.1)
            if (self.timer != -1):
                self.timer += 1
                self.main.writeText(650, 10, str(60*5-int(self.timer/10)), self.main.fenetregame.canvas, True, 10)
            if (self.timer > 10 * 60 * 5):
                self.main.sender.publish(self.PacketWin().init(self.main, "hider"))
                self.timer = -1
            if (self.count >= 5 * 10):
                self.main.sender.publish(self.PacketWin().init(self.main, "finder"))
                self.count = -1

            if (self.personne in self.main.fenetregame.findlist and self.count != -1):
                self.count += 1
            elif (len(self.main.fenetregame.findlist) != 0):
                if (self.main.fenetregame.other[self.main.fenetregame.findlist[0]][4] == 1):
                    self.personne = self.main.fenetregame.findlist[0]
                    self.count = 0
            else:
                self.count = 0
                self.personne = 0
