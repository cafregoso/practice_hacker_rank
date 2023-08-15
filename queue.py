class Queue:

    def __init__(self) -> None:
        self.__elements = []

    def get_quantity(self) -> int:
        return len(self.__elements)

    def enqueue(self, value: int):
        try:
            if isinstance(value, int):
                self.__elements.append(value)
        except:
            raise ValueError("Elements must be an int")

    def dequeue(self) -> int | str:
        if len(self.__elements) > 0:
            return self.__elements.pop(0)
        else:
            return "Queue is empty"

    def quantity(self) -> int:
        return len(self.__elements)

    def first_element(self) -> int | str:
        if len(self.__elements) > 0:
            return self.__elements[0]
        else:
            return "Queue is empty!"


if __name__ == '__main__':
    queue = Queue()
    num_op = int(input("Enter the number of operations: "))

    for i in range(num_op):
        option = int(input("Enter the option: "))

        if option < 1 or option > 3:
            raise ValueError("Num must be between 1 and 3")

        if option == 1:
            value = int(input("Enter the value: "))
            queue.enqueue(value)

        if option == 2:
            queue.dequeue()
        
        if option == 3:
            print(queue.first_element())
