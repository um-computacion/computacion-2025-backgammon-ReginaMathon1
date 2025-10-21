# Automated Reports
## Coverage Report
```text
Name                   Stmts   Miss  Cover   Missing
----------------------------------------------------
core/__init__.py           0      0   100%
core/board.py             50     13    74%   43, 70, 93, 118-128
core/checker.py           19      1    95%   49
core/dice.py              27      9    67%   47-49, 58, 62-68
core/game.py             123     64    48%   61-83, 87-90, 94-119, 125-135, 139-165, 175, 180, 184, 198-202
core/player.py            32      1    97%   74
test/__init__.py           0      0   100%
test/test_board.py        61      1    98%   99
test/test_checker.py      40      1    98%   69
test/test_dice.py         52      3    94%   63-64, 84
test/test_game.py         74      1    99%   136
test/test_player.py       55      1    98%   93
----------------------------------------------------
TOTAL                    533     95    82%

```
## Pylint Report
```text
************* Module main.py
main.py:1:0: F0001: No module named main.py (fatal)
************* Module test.py
test.py:1:0: F0001: No module named test.py (fatal)

```
