def get_length(s):
    count = 0
    try:
        while True:
            s[count]
            count += 1
    except IndexError:
        pass
    return count   