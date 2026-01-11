def auth_wrapper(*args):
    if not global_user.is_admin:
            raise PermissionError("Access Denied")
    return original_function(*args)
    


