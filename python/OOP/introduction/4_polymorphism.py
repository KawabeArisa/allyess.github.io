# 4_多態性（ポリモーフィズム）
# https://obgynai.com/%e3%80%90object-orientation-2/
# 多態性とは同じ振る舞い（method）を使い、オブジェクトによって異なる振る舞いをすること
# (1) オーバーライドとは子クラスで親クラスの宣言を上書きすること
#     'レオ'オブジェクトと'ピジョン'オブジェクトで異なる振る舞いをすること
# (2) オーバーロードとは引数、型の違いなどで、同じメソッド名を複数作ること

# Animal(親クラス)
class Animal():
	def __init__(self, name, weight):
		self.name = name
		self.weight = weight

	def sleep(self):
		print(self.name, '寝る')

	def eat(self):
		print(self.name, '食べる')

	# (1)
	def make_sound(self):
		# ① 子クラスでオーバーライドしなくても良い場合
		# pass
		# ② 子クラスでオーバーライドを必ずして欲しい場合。
		# 　子クラスでオーバーライドしていないとエラーが発生する。
		raise NotImplementedError


# Dog（子クラス）
class Dog(Animal):
	def __init__(self, name, weight, breed):
		#Animalクラスのコンストラクタを追加
		super().__init__(name, weight)
		self.breed = breed
	# (2)
	def run(self, speed = '普通'):
		if speed == '普通':
			print(self.name, '普通に走る')

		elif speed == '速い':
			print(self.name, '速く走る')

		elif speed == '遅い':
			print(self.name, '遅く走る')

	def make_sound(self):
		print(self.name, 'ワン！ワン！') 

# Bird（子クラス）
class Bird(Animal):
	def __init__(self, name, weight, types):
		super().__init__(name, weight)
		self.types = types

	def fly(self):
		print(self.name, '飛ぶ')

	def make_sound(self):
		print(self.name, 'ピー！ピー！')

# 出力テスト
animal1 = Animal('動物', 10000)

dog1 = Dog('レオ', 15, 'プードル' )
#dog1.make_sound()

bird1 = Bird('ピジョン', 10, '雀')
#bird1.make_sound()

# (2)
def func_samp(arg1,arg2=0):
	print(f'arg1:{arg1} arg2:{arg2}')
	return arg1+arg2

print(func_samp(1))
print(func_samp(0,1))
print(func_samp(1,1))

dog2 = Dog('チョコ', 10, 'チワワ')
dog2.run()
dog2.run(speed = '速い')
dog2.run(speed = '遅い')
dog2.run(speed = '普通')
