import os.path
import random
import string
import sys
import subprocess
import argparse

NOTES_DIR = "D:\Python\Projects\_notes"


def generate_unique_id():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(4))


def write_note(subject):
    note_id = generate_unique_id()
    note_path = os.path.join(NOTES_DIR, f"{subject}_{note_id}")
    note_name = str(note_path) + ".txt"

    with open(note_name, 'w') as f:
        note_text = sys.stdin.read()
        f.write(note_text)
    print(subject + note_id + " saved")

def read_notes(substring):
    for note_file in os.listdir(NOTES_DIR):
        if substring in note_file:
            with open(os.path.join(NOTES_DIR, note_file), 'r') as f:
                print(f.read())

def remove_note(note_id):
    note_file = os.path.join(NOTES_DIR, f"{note_id}") + ".txt"
    os.remove(note_file)
    print("Deleted note " + note_id + " from file directory " + NOTES_DIR)


if __name__ == "__main__":

    # create the top-level parser
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(required=True)

    if sys.argv[1] == 'write':

        # Create Parser for Write command
        parser_write = subparsers.add_parser('write')
        parser_write.add_argument('subject', action="store", type=str)
        parser_write.set_defaults(func=write_note)
        args = parser.parse_args()
        args.func(args.subject)
        exit()

    elif sys.argv[1] == 'read':
        # Create Parser for Read command
        parser_read = subparsers.add_parser('read')
        parser_read.add_argument('substring', type=str)
        parser_read.set_defaults(func=read_notes)
        args = parser.parse_args()
        args.func(args.substring)

    elif sys.argv[1] == 'remove':
        # Create Parser for Remove command
        parser_remove = subparsers.add_parser('remove')
        parser_remove.add_argument('note_id', type=str)
        parser_remove.set_defaults(func=remove_note)
        args = parser.parse_args()
        args.func(args.note_id)