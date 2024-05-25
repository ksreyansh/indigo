from django.db import models


# Create your models here.
class Country(models.Model):
    country_code = models.CharField(max_length=10, primary_key=True)
    country_name = models.CharField(max_length=50)

    def __str__(self):
        return self.country_name

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"


class State(models.Model):
    country_code = models.ForeignKey(Country, on_delete=models.CASCADE)
    state_code = models.CharField(max_length=10, primary_key=True)
    state_name = models.CharField(max_length=50)

    def __str__(self):
        return self.state_name

    class Meta:
        verbose_name = "State"
        verbose_name_plural = "States"


class City(models.Model):
    country_code = models.ForeignKey(Country, on_delete=models.CASCADE)
    state_code = models.ForeignKey(State, on_delete=models.CASCADE)
    city_code = models.CharField(max_length=10, primary_key=True)
    city_name = models.CharField(max_length=100)

    def __str__(self):
        return self.city_name

    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"


