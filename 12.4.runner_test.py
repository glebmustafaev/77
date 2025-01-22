import logging
import runner
import unittest


logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='utf-8',
                    format='%(asctime)s | %(levelname)s | %(message)s')

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            my_walk = runner.Runner('Лев', -3)
            for i in range(10):
                my_walk.walk()
            self.assertEqual(my_walk.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    def test_run(self):
        try:
            my_run = runner.Runner(12.3)
            for j in range(10):
                my_run.run()
            self.assertEqual(my_run.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

if __name__ == '__main__':
    unittest.main()


