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
