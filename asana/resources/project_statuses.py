
from .gen.project_statuses import _ProjectStatuses

class ProjectStatuses(_ProjectStatuses):
    """Project Statuses resource"""
    def create(self, project, params={}, **options):
        self.create_in_project(project, params, **options)

