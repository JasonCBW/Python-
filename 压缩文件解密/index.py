# coding:utf-8

import zipfile

class BreakZipFile:
    def extractFile(self, toPath, zFile, password):
        try:
            zFile.extractall(path=toPath,pwd=password);
            return password
        except Exception, e:
            print '当前尝试密码：' + password + '\t失败'

    def main(self):
        zFile = zipfile.ZipFile("test.zip")
        passFile = open('dict.txt')
        for line in passFile.readlines():
            password = line.strip('\n').strip()
            guess = self.extractFile(".", zFile, password);
            if guess:
                print '\n破解成功\n当前尝试密码：' + password
                exit(0)

bk = BreakZipFile()
bk.main()
