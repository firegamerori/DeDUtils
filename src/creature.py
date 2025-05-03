from character import Character

class Creature(Character):
    
    actions : dict[str, str] = {}
    senses = 10
    challange = 1
    about = ''
    
    def __init__(self, str : int, des : int, con : int, int : int, cha : int, ac : int, speed : int):
        super().__init__(str, des, con, int, cha, ac, speed)
    
    def change_about(self, about : str):
        self.about = about
    
    def add_action(self, name : str, desc : str):
        self.actions[name] = desc
    
    def save_on_archive(self):
        #TODO implement
        pass
    
    def to_json(self):
        old = super().to_json()
        old['actions'] = self.actions
        old['senses'] = self.senses
        old['challange'] = self.challange
        old['about'] = self.about
        
        return old
        pass
    
    
    
    pass