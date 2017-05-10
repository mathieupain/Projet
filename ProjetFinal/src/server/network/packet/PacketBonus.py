#!/usr/bin/env python
# -*- coding: utf-8 -*-

class PacketBonus():


    def __init__(self):
        self.main = None
        self.x = 0
        self.y = 0
        self.id = 0
        self.id2 = 0
        self.type = "pose"

    def init(self, main, type, x, y, id, id2):
        self.main = main
        self.x = x
        self.y = y
        self.type = type
        self.id = id
        self.id2 = id2
        return self

    def write(self):
        if self.type == "pose":
            return self.main.protocolmap.getProtocol(self) + "#" + self.type + "#" + str(self.x) + "#" + str(self.y)
        elif self.type == "remove" or self.type == "bonus1":
            return self.main.protocolmap.getProtocol(self) + "#" + self.type + "#" + str(self.x) + "#" + str(self.y) + "#" + str(self.id) + "#" + str(self.id2)


    def read(self, main, value):
        self.main = main
        return self

    def handle(self):
        if self.type == "bonus1":
            self.main.sender.publishall(PacketBonus().init(self.main, self.type, 0, 0, self.id, self.id2))
        return self
