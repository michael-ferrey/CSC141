class name:
    def __init__(self, user, description):
        """Initialize name and cuisine name"""
        self.user = user
        self.description = description

    def describe_user(self):
        """The name of the user"""
        print(f"The name of the user is  {self.user}!")
        print(f"This user {self.description}!")

    def greet_user(self):
        """Indicate the opening of the restaurant"""
        print(f"Hello {self.user}, how are you doing today!")
        
my_user = name("Michael", "enjoys to lift and spend time with his girlfriend")  
my_user.describe_user()
my_user.greet_user()
