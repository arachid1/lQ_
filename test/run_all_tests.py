from pathlib import Path
import unittest


def main():
    UNITTEST_DIR_PATH = str(Path().absolute() / "test_scripts")
    loader = unittest.TestLoader()

    suites = loader.discover(UNITTEST_DIR_PATH)
    runner_kwargs = {"verbosity": 3}
    runner = unittest.TextTestRunner(**runner_kwargs)
    result = runner.run(suites)


if __name__ == "__main__":
    main()
