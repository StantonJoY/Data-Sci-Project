Module(
    body=[
        Import(
            names=[alias(name='dateutil.relativedelta', asname='relativedelta')],
        ),
        Import(
            names=[alias(name='functools', asname=None)],
        ),
        Import(
            names=[alias(name='re', asname=None)],
        ),
        ImportFrom(
            module='markupsafe',
            names=[alias(name='Markup', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='werkzeug',
            names=[alias(name='urls', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[alias(name='safe_eval', asname=None)],
            level=0,
        ),
        Assign(
            targets=[Name(id='INLINE_TEMPLATE_REGEX', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='re', ctx=Load()),
                    attr='compile',
                    ctx=Load(),
                ),
                args=[Constant(value='\\{\\{(.+?)\\}\\}', kind=None)],
                keywords=[],
            ),
            type_comment=None,
        ),
        FunctionDef(
            name='relativedelta_proxy',
            args=arguments(
                posonlyargs=[],
                args=[],
                vararg=arg(arg='args', annotation=None, type_comment=None),
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                defaults=[],
            ),
            body=[
                Return(
                    value=Call(
                        func=Attribute(
                            value=Name(id='relativedelta', ctx=Load()),
                            attr='relativedelta',
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
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='template_env_globals', ctx=Store())],
            value=Dict(
                keys=[
                    Constant(value='str', kind=None),
                    Constant(value='quote', kind=None),
                    Constant(value='urlencode', kind=None),
                    Constant(value='datetime', kind=None),
                    Constant(value='len', kind=None),
                    Constant(value='abs', kind=None),
                    Constant(value='min', kind=None),
                    Constant(value='max', kind=None),
                    Constant(value='sum', kind=None),
                    Constant(value='filter', kind=None),
                    Constant(value='reduce', kind=None),
                    Constant(value='map', kind=None),
                    Constant(value='relativedelta', kind=None),
                    Constant(value='round', kind=None),
                    Constant(value='hasattr', kind=None),
                ],
                values=[
                    Name(id='str', ctx=Load()),
                    Attribute(
                        value=Name(id='urls', ctx=Load()),
                        attr='url_quote',
                        ctx=Load(),
                    ),
                    Attribute(
                        value=Name(id='urls', ctx=Load()),
                        attr='url_encode',
                        ctx=Load(),
                    ),
                    Attribute(
                        value=Name(id='safe_eval', ctx=Load()),
                        attr='datetime',
                        ctx=Load(),
                    ),
                    Name(id='len', ctx=Load()),
                    Name(id='abs', ctx=Load()),
                    Name(id='min', ctx=Load()),
                    Name(id='max', ctx=Load()),
                    Name(id='sum', ctx=Load()),
                    Name(id='filter', ctx=Load()),
                    Attribute(
                        value=Name(id='functools', ctx=Load()),
                        attr='reduce',
                        ctx=Load(),
                    ),
                    Name(id='map', ctx=Load()),
                    Attribute(
                        value=Name(id='relativedelta', ctx=Load()),
                        attr='relativedelta',
                        ctx=Load(),
                    ),
                    Name(id='round', ctx=Load()),
                    Name(id='hasattr', ctx=Load()),
                ],
            ),
            type_comment=None,
        ),
        FunctionDef(
            name='parse_inline_template',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='text', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Assign(
                    targets=[Name(id='groups', ctx=Store())],
                    value=List(elts=[], ctx=Load()),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='current_literal_index', ctx=Store())],
                    value=Constant(value=0, kind=None),
                    type_comment=None,
                ),
                For(
                    target=Name(id='match', ctx=Store()),
                    iter=Call(
                        func=Attribute(
                            value=Name(id='INLINE_TEMPLATE_REGEX', ctx=Load()),
                            attr='finditer',
                            ctx=Load(),
                        ),
                        args=[Name(id='text', ctx=Load())],
                        keywords=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='literal', ctx=Store())],
                            value=Subscript(
                                value=Name(id='text', ctx=Load()),
                                slice=Slice(
                                    lower=Name(id='current_literal_index', ctx=Load()),
                                    upper=Call(
                                        func=Attribute(
                                            value=Name(id='match', ctx=Load()),
                                            attr='start',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    step=None,
                                ),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expression', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='match', ctx=Load()),
                                    attr='group',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=1, kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='groups', ctx=Load()),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[
                                    Tuple(
                                        elts=[
                                            Name(id='literal', ctx=Load()),
                                            Name(id='expression', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='current_literal_index', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='match', ctx=Load()),
                                    attr='end',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='literal', ctx=Store())],
                    value=Subscript(
                        value=Name(id='text', ctx=Load()),
                        slice=Slice(
                            lower=Name(id='current_literal_index', ctx=Load()),
                            upper=None,
                            step=None,
                        ),
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                If(
                    test=Name(id='literal', ctx=Load()),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='groups', ctx=Load()),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[
                                    Tuple(
                                        elts=[
                                            Name(id='literal', ctx=Load()),
                                            Constant(value='', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Name(id='groups', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='convert_inline_template_to_qweb',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='template', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Assign(
                    targets=[Name(id='template_instructions', ctx=Store())],
                    value=Call(
                        func=Name(id='parse_inline_template', ctx=Load()),
                        args=[
                            BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='template', ctx=Load()),
                                    Constant(value='', kind=None),
                                ],
                            ),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='preview_markup', ctx=Store())],
                    value=List(elts=[], ctx=Load()),
                    type_comment=None,
                ),
                For(
                    target=Tuple(
                        elts=[
                            Name(id='string', ctx=Store()),
                            Name(id='expression', ctx=Store()),
                        ],
                        ctx=Store(),
                    ),
                    iter=Name(id='template_instructions', ctx=Load()),
                    body=[
                        If(
                            test=Name(id='expression', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='preview_markup', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Name(id='Markup', ctx=Load()),
                                                        args=[Constant(value='{}<t t-out="{}"/>', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    attr='format',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='string', ctx=Load()),
                                                    Name(id='expression', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='preview_markup', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='string', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                        ),
                    ],
                    orelse=[],
                    type_comment=None,
                ),
                Return(
                    value=Call(
                        func=Attribute(
                            value=Call(
                                func=Name(id='Markup', ctx=Load()),
                                args=[Constant(value='', kind=None)],
                                keywords=[],
                            ),
                            attr='join',
                            ctx=Load(),
                        ),
                        args=[Name(id='preview_markup', ctx=Load())],
                        keywords=[],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='render_inline_template',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='template_instructions', annotation=None, type_comment=None),
                    arg(arg='variables', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Assign(
                    targets=[Name(id='results', ctx=Store())],
                    value=List(elts=[], ctx=Load()),
                    type_comment=None,
                ),
                For(
                    target=Tuple(
                        elts=[
                            Name(id='string', ctx=Store()),
                            Name(id='expression', ctx=Store()),
                        ],
                        ctx=Store(),
                    ),
                    iter=Name(id='template_instructions', ctx=Load()),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='results', ctx=Load()),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[Name(id='string', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Name(id='expression', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='result', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='safe_eval', ctx=Load()),
                                            attr='safe_eval',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='expression', ctx=Load()),
                                            Name(id='variables', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='result', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='results', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Name(id='str', ctx=Load()),
                                                        args=[Name(id='result', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    orelse=[],
                    type_comment=None,
                ),
                Return(
                    value=Call(
                        func=Attribute(
                            value=Constant(value='', kind=None),
                            attr='join',
                            ctx=Load(),
                        ),
                        args=[Name(id='results', ctx=Load())],
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
