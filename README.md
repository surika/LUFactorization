This is my homework for 'Matrix Analysis and Application' 2019-20 Fall, UCAS
# Requirement
There's almost no requirement for environment because neither advanced functions nor external packages have I used.

As a reference, My interpreter is Python 3.6.2 
# Usage
```
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
for example:
```bash
python main.py -i=input -p=True -o=output
```
