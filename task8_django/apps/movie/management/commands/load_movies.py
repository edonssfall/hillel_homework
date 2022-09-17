import os.path
import time
from django.core.management.base import BaseCommand
from apps.movie.models import Movie
from art import tprint


class Command(BaseCommand):
    help = "Import Movies to DataBase"

    def add_arguments(self, parser):
        parser.add_argument("-f", "--file", type=str)

    def handle(self, *args, **options):
        print("(+)Processing...")
        start_time = time.time()
        attempts = 0
        file = options.get("file")
        if not os.path.exists(file):
            print("File not exists")
        with open(file, "r") as tsv_file:
            for line in tsv_file.readlines():
                if not line.startswith("tt"):
                    continue
                if not line:
                    continue
                data = line.split("\t")
                if data[1] not in ["short", "movie"]:
                    continue
                date = data[5]
                if date == "\\N":
                    date = None
                else:
                    date = f"{date}-01-01"
                adult = data[4]
                if adult == "0":
                    adult = False
                else:
                    adult = True
                data[8] = data[8][:-1]
                movie_data = {
                    'title_type': data[1],
                    'name': data[2],
                    'is_adult': adult,
                    'year': date,
                    'genres': data[8].split(",")
                }
                movie, created = Movie.objects.get_or_create(
                    imdb_id=data[0],
                    defaults=movie_data
                )
                if created:
                    Movie.objects.filter(id=movie.id).update(**movie_data)
                if attempts % (1 << 20) == 0:
                    print(f"Debug control: Attempts = {attempts} | Movie = {movie} | {time.time() - start_time}")
                attempts += 1
        tprint("Movies Import", "FINISH!!!", time.time()-start_time, sep='\n')
