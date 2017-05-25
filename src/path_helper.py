import inspect
import os

class PathHelper():
    def path_to_module_directory(self, module):
        init_path = inspect.getfile(module)
        directory_path = os.path.dirname(init_path)
        return directory_path

    def path_to_file_directory(self, file_path):
        directory_path = os.path.dirname(file_path)
        return directory_path

    def file_path_without_extension(self, file_path):
        no_extension_path = os.path.splitext(file_path)[0]
        return no_extension_path

    def file_extension(self, file_path):
        extension = os.path.splitext(file_path)[1]
        return extension

    def join_paths(self, first_path_component, *other_path_components):
        combined_path = os.path.join(first_path_component, *other_path_components)
        return combined_path
