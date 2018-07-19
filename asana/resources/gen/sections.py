
class _Sections:
    """A _section_ is a subdivision of a project that groups tasks together. It can
    either be a header above a list of tasks in a list view or a column in a
    board view of a project.
    """

    def __init__(self, client=None):
        self.client = client
  
    def create_in_project(self, project, params={}, **options): 
        """Creates a new section in a project.
        
        Returns the full record of the newly created section.

        Parameters
        ----------
        project : {Id} The project to create the section in
        [data] : {Object} Data for the request
          - name : {String} The text to be displayed as the section name. This cannot be an empty string.
        """
        path = "/projects/%s/sections" % (project)
        return self.client.post(path, params, **options)
        
    def find_by_project(self, project, params={}, **options): 
        """Returns the compact records for all sections in the specified project.

        Parameters
        ----------
        project : {Id} The project to get sections from.
        [params] : {Object} Parameters for the request
        """
        path = "/projects/%s/sections" % (project)
        return self.client.get(path, params, **options)
        
    def find_by_id(self, section, params={}, **options): 
        """Returns the complete record for a single section.

        Parameters
        ----------
        section : {Id} The section to get.
        [params] : {Object} Parameters for the request
        """
        path = "/sections/%s" % (section)
        return self.client.get(path, params, **options)
        
    def update(self, section, params={}, **options): 
        """A specific, existing section can be updated by making a PUT request on
        the URL for that project. Only the fields provided in the `data` block
        will be updated; any unspecified fields will remain unchanged. (note that
        at this time, the only field that can be updated is the `name` field.)
        
        When using this method, it is best to specify only those fields you wish
        to change, or else you may overwrite changes made by another user since
        you last retrieved the task.
        
        Returns the complete updated section record.

        Parameters
        ----------
        section : {Id} The section to update.
        [data] : {Object} Data for the request
        """
        path = "/sections/%s" % (section)
        return self.client.put(path, params, **options)
        
    def delete(self, section, params={}, **options): 
        """A specific, existing section can be deleted by making a DELETE request
        on the URL for that section.
        
        Note that sections must be empty to be deleted.
        
        The last remaining section in a board view cannot be deleted.
        
        Returns an empty data block.

        Parameters
        ----------
        section : {Id} The section to delete.
        """
        path = "/sections/%s" % (section)
        return self.client.delete(path, params, **options)
        
    def insert_in_project(self, project, params={}, **options): 
        """Move sections relative to each other in a board view. One of
        `before_section` or `after_section` is required.
        
        Sections cannot be moved between projects.
        
        At this point in time, moving sections is not supported in list views, only board views.
        
        Returns an empty data block.

        Parameters
        ----------
        project : {Id} The project in which to reorder the given section
        [data] : {Object} Data for the request
          - section : {Id} The section to reorder
          - [before_section] : {Id} Insert the given section immediately before the section specified by this parameter.
          - [after_section] : {Id} Insert the given section immediately after the section specified by this parameter.
        """
        path = "/projects/%s/sections/insert" % (project)
        return self.client.post(path, params, **options)
        
