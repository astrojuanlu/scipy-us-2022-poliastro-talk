# $ numba --annotate-html numba_test.py

from poliastro.examples import iss

print(iss.propagate(iss.period))
