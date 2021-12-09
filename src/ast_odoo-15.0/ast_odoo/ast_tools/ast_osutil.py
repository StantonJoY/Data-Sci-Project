Module(
    body=[
        Expr(
            value=Constant(value='\nSome functions related to the os and os.path module\n', kind=None),
        ),
        Import(
            names=[alias(name='logging', asname=None)],
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
        Import(
            names=[alias(name='zipfile', asname=None)],
        ),
        ImportFrom(
            module='contextlib',
            names=[alias(name='contextmanager', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='os.path',
            names=[alias(name='join', asname='opj')],
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
        Assign(
            targets=[Name(id='WINDOWS_RESERVED', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='re', ctx=Load()),
                    attr='compile',
                    ctx=Load(),
                ),
                args=[Constant(value='\n    ^\n    # forbidden stems: reserved keywords\n    (:?CON|PRN|AUX|NUL|COM[1-9]|LPT[1-9])\n    # even with an extension this is recommended against\n    (:?\\..*)?\n    $\n', kind=None)],
                keywords=[
                    keyword(
                        arg='flags',
                        value=BinOp(
                            left=Attribute(
                                value=Name(id='re', ctx=Load()),
                                attr='IGNORECASE',
                                ctx=Load(),
                            ),
                            op=BitOr(),
                            right=Attribute(
                                value=Name(id='re', ctx=Load()),
                                attr='VERBOSE',
                                ctx=Load(),
                            ),
                        ),
                    ),
                ],
            ),
            type_comment=None,
        ),
        FunctionDef(
            name='clean_filename',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='name', annotation=None, type_comment=None),
                    arg(arg='replacement', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[Constant(value='', kind=None)],
            ),
            body=[
                Expr(
                    value=Constant(value=' Strips or replaces possibly problematic or annoying characters our of\n    the input string, in order to make it a valid filename in most operating\n    systems (including dropping reserved Windows filenames).\n\n    If this results in an empty string, results in "Untitled" (localized).\n\n    Allows:\n\n    * any alphanumeric character (unicode)\n    * underscore (_) as that\'s innocuous\n    * dot (.) except in leading position to avoid creating dotfiles\n    * dash (-) except in leading position to avoid annoyance / confusion with\n      command options\n    * brackets ([ and ]), while they correspond to shell *character class*\n      they\'re a common way to mark / tag files especially on windows\n    * parenthesis ("(" and ")"), a more natural though less common version of\n      the former\n    * space (" ")\n\n    :param str name: file name to clean up\n    :param str replacement:\n        replacement string to use for sequences of problematic input, by default\n        an empty string to remove them entirely, each contiguous sequence of\n        problems is replaced by a single replacement\n    :rtype: str\n    ', kind=None),
                ),
                If(
                    test=Call(
                        func=Attribute(
                            value=Name(id='WINDOWS_RESERVED', ctx=Load()),
                            attr='match',
                            ctx=Load(),
                        ),
                        args=[Name(id='name', ctx=Load())],
                        keywords=[],
                    ),
                    body=[
                        Return(
                            value=Constant(value='Untitled', kind=None),
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=BoolOp(
                        op=Or(),
                        values=[
                            Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='re', ctx=Load()),
                                            attr='sub',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='[^\\w_.()\\[\\] -]+', kind=None),
                                            Name(id='replacement', ctx=Load()),
                                            Name(id='name', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='lstrip',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='.-', kind=None)],
                                keywords=[],
                            ),
                            Constant(value='Untitled', kind=None),
                        ],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='listdir',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='dir', annotation=None, type_comment=None),
                    arg(arg='recursive', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[Constant(value=False, kind=None)],
            ),
            body=[
                Expr(
                    value=Constant(value='Allow to recursively get the file listing following symlinks, returns\n    paths relative to the provided `dir` except completely broken if the symlink\n    it follows leaves `dir`...\n    ', kind=None),
                ),
                If(
                    test=UnaryOp(
                        op=Not(),
                        operand=Name(id='recursive', ctx=Load()),
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='getChild',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='listdir', kind=None)],
                                        keywords=[],
                                    ),
                                    attr='warning',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='Deprecated: just call os.listdir...', kind=None)],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    targets=[Name(id='dir', ctx=Store())],
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
                        args=[Name(id='dir', ctx=Load())],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=UnaryOp(
                        op=Not(),
                        operand=Name(id='recursive', ctx=Load()),
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='os', ctx=Load()),
                                    attr='listdir',
                                    ctx=Load(),
                                ),
                                args=[Name(id='dir', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    targets=[Name(id='res', ctx=Store())],
                    value=List(elts=[], ctx=Load()),
                    type_comment=None,
                ),
                For(
                    target=Tuple(
                        elts=[
                            Name(id='root', ctx=Store()),
                            Name(id='_', ctx=Store()),
                            Name(id='files', ctx=Store()),
                        ],
                        ctx=Store(),
                    ),
                    iter=Call(
                        func=Attribute(
                            value=Name(id='os', ctx=Load()),
                            attr='walk',
                            ctx=Load(),
                        ),
                        args=[Name(id='dir', ctx=Load())],
                        keywords=[
                            keyword(
                                arg='followlinks',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='r', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='os', ctx=Load()),
                                        attr='path',
                                        ctx=Load(),
                                    ),
                                    attr='relpath',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='root', ctx=Load()),
                                    Name(id='dir', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=YieldFrom(
                                value=GeneratorExp(
                                    elt=Call(
                                        func=Name(id='opj', ctx=Load()),
                                        args=[
                                            Name(id='r', ctx=Load()),
                                            Name(id='f', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    generators=[
                                        comprehension(
                                            target=Name(id='f', ctx=Store()),
                                            iter=Name(id='files', ctx=Load()),
                                            ifs=[],
                                            is_async=0,
                                        ),
                                    ],
                                ),
                            ),
                        ),
                    ],
                    orelse=[],
                    type_comment=None,
                ),
                Return(
                    value=Name(id='res', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='walksymlinks',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='top', annotation=None, type_comment=None),
                    arg(arg='topdown', annotation=None, type_comment=None),
                    arg(arg='onerror', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    Constant(value=True, kind=None),
                    Constant(value=None, kind=None),
                ],
            ),
            body=[
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='getChild',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='walksymlinks', kind=None)],
                                keywords=[],
                            ),
                            attr='warning',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Deprecated: use os.walk(followlinks=True) instead', kind=None)],
                        keywords=[],
                    ),
                ),
                Return(
                    value=Call(
                        func=Attribute(
                            value=Name(id='os', ctx=Load()),
                            attr='walk',
                            ctx=Load(),
                        ),
                        args=[Name(id='top', ctx=Load())],
                        keywords=[
                            keyword(
                                arg='topdown',
                                value=Name(id='topdown', ctx=Load()),
                            ),
                            keyword(
                                arg='onerror',
                                value=Name(id='onerror', ctx=Load()),
                            ),
                            keyword(
                                arg='followlinks',
                                value=Constant(value=True, kind=None),
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
            name='tempdir',
            args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
            body=[
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='getChild',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='tempdir', kind=None)],
                                keywords=[],
                            ),
                            attr='warning',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Deprecated: use tempfile.TemporaryDirectory', kind=None)],
                        keywords=[],
                    ),
                ),
                With(
                    items=[
                        withitem(
                            context_expr=Call(
                                func=Attribute(
                                    value=Name(id='tempfile', ctx=Load()),
                                    attr='TemporaryDirectory',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            optional_vars=Name(id='d', ctx=Store()),
                        ),
                    ],
                    body=[
                        Expr(
                            value=Yield(
                                value=Name(id='d', ctx=Load()),
                            ),
                        ),
                    ],
                    type_comment=None,
                ),
            ],
            decorator_list=[Name(id='contextmanager', ctx=Load())],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='zip_dir',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='path', annotation=None, type_comment=None),
                    arg(arg='stream', annotation=None, type_comment=None),
                    arg(arg='include_dir', annotation=None, type_comment=None),
                    arg(arg='fnct_sort', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    Constant(value=True, kind=None),
                    Constant(value=None, kind=None),
                ],
            ),
            body=[
                Expr(
                    value=Constant(value='\n    : param fnct_sort : Function to be passed to "key" parameter of built-in\n                        python sorted() to provide flexibility of sorting files\n                        inside ZIP archive according to specific requirements.\n    ', kind=None),
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
                        args=[Name(id='path', ctx=Load())],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='len_prefix', ctx=Store())],
                    value=IfExp(
                        test=Name(id='include_dir', ctx=Load()),
                        body=Call(
                            func=Name(id='len', ctx=Load()),
                            args=[
                                Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='os', ctx=Load()),
                                            attr='path',
                                            ctx=Load(),
                                        ),
                                        attr='dirname',
                                        ctx=Load(),
                                    ),
                                    args=[Name(id='path', ctx=Load())],
                                    keywords=[],
                                ),
                            ],
                            keywords=[],
                        ),
                        orelse=Call(
                            func=Name(id='len', ctx=Load()),
                            args=[Name(id='path', ctx=Load())],
                            keywords=[],
                        ),
                    ),
                    type_comment=None,
                ),
                If(
                    test=Name(id='len_prefix', ctx=Load()),
                    body=[
                        AugAssign(
                            target=Name(id='len_prefix', ctx=Store()),
                            op=Add(),
                            value=Constant(value=1, kind=None),
                        ),
                    ],
                    orelse=[],
                ),
                With(
                    items=[
                        withitem(
                            context_expr=Call(
                                func=Attribute(
                                    value=Name(id='zipfile', ctx=Load()),
                                    attr='ZipFile',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='stream', ctx=Load()),
                                    Constant(value='w', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='compression',
                                        value=Attribute(
                                            value=Name(id='zipfile', ctx=Load()),
                                            attr='ZIP_DEFLATED',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='allowZip64',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                            optional_vars=Name(id='zipf', ctx=Store()),
                        ),
                    ],
                    body=[
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='dirpath', ctx=Store()),
                                    Name(id='dirnames', ctx=Store()),
                                    Name(id='filenames', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='os', ctx=Load()),
                                    attr='walk',
                                    ctx=Load(),
                                ),
                                args=[Name(id='path', ctx=Load())],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='filenames', ctx=Store())],
                                    value=Call(
                                        func=Name(id='sorted', ctx=Load()),
                                        args=[Name(id='filenames', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='key',
                                                value=Name(id='fnct_sort', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='fname', ctx=Store()),
                                    iter=Name(id='filenames', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Tuple(
                                                    elts=[
                                                        Name(id='bname', ctx=Store()),
                                                        Name(id='ext', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='os', ctx=Load()),
                                                        attr='path',
                                                        ctx=Load(),
                                                    ),
                                                    attr='splitext',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='fname', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='ext', ctx=Store())],
                                            value=BoolOp(
                                                op=Or(),
                                                values=[
                                                    Name(id='ext', ctx=Load()),
                                                    Name(id='bname', ctx=Load()),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Name(id='ext', ctx=Load()),
                                                ops=[NotIn()],
                                                comparators=[
                                                    List(
                                                        elts=[
                                                            Constant(value='.pyc', kind=None),
                                                            Constant(value='.pyo', kind=None),
                                                            Constant(value='.swp', kind=None),
                                                            Constant(value='.DS_Store', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
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
                                                            attr='normpath',
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
                                                                    attr='join',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Name(id='dirpath', ctx=Load()),
                                                                    Name(id='fname', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='os', ctx=Load()),
                                                                attr='path',
                                                                ctx=Load(),
                                                            ),
                                                            attr='isfile',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='path', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='zipf', ctx=Load()),
                                                                    attr='write',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Name(id='path', ctx=Load()),
                                                                    Subscript(
                                                                        value=Name(id='path', ctx=Load()),
                                                                        slice=Slice(
                                                                            lower=Name(id='len_prefix', ctx=Load()),
                                                                            upper=None,
                                                                            step=None,
                                                                        ),
                                                                        ctx=Load(),
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
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    type_comment=None,
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        If(
            test=Compare(
                left=Attribute(
                    value=Name(id='os', ctx=Load()),
                    attr='name',
                    ctx=Load(),
                ),
                ops=[NotEq()],
                comparators=[Constant(value='nt', kind=None)],
            ),
            body=[
                Assign(
                    targets=[Name(id='getppid', ctx=Store())],
                    value=Attribute(
                        value=Name(id='os', ctx=Load()),
                        attr='getppid',
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='is_running_as_nt_service', ctx=Store())],
                    value=Lambda(
                        args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
                        body=Constant(value=False, kind=None),
                    ),
                    type_comment=None,
                ),
            ],
            orelse=[
                Import(
                    names=[alias(name='ctypes', asname=None)],
                ),
                Import(
                    names=[alias(name='win32service', asname='ws')],
                ),
                Import(
                    names=[alias(name='win32serviceutil', asname='wsu')],
                ),
                Assign(
                    targets=[Name(id='_TH32CS_SNAPPROCESS', ctx=Store())],
                    value=Constant(value=2, kind=None),
                    type_comment=None,
                ),
                ClassDef(
                    name='_PROCESSENTRY32',
                    bases=[
                        Attribute(
                            value=Name(id='ctypes', ctx=Load()),
                            attr='Structure',
                            ctx=Load(),
                        ),
                    ],
                    keywords=[],
                    body=[
                        Assign(
                            targets=[Name(id='_fields_', ctx=Store())],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='dwSize', kind=None),
                                            Attribute(
                                                value=Name(id='ctypes', ctx=Load()),
                                                attr='c_ulong',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='cntUsage', kind=None),
                                            Attribute(
                                                value=Name(id='ctypes', ctx=Load()),
                                                attr='c_ulong',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='th32ProcessID', kind=None),
                                            Attribute(
                                                value=Name(id='ctypes', ctx=Load()),
                                                attr='c_ulong',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='th32DefaultHeapID', kind=None),
                                            Attribute(
                                                value=Name(id='ctypes', ctx=Load()),
                                                attr='c_ulong',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='th32ModuleID', kind=None),
                                            Attribute(
                                                value=Name(id='ctypes', ctx=Load()),
                                                attr='c_ulong',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='cntThreads', kind=None),
                                            Attribute(
                                                value=Name(id='ctypes', ctx=Load()),
                                                attr='c_ulong',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='th32ParentProcessID', kind=None),
                                            Attribute(
                                                value=Name(id='ctypes', ctx=Load()),
                                                attr='c_ulong',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='pcPriClassBase', kind=None),
                                            Attribute(
                                                value=Name(id='ctypes', ctx=Load()),
                                                attr='c_ulong',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='dwFlags', kind=None),
                                            Attribute(
                                                value=Name(id='ctypes', ctx=Load()),
                                                attr='c_ulong',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='szExeFile', kind=None),
                                            BinOp(
                                                left=Attribute(
                                                    value=Name(id='ctypes', ctx=Load()),
                                                    attr='c_char',
                                                    ctx=Load(),
                                                ),
                                                op=Mult(),
                                                right=Constant(value=260, kind=None),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                ),
                FunctionDef(
                    name='getppid',
                    args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
                    body=[
                        Assign(
                            targets=[Name(id='CreateToolhelp32Snapshot', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Attribute(
                                        value=Name(id='ctypes', ctx=Load()),
                                        attr='windll',
                                        ctx=Load(),
                                    ),
                                    attr='kernel32',
                                    ctx=Load(),
                                ),
                                attr='CreateToolhelp32Snapshot',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='Process32First', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Attribute(
                                        value=Name(id='ctypes', ctx=Load()),
                                        attr='windll',
                                        ctx=Load(),
                                    ),
                                    attr='kernel32',
                                    ctx=Load(),
                                ),
                                attr='Process32First',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='Process32Next', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Attribute(
                                        value=Name(id='ctypes', ctx=Load()),
                                        attr='windll',
                                        ctx=Load(),
                                    ),
                                    attr='kernel32',
                                    ctx=Load(),
                                ),
                                attr='Process32Next',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='CloseHandle', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Attribute(
                                        value=Name(id='ctypes', ctx=Load()),
                                        attr='windll',
                                        ctx=Load(),
                                    ),
                                    attr='kernel32',
                                    ctx=Load(),
                                ),
                                attr='CloseHandle',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='hProcessSnap', ctx=Store())],
                            value=Call(
                                func=Name(id='CreateToolhelp32Snapshot', ctx=Load()),
                                args=[
                                    Name(id='_TH32CS_SNAPPROCESS', ctx=Load()),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='current_pid', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='os', ctx=Load()),
                                    attr='getpid',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id='pe32', ctx=Store())],
                                    value=Call(
                                        func=Name(id='_PROCESSENTRY32', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='pe32', ctx=Load()),
                                            attr='dwSize',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='ctypes', ctx=Load()),
                                            attr='sizeof',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='_PROCESSENTRY32', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Name(id='Process32First', ctx=Load()),
                                            args=[
                                                Name(id='hProcessSnap', ctx=Load()),
                                                Call(
                                                    func=Attribute(
                                                        value=Name(id='ctypes', ctx=Load()),
                                                        attr='byref',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='pe32', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='OSError', ctx=Load()),
                                                args=[Constant(value='Failed getting first process.', kind=None)],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                While(
                                    test=Constant(value=True, kind=None),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='pe32', ctx=Load()),
                                                    attr='th32ProcessID',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Name(id='current_pid', ctx=Load())],
                                            ),
                                            body=[
                                                Return(
                                                    value=Attribute(
                                                        value=Name(id='pe32', ctx=Load()),
                                                        attr='th32ParentProcessID',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Call(
                                                    func=Name(id='Process32Next', ctx=Load()),
                                                    args=[
                                                        Name(id='hProcessSnap', ctx=Load()),
                                                        Call(
                                                            func=Attribute(
                                                                value=Name(id='ctypes', ctx=Load()),
                                                                attr='byref',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Name(id='pe32', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                            body=[
                                                Return(
                                                    value=Constant(value=None, kind=None),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            handlers=[],
                            orelse=[],
                            finalbody=[
                                Expr(
                                    value=Call(
                                        func=Name(id='CloseHandle', ctx=Load()),
                                        args=[Name(id='hProcessSnap', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                ImportFrom(
                    module='contextlib',
                    names=[alias(name='contextmanager', asname=None)],
                    level=0,
                ),
                ImportFrom(
                    module='odoo.release',
                    names=[alias(name='nt_service_name', asname=None)],
                    level=0,
                ),
                FunctionDef(
                    name='is_running_as_nt_service',
                    args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
                    body=[
                        FunctionDef(
                            name='close_srv',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='srv', annotation=None, type_comment=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Try(
                                    body=[
                                        Expr(
                                            value=Yield(
                                                value=Name(id='srv', ctx=Load()),
                                            ),
                                        ),
                                    ],
                                    handlers=[],
                                    orelse=[],
                                    finalbody=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='ws', ctx=Load()),
                                                    attr='CloseServiceHandle',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='srv', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            decorator_list=[Name(id='contextmanager', ctx=Load())],
                            returns=None,
                            type_comment=None,
                        ),
                        Try(
                            body=[
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                func=Name(id='close_srv', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='ws', ctx=Load()),
                                                            attr='OpenSCManager',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value=None, kind=None),
                                                            Constant(value=None, kind=None),
                                                            Attribute(
                                                                value=Name(id='ws', ctx=Load()),
                                                                attr='SC_MANAGER_ALL_ACCESS',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            optional_vars=Name(id='hscm', ctx=Store()),
                                        ),
                                    ],
                                    body=[
                                        With(
                                            items=[
                                                withitem(
                                                    context_expr=Call(
                                                        func=Name(id='close_srv', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='wsu', ctx=Load()),
                                                                    attr='SmartOpenService',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Name(id='hscm', ctx=Load()),
                                                                    Name(id='nt_service_name', ctx=Load()),
                                                                    Attribute(
                                                                        value=Name(id='ws', ctx=Load()),
                                                                        attr='SERVICE_ALL_ACCESS',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    optional_vars=Name(id='hs', ctx=Store()),
                                                ),
                                            ],
                                            body=[
                                                Assign(
                                                    targets=[Name(id='info', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='ws', ctx=Load()),
                                                            attr='QueryServiceStatusEx',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='hs', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Return(
                                                    value=Compare(
                                                        left=Subscript(
                                                            value=Name(id='info', ctx=Load()),
                                                            slice=Constant(value='ProcessId', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[
                                                            Call(
                                                                func=Name(id='getppid', ctx=Load()),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                    ),
                                                ),
                                            ],
                                            type_comment=None,
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
                                        Return(
                                            value=Constant(value=False, kind=None),
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
            ],
        ),
        If(
            test=Compare(
                left=Name(id='__name__', ctx=Load()),
                ops=[Eq()],
                comparators=[Constant(value='__main__', kind=None)],
            ),
            body=[
                ImportFrom(
                    module='pprint',
                    names=[alias(name='pprint', asname='pp')],
                    level=0,
                ),
                Expr(
                    value=Call(
                        func=Name(id='pp', ctx=Load()),
                        args=[
                            Call(
                                func=Name(id='listdir', ctx=Load()),
                                args=[
                                    Constant(value='../report', kind=None),
                                    Constant(value=True, kind=None),
                                ],
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
    type_ignores=[],
)
