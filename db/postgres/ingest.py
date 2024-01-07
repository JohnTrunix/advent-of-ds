import json
import os
from pathlib import Path

import frontmatter
import markdown
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.engine.base import Engine


def convert_md_to_html(file_content: frontmatter.Post) -> str:
    """
    Convert markdown file to html

    :param file_content: markdown file as a string
    :return: html as a string
    """
    extensions = ["tables", "pymdownx.superfences", "pymdownx.highlight"]
    md_renderer = markdown.Markdown(extensions=extensions)
    return md_renderer.convert(file_content.content)


def insert_into_postgres(metadata: dict, html: str) -> None:
    """
    Insert metadata and html into postgres

    :param metadata: metadata of the file as a dict
    :param html: rendered html content
    :return: none
    """
    with ENGINE.connect() as conn:
        stmt = text(
            """
            INSERT INTO challenges (day_id, title, tags, open_at, created_by, content) 
            VALUES (:day_id, :title, :tags, :open_at, :created_by, :content)
            ON CONFLICT (day_id) DO UPDATE SET
                title = :title,
                tags = :tags,
                open_at = :open_at,
                created_by = :created_by,
                content = :content
            """
        ).bindparams(
            day_id=metadata["day_id"],
            title=metadata["title"],
            tags=metadata["tags"],
            open_at=metadata["open_at"],
            created_by=metadata["created_by"],
            content=html,
        )
        conn.execute(stmt)
        conn.commit()
        conn.close()


def debug_render(md_file: Path, metadata: dict, html: str) -> None:
    """
    Debug md renderer and create output files in /output/*.html/json format

    :param md_file: Path to md file
    :param metadata: metadata of the file as a dict
    :param html: rendered html content
    :return: none
    """
    with open(os.path.join(path, "output", md_file.stem + ".html"), "w") as f:
        f.write(html)

    metadata["open_at"] = str(metadata["open_at"])
    with open(os.path.join(path, "output", md_file.stem + ".json"), "w") as f:
        json.dump(metadata, f)


if __name__ == "__main__":
    load_dotenv()
    DEBUG: bool = True
    MD_DIR: str = "mocking"

    POSTGRES_URL: str = os.getenv("POSTGRES_URL")  # type: ignore
    ENGINE: Engine = create_engine(POSTGRES_URL)

    path: Path = Path(MD_DIR)
    md_files: list[Path] = list(path.glob("*.md"))
    for md_file in md_files:
        md: frontmatter.Post = frontmatter.load(md_file)
        metadata: dict = md.metadata
        html: str = convert_md_to_html(md)

        if DEBUG:
            debug_render(md_file, metadata, html)
        insert_into_postgres(metadata, html)
