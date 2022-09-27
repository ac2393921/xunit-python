from typing import Optional


class TestResult:
    def __init__(self):
        self.run_count = 0

    def test_started(self):
        self.run_count = self.run_count + 1

    def summary(self):
        return f"{self.run_count} run, 0 failed"


class TestCase:
    def __init__(self, name: str) -> None:
        self.name: str = name

    def set_up(self):
        pass

    def tear_down(self):
        pass

    def run(self):
        result = TestResult()
        result.test_started()
        self.set_up()
        method = getattr(self, self.name)
        method()
        self.tear_down()
        return result


class TestCaseTest(TestCase):
    def set_up(self):
        self.test = WasRun("test_method")

    def test_running(self):
        self.test.run()
        assert self.test.was_run

    def test_template_method(self):
        self.test.run()
        assert "set_up test_method tear_down " == self.test.log

    def test_result(self):
        test = WasRun("test_method")
        result = test.run()
        assert "1 run, 0 failed" == result.summary()

    def test_failed_result(self):
        test = WasRun("test_broken_method")
        result = test.run()
        assert "1 run, 1 failed" == result.summary()


class WasRun(TestCase):
    def set_up(self):
        self.was_run: Optional[bool] = None
        self.was_set_up = 1
        self.log = "set_up "

    def test_method(self) -> None:
        self.was_run = True
        self.log = self.log + "test_method "

    def test_broken_method(self):
        raise Exception

    def tear_down(self):
        self.log = self.log + "tear_down "


TestCaseTest("test_template_method").run()
TestCaseTest("test_result").run()
TestCaseTest("test_failed_result").run()
