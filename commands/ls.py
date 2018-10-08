import os
import datetime
from helpers import FileDetailsHelper


class ls():
    def __init__(self):
        self.show_hidden = False
        self.option_dictionary = self.get_option_dictionary()

    def __get_files_from_current_path(self):
        return FileDetailsHelper.get_files_from_path('.')
    
    def __get_files_from_path(self, path):
        return FileDetailsHelper.get_files_from_path(path)

    def get_files(self, *args):
        if args:
            return self.__get_files_from_path(*args)
        return self.__get_files_from_current_path()

    def get_option_dictionary(self):
        option_dictionary = {
            'basic': 'get_only_visible_files',
            '-r': 'get_files_in_revrese_order',
            '-la': 'get_complete_details',
            '-a': 'get_all_files',
            '-F': 'get_folders_with_backslash',
            '-l': 'get_complete_details_of_visible_files'
        }

        return option_dictionary

    def get_complete_details(self, show_hidden_files=True, *args):
        detailed_files = []
        files = self.get_files(args)
        if not show_hidden_files:
            files = FileDetailsHelper.filter_hidden_files(files)

        for filename in files:
            try:
                lstat_info = os.lstat(filename)
            except:
                print("No such file {}".format(filename))
                continue

            perms, color, link = FileDetailsHelper.get_mode_info(lstat_info.st_mode)
            nlink = "%4d" % FileDetailsHelper.get_number_of_hardlinks(lstat_info)
            name = FileDetailsHelper.get_owner_name(lstat_info)
            group = FileDetailsHelper.get_owner_group(lstat_info)
            size = "%8d" % lstat_info.st_size
            time_str = FileDetailsHelper.get_time_of_creation(lstat_info)

            info_tuple = (perms, nlink, name, group, size, time_str, filename)
            detailed_files.append(info_tuple)

        detailed_files = sorted(detailed_files, key=lambda x: datetime.datetime.strptime(x[5], '%b %d  %Y'))
        for info_tuple in reversed(detailed_files):
            for info in info_tuple:
                print(info)
            print()

    def get_only_visible_files(self, *args):
        files = self.get_files(*args)
        files = FileDetailsHelper.filter_hidden_files(files)
        self.print_to_screen(files)

    def get_files_in_revrese_order(self, *args):
        files = self.get_files(*args)
        files = FileDetailsHelper.reverse_file_ordering(files)
        self.print_to_screen(files)

    def print_to_screen(self, files):
        for filename in files:
            print(filename)

    def get_all_files(self, *args):
        files = self.get_files(*args)
        self.print_to_screen(files)

    def get_folders_with_backslash(self, *args):
        files = self.get_files(*args)
        files = FileDetailsHelper.filter_hidden_files(files)
        for i, filename in enumerate(files):

            if FileDetailsHelper.is_a_folder(os.lstat(filename).st_mode):
                filename = filename + '/'
                files[i] = filename

        self.print_to_screen(files)

    def get_complete_details_of_visible_files(self):
        self.get_complete_details(show_hidden_files=False)

    def execute(self, cls):
        try:
            option = cls.options[0]
        except IndexError:
            option = 'basic'

        methods = self.option_dictionary
        if option in methods.keys():
            method_to_execute = getattr(ls, methods[option])
            method_to_execute(self, *cls.data)
        else:
            print('Invalid option')
