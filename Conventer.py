class Conventer:
    @staticmethod
    def do(x: float) -> int:
        if x == 0.0:
            raise ValueError("Not null")
        elif x>=100.7:
            return 1000
        elif x>0:
            return int(x)
        elif x<0.0 and x>=-30.4:
            return (int(x)-5)
        else:
            return -2000