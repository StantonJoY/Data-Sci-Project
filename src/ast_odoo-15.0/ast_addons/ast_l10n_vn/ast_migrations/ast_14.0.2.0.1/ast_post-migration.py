Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='SUPERUSER_ID', asname=None),
            ],
            level=0,
        ),
        Assign(
            targets=[Name(id='FIXED_ACCOUNTS_MAP', ctx=Store())],
            value=Dict(
                keys=[
                    Constant(value='5221', kind=None),
                    Constant(value='5222', kind=None),
                    Constant(value='5223', kind=None),
                ],
                values=[
                    Constant(value='5211', kind=None),
                    Constant(value='5212', kind=None),
                    Constant(value='5213', kind=None),
                ],
            ),
            type_comment=None,
        ),
        FunctionDef(
            name='_fix_revenue_deduction_accounts_code',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='env', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Assign(
                    targets=[Name(id='vn_template', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='env', ctx=Load()),
                            attr='ref',
                            ctx=Load(),
                        ),
                        args=[Constant(value='l10n_vn.vn_template', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                For(
                    target=Name(id='company', ctx=Store()),
                    iter=Call(
                        func=Attribute(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Name(id='env', ctx=Load()),
                                        slice=Constant(value='res.company', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='with_context',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='active_test',
                                        value=Constant(value=False, kind=None),
                                    ),
                                ],
                            ),
                            attr='search',
                            ctx=Load(),
                        ),
                        args=[
                            List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='chart_template_id', kind=None),
                                            Constant(value='=', kind=None),
                                            Attribute(
                                                value=Name(id='vn_template', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                    body=[
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='incorrect_code', ctx=Store()),
                                    Name(id='correct_code', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='FIXED_ACCOUNTS_MAP', ctx=Load()),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='account', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='env', ctx=Load()),
                                                slice=Constant(value='account.account', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='code', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Name(id='incorrect_code', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='company_id', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Attribute(
                                                                value=Name(id='company', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
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
                                If(
                                    test=Name(id='account', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='account', ctx=Load()),
                                                    attr='write',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[Constant(value='code', kind=None)],
                                                        values=[Name(id='correct_code', ctx=Load())],
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
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                    type_comment=None,
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='migrate',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='cr', annotation=None, type_comment=None),
                    arg(arg='version', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Assign(
                    targets=[Name(id='env', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='Environment',
                            ctx=Load(),
                        ),
                        args=[
                            Name(id='cr', ctx=Load()),
                            Name(id='SUPERUSER_ID', ctx=Load()),
                            Dict(keys=[], values=[]),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Expr(
                    value=Call(
                        func=Name(id='_fix_revenue_deduction_accounts_code', ctx=Load()),
                        args=[Name(id='env', ctx=Load())],
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
