class duplicate():
    def __init__(self, list12):
        self.list12=list12
        print self.list12

    def __call__(self, list12):
        print list12

# using loop and list to find duplicated
new_list=[]
list12 = [1,2,3,4,5,6,1,2,3,4,5]
set_list = set(list12)
final_list=list(set_list)   # converting set into list
print(final_list)

#print("Hi this is coming from set {}".format(set_list))
def remove_duplicate(p):
    for dup in list12:
        if(dup not in new_list):
            new_list.append(dup)
    p(new_list)
p=duplicate(list12)
remove_duplicate(p)

# using set to find duplicate

list=set()
list.add('Amit')
list.add('sandeep')
list.add('awdesh')
list.add('lovelesh')
list.add('Amit')
list.add('sandeep')
list.add('awdesh')
list.add('lovelesh')

print list  # here list will only print name once , no duplicate items will be printed




