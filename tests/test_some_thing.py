""" tests for some_thing """

import pytest
from some_module import some_thing


class StubSomeThing():
    """
    simple stub class to show example use of monkeypatch, in this case incrementing counter
    to track how many times the patched functions were called, then returning dummy values -
    though this can be used to substitue any return values useful for a given test case
    """
    def __init__(self):
        self.do_some_thing_called = 0
        self.do_some_other_thing_called = 0
    def do_some_thing(self):
        """ count number of times called """
        self.do_some_thing_called += 1
        return "ok"
    def do_some_other_thing(self):
        """ count number of times called """
        self.do_some_other_thing_called += 1
        return "ok"


def test_do_some_thing_int():
    """ test do_some_thing with int """
    result = some_thing.do_some_thing(1)
    assert result == 1


def test_do_some_thing_string():
    """ test do_some_thing with string """
    result = some_thing.do_some_thing("ok")
    assert result == "ok"


def test_do_some_other_thing_int():
    """ test do_some_other_thing with int """
    result = some_thing.do_some_other_thing(1)
    assert result == 2


def test_do_some_other_thing_string():
    """ test do_some_other_thing with string """
    result = some_thing.do_some_other_thing("ok")
    assert result == "ok1"


def test_do_every_thing_int():
    """ test do_every_thing with 2 int values """
    result = some_thing.do_every_thing(3, 5)
    assert result == 9


def test_do_every_thing_string():
    """ test do_every_thing with 2 string values """
    result = some_thing.do_every_thing("yes", "no")
    assert result == "yesno1"


def test_do_every_thing_error():
    """ test do_every_thing with 1 int, 1 string in which case a ValueError is expected """
    with pytest.raises(ValueError):
        some_thing.do_every_thing("yes", "1")


def test_do_every_thing_confirm_functions_called(monkeypatch):
    """ test do_every_thing with functions overriden by monkeypatch to confirm they are called """
    stub = StubSomeThing()
    monkeypatch.setattr(some_thing, "do_some_thing", stub.do_some_thing)
    monkeypatch.setattr(some_thing, "do_some_other_thing", stub.do_some_other_thing)
    result = some_thing.do_every_thing("ok", "ok")
    assert result == "okok"
    assert stub.do_some_thing_called == 1
    assert stub.do_some_other_thing_called == 1
