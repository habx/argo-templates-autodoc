### Table of Contents
  * [utils-jq](#utils-jq)
      * [jq-rc](#jq-rc)
      * [jq-rc-to-file](#jq-rc-to-file)
      * [jq-merge-file-with-arg](#jq-merge-file-with-arg)

# utils-jq
[utils-jq | see source](../example/jq.yaml)

### jq-rc

Inputs parameters:

| name | default_value |
|:---:|:---:|
| version | 1.6 |
| jq-key | No default value |
| json | No default value |


### jq-rc-to-file

Inputs parameters:

| name | default_value |
|:---:|:---:|
| version | 1.6 |
| jq-key | No default value |


Inputs artifacts:

| name | path |
|:---:|:---:|
| data | /tmp/input/input.json |


Output artifacts:

| name | path |
|:---:|:---:|
| data | /tmp/output/output.json |


### jq-merge-file-with-arg

Inputs parameters:

| name | default_value |
|:---:|:---:|
| version | 1.6 |
| jq-args | No default value |
| jq-key | No default value |


Inputs artifacts:

| name | path |
|:---:|:---:|
| data | /tmp/input/input.json |


Output artifacts:

| name | path |
|:---:|:---:|
| data | /tmp/output/output.json |
