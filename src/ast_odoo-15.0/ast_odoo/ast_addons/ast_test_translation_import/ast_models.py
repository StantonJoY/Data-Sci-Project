Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='models', asname=None),
                alias(name='fields', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='m',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='TransientModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' A model to provide source strings. ', kind=None),
                ),
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='test.translation.import', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Test: Translation Import', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='name', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='1XBUO5PUYH2RYZSA1FTLRYS8SPCNU1UYXMEYMM25ASV7JC2KTJZQESZYRV9L8CGB', kind=None)],
                        keywords=[
                            keyword(
                                arg='size',
                                value=Constant(value=32, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Efgh', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='other_name', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Test translation with two code type and model', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='import_type', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[
                            List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='foo', kind=None),
                                            Constant(value='Foo Import Type', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='bar', kind=None),
                                            Constant(value='Bar Import Type', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Expr(
                    value=Call(
                        func=Name(id='_', ctx=Load()),
                        args=[Constant(value='Ijkl', kind=None)],
                        keywords=[],
                    ),
                ),
                Expr(
                    value=Call(
                        func=Name(id='_', ctx=Load()),
                        args=[Constant(value='1XBUO5PUYH2RYZSA1FTLRYS8SPCNU1UYXMEYMM25ASV7JC2KTJZQESZYRV9L8CGB', kind=None)],
                        keywords=[],
                    ),
                ),
                Expr(
                    value=Call(
                        func=Name(id='_', ctx=Load()),
                        args=[Constant(value='Klingon', kind=None)],
                        keywords=[],
                    ),
                ),
                Expr(
                    value=Call(
                        func=Name(id='_', ctx=Load()),
                        args=[Constant(value='Accounting', kind=None)],
                        keywords=[],
                    ),
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
