#properties/attributes
# var public method/properties
# _var These are suppose to be private method/properties
# __var (name mangling) allow to be accessed outside the class using the name of the class
# __var__ these are methods than are built already and can be overwrite

class User:
    # Class attributes
    __name_mangling = "This is a name mangling attribute"
    active_users = 0

    # Class methods
    @classmethod
    def show_active(cls):
        print(f"Active users: {cls.active_users}")

    @classmethod
    def from_str(cls, string):
        first, last, age = string.split(",")
        return cls(first, last, age)


# Constructor/Initialize method is called every time an object is created

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        User.active_users += 1

    def __repr__(self):
        return f"{self.first_name},{self.last_name}"

    def info(self):
        print(self.first_name, self.last_name, self.age)

    def initials(self):
        print(f"{self.first_name[0].upper()}.{self.last_name[0].upper()}")

    def logout(self):
        User.active_users -= 1
        print(f"{self.first_name} has logout")

    pass


user = User("Jhon", "Doe", 28)
print(user)
user2 = User("Sue", "Smith", 55)
user3 = User("Annie", "Prichet", 34)
user4 = User("Blanca", "Lopez", 22)
user5 = User("Juan", "Gomez", 48)
print(User._User__name_mangling)
user.info()
user.initials() 

User.show_active()
user.logout()
User.show_active()

user6 = User.from_str("Ana,Rodriguez,19")
user6.info()
User.show_active()