TRAIN_LETTERS = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789(),.-!?\"' ")


def clean_string(str_to_clean):
    """Cleans the given string by removing special characters
    :param str_to_clean: The string that needs to be cleaned
    :return: The clean string
    """
    str_to_clean = list(str_to_clean)
    idx = 0
    while idx < len(str_to_clean) - 1:
        curr_ch = str_to_clean[idx]
        next_ch = str_to_clean[idx + 1]
        if curr_ch not in TRAIN_LETTERS:
            str_to_clean[idx] = ' '
        if next_ch not in TRAIN_LETTERS:
            str_to_clean[idx + 1] = ' '
        if next_ch == ' ' and (curr_ch == '.' or curr_ch == ' '):
            del str_to_clean[idx + 1]
        else:
            idx += 1
    return str_to_clean


# train() starts from here
with open('brown_small.txt', 'r') as train_txt_file:
    train_text = clean_string(train_txt_file.read())
    print ''.join(train_text)
