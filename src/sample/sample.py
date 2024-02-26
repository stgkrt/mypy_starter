def add_number(a,b):
    return a+b

def concat_number(a:int,b:int) -> str:
    a = str(a)
    b = str(b)
    return a+b

def add_ifneed(a:int | None, b:int) -> int:
    c = a + b
    return c

