# 2_コンストラクタ
# （1）コンストラクタとはクラスからインスタンスを作ったタイミングで実行されるメソッド
# （2）インスタンスを作成するときは引数にプロパティの値を定義する。
# https://obgynai.com/object-orientation-1/
#Dogオブジェクト（class）
class Dog():
	# （1）
	def __init__(self, name, breed, weight):
	
	#Dogの属性（property）
		# ①名前
		self.name = name

		# ②犬種
		self.breed = breed

		# ③体重(kg)
		self.weight = weight


	#Dogの振る舞い(method)
	# 座る
	def sit(self):
		print(self.name, '座る')

	# 寝る
	def sleep(self):
		print(self.name, '寝る')

	# 食べる
	def eat(self):
		print(self.name, '食べる')


#Dogオブジェクトからdog1(レオ/プードル/15kg)を作成(instance)
# （2）
#dog1 = Dog(name='レオ', breed='プードル', weight=15)
dog1 = Dog('レオ', 'プードル', 15)
print(dog1.name, dog1.breed, dog1.weight)
dog1.sit()

#Dogオブジェクトからdog2(チョコ/チワワ/10kg)を作成(instance)
# （2）
dog2 = Dog(name='チョコ', breed='チワワ', weight=10)
print(dog2.name, dog2.breed, dog2.weight)
dog2.eat()

