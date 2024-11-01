import os
import yaml

from obsidian_buttler import get_logger
from obsidian_buttler.utils.files import find_files_by_extension

logger = get_logger(__name__)


def add_frontmatter_attribute(page_path: str, attribute: str, value: str):
    vault_base_path = os.environ.get("OBSIDIAN_BASE_PATH")
    logger.info(f"Working on vault '{vault_base_path}'")
    files = find_files_by_extension(vault_base_path + page_path, '.md')
    logger.info(f"Found {len(files)} files under directory '{page_path}'")

    for file_path in files:
        with open(file_path, 'r') as file:
            lines_content = file.read().split('\n')
            # Process the content of each page here
            logger.info(f"Processing {file_path}")
            add_frontmatter_key(lines_content, attribute, value)



def add_frontmatter_key(lines_content, key, value):
    # Check if the file has frontmatter
    if lines_content[0].strip() == "---":
        # Collect frontmatter lines
        frontmatter = []
        content = []
        in_frontmatter = True
        for line in lines_content[1:]:
            if line.strip() == "---" and in_frontmatter:
                in_frontmatter = False
                continue
            if in_frontmatter:
                frontmatter.append(line)
            else:
                content.append(line)

        # Parse, update, and re-serialize frontmatter
        try:
            frontmatter_dict = yaml.safe_load("".join(frontmatter)) or {}
            frontmatter_dict[key] = value  # Add new key-value pair
            new_frontmatter = "---\n" + yaml.dump(frontmatter_dict) + "---\n"
        except yaml.scanner.ScannerError:
            pass
            #raise ValueError("Formatting issue in file.")

        # Rewrite the file with updated frontmatter and content
        # with open(file_path, 'w') as file:
        #     file.write(new_frontmatter)
        #     file.writelines(content)
    else:
        raise ValueError("No frontmatter found in the file.")