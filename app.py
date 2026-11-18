import argparse
import json
from pathlib import Path


def unique_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"Duplicate key: {key}")
        result[key] = value
    return result


def main():
    parser = argparse.ArgumentParser(description="Format a UTF-8 JSON file to standard output.")
    parser.add_argument("file", type=Path)
    args = parser.parse_args()
    try:
        value = json.loads(args.file.read_text(encoding="utf-8"), object_pairs_hook=unique_keys)
        print(json.dumps(value, ensure_ascii=False, allow_nan=False, indent=2))
    except (OSError, ValueError) as error:
        parser.exit(1, f"{error}\n")


if __name__ == "__main__":
    main()
