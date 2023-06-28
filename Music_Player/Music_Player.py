import tkinter as tk
from tkinter import filedialog
import pygame

# Initialize pygame mixer
pygame.mixer.init()

# Function to play music
def play_music(file_path):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

# Function to stop music
def stop_music():
    pygame.mixer.music.stop()

# Function to pause music
def pause_music():
    pygame.mixer.music.pause()

# Function to unpause music
def unpause_music():
    pygame.mixer.music.unpause()

# Function to handle file selection
def select_files():
    file_paths = filedialog.askopenfilenames(filetypes=(("Audio Files", "*.mp3"), ("All Files", "*.*")))
    if file_paths:
        for file_path in file_paths:
            play_music(file_path)

# Create the main window
window = tk.Tk()
window.title("Music Player")
window.geometry("500x250")
window.configure(bg="#253646")

# Create button styles
button_style = {
    "font": ("Arial", 12),
    "width": 10,
    "bg": "#76b6fc",
    "fg": "white",
    "relief": "raised",
    "activebackground": "#997174",
    "activeforeground": "white"
}

# Create label styles
label_style = {
    "font": ("Arial", 14),
    "fg": "#ecd444",
    "bg": "#253646",
    "padx": 10,
    "pady": 10
}

# Create labels
title_label = tk.Label(window, text="Music Player", **label_style)
instruction_label = tk.Label(window, text="Select music files to play:", **label_style)
by_label = tk.Label(window, text="by @sarthakkulkarni__", **label_style)

# Create buttons
play_button = tk.Button(window, text="Play", command=select_files, **button_style)
stop_button = tk.Button(window, text="Stop", command=stop_music, **button_style)
pause_button = tk.Button(window, text="Pause", command=pause_music, **button_style)
unpause_button = tk.Button(window, text="Unpause", command=unpause_music, **button_style)
exit_button = tk.Button(window, text="Exit", command=window.quit, **button_style)

# Add labels and buttons to the window
title_label.pack()
instruction_label.pack()
by_label.pack()
play_button.pack(side=tk.LEFT, padx=10, pady=5)
stop_button.pack(side=tk.LEFT, padx=10, pady=5)
pause_button.pack(side=tk.LEFT, padx=10, pady=5)
unpause_button.pack(side=tk.LEFT, padx=10, pady=5)
exit_button.pack(side=tk.RIGHT, padx=10, pady=5)

# Run the Tkinter event loop
window.mainloop()

print("Thank you for using the Music Player!")
