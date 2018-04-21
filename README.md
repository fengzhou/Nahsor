# Nahsor
一个接口测试平台

    1. pip install allure-pytest                            # 安装allure-pytest插件
    2. py.test --alluredir=%allure_result_folder% ./tests   # 运行case并指定allure结果文件位置？
    3. allure serve %allure_result_folder%                  # 不知道啥意思，可能是默认结果文件夹？
    4. py.test --alluredir ./test                           # 同上


# Mac安装allure
如果是Mac电脑，推荐使用Homebrew安装。

    $ brew install allure


## 生成测试报告
安装完成后，通过下面的命令将./result/目录下的测试数据生成测试报告：

    $ allure generate ./result/ -o ./report/ --clean
    
这样在./report/目录下就生成了Allure的测试报告了;–clean目的是先清空测试报告目录，再生成新的测试报告。


## 打开测试报告
通过下面的命令打开测试报告：

    $ allure open -h 127.0.0.1 -p 8083 ./report/
本机的浏览器将打开http://127.0.0.1:8083/index.html网页，展示测试报告。


# Windows安装allure
## 1. 安装scoop
在windows powershell 输入：  

    1. Set-ExecutionPolicy RemoteSigned -scope CurrentUser  
    2. iex (new-object net.webclient).downloadstring('https://get.scoop.sh')  
    
## 2. 安装allure
#### 2.1在cmd输入:

    scoop install allure  
#### 2.2 配置java环境变量  

#### 2.3 安装allure-pytest  
    
    pip install allure-pytest

## 3. 运行脚本并生成测试报告需要的文件:

    py.test --alluredir=%allure_result_folder% ./tests
    
## 4. 生成报告:

    allure generate ./result/ -o ./report/ --clean
## 5. 打开报告:

    allure open -h 127.0.0.1 -p 8083 ./report/


# Pytest测试样例的命名规则

    1. 测试文件以test_开头或结尾(否则用py.test命令行不能自动识别)
    2. 测试类以Test开头，且不能带有init方法
    3. 测试函数以test_开头
    4. 断言使用assert
    5. fixture的文件名必须是conftest.py



# 参考

https://github.com/taverntesting/tavern

https://www.kawabangga.com/posts/2662

https://docs.pytest.org/en/latest/example/nonpython.html#yaml-plugin

https://docs.pytest.org/en/latest/contents.html

https://www.ctolib.com/taverntesting-tavern.html

http://cuyu.github.io/python/2016/10/12/Play-Python-Library%E4%B9%8Bpytest-plugin%E7%AF%87

https://html5up.net/
