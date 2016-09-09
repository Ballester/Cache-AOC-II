class Cache(object):
    def __init__(self, n_sets, b_size, assoc):
        self.n_sets = int(n_sets)
        self.b_size = int(b_size)
        self.assoc = int(assoc)

        self.n_acessos = 0
        self.n_hits = 0
        self.misses = 0
        self.misses_comp = 0
        self.misses_cap = 0
        self.misses_conf = 0

        
        self.dirt = np.ones((n_sets, assoc), dtype=np.int32)
        self.tags = np.zeros((n_sets, assoc), dtype=np.int32)

    def findDirect(self, end):
        """Direct mapping"""
        end = end%self.n_sets
        try:
            list(self.info[end]).index()
