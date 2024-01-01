import json
import os
from pathlib import Path

import frontmatter
import markdown
import pymongo
from dotenv import load_dotenv


def load_md_dir(md_dir: Path) -> list[Path]:
    """
    Load all markdown paths from a directory

    :param md_dir: path to directory containing markdown files
    :return: list of markdown file paths
    """
    return list(md_dir.glob("*.md"))


def parse_md_file(file_path: Path) -> frontmatter.Post:
    """
    Parse markdown file

    :param file_path: path to markdown file
    :return: parsed markdown file
    """
    return frontmatter.load(file_path)


def parse_metadata(file_content: frontmatter.Post) -> dict:
    """
    Parse metadata from markdown file

    :param file_content: markdown file as a string
    :return: metadata as a dictionary
    """
    return file_content.metadata


def convert_md_to_html(file_content: frontmatter.Post) -> str:
    """
    Convert markdown file to html

    :param file_content: markdown file as a string
    :return: html as a string
    """
    return markdown.markdown(file_content.content)


if __name__ == "__main__":
    load_dotenv()
    DEBUG: bool = True
    MD_DIR: str = "mocking"
    MONGO_URI: str = os.getenv("MONGO_URI")
    MONGO_DB: str = "aods"
    MONGO_COLLECTION: str = "challenges"

    mongo_client = pymongo.MongoClient(MONGO_URI)
    mongo_db = mongo_client[MONGO_DB]
    mongo_collection = mongo_db[MONGO_COLLECTION]

    path = Path(MD_DIR)
    md_files = load_md_dir(path)
    for md_file in md_files:
        md = parse_md_file(md_file)
        metadata = parse_metadata(md)
        html = convert_md_to_html(md)

        # debug: write to path/html
        if DEBUG:
            with open(
                os.path.join(path, "output", md_file.stem + ".html"), "w"
            ) as f:
                f.write(html)

            metadata["date"] = str(metadata["date"])
            with open(
                os.path.join(path, "output", md_file.stem + ".json"), "w"
            ) as f:
                json.dump(metadata, f)

        # insert into mongo
        mongo_collection.insert_one(
            {
                "title": metadata["title"],
                "author": metadata["author"],
                "tags": metadata["tags"],
                "date": metadata["date"],
                "content": html,
            }
        )
