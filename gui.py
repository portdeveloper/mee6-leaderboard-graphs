from ServerInfo import ServerInfo
import matplotlib.pyplot as plt
import tkinter as tk

# Assuming these variables for demonstration purposes (you may want to fetch them differently)
statuslevels = [10, 20, 30]
statusnames = ["Bronze", "Silver", "Gold"]
yvar = "xp"  # Example variable, replace with actual value
csv = False  # Example variable, replace with actual value

# Function to handle the Start button click
def on_start():
    guild_id = guild_id_entry.get()
    top = int(top_entry.get() or "100")

    url = f'https://mee6.xyz/api/plugins/levels/leaderboard/{guild_id}?limit=999&page=0'
    server = ServerInfo(url, top)

    if csv:
        server.csv()
    plt.figure()
    plt.suptitle(server.servername)
    plt.subplot(221)
    server.statuspie(statuslevels, statusnames)
    plt.subplot(222)
    server.rankbar(yvar)
    plt.subplot(223)
    server.lvldistribution()
    plt.subplot(224)
    server.randomstats()
    plt.subplots_adjust(hspace=0.3)
    plt.show()

    status_text.set("Processing complete!")

# Creating the main window
root = tk.Tk()
root.title("Mee6 Leaderboard Graphs")

# Adding Guild ID input
guild_id_label = tk.Label(root, text="Guild ID:")
guild_id_label.pack()
guild_id_entry = tk.Entry(root)
guild_id_entry.pack()

# Adding Top Members input
top_label = tk.Label(root, text="Top Members (default 100):")
top_label.pack()
top_entry = tk.Entry(root)
top_entry.pack()

# Adding Start button
start_button = tk.Button(root, text="Start", command=on_start)
start_button.pack()

# Adding Status/Result display
status_text = tk.StringVar()
status_label = tk.Label(root, textvariable=status_text)
status_label.pack()

# Running the GUI
root.mainloop()
