#coding=utf-8


# 总会遇到需要通过metaclass修改类定义的。ORM就是一个典型的例子。 “Object Relational Mapping”
# 让我们来尝试编写一个ORM框架。


class Field(object):
	def __init__(self, name, column_type):
		self.name = name
		self.column_type = column_type

	def __str__(self):
		return "<%s:%s>" % (self.name, self.column_type)


class StringField(Field):
	def __init__(self, name):
		super(StringField, self).__init__(name, "varchar(100)")


class IntergerFiled(Field):
	def __init__(self, name):
		super(IntergerFiled, self).__init__(name, "bigint")


class ModelMetaClass(type):
	def __new__(cls, name, bases, attrs):
		print("attrs = %s" % attrs)
		if name=="Model":		# 排除掉对Model类的修改
			return type.__new__(cls, name, bases, attrs)
		print("Found model: %s" % name)
		mappings = dict()
		for k, v in attrs.items():
			if isinstance(v, Field):
				print("Found mapping: %s ==> %s" % (k, v))
				mappings[k] = v
		for k in mappings.keys():
			attrs.pop(k)
		attrs["__mappings__"] = mappings  # 保存属性和列的映射关系
		attrs["__table__"] = name  # 假设表名和类名一致
		return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaClass):
	def __init__(self, **kwargs):
		super(Model, self).__init__(**kwargs)

	def __getattr__(self, key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError(r"'Model' object has no attribute '%s'" % key)

	def __setattr__(self, key, value):
		self[key] = value

	def save(self):
		fields = []
		params = []
		args = []
		for k, v in self.__mappings__.items():
			fields.append(v.name)
			params.append("?")
			args.append(getattr(self, k, None))
		sql = "insert into %s (%s) values (%s)" % (self.__table__, ",".join(fields), ",".join(params))
		print("SQL: %s" % sql)
		print("ARGS: %s" % str(args))


"""
当用户定义一个class User(Model)时，Python解释器首先在当前类User的定义中查找metaclass，
如果没有找到，就继续在父类Model中查找metaclass，
找到了，就使用Model中定义的metaclass的ModelMetaclass来创建User类，
也就是说，metaclass可以隐式地继承到子类，但子类自己却感觉不到。
"""
class User(Model):
	id = IntergerFiled("id")
	name = StringField("username")
	email = StringField("email")
	password = StringField("password")

u = User(id=1234, name="alex", email="icevmj@gmail.com", password="12345")
u.save()