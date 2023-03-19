class A:
    def __init__(self):
        print("I am class A.")
    def ima(self):
        print("I am class A.")

class B(A):
    def im(self):
        super().im()
        print("I am class B.")

class C(B):
    def im(self):
        #super().im()
        print("I am class C.")

obj = C()
obj.im()