# Python module to deal with regular expressions
import re
from unittest import result
target_str = """Jessa is a Python developer,and her salary is 8000"""
print(target_str)
# re.X is Verbose flag.This flag allows more flexibility and better formatting when writing 
# more complex regex patterns between the parentheses of the match(), search(), or other regex methods.
result  = re.search(r"""(^\w{2,}) # match 2 or more lettered word at the start 
                    .+(\d{4}$) # match 4-digit number at the end """,target_str,re.VERBOSE)
print(result.group(1))
print(result.group(2))
# An example of regular expression compiling.
# args_pattern = re.compile(
#     r"""
#     ^
#     (
#     (--(?P<Help>help).*)|
#     ((?:-s|--seperator)\s(?P<SEP>.*?)\s)?
#     ((?P<OPT1>-?\d+))(\s(?P<OP2>-?\d+))?(\s(?P<OP3>-?\d+))?
#     )
#     $
#     """,
#     re.VERBOSE,
# )
