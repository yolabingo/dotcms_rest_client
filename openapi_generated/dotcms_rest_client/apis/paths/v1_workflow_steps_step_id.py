from dotcms_rest_client.paths.v1_workflow_steps_step_id.get import ApiForget
from dotcms_rest_client.paths.v1_workflow_steps_step_id.put import ApiForput
from dotcms_rest_client.paths.v1_workflow_steps_step_id.delete import ApiFordelete


class V1WorkflowStepsStepId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
