#!/usr/bin/python3
import pathlib
import tkinter as tk
import tkinter.font as tkFont
import pygubu
from all_parserui import All_ParserUI
import yaml


class All_Parser(All_ParserUI):
    def __init__(self, master=None):
        super().__init__(master)
        self.resultText.tag_configure("bold", font='黑体 12 bold')
        self.resultText.tag_configure("redFore", foreground='red',font='黑体 12 bold')
        self.resultText.tag_configure("greenFore", foreground='green',font='黑体 12 bold')

    def runButtonClicked(self):
        ''' 重写: 点击Run回调 '''
        self.resultText.delete('1.0',tk.END)
        idx = 0
        with open(self.dataEntry.get(),"rb") as f:
            hexstr = f.read().hex()
        with open(self.cfg_entry.get(),"r",encoding='utf-8') as f:
             fmt_cfgs = yaml.safe_load(f)
        for one_cfg in fmt_cfgs:
            self.resultText.insert(tk.END,one_cfg[0]+' : ')
            this_part_str = hexstr[idx:idx+2*one_cfg[1]]
            self.resultText.insert(tk.END,this_part_str+"   ",'greenFore')
#generate bin files
            with open(one_cfg[0]+".bin","wb") as f:
                f.write(bytes.fromhex(this_part_str))

            self.resultText.insert(tk.END,"\n                        ASCII: ")
            i = 0
            for i in range(0,2*one_cfg[1],2):
                asciiInt = eval('0x'+this_part_str[i]+this_part_str[i+1])
                if(32 <= asciiInt and asciiInt  <= 126):
                    self.resultText.insert(tk.END,chr(asciiInt))
                else:
                    print(asciiInt )
                    self.resultText.insert(tk.END,'.')
            idx += 2*one_cfg[1]
            self.resultText.insert(tk.END,"\n")


if __name__ == "__main__":
    app = All_Parser()
    app.run()

