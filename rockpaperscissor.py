import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Import Pillow for handling .webp images

class RockPaperScissorsGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Rock Paper Scissors Game")
        self.attributes('-fullscreen', True)  # Set full screen
        self.configure(bg="#D2B48C")  # Main background color (Tan)
        self.resizable(False, False)

        # Load the background image (.webp file) using Pillow
        self.bg_image = self.load_image(r"C:\\Python312\\back4.jpg")  # Adjust the path as necessary

        if not self.bg_image:
            messagebox.showerror("Image Error", "Background image file is missing.")
            self.quit()

        # Set the background image using a Label
        self.bg_label = tk.Label(self, image=self.bg_image)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Load other images (rock, paper, scissors)
        self.rock_image = self.load_image(r"C:\\Python312\\images.png")  # Adjust the path as necessary
        self.paper_image = self.load_image(r"C:\\Python312\\paper1.png")  # Adjust the path as necessary
        self.scissors_image = self.load_image(r"C:\\Python312\\scissor1.png")  # Adjust the path as necessary

        if not self.rock_image or not self.paper_image or not self.scissors_image:
            messagebox.showerror("Image Error", "One or more image files are missing.")
            self.quit()  # Exit the application if images are not loaded

        # Create the game widgets (buttons, labels, etc.)
        self.create_widgets()

        # Optional: Bind the Escape key to exit full-screen mode
        self.bind("<Escape>", self.toggle_fullscreen)

    def load_image(self, filename):
        """Load an image using Pillow and return a PhotoImage object."""
        try:
            img = Image.open(filename)
            return ImageTk.PhotoImage(img)
        except Exception as e:
            print(f"Error loading image {filename}: {e}")
            return None

    def create_widgets(self):
        
        # Frame for instructions
        instruction_frame = tk.Frame(self, bg="#8B4513", bd=5, relief="ridge")  # Brown color for the frame
        instruction_frame.pack(pady=10, padx=20)

        self.instruction_label = tk.Label(instruction_frame, text="Choose Rock, Paper, or Scissors:",
                                          font=("Verdana", 22, "bold"), bg="#8B4513", fg="#FFFFFF")  # White text
        self.instruction_label.pack(pady=10)

        # Frame for buttons
        button_frame = tk.Frame(self, bg="#D2B48C")  # No frame for buttons, background matches main
        button_frame.pack(pady=20)

        # Buttons for choices (rock, paper, scissors)
        self.rock_button = tk.Button(button_frame, text="Rock", command=lambda: self.play(1), width=15, height=2,
                                     font=("Verdana", 16, "bold"), bg='#A0522D', fg='white', activebackground='#CD853F',
                                     activeforeground='white', relief="raised", bd=5, cursor="hand2")
        self.rock_button.grid(row=0, column=0, padx=20)

        self.paper_button = tk.Button(button_frame, text="Paper", command=lambda: self.play(2), width=15, height=2,
                                      font=("Verdana", 16, "bold"), bg='#A0522D', fg='white', activebackground='#CD853F',
                                      activeforeground='white', relief="raised", bd=5, cursor="hand2")
        self.paper_button.grid(row=0, column=1, padx=20)

        self.scissors_button = tk.Button(button_frame, text="Scissors", command=lambda: self.play(3), width=15, height=2,
                                         font=("Verdana", 16, "bold"), bg='#A0522D', fg='white', activebackground='#CD853F',
                                         activeforeground='white', relief="raised", bd=5, cursor="hand2")
        self.scissors_button.grid(row=0, column=2, padx=20)

        # Frame for result and images
        result_frame = tk.Frame(self, bg="#8B4513", bd=5, relief="ridge")  # Brown color for the frame
        result_frame.pack(pady=20, padx=20)

        # Result label
        self.result_label = tk.Label(result_frame, text="", font=("Verdana", 20, "bold"), bg="#D2691E", fg="#FFFFFF",
                                     width=30, height=2, bd=5, relief="ridge")
        self.result_label.pack()

        # Frame for user and computer images
        image_frame = tk.Frame(self, bg="#D2B48C")  # No frame for images, background matches main
        image_frame.pack(pady=30)

        # User and computer image labels
        self.user_image_label = tk.Label(image_frame, bg="#D2B48C", borderwidth=2, relief="solid")
        self.user_image_label.pack(side=tk.LEFT, padx=(20, 10))

        self.comp_image_label = tk.Label(image_frame, bg="#D2B48C", borderwidth=2, relief="solid")
        self.comp_image_label.pack(side=tk.RIGHT, padx=(10, 20))

        # Exit Button
        self.exit_button = tk.Button(self, text="Exit", command=self.destroy, width=10, font=("Verdana", 16, "bold"),
                                     bg='#FF4500', fg='white', activebackground='#CD5C5C', activeforeground='white',
                                     relief="raised", bd=5, cursor="hand2")
        self.exit_button.pack(pady=20)

    def toggle_fullscreen(self, event=None):
        """Toggle between full screen and windowed mode."""
        current_state = self.attributes('-fullscreen')
        self.attributes('-fullscreen', not current_state)

    def play(self, user_choice):
        # Choices dictionary
        choices = {1: 'Rock', 2: 'Paper', 3: 'Scissors'}
        user_choice_name = choices[user_choice]

        # Display user choice image
        if user_choice == 1:
            self.user_image_label.config(image=self.rock_image)
        elif user_choice == 2:
            self.user_image_label.config(image=self.paper_image)
        else:
            self.user_image_label.config(image=self.scissors_image)

        # Computer's random choice
        comp_choice = random.randint(1, 3)
        comp_choice_name = choices[comp_choice]

        # Display computer choice image
        if comp_choice == 1:
            self.comp_image_label.config(image=self.rock_image)
        elif comp_choice == 2:
            self.comp_image_label.config(image=self.paper_image)
        else:
            self.comp_image_label.config(image=self.scissors_image)

        # Determine the winner
        if user_choice == comp_choice:
            result = "It's a tie!"
        elif (user_choice == 1 and comp_choice == 2) or (user_choice == 2 and comp_choice == 3) or (user_choice == 3 and comp_choice == 1):
            result = "Computer wins!"
        else:
            result = "User wins!"

        # Update the result label
        self.result_label.config(text=f"{user_choice_name} vs {comp_choice_name}\n{result}")

        # Debugging output
        print(f"User choice: {user_choice_name}, Computer choice: {comp_choice_name}")

if __name__ == "__main__":
    app = RockPaperScissorsGame()
    app.mainloop()
