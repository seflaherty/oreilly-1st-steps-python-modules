def menu(*args):  # args is a tuple containing all passed arguments
    user_choice = input('Enter your choice: ')

    if user_choice in args:
        return user_choice

    else:
    
