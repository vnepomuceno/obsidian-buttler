import sys

import click
from dotenv import load_dotenv

from obsidian_buttler import get_logger
from obsidian_buttler.services.frontmatter import add_frontmatter_attribute


logger = get_logger(__name__)
load_dotenv()

@click.command()
@click.option("--page-path", help="Page path of attribute to add")
@click.option("--attribute", help="Name of frontmatter attribute")
@click.option("--value", help="Value of frontmatter attribute")
def add_frontmatter_attribute_command(page_path: str, attribute: str, value: str):
    logger.info(f"Received 'add_frontmatter' command with attributes page_path='{page_path}', key='{attribute}', value='{value}'")
    add_frontmatter_attribute(page_path, attribute, value)


if __name__ == "__main__":
    script_name = sys.argv[1]

    if script_name == "add_frontmatter":
        add_frontmatter_attribute(sys.argv[2], sys.argv[3], sys.argv[4])