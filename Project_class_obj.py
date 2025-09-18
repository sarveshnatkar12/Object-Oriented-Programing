class Chatbook:
    def __init__(self):
        self.__name = 'Default'
        self.username =''
        self.password =''
        self.loggedin = False
        #self.menu()

    def menu(self):
        user_input = input(""""Welcome to Chatbook !! How would you like to proceed?
                           1. Press 1 to signup
                           2. Press 2 to signin
                           3. Press 3 to write a post
                           4. Press 4 to message a friend
                           5. Press any other key to exit
                           
                           -> """) 
        
        if(user_input == '1'):
            self.signup()
        if(user_input == '2'):
            self.signin()
        if(user_input == '3'):
            self.post()
        if(user_input == '4'):
            self.sendmsg()
        else:
            exit()

    #setter
    def set_object(self , val):
        self.__name = val
        
    
    #getter
    def get_object(self):
        return self.__name


    def signup(self):
        email = input('enter your emailID-->')
        pwd = input('enter you password-->')
        self.username = email
        self.password = pwd
        print('signed up successfully')
        print()
        self.menu()

    def signin(self):
        if(self.username =='' and self.password ==''):
            print('pls signup by pressing 1 first')
        
        else:
            email = input('enter your emailID-->')
            pwd = input('enter your password-->')
            if(email == self.username and pwd == self.password):
                print('signin sucessfull')
                self.loggedin = True
            else:
                print('retry signin by pressing 2')
        print()
        self.menu()

    def post(self):
        if self.loggedin == True:
            text = input('enter your text-->')
            print('content posted')
        else:
            print('to post any content signup first')
        print()
        self.menu()
    
    def sendmsg(self):
        if self.loggedin == True:
            msg = input('enter your message-->')
            print('message sent!')
        else:
            print('to send a msg you need to signin first')
        print()
        self.menu()

