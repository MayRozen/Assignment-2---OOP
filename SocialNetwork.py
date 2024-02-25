from Users import Users


class SocialNetwork:
    _active_network = None  # Singleton

    def __new__(cls, new_name_network):  # singleton
        if cls._active_network is None:  # If an instance does not exist -> create a new one
            cls._active_network = super().__new__(cls)  # super -> from Object class
        return cls._active_network

    def __init__(self, new_name_network):
        if not hasattr(self, 'name'):
            self.new_name_network = new_name_network
            self.check_userName = []
            print(f"The social network {self.new_name_network} was created!")

    def sign_up(self, new_username, new_password):
        if new_username not in self.check_userName:
            if 4 < len(new_password) < 8:
                new_user = Users(new_username, new_password)
                self.check_userName.append(new_user)
                return new_user
            else:
                raise ValueError("This password is invalid")
        else:
            raise ValueError("This name is already registered in the system")

    def log_out(self, new_username):
        for user in self.check_userName:
            if user.username() in new_username:
                user.isConnected = False
                print(f"{new_username} disconnected")

    def log_in(self, new_username, new_password):
        for user in self.check_userName:
            if user.username() == new_username and user.password() == new_password:
                user.isConnected = True
                print(f"{new_username} connected")


    def __str__(self):
        ans = f"{self.new_name_network} social network:\n"
        for user in self.check_userName:
            if(user != self.check_userName[-1]):
                ans = ans + str(user) + "\n"
            else:
                ans = ans + str(user)
        return ans
