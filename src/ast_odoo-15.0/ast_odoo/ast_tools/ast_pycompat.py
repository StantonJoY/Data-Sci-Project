Module(
    body=[
        Import(
            names=[alias(name='csv', asname=None)],
        ),
        Import(
            names=[alias(name='codecs', asname=None)],
        ),
        Import(
            names=[alias(name='io', asname=None)],
        ),
        Assign(
            targets=[Name(id='_reader', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='codecs', ctx=Load()),
                    attr='getreader',
                    ctx=Load(),
                ),
                args=[Constant(value='utf-8', kind=None)],
                keywords=[],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='_writer', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='codecs', ctx=Load()),
                    attr='getwriter',
                    ctx=Load(),
                ),
                args=[Constant(value='utf-8', kind=None)],
                keywords=[],
            ),
            type_comment=None,
        ),
        FunctionDef(
            name='csv_reader',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='stream', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=arg(arg='params', annotation=None, type_comment=None),
                defaults=[],
            ),
            body=[
                Assert(
                    test=UnaryOp(
                        op=Not(),
                        operand=Call(
                            func=Name(id='isinstance', ctx=Load()),
                            args=[
                                Name(id='stream', ctx=Load()),
                                Attribute(
                                    value=Name(id='io', ctx=Load()),
                                    attr='TextIOBase',
                                    ctx=Load(),
                                ),
                            ],
                            keywords=[],
                        ),
                    ),
                    msg=Constant(value='For cross-compatibility purposes, csv_reader takes a bytes stream', kind=None),
                ),
                Return(
                    value=Call(
                        func=Attribute(
                            value=Name(id='csv', ctx=Load()),
                            attr='reader',
                            ctx=Load(),
                        ),
                        args=[
                            Call(
                                func=Name(id='_reader', ctx=Load()),
                                args=[Name(id='stream', ctx=Load())],
                                keywords=[],
                            ),
                        ],
                        keywords=[
                            keyword(
                                arg=None,
                                value=Name(id='params', ctx=Load()),
                            ),
                        ],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='csv_writer',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='stream', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=arg(arg='params', annotation=None, type_comment=None),
                defaults=[],
            ),
            body=[
                Assert(
                    test=UnaryOp(
                        op=Not(),
                        operand=Call(
                            func=Name(id='isinstance', ctx=Load()),
                            args=[
                                Name(id='stream', ctx=Load()),
                                Attribute(
                                    value=Name(id='io', ctx=Load()),
                                    attr='TextIOBase',
                                    ctx=Load(),
                                ),
                            ],
                            keywords=[],
                        ),
                    ),
                    msg=Constant(value='For cross-compatibility purposes, csv_writer takes a bytes stream', kind=None),
                ),
                Return(
                    value=Call(
                        func=Attribute(
                            value=Name(id='csv', ctx=Load()),
                            attr='writer',
                            ctx=Load(),
                        ),
                        args=[
                            Call(
                                func=Name(id='_writer', ctx=Load()),
                                args=[Name(id='stream', ctx=Load())],
                                keywords=[],
                            ),
                        ],
                        keywords=[
                            keyword(
                                arg=None,
                                value=Name(id='params', ctx=Load()),
                            ),
                        ],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='to_text',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='source', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=" Generates a text value (an instance of text_type) from an arbitrary\n    source.\n\n    * False and None are converted to empty strings\n    * text is passed through\n    * bytes are decoded as UTF-8\n    * rest is textified via the current version's relevant data model method\n    ", kind=None),
                ),
                If(
                    test=BoolOp(
                        op=Or(),
                        values=[
                            Compare(
                                left=Name(id='source', ctx=Load()),
                                ops=[Is()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            Compare(
                                left=Name(id='source', ctx=Load()),
                                ops=[Is()],
                                comparators=[Constant(value=False, kind=None)],
                            ),
                        ],
                    ),
                    body=[
                        Return(
                            value=Constant(value='', kind='u'),
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    test=Call(
                        func=Name(id='isinstance', ctx=Load()),
                        args=[
                            Name(id='source', ctx=Load()),
                            Name(id='bytes', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='source', ctx=Load()),
                                    attr='decode',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='utf-8', kind=None)],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    test=Call(
                        func=Name(id='isinstance', ctx=Load()),
                        args=[
                            Name(id='source', ctx=Load()),
                            Name(id='str', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    body=[
                        Return(
                            value=Name(id='source', ctx=Load()),
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Call(
                        func=Name(id='str', ctx=Load()),
                        args=[Name(id='source', ctx=Load())],
                        keywords=[],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
    ],
    type_ignores=[],
)
