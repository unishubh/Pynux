import os
import datetime
from helpers import FileDetailsHelper


class ls():
    def __init__(self):
        self.files = []
        self.show_hidden = False
        self.option_dictionary = self.get_option_dictionary()
        # print "in self"

    def get_files_from_current_path(self):
        self.files = FileDetailsHelper.get_files_from_path('.')

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

    def get_complete_details(self, show_hidden_files=True):
        detailed_files = []
        self.get_files_from_current_path()
        files = self.files
        if not show_hidden_files:
            files = FileDetailsHelper.filter_hidden_files(files)

        for filename in files:
            try:
                lstat_info = os.lstat(filename)
            except:
                print "No such file " + filename
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
                print info,
            print

    def get_only_visible_files(self):
        self.get_files_from_current_path()
        files = FileDetailsHelper.filter_hidden_files(self.files)
        self.print_to_screen(files)

    def get_files_in_revrese_order(self):
        self.get_files_from_current_path()
        files = FileDetailsHelper.reverse_file_ordering(self.files)
        self.print_to_screen(files)

    def print_to_screen(self, files):
        for filename in files:
            print filename,
        print

    def get_all_files(self):
        self.get_files_from_current_path()
        self.print_to_screen(self.files)

    def get_folders_with_backslash(self):
        self.get_files_from_current_path()
        files = FileDetailsHelper.filter_hidden_files(self.files)
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
        method_to_execute = getattr(ls, methods[option])
        method_to_execute(self)
