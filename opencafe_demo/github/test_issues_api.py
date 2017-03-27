from cafe.drivers.unittest.fixtures import BaseTestFixture

from opencafe_demo.github.github_client import GitHubClient
from opencafe_demo.github.github_config import GitHubConfig


class BasicGitHubTest(BaseTestFixture):

    @classmethod
    def setUpClass(cls):
        super(BasicGitHubTest, cls).setUpClass()  # Sets up logging/reporting
        cls.config_data = GitHubConfig()

        cls.organization = cls.config_data.organization
        cls.project = cls.config_data.project
        cls.issue_id = cls.config_data.issue_id
        cls.client = GitHubClient(cls.config_data.base_url)

    def test_get_issue_response_code_is_200(self):
        response = self.client.get_project_issue(
            self.organization, self.project, self.issue_id)
        self.assertEqual(response.status_code, 200)

    def test_id_is_not_null_for_get_issue_request(self):
        response = self.client.get_project_issue(
            self.organization, self.project, self.issue_id)
        # The response signature is the raw response from Requests except
        # for the `entity` property, which is the object that represents
        # the response content
        issue = response.entity
        self.assertIsNotNone(issue.id)
