from ServerInfo import ServerInfo
import matplotlib.pyplot as plt
import tkinter as tk

# Function to handle the Start button click
def on_start():
    guild_id = guild_id_entry.get()
    top = int(top_entry.get() or "100")
    statuslevels = [int(x) for x in statuslevels_entry.get().split(",")] if statuslevels_entry.get() else [10, 20, 30, 40, 50]
    statusnames = statusnames_entry.get().split(",") if statusnames_entry.get() != "na" else ["Bronze", "Silver", "Gold"]
    yvar = yvar_entry.get() if yvar_entry.get() else "lvl"

    url = f'https://mee6.xyz/api/plugins/levels/leaderboard/{guild_id}?limit=999&page=0'
    server = ServerInfo(url, top)

    # Output CSV is always true
    server.csv()

    plt.figure(figsize=(10, 8))
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
root.geometry("500x300")

# Adding Guild ID input
guild_id_label = tk.Label(root, text="Mee6 Server ID (REQUIRED):")
guild_id_label.pack()
guild_id_entry = tk.Entry(root)
guild_id_entry.pack()

# Adding Top Members input
top_label = tk.Label(root, text="Number of members (3 - 1000, default 100):")
top_label.pack()
top_entry = tk.Entry(root)
top_entry.pack()

# Adding Status Levels input
statuslevels_label = tk.Label(root, text="Level cutoffs for pie chart (default 10,20,30,40,50):")
statuslevels_label.pack()
statuslevels_entry = tk.Entry(root)
statuslevels_entry.pack()

# Adding Status Names input
statusnames_label = tk.Label(root, text='Names for each level range (default "Bronze, Silver, Gold"):')
statusnames_label.pack()
statusnames_entry = tk.Entry(root)
statusnames_entry.pack()

# Adding Y Variable input
yvar_label = tk.Label(root, text="Dependent var for leaderboard (lvl or exp, default lvl):")
yvar_label.pack()
yvar_entry = tk.Entry(root)
yvar_entry.pack()

# Adding Start button
start_button = tk.Button(root, text="Start", command=on_start)
start_button.pack()

# Adding Status/Result display
status_text = tk.StringVar()
status_label = tk.Label(root, textvariable=status_text)
status_label.pack()

# Running the GUI
root.mainloop()
