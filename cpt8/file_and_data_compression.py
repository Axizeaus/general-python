from zipfile import ZipFile

with ZipFile('example.zip', 'w') as z:
    z.write('content1.txt')
    z.write('content2.txt')
    z.write('content3.mp3')
    z.write('subfolder/content4.mp4')
with ZipFile('example.zip') as z:
    z.extract('content1.txt', 'extract.zip')
    z.extract('subfolder/content4.mp4', 'extract_zip')