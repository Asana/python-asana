# coding: utf-8

from __future__ import absolute_import

import os
import unittest

import asana
from asana.api.tasks_api import TasksApi  # noqa: E501
from asana.rest import ApiException
from dotenv import load_dotenv


class TestTasksApi(unittest.TestCase):
    """TasksApi unit test stubs"""

    @classmethod
    def setUpClass(cls):
        load_dotenv()

        # Load environment variables
        cls.TEXT_CUSTOM_FIELD_GID = os.environ["TEXT_CUSTOM_FIELD_GID"]
        cls.USER_GID = os.environ["USER_GID"]
        cls.WORKSPACE_GID = os.environ["WORKSPACE_GID"]

        configuration = asana.Configuration()
        configuration.access_token = os.environ["PERSONAL_ACCESS_TOKEN"]
        api_client = asana.ApiClient(configuration)

        cls.api = TasksApi(api_client)  # noqa: E501
        
        # Create a global task used for testing
        try:
            cls.task_name = "Task 1"
            cls.task_notes = "Some description"
            cls.task = cls.api.create_task(
                {
                    "data": {
                        "assignee": cls.USER_GID,
                        "name": cls.task_name,
                        "notes": cls.task_notes,
                        "workspace": cls.WORKSPACE_GID,
                    }
                },
                {}
            )
        except ApiException as e:
            raise Exception(e)

    @classmethod
    def tearDownClass(cls):
        try:
            # Delete global task
            cls.api.delete_task(cls.task["gid"])
        except ApiException as e:
            raise Exception(e)

    def test_create_task(self):
        """Test case for create_task

        Create a task  # noqa: E501
        """
        try:
            # Create a task
            task_name = "Task 2"
            task_notes = "Some description"
            task = self.api.create_task(
                {
                    "data": {
                        "name": task_name,
                        "notes": task_notes,
                        "workspace": self.WORKSPACE_GID,
                    }
                },
                {}
            )
            # Check that the task was created
            self.assertIsNotNone(task)
            self.assertEqual(task["name"], task_name)
            self.assertEqual(task["notes"], task_notes)

            # Delete task
            self.api.delete_task(task["gid"])
        except ApiException as e:
            raise Exception(e)

    def test_delete_task(self):
        """Test case for delete_task

        Delete a task  # noqa: E501
        """
        try:
            # Create a task to delete
            task_name = "Task 2"
            task_notes = "Some description"
            task = self.api.create_task(
                {
                    "data": {
                        "name": task_name,
                        "notes": task_notes,
                        "workspace": self.WORKSPACE_GID,
                    }
                },
                {}
            )

            # Delete task
            deleted_task = self.api.delete_task(task["gid"])
            
            # Check that the task got deleted
            self.assertEqual(deleted_task, {})
        except ApiException as e:
            raise Exception(e)

    def test_get_task(self):
        """Test case for get_task

        Get a task  # noqa: E501
        """
        try:
            # Get a task
            task = self.api.get_task(self.task["gid"], {})
            # Check task response
            self.assertIsNotNone(task)
            self.assertEqual(task["name"], self.task_name)
            self.assertEqual(task["notes"], self.task_notes)
            self.assertEqual(task["resource_subtype"], "default_task")
            self.assertIsNone(task["actual_time_minutes"])
            self.assertEqual(task["assignee"]["gid"], self.USER_GID)
            self.assertIsNotNone(task["assignee_status"])
            self.assertEqual(task["completed"], False)
            self.assertIsNone(task["completed_at"])
            self.assertTrue(task["custom_fields"].__class__ == list)
            self.assertIsNone(task["due_at"])
            self.assertIsNone(task["due_on"])
            self.assertTrue(task["followers"].__class__ == list)
            self.assertFalse(task["hearted"])
            self.assertTrue(task["hearts"].__class__ == list)
            self.assertFalse(task["liked"])
            self.assertTrue(task["likes"].__class__ == list)
            self.assertTrue(task["memberships"].__class__ == list)
            self.assertIsNotNone(task["modified_at"])
            self.assertEqual(task["num_hearts"], 0)
            self.assertEqual(task["num_likes"], 0)
            self.assertIsNone(task["parent"])
            self.assertIsNotNone(task["permalink_url"])
            self.assertTrue(task["projects"].__class__ == list)
            self.assertEqual(task["resource_type"], "task")
            self.assertIsNone(task["start_at"])
            self.assertIsNone(task["start_on"])
            self.assertTrue(task["tags"].__class__ == list)
            self.assertTrue(task["workspace"].__class__ == dict)
        except ApiException as e:
            raise Exception(e)
        
    def test_get_task_with_opt_fields(self):
        """Test case for get_task with opt_fields

        Get a task with opt_fields # noqa: E501
        """
        try:
            # Get a task
            task = self.api.get_task(self.task["gid"], {'opt_fields': "name,notes"})
            # Check task response
            self.assertIsNotNone(task)
            self.assertEqual(task["name"], self.task_name)
            self.assertEqual(task["notes"], self.task_notes)
        except ApiException as e:
            raise Exception(e)
        
    def test_get_tasks(self):
        """Test case for get_tasks

        Get multiple tasks  # noqa: E501
        """
        try:
            # Get multiple tasks
            tasks = self.api.get_tasks({
                'assignee': self.USER_GID,
                'workspace': self.WORKSPACE_GID,
            })
            for task in tasks:
                self.assertIsNotNone(task["gid"])
                self.assertIsNotNone(task["name"])
                self.assertIsNotNone(task["resource_type"])
                self.assertIsNotNone(task["resource_subtype"])
        except ApiException as e:
            raise Exception(e)

    def test_get_tasks_with_opt_fields(self):
        """Test case for get_tasks with opt_fields

        Get multiple tasks with opt_fields # noqa: E501
        """
        try:
            # Get multiple tasks
            tasks = self.api.get_tasks({
                'limit': 100,
                'assignee': self.USER_GID,
                'workspace': self.WORKSPACE_GID,
                'opt_fields': "actual_time_minutes,approval_status,assignee,assignee.name,assignee_section,assignee_section.name,assignee_status,completed,completed_at,completed_by,completed_by.name,created_at,created_by,custom_fields,custom_fields.asana_created_field,custom_fields.created_by,custom_fields.created_by.name,custom_fields.currency_code,custom_fields.custom_label,custom_fields.custom_label_position,custom_fields.date_value,custom_fields.date_value.date,custom_fields.date_value.date_time,custom_fields.description,custom_fields.display_value,custom_fields.enabled,custom_fields.enum_options,custom_fields.enum_options.color,custom_fields.enum_options.enabled,custom_fields.enum_options.name,custom_fields.enum_value,custom_fields.enum_value.color,custom_fields.enum_value.enabled,custom_fields.enum_value.name,custom_fields.format,custom_fields.has_notifications_enabled,custom_fields.is_formula_field,custom_fields.is_global_to_workspace,custom_fields.is_value_read_only,custom_fields.multi_enum_values,custom_fields.multi_enum_values.color,custom_fields.multi_enum_values.enabled,custom_fields.multi_enum_values.name,custom_fields.name,custom_fields.number_value,custom_fields.people_value,custom_fields.people_value.name,custom_fields.precision,custom_fields.resource_subtype,custom_fields.text_value,custom_fields.type,dependencies,dependents,due_at,due_on,external,external.data,followers,followers.name,hearted,hearts,hearts.user,hearts.user.name,html_notes,is_rendered_as_separator,liked,likes,likes.user,likes.user.name,memberships,memberships.project,memberships.project.name,memberships.section,memberships.section.name,modified_at,name,notes,num_hearts,num_likes,num_subtasks,offset,parent,parent.created_by,parent.name,parent.resource_subtype,path,permalink_url,projects,projects.name,resource_subtype,start_at,start_on,tags,tags.name,uri,workspace,workspace.name,resource_type",
            })
            for task in tasks:
                self.assertIsNotNone(task)
                if self.task_name in task["name"]:
                    self.assertEqual(task["name"], self.task_name)
                    self.assertEqual(task["notes"], self.task_notes)
                    self.assertEqual(task["resource_subtype"], "default_task")
                    self.assertIsNone(task["actual_time_minutes"])
                    self.assertEqual(task["assignee"]["gid"], self.USER_GID)
                    self.assertIsNotNone(task["assignee_status"])
                    self.assertEqual(task["completed"], False)
                    self.assertIsNone(task["completed_at"])
                    self.assertTrue(task["custom_fields"].__class__ == list)
                    self.assertIsNone(task["due_at"])
                    self.assertIsNone(task["due_on"])
                    self.assertTrue(task["followers"].__class__ == list)
                    self.assertFalse(task["hearted"])
                    self.assertTrue(task["hearts"].__class__ == list)
                    self.assertFalse(task["liked"])
                    self.assertTrue(task["likes"].__class__ == list)
                    self.assertTrue(task["memberships"].__class__ == list)
                    self.assertIsNotNone(task["modified_at"])
                    self.assertEqual(task["num_hearts"], 0)
                    self.assertEqual(task["num_likes"], 0)
                    self.assertIsNone(task["parent"])
                    self.assertIsNotNone(task["permalink_url"])
                    self.assertTrue(task["projects"].__class__ == list)
                    self.assertEqual(task["resource_type"], "task")
                    self.assertIsNone(task["start_at"])
                    self.assertIsNone(task["start_on"])
                    self.assertTrue(task["tags"].__class__ == list)
                    self.assertTrue(task["workspace"].__class__ == dict)
        except ApiException as e:
            raise Exception(e)

    def test_search_tasks_for_workspace(self):
        """Test case for search_tasks_for_workspace

        Search tasks in a workspace  # noqa: E501
        """
        try:
            search_text = "task" # Make sure this is lower case
            opts = {
                'text': search_text,
                'completed': False,
                'opt_fields': "name, notes"
            }
            tasks = self.api.search_tasks_for_workspace(self.WORKSPACE_GID, opts)
            # Check that there are tasks returned
            count = 0
            for task in tasks:
                count += 1
                # Check that the results contain the search text
                self.assertTrue(search_text in task["name"].lower() or search_text in task["notes"].lower())

            # Check that there are results
            self.assertIsNotNone(tasks)
            # We know that there is at least one result for this search.
            # Assert greater than or equal to because other tests or modifications might increase this search result.
            self.assertGreaterEqual(count, 1)

            # Delete task
            self.api.delete_task(task["gid"])
        except ApiException as e:
            raise Exception(e)
        
    def test_search_tasks_for_workspace_with_custom_field_parameter(self):
        """Test case for search_tasks_for_workspace with custom field parameter

        Search tasks in a workspace with custom field parameter # noqa: E501
        """
        try:
            search_text = "custom_value" # Make sure this is lower case
            opts = {
                f'custom_fields.{self.TEXT_CUSTOM_FIELD_GID}.value': search_text,
                'opt_fields': "custom_fields"
            }
            tasks = self.api.search_tasks_for_workspace(self.WORKSPACE_GID, opts)
            # Check that the search result only returns tasks with the custom field value of search_text
            for task in tasks:
                for custom_field in task["custom_fields"]:
                    if custom_field["gid"] == self.TEXT_CUSTOM_FIELD_GID:
                        self.assertEqual(custom_field["text_value"].lower(), search_text)
        except ApiException as e:
            raise Exception(e)

    def test_update_task(self):
        """Test case for update_task

        Update a task  # noqa: E501
        """
        try:
            # Create a task to update
            task_name = "Task 2"
            task_notes = "Some description"
            task = self.api.create_task(
                {
                    "data": {
                        "name": task_name,
                        "notes": task_notes,
                        "workspace": self.WORKSPACE_GID,
                    }
                },
                {}
            )
            # Update task
            updated_task_name = "Task 2 - Updated"
            updated_task_description = "Some description updated"
            task = self.api.update_task(
                {
                    "data": {
                        "name": updated_task_name,
                        "notes": updated_task_description,
                    }
                },
                task["gid"],
                {}
            )
            # Check that the task has been updated
            self.assertIsNotNone(task)
            self.assertEqual(task["name"], updated_task_name)
            self.assertEqual(task["notes"], updated_task_description)

            # Delete task
            self.api.delete_task(task["gid"])
        except ApiException as e:
            raise Exception(e)


if __name__ == '__main__':
    unittest.main()
