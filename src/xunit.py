from typing import Optional


class TestCase:
    def __init__(self, name: str) -> None:
        self.name: str = name

    def set_up(self):
        pass

    def run(self) -> None:
        method = getattr(self, self.name)
        method()


class TestCaseTest(TestCase):
    def set_up(self):
        self.test = WasRun("test_method")

    def test_running(self):
        self.test.run()
        assert self.test.was_run

    def test_set_up(self):
        self.test.run()
        assert self.test.was_set_up


class WasRun(TestCase):
    def set_up(self):
        self.was_run: Optional[bool] = None
        self.was_set_up = 1

    def test_method(self) -> None:
        self.was_run = True


TestCaseTest("test_running").run()
TestCaseTest("test_set_up").run()
