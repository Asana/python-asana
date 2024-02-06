# coding: utf-8

from __future__ import absolute_import

import os
import unittest

import asana
from asana.api.projects_api import ProjectsApi  # noqa: E501
from asana.rest import ApiException
from dotenv import load_dotenv


class TestProjectsApi(unittest.TestCase):
    """ProjectsApi unit test stubs"""

    @classmethod
    def setUpClass(cls):
        load_dotenv()

        # Load environment variables
        cls.TEAM_GID = os.environ["TEAM_GID"]
        cls.WORKSPACE_GID = os.environ["WORKSPACE_GID"]

        configuration = asana.Configuration()
        configuration.access_token = os.environ["PERSONAL_ACCESS_TOKEN"]
        api_client = asana.ApiClient(configuration)

        cls.api = ProjectsApi(api_client)  # noqa: E501

        # Create a global project for testing
        try:
            cls.project_name = "Project 1"
            cls.project_notes = "Some description"
            cls.project = cls.api.create_project(
                {
                    "data": {
                        "name": cls.project_name,
                        "notes": cls.project_notes,
                        "team": cls.TEAM_GID
                    }
                },
                {}
            )
        except ApiException as e:
            raise Exception(e)

    @classmethod
    def tearDownClass(cls):
        try:
            # Delete global project
            cls.api.delete_project(cls.project["gid"])
        except ApiException as e:
            raise Exception(e)

    def test_create_project(self):
        """Test case for create_project

        Create a project  # noqa: E501
        """
        try:
            # Create a project
            project_name = "Project 2"
            project_notes = "Some description"
            project = self.api.create_project(
                {
                    "data": {
                        "name": project_name,
                        "notes": project_notes,
                        "team": self.TEAM_GID
                    }
                },
                {}
            )
            # Check that the project was created
            self.assertIsNotNone(project)
            self.assertEqual(project["name"], project_name)
            self.assertEqual(project["notes"], project_notes)

            # Delete project
            self.api.delete_project(project["gid"])
        except ApiException as e:
            raise Exception(e)

    def test_delete_project(self):
        """Test case for delete_project

        Delete a project  # noqa: E501
        """
        try:
            # Create a project to delete
            project_name = "Project 2"
            project_notes = "Some description"
            project = self.api.create_project(
                {
                    "data": {
                        "name": project_name,
                        "notes": project_notes,
                        "team": self.TEAM_GID
                    }
                },
                {}
            )

            # Delete project
            deleted_project = self.api.delete_project(project["gid"])

            # Check that the project got deleted
            self.assertEqual(deleted_project, {})
        except ApiException as e:
            raise Exception(e)

    def test_get_project(self):
        """Test case for get_project

        Get a project  # noqa: E501
        """
        try:
            project = self.api.get_project(self.project["gid"], {})
            # Check project response
            self.assertIsNotNone(project)
            self.assertFalse(project["archived"])
            self.assertIsNone(project["color"])
            self.assertFalse(project["completed"])
            self.assertIsNone(project["completed_at"])
            self.assertIsNotNone(project["created_at"])
            self.assertIsNone(project["current_status"])
            self.assertIsNone(project["current_status_update"])
            self.assertTrue(project["custom_field_settings"].__class__ == list)
            self.assertTrue(project["custom_fields"].__class__ == list)
            self.assertEqual(project["default_access_level"], "editor")
            self.assertEqual(project["default_view"], "list")
            self.assertIsNone(project["due_date"])
            self.assertIsNone(project["due_on"])
            self.assertTrue(project["followers"].__class__ == list)
            self.assertIsNotNone(project["gid"])
            self.assertTrue(project["members"].__class__ == list)
            self.assertEqual(project["minimum_access_level_for_customization"], "editor")
            self.assertIsNotNone(project["modified_at"])
            self.assertEqual(project["name"], self.project_name)
            self.assertEqual(project["notes"], self.project_notes)
            self.assertIsNotNone(project["owner"])
            self.assertIsNotNone(project["permalink_url"])
            self.assertTrue(project["public"])
            self.assertEqual(project["resource_type"], 'project')
            self.assertIsNone(project["start_on"])
            self.assertIsNotNone(project["team"])
            self.assertIsNotNone(project["workspace"])
        except ApiException as e:
            raise Exception(e)

    def test_get_project_with_opt_fields(self):
        """Test case for get_project with opt_fields

        Get a project with opt_fields # noqa: E501
        """
        try:
            project = self.api.get_project(
                self.project["gid"],
                {
                    'opt_fields': "name,notes"
                }
            )
            # Check project response
            self.assertIsNotNone(project)
            self.assertIsNotNone(project["gid"])
            self.assertEqual(project["name"], self.project_name)
            self.assertEqual(project["notes"], self.project_notes)
        except ApiException as e:
            raise Exception(e)


    def test_get_projects(self):
        """Test case for get_projects

        Get multiple projects  # noqa: E501
        """
        try:
            projects = self.api.get_projects(
                {
                    'limit': 100,
                    'workspace': self.WORKSPACE_GID
                }
            )
            # Check projects response
            self.assertIsNotNone(projects)
            for project in projects:
                self.assertIsNotNone(project["gid"])
                self.assertIsNotNone(project["name"])
                self.assertEqual(project["resource_type"], "project")
        except ApiException as e:
            raise Exception(e)

    def test_get_projects_with_opt_fields(self):
        """Test case for get_projects with opt_fields

        Get multiple projects with opt_fields # noqa: E501
        """
        try:
            projects = self.api.get_projects(
                {
                    'limit': 100,
                    'workspace': self.WORKSPACE_GID,
                    'opt_fields': "name, notes"
                }
            )
            # Check projects response
            self.assertIsNotNone(projects)
            for project in projects:
                self.assertIsNotNone(project["gid"])
                self.assertIsNotNone(project["name"])
                self.assertIsNotNone(project["notes"])
        except ApiException as e:
            raise Exception(e)

    def test_update_project(self):
        """Test case for update_project

        Update a project  # noqa: E501
        """
        try:
            # Create a project to update
            project_name = "Project 2"
            project_notes = "Some description"
            project = self.api.create_project(
                {
                    "data": {
                        "name": project_name,
                        "notes": project_notes,
                        "team": self.TEAM_GID
                    }
                },
                {}
            )

            # Update project
            updated_project_name = "Project 2 - Updated"
            updated_project_description = "Some description updated"
            project = self.api.update_project(
                {
                    "data": {
                        "name": updated_project_name,
                        "notes": updated_project_description,
                    }
                },
                project["gid"],
                {}
            )

            # Check that the project has been updated
            self.assertIsNotNone(project)
            self.assertEqual(project["name"], updated_project_name)
            self.assertEqual(project["notes"], updated_project_description)

            # Delete project
            self.api.delete_project(project["gid"])
        except ApiException as e:
            raise Exception(e)


if __name__ == '__main__':
    unittest.main()
