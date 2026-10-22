# -*- mode: python -*-
a = Analysis(['MainWindow.py'],
             pathex=['D:\\WPy64-313110\\applications\\SEBASTES\\application'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='SEBASTES.exe',
          debug=False,
          strip=None,
          upx=True,
          console=False , version='version.txt', icon='resources\\rockfish.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name='application')
