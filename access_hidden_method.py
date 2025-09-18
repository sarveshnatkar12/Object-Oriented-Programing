from Project_class_obj import Chatbook

sarvesh = Chatbook()
# print(sarvesh.__name) #o/p-->AttributeError: 'Chatbook' object has no attribute '__name'

#Traditional way to fetch hidden attributes
print(sarvesh._Chatbook__name)#o/p --> Default
