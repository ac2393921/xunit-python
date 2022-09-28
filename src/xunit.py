from typing import List


class TestResult:
    def __init__(self) -> None:
        self.run_count: int = 0
        self.error_count: int = 0

    def test_started(self) -> None:
        self.run_count += 1

    def test_failed(self) -> None:
        self.error_count += 1

    def summary(self) -> str:
        return f"{self.run_count} run, 0 failed"


class TestCase:
    def __init__(self, name: str) -> None:
        self.name: str = name

    def set_up(self) -> None:
        pass

    def tear_down(self) -> None:
        pass

    def run(self, result: TestResult) -> None:
        result.test_started()
        self.set_up()
        try:
            method = getattr(self, self.name)
            method()
        except Exception:
            result.test_failed()
        self.tear_down()

    def test_suite(self) -> None:
        suite = TestSuite()
        suite.add(WasRun("test_method"))
        suite.add(WasRun("test_broken_method"))
        result = TestResult()
        suite.run(result)
        assert "2 run, 1 failed" == result.summary()


class TestCaseTest(TestCase):
    def set_up(self) -> None:
        self.result: TestResult = TestResult()

    def test_template_method(self) -> None:
        test = WasRun("test_method")
        test.run(self.result)
        assert "set_up test_method tear_down " == test.log

    def test_result(self) -> None:
        test = WasRun("test_method")
        test.run(self.result)
        assert "1 run, 0 failed" == self.result.summary()

    def test_failed_result(self) -> None:
        test = WasRun("test_broken_method")
        test.run(self.result)
        assert "1 run, 1 failed" == self.result.summary()

    def test_failed_reuslt_formatting(self) -> None:
        self.result.test_started()
        self.result.test_failed()
        assert "1 run, 1 failed" == self.result.summary()

    def test_suit(self) -> None:
        suite = TestSuite()
        suite.add(WasRun("testMethod"))
        suite.add(WasRun("testBrokenMethod"))
        self.run(self.result)
        assert "2 run, 1 failed" == self.result.summary()


class WasRun(TestCase):
    def set_up(self) -> None:
        self.log: str = "set_up "

    def test_method(self) -> None:
        self.log: str = self.log + "test_method "

    def test_broken_method(self):
        raise Exception

    def tear_down(self) -> None:
        self.log: str = self.log + "tear_down "


class TestSuite:
    def __init__(self) -> None:
        self.tests: List[TestCaseTest] = []

    def add(self, test: TestCaseTest) -> None:
        self.tests.append(test)

    def run(self, result: TestResult) -> None:
        for test in self.tests:
            test.run(result)


suite = TestSuite()
suite.add(TestCaseTest("test_template_method"))
suite.add(TestCaseTest("test_result"))
suite.add(TestCaseTest("test_failed_result"))
suite.add(TestCaseTest("test_failed_result_formatting"))
suite.add(TestCaseTest("test_suite"))
result = TestResult()
suite.run(result)
print(result.summary)
