# 1. Linked List

链表是基础的数据结构，与之对应的另外一个选择是数组。在查询方面，数组有优势，复杂度是O(1)，但是在插入删除等操作上不如链表，复杂度是O(n)；链表在插入删除等操作上有优势，复杂度是O(1)，而查询上不如数组，必须按照顺序检索，复杂度是O(n)。
以上特征的原因来自于二者不同的储存方式，数组是在内存空间中选取连续单元，所以查询速度极快，但是如果插入元素超过了附近可用的内存空间，则要整体复制迁移，重新分配内存空间。相比之下，链表的存储不是连续的内存空间，每一个位置上记录与之相邻的元素，如果是单链表，只记录下一个元素的内存位置，双链表的话还会记录上一个元素位置。

## 1.1 Linked List基本构成

一般要有两个class，一个定义单个Node的构成（value和element address），另一个定义整体的list（head起始位置）
```
class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None
#单链表的Node有两个部分构成，一个是当前element的value，另一个是下一个element的address(how to express)

class LinkedList:
    def __init__(self):
        self.head = None
# Linked list的必须元素只有head
```

## 1.2 Linked List的生成和显示

Linked List一般需要根据Class Node生成一个连续的链表，并且可以根据需要显示链表的元素。
```
class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None

class LinkedList:
    def __init__(self, L = None):
        if not L:
            self.head = None
        self.head = Node(L[0]) # 将第一个元素生成的Node(含value及next_node属性)赋给head
        current_node = self.head # current_note即当前元素生成的Node，即Node(L[0])

        for e in L[1: ]:
            current_node.next_node = Node(e)    # 第一个元素对应的Node的next_node赋值，即(L[0]).next_node = Node(e)
            current_node = current_node.next_node # 当前位置等于第二个元素

    def print_list(self, sep = ', '):
        values = []
        node = self.head
        #从head开始，只要node有值，全都变成str加入values中，方便格式化输出
        while node:
            values.append(str(node.value))
            node = node.next_node
        print(sep.join(values))
```
## 1.3 Linked List插入元素

常见的插入操作是在两端加入，所以定义两个function实现头尾两端插入元素的功能。

#Node和LinkedList上文定义过的属性功能不再重复，这里只附两个函数的代码
```
class LinkedList:
    def append(self, value):
    #在最后插入新的node
        new_node = Node(value) 
        if not self.head:
            self.head = new_node
        #如果当前Linked List中没有node，则让head指向这个新的Node
        else:
            current_node = self.head
            while current_node.next_node:
                current_node = current_node.next_node
            current_node.next_node = new_node
        #如果当下有node，则遍历所有node，直到找到最后一个node，由于while的body将当前node指向了下一个，所以终止条件是判断下一个node是否为真

    def prepend(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            new_node.next_node = self.head
            #新的node指向head，这里的head是一个linked list
            self.head = new_node
            #head指向new node，这里的head是上文提到过的LinkedList class中的一个属性
```
## 1.4 Linked List删除元素

同样，常见的删除位置是在首尾两端，和插入的方法类似，只是删除时的条件判断更加复杂。
```
class LinkedList:
    def delete_first_element(self):
        if not self.head:
            return 
        if not self.head.next_node:
        #之所以要比insert多加一个判断，是因为如果只有一个元素，head要指向None，如果多于一个元素，head指向剩下紧邻的元素
            self.head = None
        else:
            self.head = self.head.next_node
        #链表中删除元素，其实不用真的将值改变，或者移动后续元素，只需要在链表的关联中删除该元素的地址，任何元素都将无法找到这个元素，也就被删除了。

    def delete_last_element(self):
        if not self.head:
            return 
        if not self.head.next_node:
        #之所以要比insert多加一个判断，是因为如果只有一个元素，head要指向None，如果多于一个元素，head指向剩下紧邻的元素
            self.head = None
        else:
            current_node = self.head
            while current_node.next_node.next_node:
                current_node = current_node.next_node
            current_node.next_node = None
            #和在最后插入位置类似，循环判断条件需要注意，因为要删除最后一个元素，我们要让当前位置停留在倒数第二个元素，而while的body内会更改当前元素到下一个，所以判别结束条件应该是当下元素后面的第三个元素为空。
```
## 1.4 Linked List排序判断

Linked List的数据结构最擅长排序，所以自然要在class的定义中判断排序状态。
```
class LinkedList:
    def __init__(self, L = None, comparison_key = lambda x: x):
        if L is None or not len(L):
            self.head = None
        else:
            self.head = Node(L[0])
            current_last_node = self.head
            for e in L[1: ]:
                current_last_node.next_node = Node(e)
                current_last_node = current_last_node.next_node
        self.comparison_key = comparison_key

    def is_sorted(self):
        if not self.head or not self.head.next_node:
            return True
        #如果链表为空，或者只有一个元素，都认为是有序的
        node = self.head
        while node.next_node:
            if self.comparison_key(node.value) > self.comparison_key(node.next_node.value):
                return False
            node = node.next_node
        return True
```
## 1.5 Linked List逆序

和上文同样的原因，逆序也是常用功能。
```
class LinkedList:
    def reverse(self):
        if not self.head or not self.head.next_node:
            return True
        tail = self.head
        #最后的位置是现在的head处
        current_node = self.head.next_node
        #要处理的元素是head后面一个
        tail.next_code = None
        #切断tail和其他元素的联系
        while current_node:
            next_node = current_node.next_node
            #找到下一个要逆序的元素
            current_node.next_node = tail
            #建立当下处理元素的逆序关系
            tail = current_node
            #标记当前逆序list中最后一个元素
            current_node = next_node
            #处理好当前的元素后，准备再次循环处理下面的元素
        self.head = tail
        #全部逆序后，head应该指向tail的标记处     
``` 
# 2. Deque实现

Deque的数据结构也是Linked List，可以方便的插入、删除数据，一般都是在头尾操作元素。