Module(
    body=[
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        ImportFrom(
            module='odoo.tests',
            names=[alias(name='standalone', asname=None)],
            level=0,
        ),
        Assign(
            targets=[Name(id='_logger', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='logging', ctx=Load()),
                    attr='getLogger',
                    ctx=Load(),
                ),
                args=[Name(id='__name__', ctx=Load())],
                keywords=[],
            ),
            type_comment=None,
        ),
        FunctionDef(
            name='test_all_l10n',
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
                Expr(
                    value=Constant(value=' This test will install all the l10n_* modules.\n    As the module install is not yet fully transactional, the modules will\n    remain installed after the test.\n    ', kind=None),
                ),
                Assert(
                    test=Attribute(
                        value=Call(
                            func=Attribute(
                                value=Name(id='env', ctx=Load()),
                                attr='ref',
                                ctx=Load(),
                            ),
                            args=[Constant(value='base.module_account', kind=None)],
                            keywords=[],
                        ),
                        attr='demo',
                        ctx=Load(),
                    ),
                    msg=Constant(value='Need the demo to test with data', kind=None),
                ),
                Assign(
                    targets=[Name(id='l10n_mods', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Subscript(
                                value=Name(id='env', ctx=Load()),
                                slice=Constant(value='ir.module.module', kind=None),
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
                                            Constant(value='name', kind=None),
                                            Constant(value='like', kind=None),
                                            Constant(value='l10n%', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='state', kind=None),
                                            Constant(value='=', kind=None),
                                            Constant(value='uninstalled', kind=None),
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
                        func=Attribute(
                            value=Name(id='l10n_mods', ctx=Load()),
                            attr='button_immediate_install',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='env', ctx=Load()),
                            attr='reset',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                ),
                Assign(
                    targets=[Name(id='env', ctx=Store())],
                    value=Call(
                        func=Name(id='env', ctx=Load()),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='coas', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Subscript(
                                value=Name(id='env', ctx=Load()),
                                slice=Constant(value='account.chart.template', kind=None),
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
                                            Constant(value='id', kind=None),
                                            Constant(value='not in', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Name(id='env', ctx=Load()),
                                                                slice=Constant(value='res.company', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='search',
                                                            ctx=Load(),
                                                        ),
                                                        args=[List(elts=[], ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    attr='chart_template_id',
                                                    ctx=Load(),
                                                ),
                                                attr='ids',
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
                For(
                    target=Name(id='coa', ctx=Store()),
                    iter=Name(id='coas', ctx=Load()),
                    body=[
                        Assign(
                            targets=[Name(id='cname', ctx=Store())],
                            value=BinOp(
                                left=Constant(value='company_%s', kind=None),
                                op=Mod(),
                                right=Call(
                                    func=Name(id='str', ctx=Load()),
                                    args=[
                                        Attribute(
                                            value=Name(id='coa', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='company', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Name(id='env', ctx=Load()),
                                        slice=Constant(value='res.company', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='country_id', kind=None),
                                        ],
                                        values=[
                                            Name(id='cname', ctx=Load()),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='coa', ctx=Load()),
                                                    attr='country_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        AugAssign(
                            target=Attribute(
                                value=Attribute(
                                    value=Name(id='env', ctx=Load()),
                                    attr='user',
                                    ctx=Load(),
                                ),
                                attr='company_ids',
                                ctx=Store(),
                            ),
                            op=Add(),
                            value=Name(id='company', ctx=Load()),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='env', ctx=Load()),
                                        attr='user',
                                        ctx=Load(),
                                    ),
                                    attr='company_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='company', ctx=Load()),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='info',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Constant(value='Testing COA: %s (company: %s)', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Attribute(
                                                    value=Name(id='coa', ctx=Load()),
                                                    attr='name',
                                                    ctx=Load(),
                                                ),
                                                Name(id='cname', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Try(
                            body=[
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='env', ctx=Load()),
                                                        attr='cr',
                                                        ctx=Load(),
                                                    ),
                                                    attr='savepoint',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            optional_vars=None,
                                        ),
                                    ],
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='coa', ctx=Load()),
                                                    attr='try_loading',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    type_comment=None,
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='Exception', ctx=Load()),
                                    name=None,
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='error',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='Error when creating COA %s', kind=None),
                                                    Attribute(
                                                        value=Name(id='coa', ctx=Load()),
                                                        attr='name',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='exc_info',
                                                        value=Constant(value=True, kind=None),
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                    ],
                    orelse=[],
                    type_comment=None,
                ),
            ],
            decorator_list=[
                Call(
                    func=Name(id='standalone', ctx=Load()),
                    args=[Constant(value='all_l10n', kind=None)],
                    keywords=[],
                ),
            ],
            returns=None,
            type_comment=None,
        ),
    ],
    type_ignores=[],
)
