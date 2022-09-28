class TestSuite:
    def __init__(self):
        self.tests = []

    def add(self, test):
        self.tests.append(test)

    def run(self, result):
        for test in self.tests:
            test.run(result)


class TestResult:
    def __init__(self):
        self.run_count = 0
        self.error_count = 0

    def test_started(self):
        self.run_count += 1

    def test_failed(self):
        self.error_count += 1

    def summary(self):
        return f"{self.run_count} run, 0 failed"


class TestCase:
    def __init__(self, name: str) -> None:
        self.name: str = name

    def set_up(self):
        pass

    def tear_down(self):
        pass

    def run(self, result):
        result.test_started()
        self.set_up()
        try:
            method = getattr(self, self.name)
            method()
        except Exception:
            result.test_failed()
        self.tear_down()

    def test_suite(self):
        suite = TestSuite()
        suite.add(WasRun("test_method"))
        suite.add(WasRun("test_broken_method"))
        result = TestResult()
        suite.run(result)
        assert "2 run, 1 failed" == result.summary()


class TestCaseTest(TestCase):
    def set_up(self):
        self.result = TestResult()

    def test_running(self):
        self.test.run()
        assert self.test.was_run

    def test_template_method(self):
        test = WasRun("test_method")
        test.run(self.result)
        assert "set_up test_method tear_down " == test.log

    def test_result(self):
        test = WasRun("test_method")
        test.run(self.result)
        assert "1 run, 0 failed" == self.result.summary()

    def test_failed_result(self):
        test = WasRun("test_broken_method")
        test.run(self.result)
        assert "1 run, 1 failed" == self.result.summary()

    def test_failed_reuslt_formatting(self):
        self.result.test_started()
        self.result.test_failed()
        assert "1 run, 1 failed" == self.result.summary()

    def test_suit(self):
        suite = TestSuite()
        suite.add(WasRun("testMethod"))
        suite.add(WasRun("testBrokenMethod"))
        self.run(self.result)
        assert "2 run, 1 failed" == self.result.summary()


class WasRun(TestCase):
    def set_up(self):
        self.log = "set_up "

    def test_method(self) -> None:
        self.log = self.log + "test_method "

    def test_broken_method(self):
        raise Exception

    def tear_down(self):
        self.log = self.log + "tear_down "


suite = TestSuite()
suite.add(TestCaseTest("test_template_method"))
suite.add(TestCaseTest("test_result"))
suite.add(TestCaseTest("test_failed_result"))
suite.add(TestCaseTest("test_failed_result_formatting"))
suite.add(TestCaseTest("test_suite"))
result = TestResult()
suite.run(result)
print(result.summary)
