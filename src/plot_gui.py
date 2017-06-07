import Tkinter
import ttk
import tkFileDialog

class PlotGUI():
    def __init__(self, GraphPlotter):
        self.GraphPlotter = GraphPlotter

    def set_graph(self, graph):
        self.graph = graph

    def set_consider_sign(self, consider_sign):
        self.consider_sign = consider_sign

    def set_membership(self, membership):
        self.membership = membership

    def load_gui(self):
        root = Tkinter.Tk()
        frame = PlotGUI.PlotFrame(
            root, self.GraphPlotter, self.graph, self.consider_sign, 
            self.membership
            )
        root.geometry("300x515")
        root.mainloop()

    class PlotFrame(Tkinter.Frame):
        def __init__(
                self, root, GraphPlotter, graph, consider_sign, membership
                ):
            Tkinter.Frame.__init__(self, root)

            self.root = root
            self.GraphPlotter = GraphPlotter
            self.graph = graph

            self.keyword_arguments = {}
            self.keyword_arguments['consider_sign'] = consider_sign
            self.keyword_arguments['membership'] = membership

            self.set_gui_contents()

        def set_gui_contents(self):
            self.set_up_window()
            self.add_plot_argument_entries()
            self.add_plot_button()
            self.add_save_button()
            self.root.bind('<Return>', self.plot)

        def set_up_window(self):
            self.root.title("Plot Graph")
            self.pack(fill=Tkinter.BOTH, expand=1)

        def add_plot_argument_entries(self):
            self.vertex_label_size = Tkinter.StringVar(self.root)
            self.add_entry_with_label(
                'vertex label size', 5, 5, self.vertex_label_size, 180
                )

            self.vertex_shape = Tkinter.StringVar(self.root)
            vertex_shape_choices = [
                'circle', 'rectangle', 'hidden', 'triangle-up', 'triangle-down'
                ]
            self.add_optionmenu_with_label(
                'vertex shape', 5, 35, self.vertex_shape, vertex_shape_choices, 180
                )

            self.vertex_size = Tkinter.StringVar(self.root)
            self.add_entry_with_label(
                'vertex size', 5, 65, self.vertex_size, 180
                )

            self.vertex_label_angle = Tkinter.StringVar(self.root)
            self.add_entry_with_label(
                'vertex label angle (radians)', 5, 95, self.vertex_label_angle, 180
                )

            self.vertex_label_distance = Tkinter.StringVar(self.root)
            self.add_entry_with_label(
                'vertex label distance', 5, 125, self.vertex_label_distance, 180
                )

            self.edge_curvature = Tkinter.StringVar(self.root)
            self.add_entry_with_label(
                'edge curvature', 5, 155, self.edge_curvature, 180
                )
            
            self.edge_width = Tkinter.StringVar(self.root)
            self.add_entry_with_label(
                'edge width', 5, 185, self.edge_width, 180
                )

            self.arrow_size = Tkinter.StringVar(self.root)
            self.add_entry_with_label(
                'arrow size', 5, 215, self.arrow_size, 180
                )
            
            self.arrow_width = Tkinter.StringVar(self.root)
            self.add_entry_with_label(
                'arrow width', 5, 245, self.arrow_width, 180
                )

            self.layout = Tkinter.StringVar(self.root)
            layout_choices = [
                    'kk', 'circle', 'drl', 'fr', 'fr3d', 'grid_fr', 'kk3d', 
                    'large_graph', 'random', 'random_3d', 'rt', 'rt_circular', 
                    'sphere'
                    ]
            self.add_optionmenu_with_label(
                'plot layout', 5, 275, self.layout, layout_choices, 180
                )

            self.pixel_width = Tkinter.StringVar(self.root)
            self.add_entry_with_label(
                'plot width (pixels)', 5, 305, self.pixel_width, 180
                )

            self.pixel_height = Tkinter.StringVar(self.root)
            self.add_entry_with_label(
                'plot height (pixels)', 5, 335, self.pixel_height, 180
                )

            self.top_margin = Tkinter.StringVar(self.root)
            self.add_entry_with_label(
                'top margin (pixels)', 5, 365, self.top_margin, 180
                )

            self.bottom_margin = Tkinter.StringVar(self.root)
            self.add_entry_with_label(
                'bottom margin (pixels)', 5, 395, self.bottom_margin, 180
                )

            self.right_margin = Tkinter.StringVar(self.root)
            self.add_entry_with_label(
                'right margin (pixels)', 5, 425, self.right_margin, 180
                )

            self.left_margin = Tkinter.StringVar(self.root)
            self.add_entry_with_label(
                'left margin (pixels)', 5, 455, self.left_margin, 180
                )

        def add_entry_with_label(
                self, label_text, label_x, label_y, entry_variable, 
                horizontal_separation, default_entry_value = False
                ):
            self.label_text = label_text
            self.label_x = label_x
            self.label_y = label_y
            self.default_entry_value = default_entry_value
            self.horizontal_separation = horizontal_separation

            self.add_label()
            self.add_entry(entry_variable)

        def add_label(self):
            label = ttk.Label(self, text = self.label_text)

            label.place(
                x = self.label_x, y = self.label_y
                )

        def add_entry(self, entry_variable):
            if self.default_entry_value:
                entry_variable.set(default_entry_value)
            entry = ttk.Entry(
                self, textvariable = entry_variable, width = 10
                )
            entry.place(
                x = self.label_x + self.horizontal_separation, y = self.label_y
                )

        def add_optionmenu_with_label(
                self, label_text, label_x, label_y, optionmenu_variable,
                optionmenu_choices, horizontal_separation
                ):
            self.label_text = label_text
            self.label_x = label_x
            self.label_y = label_y
            self.optionmenu_choices = optionmenu_choices
            self.horizontal_separation = horizontal_separation

            self.add_label()
            self.add_optionmenu(optionmenu_variable) 

        def add_optionmenu(self, optionmenu_variable):
            optionmenu = ttk.OptionMenu(
                self, optionmenu_variable, self.optionmenu_choices[0], 
                *self.optionmenu_choices
                )
            optionmenu.place(
                x = self.label_x + self.horizontal_separation, y = self.label_y
                )

        def add_plot_button(self):
            plot_button = ttk.Button(
                self, text = "Show Plot", command = self.plot
                )
            plot_button.place(x = 5, y = 485)
            
        def plot(self, event=None):
            self.set_arguments()
            self.GraphPlotter.plot(*self.arguments, **self.keyword_arguments)

        def set_arguments(self):
            self.set_graph_and_save_file_path()
            self.set_keyword_arguments()

        def set_graph_and_save_file_path(self):
            self.arguments = []
            self.arguments.append(self.graph)
            if self.is_graph_saved:
                self.arguments.append(self.save_file_path())

        def save_file_path(self):
            save_file_path = tkFileDialog.asksaveasfilename(
                filetypes = [
                    ('PDF', '*.pdf'), ('PNG', '*.png'), ('SVG', '*.svg'), 
                    ('PS', '*.ps'), ('All files', '*')
                    ], 
                parent = self.root
                )
            return save_file_path

        def set_keyword_arguments(self):
            self.set_keyword_argument(
                'vertex_label_size', self.vertex_label_size.get(),
                isNumber = True
                )
            self.set_keyword_argument('vertex_shape', self.vertex_shape.get())
            self.set_keyword_argument(
                'vertex_size', self.vertex_size.get(), isNumber = True
                )
            self.set_keyword_argument(
                'vertex_label_angle', self.vertex_label_angle.get(), 
                isNumber = True
                )
            self.set_keyword_argument(
                'vertex_label_dist', self.vertex_label_distance.get(), 
                isNumber = True
                )
            self.set_keyword_argument(
                'edge_curved', self.edge_curvature.get(), isNumber = True
                )
            self.set_keyword_argument(
                'edge_width', self.edge_width.get(), isNumber = True
                )
            self.set_keyword_argument(
                'edge_arrow_size', self.arrow_size.get(), isNumber = True
                )
            self.set_keyword_argument(
                'edge_arrow_width', self.arrow_width.get(), isNumber = True
                )
            self.set_keyword_argument('layout', self.layout.get())
            self.set_width_and_height()
            self.set_margins()

        def set_keyword_argument(self, key_name, value, isNumber=False):
            if value:
                if isNumber:
                    value = float(value)
                self.keyword_arguments[key_name] = value

        def set_width_and_height(self):
            if self.pixel_width.get() and self.pixel_height.get():
                pixel_width = float(self.pixel_width.get())
                pixel_height = float(self.pixel_height.get())

                bbox = (pixel_width, pixel_height)
                self.keyword_arguments['bbox'] = bbox

        def set_margins(self):
            if (
                self.top_margin.get() and self.bottom_margin.get() 
                and self.right_margin.get() and self.left_margin.get()
                ):
                top_margin = float(self.top_margin.get())
                bottom_margin = float(self.bottom_margin.get())
                right_margin = float(self.right_margin.get())
                left_margin = float(self.left_margin.get())

                margin = [top_margin, right_margin, bottom_margin, left_margin]
                self.keyword_arguments['margin'] = margin

        def add_save_button(self):
            self.is_graph_saved = 0
            save_button = ttk.Button(
                self, text = 'Save Plot', command = self.save
                )
            save_button.place(x = 100, y = 485)

        def save(self):
            self.is_graph_saved = 1
            self.plot()
            self.is_graph_saved = 0
