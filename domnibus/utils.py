def camel_case_to_lower_case_underscore(string):
    """
    Split string by upper case letters.
 
    F.e. useful to convert camel case strings to underscore separated ones.
 
    @return words (list)
    """
    if not string.isupper():
        words = []
        from_char_position = 0
        for current_char_position, char in enumerate(string):
            if char.isupper() and from_char_position < current_char_position:
                words.append(string[from_char_position:current_char_position].lower())
                from_char_position = current_char_position
        words.append(string[from_char_position:].lower())
        string = '_'.join(words)

    return string

def unify_key_formats(response_dict):
    value = {}
    for k, v in response_dict.items():
        value[camel_case_to_lower_case_underscore(k)] = v
    return value