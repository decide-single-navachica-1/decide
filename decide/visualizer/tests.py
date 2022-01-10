from base.tests import BaseTestCase
import visualizer.views as view

class VisualizerTests(BaseTestCase):
    data = ['visualizer/migrations/prueba.json', ]

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()
        
    def test_vista_visualizer(self):
       response = self.client.get('/visualizer/')
       self.assertEqual(response.status_code, 200)

    def test_votacion_existente(self):
    response = self.client.get('/visualizer/1/')
    self.assertEqual(response.status_code, 200)

    def test_votacion_no_existente(self):
        response = self.client.get('/visualizer/999/')
        self.assertEqual(response.status_code, 404)
        
    def test_num_votos(self):
        num = view.votesOfVoting(1)
        res = 3;
        self.assertEqual(res, num)

    def test_abstenciones(self):
        res = 1
        abstenciones = view.abstentions(1)
        self.assertEquals(res, abstenciones)

        
  
        

    
