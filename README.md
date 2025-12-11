# 🔒 PassGen CLI

PassGen is a simple, secure, command-line tool for generating randomized credentials

GUI version: [<https://github.com/gabriel-marrone/PassGen/tree/gui>](<https://github.com/gabriel-marrone/PassGen/tree/gui>)

## ✨ Features

* **Diceware Passphrases:** Generates passphrases using a provided wordlist (like the EFF large wordlist).
* **Entropy Calculation:** Calculates and reports the entropy (in bits) for the generated password.
* **Username Generator:** Creates unique, stylized usernames.
* **Cross-Platform CLI:** Works identically on Windows, Linux, and macOS.

## 📥 Installation

Because PassGen is a Python CLI application, the installation is done via `pip`. This method creates a single `passgen` command that works in your terminal.

### Prerequisites

You must have **Python 3.8 or higher** installed on your system.

### Steps (Windows, Linux, and macOS)

1.  **Clone the Repository:**
    Since the tool relies on the wordlist files being present in the repository, you must download the project files first.
    ```bash
    git clone https://github.com/gabriel-marrone/PassGen.git
    cd PassGen
    ```

2.  **Install the Tool:**
    Use `pip` to install the package from the current directory (`.`). This automatically creates the `passgen` executable on your system path.
    ```bash
    pip install .
    ```
    *(If you use virtual environments, make sure it's activated first: `source venv/bin/activate`)*

---

## 💻 Usage

Once installed, you can run the tool using the `passgen` command from within the project's root directory.

The `--list`, `-l`, `-L`  argument requires a path to the custom wordlist file (`--list path/to/custom/file/custom_file.txt`), default uses the eff_long_wordlist.txt file located in /src/passgen/wordlists, therefore it only needs to be used if you have your own wordlist.

### 1. Generate a Password

| Command | Description |
| :--- | :--- |
| `passgen -p` | Generates a 4-word passphrase (default). |
| `passgen -p -w X` | Generates a passphrase with X numbers of words. |

**Example Output:**

Generated Password: SappyWakeRefineryVoucher
Entropy: 51.70 bits


### 2. Generate a Username Only

Use the `--username`, `-u`, `-U` flag.

| Command | Description |
| :--- | :--- |
| `passgen -u` | Generates a random username. |

**Example Output:**

Username: OYSTER_BARLEY55

### 3. Generate a Full Credential Set

Use the `--full`, `-f`, `-F` flag to generate both a password and a username.

| Command | Description |
| :--- | :--- |
| `passgen -f` | Generates a 4-word password and a username. |

**Example Output:**

Username: confirmenactment317<br>Password: BlipWannabeAgnosticMatching<br>Entropy: 51.70 bits<br>

The full command can be combined even further with other arguments such as:

| Command | Description |
| :--- | :--- |
| `passgen -f -w 5 -u kebab` | Generates a 5-word password and a username stylized with kebab-case. |

**Example Output:**

Username: natural-shifting309<br>Password: AttemptSpriteRevolvingStarboardSwell<br>Entropy: 64.62 bits<br>

---

## 📄 Licensing

This project is licensed under the [MIT License](LICENSE). The included `eff_large_wordlist.txt` is provided by the Electronic Frontier Foundation (EFF) and is in the public domain.

## 🌳 Development

This repository contains the **Command-Line Interface (CLI)** version. Development for a separate Graphical User Interface (GUI) version is taking place on the **`gui`** branch.

---
