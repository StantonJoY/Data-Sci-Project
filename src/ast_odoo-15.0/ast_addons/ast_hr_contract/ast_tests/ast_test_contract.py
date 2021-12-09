Module(
    body=[
        ImportFrom(
            module='datetime',
            names=[
                alias(name='datetime', asname=None),
                alias(name='date', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[alias(name='ValidationError', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.hr_contract.tests.common',
            names=[alias(name='TestContractCommon', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TestHrContracts',
            bases=[Name(id='TestContractCommon', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='setUpClass',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='cls', annotation=None, type_comment=None)],
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
                                        args=[
                                            Name(id='TestHrContracts', ctx=Load()),
                                            Name(id='cls', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='setUpClass',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='contracts',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='hr.contract', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='with_context',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='tracking_disable',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='create_contract',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='state', annotation=None, type_comment=None),
                            arg(arg='kanban_state', annotation=None, type_comment=None),
                            arg(arg='start', annotation=None, type_comment=None),
                            arg(arg='end', annotation=None, type_comment=None),
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
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='hr.contract', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='employee_id', kind=None),
                                            Constant(value='state', kind=None),
                                            Constant(value='kanban_state', kind=None),
                                            Constant(value='wage', kind=None),
                                            Constant(value='date_start', kind=None),
                                            Constant(value='date_end', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Contract', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='employee',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Name(id='state', ctx=Load()),
                                            Name(id='kanban_state', ctx=Load()),
                                            Constant(value=1, kind=None),
                                            Name(id='start', ctx=Load()),
                                            Name(id='end', ctx=Load()),
                                        ],
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
                    name='test_incoming_overlapping_contract',
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
                            targets=[Name(id='start', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='datetime', ctx=Load()),
                                            attr='strptime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='2015-11-01', kind=None),
                                            Constant(value='%Y-%m-%d', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='date',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='end', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='datetime', ctx=Load()),
                                            attr='strptime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='2015-11-30', kind=None),
                                            Constant(value='%Y-%m-%d', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='date',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='create_contract',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='open', kind=None),
                                    Constant(value='normal', kind=None),
                                    Name(id='start', ctx=Load()),
                                    Name(id='end', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertRaises',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='ValidationError', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='msg',
                                                value=Constant(value='It should not create two contract in state open or incoming', kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='start', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='datetime', ctx=Load()),
                                                    attr='strptime',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='2015-11-15', kind=None),
                                                    Constant(value='%Y-%m-%d', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='date',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='end', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='datetime', ctx=Load()),
                                                    attr='strptime',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='2015-12-30', kind=None),
                                                    Constant(value='%Y-%m-%d', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='date',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='create_contract',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='draft', kind=None),
                                            Constant(value='done', kind=None),
                                            Name(id='start', ctx=Load()),
                                            Name(id='end', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_pending_overlapping_contract',
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
                            targets=[Name(id='start', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='datetime', ctx=Load()),
                                            attr='strptime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='2015-11-01', kind=None),
                                            Constant(value='%Y-%m-%d', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='date',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='end', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='datetime', ctx=Load()),
                                            attr='strptime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='2015-11-30', kind=None),
                                            Constant(value='%Y-%m-%d', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='date',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='create_contract',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='open', kind=None),
                                    Constant(value='normal', kind=None),
                                    Name(id='start', ctx=Load()),
                                    Name(id='end', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertRaises',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='ValidationError', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='msg',
                                                value=Constant(value='It should not create two contract in state open or pending', kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='start', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='datetime', ctx=Load()),
                                                    attr='strptime',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='2015-11-15', kind=None),
                                                    Constant(value='%Y-%m-%d', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='date',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='end', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='datetime', ctx=Load()),
                                                    attr='strptime',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='2015-12-30', kind=None),
                                                    Constant(value='%Y-%m-%d', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='date',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='create_contract',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='open', kind=None),
                                            Constant(value='blocked', kind=None),
                                            Name(id='start', ctx=Load()),
                                            Name(id='end', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='start', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='datetime', ctx=Load()),
                                            attr='strptime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='2015-11-15', kind=None),
                                            Constant(value='%Y-%m-%d', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='date',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='end', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='datetime', ctx=Load()),
                                            attr='strptime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='2015-12-30', kind=None),
                                            Constant(value='%Y-%m-%d', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='date',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='create_contract',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='draft', kind=None),
                                    Constant(value='normal', kind=None),
                                    Name(id='start', ctx=Load()),
                                    Name(id='end', ctx=Load()),
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
                    name='test_draft_overlapping_contract',
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
                            targets=[Name(id='start', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='datetime', ctx=Load()),
                                            attr='strptime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='2015-11-01', kind=None),
                                            Constant(value='%Y-%m-%d', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='date',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='end', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='datetime', ctx=Load()),
                                            attr='strptime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='2015-11-30', kind=None),
                                            Constant(value='%Y-%m-%d', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='date',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='create_contract',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='open', kind=None),
                                    Constant(value='normal', kind=None),
                                    Name(id='start', ctx=Load()),
                                    Name(id='end', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='start', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='datetime', ctx=Load()),
                                            attr='strptime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='2015-11-15', kind=None),
                                            Constant(value='%Y-%m-%d', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='date',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='end', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='datetime', ctx=Load()),
                                            attr='strptime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='2015-12-30', kind=None),
                                            Constant(value='%Y-%m-%d', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='date',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='create_contract',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='draft', kind=None),
                                    Constant(value='normal', kind=None),
                                    Name(id='start', ctx=Load()),
                                    Name(id='end', ctx=Load()),
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
                    name='test_overlapping_contract_no_end',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='create_contract',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='open', kind=None),
                                    Constant(value='normal', kind=None),
                                    Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='datetime', ctx=Load()),
                                                    attr='strptime',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='2015-11-01', kind=None),
                                                    Constant(value='%Y-%m-%d', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='date',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertRaises',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='ValidationError', ctx=Load())],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='start', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='datetime', ctx=Load()),
                                                    attr='strptime',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='2015-11-15', kind=None),
                                                    Constant(value='%Y-%m-%d', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='date',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='end', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='datetime', ctx=Load()),
                                                    attr='strptime',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='2015-12-30', kind=None),
                                                    Constant(value='%Y-%m-%d', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='date',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='create_contract',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='draft', kind=None),
                                            Constant(value='done', kind=None),
                                            Name(id='start', ctx=Load()),
                                            Name(id='end', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_overlapping_contract_no_end2',
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
                            targets=[Name(id='start', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='datetime', ctx=Load()),
                                            attr='strptime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='2015-11-01', kind=None),
                                            Constant(value='%Y-%m-%d', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='date',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='end', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='datetime', ctx=Load()),
                                            attr='strptime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='2015-12-30', kind=None),
                                            Constant(value='%Y-%m-%d', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='date',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='create_contract',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='open', kind=None),
                                    Constant(value='normal', kind=None),
                                    Name(id='start', ctx=Load()),
                                    Name(id='end', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertRaises',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='ValidationError', ctx=Load())],
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
                                            attr='create_contract',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='draft', kind=None),
                                            Constant(value='done', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='datetime', ctx=Load()),
                                                            attr='strptime',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='2015-01-01', kind=None),
                                                            Constant(value='%Y-%m-%d', kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    attr='date',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_set_employee_contract_create',
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
                            targets=[Name(id='contract', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='create_contract',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='open', kind=None),
                                    Constant(value='normal', kind=None),
                                    Call(
                                        func=Name(id='date', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=1, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='date', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=2, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
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
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='employee',
                                            ctx=Load(),
                                        ),
                                        attr='contract_id',
                                        ctx=Load(),
                                    ),
                                    Name(id='contract', ctx=Load()),
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
                    name='test_set_employee_contract_write',
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
                            targets=[Name(id='contract', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='create_contract',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='draft', kind=None),
                                    Constant(value='normal', kind=None),
                                    Call(
                                        func=Name(id='date', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=1, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='date', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=2, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='contract', ctx=Load()),
                                    attr='state',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='open', kind=None),
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
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='employee',
                                            ctx=Load(),
                                        ),
                                        attr='contract_id',
                                        ctx=Load(),
                                    ),
                                    Name(id='contract', ctx=Load()),
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
