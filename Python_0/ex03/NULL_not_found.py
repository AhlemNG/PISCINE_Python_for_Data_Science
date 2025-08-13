
def NULL_not_found(object: any) -> int:
    obj_type = type(object)
    if object is None:
        print("Nothing:", object, obj_type)
        return (0)
    elif obj_type == float and object != object:
        print("Cheese:", object, obj_type)
        return (0)
    elif object == 0 and obj_type == int:
        print("Zero:", object, obj_type)
        return (0)
    elif object == "":
        print("Empty:", obj_type)
        return (0)
    elif object is False:
        print("Fake:", object, obj_type)
        return (0)
    print("Type not Found")
    return (1)
