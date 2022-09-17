import time
from art import tprint
from django.core.management import BaseCommand
from apps.movie.models import Person


class Command(BaseCommand):
    help = "Import Person from tsv"

    def add_arguments(self, parser):
        parser.add_argument("-f", "--file", type=str)

    def handle(self, *args, **options):
        start_time = time.time()
        print("(+)Processing...")
        attempts = 0
        file = options.get("file")
        with open(file, "r") as tsv_file:
            for line in tsv_file.readlines():
                if not line:
                    continue
                if not line.startswith("nm"):
                    continue
                data = line.split("\t")
                date_birth = data[2]
                if date_birth == "\\N":
                    date_birth = None
                else:
                    date_birth = f"{date_birth}-01-01"
                date_death = data[3]
                if date_death == "\\N":
                    date_death = None
                else:
                    date_death = f"{date_death}-01-01"
                person_data = {
                    'name': data[1],
                    'birth_year': date_birth,
                    'death_year': date_death
                }
                person, created = Person.objects.get_or_create(
                    imdb_id=data[0],
                    defaults=person_data
                )
                if created:
                    Person.objects.filter(id=person.id).update(**person_data)
                if attempts % (1 << 20) == 0:
                    print(f"Debug control: Attempts = {attempts} | Person = {person} | {time.time() - start_time}")
                attempts += 1
        tprint("Movies Import", "FINISH!!!", time.time() - start_time, sep='\n')
