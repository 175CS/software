import time
start = time.time()
class Stack:
    def _init_(self):
        self.items = []  
 
    def isEmpty(self):
        return self.items == []  

    def push(self, item):
        self.items.append(item)
        print(item) 

    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items) - 1] 

    def size(self):
        return len(self.items)

s=Stack()
print(s.isEmpty()," - because stack is empty")


print("elements are pushed into stack for Operation")
s.push(11)
s.push(12)
s.push(13)
print("Size",s.size())
print("Peek",s.peek())
print("Pop Operation")
print(s.pop())
print(s.pop())
print("Size",s.size())
print("********************")
class Queue:
    def _init_(self):
        self.items = []
  
    def isEmpty(self):
        return self.items == []
   
    def enqueue(self,item):
        self.items.append(item)
        print(item)
    
    def dequeue(self):
        return self.items.pop(0)
   
    def front(self):
        return self.items[len(self.items)-1]
   
    def size(self):
        return len(self.items)

q=Queue()
print(q.isEmpty(),"- because queue is empty")
print("Enquee")
q.enqueue(11)
q.enqueue(12)
q.enqueue(13)
print("Front",q.front())
print("Dequee")
print(q.dequeue())
print(q.dequeue())
print("Size",q.size())
print("\n")
end = time.time()
print(f"Runtime of the program is {end - start}")
