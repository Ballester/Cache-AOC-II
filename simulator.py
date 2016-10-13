from Memory import Memory
import sys
import struct
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    if len(sys.argv) != 9:
        raise Exception('Wrong Usage: cache_simulator <nsets_L1i> <bsize_L1i> <assoc_L1i> <nsets_L1d> <bsize_L1d> <assoc_L1d> \
            <nsets_L2>:<bsize_L2>:<assoc_L2> arquivo_de_entrada')


    memory = Memory()
    with open(sys.argv[-1]) as fid:
        tokens = []
        for line in fid:
            tokens += line

        for i in range(0, len(tokens), 8):
            end = struct.unpack('i', (tokens[i]+tokens[i+1]+tokens[i+2]+tokens[i+3])[::-1])[0]
            cmd = struct.unpack('i', (tokens[i+4]+tokens[i+5]+tokens[i+6]+tokens[i+7])[::-1])[0]
            print (end, cmd)

            #testa se e dado ou instrucao
            #testa se e leitura ou escrita
            if (cmd==0):
                flagHit = memory.l1i.readCache(end)#le a cache
                #se acertar, tranquilo

                #se errar:
                if(not flagHit):
                    next = memory.l1i.locateCacheBlock(end)#chama funcao pra localizar bloco novo
                    if (next != -1):
                        memory.l2.writeCache(next)
                    flagHit = memory.l2.readCache(end) #le segundo nivel
                    if(not flagHit): #se errar no segundoS
                        memory.l2.locateCacheBlock(end)

            if(cmd==1):
                flagHit = memory.l1i.writeCache(end)

                if (flagHit==False):
                    memory.l1i.locateCacheBlock(end)
                    flagHit = memory.l2.readCache(end)
                    if(flagHit==False):
                        memory.l2.locateCacheBlock(end)

        plt.bar(np.arange(3), memory.getMisses(), 0.35) 
        plt.show()

#TODO LIST
#- DO DATA/INST
#- DO localite
#- checkout the index and tag calculous