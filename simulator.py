from Memory import Memory
import sys
import struct
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
                if end > 15 :
                    flagHit = memory.l1d.readCache(end)#le a cache
                else:
                    flagHit = memory.l1i.readCache(end)
                #se acertar, tranquilo

                #se errar:
                if(not flagHit):
                    if end>15:
                        next = memory.l1d.locateCacheBlock(end)
                    else:
                        next = memory.l1i.locateCacheBlock(end)#chama funcao pra localizar bloco novo
                    if (next != -1):
                        memory.l2.writeCache(next)
                    flagHit = memory.l2.readCache(end) #le segundo nivel
                    if(not flagHit): #se errar no segundoS
                        memory.l2.locateCacheBlock(end)

            if(cmd==1):
                if end > 15:
                    flagHit = memory.l1d.writeCache(end)
                else:
                    flagHit = memory.l1i.writeCache(end)
                if (not flagHit):
                    if end > 15:
                        next = memory.l1d.locateCacheBlock(end)
                    else:
                        next = memory.l1i.locateCacheBlock(end)
                    if(next!=-1):
                        memory.l2.writeCache(next)
                    flagHit = memory.l2.readCache(end)
                    if(not flagHit):
                        memory.l2.locateCacheBlock(end)

    print 'Misses compulsorios | Misses capacidade | Misses conflito'
    print 'Misses totais: ', tuple(memory.getMisses())
    print 'Misses l1i: ', memory.l1i.getMisses()
    print 'Misses l1d: ', memory.l1d.getMisses()
    print 'Misses l2: ', memory.l2.getMisses()
    print 'Hits totais: ', memory.getHits()
    print 'Hits l1i: ', memory.l1i.n_hits
    print 'Hits l1d: ', memory.l1d.n_hits
    print 'Hits l2: ', memory.l2.n_hits
    
    total_acessos_l1i = memory.l1i.n_hits + memory.l1i.misses
    total_acessos_l1d = memory.l1d.n_hits + memory.l1d.misses
    total_acessos_l2 = memory.l2.n_hits + memory.l2.misses
    total_acessos = total_acessos_l1i + total_acessos_l1d + total_acessos_l2
    print 'Miss ratio total: ', round((float(sum(memory.getMisses()))/float(total_acessos)), 3)   
    print 'Miss ratio l1i: ', round((float(memory.l1i.misses)/float(total_acessos_l1i)), 3)
    print 'Miss ratio l1d: ', round((float(memory.l1d.misses)/float(total_acessos_l1d)), 3)   
    print 'Miss ratio l2: ', round((float(memory.l2.misses)/float(total_acessos_l2)), 3)
    print 'Hit ratio total: ', round((float(memory.getHits())/float(total_acessos)), 3)
    print 'Hit ratio l1i: ', round((float(memory.l1i.n_hits)/float(total_acessos)), 3)
    print 'Hit ratio l2: ', round((float(memory.l2.n_hits)/float(total_acessos)), 3)
    

#TODO LIST
#- DO DATA/INST
#- DO localite
#- checkout the index and tag calculous