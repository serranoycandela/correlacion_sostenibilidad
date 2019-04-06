# -*- mode: python -*-

block_cipher = None

added_files = [
                ( '/Users/fidel/Documents/GitHub/correlacion_sostenibilidad/*.png', '.' ),
                ( '/Users/fidel/Documents/GitHub/correlacion_sostenibilidad/*.ico', '.' ),
                ( '/Users/fidel/Documents/GitHub/correlacion_sostenibilidad/*.xlsx', '.' )
              ]

a = Analysis(['dashboard.py'],
             pathex=['/Users/fidel/Documents/GitHub/correlacion_sostenibilidad'],
             binaries=[
                   ('/Library/Frameworks/Python.framework/Versions/3.6/lib/libtk8.6.dylib', 'tk'),
                   ('/Library/Frameworks/Python.framework/Versions/3.6/lib/libtcl8.6.dylib', 'tcl')],
             datas = added_files,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False
         )
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='dashboard',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
          icon='/Users/fidel/Documents/GitHub/correlacion_sostenibilidad/logo.ico' )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='dashboard')
