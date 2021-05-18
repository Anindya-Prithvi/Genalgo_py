#image prog-gen with gen algo
#currently only b/w images
import cv2,numpy,random,secrets
import matplotlib.pyplot as plt

class prog_image:
    def __init__(self , init_pool_size , target):
        
        self.pool_size = init_pool_size
        self.pool = []
        self.target_img = cv2.imread(target,0)
        self.ydim = numpy.size(self.target_img,0)
        self.xdim = numpy.size(self.target_img,1)
        self.target = self.target_img.reshape(self.target_img.size)
        
        #generate pool here
        for i in range(self.pool_size):
            random.seed((random.random(),random.random(),random.random()))
            self.pool.append(self.pool_gen(self.target_img.size))


    def gen_progress(self):
        #TODO use dictionary?

        #progresses with new generation. Changes self.pool with new pool
        #replication function
        
        #self.pool.append(self.pool_gen(self.target_img.size))

        self.pool.sort(key = lambda x: self.success(x) , reverse=True)
##        print([self.success(i) for i in self.pool])

        #show
        cv2.imshow("best so far", numpy.array(self.pool[0],dtype='uint8').reshape(self.ydim,self.xdim))
        cv2.waitKey(1)
        
        #empty pool
        for i in range(int(numpy.log(self.pool_size))+4):
            _ = self.pool.pop()

##        print([self.success(i) for i in self.pool])

        #replicate pool best
        for i in range(int(numpy.log(self.pool_size))+4):
            self.pool.append(self.pool[0].copy())

##        print([self.success(i) for i in self.pool])
        
        self.mutagen()
        print([self.success(i) for i in self.pool])



    def success(self,input):
        e=numpy.e
        #use distance based grading.. i.e. near the better
        return sum(e**(-abs(a.target-input)))

    def pool_gen(self,len_word):
        #returns array of random 0-255 nums
        self.range_obj=[i for i in range(256)]
        return [secrets.choice(self.range_obj) for i in range(len_word)]

    def mutagen(self):
        #print("mutagen")
        #in this implementation double mutation may occur on single place.

        #randomly mutates self.pool elements
        #k is number of mutations
        #now set as 61.2% mutation of entire pool
        k = (int(len(self.pool)*0.612))
        choice_indices = [i for i in range(2,len(self.pool))]
        for i in range(k):
            #mutate
            mutation_index = secrets.choice(choice_indices)
##            print(mutation_index,"modified")
            #mutation power set at 20%
            self.pool[mutation_index] = self.mutate(self.pool[mutation_index] , 5)
            #print("new suc",self.success(self.pool[mutation_index]))
            #print([self.success(i) for i in self.pool])

    def mutate(self, item , mutation_power):
        #mutation power is in percentage
        for i in range(self.target_img.size):
            if random.random()<mutation_power/100:
                item[i]=(item[i]+secrets.choice([-2,-1,0,1,2]))%256
        return item

a=prog_image(13,"resized.jpeg")
i=0
storage_x=[]
storage_score=[]
while True:
    plt.clf()
    a.gen_progress()
    print(len(a.pool))
    i+=1
    print("This was gen",i,"score =",a.success(a.pool[0]))
    storage_x.append(i)
    storage_score.append(a.success(a.pool[0]))
    plt.plot(storage_x,storage_score)
    plt.pause(0.0001)
plt.show()
    
