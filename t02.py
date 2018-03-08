
n1=[i for i in range(10)]
# print(n1)
# print(type(n1))

n2=(i for i in range(10))
# print(n2)
# print(type(n2))

class Tu(object):
    name='哈哈怪'
    def go(self):
        print(self.name)
        print('这是一个方法')

t=Tu()
has_attr=hasattr(Tu,'go')
# print(has_attr)
has_attr2=hasattr(t,'go')
# print(has_attr2)
met_go=getattr(Tu,'go')
# print(type(met_go))
# met_go(t)
