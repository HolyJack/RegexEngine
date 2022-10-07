
def regex_char(single_regex, c) -> bool:
    if not single_regex:
        return True
    elif single_regex == ".":
        return True
    elif not c:
        return False
    elif single_regex == c:
        return True
    return False


def regex_string_plus_handle(regex, string_):
    if not string_:
        return False
    elif regex_char(regex[0], string_[0]):
        return regex_string_plus_handle(regex, string_[1:]) or regex_string(regex[2:], string_[1:])
    return False


def regex_string(regex, string_):
    if not regex:
        return True

    elif not string_ and regex == "$":
        return True

    elif not string_:
        return False

    elif regex[0] == '\\':
        return regex_string(regex[1:], string_)

    elif regex_char(regex[0], string_[0]) and regex[1:] and regex[1] == '+':
        return regex_string_plus_handle(regex, string_[1:]) or\
               regex_string(regex[2:], string_[1:])

    elif regex_char(regex[0], string_[0]) and regex[1:] and regex[1] == '*':
        return regex_string(regex, string_[1:]) or\
               regex_string(regex[2:], string_)

    elif regex_char(regex[0], string_[0]) and regex[1:] and regex[1] == '?':
        return regex_string(regex[2:], string_[1:]) or\
               regex_string(regex[2:], string_)

    elif regex_char(regex[0], string_[0]):
        return regex_string(regex[1:], string_[1:])

    elif regex[1:] and (regex[1] == '?' or regex[1] == '*'):
        return regex_string(regex[2:], string_)

    return False


def regex_string_improved(regex, string_):
    if not regex:
        return True
    elif not string_:
        return False
    elif regex[0] == '^':
        return regex_string(regex[1:], string_)
    elif not regex_string(regex, string_):
        return regex_string_improved(regex, string_[1:])
    elif regex_string(regex, string_):
        return True
    return False


def main():
    #   Input format "regex|string"
    regex, input_ = input().split('|')
    print(regex_string_improved(regex, input_))


if __name__ == '__main__':
    main()
