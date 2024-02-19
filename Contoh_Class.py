# di python untuk membuat class menggunakan kata kunci --> class
# __init__() --> constructor, method yang akan dieksekusi pertama kali ketika object dibuat (sama seperti constructor)
# self --> mengakses properti atau method pada class tersebut (sama seperti thisdi java)

class ContohClass:
    def __init__(self, name):
        self.name = name
        
    def getName(self):
        return self.name
    
    def setName(self, value):
        self.name = value
        
    # membuat static method (diakses langsung dari class tanpa membuat object)
    @staticmethod
    def getNameWithStatic():
        cls = ContohClass("static data from static class")
        return cls.getName()
    
# cara membuat object
object1 = ContohClass("dira sanjaya")
print(object1.getName())
object1.setName("wardana")
print(object1.getName())

# mengakses static class (diakses secara langsung dengan class, tanpa membuat object)
print(ContohClass.getNameWithStatic())