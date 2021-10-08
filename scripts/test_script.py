group_outputs = {
  "Testing log grouping": "This should be in a group.",
  "Second log group": "Hello, world!",
  "Incoming Message": "We require more vespene gas!"
}


print("Beginningr output.")

for group_name, group_message in group_outputs.items():
  print(f"::group::{group_name}")
  print(group_message)
  print("::endgroup::")

print("Finishing output.")

