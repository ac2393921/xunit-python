from typing import Optional


class TestCase:
    def __init__(self, name: str) -> None:
        self.name: str = name

    def set_up(self):
        pass

    def tear_down(self):
        pass

    def run(self) -> None:
        self.set_up()
        method = getattr(self, self.name)
        method()
        self.tear_down()


class TestCaseTest(TestCase):
    def set_up(self):
        self.test = WasRun("test_method")

    def test_running(self):
        self.test.run()
        assert self.test.was_run

    def test_template_method(self):
        self.test.run()
        assert "set_up test_method tear_down " == self.test.log


class WasRun(TestCase):
    def set_up(self):
        self.was_run: Optional[bool] = None
        self.was_set_up = 1
        self.log = "set_up "

    def test_method(self) -> None:
        self.was_run = True
        self.log = self.log + "test_method "

    def tear_down(self):
        self.log = self.log + "tear_down "


TestCaseTest("test_template_method").run()
