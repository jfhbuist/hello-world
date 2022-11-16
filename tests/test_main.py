import pytest

def test_hello(capfd):    
    import hello
    out, err = capfd.readouterr()
    assert out == "Hello World!\n"    
