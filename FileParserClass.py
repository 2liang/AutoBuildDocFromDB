# -*- coding:utf-8 -*-
import re


class FileParser:

    def __init__(self):
        pass

    # 定义分离SQL文件匹配模式
    # table_pattern = r'CREATE TABLE([\s\S]*?)LOCK TABLES'    #分离表
    table_pattern = r'CREATE TABLE([\s\S]*?);'
    name_pattern = r'.*?`(.*?)`.*?'  # 获取表名称或字段名称
    table_content_pattern = r'COMMENT=\'(.*?)\''  # 获取表详情

    def separatTable(self, content):
        '''将SQL文件中各个表分离开来
        :param content:文件内容
        :return:表分离后的内容
        '''
        pattren = re.compile(self.table_pattern)
        table_list = re.findall(pattren, content)
        return table_list

    def parserTableName(self, table_list):
        '''
        解析出数据库中所有表的表名
        列表中前者为表名,后者为表含义
        :param table_list:
        :return:
        '''
        dirty_table_name = []
        dirty_table_content = []
        table_name = []
        # 取出表名和表含义行脏数据
        for table in table_list:
            tmp = table.split('\n')
            dirty_table_name.append(tmp[0])
            dirty_table_content.append(tmp[-1])

        for i in range(len(dirty_table_name)):
            tmp = []
            # 从脏数据中取出表名
            # print dirty_table_name[i].strip()
            name = re.match(self.name_pattern, dirty_table_name[i].strip())
            if name != None:
                # print name.group(1)
                tmp.append(name.group(1))

            # 从脏数据中取出表含义
            content = re.match(self.table_content_pattern, dirty_table_content[i].split(' ')[-1])
            if content != None:
                tmp.append(content.group(1))
            else:
                tmp.append('')
            table_name.append(tmp)
        return table_name

    def parserColumn(self, table_list, table_name):
        '''
        获取字段情况
        :param table_list: separatTable中分离出的数据
        :param table_name: parserTableName中解析出的数据
        :return:
        '''
        dirty_column_list = []
        for table in table_list:
            dirty_column_list.append(table.split('\n')[1:-1])
        table_data = []

        for i in range(len(dirty_column_list)):
            dirty_column = []
            dirty_column = dirty_column_list[i]
            column_tmp = []
            '''
            先取两边空格
            用空格分割
            第一个有没有``,有取出来,无舍弃
            '''
            for column in dirty_column:
                tmp_list = column.strip().split(' ')
                column_name = re.match(r'`(.*?)`', tmp_list[0])
                if column_name != None:
                    column_name = column_name.group(1)
                    column_type = tmp_list[1]
                    # TODO:此处无法正确匹配,使用取列表最后一项,可能会有bug
                    column_comment = re.match(r'.*?COMMENT \'(.*?)\'.*?', column.strip())
                    if column_comment is not None:
                        column_comment = column_comment.group(1)
                    else:
                        column_comment = ''

                    # if '\'' in tmp_list[-1]:
                    #     column_comment = tmp_list[-1][1:-2]
                    # else:
                    #     column_comment = ''
                    column_tmp.append([column_name, column_type, column_comment])
            table_data.append([table_name[i], column_tmp])
        return table_data
