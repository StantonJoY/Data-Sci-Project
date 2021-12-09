Module(
    body=[
        ImportFrom(
            module='exceptions',
            names=[alias(name='except_orm', asname=None)],
            level=2,
        ),
        ImportFrom(
            module='models',
            names=[
                alias(name='Model', asname=None),
                alias(name='TransientModel', asname=None),
                alias(name='AbstractModel', asname=None),
            ],
            level=2,
        ),
        Assign(
            targets=[Name(id='except_osv', ctx=Store())],
            value=Name(id='except_orm', ctx=Load()),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='osv', ctx=Store())],
            value=Name(id='Model', ctx=Load()),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='osv_memory', ctx=Store())],
            value=Name(id='TransientModel', ctx=Load()),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='osv_abstract', ctx=Store())],
            value=Name(id='AbstractModel', ctx=Load()),
            type_comment=None,
        ),
    ],
    type_ignores=[],
)
