import argparse

parser = argparse.ArgumentParser(
    description='This is a PyMOTW sample program'
)

parser.add_argument('-a', action="store_true", default=False)

print(parser.parse_args(['-a', '-bval', '-c', '3']))
