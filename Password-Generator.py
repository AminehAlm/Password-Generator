import random
import nltk
nltk.download('brown', quiet=True)
nltk.download('stopwords', quiet=True)
from nltk import FreqDist
from nltk.corpus import stopwords, brown
import string
import secrets
import math
import csv
import os
import sys


class PasswordGenerator:
    """
    A versatile password generator supporting three modes:
    1. Random Password (fully customizable)
    2. Memorable Password (based on English word corpus)
    3. PIN code (numeric only)
    """

    def __init__(self, char=""):
        print("Welcome to the Password Generator system!")
        self.length = 0
        self.char = char

    def Password_selector(self):
        """Main entry point that asks the user which type of password to generate."""
        while True:
            try:
                self.typeinput = int(input(
                    "Which type of password do you prefer to be generated?\n 1: RandomPassword\n 2: MemorablePassword\n 3: Pincode\n"))
                if self.typeinput in (1, 2, 3):
                    if self.typeinput == 1:
                        self.Randompassword()
                    elif self.typeinput == 2:
                        self.words_input()
                    elif self.typeinput == 3:
                        self.Pincode()
                    break
                else:
                    print('Wrong Value. Please just choose 1, 2, or 3')
            except ValueError:
                print('Invalid input. 1, 2 or 3 are the ONLY choices')

    def passwordlength(self, min_length=6):
        """Ask the user for password length with a minimum limit."""
        while True:
            try:
                length = int(input(
                    f"What is the length of your password? (Minimum is {min_length})"))
                if length >= min_length:
                    return length
                else:
                    print(f"Please enter a positive number greater than {min_length}")
            except ValueError:
                print(f"Invalid input. Please type a number greater than {min_length}")

    def Randompassword(self):
        """Generate a fully random password with digits, symbols, and/or letters."""
        self.length = self.passwordlength()
        number = self.yes_no_q("Do you want your password to be only numbers?\n 1: Yes\n 2: No\n")
        if number is True:
            self.char += string.digits
        elif number is False:
            self.char += string.digits
            symbol = self.yes_no_q("Do you want to add symbols to your password?\n 1: Yes\n 2: No\n")
            if symbol is True:
                self.char += string.punctuation
            letter = self.yes_no_q("Do you want to add letters to your password?\n 1: Yes\n 2: No\n")
            if letter is True:
                self.lettercases()
        self.pass_generation()

    def yes_no_q(self, message):
        """Reusable yes/no input function."""
        while True:
            try:
                answer = int(input(f"{message}"))
                if answer == 1:
                    return True
                elif answer == 2:
                    return False
                else:
                    print("Invalid number! Just choose 1 or 2")
            except ValueError:
                print("Invalid input! Just choose 1 or 2")

    def lettercases(self):
        """Ask user which letter case(s) should be used in the random password."""
        while True:
            try:
                case = int(input("Which letter case do you want?\n 1: Lowercase\n 2: Uppercase\n 3: Both\n"))
                if case == 1:
                    self.char += string.ascii_lowercase
                    return self.char
                elif case == 2:
                    self.char += string.ascii_uppercase
                    return self.char
                elif case == 3:
                    self.char += string.ascii_letters
                    return self.char
                else:
                    print("ONLY choose 1, 2 or 3!")
            except ValueError:
                print("Invalid input! Please choose 1, 2 or 3")

    def entropy(self):
        """Calculate entropy (bit strength) for random passwords."""
        self.entropy_value = self.length * math.log2(len(self.char))
        self.entropy_categories()

    def pass_generation(self):
        """Generate and display a random password."""
        elements = [secrets.choice(self.char) for _ in range(self.length)]
        self.password = ''.join(elements)
        print(f"This is your password: {self.password}")
        self.entropy()

    def entropy_categories(self):
        """Categorize and report password strength based on entropy value."""
        print("The strength of your password:")
        if self.entropy_value < 40:
            print("Weak Password!")
            pass2 = self.yes_no_q("Do you want to try again?\n"
                                    "[Tip: Increase your length or add more character types]\n 1: Yes\n 2: No\n")
            if pass2:
                if self.typeinput == 1:
                    self.Randompassword()
                elif self.typeinput == 2:
                    self.words_input()
                elif self.typeinput == 3:
                    self.Pincode()
        elif 40 <= self.entropy_value <= 50:
            print("Moderate Password")
        elif 50 <= self.entropy_value <= 60:
            print("Strong Password")
        else:
            print("Excellent! Very Strong Password")
        print("Goodbye!")
        sys.exit(0)

    def upload_file(self):
        """Allow user to upload a CSV file containing custom words for a memorable password."""
        file_path = input("Enter the full path of your CSV file: ").strip()
        if not os.path.exists(file_path):
            print("File not found. Please check the path and try again.")
            return
        try:
            with open(file_path, 'r', encoding='utf_8') as f:
                reader = csv.reader(f)
                words = []
                for row in reader:
                    words.extend(row)
            self.words_list = [w.strip() for w in words if w.strip() != ""]
            print(f"{len(self.words_list)} words successfully loaded from your file.")
            self.Memorablepassword()
        except Exception as e:
            print(f"Error reading your file: {e}")

    def words_input(self):
        """Ask user whether to use a custom word list or the NLTK Brown corpus."""
        print('NOTICE: You can upload your words in CSV format, or use the default dictionary.')
        while True:
            try:
                wordsinput = int(input("Do you want to upload your words or use the default dictionary?\n 1: Upload file\n 2: Dictionary\n"))
                if wordsinput == 1:
                    self.upload_file()
                elif wordsinput == 2:
                    self.Memorablepassword()
                else:
                    print("Invalid number. Please ONLY select 1 or 2")
            except ValueError:
                print("Invalid Input. Please ONLY select 1 or 2")

    def Memorablepassword(self):
        """Generate a memorable password using NLTK’s Brown corpus and remove stopwords."""
        self.length = self.passwordlength()
        dict = {'i': '!', 'o': '0', 'l': '|', 'a': '@'}
        self.dict_table = str.maketrans(dict)

        # Prepare corpus and filter stopwords
        words = brown.words()
        frequency = FreqDist(words)
        self.exclude_words = stopwords.words('english')
        self.words_list = [word for word in words if word.lower() not in self.exclude_words]

        # Adjust if requested length > available words
        if self.length > len(self.words_list):
            print("Your password length is greater than available words. Adjusted automatically.")
            self.length = len(self.words_list)

        # Randomly select words with sufficient frequency
        chosen_words = secrets.SystemRandom().sample(self.words_list, self.length)
        self.separator = input("Choose a separator symbol between your words: ")
        for i, word in enumerate(chosen_words):
            while word not in frequency or frequency[word] < 30:
                chosen_words[i] = secrets.choice(self.words_list)
                word = chosen_words[i]

        # Capitalize the second word to add variety
        if len(chosen_words) > 1:
            chosen_words[1] = chosen_words[1].capitalize()

        self.chosen_words = chosen_words
        self.pass_generation_memorable()

    def pass_generation_memorable(self):
        """Build the final memorable password using selected words and transformations."""
        self.password = self.separator.join(self.chosen_words)
        self.password = self.password.translate(self.dict_table)
        print(f"This is your password: {self.password}")
        self.entropy_memorable()

    def entropy_memorable(self):
        """Estimate entropy for memorable passwords."""
        self.entropy_value = self.length * math.log2(len(self.words_list))
        self.entropy_categories()

    def Pincode(self):
        """Generate a simple numeric PIN code."""
        self.length = self.passwordlength()
        char = string.digits
        self.passchar = [secrets.choice(char) for _ in range(self.length)]
        self.password = ''.join(self.passchar)
        print(f"Your pincode is: {self.password}")
        self.char = char
        self.entropy()


if __name__ == "__main__":
    generator = PasswordGenerator()
    generator.Password_selector()