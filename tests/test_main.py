# test_main.py

def test_hello(capfd):
    import hello
    hello.say_hello()
    out, err = capfd.readouterr()
    assert out == "Hello World!\n"


def test_hello_unwrapped(capfd):
    import hello_unwrapped
    out, err = capfd.readouterr()
    assert out == "Hello World!\n"
