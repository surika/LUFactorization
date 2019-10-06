2019-20 秋季学期 中国科学院大学 《矩阵分析与应用》课程作业
# 要求
我在编写时使用的解释器版本为Python 3.6.2， 但考虑到程序只使用了Python的基本功能，并没有应用高级特性，也没有引入外部包，所以对环境几乎无要求。 
# 使用
```bash
python main.py -i=input -p=True -o=output
```
## 输入
input可以来自命令行或文件。

若从命令行输入，请用-i参数传入每行元素用**空格**分隔，行与行之间用**逗号**分割的矩阵。
```bash
python main.py -i='1 2 -3 4, 4 8 12 -8, 2 3 2 1, -3 -1 1 -4'
```
若从文件输入，请用-i参数传入文件名，文件格式为**矩阵每行占一行**，元素间用**空格**分隔
```bash
python main.py -i=matrix_file_name
```
输入文件格式参考：
```
1 2 -3 4
4 8 12 -8
2 3 2 1
-3 -1 1 -4
```
## 是否进行PLU分解/使用部分主元法/需要行交换
若输入的矩阵需要行交换调整主元位置，或者使用部分主元法保证较高的数值稳定性，则需要对-p传入True，使用PLU分解;若只需要生成最基本的LU分解，请传入False。**该项参数的默认值为True。**

PLU分解除了生成一个下三角矩阵 L 与上三角矩阵 U 之外，还将生成置换矩阵 P ，用于调整行顺序。 
## 输出
用-o参数传入文件名，可以将生成的分解结果写入指定文件中。
---
以上参数均可以使用--help获取详细说明
```
# python main.py --help

usage: main.py [-h] [-i INPUT] [-p PLU] [-o OUTPUT]

程序参数

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        输入需要处理的矩阵，可从命令行或文件输入.默认值为例题
  -p PLU, --plu PLU     生成PLU分解。若主元位置需要行交换/希望使用部分主元法，请设置为True.默认值为False
  -o OUTPUT, --output OUTPUT
                        将分解结果输出到文件.默认值为空

```
