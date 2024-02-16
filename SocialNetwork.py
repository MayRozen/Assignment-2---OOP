import self


class SocialNetwork:
    __active_network = None #Singleton
    userName = None
    password = None
    check_userName = []

    def __new__(cls):
        if cls.__active_network is None: # If an instance does not exist -> create a new one
            cls.__active_network = super().__new__(cls) # super -> from Object class
        return cls.__active_network


    def sign_up(self, new_userName, new_password:
        if new_userName not in self.check_userName:
            self.userName = new_userName
            self.check_userName.append(new_userName)
        else:
            print("This name is already registered in the system. Choose another name.")

        length_pass = len(new_password)
        if 4<=length_pass<=8:
            self.password = new_password
        else:
            print("This password is invalid. Please change password")
            self.password = input()

    def log_in (self,  userName,  password):
         self.users(userName, password).isConnected()



    def log_out (self, userName):
        return False



