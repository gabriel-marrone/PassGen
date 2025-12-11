import argparse
from passgen.wordlist_loader import WordlistLoader
from passgen.diceware_generator import DicewareGenerator
from passgen.username_generator import UsernameGenerator

def main():
    parser = argparse.ArgumentParser(
        description="PassGen - Credential Generator",
        formatter_class=lambda prog: argparse.ArgumentDefaultsHelpFormatter(
                prog, max_help_position=90, width=100
            )
        )

    parser.add_argument(
        "-l", "--list",
        metavar="PATH",
        required=False,
        help="Path to a Diceware-formatted wordlist (e.g., EFF large wordlist)"
    )

    parser.add_argument(
        "-w", "--words",
        metavar="N",
        type=int,
        default=4,
        help="Number of words to use when generating a password."
    )

    parser.add_argument(
        "-u", "--username",
        nargs="?",
        const="random",
        metavar="STYLE",
        choices=["random", "camel", "pascal", "lower", "kebab", "upper", "upper_plain", "leet"],
        default=None,
        help=(
            "Generate a username. Optionally choose a style:\n"
            "  random, camel, pascal, lower, kebab, upper, upper_plain, leet "
        )
    )

    parser.add_argument(
        "-p", "--password",
        action="store_true",
        help="Generate a password using the provided wordlist."
    )

    parser.add_argument(
        "-f", "--full",
        action="store_true",
        help="Generate a username + password pair.")

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

        style = args.username if args.username is not None else "random"

        username = username_gen.generate(style=style)

        print("Username: ", username)
        print("Password: ", password)
        print(f"Entropy: {entropy:.2f} bits\n")
        return

    # Username only
    if args.username:
        print("Generated Username: ", username_gen.generate(style=args.username))
        return

    # Password only
    if args.password:
        password, entropy = password_gen.generate_password(args.words)

        print("Generated Password: ", password)
        print(f"Entropy: {entropy:.2f} bits\n")

if __name__ == "__main__":
    main()