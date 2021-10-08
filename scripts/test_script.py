import logging
import sys

logging.basicConfig(
    format="%(asctime)-15s %(levelname)s %(message)s",
    level=logging.INFO,
    stream=sys.stdout,
)

group_outputs = {
    "Testing log grouping": "This should be in a group.",
    "Second log group": "Hello, world!",
    "Incoming Message": "We require more vespene gas!",
    "mcdonnnj/best-repo-ever": "Simply the best. Better than all the rest.",
}


print("Beginningr output.")

for group_name, group_message in group_outputs.items():
    print(f"::group::{group_name}")
    print(group_message)
    print("::endgroup::")

logging.info("::group::Logging test")
logging.info("Hello, world!")
logging.info("::endgroup::")

print("::group::Logging test #2")
logging.info("Hello, again!")
print("::endgroup::")

print("Finishing output.")
