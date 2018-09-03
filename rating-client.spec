# -*- mode: python -*-

block_cipher = None


a = Analysis(['rating-client.py'],
             pathex=['/home/tarun/Downloads/Compressed/FloRate-Dapp-master'],
             binaries=[],
             datas=[('/home/tarun/FloRate-Dapp-master/AddBtn.gif',''),('/home/tarun/FloRate-Dapp-master/RenmBtn.gif','')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='rating-client',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False , manifest='rating-client.spec')
