import Tkinter
import ttk
import tkFileDialog

class GraphGUILoader(Tkinter.Frame):
    def __init__(self, root, graph_loader):
        Tkinter.Frame.__init__(self, root)

        self.root = root
        self.graph_loader = graph_loader

        self.set_gui_contents()

    def set_gui_contents(self):
        self.set_up_window()
        self.add_drop_down_list_label()
        self.add_drop_down_list()
        self.add_load_button()

    def set_up_window(self):
        self.root.title("Load Graph")
        self.pack(fill=Tkinter.BOTH, expand=1)

    def add_drop_down_list_label(self):
        self.drop_down_list_label = Tkinter.Label(self.root, text='File Type')
        self.drop_down_list_label.place(x=10, y=10)

    def add_drop_down_list(self):
        self.available_file_types = ['pickle']
        self.chosen_file_type = Tkinter.StringVar()
        self.chosen_file_type.set(self.available_file_types[0])
        self.drop_down_list = Tkinter.OptionMenu(
            self.root, self.chosen_file_type, *self.available_file_types
            )
        self.drop_down_list.place(x=70, y=5)

    def add_load_button(self):
        self.load_button = ttk.Button(
            self, text="Load", command=self.load_graph
            )
        self.load_button.place(x=10, y=40)

    def load_graph(self):
        self.choose_file()
        graph = self.graph_loader.load_graph_from_file(
            self.graph_file_path, self.chosen_file_type.get()
            )
        # TODO add link to the next GUI.
        print('next GUI not implemented')

    def choose_file(self):
        self.setup_file_type_options()
        self.open_file()

    def setup_file_type_options(self):
        self.file_type_options = []
        if self.chosen_file_type.get() == 'pickle':
            self.file_type_options = [('Pickle files', '*.pickle')]
        self.file_type_options.append(('All files', '*'))

    def open_file(self):
        self.graph_file_path = tkFileDialog.askopenfilename(
            filetypes=self.file_type_options
            )

def load_graph_gui(graph_loader):
    root = Tkinter.Tk()
    gui = LoadGraphGUI(root, graph_loader)
    root.geometry("160x80")
    root.mainloop()
