Module(
    body=[
        Try(
            body=[
                ImportFrom(
                    module='xlrd',
                    names=[alias(name='xlsx', asname=None)],
                    level=0,
                ),
            ],
            handlers=[
                ExceptHandler(
                    type=Name(id='ImportError', ctx=Load()),
                    name=None,
                    body=[Pass()],
                ),
            ],
            orelse=[
                ImportFrom(
                    module='lxml',
                    names=[alias(name='etree', asname=None)],
                    level=0,
                ),
                Assign(
                    targets=[
                        Attribute(
                            value=Name(id='xlsx', ctx=Load()),
                            attr='ET',
                            ctx=Store(),
                        ),
                    ],
                    value=Name(id='etree', ctx=Load()),
                    type_comment=None,
                ),
                Assign(
                    targets=[
                        Attribute(
                            value=Name(id='xlsx', ctx=Load()),
                            attr='ET_has_iterparse',
                            ctx=Store(),
                        ),
                    ],
                    value=Constant(value=True, kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[
                        Attribute(
                            value=Name(id='xlsx', ctx=Load()),
                            attr='Element_has_iter',
                            ctx=Store(),
                        ),
                    ],
                    value=Constant(value=True, kind=None),
                    type_comment=None,
                ),
            ],
            finalbody=[],
        ),
    ],
    type_ignores=[],
)
