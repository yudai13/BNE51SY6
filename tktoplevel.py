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
            tk.Button(text="",command=self.buttonClick,width=width).place(x=start_x, y=start_y+margin_y*i)
            tk.Button(text="",command=self.buttonClick,width=width).place(x=start_x+margin_x, y=start_y+margin_y*i)

    def buttonClick(self): #セレクトページを開くためのボタンをクリックしたときの動作
        select_page = SelectPage(tk.Toplevel())



#加工の種類が表示されるページ
class SelectPage(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.master = master
        self.pack()
        master.grab_set()
        master.geometry("500x500")
        self.create_widget(master)

    def create_widget(self,master):
        width = 20
        start_x = 50
        start_y = 50
        margin_y = 27
        process_list = ["外径(荒)","外径(仕上)","ストッパー","突っ切り","正面ドリル"]
        
        tk.Label(self.master,text="加工方法選択").place(x=start_x+30,y=start_y-margin_y)
        for i in range(len(process_list)):
            tk.Button(self.master,text=process_list[i],command=self.button_click,width=20).place(x=start_x,y=start_y+margin_y*i)

    def button_click(self):
        self.master.destroy()
        input_page = InputPage(tk.Toplevel())


class InputPage(tk.Frame):
  def __init__(self,master):
    super().__init__(master)
    self.master = master
    self.pack()
    self.master.geometry("500x800")
    self.master.grab_set()
    self.button = tk.Button(self.master,text="OK",command=self.buttonClick,width=10)
    self.button.place(x=70, y=500)
    self.button.config(fg="black", bg="pink")
    self.button = tk.Button(self.master,text="キャンセル",command=self.buttonClick,width=10)
    self.button.place(x=150, y=500)



  def buttonClick(self):
    self.master.destroy()
        
"""加工方法ページ選択肢"""
class GaikeiPage(tk.Frame):
  def __init__(self,master):
    super().__init__(master)
    self.pack()
    master.geometry("500x800")
    master.grab_set()
    self.button = tk.Button(master,text="外径",command=self.buttonClick,width=10)
    self.button.place(x=70, y=500)
    self.button.config(fg="black", bg="pink")
    self.button = tk.Button(master,text="キャンセル",command=self.buttonClick,width=10)
    self.button.place(x=150, y=500)


class DorillPage(tk.Frame):
  def __init__(self,master):
    super().__init__(master)
    self.pack()
    master.geometry("500x800")
    master.grab_set()
    self.button = tk.Button(master,text="Dorill",command=self.buttonClick,width=10)
    self.button.place(x=70, y=500)
    self.button.config(fg="black", bg="pink")
    self.button = tk.Button(master,text="キャンセル",command=self.buttonClick,width=10)
    self.button.place(x=150, y=500)

def main():
  win = tk.Tk()
  app = Application(win)
  app.mainloop()

if __name__ == '__main__':
  main()
