# -*- mode: python -*-
import glob
deptypes = ('*.jpg', '*.png', '*.png', '*.ttf')
depList = []

alldeps = []
for deps in deptypes:
	alldeps.extend(glob.glob('c:\\users\\billy\\desktop\\python\\pq\\' + deps))

for eachdep in alldeps:
	depParts = eachdep.split('\\')
	depList.append( (depParts[-1], eachdep, 'DATA') )

a = Analysis(['c:\\users\\billy\\desktop\\python\\pq\\penguinQuest.py'],
             pathex=['C:\\Users\\Billy\\Desktop\\pyinstaller\\pyinstaller-2.0'],
             hiddenimports=[],
             hookspath=None)

a.datas += depList

pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name=os.path.join('dist', 'penguinQuest.exe'),
          debug=False,
          strip=None,
          icon='c:\\users\\billy\\desktop\\python\\pq\\penguin.ico',
          upx=True,
          console=False )
app = BUNDLE(exe,
             name=os.path.join('dist', 'penguinQuest.exe.app'))
