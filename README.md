# AutoBuildDocFromDB
使用SQL文件自动生成markdown格式的数据库文档。

## 使用说明

1. 使用git克隆该项目

2. 从数据库中导出sql文件,请尽量导出只有表结构无表数据的sql文件

3. 在项目目录下运行，多个sql文件空格分隔:
`python build.py sql_dir.sql sql_dir_1.sql sql_dir_2.sql`
其中sql_dir为您的sql文件路径

4. 生成成功的md文件,在项目的md文件夹中,文件名同您的sql文件名
