#!/usr/bin/env python3
import itertools
import random
import string
import time
import sys
import argparse
import json
import csv
import re

# ANSI Color Codes
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"

# ==========================
# HACKER ANIMATION
# ==========================
def animate(text, delay=0.02, end="\n"):
    """Prints text with a 'typing' animation effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(end)
    sys.stdout.flush()

# ==========================
# HACKER MASK + BANNER
# ==========================
def mask_logo():
    print(GREEN + r"""
        .-\"\"\"-.
       / -   -  \
      |  .-. .- |
      |  \o| |o (
      \     ^   /
       '.  )- .'
         '-.-'
        CyPass MODE ACTIVE
    """ + RESET)

def banner():
    animate("\nInitializing CyPass...", 0.02)
    animate("Loading modules...", 0.02)
    time.sleep(0.4)

    mask_logo()

    print(GREEN + r"""
      ██████╗ ██╗   ██╗██████╗  █████╗ ███████╗███████╗
     ██╔════╝ ██║   ██║██╔══██╗██╔══██╗██╔════╝██╔════╝
     ██║      ██║   ██║██████╔╝███████║███████╗█████╗  
     ██║      ██║   ██║██╔══██╗██╔══██║╚════██║██╔══╝  
     ╚██████╗ ╚██████╔╝██████╔╝██║  ██║███████║███████╗
      ╚═════╝  ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝
                   🕶 CyPass Wordlist Gen 🕶
    """ + RESET)

    print(RED + r"""
          ██████╗ ██╗   ██╗██████╗  █████╗ ███████╗
         ██╔════╝ ██║   ██║██╔══██╗██╔══██╗██╔════╝
         ██║      ██║   ██║██████╔╝███████║███████╗
         ██║      ██║   ██║██╔══██╗██╔══██║╚════██║
         ╚██████╗ ╚██████╔╝██████╔╝██║  ██║███████║
          ╚═════╝  ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝
    """ + RESET)

    time.sleep(0.3)
    animate("System Ready.\n", 0.02)


# ==========================
# FINAL HIGH-PREDICTIVE STRONG PASSWORD GENERATOR (Tier 1: Targeted Human Combinations)
# ==========================
def strong_passwords(name, dob, nickname, related, lucky):
    """
    Generates a high-probability password list for authorized
    personal-information-based attacks, covering all common human patterns.
    """
    
    # Symbols and sequences highly favored by humans in passwords
    HIGH_PROBABILITY_SUFFIXES = [
        "1", "123", "!", "!!", "01", "09", "99", "pass", "login", "welcome", "2024", "2025", 
        "1", "2", "3", "4", "5", "6", "7", "8", "9",
        "123", "321", "1234", "4321", "678", "789", "890", "987", "654", "007", "911", "000"
    ]

    # Curated numbers/codes based on high-hit rate observation
    HIGH_HIT_RATE_NUMBERS = set([
        '00', '01', '10', '11', '12', '21', '22', '33', '44', '55', '66', '77', '88', '99', 
        '000', '111', '222', '333', '444', '555', '666', '777', '888', '999',
        '123', '234', '345', '456', '789', '987', '654', '543', '432', '321', '098', 
        '100', '200', '300', '400', '500', '1990', '1995', '2005', '2006', '2023', '2024'
    ])
    for i in range(100):
        HIGH_HIT_RATE_NUMBERS.add(f"{i:02d}")
    
    # Common Leet Speak substitutions (lowercased)
    LEET_MAP = {
        'a': ['4', '@'], 'e': ['3'], 'i': ['1', '!'], 'o': ['0'],
        's': ['5', '$'], 't': ['7', '+'], 'l': ['1', 'l'], 'z': ['2']
    }
    
    # Date formatting for common human patterns
    year = dob[0:4]
    month = dob[4:6]
    day = dob[6:8]
    fulldate = dob      # YYYYMMDD
    revdate = day + month + year # DDMMYYYY (The crucial format for many human-chosen passwords)
    
    strong_list = set() 

    # --- 1. BASE WORD GENERATION (The "Name" component with variations) ---
    base_words = set()
    temp_bases = [name, nickname] + related
    if lucky:
        temp_bases.append(lucky)
        
    def apply_leet(w):
        leets = {w}
        for original in ['a', 'e', 'i', 'o', 's']:
            if original in w:
                for sub in LEET_MAP.get(original, []):
                    leets.add(w.replace(original, sub, 1))
        return leets
        
    for word in temp_bases:
        if not word or not isinstance(word, str) or not word.isascii(): continue
        word = word.strip().replace(" ", "")
        
        # Case variations (Vamsi, vamsi, VAMSI)
        base_words.add(word)
        base_words.add(word.lower())
        base_words.add(word.upper())
        base_words.add(word.capitalize())
        
        # Leet speak variations
        base_words.update(apply_leet(word.lower()))

    # --- 2. DECORATOR AND DATE LISTS ---
    date_decorators = [year, revdate, fulldate] 
    date_decorators.extend(["2024", "2025"]) 
    
    if lucky and isinstance(lucky, str):
        date_decorators.append(lucky)
    
    combinable_decorators = set(date_decorators)
    combinable_decorators.update(HIGH_HIT_RATE_NUMBERS) 
    
    # --- 3. PATTERN GENERATION (The core predictive combinations) ---
    
    for base in base_words:
        # Pattern 1: Base + Decorator 
        for decorator in HIGH_PROBABILITY_SUFFIXES:
            strong_list.add(f"{base}{decorator}") 

        # Pattern 2: Base + Separator + Numeric Decorator (Vamsi@2006)
        for d in combinable_decorators:
            for s in ["@", "#", "!", "_"]: 
                strong_list.add(f"{base}{s}{d}") 

                # Pattern 3: The double-separator format (Vamsi@16112006#)
                # This is highly targeted at common corporate/human patterns
                for s2 in ["#", "!", "$"]:
                    if d in [revdate, fulldate]: # Only for full dates/years
                        strong_list.add(f"{base}{s}{d}{s2}")
                    
        # Pattern 4: Combined Base Words (VamsiCypher2006, Vamsi@Cypher2006)
        for related_word in temp_bases:
            if related_word and related_word.strip().lower() != base.lower() and isinstance(related_word, str):
                related_word_clean = related_word.lower().replace(" ", "")
                for y in date_decorators:
                    strong_list.add(f"{base}{related_word_clean}{y}") 
                    for s in ["@", "#"]:
                        strong_list.add(f"{base}{s}{related_word_clean}{y}")


    # Convert to list before appending to allow the final guarantee hook to work cleanly
    return list(p for p in strong_list if len(p) >= 8)

# ==========================
# NORMAL PASSWORDS (Auxiliary Combinatorics) (Tier 2/Fallback)
# ==========================
def generate_normal_passwords(base, dob, dob_year, lucky_number):
    """Generates simple combinations from base words and personal data."""
    # This remains largely unchanged to add breadth to the list
    specials = ["@", "#", "_", ".", "123", "!"]
    pw = set()

    # Create various case combinations from the base set
    base_lower = set([w.lower().replace(" ", "") for w in base if isinstance(w, str)])
    base_cap = set([w.capitalize() for w in base_lower])
    
    
    for w in base_lower | base_cap:
        if not w: continue
        pw.add(w)
        for s in specials:
            pw.add(w + s)
            pw.add(w + s + dob_year) 
            pw.add(s + w)

    # All permutations of two base words (use lower for simplicity)
    base_words_for_perm = list(base_lower | base_cap)
    for x, y in itertools.permutations(base_words_for_perm[:5], 2): # Limit permutations to prevent list explosion
        pw.add(x + y)
        pw.add(x.capitalize() + y.capitalize())

    # Base + Date combinations
    for w in base_lower:
        pw.add(w + dob)
        pw.add(dob + w)
        pw.add(w + dob_year)
        pw.add(dob_year + w)
        pw.add(w.capitalize() + dob_year)


    if lucky_number:
        for w in base_lower:
            pw.add(w + lucky_number)
            pw.add(lucky_number + w)

    return list(p for p in pw if len(p) >= 8) # Filter normal list too

# ==========================
# STATIC HIGH-PROBABILITY PASSWORDS (Tier 0: Global Common)
# ==========================
GLOBAL_HIGH_PROBABILITY = [
    "password", "Password", "Password1", "Password!", "qwerty", "Qwerty", "qwerty123",
    "123456", "12345678", "123456789", "111111", "000000",
    "Welcome1", "Welcome!", "Welcome@", "admin123", "Admin123",
    "iloveyou", "ILoveYou", "changeme", "ChangeMe!", "secret", "Secret1",
    "summer", "Summer2023", "fall", "Fall2023", "winter", "Winter2023", "spring", "Spring2023",
    "QWERTY", "ASDFGH", "ChangeMe", "SystemAdmin", "MyPassword"
]

# ==========================
# SAVE HELPERS (NO HEADINGS)
# ==========================
def save_txt(all_pw, base_filename):
    filename = f"{base_filename}.txt"
    with open(filename, "w") as f:
        for p in all_pw:
            f.write(p + "\n")
    print(f"\n[{GREEN}+{RESET}] TXT saved -> {CYAN}{filename}{RESET}")

def save_csv(all_pw, base_filename):
    filename = f"{base_filename}.csv"
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["password"])
        for p in all_pw:
            writer.writerow([p])
    print(f"[{GREEN}+{RESET}] CSV saved -> {CYAN}{filename}{RESET}")

def save_json(all_pw, base_filename):
    filename = f"{base_filename}.json"
    with open(filename, "w") as f:
        json.dump(all_pw, f, indent=4)
    print(f"[{GREEN}+{RESET}] JSON saved -> {CYAN}{filename}{RESET}")

# ==========================
# ARGPARSE (KALI-STYLE FLAGS)
# ==========================
def parse_args():
    parser = argparse.ArgumentParser(
        prog="CyPass",
        description="CyPass - Personal Wordlist Generator (safe use only)",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("-n", "--name", help="Target user's name (for targeting and filename)")
    parser.add_argument("-d", "--dob", help="DOB YYYYMMDD or YYYY-MM-DD")
    parser.add_argument("-k", "--nick", help="Target user's nickname")
    parser.add_argument("-r", "--related", help="Related names (comma separated, e.g., pet, spouse, child)")
    parser.add_argument("-l", "--lucky", help="Lucky number or code")
    parser.add_argument(
        "-m", "--max-passwords", 
        type=int, 
        default=0, # Default to 0, meaning no maximum limit
        help="Maximum number of passwords to output (0 for no limit)"
    )
    parser.add_argument(
        "-o", "--output",
        help="Output format",
        choices=["txt", "csv", "json", "all"],
        default="txt"
    )
    return parser.parse_args()

# ==========================
# MAIN
# ==========================
def main():
    banner()
    args = parse_args()
    max_limit = args.max_passwords

    animate("Collecting your personal inputs...\n", 0.03)

    # Input gathering with coloring
    name = (args.name or input(f"[{BLUE}INPUT{RESET}] Enter Target Name : ").strip())
    dob_raw = args.dob or input(f"[{BLUE}INPUT{RESET}] Enter DOB (YYYYMMDD): ").strip()
    nickname = (args.nick or input(f"[{BLUE}INPUT{RESET}] Enter Nickname : ").strip())
    related_raw = args.related or input(f"[{BLUE}INPUT{RESET}] Enter Related Names : ").strip()
    lucky_input = args.lucky or input(f"[{BLUE}INPUT{RESET}] Enter Lucky Number/Code (optional): ").strip()

    # Pre-process name for safe filename
    filename_base = re.sub(r'[^\w\.-]', '', name.lower()).strip()
    if not filename_base:
        filename_base = "wordlist"
    
    # Dynamic Limit Check if not provided by flag
    if max_limit == 0:
        limit_input = input(f"[{RED}INPUT{RESET}] Enter Maximum Password Limit (e.g., 5000, {CYAN}0 for no limit{RESET}): ").strip()
        try:
            max_limit = int(limit_input)
        except ValueError:
            max_limit = 0
            animate(f"[{RED}!{RESET}] Invalid limit specified. Proceeding without a maximum limit.\n", 0.02)


    # Pre-processing DOB
    dob = dob_raw.replace("-", "")
    if len(dob) != 8 or not dob.isdigit():
        animate(f"[{RED}!{RESET}] Warning: DOB format must be YYYYMMDD. Using placeholder 19700101.\n", 0.02)
        dob = "19700101"
              
    dob_year = dob[0:4]
    lucky_number = lucky_input if lucky_input else None

    # Process related names, stripping them
    related_names = [r.strip() for r in related_raw.split(",") if r.strip()]

    # Collect all base word components
    base = set([
        name, nickname,
        name.lower(), nickname.lower(),
        name.capitalize(), nickname.capitalize(),
        dob, dob_year, dob[2:4] 
    ] + related_names)
    
    base.discard("")

    if lucky_number:
        base.add(lucky_number)

    animate(f"Generating human-style passwords with priority. File: {filename_base}. Limit: {max_limit if max_limit > 0 else 'None'}...\n", 0.02)

    # Run both password generation functions
    strong_pw = strong_passwords(name, dob, nickname, related_names, lucky_number)
    normal_pw = generate_normal_passwords(base, dob, dob_year, lucky_number)

    # --- HIGH-CONFIDENCE PRIORITY MERGE LOGIC ---
    
    # 1. Tier 0: Global most common passwords (Highest Priority)
    all_pw_final = list(p for p in GLOBAL_HIGH_PROBABILITY if len(p) >= 8)
    
    # 2. Tier 1: Context-specific personal patterns (Your highly targeted list)
    
    # *** ABSOLUTE GUARANTEE FOR CRITICAL USER PATTERNS ***
    if dob and len(dob) == 8:
        # DDMMYYYY is derived from YYYYMMDD
        revdate = dob[6:8] + dob[4:6] + dob[0:4]
        year = dob[0:4]
        
        # Base words to check: Name and all related words in capitalized form
        manual_bases = {name.capitalize(), nickname.capitalize()} | {r.capitalize() for r in related_names if r}

        for base_word in manual_bases:
            # General Pattern: Base@YYYY# 
            strong_pw.insert(0, f"{base_word}@{year}#")
            
            # General Pattern: Base@DDMMYYYY#
            strong_pw.insert(0, f"{base_word}@{revdate}#")
        
    # The rest of the strong_pw list (from the function) is appended after the guaranteed patterns
    all_pw_final.extend(strong_pw) 
    
    # 3. Tier 2: Auxiliary combinations
    all_pw_final.extend(normal_pw)
    
    # 4. Remove Duplicates while maintaining the high-priority order
    seen = set()
    result = []
    # Iterate in reverse to ensure the first seen item (highest priority) is kept.
    for item in reversed(all_pw_final):
        if item not in seen:
            seen.add(item)
            result.append(item)
    all_pw = list(reversed(result)) # Final list, prioritized by Tiers 0, 1, then 2.

    # Final cleanup to ensure no non-ascii characters remain
    all_pw = [p for p in all_pw if all(ord(c) < 128 for c in p)]
    
    
    # Apply Max Limit logic: Trim from the end to preserve Tiers 0 and 1.
    if max_limit > 0 and len(all_pw) > max_limit:
        animate(f"[{YELLOW}TRIM{RESET}] Total combinations ({len(all_pw)}) exceed limit ({max_limit}). Trimming list to preserve top priority tiers.\n", 0.02)
        all_pw = all_pw[:max_limit] 
        
    

    # Save to file, using the derived filename
    if args.output in ("txt", "all"):
        save_txt(all_pw, filename_base)
    if args.output in ("csv", "all"):
        save_csv(all_pw, filename_base)
    if args.output in ("json", "all"):
        save_json(all_pw, filename_base)

    print(f"\n[{GREEN}✓{RESET}] Total Unique High-Prediction Passwords Generated: {BLUE}{len(all_pw)}{RESET}")
    print("Assessment wordlist generation complete.")


if __name__ == "__main__":
    main()
