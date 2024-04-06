class MyHashSet(object):

    def __init__(self):
        self.array = [[] for _ in range(5)]

    def add(self, key):
        """
        :type key: int
         return key in self.hash_set
        :rtype: None
        """
        subkey = key % 5
        if not self.contains(key):
            self.array[subkey].append(key)
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        subkey = key % 5
        if  self.contains(key):
            self.array[subkey].remove(key);

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        subkey = key % 5
        return key in self.array[subkey]
        


# Your MyHashSet object will be instantiated and called as such:
key = 10
obj = MyHashSet()                                                      #OutPut
obj.add(key)                                                            #[[10, 25], [], [], [], [24]]
obj.add(25)                                                             #[[25], [], [], [], [24]]
obj.add(24)
print(obj.array)
obj.remove(key)
print(obj.array)
param_3 = obj.contains(key)