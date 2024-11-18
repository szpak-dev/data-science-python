import argparse


parser = argparse.ArgumentParser(description='Program that teaches us args')
parser.add_argument('--mode', help='Program mode', type=str, default='list_view')

args = parser.parse_args()
print(args.mode)
