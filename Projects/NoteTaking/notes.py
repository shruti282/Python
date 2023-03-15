import os.path
import random
import string
import sys

NOTES_DIR = "D:/Python/Projects/Notes"


def generate_unique_id():
    return ''.join(random.choice(string.ascii_uppercase + string.digits))


def write_note(subject):
    note_id = generate_unique_id()
    note_path = os.path.join(NOTES_DIR, f"{subject}_{note_id}")
    with open(note_path, 'w') as f:
        note_text = sys.stdin.read()
        f.write(note_text)
    print(note_id)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Note Taking System")
    subparser = parser.add_subparsers()

    parser_write = subparser.add_parser('write', help='Create a new Note')
    parser_write.add_argument('subject', type=str, help='Subject of the note')
    parser_write.set_defaults(func=write_note)

    # parser_read = subparser.add_parser('read', help='Read notes with given subject substring')
    # parser_read.add_argument('substring', type=str, help='Read notes with a given subject substring')
    # parser_read.set_defaults(func=read_note)

    args = parser.parse_args()
    args.func(args)
