#!c:\users\asult\documents\python projects\learning_log\ll_env\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'static==1.1.1','console_scripts','static'
__requires__ = 'static==1.1.1'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('static==1.1.1', 'console_scripts', 'static')()
    )
