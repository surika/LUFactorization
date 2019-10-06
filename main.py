import argparse # 用于读取命令行参数

default_matrix = '1 2 -3 4, 4 8 12 -8,2 3 2 1, -3 -1 1 -4'
PLU = False

parser = argparse.ArgumentParser(description='程序参数')
parser.add_argument('-i','--input',  help='输入需要处理的矩阵，可从命令行或文件输入.默认值为例题', default = default_matrix)
parser.add_argument('-p','--plu',  help='生成PLU分解。若主元位置需要行交换/希望使用部分主元法，请设置为True.默认值为True', default=True)
parser.add_argument('-o','--output',  help='将分解结果输出到文件.默认值为空', default = "output")
args = parser.parse_args()

# 打印矩阵
def PrintMatrix(M, name):
	print(name)
	for i in M:
		print(i)

def LU(A, is_change):
	# 确定矩阵的维度
	dim = len(A)

	# 根据输出矩阵的维度定义分解得到的矩阵的维度，它们维度相同
	P = [[0] * dim for _ in range(dim)]
	L = [[0] * dim for _ in range(dim)]
	#A_row.sort(key=(lambda x: abs(x[0])), reverse=True)  # 根据每行第一个元素的大小排序
	U = []
	# 附加一列记录每行原来的位置，用于生成置换矩阵P
	for i in range(dim):
		A[i].append(i)
	# 处理第i个主元
	for i in range(dim):
		if is_change:
			# 使用部分主元法：需要交换，否则不需要
			pivot_column_abs = [abs(x[i]) for x in A]
			# 部分主元法将当前主元位置数值（绝对值）最大的交换到当前行
			max_index = pivot_column_abs.index(max(pivot_column_abs))
			# 进行交换
			A[0], A[max_index] = A[max_index], A[0]
			# 用置换矩阵P记录行交换
			P[i][A[0][-1]] = 1

		# 已确定的行加入上三角矩阵U
		U.append(A[0][:-1])
		for j in range(1, dim - i): # 处理第j行
			# 进行行倍加变换
			multiple = A[j][i] / A[0][i]
			for k in range(i, dim):
				A[j][k] = A[j][k] - multiple * A[0][k]
			# 为了方便，暂时使用A矩阵记录L矩阵中的元素，该位置实际值应为0
			A[j][i] = multiple
		# 去掉已经处理完的行
		A = A[1:]

	# 生成L矩阵
	for i in range(dim):
		L[i][i] = 1
		for j in range(i):
			L[i][j] = U[i][j]
			U[i][j] = float(0)

	# 输出分解结果
	PrintMatrix(P,'P')
	PrintMatrix(L, 'L')
	PrintMatrix(U, 'U')

	# 输出到文件
	if len(args.output) > 0:
		with open(args.output, 'a') as f:
			f.write('P:\n')
			for i in P:
				f.write(str(i))
				f.write('\n')
			f.write('L:\n')
			for i in L:
				f.write(str(i))
				f.write('\n')
			f.write('U:\n')
			for i in U:
				f.write(str(i))
				f.write('\n')


if __name__ == '__main__':

	A_row = []
	ls = args.input.split(',')
	# 从命令行输入
	if len(ls) != 1:
		for line in ls:
			l = line.strip().split()
			l = [float(i) for i in l]
			A_row.append(l)
	# 从文件中读取矩阵
	else:
		file_name = args.input

		with open(file_name, 'r') as f:
			for line in f.readlines():
				l = line.strip('\n').split()
				l = [float(i) for i in l]
				A_row.append(l)

	A_copy = A_row[:]
	PrintMatrix(A_row, 'A')
	# 判断矩阵形状，不是方阵则没有LU分解
	len_row = len(A_row)
	lens_column = set([len(column) for column in A_row])
	if not (len(lens_column) == 1 and len_row in lens_column):
		print('输入的矩阵不是方阵，不存在LU分解')
	else:
		try:
			LU(A_row, args.plu)
		except ZeroDivisionError:
			if not args.plu:
				print('在主元位置遇到0，将尝试行交换')
				try:
					LU(A_copy, True)
				except ZeroDivisionError:
					print('矩阵不满秩，不存在LU分解')
			else:
				print('矩阵不满秩，不存在LU分解')
