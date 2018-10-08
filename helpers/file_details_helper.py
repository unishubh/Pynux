import os
import stat
import pwd
import grp
import time


class FileDetailsHelper():

    @staticmethod
    def get_files_from_path(path):
        try:
            files = os.listdir(path)
        except:
            print("Invalid path")
            return False
        return files

    @staticmethod
    def filter_hidden_files(files):
        visible_files = [filename for filename in files if filename[0] != '.']
        return visible_files

    @staticmethod
    def get_mode_info(detail):

        permissions = '-'
        color = ''
        link = ''

        if stat.S_ISDIR(detail):
            permissions = 'd'
            color = 'blue'
        elif stat.S_ISLNK(detail):
            permissions = 'l'
            color = "cyan"
            # link = os.readlink()
        elif stat.S_ISREG(detail):
            if detail & (stat.S_IXGRP | stat.S_IXUSR | stat.S_IXOTH):
                color = "green"
        mode = stat.S_IMODE(detail)

        for who in "USR", "GRP", "OTH":
            for what in "R", "W", "X":
                if mode & getattr(stat, "S_I" + what + who):
                    permissions = permissions + what.lower()
                else:
                    permissions = permissions + "-"

        return (permissions, color, link)

    @staticmethod
    def get_owner_name(detail):
        try:
            name = "%-8s" % pwd.getpwuid(detail.st_uid)[0]
        except KeyError:
            name = "%-8s" % detail.st_uid

        return name

    @staticmethod
    def get_owner_group(detail):
        try:
            group = "%-8s" % grp.getgrgid(detail.st_gid)[0]
        except KeyError:
            group = "%-8s" % detail.st_gid

        return group

    @staticmethod
    def get_time_of_creation(detail):
        ts = detail.st_mtime
        time_fmt = "%b %e  %Y"
        return time.strftime(time_fmt, time.gmtime(ts))

    @staticmethod
    def reverse_file_ordering(files):
        return reversed(files)

    @staticmethod
    def get_number_of_hardlinks(detail):
        return detail.st_nlink

    @staticmethod
    def is_a_folder(detail):
        if stat.S_ISDIR(detail):
            return True
        return False
