# クリニックの予約表示システム
# https://obgynai.com/object-orientation-exercises/
# 振る舞い
# (1) 病院側が患者へ診察の待ち人数を表示
# (2) 患者の予約処理をする
# (3) 患者の診察処理をする
# (4) 患者の診察予約がすでにされているか確認する

class Human():
	def __init__(self, name):
		self.name = name

class Patient(Human):
	def __init__(self, name, patient_id, symptom):
		super().__init__(name)
		self.symptom = symptom
		self.patient_id =patient_id

class Clinic():
	def __init__(self, patient_list):
		self.patient_list = patient_list
	
	def show_waiting_count(self):
		# Patient Class()に格納されたリストの待ち人数を表示
		pass

	def reserve(self, name, symptom, patient_id):
		# Patient class
		patient_list.append(name, symptom, patient_id)
		# clinicクラスの中でpatientインスタンスを作成できるのか？
		# 作成できるとした

	def diagnosis(self):
		pass

	def _check_reserved(self):
		pass


# user1 = Patient('佐藤', 111, '咳')
# print(user1.name, user1.patient_id, user1.symptom)

myclinic = Clinic()

patients = [['佐藤', '111', '咳'],
	        ['田中', '222', '腹痛'],
	        ['鈴木', '333', '鼻水'],
            ['山田', '444', '倦怠感'],
            ['川邊', '555', 'コロナ']]

# patientsリストにに入っている5人の患者をPatientクラスからインスタンス化
# 診察予約
for p in patients:
	# １回目のループ（name= "1",age）
	name, patient_id, symptom = p
	patient = Patient(name, patient_id, symptom)
	myclinic.reserve(patient)


myclinic.show_waiting_count()
