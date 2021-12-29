#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from docs_libs import utils
from docs_libs import workflow_parser
from docs_libs import index_md


OUTPUT_DIR = 'docs_examples/'
INPUT_DIR = 'examples/'

if __name__ == '__main__':
    print(utils.welcosme_msg())
    wf_p = workflow_parser.WalkPaserToMarkdown(INPUT_DIR, OUTPUT_DIR)
    wf_p.parse_to_markdown()
    index_md.IdexMD(OUTPUT_DIR).create_index_md()
    