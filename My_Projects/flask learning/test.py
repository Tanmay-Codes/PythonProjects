# def decorator_function(function):
#     def wrapper_function():
#         print("hello")
#         function()
#     return wrapper_function()
#
# @decorator_function
# def name1():
#     print("Tanmay")
#
# @decorator_function
# def name2():
#     print("Amogh")

class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def is_authenticated_decorator(self):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function()

    return wrapper

@is_authenticated_decorator
def create_post(user):
    print(f"This is {user.name}'s new blog post.")

new_user = User("Tanmay")
create_post(new_user)

