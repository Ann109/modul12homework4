import rt_with_exceptions as rt
import logging as log
import unittest

log.basicConfig(
        level=log.INFO, # Уровень - INFO
        filemode='w', # Режим - запись с заменой('w')
        filename='runner_tests.log', # Название файла - runner_tests.log
        encoding='UTF-8', # Кодировка - UTF-8
        format='%(asctime)s | %(levelname)s | %(message)s') #Формат вывода - на своё усмотрение, обязательная информация: уровень логирования, сообщение логирования.


class RunnerTest(unittest.TestCase):
        def test_walk(self):
                try:
                        runner = rt.Runner("Runner1", speed=-9)
                        runner.walk()
                        log.info('"test_walk" выполнен успешно') # В блок try добавьте логирование INFO с сообщением '"test_walk" выполнен успешно'
                except ValueError as err: # В блоке except обработайте исключение соответствующего типа и
                        log.warning("Неверная скорость для Runner") # логируйте его на уровне WARNING с сообщением "Неверная скорость для Runner".

        def test_run(self):
                try:
                        runner = rt.Runner(1, 9)
                        runner.run()
                        log.info('"test_run" выполнен успешно') # В блок try добавьте логирование INFO с сообщением '"test_run" выполнен успешно'
                except TypeError as err: # В блоке except обработайте исключение соответствующего типа и
                        log.warning("Неверный тип данных для объекта Runner") # логируйте его на уровне WARNING с сообщением "Неверный тип данных для объекта Runner".


if __name__ == '__main__':
        unittest.main()






