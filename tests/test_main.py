# test_main.py

def test_main(capfd):
    import main
    main.main()
    out, err = capfd.readouterr()
    assert out == "Hello World!\n"


def test_hello(capfd):
    import hello
    hello.say_hello()
    out, err = capfd.readouterr()
    assert out == "Hello World!\n"


def test_hello_unwrapped(capfd):
    import hello_unwrapped
    out, err = capfd.readouterr()
    assert out == "Hello World!\n"


def test_calculation():
    import calculate
    ans = 18
    out = calculate.do_calculation()
    assert out == ans
