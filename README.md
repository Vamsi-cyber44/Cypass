# Cypass
A fast and lightweight Python-based password generator for Linux terminal users. Supports flags for password length, limits, and random generation. Ideal for cybersecurity learners and ethical hacking practice. Simple, customizable, and easy to run on Kali Linux or any Python 3 environment.

# CyPass - Personal Wordlist Generator 🕶

**CyPass** is a high-efficiency reconnaissance tool designed for ethical penetration testers and security professionals. It generates highly probable password lists based on personal information (like names, nicknames, and dates of birth), targeting common human password patterns with maximum coverage.

*Disclaimer: This tool is intended strictly for authorized security assessments (penetration testing) where explicit permission has been granted (e.g., against corporate assets where you are authorized to conduct security testing).*

---

## Logo

While true color is not supported directly in standard Markdown, here is a clear ASCII representation of the CyPass logo:

       .-"""-.
     / -   -  \
    |  .-. .- |
    |  \o| |o (
    \     ^   /
     '.  )- .'
       '-.-'
      CyPass MODE ACTIVE





Features
Pattern-Based Generation: Uses 8 high-probability password patterns, including Leet Speak, date variations, and complex combinations.
Exhaustive Numeric Coverage: Includes every 2-digit (00-99) and every 3-digit (000-999) number combined with base words and separators (e.g., Tanzil@123, Tanzil-99).
Case and Complexity Variations: Automatically tests case mutations, common separators (@, !, #), and combined base words.
Flexible Output: Supports .txt, .csv, and .json output formats.

Installation and Usage
CyPass is a single Python script and requires no external libraries beyond standard Python modules.

Prerequisites
You need Python 3 installed on your system.

Git Clone and Setup

git clone https://github.com/Vamsi-cyber44/Cypass.git
cd CyPass
python3 CyPass.py --help






Basic Usage
You can run the script interactively or pass all necessary parameters via command-line flags.

Interactive Mode Example:

python3 CyPass.py 
# The script will prompt you for Name, DOB, Nickname, etc.





Flag,Argument,Description,Required,Example Input
-n / --name,<Name>,Target's Primary Name,Yes,-n Vamsi
-d / --dob,<Date>,Date of Birth (YYYYMMDD),Yes,-d 20061116
-k / --nick,<Nickname>,Target's Nickname,Yes,-k Cypher
-r / --related,<Words>,Related names (comma separated),No,"-r Sarah,PetName"
-l / --lucky,<Code>,Lucky number or code,No,-l 777
-o / --output,txt/csv/json/all,Output file format,No (Default: txt),-o all


Advanced Example
Generate a wordlist for "Vishnu" (DOB 2005/11/14) with nickname "Cypher", related name "Sarah", and lucky number "777", outputting all formats:
python3 CyPass.py \
    -n Vishnu \
    -d 20051114 \
    -k Cypher \
    -r Sarah \
    -l 777 \
    -o all
This will create a comprehensive wordlist in all three formats (wordlist.txt, wordlist.csv, and wordlist.json) containing over a hundred thousand highly probable password candidates.

Algorithm Summary
CyPass employs a sophisticated 8-Pattern generation algorithm:

Base + Decorator: Simple joins (e.g., Vamsi2006).
Base + Separator + Numeric Decorator: The most critical pattern: Combines every permutation of base words, common separators (@, #, !), and the expanded set of 2- and 3-digit numbers (00-999).
Base + Separator + Date + Separator: Vamsi@2006# style.
Combined Base Words: MaxySarah2006.
Common Suffixes on Primary: Vamsi2006!.
Common Prefixes: 2006@Vamsi.
Complex Dual-Base Pattern: BaseWord1@BaseWord2Year (e.g., Vamsi@Cypher2006).
Static High-Hit List: Industry-standard common passwords.

License
This project is licensed under the Apache2.0 License.

Author
Vamsi Krishna - An CyberSecurity Student.
