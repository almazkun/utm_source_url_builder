from urllib.parse import quote


def all_to_bytes(some_type):
    """Makes UTF-8 string from bytes, int, float"""
    if isinstance(some_type, bytes):
        return some_type
    elif isinstance(some_type, int):
        return str(some_type).encode()
    elif isinstance(some_type, float):
        return str(some_type).encode()
    else:
        return some_type.encode()


def all_to_str(some_bytes):
    """Make STR encoded UTF-8"""
    return all_to_bytes(some_bytes).decode(encoding="utf-8")


def urllizer(some_string):
    return quote(all_to_str(some_string))
