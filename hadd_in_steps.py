import subprocess
import os
import sys
import argparse

parser  = argparse.ArgumentParser()
parser.add_argument("--output", required=True)
parser.add_argument("--inputs", required=True, nargs="+")
parser.add_argument("-n", "--numBatch", default=2, type=int)
args = parser.parse_args()

inputs = args.inputs
n = args.numBatch

for i in range(0, len(inputs), n):
    step = min(i + n, len(inputs))
    if i == 0:
        subprocess.run(["hadd", "-ff", args.output] + inputs[i:step])
    else:
        subprocess.run(["hadd", "-a", args.output] + inputs[i:step])
