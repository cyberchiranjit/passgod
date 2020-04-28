# PassGod
PassGod is a tool to assist you to create a custom wordlist based on the victim's information.
______________________________________________________________________________________________________________

# Requirements
1. Python3

_________________________________________________________________________________________________________________

# Installation Guide

$ git clone https://github.com/cyberchiranjit/passgod/ 

__________________________________________________________________________________________________________________

# Usage
usage: passgod.py [-h] [-chr CHARS] [-min MIN_LENGTH] [-max MAX_LENGTH]
               [-out OUTPUT]

Python Wordlist Generator

optional arguments:
  -h, --help           		 		show this help message and exit

  -chr CHARS, --chars CHARS	 		characters to iterate
                        
  -min MIN_LENGTH, --min_length MIN_LENGTH	minimum length of characters
                        
  -max MAX_LENGTH, --max_length MAX_LENGTH      maximum length of characters
                       
  -out OUTPUT, --output OUTPUT			output of wordlist file.
                       

### Example

$ python3 passgod.py -chr=abc -min=1 -max=4 -out=output/wordlist.txt

# or

$ python3 passgod.py --chars=abc --min_length=1 --max_length=4 --output=output/password.txt


