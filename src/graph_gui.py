import Tkinter
import ttk
import tkFileDialog

class GraphGUI(Tkinter.Frame):
    def __init__(self, root, GraphLoader):
        Tkinter.Frame.__init__(self, root)

        self.root = root
        self.GraphLoader = GraphLoader

        self.set_gui_contents()

    def set_gui_contents(self):
        self.set_up_window()
        self.add_load_button()

    def set_up_window(self):
        self.root.title("Load Graph")
        self.pack(fill=Tkinter.BOTH, expand=1)

    def add_load_button(self):
        self.load_button = ttk.Button(
            self, text="Load", command=self.load_graph
            )
        self.load_button.place(x=5, y=5)

    def load_graph(self):
        self.open_file()
        graph = self.GraphLoader.graph_from_file(self.graph_file_path)

        # TODO add link to the next GUI.
        print('next GUI not implemented')

    def open_file(self):
        self.graph_file_path = tkFileDialog.askopenfilename(
            filetypes=[('All files', '*')]
            )
        if self.graph_file_path:
            print('file path')
            print(self.graph_file_path)
        else:
            print('no file path!!!')

def load_graph_gui(GraphLoader):
    root = Tkinter.Tk()
    gui = GraphGUI(root, GraphLoader)
    root.geometry("100x30")
    root.mainloop()
