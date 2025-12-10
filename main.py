import argparse
from wordlist_loader import WordlistLoader
from diceware_generator import DicewareGenerator
from username_generator import UsernameGenerator

def main():
    parser = argparse.ArgumentParser(description="DiceWare Entropy Generator")
    parser.add_argument("--list", type=str, required=True,
                        help="Path to wordlist file (EFF format, EX.: 12345 apple)")
    parser.add_argument("--words", type=int, default=4,
                        help="Number of words in the password.")
    parser.add_argument("--username", action="store_true",
                        help="Generates a random username using the wordlist provided")
    parser.add_argument("--full", action="store_true",
                        help="Generates a full set of password and username")
    args = parser.parse_args()

    # Loads wordlist
    loader = WordlistLoader(args.list)
    lookup = loader.load()
    
    # Generators
    password_gen = DicewareGenerator(lookup)
    username_gen = UsernameGenerator(lookup)

    # Full set of credentials
    if args.full:
        password, entropy = password_gen.generate_password(args.words)
        username = username_gen.generate()

        print("Username: ", username)
        print("Password: ", password)
        print(f"Entropy: {entropy:.2f} bits\n")
        return

    if args.username:
        print("Generated Username: ", username_gen.generate())
        return

    password, entropy = password_gen.generate_password(args.words)

    print("Generated Password: ", password)
    print(f"Entropy: {entropy:.2f} bits\n")

if __name__ == "__main__":
    main()