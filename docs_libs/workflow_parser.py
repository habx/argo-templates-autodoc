"""workflow parser"""
# -*- coding: utf-8 -*-
import os, yaml
from . import workflowtemplate
from markdowngenerator import markdowngenerator


class WalkPaserToMarkdown:
    def __init__(self, dir: str, output_dir: str):
        self.output_dir = output_dir
        self.get_files_dir(dir)

    def get_files_dir(self, dir):
        self.files_path = []
        for root, dirs, files in os.walk(dir):
            for file in files:
                if file.endswith('.yaml'):
                    self.files_path.append(os.path.join(root, file))

    def parse_to_markdown(self):
        for file_path in self.files_path:
            with open(file_path, "r") as stream:
                yaml_file = None
                try:
                    yaml_file = yaml.safe_load(stream)
                except yaml.YAMLError as exc:
                    print("YAML Parsing error:" + exc)
                    continue

            print("Reading file {}".format(file_path))
            if yaml_file is None:
                print("YAML file is empty: {}".format(file_path))
            wf = workflowtemplate.WorkflowTemplate(yaml_file)
            self._new_md_page(file_path, wf)

    def _new_md_page(self, file_path: str, wf: workflowtemplate.WorkflowTemplate):
        with markdowngenerator.MarkdownGenerator(
            filename=self.output_dir + wf.workflow_template_name + ".md", enable_write=False, enable_TOC=False

        ) as doc:
            doc.addHeader(1, wf.workflow_template_name)
            doc.writeTextLine(doc.generateHrefNotation(text=wf.workflow_template_name + " | see source", url="../"+file_path))
            for template in wf.get_templates_specs():
                if not hasattr(template, 'name'):
                    print("Template has no name....")
                    continue
            
                doc.addHeader(3, template.name)

                if hasattr(template, 'inputs'):
                    if "parameters" in template.inputs:
                        input_parameters = self._get_template_md_parameters(template.inputs["parameters"])
                        if input_parameters:
                            doc.writeTextLine("")
                            doc.writeTextLine("Inputs parameters:")
                            doc.addTable(dictionary_list=input_parameters)
                    if "artifacts" in template.inputs:
                        input_artifacts = self._get_template_md_artifacts(template.inputs["artifacts"])
                        if input_artifacts:
                            doc.writeTextLine("")
                            doc.writeTextLine("Inputs artifacts:")
                            doc.addTable(dictionary_list=input_artifacts)
                if hasattr(template, 'outputs'):
                    if "parameters" in template.outputs:
                        output_parameters = self._get_template_md_parameters(template.outputs["parameters"])
                        if output_parameters:
                            doc.writeTextLine("")
                            doc.writeTextLine("Outputs parameters:")
                            doc.addTable(dictionary_list=output_parameters)
                    if "artifacts" in template.outputs:
                        output_artifacts = self._get_template_md_artifacts(template.outputs["artifacts"])
                        if output_artifacts:
                            doc.writeTextLine("")
                            doc.writeTextLine("Output artifacts:")
                            doc.addTable(dictionary_list=output_artifacts)
            doc.genTableOfContent(linenumber=1, max_depth=5)

    def _get_template_md_artifacts(self, outputs: list):
        new_outputs = []
        for output in outputs:
            row = {"name": output["name"],}
            if not "path" in output:
                row["path"] = "No path"
            else:
                row["path"] = output["path"]
            new_outputs.append(row)
        return new_outputs

    def _get_template_md_parameters(self, inputs: list):
        new_inputs = []
        for input in inputs:
            row = {"name": input["name"]}
            if not "default" in input:
                row["default_value"] = "No default value"
            else:
                row["default_value"] = input["default"]
            new_inputs.append(row)
        return new_inputs