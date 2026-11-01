def NULL_not_found(object: any) -> int:
    """Print what kind of null the object is. Return 1 if it is none."""
    t = type(object)
    if object is None:
        print("Nothing:", object, t)
    elif t is float and object != object:
        print("Cheese:", object, t)
    elif t is int and object == 0:
        print("Zero:", object, t)
    elif t is str and object == "":
        print("Empty:", t)
    elif t is bool and object is False:
        print("Fake:", object, t)
    else:
        print("Type not Found")
        return 1
    return 0
