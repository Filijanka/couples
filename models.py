from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Alicja Reuben'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'couples'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    Choice1.task1 = models.CharField()
    Choice2.task1 = models.CharField()
    Choice3.task1 = models.CharField()
    Choice4.task1 = models.CharField()
    Choice5.task1 = models.CharField()
    Choice6.task1 = models.CharField()
    Choice1.task2 = models.CharField()
    Choice2.task2 = models.CharField()
    Choice3.task2 = models.CharField()
    Choice4.task2 = models.CharField()
    Choice5.task2 = models.CharField()
    Choice6.task2 = models.CharField()
    Choice1.task3 = models.CharField()
    Choice2.task3 = models.CharField()
    Choice3.task3 = models.CharField()
    Choice4.task3 = models.CharField()
    Choice5.task3 = models.CharField()
    Choice6.task3 = models.CharField()
    Choice1.task4 = models.CharField()
    Choice2.task4 = models.CharField()
    Choice3.task4 = models.CharField()
    Choice4.task4 = models.CharField()
    Choice5.task4 = models.CharField()
    Choice6.task4 = models.CharField()
    Choice1.task5 = models.CharField()
    Choice2.task5 = models.CharField()
    Choice3.task5 = models.CharField()
    Choice4.task5 = models.CharField()
    Choice5.task5 = models.CharField()
    Choice6.task5 = models.CharField()
    Choice1.task6 = models.CharField()
    Choice2.task6 = models.CharField()
    Choice3.task6 = models.CharField()
    Choice4.task6 = models.CharField()
    Choice5.task6 = models.CharField()
    Choice6.task6 = models.CharField()
    Choice1.task7 = models.CharField()
    Choice2.task7 = models.CharField()
    Choice3.task7 = models.CharField()
    Choice4.task7 = models.CharField()
    Choice5.task7 = models.CharField()
    Choice6.task7 = models.CharField()
    Choice1.task8 = models.CharField()
    Choice2.task8 = models.CharField()
    Choice3.task8 = models.CharField()
    Choice4.task8 = models.CharField()
    Choice5.task8 = models.CharField()
    Choice6.task8 = models.CharField()