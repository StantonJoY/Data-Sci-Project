Module(
    body=[
        Import(
            names=[alias(name='inspect', asname=None)],
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='warnings', asname=None)],
        ),
        Import(
            names=[alias(name='traceback', asname=None)],
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[alias(name='AccessDenied', asname=None)],
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
            name='is_autovacuum',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='func', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Return whether ``func`` is an autovacuum method. ', kind=None),
                ),
                Return(
                    value=BoolOp(
                        op=And(),
                        values=[
                            Call(
                                func=Name(id='callable', ctx=Load()),
                                args=[Name(id='func', ctx=Load())],
                                keywords=[],
                            ),
                            Call(
                                func=Name(id='getattr', ctx=Load()),
                                args=[
                                    Name(id='func', ctx=Load()),
                                    Constant(value='_autovacuum', kind=None),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                        ],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        ClassDef(
            name='AutoVacuum',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='AbstractModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' Helper model to the ``@api.autovacuum`` method decorator. ', kind=None),
                ),
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='ir.autovacuum', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Automatic Vacuum', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_run_vacuum_cleaner',
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
                            value=Constant(value='\n        Perform a complete database cleanup by safely calling every\n        ``@api.autovacuum`` decorated method.\n        ', kind=None),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='is_admin',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='AccessDenied', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        For(
                            target=Name(id='model', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='values',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='cls', ctx=Store())],
                                    value=Call(
                                        func=Name(id='type', ctx=Load()),
                                        args=[Name(id='model', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Tuple(
                                        elts=[
                                            Name(id='attr', ctx=Store()),
                                            Name(id='func', ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                    iter=Call(
                                        func=Attribute(
                                            value=Name(id='inspect', ctx=Load()),
                                            attr='getmembers',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='cls', ctx=Load()),
                                            Name(id='is_autovacuum', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='debug',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='Calling %s.%s()', kind=None),
                                                    Name(id='model', ctx=Load()),
                                                    Name(id='attr', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Try(
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Name(id='func', ctx=Load()),
                                                        args=[Name(id='model', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='cr',
                                                                ctx=Load(),
                                                            ),
                                                            attr='commit',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
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
                                                                    attr='exception',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Constant(value='Failed %s.%s()', kind=None),
                                                                    Name(id='model', ctx=Load()),
                                                                    Name(id='attr', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='env',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='cr',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='rollback',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
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
                            orelse=[],
                            type_comment=None,
                        ),
                        Try(
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='power_on',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='cr',
                                                ctx=Load(),
                                            ),
                                            attr='commit',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
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
                                                    attr='exception',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='Failed power_on', kind=None)],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='cr',
                                                        ctx=Load(),
                                                    ),
                                                    attr='rollback',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='power_on',
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
                        Assign(
                            targets=[Name(id='tb', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='traceback', ctx=Load()),
                                    attr='extract_stack',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='limit',
                                        value=Constant(value=2, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Subscript(
                                        value=Name(id='tb', ctx=Load()),
                                        slice=UnaryOp(
                                            op=USub(),
                                            operand=Constant(value=2, kind=None),
                                        ),
                                        ctx=Load(),
                                    ),
                                    attr='name',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='power_on', kind=None)],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='warnings', ctx=Load()),
                                            attr='warn',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            JoinedStr(
                                                values=[
                                                    Constant(value="You are extending the 'power_on' ir.autovacuum methodin ", kind=None),
                                                    FormattedValue(
                                                        value=Attribute(
                                                            value=Subscript(
                                                                value=Name(id='tb', ctx=Load()),
                                                                slice=UnaryOp(
                                                                    op=USub(),
                                                                    operand=Constant(value=2, kind=None),
                                                                ),
                                                                ctx=Load(),
                                                            ),
                                                            attr='filename',
                                                            ctx=Load(),
                                                        ),
                                                        conversion=-1,
                                                        format_spec=None,
                                                    ),
                                                    Constant(value=' around line ', kind=None),
                                                    FormattedValue(
                                                        value=Attribute(
                                                            value=Subscript(
                                                                value=Name(id='tb', ctx=Load()),
                                                                slice=UnaryOp(
                                                                    op=USub(),
                                                                    operand=Constant(value=2, kind=None),
                                                                ),
                                                                ctx=Load(),
                                                            ),
                                                            attr='lineno',
                                                            ctx=Load(),
                                                        ),
                                                        conversion=-1,
                                                        format_spec=None,
                                                    ),
                                                    Constant(value='. You should instead use the @api.autovacuum decorator on your garbage collecting method.', kind=None),
                                                ],
                                            ),
                                            Name(id='DeprecationWarning', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='stacklevel',
                                                value=Constant(value=2, kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
