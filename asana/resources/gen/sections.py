
class _Sections:

    def __init__(self, client=None):
        self.client = client

    def add_task_for_section(self, section_gid, params={}, **options):
        """Add task to section
        :param str section_gid: The globally unique identifier for the section. (required)
        [params] : {Object} Parameters for the request
        :return: EmptyObject
        """
        path = "/sections/{section_gid}/addTask".replace("section_gid", section_gid)
        return self.client.get(path, params, **options)


    def create_section_for_project(self, project_gid, params={}, **options):
        """Create a section in a project
        :param str project_gid: Globally unique identifier for the project. (required)
        [params] : {Object} Parameters for the request
        :return: SectionResponse
        """
        path = "/projects/{project_gid}/sections".replace("project_gid", project_gid)
        return self.client.get(path, params, **options)


    def delete_section(self, section_gid, params={}, **options):
        """Delete a section
        :param str section_gid: The globally unique identifier for the section. (required)
        [params] : {Object} Parameters for the request
        :return: EmptyObject
        """
        path = "/sections/{section_gid}".replace("section_gid", section_gid)
        return self.client.get(path, params, **options)


    def get_section(self, section_gid, params={}, **options):
        """Get a section
        :param str section_gid: The globally unique identifier for the section. (required)
        [params] : {Object} Parameters for the request
        :return: SectionResponse
        """
        path = "/sections/{section_gid}".replace("section_gid", section_gid)
        return self.client.get(path, params, **options)


    def get_sections_for_project(self, project_gid, params={}, **options):
        """Get sections in a project
        :param str project_gid: Globally unique identifier for the project. (required)
        [params] : {Object} Parameters for the request
        :return: list[SectionCompact]
        """
        path = "/projects/{project_gid}/sections".replace("project_gid", project_gid)
        return self.client.get(path, params, **options)


    def insert_section_for_project(self, project_gid, params={}, **options):
        """Move or Insert sections
        :param str project_gid: Globally unique identifier for the project. (required)
        [params] : {Object} Parameters for the request
        :return: EmptyObject
        """
        path = "/projects/{project_gid}/sections/insert".replace("project_gid", project_gid)
        return self.client.get(path, params, **options)


    def update_section(self, section_gid, params={}, **options):
        """Update a section
        :param str section_gid: The globally unique identifier for the section. (required)
        [params] : {Object} Parameters for the request
        :return: SectionResponse
        """
        path = "/sections/{section_gid}".replace("section_gid", section_gid)
        return self.client.get(path, params, **options)

