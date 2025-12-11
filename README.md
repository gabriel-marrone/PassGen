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

### 1. Generate a Password

The `--list`, `-l`, `-L`  argument requires a path to the custom wordlist file (`--list path/to/custom/file/custom_file.txt`), default uses the eff_long_wordlist.txt file located in /src/passgen/wordlists.

| Command | Description |
| :--- | :--- |
| `passgen -p` | Generates a 4-word passphrase (default). |
| `passgen -p -w 6` | Generates a 6-word passphrase. |

**Example Output:**

Generated Password: JacketGossipCarrotBreathe 
Entropy: 51.58 bits


### 2. Generate a Username Only

Use the `--username`, `-u`, `-U` flag.

| Command | Description |
| :--- | :--- |
| `passgen --username` | Generates a random username. |

**Example Output:**

Username: FastCamel 

### 3. Generate a Full Credential Set

Use the `--full`, `-f`, `-F` flag to generate both a password and a username.

| Command | Description |
| :--- | :--- |
| `passgen --words 5 --full` | Generates a 5-word password and a username. |

**Example Output:**

Username: FastCamel 
Password: JacketGossipCarrotBreatheTree
Entropy: 64.47 bits


---

## 📄 Licensing

This project is licensed under the [MIT License](LICENSE). The included `eff_large_wordlist.txt` is provided by the Electronic Frontier Foundation (EFF) and is in the public domain.

## 🌳 Development

This repository contains the **Command-Line Interface (CLI)** version. Development for a separate Graphical User Interface (GUI) version is taking place on the **`gui`** branch.

---
