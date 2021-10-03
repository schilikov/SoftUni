def age_assignment(*args, **kwargs):
    result = {}
    for name in args:
        first_letter = name[0]
        result[name] = kwargs[first_letter]
    return result