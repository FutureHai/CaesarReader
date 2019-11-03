# CaesarReader
pyqt5

1)pyinstall package exe

pyinstaller -D -w -i favicon.ico main.py
打包时添加以下内容
import sys, os
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
    

2)cx_Freeze package exe

from cx_Freeze import setup, Executable
import sys
base = 'WIN32GUI' if sys.platform == "win32" else None


executables = [Executable("main.py", base=base, icon='favicon.ico')]

packages = []
include_files=['favicon.png']
options = {
    'build_exe': {
        'packages':packages,
        'include_files': include_files
    },

}

setup(
    name = "prog",
    options = options,
    version = "1.0",
    description = 'desc of program',
    executables = executables
)

# 执行以下命令打包
# python setup.py build
