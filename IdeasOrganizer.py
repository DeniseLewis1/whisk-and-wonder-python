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
        print(f"1. {matches[idea]}")
      if word in self.all[idea]:
        matches[idea] = self.all[idea]
        print(f"2. {matches[idea]}")
    return matches

  def add_idea(self, idea, tags):
    self.all[idea] = list(tags.split(", "))
    print(self.all[idea])
    return f"{idea} has been added"

  def edit_idea(self, idea, tags):
    self.all[idea] = list(tags.split(", "))
    return f"{idea} has been updated"

  def delete_idea(self, idea):
    del self.all[idea]
    return f"{idea} has been deleted"