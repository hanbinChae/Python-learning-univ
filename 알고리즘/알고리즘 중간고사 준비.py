# 선형 리스트 삽입
def linear_append(value):
    stack.append(None)
    stack[len(stack)-1] = value
    print(stack)

# 선형 리스트 중간 삽입
def linear_insert(value,positon):
    stack.append(None)
    for i in range(len(stack)-1,positon,-1):
        stack[i] = stack[i-1]
        stack[i-1] = None
    stack[positon] = value
    print(stack)

# 선형 리스트 중간 삭제
def linear_delete(position):
    stack[position] = None
    for i in range(position,len(stack)-1,1):
        stack[i] = stack[i+1]
        stack[i+1] = None
    stack.pop()
    print(stack)

stack = ['한빈','화택','혁환']

#데이터 링크 연결리스트
class Node():
    def __init__(self):
        self.data = None
        self.link = None

node1 = Node()
node1.data = '연결리스트1'

node2 = Node()
node2.data = '연결리스트2'
node1.link = node2
# print(node1.data)
# print(node1.link.data)

# 선형리스트 연결리스트로 전환 
dataArray = ['박'+str(i) for i in range(5)]
node1 = Node()
node1.data = dataArray[0]
head1 = node1

for d in dataArray[1:]:
    pre = node1
    node1= Node()
    node1.data = d
    pre.link = node1

# 연결리스트 맨 앞에 데이터 삽입
node = Node()
node.link = head1
node.data='처음'
head1=node

# 연결리스트 중간에 데이터 삽입
head2 = head1
pre = head2
current = head2.link

while current.link != None:
    if current.data =='박2':
        node = Node()
        node.link = current
        node.data='1.5박'
        pre.link = node
        break;
    pre = current
    current = current.link

# 연결리스트 마지막에 데이터 삽입
node = Node()
node.data='마지막'
current.link = node

# 연결리스트 첫번째 값 삭제
head3 = head2
current = head3
head3 = head3.link
del(current)

#확인
# temp = head3
# while temp.link:
#     print(temp.data,end=' ')
#     temp = temp.link
# print(temp.data)

# 연결리스트 중간 값 삭제
head4 = head3
current = head4

while current.link != None:
    pre = current
    current = current.link
    if current.data =='1.5박':
        pre.link=current.link
        del(current)
        break;

# temp = head4
# while temp.link:
#     print(temp.data,end=' ')
#     temp = temp.link
# print(temp.data)

#원형 연결리스트
circle_node=Node()
circle_node.data = '채한빈'
circle_node.link = circle_node #리스트 순환 :(원형 연결리스트)
head=circle_node

# temp = head
# while temp.link: #무한반복
#     print(temp.data,end=' ')
#     temp = temp.link
# print(temp.data)

#원형 연결리스트 삽입
circle_list = ['채한빈','김학범','이민곤','이원홍','김참직']

c_node = Node()
c_node.data = circle_list[0]
c_head1 = c_node
node.link = head

current = c_node
for c in circle_list[1:]:
    c_node = Node()
    c_node.data= c
    current.link = c_node
    c_node.link = c_head1
    current = c_node

# 원형 연결리스트 맨 앞에 데이터 추가
c_head2 = c_head1
node = Node()
node.data='김'
node.link = c_head2

last = c_head2
while last.link != c_head2:
    last = last.link

last.link = node
head = node

# temp = c_head2
# while temp.link:
#     print(temp.data,end=' ')
#     temp = temp.link
# print(temp.data)

# 중간 노드 삽입
c_head3 = c_head2
pre = c_head3
current = c_head3

while current.link!=head:
    pre = current
    current = current.link
    
    if current.data == '김학범':
        node=Node()
        node.data='크리호날두'
        node.link=current
        pre.link=node
        break

# temp = c_head3
# while temp.link:
#     print(temp.data,end=' ')
#     temp = temp.link
# print(temp.data)

#첫번째 노드 삭제
c_head4 = c_head3

current = c_head4
c_head4 = c_head4.link
last = c_head4

while last.link != current:
    last = last.link

last.link=c_head4
del(current)

#원형리스트 중간노드 삭제 
head = c_head4

current=head
pre = head
while current.link != head:
    pre = current
    current = current.link
    if current.data =='크리호날두':
        pre.link = current.link
        del(current)
        break;
# temp = head
# while temp.link:
#     print(temp.data,end=' ')
#     temp = temp.link
# print(temp.data)

# 스택
def isStackFull():
    global top,stack,size
    if top==size-1:
        return True
    else:
        return False
def _push(value):
    global top,stack,size
    if isStackFull():
        return False
    else:
        top+=1
        stack[top] = value
        
def isStackEmpty():
    global top,stack,size
    if top==-1:
        return True
    else:
        return False

def _pop():
    if isStackEmpty():
        print("Stack is Empty")
        return
    else:
        data = stack[top]
        stack[top] = None
        return data


size = 5
top = 2
stack = [None for _ in range(size)]
