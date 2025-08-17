def all_thing_is_obj(object: any) -> int:
    type_name = type(object).__name__.capitalize()
    if type_name == 'Str':
        type_name = str(type(object))
        print(object + " is in the kitchen : " + type_name)
    elif type_name == 'Int':
        print("Type not found")
    else:
        print(type_name + " : " + str(type(object)))
    return 42
