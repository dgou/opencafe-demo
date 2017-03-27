from cafe.engine.models.data_interfaces import ConfigSectionInterface


class GitHubConfig(ConfigSectionInterface):

    SECTION_NAME = 'GitHub'

    @property
    def base_url(self):
        return self.get('base_url')

    @property
    def organization(self):
        return self.get('organization')

    @property
    def project(self):
        return self.get('project')

    @property
    def issue_id(self):
        return self.get('issue_id')
