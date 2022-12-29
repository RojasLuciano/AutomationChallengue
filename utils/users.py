users = [
    {"name": "standard_user", "email": "standard_user@test.com", "password": "secret_sauce", "last_name": "Doe",
     "postal_code": "12345"},
    {"name": "locked_out_user", "email": "locked_out_user@test.com", "password": "secret_sauce", "last_name": "Doe",
     "postal_code": "12345"},
    {"name": "problem_user", "email": "problem_user@test.com", "password": "secret_sauce", "last_name": "Doe",
     "postal_code": "12345"},
    {"name": "performance_glitch_user", "email": "performance_glitch_user@test.com", "password": "secret_sauce",
     "last_name": "Doe", "postal_code": "12345"},

]


def get_user(name):
    try:
        return next(user for user in users if user["name"] == name)
    except:
        print("\n     User %s is not defined, enter a valid user.\n" % name)
