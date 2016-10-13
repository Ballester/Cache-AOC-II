import math
import numpy as np
import random

class Cache(object):
    def __init__(self, n_sets, b_size, assoc):
        self.n_sets = int(n_sets)
        self.b_size = int(b_size)
        self.assoc = int(assoc)

        #code done by kris
        self.nbits_offset=math.log(self.b_size,2)
        self.nbits_indice=math.log(self.n_sets,2)
        self.nbits_tag=32-self.nbits_offset-self.nbits_indice
        print self.nbits_offset, self.nbits_indice, self.nbits_tag
        
        #

        self.n_acessos = 0
        self.n_hits = 0
        self.misses = 0
        self.misses_comp = False
        self.misses_cap = 0
        self.misses_conf = 0

        self.dirt = np.zeros((self.n_sets, self.assoc))
        self.tags = np.zeros((self.n_sets, self.assoc))
        
        #code done by kris
        self.val = np.zeros((self.n_sets/self.assoc, self.assoc))
        self.val.fill(-1)   


    def findDirect(self, end):
        """Direct mapping"""
        end = end%self.n_sets
        try:
            list(self.info[end]).index()
        except:
            print "couldnt map directly"

    def printBits(self):
        print(self.nbits_offset, self.nbits_indice, self.nbits_tag)


    def calculateTag(self, end):
        end=int(end/(2**(self.nbits_offset + self.nbits_indice)))
        return end

    def calculateIndex(self, end):
        end=int(end/(2**self.nbits_offset)) % self.n_sets
        return end

    ###TODO GENERAL TEST MISSES AND HITS###
    def readCache(self, end):
        #if value in self.val[end%self.n_sets]:  
        tag = self.calculateTag(end)
        index = self.calculateIndex(end)
        for i in range (0, self.assoc):
            if (tag==self.val[index][i]):
                #hit++ #TODO create global hit
                self.n_hits += 1
                print "HIT- index:", index, "i:", i, "tag: ", tag
                return True #TODO2 this way to return?
                

        else:
            print "MISS"
            self.misses += 1 #TODO verify the miss type
            return False
            
            """aux = random.randint(0, self.assoc) #TODO generate a random number to find  a place to allocate the value
            
            if (self.dirt[index][aux]==1): #TODO if dirty bit is on, save its previous value in the lower memory
                #######TODO CODE TO CHECK IF THE MEMORY IS THE FIRST OR THE SECOND LEVEL#########
                #if cache is level 1 then
                if(level==1):
                
                    prevTag=self.val[index][aux]
                    Memory.L2.readCache(self, end, prevTag, level+1) #read data from lower
                    Memory.L2.writeCache(self, end, prevTag, level+1) #write previous data into lower
                    self.dirt[index][aux]==0 #mark as not dirty
                    #self.val[end%self.n_sets][aux]=value

                elif (level==2):
                    self.misses += else

            1: #if dirty bit is off then
                if(level==1):   
                    Memory.L2.readCache() #read from lower
                    self.dirt[index][aux]==0 #mark as not dirty
                    #self.val[end%self.n_sets][aux]=value
                elif (level==2):
                    self.misses += 1
                #TODO return value read"""

            
    def writeCache(self, end):
        tag=self.calculateTag(end)
        index=self.calculateIndex(end)
        for i in range (0, self.assoc):
            if (tag==self.val[index][i]):
                self.n_hits += 1 
                self.val[index][i]=tag #TODO if the tag is already in the cache, just update the value if necessary
                self.dirt[index][i]=1 #TODO mark dirty as 1
                
                return True

        else:
            
            if (len(val[index])==self.b_size/4):
                misses_cap+=1
            elif (sel.miss_comp==False):
                misses_conf+=1
            self.miss_comp=True
            self.misses += 1 #TODO verify the miss type
            return False

            ''''
            aux = random.randint(0, self.assoc) #TODO generate a random number to find  a place to allocate the value
            
            if self.dirt[index][aux]==1: #TODO if dirty bit is on, save its previous value in the lower memory
                #######TODO CODE TO CHECK IF THE MEMORY IS THE FIRST OR THE SECOND LEVEL#########
                #if cache is level 1 then
                Memory.L2.writeCache() #write previous data into lower
                Memory.L2.readCache() #read data from lower

            else: #if dirty bit is off then
                Memory.L2.readCache #read from lower
                self.val[index][aux]=value #TODO if the tag is already in the cache, just update the value if necessary
                self.dirt[index][aux]=1 #TODO mark dirty as 1
                '''''

    
    def locateCacheBlock(self, end):
        aux = random.randint(0, self.assoc-1) #cria randomico
        
        tag = self.calculateTag(end)#calcula tag
        
        index = self.calculateIndex(end)#calcula index
        
        if (self.dirt[index][aux]==1):
            prevTag=self.val[index][aux] #
            prevIndex=(prevTag * (2**(self.nbits_offset + self.nbits_indice)))+index 
            self.dirt[index][aux]=0 #mark como nao sujo
            self.val[index][aux]=tag
            return prevIndex
        else:
            self.val[index][aux]=tag
            return -1