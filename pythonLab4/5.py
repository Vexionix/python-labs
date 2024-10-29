def validate_dict(validation_set, dictionary_to_validate):
    for validation_tuple in validation_set:
        if validation_tuple[0] not in dictionary_to_validate:
            return False

        key_to_validate = dictionary_to_validate[validation_tuple[0]]

        if not key_to_validate.startswith(validation_tuple[1]):
            return False

        if key_to_validate.endswith(validation_tuple[2]) or key_to_validate.startswith(validation_tuple[2]) or not key_to_validate.find(validation_tuple[2]):
            return False

        if not key_to_validate.endswith(validation_tuple[3]):
            return False

    return True

if validate_dict({("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}, {"key1": "come inside, it's too cold out", "key3": "this is not valid"}):
    print("First dictionary is valid!")
else:
    print("First dictionary is invalid!")

if validate_dict({("key1", "", "inside", ""), ("key2", "start", "middle", "winter")},{"key1": "come inside, it's too cold out", "key2": "start middle winter"}):
    print("Second dictionary is valid!")
else:
    print("Second dictionary is invalid!")