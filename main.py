import json
from IdeasOrganizer import IdeasOrganizer

with open("all.json", "r") as all, open("favorites.json", "r") as favorites, open("completed.json", "r") as completed:
  all_ideas = json.load(all)
  favorite_ideas = json.load(favorites)
  completed_ideas = json.load(completed)
  organizer = IdeasOrganizer(all_ideas, favorite_ideas, completed_ideas)

all_ideas = organizer.get_all()
favorite_ideas = organizer.get_favorites()
completed_ideas = organizer.get_completed()

def print_ideas(idea_list):
  for idea in idea_list:
    print(f"\n  {idea}: {idea_list[idea]}")

done = False

while not done:
  user_command = input(
      """
How can I help you?

  1: View all ideas
  2: View favorite ideas
  3: View completed ideas
  4: Search ideas
  5: Add ideas
  6: Edit ideas
  7: Delete ideas

  Select a number or type 'Exit' to quit: 

  """
  )

  # View all ideas
  if user_command == "1":
    print("\nAll baking ideas: ")
    print_ideas(all_ideas)

  # View favorite ideas
  elif user_command == "2":
    print("\nFavorite baking ideas: ")
    print_ideas(favorite_ideas)
    
  # View completed ideas
  elif user_command == "3":
    print("\nCompleted baking ideas: ")
    print_ideas(completed_ideas)

  # Search ideas
  elif user_command == "4":
    user_input = input("\nEnter search term: ")
    matches = organizer.search(user_input)
    if not matches:
      print(f"\nNo matches found for '{user_input}'")
    print_ideas(matches)

  # Add ideas
  elif user_command == "5":
    idea = input("\nEnter an idea to add to the list: ")
    if idea in all_ideas:
      print("\nThis idea already exists in the list.")
    else:
      tags = input("\nEnter tags associated with this idea (separate tags with a comma): ")
      print(f"\n{organizer.add_idea(idea, tags)}")

  # Edit ideas
  elif user_command == "6":
    print("\nAll baking ideas: ")
    print_ideas(all_ideas)
    idea = input("\nEnter the idea to edit: ")
    if idea not in all_ideas:
      print("\nThis idea does not exist in the list.")
    else:
      print(f"\n{idea}: {all_ideas[idea]}")
      tags = input("\nEnter tags associated with this idea (separate tags with a comma): ")
      print(f"\n{organizer.edit_idea(idea, tags)}")

  # Delete ideas
  elif user_command == "7":
    print("\nAll baking ideas: ")
    print_ideas(all_ideas)
    idea = input("\nEnter the idea to delete: ")
    if idea not in all_ideas:
      print("\nThis idea does not exist in the list.")
    else:
      print(f"\n{organizer.delete_idea(idea)}")
  
  # Exit
  elif user_command == "exit" or user_command == "Exit" or user_command == "EXIT":
    done = True
    print("\nGoodbye, see you soon!")
  else:
    print("\nNot a valid command.")

with open("all.json", "w") as write_all, open("favorites.json", "w") as write_favorites, open("completed.json", "w") as write_completed:
      json.dump(organizer.get_all(), write_all)
      json.dump(organizer.get_favorites(), write_favorites)
      json.dump(organizer.get_completed(), write_completed)