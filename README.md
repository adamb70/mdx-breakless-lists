[![Build Status](https://travis-ci.com/adamb70/mdx-breakless-lists.svg?branch=master)](https://travis-ci.com/adamb70/mdx-breakless-lists)
# Breakless Lists Markdown Extension

Use lists without requiring a line break above them, as in [GitHub flavoured markdown](https://github.github.com/gfm/#example-283).


This markdown:
> ```
> This text comes before the list
> - list item 1
> - list item 2
> ``` 

renders as this HTML:
> ```
> <p>This text comes before the list</p>
> <ul>
> <li>list item 1</li>
> <li>list item 2</li>
> </ul>
> ```

## Installation

`pip install mdx-breakless-lists`

## Usage

```python
from markdown import markdown

html = markdown(text, extensions=['mdx_breakless_lists'])
```
