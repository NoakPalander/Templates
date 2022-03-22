#!venv/bin/python3

import json
import os
import uuid
import shutil
from git import Repo
import argparse


def main():
    parser = argparse.ArgumentParser(description='Downloads a language template given a configuration.')
    parser.add_argument('-c', '--config', help='The configuration path.', type=str,
                        default=os.path.expanduser('~/.config/templates/config.json'))

    parser.add_argument('-d', '--dir', help='Where you want to download the template to.', type=str,
                        default=os.getcwd())

    parser.add_argument('-l', '--language', help='The language template you want to download.',
                        type=str, required=True)

    args = parser.parse_args()

    with open(args.config) as reader:
        config = json.load(reader)

    template = config[args.language.lower()]
    if args.dir == os.getcwd():
        temp = f'.temp-{uuid.uuid1()}'
        os.mkdir(temp)
        Repo.clone_from(template['git'], to_path=temp, branch=template['branch'])

        for file in os.listdir(temp):
            shutil.move(os.path.join(temp, file), os.getcwd())

        os.rmdir(temp)

    else:
        Repo.clone_from(template['git'], to_path=args.dir, branch=template['branch'])


if __name__ == '__main__':
    main()
