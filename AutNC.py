try:
    import Tkinter as tk
except:
    import tkinter as tk
    
class Application(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.pack()

        master.geometry("400x800")
        master.title("自動NC")

        self.create_button()

    def create_button(self): #ボタンの配置
        width = 20
        start_x = 50
        start_y = 80
        margin_x = 150
        margin_y = 27
        column = 20

        tk.Label(text="HEAD1",width=width).place(x=start_x,y=start_y-20)
        tk.Label(text="HEAD2",width=width).place(x=start_x+margin_x,y=start_y-20)
        for i in range(column):
            tk.Label(text=i+1,width=5).place(x=start_x-40,y=start_y+margin_y*i)
            tk.Button(text="",command=self.select_process,width=width).place(x=start_x, y=start_y+margin_y*i)
            tk.Button(text="",command=self.select_process,width=width).place(x=start_x+margin_x, y=start_y+margin_y*i)

    def select_process(self):
        select_process_win = tk.Toplevel(self)
        select_process_win.geometry("270x300")

        width = 20
        start_x = 50
        start_y = 50
        margin_y = 27
        process_list = ["外径(荒)","外径(仕上)","ストッパー","突っ切り","正面ドリル"]
        
        tk.Label(select_process_win,text="加工方法選択").place(x=start_x+30,y=start_y-margin_y)
        for i in range(len(process_list)):
            tk.Button(select_process_win,text=process_list[i],command=self.input_parameter,width=20).place(x=start_x,y=start_y+margin_y*i)

    def input_parameter(self):
        pass










def main():
    win = tk.Tk()
    win.resizable(width=False, height=False)
    app = Application(master=win)
    app.mainloop()


if __name__ == "__main__":
    main()
