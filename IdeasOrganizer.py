class IdeasOrganizer:
  def __init__(self, all, favorites, completed):
    self.all = all
    self.favorites = favorites
    self.completed = completed

  def get_all(self):  
    return self.all

  def get_favorites(self):
    return self.favorites

  def get_completed(self):
    return self.completed

  def search(self, word):
    matches = {}
    
    for idea in self.all:
      if word in idea:
        matches[idea] = self.all[idea]
      if word in self.all[idea]:
        matches[idea] = self.all[idea]
    return matches

  def add_idea(self, idea, tags):
    return

  def edit_idea(self, idea):
    return

  def delete_idea(self, idea):
    return