def all_thing_is_obj(object: any) -> int:
    """Print the type of the given object and return 42."""
    t = type(object)
    if t is list:
        print(f"List : {t}")
    elif t is tuple:
        print(f"Tuple : {t}")
    elif t is set:
        print(f"Set : {t}")
    elif t is dict:
        print(f"Dict : {t}")
    elif t is str:
        print(f"{object} is in the kitchen : {t}")
    else:
        print("Type not found")
    return 42
