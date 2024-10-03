import inspect

def introspection_info(obj):
    # Получение типа объекта
    obj_type = type(obj).__name__

    # Получение модуля, к которому принадлежит объект
    obj_module = obj.__module__ if hasattr(obj, '__module__') else None

    # Список всех атрибутов и методов объекта
    attributes = []
    methods = []

    # Проход по всем атрибутам объекта, используя dir()
    for attribute_name in dir(obj):
        attribute = getattr(obj, attribute_name)
        # Проверка, является ли атрибут методом или функцией
        if inspect.ismethod(attribute) or inspect.isfunction(attribute):
            methods.append(attribute_name)
        else:
            attributes.append(attribute_name)

    # Формирование словаря с информацией об объекте
    obj_info = {
        "type": obj_type,           # Тип объекта
        "module": obj_module,       # Модуль объекта
        "attributes": attributes,   # Атрибуты объекта
        "methods": methods          # Методы объекта
    }

    return obj_info

# Пример использования с целочисленным типом
number_info = introspection_info(42)
print("Информация о числе 42:")
print(number_info)

# Пример использования с пользовательским классом
class MyClass:
    def __init__(self, value):
        self.value = value

    def my_method(self):
        return self.value

    def another_method(self):
        print("Hello, World!")

# Создаем объект класса MyClass
my_object = MyClass(100)

# Получение информации об объекте
object_info = introspection_info(my_object)
print("\nИнформация об объекте my_object:")
print(object_info)