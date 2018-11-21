# -*- coding:utf-8 -*-
# Author : luck
import sys

from AutoBuildRunClass import AutoBuildRun

if __name__ == '__main__':

    if len(sys.argv) < 2:
        exit('请输入SQL文件路径')

    autoBuildRun = AutoBuildRun()
    argvNum = sys.argv.__len__() - 1
    for i in range(1,sys.argv.__len__()):
        autoBuildRun.run(sys.argv[i])


