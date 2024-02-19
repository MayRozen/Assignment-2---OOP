
class SocialNetwork:
    _active_network = None  # Singleton
    userName = None
    password = None
    check_userName = []

    def __new__(cls, new_nameNetwork):
        if cls._active_network is None:  # If an instance does not exist -> create a new one
            cls._active_network = super().__new__(cls)  # super -> from Object class
            cls._active_network = new_nameNetwork
            print(_active_network)
        return cls._active_network


    def sign_up(self, new_userName, new_password):
        if new_userName not in self.check_userName:
            self.userName = new_userName
            self.check_userName.append(new_userName)
        else:
            print("This name is already registered in the system. Choose another name.")

        length_pass = len(new_password)
        if 4 <= length_pass <= 8:
            self.password = new_password
        else:
            print("This password is invalid. Please change password")
            self.password = input()

    def log_in(self, new_userName, new_password):
        if new_userName in self.check_userName:
            if new_password in self.check_userName:
                Users.isConnected = True
                print("The user is in")

    def log_out(self, new_userName):
        if new_userName in self.check_userName:
            Users.isConnected = False
            print("The user is out")


