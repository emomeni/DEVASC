from re import S


def capitalize(s: str) -> str:
    first, *other = s
    remaining = "".join(other)
    return first.upper() + remaining.lower()

def title_case(s: str) -> str:
    return s

#def title_case(s: str) -> str:
    #words = s.split(' ')
    #return ' '.join(capitalize(word) for word in words)
