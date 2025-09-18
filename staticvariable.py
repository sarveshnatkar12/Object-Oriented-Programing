from Project_class_obj import Chatbook
                #Brfore static variable        #After Static variable
user1 = Chatbook()   # 1                                1
user2 = Chatbook()   # 1                                2
user3 = Chatbook()   # 1                                3

Chatbook.set_id(23)
user4 = Chatbook()
user4.get_id()   # op-->23
