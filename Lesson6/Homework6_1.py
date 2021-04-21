from time import sleep


class TrafficLight:
    __color=["Red", "Yellow", "Green"]
    #def __init__(self):
    #    self.__color=["Red", "Yellow", "Green"]

    def running(self):
        while True:
            print("\033[31m\033[4m{}\033[0m".format(self.__color[0]))
            # print(self.__color[0])
            sleep(7)
            print("\033[33m{}\033[0m".format(self.__color[1]))
            # print(self.__color[1])
            sleep(2)
            print("\033[32m{}\033[0m".format(self.__color[2]))
            # print(self.__color[2])
            sleep(10)
            print("\033[33m{}\033[0m".format(self.__color[1]))
            # print(self.__color[1])
            sleep(2)


a = TrafficLight()
a.running()
#print(a._TrafficLight__color)