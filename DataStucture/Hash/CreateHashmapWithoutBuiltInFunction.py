class MyHashMap(object):

    def __init__(self):
        self.data = [[] for _ in range(5)]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        hash_key = key % 5
        for i, (k, v) in enumerate(self.data[hash_key]):
            if k == key: 
                self.data[hash_key][i] = (key, value)
                return
        self.data[hash_key].append((key, value)) 

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        hash_key = key % 5
        for k, v in self.data[hash_key]:
            if k == key:
                return v 
        return -1
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        hash_key = key % 5
        for i, (k, v) in enumerate(self.data[hash_key]):
            if k == key:
                del self.data[hash_key][i] 
                return
        


# Your MyHashMap object will be instantiated and called as such:
obj = MyHashMap()
obj.put(20,"mamu")
obj.put(40,"sasu")
obj.put(24,20)
print(obj.data)         #[[(20, 'mamu'), (40, 'sasu')], [], [], [], [(24, 20)]]
print(obj.get(20))      # mamu
obj.remove(40)
print(obj.data)         #[[(20, 'mamu')], [], [], [], [(24, 20)]]