#!/usr/bin/env python
"""
Python 2.x

clientwrapper.py

Usage: clientwrapper.py -v|h
       clientwrapper.py [-c] shred <directory>
       clientwrapper.py [-k] service <name>
       clientwrapper.py [-b backup_dir] archive <from_dir> <to_dir>
"""
import sys

__VERSION = '1.0'

def shred_dir():
    pass

def change_service():
    pass

def archive_dir():
    pass

def get_usage(args):
    usage = ''
    for k in args:
        tabs = '\t' * 3
        if len(k) > 2:
            tabs = '\t'
        usage += '\t-%s%s%s\n' % (k, tabs, args[k][0])
    return 'Usage: clientwrapper.py [options] [command] [arguments]\n%s' % usage

def print_version():
    print '\clientwrapper.py\t\tv%s\n' % __VERSION
    sys.exit(0)

def print_help():
    print __HELP
    sys.exit(0)

def validate_args(argv, valid_args):
    doable = []
    params = {}
    for i, arg, in enumerate(argv):
        if arg[0] == '-':
            if len(arg) > 2 and arg[1:] in valid_args:
                return [[valid_args[1:][2], None]]
            elif arg[1:] in valid_args:
                req_params = valid_args[arg[1:]][1]
                if req_params:
                    for j in range(0, req_params + 1):
                        params[arg] = argv[(i + 1) +  j]
                    if not params:
                        params[arg] = True
                continue

        if arg[1:] in valid_args:
            for j in range(0, valid_args[arg][1] + 1):
                params[arg] = argv[(i + 1) +  j]
            doable.append([valid_args[arg[1:]][2], params])
    return doable

__VALID_ARGS = {'v':['Display version', 0, print_version],
                '-version':['Display version', 0, print_version],
                'h':['Displays help information', 0, print_help],
                '-help':['Displays help information', 0, print_help],
                'c':['Used with shred command to specify contents only', 0, None],
                'k':['Used with service command to kill specified service', 0, None],
                'b':['Used with archive command to specify a backup directory', 1, None],
                'shred':['Shreds a directory or with -c the contents only', 1, shred_dir],
                'service':['Starts or with -k kills a service', 1, change_service],
                'archive':['Archives a folder, optionally with -b sets backup too', 2, archive_dir]}

__HELP = """clientwrapper.py -v|h
            clientwrapper.py [-c] shred <directory>
            clientwrapper.py -k|s service <name>
            clientwrapper.py [-b backup_dir] archive <from_dir> <to_dir>"""

def main(argv):
    doable_args = []
    if not argv:
        return get_usage(__VALID_ARGS)

    doable_args = validate_args(argv, __VALID_ARGS)
    if not doable_args:
        return get_usage(__VALID_ARGS)

    for arg in doable_args:
        f = arg[0]
        if len(arg) > 1:
            f(arg[1])
            continue
        f()

    # Python 2.x
    raw_input("Press [ENTER] to exit...")

    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
