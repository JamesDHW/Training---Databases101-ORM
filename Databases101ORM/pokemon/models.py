# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models


class ShardedModel(models.Model):
    shard_id = models.CharField(max_length=50, default="server_1")

    class Meta:
        # Be wary - do you want a real database relation or a Python class parent-child relation?
        abstract = True


class PokemonTrainers(ShardedModel):
    trainer_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class PokemonTypes(ShardedModel):
    type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class PokemonSpecies(ShardedModel):
    species_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)
    evolves_to = models.ForeignKey("self", blank=True, null=True)
    types = models.ManyToManyField(PokemonTypes, blank=True)

    def __str__(self):
        return self.name


class Pokemon(ShardedModel):
    pokemon_id = models.AutoField(primary_key=True)
    species = models.ForeignKey(PokemonSpecies)
    health_points = models.IntegerField()
    level = models.IntegerField()
    nickname = models.CharField(max_length=50, blank=True, null=True)
    trainer = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.species} {self.nickname} {self.trainer}"