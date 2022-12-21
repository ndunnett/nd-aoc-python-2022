from urllib.request import Request, urlopen
import os


def download_file(url):
    request = Request(url=url, headers={"Cookie": f"session={os.environ['AOC_SESSION']}"})

    with urlopen(request) as response:
        return response.read().decode("utf-8")


def load_input(day):
    cache_folder = ".cache"
    file_name = f"input-day-{day:02}.txt"
    file_path = "/".join([cache_folder, file_name])

    if not os.path.isdir(cache_folder):
        os.mkdir(cache_folder)

    if not os.path.exists(file_path):
        url = f"https://adventofcode.com/2022/day/{day}/input"

        with open(file_path, encoding="utf-8", mode="w") as file:
            downloaded = download_file(url)
            file.write(downloaded)
            return downloaded.splitlines()

    with open(file_path, encoding="utf-8", mode="r") as file:
        return file.read().splitlines()
