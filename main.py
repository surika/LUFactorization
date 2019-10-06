import argparse # 用于读取命令行参数

A_row = [[2,2,2],[4,7,7],[6,18,22]]
A_row = [[1,2,-3,4],[4,8,12,-8],[2,3,2,1],[-3,-1,1,-4]]
A_row = [[1,2,4,17],[3,6,12,3],[2,3,-3,2],[0,0,0,0]]
default_matrix = '1 2 -3 4, 4 8 12 -8,2 3 2 1, -3 -1 1 -4'
PLU = False

parser = argparse.ArgumentParser(description='程序参数')
parser.add_argument('--matrix', '-m', help='需要处理的数据，非必要参数', default = default_matrix)
parser.add_argument('--plu', '-p', help='若希望使用PLU分解/主元位置需要行交换/希望使用部分主元法，请选择True.默认值为True', default=True)
args = parser.parse_args()

def PrintMatrix(M, name):
	print(name)
	for i in M:
		print(i)

def LU(A_row):
	dim = len(A_row)

	P = [[0] * dim for _ in range(dim)]
	L = [[0] * dim for _ in range(dim)]
	#A_row.sort(key=(lambda x: abs(x[0])), reverse=True)  # 根据每行第一个元素的大小排序
	U = []
	for i in range(dim):
		A_row[i].append(i)
	for i in range(dim): # 处理第i个主元
		#'''
		# 使用部分主元法：需要交换，否则不需要
		pivot_column_abs = [abs(x[i]) for x in A_row]
		max_index = pivot_column_abs.index(max(pivot_column_abs))
		A_row[0], A_row[max_index] = A_row[max_index], A_row[0]
		#'''
		P[i][A_row[0][-1]] = 1

		U.append(A_row[0][:-1])
		for j in range(1, dim - i): # 处理第j行
			multiple = A_row[j][i] / A_row[0][i]
			for k in range(i, dim):
				A_row[j][k] = A_row[j][k] - multiple * A_row[0][k]
			A_row[j][i] = multiple
		A_row = A_row[1:]

	# 生成L矩阵
	for i in range(dim):
		L[i][i] = 1
		for j in range(i):
			L[i][j] = U[i][j]
			U[i][j] = 0

	PrintMatrix(P,'P')
	PrintMatrix(L, 'L')
	PrintMatrix(U, 'U')


if __name__ == '__main__':

	A_row = []
	ls = args.matrix.split(',')
	if len(ls) != 1: # 从命令行输入
		for line in ls:
			l = line.strip().split()
			l = [float(i) for i in l]
			A_row.append(l)
	else: # 从文件中读取矩阵
		file_name = args.matrix

		with open(file_name, 'r') as f:
			for line in f.readlines():
				l = line.strip('\n').split()
				l = [float(i) for i in l]
				A_row.append(l)
	PrintMatrix(A_row, 'A')
	LU(A_row)

'''
	len_row = len(A_row)
	lens_column = set([len(column) for column in A_row])
	if not (len(lens_column) == 1 and len_row in lens_column):
		print('输入的矩阵不是方阵，不存在LU分解')
	else:
		try:
			LU()
		except ZeroDivisionError:
			if not PLU:
				print('在主元位置遇到0，将尝试行交换')
				PLU = False
				try:
					LU()
				except ZeroDivisionError:
					print('矩阵不满秩，不存在LU分解')
'''


