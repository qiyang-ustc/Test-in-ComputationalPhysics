# This is an example of args.py file in an actual computational project (study a fermionic Hubbard chain at finite temperature)

import argparse
# If other modules need to use these variables, import variables in __all__ from args.py by:
# import * from args
__all__ = ['N', 'beta', 'U', 'krylov', 'dirname']

parser = argparse.ArgumentParser(description='some description to hint.')
parser.add_argument("--dir", default='/data/yangqi/cmpsfit/',help="where to store results. h5file")
parser.add_argument("--Krylov", type=int, default=20, help="Krylov space dimension")
parser.add_argument("--beta", type=float, default=8.0, help="Inverse temperature")
parser.add_argument("--N", type=int, default=16, help="Number of sites")
parser.add_argument("--U", type=float, default=4.0, help="U in Hubbard")

args = parser.parse_args()

# Default settings: extract variables.
N = args.N
beta = args.beta
U = args.U
krylov = args.Krylov
dirname = args.dir

# Have a try.
print(args)
print(N,beta,U,krylov,dirname)
