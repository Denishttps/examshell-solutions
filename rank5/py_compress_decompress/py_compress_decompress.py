def compress(s: str) -> str:
    if not s:
        return ""

    encoded = []
    run_char = s[0]
    run_length = 1
    for char in s[1:]:
        if char == run_char:
            run_length += 1
        else:
            encoded.append(run_char)
            if run_length > 1:
                encoded.append(str(run_length))
            run_char = char
            run_length = 1

    encoded.append(run_char)
    if run_length > 1:
        encoded.append(str(run_length))
    return "".join(encoded)


def decompress(s: str) -> str:
    decoded = []
    index = 0
    while index < len(s):
        char = s[index]
        index += 1
        count_start = index
        while index < len(s) and s[index].isdigit():
            index += 1
        count = int(s[count_start:index]) if index > count_start else 1
        decoded.append(char * count)
    return "".join(decoded)