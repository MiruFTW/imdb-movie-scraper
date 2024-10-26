# imdb_gui.py
import tkinter as tk
from imdb_scraper import scrape_imdb  # Import the scraper function

# Function to display results in the GUI
def display_results():
    choice = selected_option.get()
    results = scrape_imdb(choice)
    blank = ""
    
    # Clear previous results
    results_display.delete(1.0, tk.END)

    results_display.insert(tk.END, f"Title{blank:45} | Rating\n")

    # Display each title and rating with aligned formatting
    for title, rating in results:
        results_display.insert(tk.END, f"{title:50} | {rating}\n")

# Initialize Tkinter window
root = tk.Tk()
root.title("IMDb Scraper")
root.geometry("640x480")

# Add title label
title_label = tk.Label(root, text="IMDb Movie Scraper", font=("Arial", 16))
title_label.pack(pady=10)

# Radio buttons for options
selected_option = tk.StringVar(value="Popular Movies")
box_office_button = tk.Radiobutton(root, text="Box Office Top 10", variable=selected_option, value="Box Office Top 10")
popular_movies_button = tk.Radiobutton(root, text="Popular Movies", variable=selected_option, value="Popular Movies")
box_office_button.pack(anchor="w", padx=20)
popular_movies_button.pack(anchor="w", padx=20)

# Button to run the scraper
scrape_button = tk.Button(root, text="Scrape IMDb", command=display_results)
scrape_button.pack(pady=10)

# Text widget to display results
results_display = tk.Text(root, wrap="word", height=50, width=100)
results_display.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()
