***

### 1. Which issues were the easiest to fix, and which were the hardest? Why?

* **Easiest:** The easiest issues to fix were the low-severity style and formatting errors flagged by Flake8 and Pylint, such as `F401: Unused import`, `E302: Expected 2 blank lines`, or `C0304: Final newline missing`. These were easy because they required minimal thought and were simple, mechanical changes (like deleting a line or adding a newline).
* **Hardest:** The hardest issue to fix was the `W0603: Using the global statement`. This was the most difficult because it wasn't a one-line bug fix; it required a complete **architectural refactor** of the entire program. We had to change the function definitions and call sites for almost every function to pass the `stock` dictionary as an argument, which was far more complex than fixing any of the high-severity bugs.

### 2. Did the static analysis tools report any false positives? If so, describe one example.

No, I did not encounter any clear false positives during this lab. The `inventory_system.py` file contained genuine issues that were all correctly identified by the tools.

* The critical bugs flagged by Pylint, like the **Mutable Default Argument (W0102)** and the **Bare `except:` (W0702)**, were legitimate logic flaws.
* The **`eval()` use (B307)** flagged by Bandit was a valid, high-risk security vulnerability.
* All style and convention errors from Flake8 and Pylint were correct violations of PEP 8 style guidelines.

### 3. How would you integrate static analysis tools into your actual software development workflow?

I would integrate them in two key places to create a comprehensive quality net:

* **Local Development:** I would integrate Pylint, Flake8, and Bandit directly into my code editor (IDE) to get **real-time feedback** as I type. I would also set up a **pre-commit hook**, which automatically runs all three tools on my code before I'm allowed to commit. This blocks low-quality or insecure code from ever entering the repository.
* [cite_start]**Continuous Integration (CI):** I would configure a CI pipeline (like GitHub Actions) to automatically run all static analysis tools every time code is pushed or a pull request is opened[cite: 88]. This acts as a "quality gate" for the whole team, automatically **failing the build** if any high-severity security issues are found or if the code quality score drops below a set threshold.

### 4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?

The improvements were significant and tangible across three main areas:

* **Robustness:** The code is far more stable. We eliminated critical bugs like the **bare `except:`** and the **mutable default argument**. We also removed the **`eval()` security hole** and added **input validation** to prevent the `TypeError` runtime crash.
* **Maintainability:** This saw the biggest improvement. By **eliminating the global variable**, the code no longer has hidden side effects. [cite_start]Functions are now "pure" (operating only on given inputs), which makes them drastically easier to test, debug, and safely modify in the future[cite: 17].
* [cite_start]**Readability:** The code now adheres to professional PEP 8 standards[cite: 26]. [cite_start]The use of consistent `snake_case` naming, proper spacing, and descriptive **docstrings** for every function makes the code's intent clear and easy for any developer to understand[cite: 17].