class Cache(object):
    def __init__(self, n_sets, b_size, assoc):
        self.n_sets = int(n_sets)
        self.b_size = int(b_size)
        self.assoc = int(assoc)

        #code done by kris
        self.nbits_offset=math.log2(self.b_size)
        self.nbits_indice=math.log2(self.n_sets)
        self.nbits_tag=32-self.nbits_offset-self.nbits_indice
        #

        self.n_acessos = 0
        self.n_hits = 0
        self.misses = 0
        self.misses_comp = 0
        self.misses_cap = 0
        self.misses_conf = 0

        
        self.dirt = np.ones((n_sets, assoc), dtype=np.int32)
        self.tags = np.zeros((n_sets, assoc), dtype=np.int32)

        #code done by kris
        self.val=[[]]
        for i in range (0, self.n_sets):
            self.val.append([]) # TODO for each there is a array for the associativity
        #


    def findDirect(self, end):
        """Direct mapping"""
        end = end%self.n_sets
        try:
            list(self.info[end]).index()


    ###TODO GENERAL TEST MISSES AND HITS###
    def readCache(self, end, value, level)
        #if value in self.val[end%self.n_sets][:  # TODO testa se o dado esta no vetor
        for i in range(0, n_sets):
            if (value==self.val[end%self.n_sets][i]):
                hit++; #TODO create global hit
                self.n_hits++;
                #return self.val[i][j] #TODO2 this way to return?

        else
            self.misses++ #TODO verify the miss type
            
            aux = random.randint(0, self.assoc) #TODO generate a random number to find  a place to allocate the value
            
            if (self.dirt[end%self.n_sets][aux]==1): #TODO if dirty bit is on, save its previous value in the lower memory
                #######TODO CODE TO CHECK IF THE MEMORY IS THE FIRST OR THE SECOND LEVEL#########
                #if cache is level 1 then
                if(level==1):
                
                    prevData=self.val[end%self.n_sets][aux]
                    Memory.L2.readCache(self, end, prevData, level+1) #read data from lower
                    Memory.L2.writeCache(self, end, prevData, level+1) #write previous data into lower

                else if (level==2):
                    self.misses++

            else #if dirty bit is off then
                if(level==1)   
                    Memory.L2.readCache #read from lower
                    self.dirt[end%self.n_sets][aux]==0 #mark as not dirty
                    self.val[end%self.n_sets][aux]=value
                else if (level==2)
                    self.misses++
                #TODO return value read

            
    def writeCache(self, end, value)
        for i in range(0, n_sets):
            if (value==self.val[end%self.n_sets][i]):
                hit++; #TODO create global hi t
                self.n_hits++; 
                self.val[end%self.n_sets][aux]=value #TODO if the tag is already in the cache, just update the value if necessary
                self.dirt[end%self.n_sets][aux]=1 #TODO mark dirty as 1

        else
            self.misses++ #TODO verify the miss type
            
            aux = random.randint(0, self.assoc) #TODO generate a random number to find  a place to allocate the value
            
            if self.dirt[end%self.n_sets][aux]==1: #TODO if dirty bit is on, save its previous value in the lower memory
                #######TODO CODE TO CHECK IF THE MEMORY IS THE FIRST OR THE SECOND LEVEL#########
                #if cache is level 1 then
                Memory.L2.writeCache #write previous data into lower
                Memory.L2.readCache #read data from lower

            else #if dirty bit is off then
                Memory.L2.readCache #read from lower
                self.val[end%self.n_sets][aux]=value #TODO if the tag is already in the cache, just update the value if necessary
                self.dirt[end%self.n_sets][aux]=1 #TODO mark dirty as 1

           

