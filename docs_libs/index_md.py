"""workflow parser"""
# -*- coding: utf-8 -*-
import os
from markdowngenerator import markdowngenerator


class IdexMD:
    def __init__(self, output_dir: str):
        self.files_path = []
        self._output_dir = output_dir
        self.get_files_dir()

    def get_files_dir(self):
        for root, dirs, files in os.walk(self._output_dir):
            for file in files:
                if file.endswith('.md'):
                    self.files_path.append(os.path.join(root, file))

    def create_index_md(self):
        with markdowngenerator.MarkdownGenerator(
            filename=self._output_dir + "index.md", enable_write=False, enable_TOC=False

        ) as doc:
            doc.addHeader(1, "Workflow template")
            doc.writeTextLine("")
            for file in self.files_path:
                doc.writeTextLine(doc.generateHrefNotation(text=file.replace(self._output_dir, ""), url=file.replace(self._output_dir, "")))
           