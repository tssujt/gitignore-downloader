import argparse
import requests


def download_gitignore(language: str):
    url = f"https://raw.githubusercontent.com/github/gitignore/master/{language}.gitignore"
    try:
        response = requests.get(url)
        response.raise_for_status()

        filename = ".gitignore"
        with open(filename, "w") as file:
            file.write(response.text)

        print(
            f"Successfully downloaded .gitignore file for {language} language"
        )

    except requests.exceptions.HTTPError as e:
        print(
            f"Failed to download .gitignore file for {language} language: "
            f"{e.response.status_code} - {e.response.reason}"
        )


def main():
    parser = argparse.ArgumentParser(
        description="Download .gitignore file for a specified language."
    )
    parser.add_argument(
        "language", help="Specify the language for .gitignore file"
    )
    args = parser.parse_args()

    download_gitignore(args.language)
