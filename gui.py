import customtkinter as ctk
from wordlist_loader import WordlistLoader
from diceware_generator import DicewareGenerator
from username_generator import UsernameGenerator

import pyperclip
import os


class PasswordGUI(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("PassGen - a credential generator")
        self.resizable(False, False)
        self.geometry("420x550")

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Placeholder until a file is chosen
        self.lookup = None
        self.wordlist_path = None

        """
            UI
        """

        self.label_title = ctk.CTkLabel(
            self, text="PassGen", font=("Segoe UI", 24)
        )
        self.label_title.pack(pady=10)

        # Wordlist picker
        self.btn_choose_list = ctk.CTkButton(
            self, text="Choose Wordlist", command=self.choose_wordlist
        )
        self.btn_choose_list.pack(pady=5)

        # Label that shows file chosen
        self.label_list_name = ctk.CTkLabel(self, text="No wordlist loaded")
        self.label_list_name.pack(pady=5)

        # Username frame
        self.frame_user = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_user.pack(pady=5)

        self.label_username = ctk.CTkLabel(self.frame_user, text="Username:")
        self.label_username.pack(anchor="w")

        self.entry_username = ctk.CTkEntry(self.frame_user, width=350, state="readonly")
        self.entry_username.pack()

        # Password frame
        self.frame_pass = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_pass.pack(pady=5)

        self.label_password = ctk.CTkLabel(self.frame_pass, text="Password:")
        self.label_password.pack(anchor="w")

        self.entry_password = ctk.CTkEntry(self.frame_pass, width=350, state="readonly")
        self.entry_password.pack()

        # Entropy frame
        self.frame_entropy = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_entropy.pack(pady=5)

        self.label_entropy = ctk.CTkLabel(self.frame_entropy, text="Entropy:")
        self.label_entropy.pack(anchor="w")

        self.entry_entropy = ctk.CTkEntry(self.frame_entropy, width=350, state="readonly")
        self.entry_entropy.pack()

        # Buttons
        self.btn_username = ctk.CTkButton(
            self, text="Generate Username", command=self.generate_username
        )
        self.btn_username.pack(pady=10)

        self.btn_password = ctk.CTkButton(
            self, text="Generate Password", command=self.generate_password
        )
        self.btn_password.pack(pady=10)

        self.btn_full = ctk.CTkButton(
            self,
            text="Generate Full set (user and password)",
            command=self.generate_full
        )
        self.btn_full.pack(pady=10)

        # Copy buttons
        self.btn_copy_user = ctk.CTkButton(
            self, text="Copy Username", width=200, command=self.copy_username
        )
        self.btn_copy_user.pack(pady=4)

        self.btn_copy_pass = ctk.CTkButton(
            self, text="Copy Password", width=200, command=self.copy_password
        )
        self.btn_copy_pass.pack(pady=4)

    """
        LOGIC
    """

    def ensure_loaded(self):
        if self.wordlist_path is None:
            self.label_list_name.configure(text="Load a wordlist first!")
            return False
        return True

    def choose_wordlist(self):
        """
            file picker dialog for the user to select a .txt wordlist.
        """
        from tkinter import filedialog

        default_folder = os.path.join(os.path.dirname(__file__), "wordlists")

        path = filedialog.askopenfilename(
            title="Select Wordlist",
            initialdir=default_folder,
            filetypes=[("Text Files", "*.txt")]
        )

        if not path:
            return

        self.wordlist_path = path
        self.label_list_name.configure(text=f"Loaded: {os.path.basename(path)}")

        # Actually load the lookup
        loader = WordlistLoader(path)
        lookup = loader.load()
        self.lookup = lookup

        # NOW we create the generators
        self.password_gen = DicewareGenerator(lookup)
        self.username_gen = UsernameGenerator(lookup)

    def generate_username(self):
        if not self.ensure_loaded():
            return

        username = self.username_gen.generate()
        self.entry_username.configure(state="normal")
        self.entry_username.delete(0, "end")
        self.entry_username.insert(0, username)
        self.entry_username.configure(state="readonly")

    def generate_password(self):
        if not self.ensure_loaded():
            return

        password, entropy = self.password_gen.generate_password(4)
        self.entry_password.configure(state="normal")
        self.entry_password.delete(0, "end")
        self.entry_password.insert(0, password)
        self.entry_password.configure(state="readonly")

        self.entry_entropy.configure(state="normal")
        self.entry_entropy.delete(0, "end")
        self.entry_entropy.insert(0, f"{entropy:.2f} bits")
        self.entry_entropy.configure(state="readonly")

    def generate_full(self):
        if not self.ensure_loaded():
            return

        username = self.username_gen.generate()
        password, entropy = self.password_gen.generate_password(4)

        self.entry_username.configure(state="normal")
        self.entry_username.delete(0, "end")
        self.entry_username.insert(0, username)
        self.entry_username.configure(state="readonly")

        self.entry_password.configure(state="normal")
        self.entry_password.delete(0, "end")
        self.entry_password.insert(0, password)
        self.entry_password.configure(state="readonly")

        self.entry_entropy.configure(state="normal")
        self.entry_entropy.delete(0, "end")
        self.entry_entropy.insert(0, f"{entropy:.2f} bits")
        self.entry_entropy.configure(state="readonly")

    def copy_username(self):
        pyperclip.copy(self.entry_username.get())

    def copy_password(self):
        pyperclip.copy(self.entry_password.get())


if __name__ == "__main__":
    app = PasswordGUI()
    app.mainloop()
