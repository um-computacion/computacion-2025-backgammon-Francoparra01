class Tablero:
    def __init__(self):
        # 24 agujas sin fichas
        self.__agujas__ = [("ninguno", 0) for _ in range(24)]
        self.__barra__ = {"blanco": 0, "negro": 0}
        self.__retirada__ = {"blanco": 0, "negro": 0}

        # tablero inicial
        self.__agujas__[0] = ("blanco", 2)   
        self.__agujas__[11] = ("blanco", 5)
        self.__agujas__[16] = ("blanco", 3)
        self.__agujas__[18] = ("blanco", 5)

        self.__agujas__[23] = ("negro", 2)   
        self.__agujas__[12] = ("negro", 5)
        self.__agujas__[7] = ("negro", 3)
        self.__agujas__[5] = ("negro", 5)

    def estado_aguja(self, idx: int):
        return self.__agujas__[idx]
    
    def fichas_retiradas(self, color: str) -> int:
    return self.__retirada__[color]
    
    def fichas_en_barra(self, color: str) -> int:
    return self.__barra__[color]

    

    

    
   

    
    
    
    

