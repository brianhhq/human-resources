from argparse import Action, ArgumentParser

def create_parser():
    parser = ArgumentParser(description="""
    Create User via inventory json file
    """)
    parser.add_argument("inventory_file", help="Inventory Json file to create users")
    parser.add_argument("--export",
            action='store_true',
            help="Whether is to export"
            )
    return parser

def main():
    from hr import hr
    args = create_parser().parse_args()

    if args.export:
        pass
    else:
        users = hr.parse_inventory_file(args.inventory_file)
        hr.create_user(users[0])
