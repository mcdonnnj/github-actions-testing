import json
import sys

import yaml


def main():
    with open(sys.argv[1]) as in_file, open(sys.argv[2], "w") as out_file:
        data = yaml.safe_load(in_file)
        out_file.write(json.dumps(data, indent=2))


if __name__ == "__main__":
    main()
