def for_save(user, password):
    user.set_password(password)
    user.save()
    return user
