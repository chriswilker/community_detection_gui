import unittest
import community_detection_gui.src.path_helper as path_helper

import sys

class TestPathHelper(unittest.TestCase):
    def test_remove_extension(self):
        file_path_with_extension = 'folder/folder/file.txt'
        expected_result = 'folder/folder/file'
        
        helper = path_helper.PathHelper()
        
        file_path_without_extension = helper.file_path_without_extension(
                file_path_with_extension
                )

        self.assertEqual(file_path_without_extension, expected_result)

    def test_find_extension(self):
        file_path_with_extension = 'folder/folder/file.txt'
        expected_result = '.txt'
        
        helper = path_helper.PathHelper()
        
        file_extension = helper.file_extension(file_path_with_extension)

        self.assertEqual(file_extension, expected_result)


    def test_join_paths(self):
        helper = path_helper.PathHelper()

        if sys.platform.startswith('linux') or (sys.platform == 'darwin'):
            folder_path = 'folder/otherfolder'
            file_name = 'file.json'
            expected_result = 'folder/otherfolder/file.json'

            file_path = helper.join_paths(folder_path, file_name)
            self.assertEqual(expected_result, file_path)
        elif sys.platform.startswith('win'):
            folder_path = 'folder\\otherfolder'
            file_name = 'file.json'
            expected_result = 'folder\\otherfolder\\file.json'

            file_path = helper.join_paths(folder_path, file_name)
            self.assertEqual(expected_result, file_path)

if __name__ == '__main__':
    unittest.main()

