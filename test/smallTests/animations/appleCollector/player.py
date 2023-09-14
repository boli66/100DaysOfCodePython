import time

from base import Base
from consts import *

class Player(Base):
    def __init__(self):
        super().__init__()

    def jump(self,r):
        def go(func):
            for i in range(2):
                self.off(r)
                func(r)
                self.on(r)
                r.show()
                time.sleep(FRAMESPEED)

        go(self.fd)
        go(self.bk)
