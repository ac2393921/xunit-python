class WasRun:
    def __init__(self, name) -> None:
        self.was_run = None

    def run(self) -> None:
        self.test_method()

    def test_method(self) -> None:
        self.was_run = 1


test = WasRun("testMethod")
print(test.was_run)
test.run()
print(test.was_run)
