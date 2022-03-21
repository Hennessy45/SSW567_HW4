import unittest

from HW4A import get_repo_info


class GithubAPI(unittest.TestCase):
    def test_normal_response(self):
        expected = ['User: Hennessy45',
                    'Repo: test1 Number of commits: 3',
                    'Repo: test2 Number of commits: 2',
                    'Repo: Triangle567 Number of commits: 1']
        self.assertEqual(get_repo_info(), expected)

    def test_bad_user_name(self):
        self.assertEqual(get_repo_info('dhfilahofhaodsjf'), 'unable to fetch repos from user')
        self.assertEqual(get_repo_info(''), 'unable to fetch repos from user')


if __name__ == '__main__':
    unittest.main()