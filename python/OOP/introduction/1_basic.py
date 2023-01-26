# 1_基礎
# オブジェクト：犬
# 属性：名前/犬種/体重（各犬ごとに値を定義する）
# 振る舞い：座る/寝る/食べる（各犬が共通で使えるもの）
# selfとはインスタンス実体「そのもの」
#         インスタンスで定義したdog1であるレオちゃんにとってselfはdog1を意味する。

# https://obgynai.com/object-orientation-1/
#Dogオブジェクト（class）
class Dog():

	#Dogの属性（property）
	# ①名前
	name = ""

	# ②犬種
	breed = ""

	# ③体重(kg)
	weight = 0


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
dog1 = Dog()
dog1.name = "レオ"
dog1.breed = "プードル"
dog1.weight = 15

print(dog1.name, dog1.breed, dog1.weight)
dog1.sit()

#Dogオブジェクトからdog2(チョコ/チワワ/10kg)を作成(instance)
dog2 = Dog()
dog2.name = "チョコ"
dog2.breed = "チワワ"
dog2.weight = 10

print(dog2.name, dog2.breed, dog2.weight)
dog2.eat()

print(id(dog1))
print(id(dog2))
print(hash(dog1))
print(hash(dog2))
