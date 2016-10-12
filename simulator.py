from Memory import Memory
import sys
import struct

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
    if (cmd==1):
        flagHit=L1i.readCache(self, end)#le a cache
        #se acertar, tranquilo

        #se errar:
        if(flagHit==False):
            L1i.locateCacheBlock()#chama funcao pra localizar bloco novo
            flagHit=L2.readCache(self, end) #le segundo nivel
            if(flagHit==False): #se errar no segundoS
                L2.locateCacheBlock()

    if(cmd==2):
        flagHit=L1i.writeCache(self, end)

        if (flagHit==False):
            L1i.locateCacheBlock(self, end)
            flagHit=l2.readCache(self, end)
            if(flagHit==False):
                l2.locateCacheBlock(self, end)

            

#TODO LIST
#- DO MISS TYPE
#- DO DATA/INST
#- DO localite
#- checkout the index and tag calculous