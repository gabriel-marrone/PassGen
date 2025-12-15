import customtkinter as ctk
from .wordlist_loader import WordlistLoader
from .diceware_generator import DicewareGenerator
from .username_generator import UsernameGenerator

import pyperclip
import os

DEFAULT_WORDLIST = os.path.join(os.path.dirname(__file__), "wordlists", "eff_large_wordlist.txt")

class PasswordGUI(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("PassGen - a credential generator")
        self.resizable(False, False)
        self.geometry("420x710")

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Hold the loaded lookup
        self.lookup = None
        self.wordlist_path = None

        """
            UI
        """

        self.label_title = ctk.CTkLabel(
            self, text="PassGen", font=("Segoa UI", 24)
        )
        self.label_title.pack(pady=10)

        # Wordlist picker button
        self.btn_choose_list = ctk.CTkButton(
            self, text="Choose Wordlist",
            command=self.choose_wordlist,
            state="disabled"
        )
        self.btn_choose_list.pack(pady=5)

        # Checkbox for custom wordlist
        self.checkbox_var = ctk.BooleanVar(value=False)

        self.checkbox_custom_list = ctk.CTkCheckBox(
            self,
            text="Enable custom wordlist",
            variable=self.checkbox_var,
            command=self.toggle_custom_wordlist
        )
        self.checkbox_custom_list.pack(pady=(0, 5))

        # Label that shows which wordlist is currently loaded
        self.label_list_name = ctk.CTkLabel(self, text="Loaded: default wordlist")
        self.label_list_name.pack(pady=5)

        # Loads default list on startup
        self.load_default_wordlist()

        # Username frame
        self.frame_user = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_user.pack(pady=5)

        self.label_username = ctk.CTkLabel(self.frame_user, text="Username:")
        self.label_username.pack(anchor="w")

        self.entry_username = ctk.CTkEntry(self.frame_user, width=350, state="readonly")
        self.entry_username.pack()

        self.username_style_var = ctk.StringVar(value="random")

        self.label_username_style = ctk.CTkLabel(
            self.frame_user,
            text="Username Style:"
        )
        self.label_username_style.pack(anchor="w", pady=(4, 0))

        self.combo_username_style = ctk.CTkComboBox(
            self.frame_user,
            variable=self.username_style_var,
            values=[
                "random",
                "camel",
                "pascal",
                "lower",
                "kebab",
                "plain",
                "upper",
                "upper_plain",
                "leet",
            ],
            state="readonly",
            width=350
        )
        self.combo_username_style.pack(pady=(0, 4))

        # Password frame
        self.frame_pass = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_pass.pack(pady=5)

        self.label_password = ctk.CTkLabel(self.frame_pass, text="Password:")
        self.label_password.pack(anchor="w")

        self.entry_password = ctk.CTkEntry(self.frame_pass, width=350, state="readonly")
        self.entry_password.pack()

        # Password length frame
        self.frame_length = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_length.pack(pady=5)

        self.label_length = ctk.CTkLabel(self.frame_length, text="Password Length:")
        self.label_length.pack(anchor="w")

        self.entry_length = ctk.CTkEntry(self.frame_length, width=350)
        self.entry_length.insert(0, "4")  # Default length
        self.entry_length.pack()

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

    def toggle_custom_wordlist(self):
        """ If checkbox is on -> enables wordlist button, If checkbox is off -> uses default wordlist """
        
        if self.checkbox_var.get():
            self.btn_choose_list.configure(state="normal")
        else:
            self.btn_choose_list.configure(state="disabled")
            self.load_default_wordlist()
    
    def load_default_wordlist(self):
        """ Loads the built-in EFF wordlist automatically """
        self.wordlist_path = DEFAULT_WORDLIST
        loader = WordlistLoader(DEFAULT_WORDLIST)
        self.lookup = loader.load()
        self.password_gen = DicewareGenerator(self.lookup)
        self.username_gen = UsernameGenerator(self.lookup)
        self.label_list_name.configure(text=f"Loaded: {os.path.basename(DEFAULT_WORDLIST)}")

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
        import platform

        if platform.system() == "Windows":
            default_folder = os.environ.get('USERPROFILE', 'C:\\')
        else:
            default_folder = os.path.expanduser("~")

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

        username = self.username_gen.generate(style=self.username_style_var.get())

        self.entry_username.configure(state="normal")
        self.entry_username.delete(0, "end")
        self.entry_username.insert(0, username)
        self.entry_username.configure(state="readonly")

    def generate_password(self):
        if not self.ensure_loaded():
            return

        # Custom length text box logic
        try:
            length = int(self.entry_length.get())
        except ValueError:
            self.entry_length.delete(0, "end")
            self.entry_length.insert(0, "4")
            length = 4 # Default if input is invalid

        password, entropy = self.password_gen.generate_password(length)
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

        username = self.username_gen.generate(style=self.username_style_var.get())

        # Custom length text box logic
        try:
            length = int(self.entry_length.get())
        except ValueError:
            self.entry_length.delete(0, "end")
            self.entry_length.insert(0, "4")
            length = 4 # Default if input is invalid

        password, entropy = self.password_gen.generate_password(length)

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