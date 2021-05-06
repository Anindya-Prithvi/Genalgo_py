#break SHA with gen algo?
#current optimum pool is 1000 for
##a= Genalgo("Aifjtt14htfu8")
##import time
##while True:
##	a.gen_progress()
##	time.sleep(0.2)

import hashlib,secrets,random


def hashing_md5(string):
    result = hashlib.md5(string.encode)
    return result.hexdigest()

class Genalgo:
    def __init__(self,init_pool_size,target):
        self.pool_size=init_pool_size
        self.pool=[]
        self.target=target
        #generate pool here
        for i in range(self.pool_size):
            self.pool.append(self.pool_gen(len(target)))


    def gen_progress(self):
        #progresses with new generation. Changes self.pool with new pool
        #replication function
        a=len(self.pool)
        for i in range(a):
            for j in range(self.success(self.pool[i])*2):
                self.pool.append(self.pool[i])
        self.mutagen()
        
        a=sorted(self.pool,key = lambda x: self.success(x),reverse=True)
        print("The best kids were,",a[:10])
        print("The best score is", self.success(a[0]))
        if len(a)>self.pool_size*2.5:
            a=a[:int(self.pool_size*2.4)]
        random.shuffle(a)
        self.pool=a

    def success(self,input):
        i=0
        for j in range(len(self.target)):
            if input[j]==self.target[j]:
                i+=1
        return i

    def pool_gen(self,len_word):
        char_big = [chr(i) for i in range(65,91)]
        char_small = [chr(i) for i in range(97,123)]
        digits = [str(i) for i in range(10)]
        self.char_set = char_small + char_big + [' '] + digits

        word_gen=''
        for i in range(len_word):
            word_gen+=secrets.choice(self.char_set)
        return word_gen

    def mutagen(self):
        #randomly mutates self.pool elements
        #k is number of mutations
        #now set as 2% mutation of entire pool
        k = int(len(self.pool)*0.02)
        choice_indices = [i for i in range(len(self.pool))]
        for i in range(k):
            #mutate
            mutation_index = secrets.choice(choice_indices)
            #mutation power set at 20%
            self.pool[mutation_index] = self.mutate(self.pool[mutation_index] , 20)

    def mutate(self,word, mutation_power):
        #mutation power is in percentage
        words = list(word)
        mutations = (mutation_power*len(words))//100
        #print("number of mutations is",mutations)
        choice_indices = [i for i in range(len(words))]
        for i in range(mutations):
            #print("mutated")
            temp = secrets.choice(choice_indices)
            #print(words[temp])
            words[temp] =  secrets.choice(self.char_set)
            #print(words[temp])
            
        words = ''.join(words)
        return words





