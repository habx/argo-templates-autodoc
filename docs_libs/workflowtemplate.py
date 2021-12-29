
class WorkflowTemplate:
    def __init__(self, workflow: object):
        self._workflow = workflow
        self.workflow_template_name = self._get_workflow_template_name()
        self.workflow_templates_spec = self._reduce_specs(self._get_workflow_template_spec())

    def get_templates_specs(self):
        templates = []
        for template in self.workflow_templates_spec:
            templates.append(WorkflowTemplateInputs(**template))
        return templates

    def _get_workflow_template_name(self):
        if self._metadata_name_exists():
            return self._workflow["metadata"]["name"]
        return None

    def _get_workflow_template_spec(self):
        if self._spec_templates_exists():
            return self._workflow["spec"]["templates"]
        return None

    # Remove all specs that are not needed
    def _reduce_specs(self, spec):
        new_spec = []
        if spec is None:
            return new_spec
        for s in spec:
            new_spec_object = {}
            if "name" in s:
                new_spec_object["name"] = s["name"]
            if "inputs" in s:
                new_spec_object["inputs"] = s["inputs"]
            if "outputs" in s:
                new_spec_object["outputs"] = s["outputs"]
            new_spec.append(new_spec_object)
        return new_spec
            
    # metadata > name    
    def _metadata_name_exists(self):
        if self._metadata_exists():
            if "name" in self._workflow["metadata"]:
                return True
        return False
    # metadata 
    def _metadata_exists(self):
        if "metadata" in self._workflow:
            return True
        return False

    # spec > templates
    def _spec_templates_exists(self):
        if self._spec_exists():
            if "templates" in self._workflow["spec"]:
                return True
        return False

    # spec 
    def _spec_exists(self):
        if "spec" in self._workflow:
            return True
        return False

    

class WorkflowTemplateInputs(WorkflowTemplate):
    def __init__(self, **entries: object):
        self.__dict__.update(entries)
    def __repr__(self):
        return str(self.__dict__)
    def new_default(self, default: str):
        self.default = default
