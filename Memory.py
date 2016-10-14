import sys
from Cache import Cache
import numpy as np

class Memory(object):
    def __init__(self):
        self.n_writes = 0
        self.n_reads = 0

        """Get flags from command line"""
        l1i_flags = sys.argv[1:4]
        l1d_flags = sys.argv[4:7]
        l2_flags = sys.argv[7].split(':')

        """Instantiate Caches"""
        self.l1i = Cache(l1i_flags[0], l1i_flags[1], l1i_flags[2])
        self.l1d = Cache(l1d_flags[0], l1d_flags[1], l1d_flags[2])
        self.l2 = Cache(l2_flags[0], l2_flags[1], l2_flags[2])

    def read(self, end):
        self.l1i.findDirect(end)

    def write(self, end):
        pass

    def printB(self):
        self.l1i.printBits()
        
    def getMisses(self):
        misses = np.array(self.l1i.getMisses())
        misses += np.array(self.l1d.getMisses())
        misses += np.array(self.l2.getMisses())
        return misses
        
    def getHits(self):
        return self.l1i.n_hits + self.l1d.n_hits + self.l2.n_hits

    def getWriteMiss(self):
        return (self.l1i.getWriteMiss(), self.l1d.getWriteMiss(), self.l2.getWriteMiss())
       
        
    