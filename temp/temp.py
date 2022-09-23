class CLASSDB:
    def __init__(self):
        print("__init__")

    def __enter__(self):
        print("__enter__")
        return self

    def __del__(self):
        print("__del__")


db_class = CLASSDB()
print(db_class)
