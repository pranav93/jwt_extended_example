profile_info = dict(
        name='Dummy Name',
        age=23,
        hobbies=['watching movies', 'playing games']
    )


def get_profile():
    global profile_info
    return profile_info


def get_profile_pic():
    global profile_info
    return profile_info['profile_pic']
