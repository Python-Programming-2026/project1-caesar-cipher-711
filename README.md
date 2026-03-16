[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/fPQK30A4)
说明文档
这是一个使用 Python 编写的凯撒密码（Caesar Cipher）加密与解密工具。  
该程序支持任意整数密钥，并能够处理大小写字母，同时保持非字母字符不变。

 一、凯撒密码

凯撒密码是一种经典的替换加密方法，相传由古罗马统帅凯撒用于军事通信。

其基本思想是：

将字母在字母表中按固定距离进行移动。

例如：

明文

Hello

密钥 = 3

加密结果

Khoor

 二、功能特点

本程序具有以下特点：

支持 加密和解密
密钥支持 任意整数
自动进行 模26运算
保留 数字、标点、空格
同时支持 大小写字母
使用示例
加密示例
=== 凯撒密码工具 ===
请选择模式：A=加密  B=解密：A
请输入密钥（整数）：5
请输入明文：Hello, World

加密后的密文为：
Mjqqt, Btwqi
解密示例
=== 凯撒密码工具 ===
请选择模式：A=加密  B=解密：B
请输入密钥（整数）：5
请输入密文：Mjqqt, Btwqi

解密后的明文为：
Hello, World
代码结构说明
项目主要包含两个核心部分：
1 核心函数
caesar(text, key, decrypt)
功能：
对输入文本进行凯撒密码加密或解密。
参数：
text
输入文本
key
加密密钥
decrypt
是否为解密模式
2 主程序
main()
功能：
提供用户交互界面，获取用户输入并调用加密函数。
算法原理
凯撒密码的数学表达式为：
加密：
E(x) = (x + k) mod 26
其中：
x 表示字母在字母表中的位置
k 表示密钥
解密：
D(x) = (x - k) mod 26
