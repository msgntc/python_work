def buld_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
user_info = buld_profile('Josiah', 'Cruz', location= 'The place I am at.', field = 'The thing I do.',
                          hobby= 'The thing I like to do.', age= 'The number of years I have lived.')
print(user_info)
