from dotcms_rest_client.paths.v1_workflow_actions_action_id.get import ApiForget
from dotcms_rest_client.paths.v1_workflow_actions_action_id.put import ApiForput
from dotcms_rest_client.paths.v1_workflow_actions_action_id.delete import ApiFordelete


class V1WorkflowActionsActionId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
