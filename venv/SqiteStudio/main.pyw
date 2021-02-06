import tkinter
import  sqlite3
class MainWindow(tkinter.Tk):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.geometry("500x600")
        self.lblTitle = tkinter.Label(self,text="sqlite studio",relief="raised")
        self.lblTitle.grid(row=0,column=0)
        self.lbldbname = tkinter.Label(self,text="Name")
        self.lbldbname.grid(row=1,column=0)
        self.txtdbname = tkinter.Entry(self)
        self.txtdbname.grid(row=2,column=0)
        self.lblsql = tkinter.Label(self,text="query txt")
        self.lblsql.grid(row=4,column=0)
        self.txtsql = tkinter.Text(self)
        self.txtsql.grid(row=5,column=0)
        self.btnExecute = tkinter.Button(self,text="exequete",command=self.Execute)
        self.btnExecute.grid(row=6,column=0)
        self.status = tkinter.Text(self)
        self.status.grid(row=8,column=0)
    def Execute(self):

        self.queryname = sqlite3.connect(self.txtdbname.get())
        self.cmds = self.queryname.cursor()
        self.lines = self.txtsql.get('1.0')
        try:
            with open("query.sql", "w") as q:
                for self.line in self.lines:
                    q.write(self.line)
            with open("query.sql","r") as c:
                self.sqlines = c.readlines()
                for self.sqline in self.sqlines:
                    self.cmds.execute(self.sqline)

        except Exception as e:
            self.status.insert('1.0', e)












mainwindow = MainWindow()
mainwindow.mainloop()