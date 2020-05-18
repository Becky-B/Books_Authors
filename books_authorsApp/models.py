from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=30)
    genre = models.TextField()
    #authors_of = models.ManyToManyField(Books, related_name='books_of_author')
    year_published = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f'{self.title} was published {self.year_published}'


class Authors(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    books_by_author = models.ManyToManyField(Books, related_name ='authors_of')
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f'{self.first_name}{self.last_name}'
