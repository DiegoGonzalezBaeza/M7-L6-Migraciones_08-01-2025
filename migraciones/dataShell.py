import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'migraciones.settings')
django.setup()

from modelos.models import Author, Book
from datetime import date

def poblar_datos():
    author1 = Author.objects.create(first_name="Jane", last_name="Austen", birth_date=date(1780, 6, 8), email="jane.austen@example.com")
    author2 = Author.objects.create(first_name="George", last_name="Orwell", birth_date=date(1866, 12, 12), email="george.orwell@example.com")

    Book.objects.create(title="Pride and Prejudice", published_date=date(1813, 1, 28), author=author1)
    Book.objects.create(title="1984", published_date=date(1949, 6, 8), author=author2)
    Book.objects.create(title="Emma", published_date=date(1815, 12, 23), author=author1)

    print("Datos iniciales cargados con éxito.")

if __name__ == "__main__":
    poblar_datos()