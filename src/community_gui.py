import Tkinter
import ttk
import tkFileDialog

class CommunityGUI():
    def __init__(self, CommunityFinder, PlotGUI):
        self.CommunityFinder = CommunityFinder
        self.PlotGUI = PlotGUI

    def set_graph(self, graph):
        self.graph = graph

    def load_gui(self):
        root = Tkinter.Tk()
        frame = CommunityGUI.CommunityFrame(root, self.CommunityFinder, self.PlotGUI, self.graph)
        root.geometry("260x130")
        root.mainloop()

    class CommunityFrame(Tkinter.Frame):
        def __init__(self, root, CommunityFinder, PlotGUI, graph):
            Tkinter.Frame.__init__(self, root)

            self.root = root
            self.CommunityFinder = CommunityFinder
            self.PlotGUI = PlotGUI
            self.graph = graph

            self.set_gui_contents()

        def set_gui_contents(self):
            self.set_up_window()
            self.add_consider_sign_checkbutton()
            self.add_detection_method()
            self.add_resolution_parameter()
            self.add_apply_button()
            self.root.bind('<Return>', self.apply_settings)

        def set_up_window(self):
            self.root.title("Community Detection")
            self.pack(fill=Tkinter.BOTH, expand=1)

        def add_consider_sign_checkbutton(self):
            self.consider_sign = Tkinter.IntVar(self.root)
            self.consider_sign.set(1)
            self.consider_sign_checkbutton = ttk.Checkbutton(
                self, text = "consider edge sign", 
                variable = self.consider_sign, onvalue = 1, offvalue = 0,
                )
            self.consider_sign_checkbutton.place(x=5, y=5)

        def add_detection_method(self):
            self.add_detection_method_label()
            self.add_detection_method_optionmenu()

        def add_detection_method_label(self):
            self.detection_method_label = ttk.Label(
                self, text='detection method'
                )
            self.detection_method_label_x = 5
            self.detection_method_label_y = 35
            self.detection_method_label.place(
                    x = self.detection_method_label_x, 
                    y = self.detection_method_label_y
                    )

        def add_detection_method_optionmenu(self):
            self.detection_method = Tkinter.StringVar(self.root)
            available_detection_methods = [
                    'Modularity', 'RBConfiguration', 'RBER', 'CPM', 
                    'Significance', 'Surprise'
                    ]
            self.detection_method_optionmenu = ttk.OptionMenu(
                self, self.detection_method, available_detection_methods[0],
                *available_detection_methods
                )
            self.detection_method_optionmenu.place(
                x = self.detection_method_label_x + 115, 
                y = self.detection_method_label_y
                )

        def add_resolution_parameter(self):
            self.add_resolution_parameter_label()
            self.add_resolution_parameter_entry()

        def add_resolution_parameter_label(self):
            self.resolution_parameter_label = ttk.Label(
                self, text='resolution parameter'
                )
            self.resolution_parameter_label_x = 5
            self.resolution_parameter_label_y = 65
            self.resolution_parameter_label.place(
                    x = self.resolution_parameter_label_x, 
                    y = self.resolution_parameter_label_y
                    )

        def add_resolution_parameter_entry(self):
            self.resolution_parameter = Tkinter.StringVar(self.root)
            self.resolution_parameter.set('1.0')
            self.resolution_parameter_entry = ttk.Entry(
                self, textvariable = self.resolution_parameter, width = 10
                )
            self.resolution_parameter_entry.place(
                    x = self.resolution_parameter_label_x + 130, 
                    y = self.resolution_parameter_label_y
                    )

        def add_apply_button(self):
            self.load_button = ttk.Button(
                self, text="Apply", command=self.apply_settings
                )
            self.load_button.place(x = 5, y = 95)

        def apply_settings(self, event=None):
            self.PlotGUI.set_graph(self.graph)
            self.PlotGUI.set_consider_sign(self.consider_sign.get())
            self.PlotGUI.set_membership(self.membership())
            self.PlotGUI.load_gui()

        def membership(self):
            return self.CommunityFinder.membership_list(
                self.graph, consider_sign = self.consider_sign.get(),
                detection_method = self.detection_method.get(),
                resolution_parameter = float(self.resolution_parameter.get())
                )
