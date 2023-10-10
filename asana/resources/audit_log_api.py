
from .gen.audit_log_api import _AuditLogAPI
from ..page_iterator import AuditLogAPIIterator


class AuditLogAPI(_AuditLogAPI):
    """AuditLogAPI resource"""

    def get_audit_log_events(self, workspace_gid, params={}, **options):
        """Override get_audit_log_events to handle non-empty next_page parameter"""
        path = "/workspaces/{workspace_gid}/audit_log_events".replace(
            "{workspace_gid}", workspace_gid)
        options = self.client._merge_options(options)
        if options['iterator_type'] == 'items':
            return AuditLogAPIIterator(self.client, path, params, options).items()
        if options['iterator_type'] is None:
            return self.client.get(path, params, **options)
        raise Exception('Unknown value for "iterator_type" option: {}'.format(
            str(options['iterator_type'])))
