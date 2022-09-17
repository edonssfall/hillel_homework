import json
import time
from art import tprint
from django.core.management import BaseCommand
from apps.movie.models import PersonMovie, Person, Movie


class Command(BaseCommand):
    help = "Import Persons Movies"

    def add_arguments(self, parser):
        parser.add_argument('-f', '--file', type=str)

    def handle(self, *args, **options):
        start_time = time.time()
        print("(+)Processing...")
        attempts = 0
        file = options.get("file")
        with open(file, "r") as tsv_file:
            for line in tsv_file.readlines():
                if not line:
                    continue
                if not line.startswith('tt'):
                    continue
                person_movie = line.split('\t')
                movie = Movie.objects.filter(imdb_id=person_movie[0]).first()
                if not movie:
                    continue
                person = Person.objects.filter(imdb_id=person_movie[2]).first()
                if not person:
                    continue
                job = person_movie[4]
                if job == "\\N":
                    job = None
                characters = person_movie[5]
                if characters.startswith("\\N"):
                    characters = None
                else:
                    characters = json.loads(characters)
                data = {
                    'order': int(person_movie[1]),
                    'category': person_movie[3],
                    'job': job,
                    'characters': characters
                }
                print(data)
                pm, created = PersonMovie.objects.get_or_create(
                    movie=movie,
                    person=person,
                    defaults=data
                )
                if created:
                    PersonMovie.objects.filter(id=pm.id).update(**data)
                if attempts % (1 << 20) == 0:
                    print(f"Debug control: Attempts = {attempts} | PersonMovies = {pm} | {time.time() - start_time}")
                attempts += 1
        tprint("Movies Import", "FINISH!!!", time.time()-start_time, sep='\n')

