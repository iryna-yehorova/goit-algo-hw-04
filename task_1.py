import shutil
import sys
from pathlib import Path


def copy_files(folder, destination):
    try:
        for item in folder.iterdir():
            try:
                if item.resolve() == destination:
                    continue

                if item.is_dir():
                    copy_files(item, destination)
                elif item.is_file():
                    extension = item.suffix[1:].lower()
                    if not extension:
                        extension = "no_extension"

                    new_folder = destination / extension
                    new_folder.mkdir(parents=True, exist_ok=True)
                    new_file = new_folder / item.name
                    number = 1
                    while new_file.exists():
                        new_file = new_folder / f"{item.stem}_{number}{item.suffix}"
                        number += 1

                    shutil.copy2(item, new_file)
            except OSError as error:
                print(f"Error processing {item}: {error}")
    except OSError as error:
        print(f"Could not open folder {folder}: {error}")


if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: python3 task_1.py source [destination]")
        sys.exit(1)

    source = Path(sys.argv[1]).resolve()
    if len(sys.argv) == 3:
        destination = Path(sys.argv[2]).resolve()
    else:
        destination = Path("dist").resolve()

    if not source.is_dir():
        print("Source folder does not exist")
        sys.exit(1)
    if source == destination:
        print("Source and destination folders must be different")
        sys.exit(1)

    copy_files(source, destination)
