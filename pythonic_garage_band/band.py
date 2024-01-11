class Band():
    
    """_summary_
    A class to represent a band.

    Attributes:
    
    instances (list): A class variable that tracks all instances of Band.
    name (str): The name of the band.
    members (list): A list of Musician instances that are members of the band.

    Methods:
    
    play_solos(): Returns a list of solos played by the band members.
    to_list(): Class method that returns the list of Band instances.
    """
    
    instances = []
    
    def __init__(self, name, members):
        self.name = name
        self.members = members
        Band.instances.append(self)
        
    def play_solos(self):
        return [member.play_solo() for member in self.members]
    
    @classmethod
    def to_list(cls):
        return cls.instances

class Musician():
    
    """_summary_
    A base class to represent a musician.

    Attributes:
    
    name (str): The name of the musician.

    Methods:
    
    __str__(): Returns a string representation of the musician.
    __repr__(): Returns an official string representation of the musician.
    get_instrument(): Abstract method, should be implemented by subclasses.
    play_solo(): Abstract method, should be implemented by subclasses.
    """
    
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f"My name is {self.name} and I play"

    def __repr__(self):
        return f"Musician('{self.name}')"
    
    def get_instrument(self):
        raise NotImplementedError("Hecks no")
    
    def play_solo(self):
        raise NotImplementedError("Hecks no")
    
class Guitarist(Musician):
    
    """_summary_
    A class to represent a guitarist, inheriting from the Musician class.

    Methods:
    
    get_instrument(): Returns 'guitar' indicating the instrument of the musician.
    play_solo(): Returns a string representing the solo played by the guitarist.
    """
    
    def __init__(self, name):
        super().__init__(name)
    
    def get_instrument(self):
        return "guitar"
    
    def __str__(self):
        instrument = self.get_instrument()
        return f"My name is {self.name} and I play {instrument}"
    
    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"
    
    def play_solo(self):
        return "face melting guitar solo"
    
    
class Bassist(Musician):
    
    """_summary_
    A class to represent a bassist, inheriting from the Musician class.

    Methods:
    
    get_instrument(): Returns 'bass' indicating the instrument of the musician.
    play_solo(): Returns a string representing the solo played by the bassist.
    """
    
    def __init__(self, name):
        super().__init__(name)
    
    def get_instrument(self):
        return "bass"
    
    def __str__(self):
        instrument = self.get_instrument()
        return f"My name is {self.name} and I play {instrument}"
    
    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"
    
    def play_solo(self):
        return "bom bom buh bom"

class Drummer(Musician):
    
    """_summary_
    
     A class to represent a drummer, inheriting from the Musician class.

    Methods:
    
    get_instrument(): Returns 'drums' indicating the instrument of the musician.
    play_solo(): Returns a string representing the solo played by the drummer.
    """
    
    def __init__(self, name):
        super().__init__(name)
    
    def get_instrument(self):
        return "drums"
    
    def __str__(self):
        instrument = self.get_instrument()
        return f"My name is {self.name} and I play {instrument}"
    
    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"
    
    def play_solo(self):
        return "rattle boom crash"

