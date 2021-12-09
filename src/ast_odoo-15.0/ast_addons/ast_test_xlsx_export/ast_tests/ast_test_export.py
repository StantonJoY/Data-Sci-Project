Module(
    body=[
        Import(
            names=[alias(name='json', asname=None)],
        ),
        ImportFrom(
            module='datetime',
            names=[alias(name='date', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='unittest.mock',
            names=[alias(name='patch', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[alias(name='http', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests',
            names=[
                alias(name='common', asname=None),
                alias(name='tagged', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.web.controllers.main',
            names=[alias(name='ExportXlsxWriter', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.mail.tests.common',
            names=[alias(name='mail_new_test_user', asname=None)],
            level=0,
        ),
        ClassDef(
            name='XlsxCreatorCase',
            bases=[
                Attribute(
                    value=Name(id='common', ctx=Load()),
                    attr='HttpCase',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='model_name', ctx=Store())],
                    value=Constant(value=False, kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=arg(arg='args', annotation=None, type_comment=None),
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='__init__',
                                    ctx=Load(),
                                ),
                                args=[
                                    Starred(
                                        value=Name(id='args', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg=None,
                                        value=Name(id='kwargs', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='model',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='setUp',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='setUp',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='model',
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='model_name',
                                    ctx=Load(),
                                ),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='mail_new_test_user', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='login',
                                        value=Constant(value='fof', kind=None),
                                    ),
                                    keyword(
                                        arg='password',
                                        value=Constant(value='123456789', kind=None),
                                    ),
                                    keyword(
                                        arg='groups',
                                        value=Constant(value='base.group_user,base.group_allow_export', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='session',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='authenticate',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='fof', kind=None),
                                    Constant(value='123456789', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='worksheet',
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='default_params',
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(
                                keys=[
                                    Constant(value='domain', kind=None),
                                    Constant(value='fields', kind=None),
                                    Constant(value='groupby', kind=None),
                                    Constant(value='ids', kind=None),
                                    Constant(value='import_compat', kind=None),
                                    Constant(value='model', kind=None),
                                ],
                                values=[
                                    List(elts=[], ctx=Load()),
                                    ListComp(
                                        elt=Dict(
                                            keys=[
                                                Constant(value='name', kind=None),
                                                Constant(value='label', kind=None),
                                            ],
                                            values=[
                                                Attribute(
                                                    value=Name(id='field', ctx=Load()),
                                                    attr='name',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Name(id='field', ctx=Load()),
                                                    attr='string',
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='field', ctx=Store()),
                                                iter=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='model',
                                                                ctx=Load(),
                                                            ),
                                                            attr='_fields',
                                                            ctx=Load(),
                                                        ),
                                                        attr='values',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    List(elts=[], ctx=Load()),
                                    Constant(value=False, kind=None),
                                    Constant(value=False, kind=None),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='model',
                                            ctx=Load(),
                                        ),
                                        attr='_name',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_mock_write',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='row', annotation=None, type_comment=None),
                            arg(arg='column', annotation=None, type_comment=None),
                            arg(arg='value', annotation=None, type_comment=None),
                            arg(arg='style', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Subscript(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='worksheet',
                                        ctx=Load(),
                                    ),
                                    slice=Tuple(
                                        elts=[
                                            Name(id='row', ctx=Load()),
                                            Name(id='column', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='str', ctx=Load()),
                                args=[Name(id='value', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='make',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='values', annotation=None, type_comment=None),
                            arg(arg='context', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='model',
                                                ctx=Load(),
                                            ),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg=None,
                                                value=BoolOp(
                                                    op=Or(),
                                                    values=[
                                                        Name(id='context', ctx=Load()),
                                                        Dict(keys=[], values=[]),
                                                    ],
                                                ),
                                            ),
                                        ],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Name(id='values', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='export',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='values', annotation=None, type_comment=None),
                            arg(arg='fields', annotation=None, type_comment=None),
                            arg(arg='params', annotation=None, type_comment=None),
                            arg(arg='context', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            List(elts=[], ctx=Load()),
                            Dict(keys=[], values=[]),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='worksheet',
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='make',
                                    ctx=Load(),
                                ),
                                args=[Name(id='values', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='context',
                                        value=Name(id='context', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='fields', ctx=Load()),
                                    Compare(
                                        left=Constant(value='fields', kind=None),
                                        ops=[NotIn()],
                                        comparators=[Name(id='params', ctx=Load())],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='params', ctx=Load()),
                                            slice=Constant(value='fields', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=ListComp(
                                        elt=Dict(
                                            keys=[
                                                Constant(value='name', kind=None),
                                                Constant(value='label', kind=None),
                                                Constant(value='type', kind=None),
                                            ],
                                            values=[
                                                Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='model',
                                                                ctx=Load(),
                                                            ),
                                                            attr='_fields',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Name(id='f', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                    attr='name',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='model',
                                                                ctx=Load(),
                                                            ),
                                                            attr='_fields',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Name(id='f', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                    attr='string',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='model',
                                                                ctx=Load(),
                                                            ),
                                                            attr='_fields',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Name(id='f', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                    attr='type',
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='f', ctx=Store()),
                                                iter=Name(id='fields', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='patch', ctx=Load()),
                                            attr='object',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='ExportXlsxWriter', ctx=Load()),
                                            Constant(value='write', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_mock_write',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='url_open',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='/web/export/xlsx', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='data',
                                                value=Dict(
                                                    keys=[
                                                        Constant(value='data', kind=None),
                                                        Constant(value='token', kind=None),
                                                        Constant(value='csrf_token', kind=None),
                                                    ],
                                                    values=[
                                                        Call(
                                                            func=Attribute(
                                                                value=Name(id='json', ctx=Load()),
                                                                attr='dumps',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Call(
                                                                    func=Name(id='dict', ctx=Load()),
                                                                    args=[
                                                                        Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='default_params',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                    keywords=[
                                                                        keyword(
                                                                            arg=None,
                                                                            value=Name(id='params', ctx=Load()),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        Constant(value='dummy', kind=None),
                                                        Call(
                                                            func=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='http', ctx=Load()),
                                                                    attr='WebRequest',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='csrf_token',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Name(id='self', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        Return(
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='worksheet',
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='assertExportEqual',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='value', annotation=None, type_comment=None),
                            arg(arg='expected', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        For(
                            target=Name(id='row', ctx=Store()),
                            iter=Call(
                                func=Name(id='range', ctx=Load()),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='expected', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                For(
                                    target=Name(id='column', ctx=Store()),
                                    iter=Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='len', ctx=Load()),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='expected', ctx=Load()),
                                                        slice=Name(id='row', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='cell_value', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='value', ctx=Load()),
                                                    attr='pop',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Tuple(
                                                        elts=[
                                                            Name(id='row', ctx=Load()),
                                                            Name(id='column', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='expected_value', ctx=Store())],
                                            value=Subscript(
                                                value=Subscript(
                                                    value=Name(id='expected', ctx=Load()),
                                                    slice=Name(id='row', ctx=Load()),
                                                    ctx=Load(),
                                                ),
                                                slice=Name(id='column', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='assertEqual',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='cell_value', ctx=Load()),
                                                    Name(id='expected_value', ctx=Load()),
                                                    BinOp(
                                                        left=Constant(value='Cell %s, %s have a wrong value', kind=None),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            elts=[
                                                                Name(id='row', ctx=Load()),
                                                                Name(id='column', ctx=Load()),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='value', ctx=Load()),
                                    Constant(value='There are unexpected cells in the export', kind=None),
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
        ClassDef(
            name='TestGroupedExport',
            bases=[Name(id='XlsxCreatorCase', ctx=Load())],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='model_name', ctx=Store())],
                    value=Constant(value='export.group_operator', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_int_sum_max',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=List(
                                elts=[
                                    Dict(
                                        keys=[
                                            Constant(value='int_sum', kind=None),
                                            Constant(value='int_max', kind=None),
                                        ],
                                        values=[
                                            Constant(value=10, kind=None),
                                            Constant(value=20, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='int_sum', kind=None),
                                            Constant(value='int_max', kind=None),
                                        ],
                                        values=[
                                            Constant(value=10, kind=None),
                                            Constant(value=50, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='int_sum', kind=None),
                                            Constant(value='int_max', kind=None),
                                        ],
                                        values=[
                                            Constant(value=20, kind=None),
                                            Constant(value=30, kind=None),
                                        ],
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='export', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='export',
                                    ctx=Load(),
                                ),
                                args=[Name(id='values', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='fields',
                                        value=List(
                                            elts=[
                                                Constant(value='int_sum', kind=None),
                                                Constant(value='int_max', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='params',
                                        value=Dict(
                                            keys=[Constant(value='groupby', kind=None)],
                                            values=[
                                                List(
                                                    elts=[
                                                        Constant(value='int_sum', kind=None),
                                                        Constant(value='int_max', kind=None),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertExportEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='export', ctx=Load()),
                                    List(
                                        elts=[
                                            List(
                                                elts=[
                                                    Constant(value='Int Sum', kind=None),
                                                    Constant(value='Int Max', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='10 (2)', kind=None),
                                                    Constant(value='50', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='    20 (1)', kind=None),
                                                    Constant(value='20', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='10', kind=None),
                                                    Constant(value='20', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='    50 (1)', kind=None),
                                                    Constant(value='50', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='10', kind=None),
                                                    Constant(value='50', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='20 (1)', kind=None),
                                                    Constant(value='30', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='    30 (1)', kind=None),
                                                    Constant(value='30', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='20', kind=None),
                                                    Constant(value='30', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='export', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='export',
                                    ctx=Load(),
                                ),
                                args=[List(elts=[], ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='fields',
                                        value=List(
                                            elts=[
                                                Constant(value='int_max', kind=None),
                                                Constant(value='int_sum', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='params',
                                        value=Dict(
                                            keys=[Constant(value='groupby', kind=None)],
                                            values=[
                                                List(
                                                    elts=[
                                                        Constant(value='int_sum', kind=None),
                                                        Constant(value='int_max', kind=None),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertExportEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='export', ctx=Load()),
                                    List(
                                        elts=[
                                            List(
                                                elts=[
                                                    Constant(value='Int Max', kind=None),
                                                    Constant(value='Int Sum', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='10 (2)', kind=None),
                                                    Constant(value='20', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='    20 (1)', kind=None),
                                                    Constant(value='10', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='20', kind=None),
                                                    Constant(value='10', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='    50 (1)', kind=None),
                                                    Constant(value='10', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='50', kind=None),
                                                    Constant(value='10', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='20 (1)', kind=None),
                                                    Constant(value='20', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='    30 (1)', kind=None),
                                                    Constant(value='20', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='30', kind=None),
                                                    Constant(value='20', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
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
                FunctionDef(
                    name='test_float_min',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=List(
                                elts=[
                                    Dict(
                                        keys=[
                                            Constant(value='int_sum', kind=None),
                                            Constant(value='float_min', kind=None),
                                        ],
                                        values=[
                                            Constant(value=10, kind=None),
                                            Constant(value=111.0, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='int_sum', kind=None),
                                            Constant(value='float_min', kind=None),
                                        ],
                                        values=[
                                            Constant(value=10, kind=None),
                                            Constant(value=222.0, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='int_sum', kind=None),
                                            Constant(value='float_min', kind=None),
                                        ],
                                        values=[
                                            Constant(value=20, kind=None),
                                            Constant(value=333.0, kind=None),
                                        ],
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='export', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='export',
                                    ctx=Load(),
                                ),
                                args=[Name(id='values', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='fields',
                                        value=List(
                                            elts=[
                                                Constant(value='int_sum', kind=None),
                                                Constant(value='float_min', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='params',
                                        value=Dict(
                                            keys=[Constant(value='groupby', kind=None)],
                                            values=[
                                                List(
                                                    elts=[
                                                        Constant(value='int_sum', kind=None),
                                                        Constant(value='float_min', kind=None),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertExportEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='export', ctx=Load()),
                                    List(
                                        elts=[
                                            List(
                                                elts=[
                                                    Constant(value='Int Sum', kind=None),
                                                    Constant(value='Float Min', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='10 (2)', kind=None),
                                                    Constant(value='111.00', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='    111.0 (1)', kind=None),
                                                    Constant(value='111.00', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='10', kind=None),
                                                    Constant(value='111.0', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='    222.0 (1)', kind=None),
                                                    Constant(value='222.00', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='10', kind=None),
                                                    Constant(value='222.0', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='20 (1)', kind=None),
                                                    Constant(value='333.00', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='    333.0 (1)', kind=None),
                                                    Constant(value='333.00', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='20', kind=None),
                                                    Constant(value='333.0', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
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
                FunctionDef(
                    name='test_float_avg',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=List(
                                elts=[
                                    Dict(
                                        keys=[
                                            Constant(value='int_sum', kind=None),
                                            Constant(value='float_avg', kind=None),
                                        ],
                                        values=[
                                            Constant(value=10, kind=None),
                                            Constant(value=100.0, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='int_sum', kind=None),
                                            Constant(value='float_avg', kind=None),
                                        ],
                                        values=[
                                            Constant(value=10, kind=None),
                                            Constant(value=200.0, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='int_sum', kind=None),
                                            Constant(value='float_avg', kind=None),
                                        ],
                                        values=[
                                            Constant(value=20, kind=None),
                                            Constant(value=300.0, kind=None),
                                        ],
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='export', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='export',
                                    ctx=Load(),
                                ),
                                args=[Name(id='values', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='fields',
                                        value=List(
                                            elts=[
                                                Constant(value='int_sum', kind=None),
                                                Constant(value='float_avg', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='params',
                                        value=Dict(
                                            keys=[Constant(value='groupby', kind=None)],
                                            values=[
                                                List(
                                                    elts=[
                                                        Constant(value='int_sum', kind=None),
                                                        Constant(value='float_avg', kind=None),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertExportEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='export', ctx=Load()),
                                    List(
                                        elts=[
                                            List(
                                                elts=[
                                                    Constant(value='Int Sum', kind=None),
                                                    Constant(value='Float Avg', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='10 (2)', kind=None),
                                                    Constant(value='150.00', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='    100.0 (1)', kind=None),
                                                    Constant(value='100.00', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='10', kind=None),
                                                    Constant(value='100.0', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='    200.0 (1)', kind=None),
                                                    Constant(value='200.00', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='10', kind=None),
                                                    Constant(value='200.0', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='20 (1)', kind=None),
                                                    Constant(value='300.00', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='    300.0 (1)', kind=None),
                                                    Constant(value='300.00', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='20', kind=None),
                                                    Constant(value='300.0', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
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
                FunctionDef(
                    name='test_float_avg_nested',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' With more than one nested level (avg aggregation) ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=List(
                                elts=[
                                    Dict(
                                        keys=[
                                            Constant(value='int_sum', kind=None),
                                            Constant(value='int_max', kind=None),
                                            Constant(value='float_avg', kind=None),
                                        ],
                                        values=[
                                            Constant(value=10, kind=None),
                                            Constant(value=30, kind=None),
                                            Constant(value=100.0, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='int_sum', kind=None),
                                            Constant(value='int_max', kind=None),
                                            Constant(value='float_avg', kind=None),
                                        ],
                                        values=[
                                            Constant(value=10, kind=None),
                                            Constant(value=30, kind=None),
                                            Constant(value=200.0, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='int_sum', kind=None),
                                            Constant(value='int_max', kind=None),
                                            Constant(value='float_avg', kind=None),
                                        ],
                                        values=[
                                            Constant(value=10, kind=None),
                                            Constant(value=20, kind=None),
                                            Constant(value=600.0, kind=None),
                                        ],
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='export', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='export',
                                    ctx=Load(),
                                ),
                                args=[Name(id='values', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='fields',
                                        value=List(
                                            elts=[
                                                Constant(value='int_sum', kind=None),
                                                Constant(value='float_avg', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='params',
                                        value=Dict(
                                            keys=[Constant(value='groupby', kind=None)],
                                            values=[
                                                List(
                                                    elts=[
                                                        Constant(value='int_sum', kind=None),
                                                        Constant(value='int_max', kind=None),
                                                        Constant(value='float_avg', kind=None),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertExportEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='export', ctx=Load()),
                                    List(
                                        elts=[
                                            List(
                                                elts=[
                                                    Constant(value='Int Sum', kind=None),
                                                    Constant(value='Float Avg', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='10 (3)', kind=None),
                                                    Constant(value='300.00', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='    20 (1)', kind=None),
                                                    Constant(value='600.00', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='        600.0 (1)', kind=None),
                                                    Constant(value='600.00', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='10', kind=None),
                                                    Constant(value='600.0', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='    30 (2)', kind=None),
                                                    Constant(value='150.00', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='        100.0 (1)', kind=None),
                                                    Constant(value='100.00', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='10', kind=None),
                                                    Constant(value='100.0', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='        200.0 (1)', kind=None),
                                                    Constant(value='200.00', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='10', kind=None),
                                                    Constant(value='200.0', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
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
                FunctionDef(
                    name='test_float_avg_nested_no_value',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' With more than one nested level (avg aggregation is done on 0, not False) ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=List(
                                elts=[
                                    Dict(
                                        keys=[
                                            Constant(value='int_sum', kind=None),
                                            Constant(value='int_max', kind=None),
                                            Constant(value='float_avg', kind=None),
                                        ],
                                        values=[
                                            Constant(value=10, kind=None),
                                            Constant(value=20, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='int_sum', kind=None),
                                            Constant(value='int_max', kind=None),
                                            Constant(value='float_avg', kind=None),
                                        ],
                                        values=[
                                            Constant(value=10, kind=None),
                                            Constant(value=30, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='int_sum', kind=None),
                                            Constant(value='int_max', kind=None),
                                            Constant(value='float_avg', kind=None),
                                        ],
                                        values=[
                                            Constant(value=10, kind=None),
                                            Constant(value=30, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='export', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='export',
                                    ctx=Load(),
                                ),
                                args=[Name(id='values', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='fields',
                                        value=List(
                                            elts=[
                                                Constant(value='int_sum', kind=None),
                                                Constant(value='float_avg', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='params',
                                        value=Dict(
                                            keys=[Constant(value='groupby', kind=None)],
                                            values=[
                                                List(
                                                    elts=[
                                                        Constant(value='int_sum', kind=None),
                                                        Constant(value='int_max', kind=None),
                                                        Constant(value='float_avg', kind=None),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertExportEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='export', ctx=Load()),
                                    List(
                                        elts=[
                                            List(
                                                elts=[
                                                    Constant(value='Int Sum', kind=None),
                                                    Constant(value='Float Avg', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='10 (3)', kind=None),
                                                    Constant(value='0.00', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='    20 (1)', kind=None),
                                                    Constant(value='0.00', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='        Undefined (1)', kind=None),
                                                    Constant(value='0.00', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='10', kind=None),
                                                    Constant(value='0.0', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='    30 (2)', kind=None),
                                                    Constant(value='0.00', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='        Undefined (2)', kind=None),
                                                    Constant(value='0.00', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='10', kind=None),
                                                    Constant(value='0.0', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='10', kind=None),
                                                    Constant(value='0.0', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
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
                FunctionDef(
                    name='test_date_max',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=List(
                                elts=[
                                    Dict(
                                        keys=[
                                            Constant(value='int_sum', kind=None),
                                            Constant(value='date_max', kind=None),
                                        ],
                                        values=[
                                            Constant(value=10, kind=None),
                                            Call(
                                                func=Name(id='date', ctx=Load()),
                                                args=[
                                                    Constant(value=2019, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=1, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='int_sum', kind=None),
                                            Constant(value='date_max', kind=None),
                                        ],
                                        values=[
                                            Constant(value=10, kind=None),
                                            Call(
                                                func=Name(id='date', ctx=Load()),
                                                args=[
                                                    Constant(value=2000, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=1, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='int_sum', kind=None),
                                            Constant(value='date_max', kind=None),
                                        ],
                                        values=[
                                            Constant(value=20, kind=None),
                                            Call(
                                                func=Name(id='date', ctx=Load()),
                                                args=[
                                                    Constant(value=1980, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=1, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='export', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='export',
                                    ctx=Load(),
                                ),
                                args=[Name(id='values', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='fields',
                                        value=List(
                                            elts=[
                                                Constant(value='int_sum', kind=None),
                                                Constant(value='date_max', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='params',
                                        value=Dict(
                                            keys=[Constant(value='groupby', kind=None)],
                                            values=[
                                                List(
                                                    elts=[
                                                        Constant(value='int_sum', kind=None),
                                                        Constant(value='date_max:month', kind=None),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertExportEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='export', ctx=Load()),
                                    List(
                                        elts=[
                                            List(
                                                elts=[
                                                    Constant(value='Int Sum', kind=None),
                                                    Constant(value='Date Max', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='10 (2)', kind=None),
                                                    Constant(value='2019-01-01', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='    January 2000 (1)', kind=None),
                                                    Constant(value='2000-01-01', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='10', kind=None),
                                                    Constant(value='2000-01-01', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='    January 2019 (1)', kind=None),
                                                    Constant(value='2019-01-01', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='10', kind=None),
                                                    Constant(value='2019-01-01', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='20 (1)', kind=None),
                                                    Constant(value='1980-01-01', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='    January 1980 (1)', kind=None),
                                                    Constant(value='1980-01-01', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='20', kind=None),
                                                    Constant(value='1980-01-01', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
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
                FunctionDef(
                    name='test_bool_and',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=List(
                                elts=[
                                    Dict(
                                        keys=[
                                            Constant(value='int_sum', kind=None),
                                            Constant(value='bool_and', kind=None),
                                        ],
                                        values=[
                                            Constant(value=10, kind=None),
                                            Constant(value=True, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='int_sum', kind=None),
                                            Constant(value='bool_and', kind=None),
                                        ],
                                        values=[
                                            Constant(value=10, kind=None),
                                            Constant(value=True, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='int_sum', kind=None),
                                            Constant(value='bool_and', kind=None),
                                        ],
                                        values=[
                                            Constant(value=20, kind=None),
                                            Constant(value=True, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='int_sum', kind=None),
                                            Constant(value='bool_and', kind=None),
                                        ],
                                        values=[
                                            Constant(value=20, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='export', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='export',
                                    ctx=Load(),
                                ),
                                args=[Name(id='values', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='fields',
                                        value=List(
                                            elts=[
                                                Constant(value='int_sum', kind=None),
                                                Constant(value='bool_and', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='params',
                                        value=Dict(
                                            keys=[Constant(value='groupby', kind=None)],
                                            values=[
                                                List(
                                                    elts=[
                                                        Constant(value='int_sum', kind=None),
                                                        Constant(value='bool_and', kind=None),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertExportEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='export', ctx=Load()),
                                    List(
                                        elts=[
                                            List(
                                                elts=[
                                                    Constant(value='Int Sum', kind=None),
                                                    Constant(value='Bool And', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='10 (2)', kind=None),
                                                    Constant(value='True', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='    True (2)', kind=None),
                                                    Constant(value='True', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='10', kind=None),
                                                    Constant(value='True', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='10', kind=None),
                                                    Constant(value='True', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='20 (2)', kind=None),
                                                    Constant(value='False', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='    False (1)', kind=None),
                                                    Constant(value='False', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='20', kind=None),
                                                    Constant(value='False', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='    True (1)', kind=None),
                                                    Constant(value='True', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='20', kind=None),
                                                    Constant(value='True', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
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
                FunctionDef(
                    name='test_bool_or',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=List(
                                elts=[
                                    Dict(
                                        keys=[
                                            Constant(value='int_sum', kind=None),
                                            Constant(value='bool_or', kind=None),
                                        ],
                                        values=[
                                            Constant(value=10, kind=None),
                                            Constant(value=True, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='int_sum', kind=None),
                                            Constant(value='bool_or', kind=None),
                                        ],
                                        values=[
                                            Constant(value=10, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='int_sum', kind=None),
                                            Constant(value='bool_or', kind=None),
                                        ],
                                        values=[
                                            Constant(value=20, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='int_sum', kind=None),
                                            Constant(value='bool_or', kind=None),
                                        ],
                                        values=[
                                            Constant(value=20, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='export', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='export',
                                    ctx=Load(),
                                ),
                                args=[Name(id='values', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='fields',
                                        value=List(
                                            elts=[
                                                Constant(value='int_sum', kind=None),
                                                Constant(value='bool_or', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='params',
                                        value=Dict(
                                            keys=[Constant(value='groupby', kind=None)],
                                            values=[
                                                List(
                                                    elts=[
                                                        Constant(value='int_sum', kind=None),
                                                        Constant(value='bool_or', kind=None),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertExportEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='export', ctx=Load()),
                                    List(
                                        elts=[
                                            List(
                                                elts=[
                                                    Constant(value='Int Sum', kind=None),
                                                    Constant(value='Bool Or', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='10 (2)', kind=None),
                                                    Constant(value='True', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='    False (1)', kind=None),
                                                    Constant(value='False', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='10', kind=None),
                                                    Constant(value='False', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='    True (1)', kind=None),
                                                    Constant(value='True', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='10', kind=None),
                                                    Constant(value='True', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='20 (2)', kind=None),
                                                    Constant(value='False', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='    False (2)', kind=None),
                                                    Constant(value='False', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='20', kind=None),
                                                    Constant(value='False', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='20', kind=None),
                                                    Constant(value='False', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
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
                FunctionDef(
                    name='test_many2one',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=List(
                                elts=[
                                    Dict(
                                        keys=[
                                            Constant(value='int_sum', kind=None),
                                            Constant(value='many2one', kind=None),
                                        ],
                                        values=[
                                            Constant(value=10, kind=None),
                                            Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='export.integer', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='create',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Dict(keys=[], values=[])],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Dict(
                                        keys=[Constant(value='int_sum', kind=None)],
                                        values=[Constant(value=10, kind=None)],
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='export', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='export',
                                    ctx=Load(),
                                ),
                                args=[Name(id='values', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='fields',
                                        value=List(
                                            elts=[
                                                Constant(value='int_sum', kind=None),
                                                Constant(value='many2one', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='params',
                                        value=Dict(
                                            keys=[Constant(value='groupby', kind=None)],
                                            values=[
                                                List(
                                                    elts=[
                                                        Constant(value='int_sum', kind=None),
                                                        Constant(value='many2one', kind=None),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertExportEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='export', ctx=Load()),
                                    List(
                                        elts=[
                                            List(
                                                elts=[
                                                    Constant(value='Int Sum', kind=None),
                                                    Constant(value='Many2One', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='10 (2)', kind=None),
                                                    Constant(value='', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='    export.integer:4 (1)', kind=None),
                                                    Constant(value='', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='10', kind=None),
                                                    Constant(value='export.integer:4', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='    Undefined (1)', kind=None),
                                                    Constant(value='', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='10', kind=None),
                                                    Constant(value='False', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
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
                FunctionDef(
                    name='test_nested_records',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value="\n        aggregated values currently not supported for nested record export, but it should not crash\n        e.g. export 'many2one/const'\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=List(
                                elts=[
                                    Dict(
                                        keys=[
                                            Constant(value='int_sum', kind=None),
                                            Constant(value='date_max', kind=None),
                                            Constant(value='many2one', kind=None),
                                        ],
                                        values=[
                                            Constant(value=10, kind=None),
                                            Call(
                                                func=Name(id='date', ctx=Load()),
                                                args=[
                                                    Constant(value=2019, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=1, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='export.integer', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='create',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Dict(keys=[], values=[])],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='int_sum', kind=None),
                                            Constant(value='date_max', kind=None),
                                            Constant(value='many2one', kind=None),
                                        ],
                                        values=[
                                            Constant(value=10, kind=None),
                                            Call(
                                                func=Name(id='date', ctx=Load()),
                                                args=[
                                                    Constant(value=2000, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=1, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='export.integer', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='create',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Dict(keys=[], values=[])],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='export', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='export',
                                    ctx=Load(),
                                ),
                                args=[Name(id='values', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='params',
                                        value=Dict(
                                            keys=[
                                                Constant(value='groupby', kind=None),
                                                Constant(value='fields', kind=None),
                                            ],
                                            values=[
                                                List(
                                                    elts=[
                                                        Constant(value='int_sum', kind=None),
                                                        Constant(value='date_max:month', kind=None),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                                List(
                                                    elts=[
                                                        Dict(
                                                            keys=[
                                                                Constant(value='name', kind=None),
                                                                Constant(value='label', kind=None),
                                                            ],
                                                            values=[
                                                                Constant(value='int_sum', kind=None),
                                                                Constant(value='Int Sum', kind=None),
                                                            ],
                                                        ),
                                                        Dict(
                                                            keys=[
                                                                Constant(value='name', kind=None),
                                                                Constant(value='label', kind=None),
                                                            ],
                                                            values=[
                                                                Constant(value='date_max', kind=None),
                                                                Constant(value='Date Max', kind=None),
                                                            ],
                                                        ),
                                                        Dict(
                                                            keys=[
                                                                Constant(value='name', kind=None),
                                                                Constant(value='label', kind=None),
                                                            ],
                                                            values=[
                                                                Constant(value='many2one/value', kind=None),
                                                                Constant(value='Many2One/Value', kind=None),
                                                            ],
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertExportEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='export', ctx=Load()),
                                    List(
                                        elts=[
                                            List(
                                                elts=[
                                                    Constant(value='Int Sum', kind=None),
                                                    Constant(value='Date Max', kind=None),
                                                    Constant(value='Many2One/Value', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='10 (2)', kind=None),
                                                    Constant(value='2019-01-01', kind=None),
                                                    Constant(value='', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='    January 2000 (1)', kind=None),
                                                    Constant(value='2000-01-01', kind=None),
                                                    Constant(value='', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='10', kind=None),
                                                    Constant(value='2000-01-01', kind=None),
                                                    Constant(value='4', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='    January 2019 (1)', kind=None),
                                                    Constant(value='2019-01-01', kind=None),
                                                    Constant(value='', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='10', kind=None),
                                                    Constant(value='2019-01-01', kind=None),
                                                    Constant(value='4', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
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
                FunctionDef(
                    name='test_one2many',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=List(
                                elts=[
                                    Dict(
                                        keys=[
                                            Constant(value='int_sum', kind=None),
                                            Constant(value='one2many', kind=None),
                                        ],
                                        values=[
                                            Constant(value=10, kind=None),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[Constant(value='value', kind=None)],
                                                                values=[Constant(value=8, kind=None)],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[Constant(value='value', kind=None)],
                                                                values=[Constant(value=9, kind=None)],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='export', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='export',
                                    ctx=Load(),
                                ),
                                args=[Name(id='values', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='params',
                                        value=Dict(
                                            keys=[
                                                Constant(value='groupby', kind=None),
                                                Constant(value='fields', kind=None),
                                            ],
                                            values=[
                                                List(
                                                    elts=[Constant(value='int_sum', kind=None)],
                                                    ctx=Load(),
                                                ),
                                                List(
                                                    elts=[
                                                        Dict(
                                                            keys=[
                                                                Constant(value='name', kind=None),
                                                                Constant(value='label', kind=None),
                                                            ],
                                                            values=[
                                                                Constant(value='int_sum', kind=None),
                                                                Constant(value='Int Sum', kind=None),
                                                            ],
                                                        ),
                                                        Dict(
                                                            keys=[
                                                                Constant(value='name', kind=None),
                                                                Constant(value='label', kind=None),
                                                            ],
                                                            values=[
                                                                Constant(value='one2many/value', kind=None),
                                                                Constant(value='One2many/Value', kind=None),
                                                            ],
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertExportEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='export', ctx=Load()),
                                    List(
                                        elts=[
                                            List(
                                                elts=[
                                                    Constant(value='Int Sum', kind=None),
                                                    Constant(value='One2many/Value', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='10 (1)', kind=None),
                                                    Constant(value='', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='10', kind=None),
                                                    Constant(value='8', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='', kind=None),
                                                    Constant(value='9', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
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
                FunctionDef(
                    name='test_unset_date_values',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=List(
                                elts=[
                                    Dict(
                                        keys=[
                                            Constant(value='int_sum', kind=None),
                                            Constant(value='date_max', kind=None),
                                        ],
                                        values=[
                                            Constant(value=10, kind=None),
                                            Call(
                                                func=Name(id='date', ctx=Load()),
                                                args=[
                                                    Constant(value=2019, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=1, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='int_sum', kind=None),
                                            Constant(value='date_max', kind=None),
                                        ],
                                        values=[
                                            Constant(value=10, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='export', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='export',
                                    ctx=Load(),
                                ),
                                args=[Name(id='values', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='fields',
                                        value=List(
                                            elts=[
                                                Constant(value='int_sum', kind=None),
                                                Constant(value='date_max', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='params',
                                        value=Dict(
                                            keys=[Constant(value='groupby', kind=None)],
                                            values=[
                                                List(
                                                    elts=[
                                                        Constant(value='int_sum', kind=None),
                                                        Constant(value='date_max:month', kind=None),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertExportEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='export', ctx=Load()),
                                    List(
                                        elts=[
                                            List(
                                                elts=[
                                                    Constant(value='Int Sum', kind=None),
                                                    Constant(value='Date Max', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='10 (2)', kind=None),
                                                    Constant(value='2019-01-01', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='    January 2019 (1)', kind=None),
                                                    Constant(value='2019-01-01', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='10', kind=None),
                                                    Constant(value='2019-01-01', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='    Undefined (1)', kind=None),
                                                    Constant(value='', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='10', kind=None),
                                                    Constant(value='', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
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
                FunctionDef(
                    name='test_float_representation',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='currency', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='res.currency', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='symbol', kind=None),
                                            Constant(value='rounding', kind=None),
                                            Constant(value='decimal_places', kind=None),
                                        ],
                                        values=[
                                            Constant(value='bottlecap', kind=None),
                                            Constant(value='b', kind=None),
                                            Constant(value=0.001, kind=None),
                                            Constant(value=3, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=List(
                                elts=[
                                    Dict(
                                        keys=[
                                            Constant(value='int_sum', kind=None),
                                            Constant(value='currency_id', kind=None),
                                            Constant(value='float_monetary', kind=None),
                                        ],
                                        values=[
                                            Constant(value=1, kind=None),
                                            Attribute(
                                                value=Name(id='currency', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=60739.2000000004, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='int_sum', kind=None),
                                            Constant(value='currency_id', kind=None),
                                            Constant(value='float_monetary', kind=None),
                                        ],
                                        values=[
                                            Constant(value=2, kind=None),
                                            Attribute(
                                                value=Name(id='currency', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=2.0, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='int_sum', kind=None),
                                            Constant(value='currency_id', kind=None),
                                            Constant(value='float_monetary', kind=None),
                                        ],
                                        values=[
                                            Constant(value=3, kind=None),
                                            Attribute(
                                                value=Name(id='currency', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=999.9995999, kind=None),
                                        ],
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='export', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='export',
                                    ctx=Load(),
                                ),
                                args=[Name(id='values', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='fields',
                                        value=List(
                                            elts=[
                                                Constant(value='int_sum', kind=None),
                                                Constant(value='float_monetary', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='params',
                                        value=Dict(
                                            keys=[Constant(value='groupby', kind=None)],
                                            values=[
                                                List(
                                                    elts=[
                                                        Constant(value='int_sum', kind=None),
                                                        Constant(value='float_monetary', kind=None),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertExportEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='export', ctx=Load()),
                                    List(
                                        elts=[
                                            List(
                                                elts=[
                                                    Constant(value='Int Sum', kind=None),
                                                    Constant(value='Float Monetary', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='1 (1)', kind=None),
                                                    Constant(value='60739.200', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='    60739.2 (1)', kind=None),
                                                    Constant(value='60739.200', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='1', kind=None),
                                                    Constant(value='60739.2', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='2 (1)', kind=None),
                                                    Constant(value='2.000', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='    2.0 (1)', kind=None),
                                                    Constant(value='2.000', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='2', kind=None),
                                                    Constant(value='2.0', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='3 (1)', kind=None),
                                                    Constant(value='1000.000', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='    1000.0 (1)', kind=None),
                                                    Constant(value='1000.000', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='3', kind=None),
                                                    Constant(value='1000.0', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
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
            decorator_list=[
                Call(
                    func=Name(id='tagged', ctx=Load()),
                    args=[
                        Constant(value='-at_install', kind=None),
                        Constant(value='post_install', kind=None),
                    ],
                    keywords=[],
                ),
            ],
        ),
    ],
    type_ignores=[],
)
