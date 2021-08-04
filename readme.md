# VAPD代码存档

**项目文件py**，是数据依赖的运算程序

**项目文件**  存放前端展示程序 ->static->XiTong.html

## VAPD概述

VAPD是一个用于分析蛋白质内部的动态口袋的程序。支持2D加3D交互探索蛋白质中口袋的各种动态特性，可以分析口袋之间的相关性（探索别构位点），口袋连续性，口袋的理化性质。

在应用中可以作为辅助制药（别构药物）的小工具。



## 小插件

调用应用 文件夹

自动调用pymol程序

ev录屏自动录屏脚本

## 数据介绍

数据来源 http://www.d3pharma.com/D3Pocket/index.php      GPX4

数据介绍：蛋白质GPX4的分子动力学模拟数据，数据1000帧，使用fpocket抽取pocket

抽取的口袋数据存放在 ：<u>项目py->data</u>    测试数据： <u>项目py->testdata</u>

## 使用方法

使用fpocket提取口袋之后的数据文件

-  mdpout_mdpocket_atoms  

- mdpout_mdpocket

  

  上面两个文件存放入 项目py ->data中，根据需求运行main.py

运行完毕之后，打开项目文件->static->XiTong.html 查看结果

##### 程序改进方向

- 目前只提供了一个蛋白质中不同口袋相关性计算，需要适配不同蛋白质口袋相关性的计算
- 前端展示页面进行改进适配上述分析需求
- nglview插件交互调试