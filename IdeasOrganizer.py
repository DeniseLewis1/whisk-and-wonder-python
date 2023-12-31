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
    self.all[idea] = list(tags.split(", "))
    return f"{idea} has been added"

  def edit_idea(self, idea, tags):
    self.all[idea] = list(tags.split(", "))
    return f"{idea} has been updated"

  def delete_idea(self, idea):
    del self.all[idea]
    return f"{idea} has been deleted"

  def add_favorite(self, idea):
    self.favorites[idea] = self.all[idea]
    return f"{idea} has been added to favorites"

  def remove_favorite(self, idea):
    del self.favorites[idea]
    return f"{idea} has been removed from favorites"

  def add_completed(self, idea):
    self.completed[idea] = self.all[idea]
    return f"{idea} has been added to completed"
  
  def remove_completed(self, idea):
    del self.completed[idea]
    return f"{idea} has been removed from completed"