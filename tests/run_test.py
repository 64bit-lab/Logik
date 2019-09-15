import test_sat
import test_parser


def run():
    print('Starting all unittests :')
    test_sat.run()
    test_parser.run()


if __name__ == '__main__':
    run()