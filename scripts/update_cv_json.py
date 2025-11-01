import os
import sys
import subprocess
from pathlib import Path
import time


def create_cv_json(input_file, config_file, repo_root, output_file):
    """
    Dummy placeholder for the actual conversion function.
    Replace this with the real 'create_cv_json' logic
    from cv_markdown_to_json.py if needed.
    """
    print(f"Simulating conversion from {input_file} to {output_file}")
    # 导入并调用 cv_markdown_to_json.py 文件
    from cv_markdown_to_json import create_cv_json

    create_cv_json(input_file, config_file, repo_root, output_file)


def main():
    """Automatically update CV JSON and optionally rebuild Jekyll site."""
    # 自动检测仓库根目录
    repo_root = Path(__file__).resolve().parent.parent
    print(f"📁 Repository root detected: {repo_root}")

    # 定义文件路径
    cv_markdown = repo_root / "_pages" / "cv.md"
    cv_json = repo_root / "_data" / "cv.json"
    config_file = repo_root / "_config.yml"

    # 检查文件存在性
    if not cv_markdown.exists():
        print(f"Error: Markdown CV not found at {cv_markdown}")
        input("Press Enter to exit...")
        sys.exit(1)
    if not config_file.exists():
        print(f"Error: Jekyll config file not found at {config_file}")
        input("Press Enter to exit...")
        sys.exit(1)

    # 执行转换
    print("🔄 Converting markdown CV to JSON...")
    try:
        create_cv_json(str(cv_markdown), str(config_file), str(repo_root), str(cv_json))
    except Exception as e:
        print(f"Error during conversion: {e}")
        input("Press Enter to exit...")
        sys.exit(1)

    # 成功信息
    print(f"\nSuccessfully updated CV JSON file at: {cv_json}")


if __name__ == "__main__":
    main()
