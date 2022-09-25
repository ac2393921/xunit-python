from typing import Optional


class WasRun:
    def __init__(self, name: str) -> None:
        self.was_run: Optional[bool] = None
        self.name: str = name

    def run(self) -> None:
        self.test_method()
        method = getattr(self, self.name)
        method()

    def test_method(self) -> None:
        self.was_run = True


test = WasRun("testMethod")
print(test.was_run)
test.run()
print(test.was_run)
