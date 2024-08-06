from django.db import models

class Artist(models.Model):
	name = models.CharField(max_length=30, null=False)
	country = models.CharField(max_length=30, null=False)

	def __str__(self) -> str:
		return f'{self.name}'

class Album(models.Model):
	name =  models.CharField(max_length=30, null=False)
	
	GENRES = {
        ('R', 'Rock'),
        ('E', 'Electronica'),
        ('H', 'Hip-Hop'),
        ('C','Clasica'),
        ('B','Bossa Nova'),

            }
	genre = models.CharField(max_length=30, choices=GENRES, null=False)
	artist = models.ForeignKey(Artist, on_delete=models.CASCADE, default=1)
	year = models.IntegerField(null=False, default = 2000)
	picture = models.ImageField(upload_to='pokemons_images')

	def __str__(self) -> str:
		return self.name
