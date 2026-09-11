class loginSystem:
    def __init__(self, password):
        self.__password = password
    def set_password(self, password):
        self.__password = password
    def validate_password(self, password):
        return self.__password == password  
log = loginSystem("myPassword123")
print(log.validate_password("myPassword123"))  # Output: True
