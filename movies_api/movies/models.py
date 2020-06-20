from django.db import models


class Movies(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1024)
    poster_path = models.CharField(null=True, max_length=100)
    ranking = models.PositiveSmallIntegerField(default=0)
    director = models.CharField(null=True, max_length=100)
    trailer = models.URLField(null=True)
    tmdb_id = models.PositiveSmallIntegerField(default=0)
    # writers
    # actors/stars

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # add the complete route to the poster field
        if not self.pk:
            tmdb_path = 'https://image.tmdb.org/t/p/w500'
            self.poster_path = tmdb_path + self.poster_path
        super().save(*args, **kwargs)
