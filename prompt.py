import os
import tkinter as tk
from tkinter import ttk

class DynamicFormApp:
    def __init__(self, master, fields):
        self.master = master
        self.fields = fields
        self.entries = {}
        
        self.create_widgets()

    def create_widgets(self):
        # Iterate over the fields and create label-entry pairs
        for index, field in enumerate(self.fields):
            label_text = field.replace('_', ' ').capitalize()
            label = ttk.Label(self.master, text=f"{label_text}:")
            label.grid(row=index, column=0, padx=10, pady=5, sticky=tk.W)

            entry = ttk.Entry(self.master)
            entry.grid(row=index, column=1, padx=10, pady=5, sticky=(tk.W + tk.E))
            self.entries[field] = entry

        # Add a submit button at the end
        submit_button = ttk.Button(self.master, text="Submit", command=self.submit)
        submit_button.grid(row=len(self.fields), column=0, columnspan=2, pady=10)

    def submit(self):
        # Example action for the submit button
        for field, entry in self.entries.items():
            print(f"{field}: {entry.get()}")

        self.master.destroy()

def main():
    root = tk.Tk()
    root.title("Dynamic Form Example")

    # Fetch 'prompt_fields' environment variable, split by comma, and strip each field
    prompt_fields_env = os.getenv('prompt_fields', '')
    fields = [field.strip() for field in prompt_fields_env.split(',') if field.strip()]

    # Ensure there are fields to create form elements for
    if fields:
        app = DynamicFormApp(root, fields)
        # Configure the grid to resize with the window
        root.columnconfigure(1, weight=1)
        root.rowconfigure(len(fields), weight=1)
        root.mainloop()
    else:
        print("Error: No fields provided in 'prompt_fields' environment variable.")

if __name__ == "__main__":
    main()

