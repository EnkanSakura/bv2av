# bv2av
 b站av号和bv号的相互转换

## Problem

bv号较av号复杂不易于记忆，制作了该简易av号和bv号的相互转换工具

## Solution

### 核心解码部分的代码来自于知乎回答

> 如何看待 2020 年 3 月 23 日哔哩哔哩将稿件的「av 号」变更为「BV 号」？ - mcfx的回答 - 知乎
>
>  https://www.zhihu.com/question/381784377/answer/1099438784

算法可移步至原回答，此处不再赘述	~~（因为我也看不懂）~~

只对原代码末尾**输出示例部分**进行删改

### **GUI**

**使用wxpython**

由于py刚接触不久并不熟练，wx也是现学现卖，照着案例删删改改就成了这副模样（起码能用了）

最初是在原回答的代码的基础上加了个菜单循环做成控制台程序，用惯了C++实在无法适应Py，便直接套了个GUI出来