Module(
    body=[
        Expr(
            value=Constant(value='\n    Vendored copy of https://github.com/pallets/werkzeug/blob/2b2c4c3dd3cf7389e9f4aa06371b7332257c6289/src/werkzeug/contrib/sessions.py\n\n    werkzeug.contrib was removed from werkzeug 1.0. sessions (and secure\n    cookies) were moved to the secure-cookies package. Problem is distros\n    are starting to update werkzeug to 1.0 without having secure-cookies\n    (e.g. Arch has done so, Debian has updated python-werkzeug in\n    "experimental"), which will be problematic once that starts trickling\n    down onto more stable distros and people start deploying that.\n\n    Edited some to fix imports and remove some compatibility things\n    (mostly PY2) and the unnecessary (to us) SessionMiddleware\n\n    :copyright: 2007 Pallets\n    :license: BSD-3-Clause\n', kind=None),
        ),
        Import(
            names=[alias(name='os', asname=None)],
        ),
        Import(
            names=[alias(name='re', asname=None)],
        ),
        Import(
            names=[alias(name='tempfile', asname=None)],
        ),
        ImportFrom(
            module='hashlib',
            names=[alias(name='sha1', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='os',
            names=[alias(name='path', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='pickle',
            names=[alias(name='dump', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='pickle',
            names=[alias(name='HIGHEST_PROTOCOL', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='pickle',
            names=[alias(name='load', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='time',
            names=[alias(name='time', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='werkzeug.datastructures',
            names=[alias(name='CallbackDict', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='werkzeug.posixemulation',
            names=[alias(name='rename', asname=None)],
            level=0,
        ),
        Assign(
            targets=[Name(id='_sha1_re', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='re', ctx=Load()),
                    attr='compile',
                    ctx=Load(),
                ),
                args=[Constant(value='^[a-f0-9]{40}$', kind=None)],
                keywords=[],
            ),
            type_comment=None,
        ),
        FunctionDef(
            name='generate_key',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='salt', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[Constant(value=None, kind=None)],
            ),
            body=[
                If(
                    test=Compare(
                        left=Name(id='salt', ctx=Load()),
                        ops=[Is()],
                        comparators=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='salt', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='repr', ctx=Load()),
                                        args=[Name(id='salt', ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='encode',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='ascii', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Call(
                        func=Attribute(
                            value=Call(
                                func=Name(id='sha1', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Constant(value=b'', kind=None),
                                            attr='join',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Name(id='salt', ctx=Load()),
                                                    Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Name(id='str', ctx=Load()),
                                                                args=[
                                                                    Call(
                                                                        func=Name(id='time', ctx=Load()),
                                                                        args=[],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            attr='encode',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='ascii', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='os', ctx=Load()),
                                                            attr='urandom',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value=30, kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            attr='hexdigest',
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
        ClassDef(
            name='ModificationTrackingDict',
            bases=[Name(id='CallbackDict', ctx=Load())],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='__slots__', ctx=Store())],
                    value=Tuple(
                        elts=[Constant(value='modified', kind=None)],
                        ctx=Load(),
                    ),
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
                        FunctionDef(
                            name='on_update',
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
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='modified',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=True, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='modified',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='CallbackDict', ctx=Load()),
                                    attr='__init__',
                                    ctx=Load(),
                                ),
                                args=[Name(id='self', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='on_update',
                                        value=Name(id='on_update', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='dict', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='copy',
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
                            value=Constant(value='Create a flat copy of the dict.', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='missing', ctx=Store())],
                            value=Call(
                                func=Name(id='object', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='object', ctx=Load()),
                                    attr='__new__',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='__class__',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='name', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='__slots__',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='val', ctx=Store())],
                                    value=Call(
                                        func=Name(id='getattr', ctx=Load()),
                                        args=[
                                            Name(id='self', ctx=Load()),
                                            Name(id='name', ctx=Load()),
                                            Name(id='missing', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='val', ctx=Load()),
                                        ops=[IsNot()],
                                        comparators=[Name(id='missing', ctx=Load())],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Name(id='setattr', ctx=Load()),
                                                args=[
                                                    Name(id='result', ctx=Load()),
                                                    Name(id='name', ctx=Load()),
                                                    Name(id='val', ctx=Load()),
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
                        Return(
                            value=Name(id='result', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='__copy__',
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
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='copy',
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
            decorator_list=[],
        ),
        ClassDef(
            name='Session',
            bases=[Name(id='ModificationTrackingDict', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value='Subclass of a dict that keeps track of direct object changes.  Changes\n    in mutable structures are not tracked, for those you have to set\n    `modified` to `True` by hand.\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='__slots__', ctx=Store())],
                    value=BinOp(
                        left=Attribute(
                            value=Name(id='ModificationTrackingDict', ctx=Load()),
                            attr='__slots__',
                            ctx=Load(),
                        ),
                        op=Add(),
                        right=Tuple(
                            elts=[
                                Constant(value='sid', kind=None),
                                Constant(value='new', kind=None),
                            ],
                            ctx=Load(),
                        ),
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='data', annotation=None, type_comment=None),
                            arg(arg='sid', annotation=None, type_comment=None),
                            arg(arg='new', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=False, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='ModificationTrackingDict', ctx=Load()),
                                    attr='__init__',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='self', ctx=Load()),
                                    Name(id='data', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='sid',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='sid', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='new',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='new', ctx=Load()),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='__repr__',
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
                        Return(
                            value=BinOp(
                                left=Constant(value='<%s %s%s>', kind=None),
                                op=Mod(),
                                right=Tuple(
                                    elts=[
                                        Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='__class__',
                                                ctx=Load(),
                                            ),
                                            attr='__name__',
                                            ctx=Load(),
                                        ),
                                        Call(
                                            func=Attribute(
                                                value=Name(id='dict', ctx=Load()),
                                                attr='__repr__',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='self', ctx=Load())],
                                            keywords=[],
                                        ),
                                        IfExp(
                                            test=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='should_save',
                                                ctx=Load(),
                                            ),
                                            body=Constant(value='*', kind=None),
                                            orelse=Constant(value='', kind=None),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='should_save',
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
                            value=Constant(value='True if the session should be saved.\n\n        .. versionchanged:: 0.6\n           By default the session is now only saved if the session is\n           modified, not if it is new like it was before.\n        ', kind=None),
                        ),
                        Return(
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='modified',
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
            name='SessionStore',
            bases=[Name(id='object', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value='Baseclass for all session stores.  The Werkzeug contrib module does not\n    implement any useful stores besides the filesystem store, application\n    developers are encouraged to create their own stores.\n\n    :param session_class: The session class to use.  Defaults to\n                          :class:`Session`.\n    ', kind=None),
                ),
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='session_class', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        If(
                            test=Compare(
                                left=Name(id='session_class', ctx=Load()),
                                ops=[Is()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='session_class', ctx=Store())],
                                    value=Name(id='Session', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='session_class',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='session_class', ctx=Load()),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='is_valid_key',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='key', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Check if a key has the correct format.', kind=None),
                        ),
                        Return(
                            value=Compare(
                                left=Call(
                                    func=Attribute(
                                        value=Name(id='_sha1_re', ctx=Load()),
                                        attr='match',
                                        ctx=Load(),
                                    ),
                                    args=[Name(id='key', ctx=Load())],
                                    keywords=[],
                                ),
                                ops=[IsNot()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='generate_key',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='salt', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Simple function that generates a new session key.', kind=None),
                        ),
                        Return(
                            value=Call(
                                func=Name(id='generate_key', ctx=Load()),
                                args=[Name(id='salt', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='new',
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
                            value=Constant(value='Generate a new session.', kind=None),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='session_class',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(keys=[], values=[]),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='generate_key',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Constant(value=True, kind=None),
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
                    name='save',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='session', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Save a session.', kind=None),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='save_if_modified',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='session', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Save if a session class wants an update.', kind=None),
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='session', ctx=Load()),
                                attr='should_save',
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='save',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='session', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='delete',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='session', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Delete a session.', kind=None),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='sid', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value="Get a session for this sid or a new session object.  This method\n        has to check if the session key is valid and create a new session if\n        that wasn't the case.\n        ", kind=None),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='session_class',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(keys=[], values=[]),
                                    Name(id='sid', ctx=Load()),
                                    Constant(value=True, kind=None),
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
        Assign(
            targets=[Name(id='_fs_transaction_suffix', ctx=Store())],
            value=Constant(value='.__wz_sess', kind=None),
            type_comment=None,
        ),
        ClassDef(
            name='FilesystemSessionStore',
            bases=[Name(id='SessionStore', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value='Simple example session store that saves sessions on the filesystem.\n    This store works best on POSIX systems and Windows Vista / Windows\n    Server 2008 and newer.\n\n    .. versionchanged:: 0.6\n       `renew_missing` was added.  Previously this was considered `True`,\n       now the default changed to `False` and it can be explicitly\n       deactivated.\n\n    :param path: the path to the folder used for storing the sessions.\n                 If not provided the default temporary directory is used.\n    :param filename_template: a string template used to give the session\n                              a filename.  ``%s`` is replaced with the\n                              session id.\n    :param session_class: The session class to use.  Defaults to\n                          :class:`Session`.\n    :param renew_missing: set to `True` if you want the store to\n                          give the user a new sid if the session was\n                          not yet saved.\n    ', kind=None),
                ),
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='path', annotation=None, type_comment=None),
                            arg(arg='filename_template', annotation=None, type_comment=None),
                            arg(arg='session_class', annotation=None, type_comment=None),
                            arg(arg='renew_missing', annotation=None, type_comment=None),
                            arg(arg='mode', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value='werkzeug_%s.sess', kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=420, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='SessionStore', ctx=Load()),
                                    attr='__init__',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='self', ctx=Load()),
                                    Name(id='session_class', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Compare(
                                left=Name(id='path', ctx=Load()),
                                ops=[Is()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='path', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='tempfile', ctx=Load()),
                                            attr='gettempdir',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='path',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='path', ctx=Load()),
                            type_comment=None,
                        ),
                        Assert(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Name(id='filename_template', ctx=Load()),
                                        attr='endswith',
                                        ctx=Load(),
                                    ),
                                    args=[Name(id='_fs_transaction_suffix', ctx=Load())],
                                    keywords=[],
                                ),
                            ),
                            msg=BinOp(
                                left=Constant(value='filename templates may not end with %s', kind=None),
                                op=Mod(),
                                right=Name(id='_fs_transaction_suffix', ctx=Load()),
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='filename_template',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='filename_template', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='renew_missing',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='renew_missing', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='mode',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='mode', ctx=Load()),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_session_filename',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='sid', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='path', ctx=Load()),
                                    attr='join',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='path',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='filename_template',
                                            ctx=Load(),
                                        ),
                                        op=Mod(),
                                        right=Name(id='sid', ctx=Load()),
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
                    name='save',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='session', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='fn', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='get_session_filename',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='session', ctx=Load()),
                                        attr='sid',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='fd', ctx=Store()),
                                        Name(id='tmp', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='tempfile', ctx=Load()),
                                    attr='mkstemp',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='suffix',
                                        value=Name(id='_fs_transaction_suffix', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='dir',
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='path',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='f', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='os', ctx=Load()),
                                    attr='fdopen',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='fd', ctx=Load()),
                                    Constant(value='wb', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Try(
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='dump', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='dict', ctx=Load()),
                                                args=[Name(id='session', ctx=Load())],
                                                keywords=[],
                                            ),
                                            Name(id='f', ctx=Load()),
                                            Name(id='HIGHEST_PROTOCOL', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            handlers=[],
                            orelse=[],
                            finalbody=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='f', ctx=Load()),
                                            attr='close',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                        ),
                        Try(
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='rename', ctx=Load()),
                                        args=[
                                            Name(id='tmp', ctx=Load()),
                                            Name(id='fn', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='os', ctx=Load()),
                                            attr='chmod',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='fn', ctx=Load()),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='mode',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Tuple(
                                        elts=[
                                            Name(id='IOError', ctx=Load()),
                                            Name(id='OSError', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                    name=None,
                                    body=[Pass()],
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
                    name='delete',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='session', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='fn', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='get_session_filename',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='session', ctx=Load()),
                                        attr='sid',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Try(
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='os', ctx=Load()),
                                            attr='unlink',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='fn', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='OSError', ctx=Load()),
                                    name=None,
                                    body=[Pass()],
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
                    name='get',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='sid', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='is_valid_key',
                                        ctx=Load(),
                                    ),
                                    args=[Name(id='sid', ctx=Load())],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='new',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id='f', ctx=Store())],
                                    value=Call(
                                        func=Name(id='open', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='get_session_filename',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='sid', ctx=Load())],
                                                keywords=[],
                                            ),
                                            Constant(value='rb', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='IOError', ctx=Load()),
                                    name=None,
                                    body=[
                                        If(
                                            test=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='renew_missing',
                                                ctx=Load(),
                                            ),
                                            body=[
                                                Return(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='new',
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
                                            targets=[Name(id='data', ctx=Store())],
                                            value=Dict(keys=[], values=[]),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[
                                Try(
                                    body=[
                                        Try(
                                            body=[
                                                Assign(
                                                    targets=[Name(id='data', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='load', ctx=Load()),
                                                        args=[Name(id='f', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            handlers=[
                                                ExceptHandler(
                                                    type=Name(id='Exception', ctx=Load()),
                                                    name=None,
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='data', ctx=Store())],
                                                            value=Dict(keys=[], values=[]),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            orelse=[],
                                            finalbody=[],
                                        ),
                                    ],
                                    handlers=[],
                                    orelse=[],
                                    finalbody=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='f', ctx=Load()),
                                                    attr='close',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            finalbody=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='session_class',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='data', ctx=Load()),
                                    Name(id='sid', ctx=Load()),
                                    Constant(value=False, kind=None),
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
                    name='list',
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
                            value=Constant(value='Lists all sessions in the store.\n\n        .. versionadded:: 0.6\n        ', kind=None),
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='before', ctx=Store()),
                                        Name(id='after', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='filename_template',
                                        ctx=Load(),
                                    ),
                                    attr='split',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='%s', kind=None),
                                    Constant(value=1, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='filename_re', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='re', ctx=Load()),
                                    attr='compile',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Constant(value='%s(.{5,})%s$', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Call(
                                                    func=Attribute(
                                                        value=Name(id='re', ctx=Load()),
                                                        attr='escape',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='before', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                Call(
                                                    func=Attribute(
                                                        value=Name(id='re', ctx=Load()),
                                                        attr='escape',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='after', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='filename', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='os', ctx=Load()),
                                    attr='listdir',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='path',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Name(id='filename', ctx=Load()),
                                            attr='endswith',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='_fs_transaction_suffix', ctx=Load())],
                                        keywords=[],
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='match', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='filename_re', ctx=Load()),
                                            attr='match',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='filename', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='match', ctx=Load()),
                                        ops=[IsNot()],
                                        comparators=[Constant(value=None, kind=None)],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='result', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='match', ctx=Load()),
                                                            attr='group',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value=1, kind=None)],
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
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='result', ctx=Load()),
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
