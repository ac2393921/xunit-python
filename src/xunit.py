from typing import Optional


class TestCase:
    def __init__(self, name: str) -> None:
        self.name: str = name

    def run(self) -> None:
        method = getattr(self, self.name)
        method()


class TestCaseTest(TestCase):
    def test_running(self):
        test = WasRun("test_method")
        assert not test.was_run
        test.run()
        assert test.was_run


class WasRun(TestCase):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.was_run: Optional[bool] = None

    def test_method(self) -> None:
        self.was_run = True


TestCaseTest("test_running").run()
