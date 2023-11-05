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
    print("\nAll baking ideas: ")
    print(f"\n{organizer.get_all()}")

  # View favorite ideas
  elif user_command == "2":
    print("\nFavorite baking ideas: ")
    print(f"\n{organizer.get_favorites()}")
    
  # View completed ideas
  elif user_command == "3":
    print("\nCompleted baking ideas: ")
    print(f"\n{organizer.get_completed()}")

  # Search ideas
  elif user_command == "4":
    user_input = input("Enter search term: ")
    print(f"\n{organizer.search(user_input)}")

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


# Save list of ideas in json files
#   All ideas, favorites, completed
#   Use a dictionary to store ideas
#     Key: idea ("")
#     Value: list of tags ([])
#   All ideas need to save the favorites and completed statuses