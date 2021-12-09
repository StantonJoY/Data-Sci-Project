Module(
    body=[
        Expr(
            value=Constant(value='Utilities for determining application-specific dirs.\n\nSee <http://github.com/ActiveState/appdirs> for details and usage.\n', kind=None),
        ),
        ImportFrom(
            module='__future__',
            names=[alias(name='print_function', asname=None)],
            level=0,
        ),
        Assign(
            targets=[Name(id='__version_info__', ctx=Store())],
            value=Tuple(
                elts=[
                    Constant(value=1, kind=None),
                    Constant(value=3, kind=None),
                    Constant(value=0, kind=None),
                ],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='__version__', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Constant(value='.', kind=None),
                    attr='join',
                    ctx=Load(),
                ),
                args=[
                    GeneratorExp(
                        elt=Call(
                            func=Name(id='str', ctx=Load()),
                            args=[Name(id='v', ctx=Load())],
                            keywords=[],
                        ),
                        generators=[
                            comprehension(
                                target=Name(id='v', ctx=Store()),
                                iter=Name(id='__version_info__', ctx=Load()),
                                ifs=[],
                                is_async=0,
                            ),
                        ],
                    ),
                ],
                keywords=[],
            ),
            type_comment=None,
        ),
        Import(
            names=[alias(name='sys', asname=None)],
        ),
        Import(
            names=[alias(name='os', asname=None)],
        ),
        FunctionDef(
            name='user_data_dir',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='appname', annotation=None, type_comment=None),
                    arg(arg='appauthor', annotation=None, type_comment=None),
                    arg(arg='version', annotation=None, type_comment=None),
                    arg(arg='roaming', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    Constant(value=None, kind=None),
                    Constant(value=None, kind=None),
                    Constant(value=None, kind=None),
                    Constant(value=False, kind=None),
                ],
            ),
            body=[
                Expr(
                    value=Constant(value='Return full path to the user-specific data dir for this application.\n\n        "appname" is the name of application.\n            If None, just the system directory is returned.\n        "appauthor" (only required and used on Windows) is the name of the\n            appauthor or distributing body for this application. Typically\n            it is the owning company name. This falls back to appname.\n        "version" is an optional version path element to append to the\n            path. You might want to use this if you want multiple versions\n            of your app to be able to run independently. If used, this\n            would typically be "<major>.<minor>".\n            Only applied when appname is present.\n        "roaming" (boolean, default False) can be set True to use the Windows\n            roaming appdata directory. That means that for users on a Windows\n            network setup for roaming profiles, this user data will be\n            sync\'d on login. See\n            <http://technet.microsoft.com/en-us/library/cc766489(WS.10).aspx>\n            for a discussion of issues.\n\n    Typical user data directories are:\n        Mac OS X:               ~/Library/Application Support/<AppName>\n        Unix:                   ~/.local/share/<AppName>    # or in $XDG_DATA_HOME, if defined\n        Win XP (not roaming):   C:\\Documents and Settings\\<username>\\Application Data\\<AppAuthor>\\<AppName>\n        Win XP (roaming):       C:\\Documents and Settings\\<username>\\Local Settings\\Application Data\\<AppAuthor>\\<AppName>\n        Win 7  (not roaming):   C:\\Users\\<username>\\AppData\\Local\\<AppAuthor>\\<AppName>\n        Win 7  (roaming):       C:\\Users\\<username>\\AppData\\Roaming\\<AppAuthor>\\<AppName>\n\n    For Unix, we follow the XDG spec and support $XDG_DATA_HOME.\n    That means, by default "~/.local/share/<AppName>".\n    ', kind=None),
                ),
                If(
                    test=Compare(
                        left=Attribute(
                            value=Name(id='sys', ctx=Load()),
                            attr='platform',
                            ctx=Load(),
                        ),
                        ops=[Eq()],
                        comparators=[Constant(value='win32', kind=None)],
                    ),
                    body=[
                        If(
                            test=Compare(
                                left=Name(id='appauthor', ctx=Load()),
                                ops=[Is()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='appauthor', ctx=Store())],
                                    value=Name(id='appname', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='const', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='roaming', ctx=Load()),
                                            Constant(value='CSIDL_APPDATA', kind=None),
                                        ],
                                    ),
                                    Constant(value='CSIDL_LOCAL_APPDATA', kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='path', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='os', ctx=Load()),
                                        attr='path',
                                        ctx=Load(),
                                    ),
                                    attr='normpath',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='_get_win_folder', ctx=Load()),
                                        args=[Name(id='const', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='appname', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='path', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='os', ctx=Load()),
                                                attr='path',
                                                ctx=Load(),
                                            ),
                                            attr='join',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='path', ctx=Load()),
                                            Name(id='appauthor', ctx=Load()),
                                            Name(id='appname', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    orelse=[
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='sys', ctx=Load()),
                                    attr='platform',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='darwin', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='path', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='os', ctx=Load()),
                                                attr='path',
                                                ctx=Load(),
                                            ),
                                            attr='expanduser',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='~/Library/Application Support/', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='appname', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='path', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='os', ctx=Load()),
                                                        attr='path',
                                                        ctx=Load(),
                                                    ),
                                                    attr='join',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='path', ctx=Load()),
                                                    Name(id='appname', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='path', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='os', ctx=Load()),
                                            attr='getenv',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='XDG_DATA_HOME', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='os', ctx=Load()),
                                                        attr='path',
                                                        ctx=Load(),
                                                    ),
                                                    attr='expanduser',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='~/.local/share', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='appname', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='path', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='os', ctx=Load()),
                                                        attr='path',
                                                        ctx=Load(),
                                                    ),
                                                    attr='join',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='path', ctx=Load()),
                                                    Name(id='appname', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                        ),
                    ],
                ),
                If(
                    test=BoolOp(
                        op=And(),
                        values=[
                            Name(id='appname', ctx=Load()),
                            Name(id='version', ctx=Load()),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='path', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='os', ctx=Load()),
                                        attr='path',
                                        ctx=Load(),
                                    ),
                                    attr='join',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='path', ctx=Load()),
                                    Name(id='version', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Name(id='path', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='site_data_dir',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='appname', annotation=None, type_comment=None),
                    arg(arg='appauthor', annotation=None, type_comment=None),
                    arg(arg='version', annotation=None, type_comment=None),
                    arg(arg='multipath', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    Constant(value=None, kind=None),
                    Constant(value=None, kind=None),
                    Constant(value=None, kind=None),
                    Constant(value=False, kind=None),
                ],
            ),
            body=[
                Expr(
                    value=Constant(value='Return full path to the user-shared data dir for this application.\n\n        "appname" is the name of application.\n            If None, just the system directory is returned.\n        "appauthor" (only required and used on Windows) is the name of the\n            appauthor or distributing body for this application. Typically\n            it is the owning company name. This falls back to appname.\n        "version" is an optional version path element to append to the\n            path. You might want to use this if you want multiple versions\n            of your app to be able to run independently. If used, this\n            would typically be "<major>.<minor>".\n            Only applied when appname is present.\n        "multipath" is an optional parameter only applicable to *nix\n            which indicates that the entire list of data dirs should be\n            returned. By default, the first item from XDG_DATA_DIRS is\n            returned, or \'/usr/local/share/<AppName>\',\n            if XDG_DATA_DIRS is not set\n\n    Typical user data directories are:\n        Mac OS X:   /Library/Application Support/<AppName>\n        Unix:       /usr/local/share/<AppName> or /usr/share/<AppName>\n        Win XP:     C:\\Documents and Settings\\All Users\\Application Data\\<AppAuthor>\\<AppName>\n        Vista:      (Fail! "C:\\ProgramData" is a hidden *system* directory on Vista.)\n        Win 7:      C:\\ProgramData\\<AppAuthor>\\<AppName>   # Hidden, but writeable on Win 7.\n\n    For Unix, this is using the $XDG_DATA_DIRS[0] default.\n\n    WARNING: Do not use this on Windows. See the Vista-Fail note above for why.\n    ', kind=None),
                ),
                If(
                    test=Compare(
                        left=Attribute(
                            value=Name(id='sys', ctx=Load()),
                            attr='platform',
                            ctx=Load(),
                        ),
                        ops=[Eq()],
                        comparators=[Constant(value='win32', kind=None)],
                    ),
                    body=[
                        If(
                            test=Compare(
                                left=Name(id='appauthor', ctx=Load()),
                                ops=[Is()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='appauthor', ctx=Store())],
                                    value=Name(id='appname', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='path', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='os', ctx=Load()),
                                        attr='path',
                                        ctx=Load(),
                                    ),
                                    attr='normpath',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='_get_win_folder', ctx=Load()),
                                        args=[Constant(value='CSIDL_COMMON_APPDATA', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='appname', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='path', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='os', ctx=Load()),
                                                attr='path',
                                                ctx=Load(),
                                            ),
                                            attr='join',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='path', ctx=Load()),
                                            Name(id='appauthor', ctx=Load()),
                                            Name(id='appname', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    orelse=[
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='sys', ctx=Load()),
                                    attr='platform',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='darwin', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='path', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='os', ctx=Load()),
                                                attr='path',
                                                ctx=Load(),
                                            ),
                                            attr='expanduser',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='/Library/Application Support', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='appname', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='path', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='os', ctx=Load()),
                                                        attr='path',
                                                        ctx=Load(),
                                                    ),
                                                    attr='join',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='path', ctx=Load()),
                                                    Name(id='appname', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='path', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='os', ctx=Load()),
                                            attr='getenv',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='XDG_DATA_DIRS', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='os', ctx=Load()),
                                                        attr='pathsep',
                                                        ctx=Load(),
                                                    ),
                                                    attr='join',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Constant(value='/usr/local/share', kind=None),
                                                            Constant(value='/usr/share', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='pathlist', ctx=Store())],
                                    value=ListComp(
                                        elt=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id='os', ctx=Load()),
                                                    attr='path',
                                                    ctx=Load(),
                                                ),
                                                attr='expanduser',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Call(
                                                    func=Attribute(
                                                        value=Name(id='x', ctx=Load()),
                                                        attr='rstrip',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Attribute(
                                                            value=Name(id='os', ctx=Load()),
                                                            attr='sep',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='x', ctx=Store()),
                                                iter=Call(
                                                    func=Attribute(
                                                        value=Name(id='path', ctx=Load()),
                                                        attr='split',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Attribute(
                                                            value=Name(id='os', ctx=Load()),
                                                            attr='pathsep',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='appname', ctx=Load()),
                                    body=[
                                        If(
                                            test=Name(id='version', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='appname', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='os', ctx=Load()),
                                                                attr='path',
                                                                ctx=Load(),
                                                            ),
                                                            attr='join',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='appname', ctx=Load()),
                                                            Name(id='version', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='pathlist', ctx=Store())],
                                            value=ListComp(
                                                elt=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='os', ctx=Load()),
                                                            attr='sep',
                                                            ctx=Load(),
                                                        ),
                                                        attr='join',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        List(
                                                            elts=[
                                                                Name(id='x', ctx=Load()),
                                                                Name(id='appname', ctx=Load()),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='x', ctx=Store()),
                                                        iter=Name(id='pathlist', ctx=Load()),
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
                                If(
                                    test=Name(id='multipath', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='path', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='os', ctx=Load()),
                                                        attr='pathsep',
                                                        ctx=Load(),
                                                    ),
                                                    attr='join',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='pathlist', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='path', ctx=Store())],
                                            value=Subscript(
                                                value=Name(id='pathlist', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                                Return(
                                    value=Name(id='path', ctx=Load()),
                                ),
                            ],
                        ),
                    ],
                ),
                If(
                    test=BoolOp(
                        op=And(),
                        values=[
                            Name(id='appname', ctx=Load()),
                            Name(id='version', ctx=Load()),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='path', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='os', ctx=Load()),
                                        attr='path',
                                        ctx=Load(),
                                    ),
                                    attr='join',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='path', ctx=Load()),
                                    Name(id='version', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Name(id='path', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='user_config_dir',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='appname', annotation=None, type_comment=None),
                    arg(arg='appauthor', annotation=None, type_comment=None),
                    arg(arg='version', annotation=None, type_comment=None),
                    arg(arg='roaming', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    Constant(value=None, kind=None),
                    Constant(value=None, kind=None),
                    Constant(value=None, kind=None),
                    Constant(value=False, kind=None),
                ],
            ),
            body=[
                Expr(
                    value=Constant(value='Return full path to the user-specific config dir for this application.\n\n        "appname" is the name of application.\n            If None, just the system directory is returned.\n        "appauthor" (only required and used on Windows) is the name of the\n            appauthor or distributing body for this application. Typically\n            it is the owning company name. This falls back to appname.\n        "version" is an optional version path element to append to the\n            path. You might want to use this if you want multiple versions\n            of your app to be able to run independently. If used, this\n            would typically be "<major>.<minor>".\n            Only applied when appname is present.\n        "roaming" (boolean, default False) can be set True to use the Windows\n            roaming appdata directory. That means that for users on a Windows\n            network setup for roaming profiles, this user data will be\n            sync\'d on login. See\n            <http://technet.microsoft.com/en-us/library/cc766489(WS.10).aspx>\n            for a discussion of issues.\n\n    Typical user data directories are:\n        Mac OS X:               same as user_data_dir\n        Unix:                   ~/.config/<AppName>     # or in $XDG_CONFIG_HOME, if defined\n        Win *:                  same as user_data_dir\n\n    For Unix, we follow the XDG spec and support $XDG_DATA_HOME.\n    That means, by default "~/.local/share/<AppName>".\n    ', kind=None),
                ),
                If(
                    test=Compare(
                        left=Attribute(
                            value=Name(id='sys', ctx=Load()),
                            attr='platform',
                            ctx=Load(),
                        ),
                        ops=[In()],
                        comparators=[
                            List(
                                elts=[
                                    Constant(value='win32', kind=None),
                                    Constant(value='darwin', kind=None),
                                ],
                                ctx=Load(),
                            ),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='path', ctx=Store())],
                            value=Call(
                                func=Name(id='user_data_dir', ctx=Load()),
                                args=[
                                    Name(id='appname', ctx=Load()),
                                    Name(id='appauthor', ctx=Load()),
                                    Constant(value=None, kind=None),
                                    Name(id='roaming', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[
                        Assign(
                            targets=[Name(id='path', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='os', ctx=Load()),
                                    attr='getenv',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='XDG_CONFIG_HOME', kind=None),
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='os', ctx=Load()),
                                                attr='path',
                                                ctx=Load(),
                                            ),
                                            attr='expanduser',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='~/.config', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='appname', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='path', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='os', ctx=Load()),
                                                attr='path',
                                                ctx=Load(),
                                            ),
                                            attr='join',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='path', ctx=Load()),
                                            Name(id='appname', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                ),
                If(
                    test=BoolOp(
                        op=And(),
                        values=[
                            Name(id='appname', ctx=Load()),
                            Name(id='version', ctx=Load()),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='path', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='os', ctx=Load()),
                                        attr='path',
                                        ctx=Load(),
                                    ),
                                    attr='join',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='path', ctx=Load()),
                                    Name(id='version', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Name(id='path', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='site_config_dir',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='appname', annotation=None, type_comment=None),
                    arg(arg='appauthor', annotation=None, type_comment=None),
                    arg(arg='version', annotation=None, type_comment=None),
                    arg(arg='multipath', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    Constant(value=None, kind=None),
                    Constant(value=None, kind=None),
                    Constant(value=None, kind=None),
                    Constant(value=False, kind=None),
                ],
            ),
            body=[
                Expr(
                    value=Constant(value='Return full path to the user-shared data dir for this application.\n\n        "appname" is the name of application.\n            If None, just the system directory is returned.\n        "appauthor" (only required and used on Windows) is the name of the\n            appauthor or distributing body for this application. Typically\n            it is the owning company name. This falls back to appname.\n        "version" is an optional version path element to append to the\n            path. You might want to use this if you want multiple versions\n            of your app to be able to run independently. If used, this\n            would typically be "<major>.<minor>".\n            Only applied when appname is present.\n        "multipath" is an optional parameter only applicable to *nix\n            which indicates that the entire list of config dirs should be\n            returned. By default, the first item from XDG_CONFIG_DIRS is\n            returned, or \'/etc/xdg/<AppName>\', if XDG_CONFIG_DIRS is not set\n\n    Typical user data directories are:\n        Mac OS X:   same as site_data_dir\n        Unix:       /etc/xdg/<AppName> or $XDG_CONFIG_DIRS[i]/<AppName> for each value in\n                    $XDG_CONFIG_DIRS\n        Win *:      same as site_data_dir\n        Vista:      (Fail! "C:\\ProgramData" is a hidden *system* directory on Vista.)\n\n    For Unix, this is using the $XDG_CONFIG_DIRS[0] default, if multipath=False\n\n    WARNING: Do not use this on Windows. See the Vista-Fail note above for why.\n    ', kind=None),
                ),
                If(
                    test=Compare(
                        left=Attribute(
                            value=Name(id='sys', ctx=Load()),
                            attr='platform',
                            ctx=Load(),
                        ),
                        ops=[In()],
                        comparators=[
                            List(
                                elts=[
                                    Constant(value='win32', kind=None),
                                    Constant(value='darwin', kind=None),
                                ],
                                ctx=Load(),
                            ),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='path', ctx=Store())],
                            value=Call(
                                func=Name(id='site_data_dir', ctx=Load()),
                                args=[
                                    Name(id='appname', ctx=Load()),
                                    Name(id='appauthor', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='appname', ctx=Load()),
                                    Name(id='version', ctx=Load()),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='path', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='os', ctx=Load()),
                                                attr='path',
                                                ctx=Load(),
                                            ),
                                            attr='join',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='path', ctx=Load()),
                                            Name(id='version', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    orelse=[
                        Assign(
                            targets=[Name(id='path', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='os', ctx=Load()),
                                    attr='getenv',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='XDG_CONFIG_DIRS', kind=None),
                                    Constant(value='/etc/xdg', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='pathlist', ctx=Store())],
                            value=ListComp(
                                elt=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='os', ctx=Load()),
                                            attr='path',
                                            ctx=Load(),
                                        ),
                                        attr='expanduser',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Call(
                                            func=Attribute(
                                                value=Name(id='x', ctx=Load()),
                                                attr='rstrip',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Attribute(
                                                    value=Name(id='os', ctx=Load()),
                                                    attr='sep',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='x', ctx=Store()),
                                        iter=Call(
                                            func=Attribute(
                                                value=Name(id='path', ctx=Load()),
                                                attr='split',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Attribute(
                                                    value=Name(id='os', ctx=Load()),
                                                    attr='pathsep',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='appname', ctx=Load()),
                            body=[
                                If(
                                    test=Name(id='version', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='appname', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='os', ctx=Load()),
                                                        attr='path',
                                                        ctx=Load(),
                                                    ),
                                                    attr='join',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='appname', ctx=Load()),
                                                    Name(id='version', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='pathlist', ctx=Store())],
                                    value=ListComp(
                                        elt=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id='os', ctx=Load()),
                                                    attr='sep',
                                                    ctx=Load(),
                                                ),
                                                attr='join',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                List(
                                                    elts=[
                                                        Name(id='x', ctx=Load()),
                                                        Name(id='appname', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='x', ctx=Store()),
                                                iter=Name(id='pathlist', ctx=Load()),
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
                        If(
                            test=Name(id='multipath', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='path', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='os', ctx=Load()),
                                                attr='pathsep',
                                                ctx=Load(),
                                            ),
                                            attr='join',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='pathlist', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='path', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='pathlist', ctx=Load()),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                    ],
                ),
                Return(
                    value=Name(id='path', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='user_cache_dir',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='appname', annotation=None, type_comment=None),
                    arg(arg='appauthor', annotation=None, type_comment=None),
                    arg(arg='version', annotation=None, type_comment=None),
                    arg(arg='opinion', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    Constant(value=None, kind=None),
                    Constant(value=None, kind=None),
                    Constant(value=None, kind=None),
                    Constant(value=True, kind=None),
                ],
            ),
            body=[
                Expr(
                    value=Constant(value='Return full path to the user-specific cache dir for this application.\n\n        "appname" is the name of application.\n            If None, just the system directory is returned.\n        "appauthor" (only required and used on Windows) is the name of the\n            appauthor or distributing body for this application. Typically\n            it is the owning company name. This falls back to appname.\n        "version" is an optional version path element to append to the\n            path. You might want to use this if you want multiple versions\n            of your app to be able to run independently. If used, this\n            would typically be "<major>.<minor>".\n            Only applied when appname is present.\n        "opinion" (boolean) can be False to disable the appending of\n            "Cache" to the base app data dir for Windows. See\n            discussion below.\n\n    Typical user cache directories are:\n        Mac OS X:   ~/Library/Caches/<AppName>\n        Unix:       ~/.cache/<AppName> (XDG default)\n        Win XP:     C:\\Documents and Settings\\<username>\\Local Settings\\Application Data\\<AppAuthor>\\<AppName>\\Cache\n        Vista:      C:\\Users\\<username>\\AppData\\Local\\<AppAuthor>\\<AppName>\\Cache\n\n    On Windows the only suggestion in the MSDN docs is that local settings go in\n    the `CSIDL_LOCAL_APPDATA` directory. This is identical to the non-roaming\n    app data dir (the default returned by `user_data_dir` above). Apps typically\n    put cache data somewhere *under* the given dir here. Some examples:\n        ...\\Mozilla\\Firefox\\Profiles\\<ProfileName>\\Cache\n        ...\\Acme\\SuperApp\\Cache\\1.0\n    OPINION: This function appends "Cache" to the `CSIDL_LOCAL_APPDATA` value.\n    This can be disabled with the `opinion=False` option.\n    ', kind=None),
                ),
                If(
                    test=Compare(
                        left=Attribute(
                            value=Name(id='sys', ctx=Load()),
                            attr='platform',
                            ctx=Load(),
                        ),
                        ops=[Eq()],
                        comparators=[Constant(value='win32', kind=None)],
                    ),
                    body=[
                        If(
                            test=Compare(
                                left=Name(id='appauthor', ctx=Load()),
                                ops=[Is()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='appauthor', ctx=Store())],
                                    value=Name(id='appname', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='path', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='os', ctx=Load()),
                                        attr='path',
                                        ctx=Load(),
                                    ),
                                    attr='normpath',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='_get_win_folder', ctx=Load()),
                                        args=[Constant(value='CSIDL_LOCAL_APPDATA', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='appname', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='path', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='os', ctx=Load()),
                                                attr='path',
                                                ctx=Load(),
                                            ),
                                            attr='join',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='path', ctx=Load()),
                                            Name(id='appauthor', ctx=Load()),
                                            Name(id='appname', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='opinion', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='path', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='os', ctx=Load()),
                                                        attr='path',
                                                        ctx=Load(),
                                                    ),
                                                    attr='join',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='path', ctx=Load()),
                                                    Constant(value='Cache', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    orelse=[
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='sys', ctx=Load()),
                                    attr='platform',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='darwin', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='path', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='os', ctx=Load()),
                                                attr='path',
                                                ctx=Load(),
                                            ),
                                            attr='expanduser',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='~/Library/Caches', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='appname', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='path', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='os', ctx=Load()),
                                                        attr='path',
                                                        ctx=Load(),
                                                    ),
                                                    attr='join',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='path', ctx=Load()),
                                                    Name(id='appname', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='path', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='os', ctx=Load()),
                                            attr='getenv',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='XDG_CACHE_HOME', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='os', ctx=Load()),
                                                        attr='path',
                                                        ctx=Load(),
                                                    ),
                                                    attr='expanduser',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='~/.cache', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='appname', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='path', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='os', ctx=Load()),
                                                        attr='path',
                                                        ctx=Load(),
                                                    ),
                                                    attr='join',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='path', ctx=Load()),
                                                    Name(id='appname', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                        ),
                    ],
                ),
                If(
                    test=BoolOp(
                        op=And(),
                        values=[
                            Name(id='appname', ctx=Load()),
                            Name(id='version', ctx=Load()),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='path', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='os', ctx=Load()),
                                        attr='path',
                                        ctx=Load(),
                                    ),
                                    attr='join',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='path', ctx=Load()),
                                    Name(id='version', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Name(id='path', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='user_log_dir',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='appname', annotation=None, type_comment=None),
                    arg(arg='appauthor', annotation=None, type_comment=None),
                    arg(arg='version', annotation=None, type_comment=None),
                    arg(arg='opinion', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    Constant(value=None, kind=None),
                    Constant(value=None, kind=None),
                    Constant(value=None, kind=None),
                    Constant(value=True, kind=None),
                ],
            ),
            body=[
                Expr(
                    value=Constant(value='Return full path to the user-specific log dir for this application.\n\n        "appname" is the name of application.\n            If None, just the system directory is returned.\n        "appauthor" (only required and used on Windows) is the name of the\n            appauthor or distributing body for this application. Typically\n            it is the owning company name. This falls back to appname.\n        "version" is an optional version path element to append to the\n            path. You might want to use this if you want multiple versions\n            of your app to be able to run independently. If used, this\n            would typically be "<major>.<minor>".\n            Only applied when appname is present.\n        "opinion" (boolean) can be False to disable the appending of\n            "Logs" to the base app data dir for Windows, and "log" to the\n            base cache dir for Unix. See discussion below.\n\n    Typical user cache directories are:\n        Mac OS X:   ~/Library/Logs/<AppName>\n        Unix:       ~/.cache/<AppName>/log  # or under $XDG_CACHE_HOME if defined\n        Win XP:     C:\\Documents and Settings\\<username>\\Local Settings\\Application Data\\<AppAuthor>\\<AppName>\\Logs\n        Vista:      C:\\Users\\<username>\\AppData\\Local\\<AppAuthor>\\<AppName>\\Logs\n\n    On Windows the only suggestion in the MSDN docs is that local settings\n    go in the `CSIDL_LOCAL_APPDATA` directory. (Note: I\'m interested in\n    examples of what some windows apps use for a logs dir.)\n\n    OPINION: This function appends "Logs" to the `CSIDL_LOCAL_APPDATA`\n    value for Windows and appends "log" to the user cache dir for Unix.\n    This can be disabled with the `opinion=False` option.\n    ', kind=None),
                ),
                If(
                    test=Compare(
                        left=Attribute(
                            value=Name(id='sys', ctx=Load()),
                            attr='platform',
                            ctx=Load(),
                        ),
                        ops=[Eq()],
                        comparators=[Constant(value='darwin', kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='path', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='os', ctx=Load()),
                                        attr='path',
                                        ctx=Load(),
                                    ),
                                    attr='join',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='os', ctx=Load()),
                                                attr='path',
                                                ctx=Load(),
                                            ),
                                            attr='expanduser',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='~/Library/Logs', kind=None)],
                                        keywords=[],
                                    ),
                                    Name(id='appname', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='sys', ctx=Load()),
                                    attr='platform',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='win32', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='path', ctx=Store())],
                                    value=Call(
                                        func=Name(id='user_data_dir', ctx=Load()),
                                        args=[
                                            Name(id='appname', ctx=Load()),
                                            Name(id='appauthor', ctx=Load()),
                                            Name(id='version', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='version', ctx=Store())],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='opinion', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='path', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='os', ctx=Load()),
                                                        attr='path',
                                                        ctx=Load(),
                                                    ),
                                                    attr='join',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='path', ctx=Load()),
                                                    Constant(value='Logs', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='path', ctx=Store())],
                                    value=Call(
                                        func=Name(id='user_cache_dir', ctx=Load()),
                                        args=[
                                            Name(id='appname', ctx=Load()),
                                            Name(id='appauthor', ctx=Load()),
                                            Name(id='version', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='version', ctx=Store())],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='opinion', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='path', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='os', ctx=Load()),
                                                        attr='path',
                                                        ctx=Load(),
                                                    ),
                                                    attr='join',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='path', ctx=Load()),
                                                    Constant(value='log', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                        ),
                    ],
                ),
                If(
                    test=BoolOp(
                        op=And(),
                        values=[
                            Name(id='appname', ctx=Load()),
                            Name(id='version', ctx=Load()),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='path', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='os', ctx=Load()),
                                        attr='path',
                                        ctx=Load(),
                                    ),
                                    attr='join',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='path', ctx=Load()),
                                    Name(id='version', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Name(id='path', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        ClassDef(
            name='AppDirs',
            bases=[Name(id='object', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value='Convenience wrapper for getting application dirs.', kind=None),
                ),
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='appname', annotation=None, type_comment=None),
                            arg(arg='appauthor', annotation=None, type_comment=None),
                            arg(arg='version', annotation=None, type_comment=None),
                            arg(arg='roaming', annotation=None, type_comment=None),
                            arg(arg='multipath', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=False, kind=None),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='appname',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='appname', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='appauthor',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='appauthor', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='version',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='version', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='roaming',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='roaming', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='multipath',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='multipath', ctx=Load()),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='user_data_dir',
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
                                func=Name(id='user_data_dir', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='appname',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='appauthor',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='version',
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='version',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='roaming',
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='roaming',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='property', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='site_data_dir',
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
                                func=Name(id='site_data_dir', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='appname',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='appauthor',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='version',
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='version',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='multipath',
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='multipath',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='property', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='user_config_dir',
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
                                func=Name(id='user_config_dir', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='appname',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='appauthor',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='version',
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='version',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='roaming',
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='roaming',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='property', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='site_config_dir',
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
                                func=Name(id='site_data_dir', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='appname',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='appauthor',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='version',
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='version',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='multipath',
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='multipath',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='property', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='user_cache_dir',
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
                                func=Name(id='user_cache_dir', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='appname',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='appauthor',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='version',
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='version',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='property', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='user_log_dir',
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
                                func=Name(id='user_log_dir', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='appname',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='appauthor',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='version',
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='version',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
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
        FunctionDef(
            name='_get_win_folder_from_registry',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='csidl_name', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value="This is a fallback technique at best. I'm not sure if using the\n    registry for this guarantees us the correct answer for all CSIDL_*\n    names.\n    ", kind=None),
                ),
                Import(
                    names=[alias(name='winreg', asname='_winreg')],
                ),
                Assign(
                    targets=[Name(id='shell_folder_name', ctx=Store())],
                    value=Subscript(
                        value=Dict(
                            keys=[
                                Constant(value='CSIDL_APPDATA', kind=None),
                                Constant(value='CSIDL_COMMON_APPDATA', kind=None),
                                Constant(value='CSIDL_LOCAL_APPDATA', kind=None),
                            ],
                            values=[
                                Constant(value='AppData', kind=None),
                                Constant(value='Common AppData', kind=None),
                                Constant(value='Local AppData', kind=None),
                            ],
                        ),
                        slice=Name(id='csidl_name', ctx=Load()),
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='key', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='_winreg', ctx=Load()),
                            attr='OpenKey',
                            ctx=Load(),
                        ),
                        args=[
                            Attribute(
                                value=Name(id='_winreg', ctx=Load()),
                                attr='HKEY_CURRENT_USER',
                                ctx=Load(),
                            ),
                            Constant(value='Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Shell Folders', kind=None),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[
                        Tuple(
                            elts=[
                                Name(id='dir', ctx=Store()),
                                Name(id='type', ctx=Store()),
                            ],
                            ctx=Store(),
                        ),
                    ],
                    value=Call(
                        func=Attribute(
                            value=Name(id='_winreg', ctx=Load()),
                            attr='QueryValueEx',
                            ctx=Load(),
                        ),
                        args=[
                            Name(id='key', ctx=Load()),
                            Name(id='shell_folder_name', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Return(
                    value=Name(id='dir', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='_get_win_folder_with_pywin32',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='csidl_name', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                ImportFrom(
                    module='win32com.shell',
                    names=[
                        alias(name='shellcon', asname=None),
                        alias(name='shell', asname=None),
                    ],
                    level=0,
                ),
                Assign(
                    targets=[Name(id='dir', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='shell', ctx=Load()),
                            attr='SHGetFolderPath',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value=0, kind=None),
                            Call(
                                func=Name(id='getattr', ctx=Load()),
                                args=[
                                    Name(id='shellcon', ctx=Load()),
                                    Name(id='csidl_name', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            Constant(value=0, kind=None),
                            Constant(value=0, kind=None),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Try(
                    body=[
                        Assign(
                            targets=[Name(id='dir', ctx=Store())],
                            value=Call(
                                func=Name(id='str', ctx=Load()),
                                args=[Name(id='dir', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='has_high_char', ctx=Store())],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='c', ctx=Store()),
                            iter=Name(id='dir', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Call(
                                            func=Name(id='ord', ctx=Load()),
                                            args=[Name(id='c', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ops=[Gt()],
                                        comparators=[Constant(value=255, kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='has_high_char', ctx=Store())],
                                            value=Constant(value=True, kind=None),
                                            type_comment=None,
                                        ),
                                        Break(),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='has_high_char', ctx=Load()),
                            body=[
                                Try(
                                    body=[
                                        Import(
                                            names=[alias(name='win32api', asname=None)],
                                        ),
                                        Assign(
                                            targets=[Name(id='dir', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='win32api', ctx=Load()),
                                                    attr='GetShortPathName',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='dir', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='ImportError', ctx=Load()),
                                            name=None,
                                            body=[Pass()],
                                        ),
                                    ],
                                    orelse=[],
                                    finalbody=[],
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    handlers=[
                        ExceptHandler(
                            type=Name(id='UnicodeError', ctx=Load()),
                            name=None,
                            body=[Pass()],
                        ),
                    ],
                    orelse=[],
                    finalbody=[],
                ),
                Return(
                    value=Name(id='dir', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='_get_win_folder_with_ctypes',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='csidl_name', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Import(
                    names=[alias(name='ctypes', asname=None)],
                ),
                Assign(
                    targets=[Name(id='csidl_const', ctx=Store())],
                    value=Subscript(
                        value=Dict(
                            keys=[
                                Constant(value='CSIDL_APPDATA', kind=None),
                                Constant(value='CSIDL_COMMON_APPDATA', kind=None),
                                Constant(value='CSIDL_LOCAL_APPDATA', kind=None),
                            ],
                            values=[
                                Constant(value=26, kind=None),
                                Constant(value=35, kind=None),
                                Constant(value=28, kind=None),
                            ],
                        ),
                        slice=Name(id='csidl_name', ctx=Load()),
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='buf', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='ctypes', ctx=Load()),
                            attr='create_unicode_buffer',
                            ctx=Load(),
                        ),
                        args=[Constant(value=1024, kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='ctypes', ctx=Load()),
                                    attr='windll',
                                    ctx=Load(),
                                ),
                                attr='shell32',
                                ctx=Load(),
                            ),
                            attr='SHGetFolderPathW',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value=None, kind=None),
                            Name(id='csidl_const', ctx=Load()),
                            Constant(value=None, kind=None),
                            Constant(value=0, kind=None),
                            Name(id='buf', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                ),
                Assign(
                    targets=[Name(id='has_high_char', ctx=Store())],
                    value=Constant(value=False, kind=None),
                    type_comment=None,
                ),
                For(
                    target=Name(id='c', ctx=Store()),
                    iter=Name(id='buf', ctx=Load()),
                    body=[
                        If(
                            test=Compare(
                                left=Call(
                                    func=Name(id='ord', ctx=Load()),
                                    args=[Name(id='c', ctx=Load())],
                                    keywords=[],
                                ),
                                ops=[Gt()],
                                comparators=[Constant(value=255, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='has_high_char', ctx=Store())],
                                    value=Constant(value=True, kind=None),
                                    type_comment=None,
                                ),
                                Break(),
                            ],
                            orelse=[],
                        ),
                    ],
                    orelse=[],
                    type_comment=None,
                ),
                If(
                    test=Name(id='has_high_char', ctx=Load()),
                    body=[
                        Assign(
                            targets=[Name(id='buf2', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='ctypes', ctx=Load()),
                                    attr='create_unicode_buffer',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=1024, kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='ctypes', ctx=Load()),
                                            attr='windll',
                                            ctx=Load(),
                                        ),
                                        attr='kernel32',
                                        ctx=Load(),
                                    ),
                                    attr='GetShortPathNameW',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='buf', ctx=Load()),
                                        attr='value',
                                        ctx=Load(),
                                    ),
                                    Name(id='buf2', ctx=Load()),
                                    Constant(value=1024, kind=None),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='buf', ctx=Store())],
                                    value=Name(id='buf2', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Attribute(
                        value=Name(id='buf', ctx=Load()),
                        attr='value',
                        ctx=Load(),
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        If(
            test=Compare(
                left=Attribute(
                    value=Name(id='sys', ctx=Load()),
                    attr='platform',
                    ctx=Load(),
                ),
                ops=[Eq()],
                comparators=[Constant(value='win32', kind=None)],
            ),
            body=[
                Try(
                    body=[
                        Import(
                            names=[alias(name='win32com.shell', asname=None)],
                        ),
                        Assign(
                            targets=[Name(id='_get_win_folder', ctx=Store())],
                            value=Name(id='_get_win_folder_with_pywin32', ctx=Load()),
                            type_comment=None,
                        ),
                    ],
                    handlers=[
                        ExceptHandler(
                            type=Name(id='ImportError', ctx=Load()),
                            name=None,
                            body=[
                                Try(
                                    body=[
                                        Import(
                                            names=[alias(name='ctypes', asname=None)],
                                        ),
                                        Assign(
                                            targets=[Name(id='_get_win_folder', ctx=Store())],
                                            value=Name(id='_get_win_folder_with_ctypes', ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='ImportError', ctx=Load()),
                                            name=None,
                                            body=[
                                                Assign(
                                                    targets=[Name(id='_get_win_folder', ctx=Store())],
                                                    value=Name(id='_get_win_folder_from_registry', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                    finalbody=[],
                                ),
                            ],
                        ),
                    ],
                    orelse=[],
                    finalbody=[],
                ),
            ],
            orelse=[],
        ),
        If(
            test=Compare(
                left=Name(id='__name__', ctx=Load()),
                ops=[Eq()],
                comparators=[Constant(value='__main__', kind=None)],
            ),
            body=[
                Assign(
                    targets=[Name(id='appname', ctx=Store())],
                    value=Constant(value='MyApp', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='appauthor', ctx=Store())],
                    value=Constant(value='MyCompany', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='props', ctx=Store())],
                    value=Tuple(
                        elts=[
                            Constant(value='user_data_dir', kind=None),
                            Constant(value='site_data_dir', kind=None),
                            Constant(value='user_config_dir', kind=None),
                            Constant(value='site_config_dir', kind=None),
                            Constant(value='user_cache_dir', kind=None),
                            Constant(value='user_log_dir', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Expr(
                    value=Call(
                        func=Name(id='print', ctx=Load()),
                        args=[Constant(value="-- app dirs (with optional 'version')", kind=None)],
                        keywords=[],
                    ),
                ),
                Assign(
                    targets=[Name(id='dirs', ctx=Store())],
                    value=Call(
                        func=Name(id='AppDirs', ctx=Load()),
                        args=[
                            Name(id='appname', ctx=Load()),
                            Name(id='appauthor', ctx=Load()),
                        ],
                        keywords=[
                            keyword(
                                arg='version',
                                value=Constant(value='1.0', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                For(
                    target=Name(id='prop', ctx=Store()),
                    iter=Name(id='props', ctx=Load()),
                    body=[
                        Expr(
                            value=Call(
                                func=Name(id='print', ctx=Load()),
                                args=[
                                    BinOp(
                                        left=Constant(value='%s: %s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Name(id='prop', ctx=Load()),
                                                Call(
                                                    func=Name(id='getattr', ctx=Load()),
                                                    args=[
                                                        Name(id='dirs', ctx=Load()),
                                                        Name(id='prop', ctx=Load()),
                                                    ],
                                                    keywords=[],
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
                    orelse=[],
                    type_comment=None,
                ),
                Expr(
                    value=Call(
                        func=Name(id='print', ctx=Load()),
                        args=[Constant(value="\n-- app dirs (without optional 'version')", kind=None)],
                        keywords=[],
                    ),
                ),
                Assign(
                    targets=[Name(id='dirs', ctx=Store())],
                    value=Call(
                        func=Name(id='AppDirs', ctx=Load()),
                        args=[
                            Name(id='appname', ctx=Load()),
                            Name(id='appauthor', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                For(
                    target=Name(id='prop', ctx=Store()),
                    iter=Name(id='props', ctx=Load()),
                    body=[
                        Expr(
                            value=Call(
                                func=Name(id='print', ctx=Load()),
                                args=[
                                    BinOp(
                                        left=Constant(value='%s: %s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Name(id='prop', ctx=Load()),
                                                Call(
                                                    func=Name(id='getattr', ctx=Load()),
                                                    args=[
                                                        Name(id='dirs', ctx=Load()),
                                                        Name(id='prop', ctx=Load()),
                                                    ],
                                                    keywords=[],
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
                    orelse=[],
                    type_comment=None,
                ),
                Expr(
                    value=Call(
                        func=Name(id='print', ctx=Load()),
                        args=[Constant(value="\n-- app dirs (without optional 'appauthor')", kind=None)],
                        keywords=[],
                    ),
                ),
                Assign(
                    targets=[Name(id='dirs', ctx=Store())],
                    value=Call(
                        func=Name(id='AppDirs', ctx=Load()),
                        args=[Name(id='appname', ctx=Load())],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                For(
                    target=Name(id='prop', ctx=Store()),
                    iter=Name(id='props', ctx=Load()),
                    body=[
                        Expr(
                            value=Call(
                                func=Name(id='print', ctx=Load()),
                                args=[
                                    BinOp(
                                        left=Constant(value='%s: %s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Name(id='prop', ctx=Load()),
                                                Call(
                                                    func=Name(id='getattr', ctx=Load()),
                                                    args=[
                                                        Name(id='dirs', ctx=Load()),
                                                        Name(id='prop', ctx=Load()),
                                                    ],
                                                    keywords=[],
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
                    orelse=[],
                    type_comment=None,
                ),
            ],
            orelse=[],
        ),
    ],
    type_ignores=[],
)
