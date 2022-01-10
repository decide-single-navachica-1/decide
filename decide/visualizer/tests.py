from django.test import TestCase
from base.tests import BaseTestCase
import visualizer.views as view

class VisualizerTests(BaseTestCase):
    data = ['visualizer/migrations/prueba.json', ]

def test_votaciones_no_empezadas(self):
    res = 1
    num = view.unstartedVotings()
    self.assertEquals(res, num)

def test_votaciones_empezadas(self):
    res = 4
    num = view.startedVotings()
    self.assertEquals(res, num)

def test_votaciones_terminadas(self):
    res = 2
    num = view.finishedVotings()
    self.assertEquals(res, num)

def test_votaciones_cerradas(self):
    res = 2
    num = view.closedVotings()
    self.assertEquals(res, num)

def test_comparador(self):
    res = 150
    comp = view.votingComparator(1,2)
    self.assertEquals(res, comp)
