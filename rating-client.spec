# -*- mode: python -*-

block_cipher = None


a = Analysis(['rating-client.py'],
             pathex=['/home/tarun/FloRate-Dapp'],
             binaries=[],
             datas=[('/home/tarun/FloRate-Dapp/AddBtn.gif',''),('/home/tarun/FloRate-Dapp/RenmBtn.gif','')],
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
          console=True )
