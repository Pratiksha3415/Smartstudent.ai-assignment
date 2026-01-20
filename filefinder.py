import os
import argparse

def search_files(directory, filename=None, extension=None):
    results = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            if filename and filename.lower() in file.lower():
                results.append(os.path.join(root, file))
            elif extension and file.lower().endswith(extension.lower()):
                results.append(os.path.join(root, file))

    return results


def main():
    parser = argparse.ArgumentParser(description="File Search Utility")
    parser.add_argument("directory", help="Directory path to search")
    parser.add_argument("--name", help="File name to search")
    parser.add_argument("--ext", help="File extension to search (e.g. .txt, .pdf)")

    args = parser.parse_args()

    if not args.name and not args.ext:
        print("Please provide either --name or --ext option")
        return

    files = search_files(args.directory, args.name, args.ext)

    if files:
        print("\nFiles Found:\n")
        for file in files:
            print(file)
    else:
        print("No matching files found.")


if __name__ == "__main__":
    main()
