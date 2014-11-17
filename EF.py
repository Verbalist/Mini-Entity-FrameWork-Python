import postgresql

#конект к дб
db = postgresql.open(user = 'postgres', host = 'localhost', port = 5432, password='1111', database='course')

#пустой метаклас
class EntityBase(object): pass

#наследник мета класа с расширением его поведения
class Entity(EntityBase):
	def __init__(self, ATTRIBUTES, args):
		[self.__setattr__(k, v) for (k,v) in zip(ATTRIBUTES, args)] 
	#show, read вывод в консоль
	def read(self):
		print('\n'.join([k + " : " + str(self.__dict__[k]) for k in self.__dict__]))
	#update принимает на вход словарь
	def update(self, dct):
		[self.__setattr__(k, dct[k]) for k in dct]

#функция для запроса с последуюшим возвращением листа класов
def query(sqlQuery):
	f = db.prepare(sqlQuery)
	ATTRIBUTES = f.column_names
	EntityBase = type('EntityBase', (), {}.fromkeys(ATTRIBUTES)) 
	ret = []
	
	for row in f:
		ret.append(Entity(ATTRIBUTES, row))
	
	return ret;
