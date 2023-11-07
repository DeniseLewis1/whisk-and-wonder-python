import json
from IdeasOrganizer import IdeasOrganizer

with open("all.json", "r") as all, open("favorites.json", "r") as favorites, open("completed.json", "r") as completed:
  all_ideas = json.load(all)
  favorite_ideas = json.load(favorites)
  completed_ideas = json.load(completed)
  organizer = IdeasOrganizer(all_ideas, favorite_ideas, completed_ideas)

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
    all_ideas = organizer.get_all()
    print("\nAll baking ideas: ")
    for idea in all_ideas:
      print(f"\n{idea}: {all_ideas[idea]}")

  # View favorite ideas
  elif user_command == "2":
    favorite_ideas = organizer.get_favorites()
    print("\nFavorite baking ideas: ")
    for idea in favorite_ideas:
      print(f"\n{idea}: {favorite_ideas[idea]}")
    
  # View completed ideas
  elif user_command == "3":
    completed_ideas = organizer.get_completed()
    print("\nCompleted baking ideas: ")
    for idea in completed_ideas:
      print(f"\n{idea}: {completed_ideas[idea]}")

  # Search ideas
  elif user_command == "4":
    user_input = input("\nEnter search term: ")
    matches = organizer.search(user_input)
    for idea in matches:
      print(f"\n{idea}: {matches[idea]}")

  # Add ideas
  elif user_command == "5":
    idea = input("Enter idea to add to list: ")
    tags = input("Enter tags associated with this idea: ")
    print(f"\n{organizer.add_idea(idea, tags)}")

  # Edit ideas
  elif user_command == "6":
    print("\nAll baking ideas: ")
    print(f"\n{organizer.get_all()}")
    user_input = input("Enter the number of the idea to edit: ")
    print(f"\n{organizer.edit_idea(user_input)}")

  # Delete ideas
  elif user_command == "7":
    print("\nAll baking ideas: ")
    print(f"\n{organizer.get_all()}")
    user_input = input("Enter the number of the idea to delete: ")
    print(f"\n{organizer.delete_idea(user_input)}")
  
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

# Save list of ideas in json files
#   All ideas, favorites, completed
#   Use a dictionary to store ideas
#     Key: idea ("")
#     Value: list of tags ([])
#   All ideas need to save the favorites and completed statuses