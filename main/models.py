from django.db import models

# Create your models here.

# Cereal Name,Manufacturer,Type,Calories,Protein (g),Fat,Sodium,Dietary Fiber,
# Carbs,Sugars,Display Shelf,Potassium,Vitamins and Minerals,Serving Size Weight,
# Cups per Serving

class Manufacturer(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return "%s" % self.name


class Cereal(models.Model):

    name = models.CharField(max_length=30, unique=True)
    manufacturer = models.ForeignKey('main.Manufacturer', null=True) #One To Many Relationship with the Manufacturer
    type = models.CharField(max_length=30, null=True)
    display_shelf = models.FloatField(null=True)
   
    

    def __unicode__(self):
        return "%s" % self.name

class Nutritional_Information(models.Model):

    cereal = models.OneToOneField('main.Cereal', null=False)
    calories = models.FloatField(null=True)
    protien_in_g = models.FloatField(null=True)
    fat = models.FloatField(null=True)
    sodium = models.FloatField(null=True)
    dietary_fiber = models.FloatField(null=True)
    carbs = models.FloatField(null=True)
    sugars = models.FloatField(null=True)
    potassium = models.FloatField(null=True)
    vitamins_and_minerals = models.FloatField(null=True)
    serving_size_weight = models.FloatField(null=True)
    cups_per_serving = models.FloatField(null=True)

    def __unicode__(self):
        return "%s" % self.cereal


    def nutrition_list(self):
        value_list = []
        value_list.append("Protien: %s" % self.protien_in_g)
        value_list.append("Calories: %s" % self.calories)
        value_list.append("Fat: %s" % self.fat)
        value_list.append("Soium: %s" % self.sodium)
        value_list.append("Dietary Fiber: %s" % self.dietary_fiber)
        value_list.append("Carbs: %s" % self.carbs)
        value_list.append("Sugars: %s" % self.sugars)
        value_list.append("Potassium: %s" % self.potassium)
        value_list.append("Vitamins and Minerals: %s" % self.vitamins_and_minerals)
        value_list.append("Serving Size Weight: %s" % self.serving_size_weight)
        value_list.append("Cups Per Serving: %s" % self.cups_per_serving)

        return value_list









