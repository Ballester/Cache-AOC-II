import sys
from Cache import Cache

class Memory(object):
    def __init__(self):
        self.n_writes = 0
        self.n_reads = 0

        """Get flags from command line"""
        l1i_flags = sys.argv[1:4]
        l1d_flags = sys.argv[4:7]
        l2_flags = sys.argv[7].split(':')

        """Instantiate Caches"""
        self.L1i = Cache(l1i_flags[0], l1i_flags[1], l1i_flags[2])
        self.L1d = Cache(l1d_flags[0], l1d_flags[1], l1d_flags[2])
        self.L2 = Cache(l2_flags[0], l2_flags[1], l2_flags[2])

    def read(self, end):
        self.L1i.findDirect(end)

    def write(self, end):
        pass
