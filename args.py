import argparse
# If other modules need to use these variables, import variables in __all__ from args.py by:
# import * from args
__all__ = ['chi', 'beta', 'U', 'krylov', 'dirname','V','D','N']

parser = argparse.ArgumentParser(description='some description to hint.')
parser.add_argument("--dir", default='/data/yangqi/cmpsfit/',help="where to store results. h5file")
parser.add_argument("--Krylov", type=int, default=20, help="Krylov space dimension")
parser.add_argument("--beta", type=float, default=8.0, help="Inverse temperature")
parser.add_argument("--chi", type=int, default=16, help="virtual bond dimension of bath")
parser.add_argument("--U", type=float, default=4.0, help="U in Hubbard")

parser.add_argument("--D", type=float, default=100.0, help="QMC Wilson width")
parser.add_argument("--V", type=float, default=10.0, help="QMC coupling strength, to be sqrt(D)")

args = parser.parse_args()

# Default settings: extract variables.
chi = args.chi
beta = args.beta
U = args.U
krylov = args.Krylov
dirname = args.dir

# Have a try.
print(args)
print(chi,beta,U,krylov,dirname)
