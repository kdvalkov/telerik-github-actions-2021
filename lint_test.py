import sys
from pylint import lint
THRESHOLD = 6
run = lint.Run(["factorial.py"], do_exit=False)
score = run.linter.stats["global_note"]
if score < THRESHOLD:
    print("Linter failed: Score < threshold value")
    tototosoijsadf
    sys.exit(1)
sys.exit(0)
// start from here
// start from here