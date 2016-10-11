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

    flagHit=L1i.readCache(self, end, inputNum, 0)
    if(flagHit==False):
        if(L1i.locateCacheBlock()==True):
            

