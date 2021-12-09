Module(
    body=[
        Expr(
            value=Constant(value="The Odoo Exceptions module defines a few core exception types.\n\nThose types are understood by the RPC layer.\nAny other exception type bubbling until the RPC layer will be\ntreated as a 'Server error'.\n\n.. note::\n    If you consider introducing new exceptions,\n    check out the :mod:`odoo.addons.test_exceptions` module.\n", kind=None),
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='warnings', asname=None)],
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
        ClassDef(
            name='UserError',
            bases=[Name(id='Exception', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value='Generic error managed by the client.\n\n    Typically when the user tries to do something that has no sense given the current\n    state of a record. Semantically comparable to the generic 400 HTTP status codes.\n    ', kind=None),
                ),
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='message', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n        :param message: exception message and frontend modal content\n        ', kind=None),
                        ),
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
                                args=[Name(id='message', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='name',
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
                                    value=Name(id='warnings', ctx=Load()),
                                    attr='warn',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value="UserError attribute 'name' is a deprecated alias to args[0]", kind=None),
                                    Name(id='DeprecationWarning', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='args',
                                    ctx=Load(),
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='property', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='RedirectWarning',
            bases=[Name(id='Exception', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' Warning with a possibility to redirect the user instead of simply\n    displaying the warning message.\n\n    :param str message: exception message and frontend modal content\n    :param int action_id: id of the action where to perform the redirection\n    :param str button_text: text to put on the button that will trigger\n        the redirection.\n    :param dict additional_context: parameter passed to action_id.\n           Can be used to limit a view to active_ids for example.\n    ', kind=None),
                ),
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='message', annotation=None, type_comment=None),
                            arg(arg='action', annotation=None, type_comment=None),
                            arg(arg='button_text', annotation=None, type_comment=None),
                            arg(arg='additional_context', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
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
                                    Name(id='message', ctx=Load()),
                                    Name(id='action', ctx=Load()),
                                    Name(id='button_text', ctx=Load()),
                                    Name(id='additional_context', ctx=Load()),
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
                    name='name',
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
                                    value=Name(id='warnings', ctx=Load()),
                                    attr='warn',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value="RedirectWarning attribute 'name' is a deprecated alias to args[0]", kind=None),
                                    Name(id='DeprecationWarning', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='args',
                                    ctx=Load(),
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='property', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='AccessDenied',
            bases=[Name(id='UserError', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value='Login/password error.\n\n    .. note::\n\n        No traceback.\n\n    .. admonition:: Example\n\n        When you try to log with a wrong password.\n    ', kind=None),
                ),
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='message', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value='Access Denied', kind=None)],
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
                                args=[Name(id='message', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='with_traceback',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=None, kind=None)],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='__cause__',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='traceback',
                                    ctx=Store(),
                                ),
                            ],
                            value=Tuple(
                                elts=[
                                    Constant(value='', kind=None),
                                    Constant(value='', kind=None),
                                    Constant(value='', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
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
            name='AccessError',
            bases=[Name(id='UserError', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value='Access rights error.\n\n    .. admonition:: Example\n\n        When you try to read a record that you are not allowed to.\n    ', kind=None),
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='CacheMiss',
            bases=[Name(id='KeyError', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value='Missing value(s) in cache.\n\n    .. admonition:: Example\n\n        When you try to read a value in a flushed cache.\n    ', kind=None),
                ),
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='record', annotation=None, type_comment=None),
                            arg(arg='field', annotation=None, type_comment=None),
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
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='__init__',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Constant(value='%r.%s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Name(id='record', ctx=Load()),
                                                Attribute(
                                                    value=Name(id='field', ctx=Load()),
                                                    attr='name',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
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
        ClassDef(
            name='MissingError',
            bases=[Name(id='UserError', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value='Missing record(s).\n\n    .. admonition:: Example\n\n        When you try to write on a deleted record.\n    ', kind=None),
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='ValidationError',
            bases=[Name(id='UserError', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value='Violation of python constraints.\n\n    .. admonition:: Example\n\n        When you try to create a new user with a login which already exist in the db.\n    ', kind=None),
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='except_orm',
            bases=[Name(id='UserError', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='name', annotation=None, type_comment=None),
                            arg(arg='value', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
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
                                    Constant(value='except_orm is a deprecated alias to UserError.', kind=None),
                                    Name(id='DeprecationWarning', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                    JoinedStr(
                                        values=[
                                            FormattedValue(
                                                value=Name(id='name', ctx=Load()),
                                                conversion=-1,
                                                format_spec=None,
                                            ),
                                            Constant(value=': ', kind=None),
                                            FormattedValue(
                                                value=Name(id='value', ctx=Load()),
                                                conversion=-1,
                                                format_spec=None,
                                            ),
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
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='Warning',
            bases=[Name(id='UserError', ctx=Load())],
            keywords=[],
            body=[
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
                                    value=Name(id='warnings', ctx=Load()),
                                    attr='warn',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='Warning is a deprecated alias to UserError.', kind=None),
                                    Name(id='DeprecationWarning', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
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
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='QWebException',
            bases=[Name(id='Exception', ctx=Load())],
            keywords=[],
            body=[
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
                                    value=Name(id='warnings', ctx=Load()),
                                    attr='warn',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='qweb.QWebException is the exception you are looking for.', kind=None),
                                    Name(id='DeprecationWarning', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
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
