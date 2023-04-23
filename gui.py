import tkinter as tk


class Gui:
    # create the main window
    # create a function to handle the search button click
    def handle_search(self, query):
        print("your", query)
        return

    # create the search button
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Search Box GUI")
        self.frame1 = tk.Frame(self.root, highlightbackground="blue", highlightthickness=2)
        self.frame2 = tk.Frame(self.root, highlightbackground="red", highlightthickness=2)
        # create the search box and label
        self.search_label = tk.Label(self.frame1, text="Search:")
        self.search_label.pack(side=tk.LEFT)
        self.search_entry = tk.Entry(self.frame1, width=50)
        self.search_entry.pack(side=tk.LEFT)
        self.result_text = tk.Text(self.frame2)
        self.result_text.pack(fill='x', expand=True)
        self.result_text.config(state=tk.DISABLED)  # disable editing
        self.search_button = tk.Button(self.frame1, text="Search",
                                       command=lambda: self.handle_search(self.search_entry.get()))
        self.search_button.pack(side=tk.LEFT)
        # create a text box for displaying search results

        # bind the <Return> event to the search box
        self.frame1.pack(padx=1, pady=1)
        self.frame2.pack(padx=1, pady=1, fill='x', expand=True)
        self.search_entry.bind("<Return>", lambda event: self.handle_search(self.search_entry.get() ))

    # run the main event loop
    def run(self):
        self.root.mainloop()
