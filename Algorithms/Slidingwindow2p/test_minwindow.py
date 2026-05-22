import importlib.util
import pathlib
import sys


def _load_solution():
    repo_root = pathlib.Path(__file__).resolve().parents[2]
    mod_path = repo_root / "Algorithms" / "Slidingwindow2p" / "minwindowsubstring.py"
    spec = importlib.util.spec_from_file_location("minwindowsubstring", str(mod_path))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.Solution


def run_tests():
    Solution = _load_solution()
    sol = Solution()
    cases = [
        ["ADOBECODEBANC", "ABC"],
        ["a", "a"],
        ["a", "aa"],
    ]

    for i, (s, t) in enumerate(cases, 1):
        out = sol.minWindow(s, t)
        print(f"Test {i}: input={[s, t]} -> output={out!r}")


if __name__ == "__main__":
    run_tests()
