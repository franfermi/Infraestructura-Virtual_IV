import unittest
import metodosBD

class TestMetodos(unittest.TestCase):

    """ Test que comprueba que una asignatura esta disponible """
    def test_asig_disponible(self, nombAsig):
        num_asig = metodosBD.nombreAsignatura(nombAsig)
        self.assertTrue(num_asig)

if __name__ == '__main__':
   unittest.main()
