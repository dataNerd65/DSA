class mergeArray():
    @staticmethod
    def merge(nm1, m, nm2, n):
        #Setting pointers
        p1 = m - 1
        p2 = n - 1
        #pointer at also end of merged array
        p = m + n - 1

        #Iterating from end of both arrays to the start
        while p1 >= 0 and p2 >= 0:
            if nm1[p1] > nm2[p2]:
                nm1[p] = nm1[p1]
                p1 -= 1
            else:
                nm1[p] = nm2[p2]
                p2 -= 1
            p -= 1

        if p2 >= 0:
            nm1[:p2 + 1] = nm2[:p2 + 1]

#Test cases
nm1 = [34, 45, 90, 0, 0, 0]
m = 3
nm2 = [2, 5, 6]
n = 3
mergeArray.merge(nm1, m, nm2, n)
print(nm1)

# @staticmethod decorator
class Math:
    @staticmethod
    def square(n):
        return n * n
    
print(Math.square(5))

# @classmethod
class MyClass:
    class_attributes = "Initial value"

    @classmethod
    def modify_class_attribute(cls, new_value):
        cls.class_attribute = new_value

#Modify the class attribute using the class method
MyClass.modify_class_attribute("New Value")

#Print the modified class attribute
print(MyClass.class_attribute)


