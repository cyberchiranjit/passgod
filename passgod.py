#!/usr/bin/python3

import os
import sys
import time
import string
import argparse
import itertools

# Banner Block

print("     							                        ")
print("\033[1;31;40m|  _ \ / \  / ___/ ___|   / ___|/ _ \|  _ \ \033[1;31;40m")
print("\033[1;31;40m| |_) / _ \ \___ \___ \  | |  _| | | | | | |\033[1;31;40m ")
print("\033[1;31;40m|  __/ ___ \ ___) |__) | | |_| | |_| | |_| |\033[1;31;40m ")
print("\033[1;31;40m|_| /_/   \_\____/____/   \____|\___/|____/ \033[1;31;40m")
print("\n")

print("\033[07m[ Chiranjit Ghosh | chiranjitofficial.tk | instagram.com/cyberchiranjit]\033[27m  ")
print("\n")

# Processing Block



def createpassword(chrs, min_length, max_length, output):

    if min_length > max_length:
        print ("[!] Please `min_length` must smaller or same as with `max_length`")
        sys.exit()

    if os.path.exists(os.path.dirname(output)) == False:
        os.makedirs(os.path.dirname(output))

    print ('[+] Creating password at `%s`...' % output)
    print ('[i] Starting time: %s' % time.strftime('%H:%M:%S'))

    output = open(output, 'w')

    for n in range(min_length, max_length + 1):
        for xs in itertools.product(chrs, repeat=n):
            chars = ''.join(xs)
            output.write("%s\n" % chars)
            sys.stdout.write('\r[+] saving character `%s`' % chars)
            sys.stdout.flush()
    output.close()

    print ('\n[i] End time: %s' % time.strftime('%H:%M:%S'))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        description='                \033[1;32;40m++++++Generating Your Custom Wordlist++++++ \n')
    parser.add_argument(
        '-chr', '--chars',
        default=None, help='characters to iterate')
    parser.add_argument(
        '-min', '--min_length', type=int,
        default=1, help='minimum length of characters')
    parser.add_argument(
        '-max', '--max_length', type=int,
        default=2, help='maximum length of characters')
    parser.add_argument(
        '-out', '--output',
        default='output/password.txt', help='output of password file.')

    args = parser.parse_args()
    if args.chars is None:
        args.chars = string.printable.replace(' \t\n\r\x0b\x0c', '')
    createpassword(args.chars, args.min_length, args.max_length, args.output)
