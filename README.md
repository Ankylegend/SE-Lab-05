Issue	Type	Line(s)	Description	Fix Approach
Mutable Default Argument	Pylint (W0102)	8	Dangerous default value [] as argument. The logs list was shared across all function calls.	Changed the default value to None and initialized logs = [] inside the function.
Bare except: Clause	Pylint (W0702), Flake8 (E722)	19	No exception type(s) specified. This hides all bugs.	Replaced the bare except: with except KeyError: and added a print statement for user feedback.
Insecure Use of eval()	Pylint (W0123), Bandit (B307)	59	Use of eval. This is a major security vulnerability.	Removed the entire eval("print('eval used')") line.
Poor Resource Management	Pylint (R1732)	26, 32	Consider using 'with'. Files were not opened using a context manager.	Replaced the f = open() and f.close() calls with with open(...) as f: in load_data and save_data.
Unused Import	Pylint (W0611), Flake8 (F401)	2	Unused import logging.	Removed the import logging line.
Input Validation	Runtime (TypeError)	53	Code crashed with TypeError when adding (123, "ten").	Added isinstance() check in add_item to validate qty is a number.
Use of global Statement	Pylint (W0603)	27, 82	Using the global statement. Pylint discourages modifying globals from within functions.	Refactored the entire program to pass the stock dictionary as an argument to functions instead of using a global variable.
Missing Docstrings	Pylint (C0114, C0116)	1, 8, etc.	Missing module docstring and Missing function or method docstring.	Added docstrings ("""...""") to the top of the module and for every function.
Naming Convention	Pylint (C0103)	8, 14, etc.	Function name "addItem" doesn't conform to snake_case naming style.	Renamed all functions from camelCase to snake_case (e.g., addItem became add_item).
Missing Encoding	Pylint (W1514)	26, 32	Using open without explicitly specifying an encoding.	Added encoding="utf-8" to both with open(...) statements.
Missing Blank Lines	Flake8 (E302, E305)	8, 14, etc.	expected 2 blank lines. PEP 8 requires two blank lines between functions.	Added the required two blank lines between all function definitions.
Line Too Long	Flake8 (E501)	21, 54	line too long. Lines exceeded the 79-character limit.	Broke the long print statements onto multiple lines.
String Formatting	Pylint (C0209)	12	Formatting a regular string which could be an f-string.	Changed the string concatenation in add_item to use an f-string.
Final Newline Missing	Pylint (C0304), Flake8 (W292)	100-101	Final newline missing / no newline at end of file.	Added a single blank line to the very end of the file.
Trailing Whitespace	Flake8 (W293)	101	blank line contains whitespace. The final blank line had spaces on it.	Removed the trailing whitespace from the final blank line.
