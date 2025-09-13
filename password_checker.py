import re
import tkinter as tk
from tkinter import messagebox



def check_password_strength(password):
    strength = 0  # Score to calculate strength
    
    # Minimum length 8
    if len(password) >= 8:
        strength += 1
    
    # Uppercase check
    if re.search(r"[A-Z]", password):
        strength += 1
    
    # Lowercase check
    if re.search(r"[a-z]", password):
        strength += 1
    
    # Number check
    if re.search(r"[0-9]", password):
        strength += 1
    
    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    
    # Determine password strength
    if strength < 3:
        return "Weak"
    elif strength == 3 or strength == 4:
        return "Medium"
    elif strength == 5:
        return "Strong"
    

# Create main window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("500x300")          # Bigger window
root.resizable(False, False)
root.configure(bg="#f0f4f8")      # Light blue background





# Label
label = tk.Label(root, text="Enter Your Password", font=("Helvetica", 16, "bold"), bg="#f0f4f8", fg="#333333")
label.pack(pady=20)


# Entry (password input)
password_entry = tk.Entry(root, show="*", width=30)
password_entry.pack(pady=5)

# Function to run on button click
result_label = tk.Label(root, text="", font=("Helvetica", 14, "bold"), bg="#f0f4f8")
result_label.pack(pady=10)

def check():
    password = password_entry.get()
    if password == "":
        result_label.config(text="Please enter a password!", fg="red")
    else:
        result = check_password_strength(password)
        if result == "Weak":
            color = "red"
        elif result == "Medium":
            color = "orange"
        else:
            color = "green"
        result_label.config(text=f"Password Strength: {result}", fg=color)

# Button
check_button = tk.Button(root, text="Check Strength", command=check,
                         font=("Helvetica", 14, "bold"), bg="#4CAF50", fg="white", activebackground="#45a049",
                         padx=10, pady=5, bd=0, relief="raised")
check_button.pack(pady=20)




# Keep the window open
root.mainloop()




