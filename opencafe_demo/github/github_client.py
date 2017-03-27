from cafe.engine.http.client import AutoMarshallingHTTPClient

from opencafe_demo.github.github_models import Issue


class GitHubClient(AutoMarshallingHTTPClient):

    def __init__(self, base_url):
        super(GitHubClient, self).__init__('json', 'json')
        self.base_url = base_url

    def get_project_issue(self, org_name, project_name, issue_id):

        url = '{base_url}/repos/{org}/{project}/issues/{issue_id}'.format(
            base_url=self.base_url, org=org_name, project=project_name,
            issue_id=issue_id)
        return self.get(url, response_entity_type=Issue)
