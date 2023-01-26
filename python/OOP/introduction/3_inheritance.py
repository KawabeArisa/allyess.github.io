# 3_継承
# https://obgynai.com/%e3%80%90object-orientation-2/
# Animal（親クラス） →   Dog（子クラス）,Bird（子クラス）
#                 【継承】

# Animal(親クラス)
class Animal():
	def __init__(self, name, weight):
		self.name = name
		self.weight = weight

	def sleep(self):
		print(self.name, '寝る')

	def eat(self):
		print(self.name, '食べる')


# Dog（子クラス）
class Dog(Animal):
	def __init__(self, name, weight, breed):
		#Animalクラスのコンストラクタを追加
		super().__init__(name, weight)
		self.breed = breed

	def run(self):
		print(self.name, '走る')

 

# Bird（子クラス）
class Bird(Animal):
	def __init__(self, name, weight, types):
		super().__init__(name, weight)
		self.types = types

	def fly(self):
		print(self.name, '飛ぶ')

# 出力テスト
animal1 = Animal('動物', 10000)
print(animal1.name, animal1.weight)
animal1.sleep()
animal1.eat()

dog1 = Dog('レオ', 15, 'プードル' )
print(dog1.name, dog1.weight, dog1.breed)
dog1.run()
dog1.fly()

bird1 = Bird('ピジョン', 10, '雀')
print(bird1.name, bird1.weight, bird1.types)
bird1.fly()
