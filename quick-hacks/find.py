# Task: Implement find
#X v1: find <starting dir>
#X v2: find <starting dir> -name "*.txt"
#X v3: find <starting dir> -type d
# v4: -type f
# v5: -exec {} \;
# v5: -perm xxx
import argparse
import glob
import os
import sys
class Cmd(object):
    def __init__(self):
        print(sys.argv)
        parser = argparse.ArgumentParser()
        parser.add_argument("dir",
                            help="The starting directory",
                            type=str)
        parser.add_argument("-name", help="Filter by name", type=str)
        parser.add_argument("-type", help="Filter by type", type=str)

        # Treat exec like a subcommand.
        # Enable subcommand ability
        subparser = parser.add_subparsers(help="Subcommand help")
        parser_exec = subparser.add_parser('exec', help='Execute an action')
        parser_exec.add_argument('cmd', help="Action to take", 
                type=str, nargs='+')

        self._args = parser.parse_args()
        print(parser.parse_known_args())

    def find(self):

        path = self._args.dir if self._args.dir else '.'
        path += '/**' # Modify path to search in subdirectories

        if self._args.name:
            path += '/%s' % self._args.name

        for name in glob.iglob(path, recursive=True):
            if self._args.type == 'd' and not os.path.isdir(name):
                continue
            if hasattr(self._args,'cmd'):
                # print('exec present')
                # do stuff here
                self.__exec(name)
            else:
                print(name)


    def __exec(self, path):
        #print('action=_exec', 'current_path=%s' % path, 'cmd=', 
        #       self._args.cmd[0])
        command_to_run = '%s %s' % (self._args.cmd[0], path)
        os.system(command_to_run)

if __name__ == '__main__':
    Cmd().find()
