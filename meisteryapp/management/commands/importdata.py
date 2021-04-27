from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.http import Http404
import csv


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("email")
        parser.add_argument("csv_file")

    def handle(self, *args, **options):
        email = options["email"]
        csv_file = options["csv_file"]

        try:
            user = get_object_or_404(get_user_model(), username=email)
        except Http404:
            user = get_user_model().objects.create_user(username=email)

        with open(csv_file) as f:
            header = ",".join(f.readline().split(",")[:-1]) + "\n"
            f.seek(0)
            reader = csv.DictReader(f)
            filtered_rows = filter(lambda row: row['user_email'] == email, reader)
            user.product_info = header + "\n".join([",".join(tuple(row.values())[:-1]) for row in filtered_rows])
            user.save()
