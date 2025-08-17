def all_thing_is_obj(obj: any) -> int:
    type_name = type(obj).__name__.capitalize()
    if type_name == 'Str':
        print(f"{obj} is in the kitchen : {type(obj)}")
    elif type_name in ['List', 'Tuple', 'Set', 'Dict']:
        print(f"{type_name} : {type(obj)}")
    else:
        print("Type not Found")
    return 42
