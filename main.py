from tfdf import Search
from gui import Gui
from parse import Parser
import tkinter as tk

class TfDfGui(Gui):
    def __init__(self):
        self.search = Search()
        self.parser = Parser()

        super().__init__()

    def handle_search(self, query):

        result = self.search.query_result(self.parser.extract_free_style(query))
        self.result_text.config(state=tk.NORMAL)  # enable editing
        self.result_text.delete(1.0, tk.END)  # clear the text box
        self.result_text.insert(tk.END, f"Search results for: {query}\n")  # add search query to text box

        for i in result:
            self.result_text.insert(tk.END, i[0] + ' with score:'+ str(i[1]) + '\n')
        self.result_text.config(state=tk.DISABLED)  # disable editing
        return




gui = TfDfGui()
gui.run()

