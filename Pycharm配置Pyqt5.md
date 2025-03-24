首先在终端中进入 conda的虚拟环境 用的是**Python3.9，**高版本的python没测试，之前3.10好像不行，一开始我用的3.12安装不上pyqt5-tools 老是卡住，索性换了python3.9的。

![image-20241208144258040](C:\Users\39335\Desktop\Hardward_Research\Pycharm配置Pyqt5.assets\image-20241208144258040.png)

![image-20241208130856170](C:\Users\39335\Desktop\Hardward_Research\Pycharm配置Pyqt5.assets\image-20241208130856170.png)

终端中进入虚拟环境  conda activate Python3.9

### **1--升级pip**

python -m pip install --upgrade pip

### **2--换源**

pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
pip config set install.trusted-host mirrors.aliyun.com

### **3--安装**

pip install PyQt5
pip install PyQt5-tools

安装成功会提示Successful

### **4--在虚拟环境的目录下找到designer.exe**

D:\Anaconda\envs\Python3.9\Lib\site-packages\qt5_applications\Qt\bin

![image-20241208132240304](C:\Users\39335\Desktop\Hardward_Research\Pycharm配置Pyqt5.assets\image-20241208132240304.png)

### **5、Pyuic和Pyrcc**

跟第四步一样 继续找到这个外部工具

pyuic是将ui文件转为py文件  使用的话是在Pycharm中打开Qtdesigner，然后保存到Pyuic的目录下

pyrcc是用于将Qt资源文件（.qrc文件）编译成.py 



D:\Anaconda\envs\Python3.9\Scripts\UI

**工作目录可以保存到自己想要的文件夹下**        

![image-20241208145217608](C:\Users\39335\Desktop\Hardward_Research\Pycharm配置Pyqt5.assets\image-20241208145217608.png)

填写实参：$FileName$ -o $FileNameWithoutExtension$.py

- 意思将选中的 `xxx.ui` 文件转换为同名的 `xxx.py`文件

- 需要特别注意的是，执行的时候需要右键选中对应的 `xxx.ui` 文件，不然会出错的。

  

D:\Anaconda\envs\Python3.9\Scripts\QRC  

**工作目录可以保存到自己想要的文件夹下**

![image-20241208140646977](C:\Users\39335\Desktop\Hardward_Research\Pycharm配置Pyqt5.assets\image-20241208140646977.png)



### **6--使用方法**

#### **--Pyuic5的使用**

首先是Qtdesigner，电脑上已经安装

然后再Pycharm中打开

![image-20241208133156093](C:\Users\39335\Desktop\Hardward_Research\Pycharm配置Pyqt5.assets\image-20241208133156093.png)

![image-20241208133203562](C:\Users\39335\Desktop\Hardward_Research\Pycharm配置Pyqt5.assets\image-20241208133203562.png)

把生成的ui文件保存到**pyuic5存放的文件夹下面**（可以再新建一个文件夹），就可以把ui转换成py了。

![image-20241208145136721](C:\Users\39335\Desktop\Hardward_Research\Pycharm配置Pyqt5.assets\image-20241208145136721.png)

![image-20241208145105904](C:\Users\39335\Desktop\Hardward_Research\Pycharm配置Pyqt5.assets\image-20241208145105904.png)



可以看到生成了asd.ui对应的asd.py文件



#### **--Pyrcc5的使用**

再Qtdesigner中 右键添加样式表

![image-20241208135728255](C:\Users\39335\Desktop\Hardward_Research\Pycharm配置Pyqt5.assets\image-20241208135728255.png)

点击添加资源

![image-20241208135747083](C:\Users\39335\Desktop\Hardward_Research\Pycharm配置Pyqt5.assets\image-20241208135747083.png)

点击笔

![image-20241208135756680](C:\Users\39335\Desktop\Hardward_Research\Pycharm配置Pyqt5.assets\image-20241208135756680.png)

然后左下角新建文件

D:\Anaconda\envs\Python3.9\Scripts\QRC

保存到pyrcc的文件夹下面

![image-20241208135852145](C:\Users\39335\Desktop\Hardward_Research\Pycharm配置Pyqt5.assets\image-20241208135852145.png)

然后添加名字

![image-20241208135918052](C:\Users\39335\Desktop\Hardward_Research\Pycharm配置Pyqt5.assets\image-20241208135918052.png)

随便导入一个照片,要在这个目录下面，相对路径

![image-20241208141100193](C:\Users\39335\Desktop\Hardward_Research\Pycharm配置Pyqt5.assets\image-20241208141100193.png)

![image-20241208141120529](C:\Users\39335\Desktop\Hardward_Research\Pycharm配置Pyqt5.assets\image-20241208141120529.png)

点击OK

在url前面随便写点东西 

![image-20241208140053774](C:\Users\39335\Desktop\Hardward_Research\Pycharm配置Pyqt5.assets\image-20241208140053774.png)

OK！

右下角已经有了资源

![image-20241208141152604](C:\Users\39335\Desktop\Hardward_Research\Pycharm配置Pyqt5.assets\image-20241208141152604.png)

然后到pycharm中使用pyrcc

打开这个目录 点击test.qrc文件

![image-20241208141357250](C:\Users\39335\Desktop\Hardward_Research\Pycharm配置Pyqt5.assets\image-20241208141357250.png)

![image-20241208141440204](C:\Users\39335\Desktop\Hardward_Research\Pycharm配置Pyqt5.assets\image-20241208141440204.png)

**可以看到已经生成了py文件，至此成功把qrc文件编译成py文件，完成了pyrcc的使用！**

### 7--测试：

**测试**一下Dialog

（如果要用图的话得用MainWindow，之前QtCreator生成的，本质上就是生成Qtcreator制作的窗口，主要的还是测试python和qtcreator的关联功能）

![image-20241208142811939](C:\Users\39335\Desktop\Hardward_Research\Pycharm配置Pyqt5.assets\image-20241208142811939.png)

这里需要把QRC生成的文件rc放到UI目录下，因为生成的py文件有一行 import test_rc 

在test.py最下面添加这段测试代码

**直接添加测试代码就可以，不一定要加 import test_rc**  ---后面测试得出

#### **测试代码如下：**

```
import test_rc
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog
import sys
if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(window)

    window.show()
    sys.exit(app.exec_())
```

测试！

切换到该环境的编解释器，然后编译运行

![image-20241208142917662](C:\Users\39335\Desktop\Hardward_Research\Pycharm配置Pyqt5.assets\image-20241208142917662.png)

![image-20241208142936459](C:\Users\39335\Desktop\Hardward_Research\Pycharm配置Pyqt5.assets\image-20241208142936459.png)

