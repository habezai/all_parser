#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk


class All_ParserUI:
    def __init__(self, master=None):
        # build ui
        self.root = tk.Tk(master)
        self.root.title("All-Parser")
        self.cfg_button = ttk.Button(self.root, name="cfg_button")
        self.cfg_button.configure(text='Select YAML On Disk')
        self.cfg_button.grid(column=2, padx=5, pady=5, row=20, sticky="ew")
        self.cfg_lable = ttk.Label(self.root, name="cfg_lable")
        self.cfg_lable.configure(text='Format File')
        self.cfg_lable.grid(column=0, padx=5, pady=5, row=20, sticky="ew")
        self.cfg_entry = ttk.Entry(self.root, name="cfg_entry")
        self.cfg_entry.configure(width=30)
        _text_ = 'example.yaml'
        self.cfg_entry.delete("0", "end")
        self.cfg_entry.insert("0", _text_)
        self.cfg_entry.grid(column=1, padx=5, pady=5, row=20, sticky="ew")
        self.dataLabel = ttk.Label(self.root, name="datalabel")
        self.dataLabel.configure(text='Data File')
        self.dataLabel.grid(column=0, padx=5, pady=5, row=10, sticky="ew")
        self.dataEntry = ttk.Entry(self.root, name="dataentry")
        _text_ = 'example.bin'
        self.dataEntry.delete("0", "end")
        self.dataEntry.insert("0", _text_)
        self.dataEntry.grid(column=1, padx=5, pady=5, row=10, sticky="ew")
        self.dataButton = ttk.Button(self.root, name="databutton")
        self.dataButton.configure(text='Select bin On Disk')
        self.dataButton.grid(column=2, padx=5, pady=5, row=10, sticky="ew")
        self.resultText = tk.Text(self.root, name="resulttext")
        self.resultText.configure(height=20, width=70)
        self.resultText.grid(
            column=0,
            columnspan=5,
            padx=5,
            pady=5,
            row=40,
            sticky="ew")
        self.resultText.configure(yscrollcommand=self.scroll_bae)
        self.runButton = ttk.Button(self.root, name="runbutton")
        self.runButton.configure(text='Run')
        self.runButton.grid(column=1, row=30)
        self.runButton.configure(command=self.runButtonClicked)
        self.scroll_bar = ttk.Scrollbar(self.root, name="scroll_bar")
        self.scroll_bar.configure(orient="vertical")
        self.scroll_bar.grid(column=100, row=40, sticky="ns")
        self.scroll_bar.configure(command=self.result)

        # Main widget
        self.mainwindow = self.root

    def run(self):
        self.mainwindow.mainloop()

    def scroll_bae(self, first, last):
        pass

    def runButtonClicked(self):
        pass

    def result(self, mode=None, value=None, units=None):
        pass


if __name__ == "__main__":
    app = All_ParserUI()
    app.run()
