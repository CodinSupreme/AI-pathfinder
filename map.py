import random

_ = False
mini_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    
]
lst=[
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 3, 1],
    [1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1],
    [1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 4, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    
]



class Map:
    def get_map(self, k:int):
        self.map_list=[]
        self.previous={}

        for i in range(k):
            if i == 0 or i == k-1:
                lst=[]
                for j in range(k):
                    lst.append(1)

                self.map_list.append(lst)

            else:
                lst=[1]
                for j in range(k-2):
                    pos=int(random.randrange(0, 50))
                    if pos % 7 == 0:
                        pos=0
                    else:pos=1
                    lst.append(pos)
                
                if i == 1:
                    if 0 not in lst:
                        lst.insert(random.randrange(1, k-1), 3)
                    else:
                        d=lst.index(0)
                        lst.pop(d)
                        lst.insert(d, 3)

                if len(self.previous) != 0:
                    for key, data in self.previous.items():

                        lst.pop(key)
                        lst.insert(key, data)
                
                m = lst.copy()
                self.previous.clear()
                for index, data in enumerate(m):
                    if data == 0 or data == 3:
                        if data == 3:
                            self.previous[index] = 0

                        else:
                            if index != 0 and index != len(m) and (index + 1 ) < len(m):
                                if m[index-1] == 0 or m[index + 1] == 0:
                                    d=[[index-1, m[index-1]], [index, data], [index+1, m[index + 1]]]
                                    choice=random.choice(d)
                                    d.remove(choice)
                                    d=random.choice(d)
                                    self.previous[choice[0]]= choice[1]
                                    self.previous[d[0]]=d[1]

                                else:
                                    self.previous[index] = data 
                if i == k-2:
                    ch=random.randrange(1, len(lst)-1)
                    lst.pop(ch)
                    lst.insert(ch, 4)
                lst.append(1)
                
                self.map_list.append(lst)

        return self.map_list


map = Map().get_map(10)
for i in map:
    print(i)               
 


     
         
