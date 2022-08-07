def generate():
    print("yeilding ")
    yield 3

    print("here ")
    yield 3

    print("and here ")
    yield 3

myGen = generate()
next(myGen)