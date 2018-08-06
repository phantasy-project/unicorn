# Manage unicorn data

## For xlsx file:

1. `fn_templates`: function templates
2. `fn_egroups`: groups of elements
3. `fn_data`: x and y data for curve
4. `generate_data.py`:
    - Import function template, data and groups
    - Create for-loop to iterate all elements with defined parameters
    - Run `generate_data.py` to generate `.xlsx` file (adjust filename inside)

## For UNICORN web application:

0. Get the generated xlsx file ready
1. Run `fn-push3 --url <UNICORN service address> <xlsx data file>`
