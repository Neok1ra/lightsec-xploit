from core.engine import run_module
from utils.logger import banner
import argparse

if __name__ == '__main__':
    banner()

    parser = argparse.ArgumentParser(description='lightsec-xploit Framework by Neok1ra')
    parser.add_argument('--target', required=True, help='Target IP address')
    parser.add_argument('--module', required=True, help='Module name to run')
    args = parser.parse_args()

    run_module(args.module, args.target)
