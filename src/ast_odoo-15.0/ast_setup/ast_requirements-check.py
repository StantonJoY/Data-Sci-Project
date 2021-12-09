Module(
    body=[
        Expr(
            value=Constant(value="\nChecks versions from the requirements files against distribution-provided\nversions, taking distribution's Python version in account e.g. if checking\nagainst a release which bundles Python 3.5, checks the 3.5 version of\nrequirements.\n\n* only shows requirements for which at least one release diverges from the\n  matching requirements version\n* empty cells mean that specific release matches its requirement (happens when\n  checking multiple releases: one of the other releases may mismatch the its\n  requirements necessating showing the row)\n\nOnly handles the subset of requirements files we're currently using:\n* no version spec or strict equality\n* no extras\n* only sys_platform and python_version environment markers\n", kind=None),
        ),
        Import(
            names=[alias(name='argparse', asname=None)],
        ),
        Import(
            names=[alias(name='gzip', asname=None)],
        ),
        Import(
            names=[alias(name='itertools', asname=None)],
        ),
        Import(
            names=[alias(name='json', asname=None)],
        ),
        Import(
            names=[alias(name='operator', asname=None)],
        ),
        Import(
            names=[alias(name='re', asname=None)],
        ),
        Import(
            names=[alias(name='string', asname=None)],
        ),
        ImportFrom(
            module='abc',
            names=[
                alias(name='ABC', asname=None),
                alias(name='abstractmethod', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='pathlib',
            names=[alias(name='Path', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='urllib.request',
            names=[alias(name='urlopen', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='sys',
            names=[
                alias(name='stdout', asname=None),
                alias(name='stderr', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='typing',
            names=[
                alias(name='Dict', asname=None),
                alias(name='List', asname=None),
                alias(name='Set', asname=None),
                alias(name='Optional', asname=None),
                alias(name='Any', asname=None),
                alias(name='Tuple', asname=None),
            ],
            level=0,
        ),
        Assign(
            targets=[Name(id='Version', ctx=Store())],
            value=Subscript(
                value=Name(id='Tuple', ctx=Load()),
                slice=Tuple(
                    elts=[
                        Name(id='int', ctx=Load()),
                        Constant(value=Ellipsis, kind=None),
                    ],
                    ctx=Load(),
                ),
                ctx=Load(),
            ),
            type_comment=None,
        ),
        FunctionDef(
            name='parse_version',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(
                        arg='vstring',
                        annotation=Name(id='str', ctx=Load()),
                        type_comment=None,
                    ),
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
                        operand=Name(id='vstring', ctx=Load()),
                    ),
                    body=[
                        Return(
                            value=Constant(value=None, kind=None),
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Call(
                        func=Name(id='tuple', ctx=Load()),
                        args=[
                            Call(
                                func=Name(id='map', ctx=Load()),
                                args=[
                                    Name(id='int', ctx=Load()),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='vstring', ctx=Load()),
                                            attr='split',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='.', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ],
                        keywords=[],
                    ),
                ),
            ],
            decorator_list=[],
            returns=Subscript(
                value=Name(id='Optional', ctx=Load()),
                slice=Name(id='Version', ctx=Load()),
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='SPECIAL', ctx=Store())],
            value=Dict(
                keys=[
                    Constant(value='pytz', kind=None),
                    Constant(value='libsass', kind=None),
                ],
                values=[
                    Constant(value='tz', kind=None),
                    Constant(value='libsass-python', kind=None),
                ],
            ),
            type_comment=None,
        ),
        FunctionDef(
            name='unfuck',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(
                        arg='s',
                        annotation=Name(id='str', ctx=Load()),
                        type_comment=None,
                    ),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Try to strip the garbage from the version string, just remove everything\n    following the first `+`, `~` or `-`\n    ', kind=None),
                ),
                Return(
                    value=Subscript(
                        value=Call(
                            func=Attribute(
                                value=Name(id='re', ctx=Load()),
                                attr='match',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='\n        (?:\\d+:)? # debian crud prefix\n        (.*?) # the shit we actually want\n        (?:~|\\+|-|\\.dfsg)\n        .*\n    ', kind=None),
                                Name(id='s', ctx=Load()),
                            ],
                            keywords=[
                                keyword(
                                    arg='flags',
                                    value=Attribute(
                                        value=Name(id='re', ctx=Load()),
                                        attr='VERBOSE',
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                        ),
                        slice=Constant(value=1, kind=None),
                        ctx=Load(),
                    ),
                ),
            ],
            decorator_list=[],
            returns=Name(id='str', ctx=Load()),
            type_comment=None,
        ),
        ClassDef(
            name='Distribution',
            bases=[Name(id='ABC', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='release', annotation=None, type_comment=None),
                        ],
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
                                    attr='_release',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='release', ctx=Load()),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_version',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(
                                arg='package',
                                annotation=Name(id='str', ctx=Load()),
                                type_comment=None,
                            ),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=Ellipsis, kind=None),
                        ),
                    ],
                    decorator_list=[Name(id='abstractmethod', ctx=Load())],
                    returns=Subscript(
                        value=Name(id='Optional', ctx=Load()),
                        slice=Name(id='Version', ctx=Load()),
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='__str__',
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
                            value=JoinedStr(
                                values=[
                                    FormattedValue(
                                        value=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Call(
                                                        func=Name(id='type', ctx=Load()),
                                                        args=[Name(id='self', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    attr='__name__',
                                                    ctx=Load(),
                                                ),
                                                attr='lower',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        conversion=-1,
                                        format_spec=None,
                                    ),
                                    Constant(value=' ', kind=None),
                                    FormattedValue(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_release',
                                            ctx=Load(),
                                        ),
                                        conversion=-1,
                                        format_spec=None,
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
                    name='get',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='cls', annotation=None, type_comment=None),
                            arg(arg='name', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Try(
                            body=[
                                Return(
                                    value=Call(
                                        func=Name(id='next', ctx=Load()),
                                        args=[
                                            GeneratorExp(
                                                elt=Name(id='c', ctx=Load()),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='c', ctx=Store()),
                                                        iter=Call(
                                                            func=Attribute(
                                                                value=Name(id='cls', ctx=Load()),
                                                                attr='__subclasses__',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                        ifs=[
                                                            Compare(
                                                                left=Call(
                                                                    func=Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='c', ctx=Load()),
                                                                            attr='__name__',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='lower',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[],
                                                                    keywords=[],
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[Name(id='name', ctx=Load())],
                                                            ),
                                                        ],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='StopIteration', ctx=Load()),
                                    name=None,
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='ValueError', ctx=Load()),
                                                args=[
                                                    JoinedStr(
                                                        values=[
                                                            Constant(value='Unknown distribution ', kind=None),
                                                            FormattedValue(
                                                                value=Name(id='name', ctx=Load()),
                                                                conversion=114,
                                                                format_spec=None,
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='Debian',
            bases=[Name(id='Distribution', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='get_version',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='package', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Try to find which version of ``package`` is in Debian release {release}\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='package', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='SPECIAL', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='package', ctx=Load()),
                                    Name(id='package', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='prefix', ctx=Store()),
                            iter=List(
                                elts=[
                                    Constant(value='python-', kind=None),
                                    Constant(value='', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='res', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='json', ctx=Load()),
                                            attr='load',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='urlopen', ctx=Load()),
                                                args=[
                                                    JoinedStr(
                                                        values=[
                                                            Constant(value='https://sources.debian.org/api/src/', kind=None),
                                                            FormattedValue(
                                                                value=Name(id='prefix', ctx=Load()),
                                                                conversion=-1,
                                                                format_spec=None,
                                                            ),
                                                            FormattedValue(
                                                                value=Name(id='package', ctx=Load()),
                                                                conversion=-1,
                                                                format_spec=None,
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Call(
                                            func=Attribute(
                                                value=Name(id='res', ctx=Load()),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='error', kind=None)],
                                            keywords=[],
                                        ),
                                        ops=[Is()],
                                        comparators=[Constant(value=None, kind=None)],
                                    ),
                                    body=[Break()],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='res', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='error', kind=None)],
                                keywords=[],
                            ),
                            body=[Return(value=None)],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Name(id='next', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Call(
                                            func=Name(id='parse_version', ctx=Load()),
                                            args=[
                                                Call(
                                                    func=Name(id='unfuck', ctx=Load()),
                                                    args=[
                                                        Subscript(
                                                            value=Name(id='distr', ctx=Load()),
                                                            slice=Constant(value='version', kind=None),
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
                                                target=Name(id='distr', ctx=Store()),
                                                iter=Subscript(
                                                    value=Name(id='res', ctx=Load()),
                                                    slice=Constant(value='versions', kind=None),
                                                    ctx=Load(),
                                                ),
                                                ifs=[
                                                    Compare(
                                                        left=Subscript(
                                                            value=Name(id='distr', ctx=Load()),
                                                            slice=Constant(value='area', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='main', kind=None)],
                                                    ),
                                                    Compare(
                                                        left=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_release',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[In()],
                                                        comparators=[
                                                            Subscript(
                                                                value=Name(id='distr', ctx=Load()),
                                                                slice=Constant(value='suites', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                is_async=0,
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
            name='Ubuntu',
            bases=[Name(id='Distribution', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=" Ubuntu doesn't have an API, instead it has a huge text file\n    ", kind=None),
                ),
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='release', annotation=None, type_comment=None),
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
                                args=[Name(id='release', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_packages',
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='gzip', ctx=Load()),
                                    attr='open',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='urlopen', ctx=Load()),
                                        args=[
                                            JoinedStr(
                                                values=[
                                                    Constant(value='https://packages.ubuntu.com/source/', kind=None),
                                                    FormattedValue(
                                                        value=Name(id='release', ctx=Load()),
                                                        conversion=-1,
                                                        format_spec=None,
                                                    ),
                                                    Constant(value='/allpackages?format=txt.gz', kind=None),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='mode',
                                        value=Constant(value='rt', kind=None),
                                    ),
                                    keyword(
                                        arg='encoding',
                                        value=Constant(value='utf-8', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='line', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='itertools', ctx=Load()),
                                    attr='islice',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='data', ctx=Load()),
                                    Constant(value=6, kind=None),
                                    Constant(value=None, kind=None),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='m', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='re', ctx=Load()),
                                            attr='match',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='(\\S+) \\(([^)]+)\\)', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='strip',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assert(
                                    test=Name(id='m', ctx=Load()),
                                    msg=JoinedStr(
                                        values=[
                                            Constant(value='invalid line ', kind=None),
                                            FormattedValue(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='line', ctx=Load()),
                                                        attr='strip',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                conversion=114,
                                                format_spec=None,
                                            ),
                                        ],
                                    ),
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_packages',
                                                ctx=Load(),
                                            ),
                                            slice=Subscript(
                                                value=Name(id='m', ctx=Load()),
                                                slice=Constant(value=1, kind=None),
                                                ctx=Load(),
                                            ),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Name(id='m', ctx=Load()),
                                        slice=Constant(value=2, kind=None),
                                        ctx=Load(),
                                    ),
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
                    name='get_version',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='package', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='package', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='SPECIAL', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='package', ctx=Load()),
                                    Name(id='package', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='prefix', ctx=Store()),
                            iter=List(
                                elts=[
                                    Constant(value='python3-', kind=None),
                                    Constant(value='python-', kind=None),
                                    Constant(value='', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='v', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_packages',
                                                ctx=Load(),
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            JoinedStr(
                                                values=[
                                                    FormattedValue(
                                                        value=Name(id='prefix', ctx=Load()),
                                                        conversion=-1,
                                                        format_spec=None,
                                                    ),
                                                    FormattedValue(
                                                        value=Name(id='package', ctx=Load()),
                                                        conversion=-1,
                                                        format_spec=None,
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='v', ctx=Load()),
                                    body=[
                                        Return(
                                            value=Call(
                                                func=Name(id='parse_version', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='unfuck', ctx=Load()),
                                                        args=[Name(id='v', ctx=Load())],
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
                            value=Constant(value=None, kind=None),
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
            name='Markers',
            bases=[],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' Simplistic RD parser for requirements env markers.\n\n    Evaluation of the env markers is so basic it goes to brunch in uggs.\n    ', kind=None),
                ),
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='s', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='rules',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='s', ctx=Load()),
                                ops=[IsNot()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='rules',
                                                    ctx=Store(),
                                                ),
                                                Name(id='rest', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_parse_marker',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='s', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assert(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='rest', ctx=Load()),
                                    ),
                                    msg=None,
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
                    name='evaluate',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(
                                arg='context',
                                annotation=Subscript(
                                    value=Name(id='Dict', ctx=Load()),
                                    slice=Tuple(
                                        elts=[
                                            Name(id='str', ctx=Load()),
                                            Name(id='Any', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                    ctx=Load(),
                                ),
                                type_comment=None,
                            ),
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
                                operand=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='rules',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Return(
                                    value=Constant(value=True, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_eval',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='rules',
                                        ctx=Load(),
                                    ),
                                    Name(id='context', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=Name(id='bool', ctx=Load()),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_eval',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='rule', annotation=None, type_comment=None),
                            arg(arg='context', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=Compare(
                                left=Subscript(
                                    value=Name(id='rule', ctx=Load()),
                                    slice=Constant(value=0, kind=None),
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='OR', kind=None)],
                            ),
                            body=[
                                Return(
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_eval',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='rule', ctx=Load()),
                                                        slice=Constant(value=1, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='context', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_eval',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='rule', ctx=Load()),
                                                        slice=Constant(value=2, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='context', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Subscript(
                                            value=Name(id='rule', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='AND', kind=None)],
                                    ),
                                    body=[
                                        Return(
                                            value=BoolOp(
                                                op=And(),
                                                values=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_eval',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='rule', ctx=Load()),
                                                                slice=Constant(value=1, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            Name(id='context', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_eval',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='rule', ctx=Load()),
                                                                slice=Constant(value=2, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            Name(id='context', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Subscript(
                                                    value=Name(id='rule', ctx=Load()),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='ENV', kind=None)],
                                            ),
                                            body=[
                                                Return(
                                                    value=Subscript(
                                                        value=Name(id='context', ctx=Load()),
                                                        slice=Subscript(
                                                            value=Name(id='rule', ctx=Load()),
                                                            slice=Constant(value=1, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Compare(
                                                        left=Subscript(
                                                            value=Name(id='rule', ctx=Load()),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='LIT', kind=None)],
                                                    ),
                                                    body=[
                                                        Return(
                                                            value=Subscript(
                                                                value=Name(id='rule', ctx=Load()),
                                                                slice=Constant(value=1, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[
                                                        Assign(
                                                            targets=[
                                                                Tuple(
                                                                    elts=[
                                                                        Name(id='op', ctx=Store()),
                                                                        Name(id='var1', ctx=Store()),
                                                                        Name(id='var2', ctx=Store()),
                                                                    ],
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Name(id='rule', ctx=Load()),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='var1', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='_eval',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Name(id='var1', ctx=Load()),
                                                                    Name(id='context', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='var2', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='_eval',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Name(id='var2', ctx=Load()),
                                                                    Name(id='context', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        If(
                                                            test=Compare(
                                                                left=Name(id='op', ctx=Load()),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='==', kind=None)],
                                                            ),
                                                            body=[
                                                                Return(
                                                                    value=Compare(
                                                                        left=Name(id='var1', ctx=Load()),
                                                                        ops=[Eq()],
                                                                        comparators=[Name(id='var2', ctx=Load())],
                                                                    ),
                                                                ),
                                                            ],
                                                            orelse=[
                                                                If(
                                                                    test=Compare(
                                                                        left=Name(id='op', ctx=Load()),
                                                                        ops=[Eq()],
                                                                        comparators=[Constant(value='!=', kind=None)],
                                                                    ),
                                                                    body=[
                                                                        Return(
                                                                            value=Compare(
                                                                                left=Name(id='var1', ctx=Load()),
                                                                                ops=[NotEq()],
                                                                                comparators=[Name(id='var2', ctx=Load())],
                                                                            ),
                                                                        ),
                                                                    ],
                                                                    orelse=[
                                                                        If(
                                                                            test=Compare(
                                                                                left=Name(id='op', ctx=Load()),
                                                                                ops=[Eq()],
                                                                                comparators=[Constant(value='<', kind=None)],
                                                                            ),
                                                                            body=[
                                                                                Return(
                                                                                    value=Compare(
                                                                                        left=Name(id='var1', ctx=Load()),
                                                                                        ops=[Lt()],
                                                                                        comparators=[Name(id='var2', ctx=Load())],
                                                                                    ),
                                                                                ),
                                                                            ],
                                                                            orelse=[
                                                                                If(
                                                                                    test=Compare(
                                                                                        left=Name(id='op', ctx=Load()),
                                                                                        ops=[Eq()],
                                                                                        comparators=[Constant(value='<=', kind=None)],
                                                                                    ),
                                                                                    body=[
                                                                                        Return(
                                                                                            value=Compare(
                                                                                                left=Name(id='var1', ctx=Load()),
                                                                                                ops=[LtE()],
                                                                                                comparators=[Name(id='var2', ctx=Load())],
                                                                                            ),
                                                                                        ),
                                                                                    ],
                                                                                    orelse=[
                                                                                        If(
                                                                                            test=Compare(
                                                                                                left=Name(id='op', ctx=Load()),
                                                                                                ops=[Eq()],
                                                                                                comparators=[Constant(value='>', kind=None)],
                                                                                            ),
                                                                                            body=[
                                                                                                Return(
                                                                                                    value=Compare(
                                                                                                        left=Name(id='var1', ctx=Load()),
                                                                                                        ops=[Gt()],
                                                                                                        comparators=[Name(id='var2', ctx=Load())],
                                                                                                    ),
                                                                                                ),
                                                                                            ],
                                                                                            orelse=[
                                                                                                If(
                                                                                                    test=Compare(
                                                                                                        left=Name(id='op', ctx=Load()),
                                                                                                        ops=[Eq()],
                                                                                                        comparators=[Constant(value='>=', kind=None)],
                                                                                                    ),
                                                                                                    body=[
                                                                                                        Return(
                                                                                                            value=Compare(
                                                                                                                left=Name(id='var1', ctx=Load()),
                                                                                                                ops=[GtE()],
                                                                                                                comparators=[Name(id='var2', ctx=Load())],
                                                                                                            ),
                                                                                                        ),
                                                                                                    ],
                                                                                                    orelse=[
                                                                                                        Raise(
                                                                                                            exc=Call(
                                                                                                                func=Name(id='NotImplementedError', ctx=Load()),
                                                                                                                args=[
                                                                                                                    JoinedStr(
                                                                                                                        values=[
                                                                                                                            Constant(value='Operator ', kind=None),
                                                                                                                            FormattedValue(
                                                                                                                                value=Name(id='op', ctx=Load()),
                                                                                                                                conversion=114,
                                                                                                                                format_spec=None,
                                                                                                                            ),
                                                                                                                        ],
                                                                                                                    ),
                                                                                                                ],
                                                                                                                keywords=[],
                                                                                                            ),
                                                                                                            cause=None,
                                                                                                        ),
                                                                                                    ],
                                                                                                ),
                                                                                            ],
                                                                                        ),
                                                                                    ],
                                                                                ),
                                                                            ],
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_parse_marker',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='s', annotation=None, type_comment=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='_parse_or',
                                    ctx=Load(),
                                ),
                                args=[Name(id='s', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_parse_or',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='s', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='sub1', ctx=Store()),
                                        Name(id='rest', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_parse_and',
                                    ctx=Load(),
                                ),
                                args=[Name(id='s', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='expr', ctx=Store()),
                                        Name(id='n', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='re', ctx=Load()),
                                    attr='subn',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='^\\s*or\\b', kind=None),
                                    Constant(value='', kind=None),
                                    Name(id='rest', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='count',
                                        value=Constant(value=1, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='n', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Tuple(
                                        elts=[
                                            Name(id='sub1', ctx=Load()),
                                            Name(id='rest', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='sub2', ctx=Store()),
                                        Name(id='rest', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_parse_and',
                                    ctx=Load(),
                                ),
                                args=[Name(id='expr', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='OR', kind=None),
                                            Name(id='sub1', ctx=Load()),
                                            Name(id='sub2', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Name(id='rest', ctx=Load()),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_parse_and',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='s', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='sub1', ctx=Store()),
                                        Name(id='rest', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_parse_expr',
                                    ctx=Load(),
                                ),
                                args=[Name(id='s', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='expr', ctx=Store()),
                                        Name(id='n', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='re', ctx=Load()),
                                    attr='subn',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='\\s*and\\b', kind=None),
                                    Constant(value='', kind=None),
                                    Name(id='rest', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='count',
                                        value=Constant(value=1, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='n', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Tuple(
                                        elts=[
                                            Name(id='sub1', ctx=Load()),
                                            Name(id='rest', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='sub2', ctx=Store()),
                                        Name(id='rest', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_parse_expr',
                                    ctx=Load(),
                                ),
                                args=[Name(id='expr', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='AND', kind=None),
                                            Name(id='sub1', ctx=Load()),
                                            Name(id='sub2', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Name(id='rest', ctx=Load()),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_parse_expr',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='s', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='expr', ctx=Store()),
                                        Name(id='n', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='re', ctx=Load()),
                                    attr='subn',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='^\\s*\\(', kind=None),
                                    Constant(value='', kind=None),
                                    Name(id='s', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='count',
                                        value=Constant(value=1, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='n', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='sub', ctx=Store()),
                                                Name(id='rest', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='parse_marker',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='expr', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='rest', ctx=Store()),
                                                Name(id='n', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='re', ctx=Load()),
                                            attr='subn',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='\\s*\\)', kind=None),
                                            Constant(value='', kind=None),
                                            Name(id='rest', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='count',
                                                value=Constant(value=1, kind=None),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assert(
                                    test=Name(id='n', ctx=Load()),
                                    msg=JoinedStr(
                                        values=[
                                            Constant(value='expected closing parenthesis, found ', kind=None),
                                            FormattedValue(
                                                value=Name(id='rest', ctx=Load()),
                                                conversion=-1,
                                                format_spec=None,
                                            ),
                                        ],
                                    ),
                                ),
                                Return(
                                    value=Tuple(
                                        elts=[
                                            Name(id='sub', ctx=Load()),
                                            Name(id='rest', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='var1', ctx=Store()),
                                        Name(id='rest', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_parse_var',
                                    ctx=Load(),
                                ),
                                args=[Name(id='s', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='op', ctx=Store()),
                                        Name(id='rest', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_parse_op',
                                    ctx=Load(),
                                ),
                                args=[Name(id='rest', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='var2', ctx=Store()),
                                        Name(id='rest', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_parse_var',
                                    ctx=Load(),
                                ),
                                args=[Name(id='rest', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Name(id='op', ctx=Load()),
                                            Name(id='var1', ctx=Load()),
                                            Name(id='var2', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Name(id='rest', ctx=Load()),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_parse_op',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='s', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='m', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='re', ctx=Load()),
                                    attr='match',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='\n            \\s*\n            (<= | < | != | >= | > | ~= | ===? | in \\b | not \\s+ in \\b)\n            (.*)\n        ', kind=None),
                                    Name(id='s', ctx=Load()),
                                    Attribute(
                                        value=Name(id='re', ctx=Load()),
                                        attr='VERBOSE',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assert(
                            test=Name(id='m', ctx=Load()),
                            msg=JoinedStr(
                                values=[
                                    Constant(value='no operator in ', kind=None),
                                    FormattedValue(
                                        value=Name(id='s', ctx=Load()),
                                        conversion=114,
                                        format_spec=None,
                                    ),
                                ],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='m', ctx=Load()),
                                    attr='groups',
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
                    name='_parse_var',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='s', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='python_str', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='re', ctx=Load()),
                                    attr='escape',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='string', ctx=Load()),
                                                attr='printable',
                                                ctx=Load(),
                                            ),
                                            attr='translate',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='str', ctx=Load()),
                                                    attr='maketrans',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='"', kind=None),
                                                            Constant(value="'", kind=None),
                                                            Constant(value='\\', kind=None),
                                                            Constant(value='-', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='', kind=None),
                                                            Constant(value='', kind=None),
                                                            Constant(value='', kind=None),
                                                            Constant(value='', kind=None),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
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
                            targets=[Name(id='m', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='re', ctx=Load()),
                                    attr='match',
                                    ctx=Load(),
                                ),
                                args=[
                                    JoinedStr(
                                        values=[
                                            Constant(value='\n            \\s*\n            (:?\n                # TODO: add more envvars\n                (?P<env>python_version | os_name | sys_platform)\n              | " (?P<dquote>[\'', kind=None),
                                            FormattedValue(
                                                value=Name(id='python_str', ctx=Load()),
                                                conversion=-1,
                                                format_spec=None,
                                            ),
                                            Constant(value='-]*) "\n              | \' (?P<squote>["', kind=None),
                                            FormattedValue(
                                                value=Name(id='python_str', ctx=Load()),
                                                conversion=-1,
                                                format_spec=None,
                                            ),
                                            Constant(value="-]*) '\n            )\n            (?P<rest>.*)\n        ", kind=None),
                                        ],
                                    ),
                                    Name(id='s', ctx=Load()),
                                    Attribute(
                                        value=Name(id='re', ctx=Load()),
                                        attr='VERBOSE',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assert(
                            test=Name(id='m', ctx=Load()),
                            msg=JoinedStr(
                                values=[
                                    Constant(value='failed to find marker var in ', kind=None),
                                    FormattedValue(
                                        value=Name(id='s', ctx=Load()),
                                        conversion=-1,
                                        format_spec=None,
                                    ),
                                ],
                            ),
                        ),
                        If(
                            test=Subscript(
                                value=Name(id='m', ctx=Load()),
                                slice=Constant(value='env', kind=None),
                                ctx=Load(),
                            ),
                            body=[
                                Return(
                                    value=Tuple(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='ENV', kind=None),
                                                    Subscript(
                                                        value=Name(id='m', ctx=Load()),
                                                        slice=Constant(value='env', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='m', ctx=Load()),
                                                slice=Constant(value='rest', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='LIT', kind=None),
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    Subscript(
                                                        value=Name(id='m', ctx=Load()),
                                                        slice=Constant(value='dquote', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Subscript(
                                                        value=Name(id='m', ctx=Load()),
                                                        slice=Constant(value='squote', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='', kind=None),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Name(id='m', ctx=Load()),
                                        slice=Constant(value='rest', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
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
        FunctionDef(
            name='parse_spec',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(
                        arg='line',
                        annotation=Name(id='str', ctx=Load()),
                        type_comment=None,
                    ),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=" Parse a requirements specification (a line of requirements)\n\n    Returns the package name, a version spec (operator and comparator) possibly\n    None and a Markers object.\n\n    Not correctly supported:\n\n    * version matching, not all operators are implemented and those which are\n      almost certainly don't match PEP 440\n\n    Not supported:\n\n    * url requirements\n    * multi-versions spec\n    * extras\n    * continuations\n\n    Full grammar is at https://www.python.org/dev/peps/pep-0508/#complete-grammar\n    ", kind=None),
                ),
                Assign(
                    targets=[
                        Tuple(
                            elts=[
                                Name(id='name', ctx=Store()),
                                Name(id='rest', ctx=Store()),
                            ],
                            ctx=Store(),
                        ),
                    ],
                    value=Call(
                        func=Attribute(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='re', ctx=Load()),
                                    attr='match',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='([\\w\\d](?:[._-]*[\\w\\d]+)*)\\s*(.*)', kind=None),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='strip',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            attr='groups',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[
                        Name(id='version_cmp', ctx=Store()),
                        Name(id='version', ctx=Store()),
                    ],
                    value=Constant(value=None, kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='versionspec', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='re', ctx=Load()),
                            attr='match',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='\n        (< | <= | != | == | >= | > | ~= | ===)\n        \\s*\n        ([\\w\\d_.*+!-]+)\n        \\s*\n        (.*)\n    ', kind=None),
                            Name(id='rest', ctx=Load()),
                            Attribute(
                                value=Name(id='re', ctx=Load()),
                                attr='VERBOSE',
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=Name(id='versionspec', ctx=Load()),
                    body=[
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='version_cmp', ctx=Store()),
                                        Name(id='version', ctx=Store()),
                                        Name(id='rest', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='versionspec', ctx=Load()),
                                    attr='groups',
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
                    targets=[Name(id='markers', ctx=Store())],
                    value=Call(
                        func=Name(id='Markers', ctx=Load()),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=Compare(
                        left=Subscript(
                            value=Name(id='rest', ctx=Load()),
                            slice=Slice(
                                lower=None,
                                upper=Constant(value=1, kind=None),
                                step=None,
                            ),
                            ctx=Load(),
                        ),
                        ops=[Eq()],
                        comparators=[Constant(value=';', kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='markers', ctx=Store())],
                            value=Call(
                                func=Name(id='Markers', ctx=Load()),
                                args=[
                                    Subscript(
                                        value=Name(id='rest', ctx=Load()),
                                        slice=Slice(
                                            lower=Constant(value=1, kind=None),
                                            upper=None,
                                            step=None,
                                        ),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Tuple(
                        elts=[
                            Name(id='name', ctx=Load()),
                            Tuple(
                                elts=[
                                    Name(id='version_cmp', ctx=Load()),
                                    Name(id='version', ctx=Load()),
                                ],
                                ctx=Load(),
                            ),
                            Name(id='markers', ctx=Load()),
                        ],
                        ctx=Load(),
                    ),
                ),
            ],
            decorator_list=[],
            returns=Tuple(
                elts=[
                    Name(id='str', ctx=Load()),
                    Tuple(
                        elts=[
                            Subscript(
                                value=Name(id='Optional', ctx=Load()),
                                slice=Name(id='str', ctx=Load()),
                                ctx=Load(),
                            ),
                            Subscript(
                                value=Name(id='Optional', ctx=Load()),
                                slice=Name(id='str', ctx=Load()),
                                ctx=Load(),
                            ),
                        ],
                        ctx=Load(),
                    ),
                    Name(id='Markers', ctx=Load()),
                ],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        FunctionDef(
            name='parse_requirements',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(
                        arg='reqpath',
                        annotation=Name(id='Path', ctx=Load()),
                        type_comment=None,
                    ),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Parses a requirement file to a dict of {package: [(version, markers)]}\n\n    The env markers express *whether* that specific dep applies.\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='reqs', ctx=Store())],
                    value=Dict(keys=[], values=[]),
                    type_comment=None,
                ),
                For(
                    target=Name(id='line', ctx=Store()),
                    iter=Call(
                        func=Attribute(
                            value=Name(id='reqpath', ctx=Load()),
                            attr='open',
                            ctx=Load(),
                        ),
                        args=[Constant(value='r', kind=None)],
                        keywords=[
                            keyword(
                                arg='encoding',
                                value=Constant(value='utf-8', kind=None),
                            ),
                        ],
                    ),
                    body=[
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='isspace',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='startswith',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='#', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[Continue()],
                            orelse=[],
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='name', ctx=Store()),
                                        Tuple(
                                            elts=[
                                                Name(id='op', ctx=Store()),
                                                Name(id='version', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                        Name(id='markers', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='parse_spec', ctx=Load()),
                                args=[Name(id='line', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assert(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Compare(
                                        left=Name(id='op', ctx=Load()),
                                        ops=[Is()],
                                        comparators=[Constant(value=None, kind=None)],
                                    ),
                                    Compare(
                                        left=Name(id='op', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='==', kind=None)],
                                    ),
                                ],
                            ),
                            msg=JoinedStr(
                                values=[
                                    Constant(value='unexpected version comparator ', kind=None),
                                    FormattedValue(
                                        value=Name(id='op', ctx=Load()),
                                        conversion=-1,
                                        format_spec=None,
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='reqs', ctx=Load()),
                                            attr='setdefault',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='name', ctx=Load()),
                                            List(elts=[], ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[
                                    Tuple(
                                        elts=[
                                            Name(id='version', ctx=Load()),
                                            Name(id='markers', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[],
                    type_comment=None,
                ),
                Return(
                    value=Name(id='reqs', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=Subscript(
                value=Name(id='Dict', ctx=Load()),
                slice=Tuple(
                    elts=[
                        Name(id='str', ctx=Load()),
                        Subscript(
                            value=Name(id='List', ctx=Load()),
                            slice=Subscript(
                                value=Name(id='Tuple', ctx=Load()),
                                slice=Tuple(
                                    elts=[
                                        Name(id='str', ctx=Load()),
                                        Name(id='Markers', ctx=Load()),
                                    ],
                                    ctx=Load(),
                                ),
                                ctx=Load(),
                            ),
                            ctx=Load(),
                        ),
                    ],
                    ctx=Load(),
                ),
                ctx=Load(),
            ),
            type_comment=None,
        ),
        FunctionDef(
            name='main',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='args', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Assign(
                    targets=[Name(id='checkers', ctx=Store())],
                    value=ListComp(
                        elt=Call(
                            func=Call(
                                func=Attribute(
                                    value=Name(id='Distribution', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Name(id='distro', ctx=Load())],
                                keywords=[],
                            ),
                            args=[Name(id='release', ctx=Load())],
                            keywords=[],
                        ),
                        generators=[
                            comprehension(
                                target=Name(id='version', ctx=Store()),
                                iter=Attribute(
                                    value=Name(id='args', ctx=Load()),
                                    attr='release',
                                    ctx=Load(),
                                ),
                                ifs=[],
                                is_async=0,
                            ),
                            comprehension(
                                target=Tuple(
                                    elts=[
                                        Name(id='distro', ctx=Store()),
                                        Name(id='release', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                                iter=List(
                                    elts=[
                                        Call(
                                            func=Attribute(
                                                value=Name(id='version', ctx=Load()),
                                                attr='split',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value=':', kind=None)],
                                            keywords=[],
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                                ifs=[],
                                is_async=0,
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='stderr', ctx=Load()),
                            attr='write',
                            ctx=Load(),
                        ),
                        args=[
                            JoinedStr(
                                values=[Constant(value='Fetch Python versions...\n', kind=None)],
                            ),
                        ],
                        keywords=[],
                    ),
                ),
                Assign(
                    targets=[Name(id='pyvers', ctx=Store())],
                    value=ListComp(
                        elt=Call(
                            func=Attribute(
                                value=Constant(value='.', kind=None),
                                attr='join',
                                ctx=Load(),
                            ),
                            args=[
                                Call(
                                    func=Name(id='map', ctx=Load()),
                                    args=[
                                        Name(id='str', ctx=Load()),
                                        Subscript(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='checker', ctx=Load()),
                                                    attr='get_version',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='python3-defaults', kind=None)],
                                                keywords=[],
                                            ),
                                            slice=Slice(
                                                lower=None,
                                                upper=Constant(value=2, kind=None),
                                                step=None,
                                            ),
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
                                target=Name(id='checker', ctx=Store()),
                                iter=Name(id='checkers', ctx=Load()),
                                ifs=[],
                                is_async=0,
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='uniq', ctx=Store())],
                    value=Call(
                        func=Name(id='sorted', ctx=Load()),
                        args=[
                            GeneratorExp(
                                elt=Name(id='v', ctx=Load()),
                                generators=[
                                    comprehension(
                                        target=Name(id='v', ctx=Store()),
                                        iter=Call(
                                            func=Name(id='set', ctx=Load()),
                                            args=[Name(id='pyvers', ctx=Load())],
                                            keywords=[],
                                        ),
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
                Assign(
                    targets=[Name(id='table', ctx=Store())],
                    value=List(
                        elts=[
                            BinOp(
                                left=BinOp(
                                    left=List(
                                        elts=[Constant(value='', kind=None)],
                                        ctx=Load(),
                                    ),
                                    op=Add(),
                                    right=ListComp(
                                        elt=JoinedStr(
                                            values=[
                                                Constant(value='req ', kind=None),
                                                FormattedValue(
                                                    value=Name(id='v', ctx=Load()),
                                                    conversion=-1,
                                                    format_spec=None,
                                                ),
                                            ],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='v', ctx=Store()),
                                                iter=Name(id='uniq', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ),
                                op=Add(),
                                right=ListComp(
                                    elt=JoinedStr(
                                        values=[
                                            FormattedValue(
                                                value=Attribute(
                                                    value=Name(id='checker', ctx=Load()),
                                                    attr='_release',
                                                    ctx=Load(),
                                                ),
                                                conversion=-1,
                                                format_spec=None,
                                            ),
                                            Constant(value=' (', kind=None),
                                            FormattedValue(
                                                value=Name(id='version', ctx=Load()),
                                                conversion=-1,
                                                format_spec=None,
                                            ),
                                            Constant(value=')', kind=None),
                                        ],
                                    ),
                                    generators=[
                                        comprehension(
                                            target=Tuple(
                                                elts=[
                                                    Name(id='checker', ctx=Store()),
                                                    Name(id='version', ctx=Store()),
                                                ],
                                                ctx=Store(),
                                            ),
                                            iter=Call(
                                                func=Name(id='zip', ctx=Load()),
                                                args=[
                                                    Name(id='checkers', ctx=Load()),
                                                    Name(id='pyvers', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            ifs=[],
                                            is_async=0,
                                        ),
                                    ],
                                ),
                            ),
                        ],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='reqs', ctx=Store())],
                    value=Call(
                        func=Name(id='parse_requirements', ctx=Load()),
                        args=[
                            BinOp(
                                left=Attribute(
                                    value=Attribute(
                                        value=BinOp(
                                            left=Call(
                                                func=Attribute(
                                                    value=Name(id='Path', ctx=Load()),
                                                    attr='cwd',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            op=Div(),
                                            right=Name(id='__file__', ctx=Load()),
                                        ),
                                        attr='parent',
                                        ctx=Load(),
                                    ),
                                    attr='parent',
                                    ctx=Load(),
                                ),
                                op=Div(),
                                right=Constant(value='requirements.txt', kind=None),
                            ),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='tot', ctx=Store())],
                    value=BinOp(
                        left=Call(
                            func=Name(id='len', ctx=Load()),
                            args=[Name(id='reqs', ctx=Load())],
                            keywords=[],
                        ),
                        op=Mult(),
                        right=Call(
                            func=Name(id='len', ctx=Load()),
                            args=[Name(id='checkers', ctx=Load())],
                            keywords=[],
                        ),
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='progress',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='n', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Call(
                                func=Name(id='iter', ctx=Load()),
                                args=[
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Name(id='tot', ctx=Load()),
                                                op=Add(),
                                                right=Constant(value=1, kind=None),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='stderr', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    JoinedStr(
                                        values=[
                                            Constant(value='\rFetch requirements: ', kind=None),
                                            FormattedValue(
                                                value=Call(
                                                    func=Name(id='next', ctx=Load()),
                                                    args=[Name(id='n', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                conversion=-1,
                                                format_spec=None,
                                            ),
                                            Constant(value=' / ', kind=None),
                                            FormattedValue(
                                                value=Name(id='tot', ctx=Load()),
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
                Expr(
                    value=Call(
                        func=Name(id='progress', ctx=Load()),
                        args=[],
                        keywords=[],
                    ),
                ),
                For(
                    target=Tuple(
                        elts=[
                            Name(id='req', ctx=Store()),
                            Name(id='options', ctx=Store()),
                        ],
                        ctx=Store(),
                    ),
                    iter=Call(
                        func=Attribute(
                            value=Name(id='reqs', ctx=Load()),
                            attr='items',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='row', ctx=Store())],
                            value=List(
                                elts=[Name(id='req', ctx=Load())],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='byver', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='pyver', ctx=Store()),
                            iter=Name(id='uniq', ctx=Load()),
                            body=[
                                For(
                                    target=Tuple(
                                        elts=[
                                            Name(id='version', ctx=Store()),
                                            Name(id='markers', ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                    iter=Name(id='options', ctx=Load()),
                                    body=[
                                        If(
                                            test=Call(
                                                func=Attribute(
                                                    value=Name(id='markers', ctx=Load()),
                                                    attr='evaluate',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='python_version', kind=None),
                                                            Constant(value='sys_platform', kind=None),
                                                        ],
                                                        values=[
                                                            Name(id='pyver', ctx=Load()),
                                                            Constant(value='linux', kind=None),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='byver', ctx=Load()),
                                                            slice=Name(id='pyver', ctx=Load()),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Name(id='version', ctx=Load()),
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
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='row', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='byver', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='pyver', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    Constant(value='', kind=None),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='byver', ctx=Load()),
                            ),
                            body=[
                                For(
                                    target=Name(id='_', ctx=Store()),
                                    iter=Name(id='checkers', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Name(id='progress', ctx=Load()),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                Continue(),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='mismatch', ctx=Store())],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='i', ctx=Store()),
                                    Name(id='c', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Name(id='enumerate', ctx=Load()),
                                args=[Name(id='checkers', ctx=Load())],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='req_version', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='byver', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='pyvers', ctx=Load()),
                                                slice=Name(id='i', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            Constant(value='', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='check_version', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Constant(value='.', kind=None),
                                            attr='join',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='map', ctx=Load()),
                                                args=[
                                                    Name(id='str', ctx=Load()),
                                                    BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='c', ctx=Load()),
                                                                    attr='get_version',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Name(id='req', ctx=Load()),
                                                                            attr='lower',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            List(
                                                                elts=[Constant(value='<missing>', kind=None)],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
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
                                        func=Name(id='progress', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='req_version', ctx=Load()),
                                        ops=[NotEq()],
                                        comparators=[Name(id='check_version', ctx=Load())],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='row', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='check_version', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[Name(id='mismatch', ctx=Store())],
                                            value=Constant(value=True, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='row', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='', kind=None)],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='mismatch', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='table', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='row', ctx=Load())],
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
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='stderr', ctx=Load()),
                            attr='write',
                            ctx=Load(),
                        ),
                        args=[Constant(value='\n', kind=None)],
                        keywords=[],
                    ),
                ),
                Assign(
                    targets=[Name(id='sizes', ctx=Store())],
                    value=BinOp(
                        left=List(
                            elts=[Constant(value=0, kind=None)],
                            ctx=Load(),
                        ),
                        op=Mult(),
                        right=BinOp(
                            left=BinOp(
                                left=Call(
                                    func=Name(id='len', ctx=Load()),
                                    args=[Name(id='checkers', ctx=Load())],
                                    keywords=[],
                                ),
                                op=Add(),
                                right=Call(
                                    func=Name(id='len', ctx=Load()),
                                    args=[Name(id='uniq', ctx=Load())],
                                    keywords=[],
                                ),
                            ),
                            op=Add(),
                            right=Constant(value=1, kind=None),
                        ),
                    ),
                    type_comment=None,
                ),
                For(
                    target=Name(id='row', ctx=Store()),
                    iter=Name(id='table', ctx=Load()),
                    body=[
                        Assign(
                            targets=[Name(id='sizes', ctx=Store())],
                            value=ListComp(
                                elt=Call(
                                    func=Name(id='max', ctx=Load()),
                                    args=[
                                        Name(id='s', ctx=Load()),
                                        Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[Name(id='cell', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                generators=[
                                    comprehension(
                                        target=Tuple(
                                            elts=[
                                                Name(id='s', ctx=Store()),
                                                Name(id='cell', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                        iter=Call(
                                            func=Name(id='zip', ctx=Load()),
                                            args=[
                                                Name(id='sizes', ctx=Load()),
                                                Name(id='row', ctx=Load()),
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
                    ],
                    orelse=[],
                    type_comment=None,
                ),
                For(
                    target=Name(id='row', ctx=Store()),
                    iter=Name(id='table', ctx=Load()),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='stdout', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='| ', kind=None)],
                                keywords=[],
                            ),
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='cell', ctx=Store()),
                                    Name(id='width', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Name(id='zip', ctx=Load()),
                                args=[
                                    Name(id='row', ctx=Load()),
                                    Name(id='sizes', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='stdout', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            JoinedStr(
                                                values=[
                                                    FormattedValue(
                                                        value=Name(id='cell', ctx=Load()),
                                                        conversion=-1,
                                                        format_spec=JoinedStr(
                                                            values=[
                                                                Constant(value='<', kind=None),
                                                                FormattedValue(
                                                                    value=Name(id='width', ctx=Load()),
                                                                    conversion=-1,
                                                                    format_spec=None,
                                                                ),
                                                            ],
                                                        ),
                                                    ),
                                                    Constant(value=' | ', kind=None),
                                                ],
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
                                func=Attribute(
                                    value=Name(id='stdout', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='\n', kind=None)],
                                keywords=[],
                            ),
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
        If(
            test=Compare(
                left=Name(id='__name__', ctx=Load()),
                ops=[Eq()],
                comparators=[Constant(value='__main__', kind=None)],
            ),
            body=[
                Assign(
                    targets=[Name(id='parser', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='argparse', ctx=Load()),
                            attr='ArgumentParser',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='description',
                                value=Name(id='__doc__', ctx=Load()),
                            ),
                            keyword(
                                arg='formatter_class',
                                value=Attribute(
                                    value=Name(id='argparse', ctx=Load()),
                                    attr='RawDescriptionHelpFormatter',
                                    ctx=Load(),
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='parser', ctx=Load()),
                            attr='add_argument',
                            ctx=Load(),
                        ),
                        args=[Constant(value='release', kind=None)],
                        keywords=[
                            keyword(
                                arg='nargs',
                                value=Constant(value='+', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value="Release to check against, should use the format '{distro}:{release}' e.g. 'debian:sid'", kind=None),
                            ),
                        ],
                    ),
                ),
                Assign(
                    targets=[Name(id='args', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='parser', ctx=Load()),
                            attr='parse_args',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Expr(
                    value=Call(
                        func=Name(id='main', ctx=Load()),
                        args=[Name(id='args', ctx=Load())],
                        keywords=[],
                    ),
                ),
            ],
            orelse=[],
        ),
    ],
    type_ignores=[],
)
