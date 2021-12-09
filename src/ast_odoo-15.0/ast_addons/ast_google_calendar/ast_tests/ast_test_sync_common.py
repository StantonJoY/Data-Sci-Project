Module(
    body=[
        ImportFrom(
            module='unittest.mock',
            names=[
                alias(name='MagicMock', asname=None),
                alias(name='patch', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests.common',
            names=[alias(name='TransactionCase', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.google_calendar.utils.google_calendar',
            names=[alias(name='GoogleCalendarService', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.google_calendar.models.res_users',
            names=[alias(name='User', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.google_calendar.models.google_sync',
            names=[alias(name='GoogleSync', asname=None)],
            level=0,
        ),
        FunctionDef(
            name='patch_api',
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
                FunctionDef(
                    name='patched',
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
                        Return(
                            value=Call(
                                func=Name(id='func', ctx=Load()),
                                args=[
                                    Name(id='self', ctx=Load()),
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
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='patch', ctx=Load()),
                                attr='object',
                                ctx=Load(),
                            ),
                            args=[
                                Name(id='GoogleSync', ctx=Load()),
                                Constant(value='_google_insert', kind=None),
                                Call(
                                    func=Name(id='MagicMock', ctx=Load()),
                                    args=[],
                                    keywords=[
                                        keyword(
                                            arg='spec',
                                            value=Attribute(
                                                value=Name(id='GoogleSync', ctx=Load()),
                                                attr='_google_insert',
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            keywords=[],
                        ),
                        Call(
                            func=Attribute(
                                value=Name(id='patch', ctx=Load()),
                                attr='object',
                                ctx=Load(),
                            ),
                            args=[
                                Name(id='GoogleSync', ctx=Load()),
                                Constant(value='_google_delete', kind=None),
                                Call(
                                    func=Name(id='MagicMock', ctx=Load()),
                                    args=[],
                                    keywords=[
                                        keyword(
                                            arg='spec',
                                            value=Attribute(
                                                value=Name(id='GoogleSync', ctx=Load()),
                                                attr='_google_delete',
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            keywords=[],
                        ),
                        Call(
                            func=Attribute(
                                value=Name(id='patch', ctx=Load()),
                                attr='object',
                                ctx=Load(),
                            ),
                            args=[
                                Name(id='GoogleSync', ctx=Load()),
                                Constant(value='_google_patch', kind=None),
                                Call(
                                    func=Name(id='MagicMock', ctx=Load()),
                                    args=[],
                                    keywords=[
                                        keyword(
                                            arg='spec',
                                            value=Attribute(
                                                value=Name(id='GoogleSync', ctx=Load()),
                                                attr='_google_patch',
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                Return(
                    value=Name(id='patched', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        ClassDef(
            name='TestSyncGoogle',
            bases=[Name(id='TransactionCase', ctx=Load())],
            keywords=[],
            body=[
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
                                    attr='google_service',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='GoogleCalendarService', ctx=Load()),
                                args=[
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='google.service', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
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
                    name='assertGoogleEventDeleted',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='google_id', annotation=None, type_comment=None),
                        ],
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
                                    value=Attribute(
                                        value=Name(id='GoogleSync', ctx=Load()),
                                        attr='_google_delete',
                                        ctx=Load(),
                                    ),
                                    attr='assert_called',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='args', ctx=Store()),
                                        Name(id='dummy', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='GoogleSync', ctx=Load()),
                                    attr='_google_delete',
                                    ctx=Load(),
                                ),
                                attr='call_args',
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
                                    Subscript(
                                        value=Name(id='args', ctx=Load()),
                                        slice=Constant(value=1, kind=None),
                                        ctx=Load(),
                                    ),
                                    Name(id='google_id', ctx=Load()),
                                    Constant(value='Event should have been deleted', kind=None),
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
                    name='assertGoogleEventNotDeleted',
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
                                    value=Attribute(
                                        value=Name(id='GoogleSync', ctx=Load()),
                                        attr='_google_delete',
                                        ctx=Load(),
                                    ),
                                    attr='assert_not_called',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='assertGoogleEventInserted',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='values', annotation=None, type_comment=None),
                            arg(arg='timeout', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='expected_args', ctx=Store())],
                            value=Tuple(
                                elts=[Name(id='values', ctx=Load())],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expected_kwargs', ctx=Store())],
                            value=IfExp(
                                test=Name(id='timeout', ctx=Load()),
                                body=Dict(
                                    keys=[Constant(value='timeout', kind=None)],
                                    values=[Name(id='timeout', ctx=Load())],
                                ),
                                orelse=Dict(keys=[], values=[]),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='GoogleSync', ctx=Load()),
                                        attr='_google_insert',
                                        ctx=Load(),
                                    ),
                                    attr='assert_called_once',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='args', ctx=Store()),
                                        Name(id='kwargs', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='GoogleSync', ctx=Load()),
                                    attr='_google_insert',
                                    ctx=Load(),
                                ),
                                attr='call_args',
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
                                    Subscript(
                                        value=Name(id='args', ctx=Load()),
                                        slice=Slice(
                                            lower=Constant(value=1, kind=None),
                                            upper=None,
                                            step=None,
                                        ),
                                        ctx=Load(),
                                    ),
                                    Name(id='expected_args', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='kwargs', ctx=Load()),
                                    Name(id='expected_kwargs', ctx=Load()),
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
                    name='assertGoogleEventNotInserted',
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
                                    value=Attribute(
                                        value=Name(id='GoogleSync', ctx=Load()),
                                        attr='_google_insert',
                                        ctx=Load(),
                                    ),
                                    attr='assert_not_called',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='assertGoogleEventPatched',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='google_id', annotation=None, type_comment=None),
                            arg(arg='values', annotation=None, type_comment=None),
                            arg(arg='timeout', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='expected_args', ctx=Store())],
                            value=Tuple(
                                elts=[
                                    Name(id='google_id', ctx=Load()),
                                    Name(id='values', ctx=Load()),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expected_kwargs', ctx=Store())],
                            value=IfExp(
                                test=Name(id='timeout', ctx=Load()),
                                body=Dict(
                                    keys=[Constant(value='timeout', kind=None)],
                                    values=[Name(id='timeout', ctx=Load())],
                                ),
                                orelse=Dict(keys=[], values=[]),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='GoogleSync', ctx=Load()),
                                        attr='_google_patch',
                                        ctx=Load(),
                                    ),
                                    attr='assert_called_once',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='args', ctx=Store()),
                                        Name(id='kwargs', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='GoogleSync', ctx=Load()),
                                    attr='_google_patch',
                                    ctx=Load(),
                                ),
                                attr='call_args',
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
                                    Subscript(
                                        value=Name(id='args', ctx=Load()),
                                        slice=Slice(
                                            lower=Constant(value=1, kind=None),
                                            upper=None,
                                            step=None,
                                        ),
                                        ctx=Load(),
                                    ),
                                    Name(id='expected_args', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='kwargs', ctx=Load()),
                                    Name(id='expected_kwargs', ctx=Load()),
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
                    name='assertGoogleEventNotPatched',
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
                                    value=Attribute(
                                        value=Name(id='GoogleSync', ctx=Load()),
                                        attr='_google_patch',
                                        ctx=Load(),
                                    ),
                                    attr='assert_not_called',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='assertGoogleAPINotCalled',
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
                                    attr='assertGoogleEventNotPatched',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertGoogleEventNotInserted',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertGoogleEventNotDeleted',
                                    ctx=Load(),
                                ),
                                args=[],
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
                    func=Attribute(
                        value=Name(id='patch', ctx=Load()),
                        attr='object',
                        ctx=Load(),
                    ),
                    args=[
                        Name(id='User', ctx=Load()),
                        Constant(value='_get_google_calendar_token', kind=None),
                        Lambda(
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='user', annotation=None, type_comment=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=Constant(value='dummy-token', kind=None),
                        ),
                    ],
                    keywords=[],
                ),
            ],
        ),
    ],
    type_ignores=[],
)
