
def get_promt_num(msg, retry=2, default_val=10):
    num = ""
    while not num.isnumeric() and retry:
        num = input(msg)
        retry -= 1
    if not retry:
        print(msg[len("Enter "):], default_val)
        return default_val

    return int(num)
