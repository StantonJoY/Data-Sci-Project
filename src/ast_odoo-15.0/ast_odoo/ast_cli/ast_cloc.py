Module(
    body=[
        Import(
            names=[alias(name='argparse', asname=None)],
        ),
        Import(
            names=[alias(name='os', asname=None)],
        ),
        Import(
            names=[alias(name='sys', asname=None)],
        ),
        Import(
            names=[alias(name='textwrap', asname=None)],
        ),
        ImportFrom(
            module='odoo.tools',
            names=[
                alias(name='cloc', asname=None),
                alias(name='config', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module=None,
            names=[alias(name='Command', asname=None)],
            level=1,
        ),
        ClassDef(
            name='Cloc',
            bases=[Name(id='Command', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value='    Odoo cloc is a tool to count the number of relevant lines written in\n    Python, Javascript or XML. This can be used as rough metric for pricing\n    maintenance of customizations.\n\n    It has two modes of operation, either by providing a path:\n\n        odoo-bin cloc -p module_path\n\n    Or by providing the name of a database:\n\n        odoo-bin cloc --addons-path=dirs -d database\n\n    In the latter mode, only the custom code is accounted for.\n    ', kind=None),
                ),
                FunctionDef(
                    name='run',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='args', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='parser', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='argparse', ctx=Load()),
                                    attr='ArgumentParser',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='prog',
                                        value=BinOp(
                                            left=Constant(value='%s cloc', kind=None),
                                            op=Mod(),
                                            right=Subscript(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='sys', ctx=Load()),
                                                                attr='argv',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='split',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Attribute(
                                                            value=Attribute(
                                                                value=Name(id='os', ctx=Load()),
                                                                attr='path',
                                                                ctx=Load(),
                                                            ),
                                                            attr='sep',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                slice=UnaryOp(
                                                    op=USub(),
                                                    operand=Constant(value=1, kind=None),
                                                ),
                                                ctx=Load(),
                                            ),
                                        ),
                                    ),
                                    keyword(
                                        arg='description',
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='textwrap', ctx=Load()),
                                                attr='dedent',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='__doc__',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                    keyword(
                                        arg='formatter_class',
                                        value=Attribute(
                                            value=Name(id='argparse', ctx=Load()),
                                            attr='RawDescriptionHelpFormatter',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='parser', ctx=Load()),
                                    attr='add_argument',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='--database', kind=None),
                                    Constant(value='-d', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='dest',
                                        value=Constant(value='database', kind=None),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=Constant(value='Database name', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='parser', ctx=Load()),
                                    attr='add_argument',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='--path', kind=None),
                                    Constant(value='-p', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='action',
                                        value=Constant(value='append', kind=None),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=Constant(value='File or directory path', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='parser', ctx=Load()),
                                    attr='add_argument',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='--verbose', kind=None),
                                    Constant(value='-v', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='action',
                                        value=Constant(value='count', kind=None),
                                    ),
                                    keyword(
                                        arg='default',
                                        value=Constant(value=0, kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='opt', ctx=Store()),
                                        Name(id='unknown', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='parser', ctx=Load()),
                                    attr='parse_known_args',
                                    ctx=Load(),
                                ),
                                args=[Name(id='args', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='opt', ctx=Load()),
                                            attr='database',
                                            ctx=Load(),
                                        ),
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='opt', ctx=Load()),
                                            attr='path',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='parser', ctx=Load()),
                                            attr='print_help',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='sys', ctx=Load()),
                                            attr='exit',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='c', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cloc', ctx=Load()),
                                    attr='Cloc',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='opt', ctx=Load()),
                                attr='database',
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='config', ctx=Load()),
                                            attr='parse_config',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=List(
                                                    elts=[
                                                        Constant(value='-d', kind=None),
                                                        Attribute(
                                                            value=Name(id='opt', ctx=Load()),
                                                            attr='database',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                                op=Add(),
                                                right=Name(id='unknown', ctx=Load()),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='c', ctx=Load()),
                                            attr='count_database',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='opt', ctx=Load()),
                                                attr='database',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='opt', ctx=Load()),
                                attr='path',
                                ctx=Load(),
                            ),
                            body=[
                                For(
                                    target=Name(id='i', ctx=Store()),
                                    iter=Attribute(
                                        value=Name(id='opt', ctx=Load()),
                                        attr='path',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='c', ctx=Load()),
                                                    attr='count_path',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='i', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='c', ctx=Load()),
                                    attr='report',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='opt', ctx=Load()),
                                        attr='verbose',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
