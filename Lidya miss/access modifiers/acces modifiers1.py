# super class
class A:
    # public data member
    var1=None

    # protected data member
    _var2=None

    # private data member
    __var3=None

    # constructor
    def __init__(self,var1,var2,var3):
        self.var1 = var1
        self._var2 = var2
        self.__var3 = var3

    # public member functions
    def displayPublicMembers(self):
        # accessing public data members
        print("Public Data Member: ",self.var1)

    # protected member functions
    def _displayProtectedMembers(self):
        # accesing protected data members
        print("Protected Data Member: ",self._var2)

    # private member function
    def __displayPrivateMembers(self):
        # accesing private data members
        print("Private Data Member: ",self.__var3)

    # public member function
    def accessPrivateMembers(self):
        # accesing private member function
        self.__displayPrivateMembers()

# derived class
class B(A):

    #constructor
    def __init__(self,var1,var2,var3):
        A.__init__(self,var1,var2,var3)

    # public member function
    def accessProtectedMembers(self):
        #accesing protected member functions of super class
        self._displayProtectedMembers()


# creating objects of the derived class
obj=B("Pub_Red", "Pro_White","Private_Green")

# calling public member functions of the class
obj.displayPublicMembers()
obj.accessProtectedMembers()
obj.accessPrivateMembers()
# obj.accessPrivateMembers()
# Object can access Public member
print("Object is accesing Private member: ",obj.var1)
# Object can access protected member
print("Object is accesing protected member: ",obj._var2)

# object can not access privare member, so it will generate Attribute error
# print(obj.__var3)
print(obj._A__var3) #Accesing Name Mangled variables
# name mangling
# a process in which any  identifier with one trailing undetscore and two leading underscores is
# textually replaced with the _ClassName__Identifier is known as name mangling
# In _ClassName__Identifier name, ClassName is the name of current class where identifier is present