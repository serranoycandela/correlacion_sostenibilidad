import os
import shutil
import glob
def patch_osx_app():
    """Patch .app to copy missing data and link some libs.
    See https://github.com/pyinstaller/pyinstaller/issues/2276
    """
    app_path = os.path.join('dist', 'dashboard.app')
    qtwe_core_dir = os.path.join('/Library', 'Frameworks', 'Python.framework', 'Versions','3.6', 'lib', 'python3.6',
                                 'site-packages', 'PyQt5', 'Qt', 'lib',
                                 'QtWebengineCore.framework')
    # Copy QtWebEngineProcess.app
    proc_app = 'QtWebEngineProcess.app'
    shutil.copytree(os.path.join(qtwe_core_dir, 'Helpers', proc_app),
                    os.path.join(app_path, proc_app))
    # Copy resources
    for f in glob.glob(os.path.join(qtwe_core_dir, 'Resources', '*')):
        dest = os.path.join(app_path)
        if os.path.isdir(f):
            shutil.copytree(f, os.path.join(dest, f))
        else:
            shutil.copy(f, dest)
    # Link dependencies
    # for lib in ['QtCore', 'QtWebEngineCore', 'QtQuick', 'QtQml', 'QtNetwork',
    #             'QtGui', 'QtWebChannel', 'QtPositioning']:
    #     dest = os.path.join(app_path, lib + '.framework', 'Versions', '5')
    #     os.makedirs(dest)
    #     os.symlink(os.path.join(os.pardir, os.pardir, os.pardir, 'Contents',
    #                             'MacOS', lib),
    #                os.path.join(dest, lib))

patch_osx_app()
