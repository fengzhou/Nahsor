# Nahsor
一个接口测试平台


$ pip install allure-pytest
$ py.test --alluredir=%allure_result_folder% ./tests
$ allure serve %allure_result_folder%

py.test --alluredir ./test


安装命令行工具
首先需要安装命令行工具，如果是Mac电脑，推荐使用Homebrew安装。
```$ brew install allure```


生成测试报告
安装完成后，通过下面的命令将./result/目录下的测试数据生成测试报告：
```$ allure generate ./result/ -o ./report/ --clean```
这样在./report/目录下就生成了Allure的测试报告了。–clean目的是先清空测试报告目录，再生成新的测试报告。


打开测试报告
通过下面的命令打开测试报告：
```$ allure open -h 127.0.0.1 -p 8083 ./report/```
本机的浏览器将打开http://127.0.0.1:8083/index.html网页，展示测试报告。


#安装scopr
1、在windows powershell 输入：  
Set-ExecutionPolicy RemoteSigned -scope CurrentUser  
iex (new-object net.webclient).downloadstring('https://get.scoop.sh')  
# 安装allure
2、在cmd输入  
scoop install allure  
3、配置java环境变量  
4、安装allure-pytest  
OK
运行脚本并生成测试报告需要的文件
py.test --alluredir=%allure_result_folder% ./tests
生成报告
allure generate ./result/ -o ./report/ --clean
打开报告
allure open -h 127.0.0.1 -p 8083 ./report/


# Pytest测试样例的命名规则
测试文件以test_开头或结尾(否则用py.test命令行不能自动识别)
测试类以Test开头，且不能带有init方法
测试函数以test_开头
断言使用assert
fixture的文件名必须是conftest.py



https://github.com/LangJin/Nahsor/invitations