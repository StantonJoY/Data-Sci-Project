Module(
    body=[
        Assign(
            targets=[Name(id='__all__', ctx=Store())],
            value=List(
                elts=[
                    Constant(value='convert_file', kind=None),
                    Constant(value='convert_sql_import', kind=None),
                    Constant(value='convert_csv_import', kind=None),
                    Constant(value='convert_xml_import', kind=None),
                ],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Import(
            names=[alias(name='base64', asname=None)],
        ),
        Import(
            names=[alias(name='io', asname=None)],
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='os.path', asname=None)],
        ),
        Import(
            names=[alias(name='pprint', asname=None)],
        ),
        Import(
            names=[alias(name='re', asname=None)],
        ),
        Import(
            names=[alias(name='subprocess', asname=None)],
        ),
        Import(
            names=[alias(name='warnings', asname=None)],
        ),
        ImportFrom(
            module='datetime',
            names=[
                alias(name='datetime', asname=None),
                alias(name='timedelta', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='dateutil.relativedelta',
            names=[alias(name='relativedelta', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='pytz', asname=None)],
        ),
        ImportFrom(
            module='lxml',
            names=[
                alias(name='etree', asname=None),
                alias(name='builder', asname=None),
            ],
            level=0,
        ),
        Try(
            body=[
                Import(
                    names=[alias(name='jingtrang', asname=None)],
                ),
            ],
            handlers=[
                ExceptHandler(
                    type=Name(id='ImportError', ctx=Load()),
                    name=None,
                    body=[
                        Assign(
                            targets=[Name(id='jingtrang', ctx=Store())],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                    ],
                ),
            ],
            orelse=[],
            finalbody=[],
        ),
        Import(
            names=[alias(name='odoo', asname=None)],
        ),
        ImportFrom(
            module=None,
            names=[alias(name='pycompat', asname=None)],
            level=1,
        ),
        ImportFrom(
            module='config',
            names=[alias(name='config', asname=None)],
            level=1,
        ),
        ImportFrom(
            module='misc',
            names=[
                alias(name='file_open', asname=None),
                alias(name='unquote', asname=None),
                alias(name='ustr', asname=None),
                alias(name='SKIPPED_ELEMENT_TYPES', asname=None),
            ],
            level=1,
        ),
        ImportFrom(
            module='translate',
            names=[alias(name='_', asname=None)],
            level=1,
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='SUPERUSER_ID', asname=None),
                alias(name='api', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[alias(name='ValidationError', asname=None)],
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
        ImportFrom(
            module='safe_eval',
            names=[
                alias(name='safe_eval', asname='s_eval'),
                alias(name='pytz', asname=None),
                alias(name='time', asname=None),
            ],
            level=1,
        ),
        Assign(
            targets=[Name(id='safe_eval', ctx=Store())],
            value=Lambda(
                args=arguments(
                    posonlyargs=[],
                    args=[
                        arg(arg='expr', annotation=None, type_comment=None),
                        arg(arg='ctx', annotation=None, type_comment=None),
                    ],
                    vararg=None,
                    kwonlyargs=[],
                    kw_defaults=[],
                    kwarg=None,
                    defaults=[Dict(keys=[], values=[])],
                ),
                body=Call(
                    func=Name(id='s_eval', ctx=Load()),
                    args=[
                        Name(id='expr', ctx=Load()),
                        Name(id='ctx', ctx=Load()),
                    ],
                    keywords=[
                        keyword(
                            arg='nocopy',
                            value=Constant(value=True, kind=None),
                        ),
                    ],
                ),
            ),
            type_comment=None,
        ),
        ClassDef(
            name='ParseError',
            bases=[Name(id='Exception', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=Ellipsis, kind=None),
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='RecordDictWrapper',
            bases=[Name(id='dict', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value='\n    Used to pass a record as locals in eval:\n    records do not strictly behave like dict, so we force them to.\n    ', kind=None),
                ),
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='record', annotation=None, type_comment=None),
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
                                    attr='record',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='record', ctx=Load()),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='__getitem__',
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
                        If(
                            test=Compare(
                                left=Name(id='key', ctx=Load()),
                                ops=[In()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='record',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='record',
                                            ctx=Load(),
                                        ),
                                        slice=Name(id='key', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='dict', ctx=Load()),
                                    attr='__getitem__',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='self', ctx=Load()),
                                    Name(id='key', ctx=Load()),
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
        FunctionDef(
            name='_get_idref',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='self', annotation=None, type_comment=None),
                    arg(arg='env', annotation=None, type_comment=None),
                    arg(arg='model_str', annotation=None, type_comment=None),
                    arg(arg='idref', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Assign(
                    targets=[Name(id='idref2', ctx=Store())],
                    value=Call(
                        func=Name(id='dict', ctx=Load()),
                        args=[Name(id='idref', ctx=Load())],
                        keywords=[
                            keyword(
                                arg='Command',
                                value=Attribute(
                                    value=Attribute(
                                        value=Name(id='odoo', ctx=Load()),
                                        attr='fields',
                                        ctx=Load(),
                                    ),
                                    attr='Command',
                                    ctx=Load(),
                                ),
                            ),
                            keyword(
                                arg='time',
                                value=Name(id='time', ctx=Load()),
                            ),
                            keyword(
                                arg='DateTime',
                                value=Name(id='datetime', ctx=Load()),
                            ),
                            keyword(
                                arg='datetime',
                                value=Name(id='datetime', ctx=Load()),
                            ),
                            keyword(
                                arg='timedelta',
                                value=Name(id='timedelta', ctx=Load()),
                            ),
                            keyword(
                                arg='relativedelta',
                                value=Name(id='relativedelta', ctx=Load()),
                            ),
                            keyword(
                                arg='version',
                                value=Attribute(
                                    value=Attribute(
                                        value=Name(id='odoo', ctx=Load()),
                                        attr='release',
                                        ctx=Load(),
                                    ),
                                    attr='major_version',
                                    ctx=Load(),
                                ),
                            ),
                            keyword(
                                arg='ref',
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='id_get',
                                    ctx=Load(),
                                ),
                            ),
                            keyword(
                                arg='pytz',
                                value=Name(id='pytz', ctx=Load()),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                If(
                    test=Name(id='model_str', ctx=Load()),
                    body=[
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='idref2', ctx=Load()),
                                    slice=Constant(value='obj', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Subscript(
                                    value=Name(id='env', ctx=Load()),
                                    slice=Name(id='model_str', ctx=Load()),
                                    ctx=Load(),
                                ),
                                attr='browse',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Name(id='idref2', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='_fix_multiple_roots',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='node', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value='\n    Surround the children of the ``node`` element of an XML field with a\n    single root "data" element, to prevent having a document with multiple\n    roots once parsed separately.\n\n    XML nodes should have one root only, but we\'d like to support\n    direct multiple roots in our partial documents (like inherited view architectures).\n    As a convention we\'ll surround multiple root with a container "data" element, to be\n    ignored later when parsing.\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='real_nodes', ctx=Store())],
                    value=ListComp(
                        elt=Name(id='x', ctx=Load()),
                        generators=[
                            comprehension(
                                target=Name(id='x', ctx=Store()),
                                iter=Name(id='node', ctx=Load()),
                                ifs=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Name(id='isinstance', ctx=Load()),
                                            args=[
                                                Name(id='x', ctx=Load()),
                                                Name(id='SKIPPED_ELEMENT_TYPES', ctx=Load()),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                                is_async=0,
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                If(
                    test=Compare(
                        left=Call(
                            func=Name(id='len', ctx=Load()),
                            args=[Name(id='real_nodes', ctx=Load())],
                            keywords=[],
                        ),
                        ops=[Gt()],
                        comparators=[Constant(value=1, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='data_node', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='etree', ctx=Load()),
                                    attr='Element',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='data', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='child', ctx=Store()),
                            iter=Name(id='node', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='data_node', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='child', ctx=Load())],
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
                                    value=Name(id='node', ctx=Load()),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[Name(id='data_node', ctx=Load())],
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
            name='_eval_xml',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='self', annotation=None, type_comment=None),
                    arg(arg='node', annotation=None, type_comment=None),
                    arg(arg='env', annotation=None, type_comment=None),
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
                        left=Attribute(
                            value=Name(id='node', ctx=Load()),
                            attr='tag',
                            ctx=Load(),
                        ),
                        ops=[In()],
                        comparators=[
                            Tuple(
                                elts=[
                                    Constant(value='field', kind=None),
                                    Constant(value='value', kind=None),
                                ],
                                ctx=Load(),
                            ),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='t', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='node', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='type', kind=None),
                                    Constant(value='char', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='f_model', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='node', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='model', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='node', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='search', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='f_search', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='node', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='search', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='f_use', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='node', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='use', kind=None),
                                            Constant(value='id', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='f_name', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='node', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='name', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='idref2', ctx=Store())],
                                    value=Dict(keys=[], values=[]),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='f_search', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='idref2', ctx=Store())],
                                            value=Call(
                                                func=Name(id='_get_idref', ctx=Load()),
                                                args=[
                                                    Name(id='self', ctx=Load()),
                                                    Name(id='env', ctx=Load()),
                                                    Name(id='f_model', ctx=Load()),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='idref',
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
                                Assign(
                                    targets=[Name(id='q', ctx=Store())],
                                    value=Call(
                                        func=Name(id='safe_eval', ctx=Load()),
                                        args=[
                                            Name(id='f_search', ctx=Load()),
                                            Name(id='idref2', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='ids', ctx=Store())],
                                    value=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Name(id='env', ctx=Load()),
                                                    slice=Name(id='f_model', ctx=Load()),
                                                    ctx=Load(),
                                                ),
                                                attr='search',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='q', ctx=Load())],
                                            keywords=[],
                                        ),
                                        attr='ids',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='f_use', ctx=Load()),
                                        ops=[NotEq()],
                                        comparators=[Constant(value='id', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='ids', ctx=Store())],
                                            value=ListComp(
                                                elt=Subscript(
                                                    value=Name(id='x', ctx=Load()),
                                                    slice=Name(id='f_use', ctx=Load()),
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='x', ctx=Store()),
                                                        iter=Call(
                                                            func=Attribute(
                                                                value=Call(
                                                                    func=Attribute(
                                                                        value=Subscript(
                                                                            value=Name(id='env', ctx=Load()),
                                                                            slice=Name(id='f_model', ctx=Load()),
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='browse',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[Name(id='ids', ctx=Load())],
                                                                    keywords=[],
                                                                ),
                                                                attr='read',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                List(
                                                                    elts=[Name(id='f_use', ctx=Load())],
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
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='_fields', ctx=Store())],
                                    value=Attribute(
                                        value=Subscript(
                                            value=Name(id='env', ctx=Load()),
                                            slice=Name(id='f_model', ctx=Load()),
                                            ctx=Load(),
                                        ),
                                        attr='_fields',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Name(id='f_name', ctx=Load()),
                                                ops=[In()],
                                                comparators=[Name(id='_fields', ctx=Load())],
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Subscript(
                                                        value=Name(id='_fields', ctx=Load()),
                                                        slice=Name(id='f_name', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                    attr='type',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='many2many', kind=None)],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Return(
                                            value=Name(id='ids', ctx=Load()),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='f_val', ctx=Store())],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                                If(
                                    test=Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='ids', ctx=Load())],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='f_val', ctx=Store())],
                                            value=Subscript(
                                                value=Name(id='ids', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Call(
                                                func=Name(id='isinstance', ctx=Load()),
                                                args=[
                                                    Name(id='f_val', ctx=Load()),
                                                    Name(id='tuple', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='f_val', ctx=Store())],
                                                    value=Subscript(
                                                        value=Name(id='f_val', ctx=Load()),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Return(
                                    value=Name(id='f_val', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='a_eval', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='node', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='eval', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='a_eval', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='idref2', ctx=Store())],
                                    value=Call(
                                        func=Name(id='_get_idref', ctx=Load()),
                                        args=[
                                            Name(id='self', ctx=Load()),
                                            Name(id='env', ctx=Load()),
                                            Name(id='f_model', ctx=Load()),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='idref',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Try(
                                    body=[
                                        Return(
                                            value=Call(
                                                func=Name(id='safe_eval', ctx=Load()),
                                                args=[
                                                    Name(id='a_eval', ctx=Load()),
                                                    Name(id='idref2', ctx=Load()),
                                                ],
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
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='logging', ctx=Load()),
                                                                    attr='getLogger',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='odoo.tools.convert.init', kind=None)],
                                                                keywords=[],
                                                            ),
                                                            attr='error',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='Could not eval(%s) for %s in %s', kind=None),
                                                            Name(id='a_eval', ctx=Load()),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='node', ctx=Load()),
                                                                    attr='get',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='name', kind=None)],
                                                                keywords=[],
                                                            ),
                                                            Attribute(
                                                                value=Name(id='env', ctx=Load()),
                                                                attr='context',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Raise(exc=None, cause=None),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                    finalbody=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        FunctionDef(
                            name='_process',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='s', annotation=None, type_comment=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='matches', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='re', ctx=Load()),
                                            attr='finditer',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Constant(value=b'[^%]%\\((.*?)\\)[ds]', kind=None),
                                                    attr='decode',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='utf-8', kind=None)],
                                                keywords=[],
                                            ),
                                            Name(id='s', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='done', ctx=Store())],
                                    value=Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='m', ctx=Store()),
                                    iter=Name(id='matches', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='found', ctx=Store())],
                                            value=Subscript(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='m', ctx=Load()),
                                                        attr='group',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                slice=Slice(
                                                    lower=Constant(value=1, kind=None),
                                                    upper=None,
                                                    step=None,
                                                ),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Name(id='found', ctx=Load()),
                                                ops=[In()],
                                                comparators=[Name(id='done', ctx=Load())],
                                            ),
                                            body=[Continue()],
                                            orelse=[],
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='done', ctx=Load()),
                                                    attr='add',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='found', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[Name(id='id', ctx=Store())],
                                            value=Subscript(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='m', ctx=Load()),
                                                        attr='groups',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Compare(
                                                    left=Name(id='id', ctx=Load()),
                                                    ops=[In()],
                                                    comparators=[
                                                        Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='idref',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='idref',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Name(id='id', ctx=Load()),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='id_get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='id', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='s', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='s', ctx=Load()),
                                                    attr='replace',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='found', ctx=Load()),
                                                    Call(
                                                        func=Name(id='str', ctx=Load()),
                                                        args=[
                                                            Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='idref',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Name(id='id', ctx=Load()),
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
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='s', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='s', ctx=Load()),
                                            attr='replace',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='%%', kind=None),
                                            Constant(value='%', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Return(
                                    value=Name(id='s', ctx=Load()),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='t', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='xml', kind=None)],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='_fix_multiple_roots', ctx=Load()),
                                        args=[Name(id='node', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Return(
                                    value=BinOp(
                                        left=Constant(value='<?xml version="1.0"?>\n', kind=None),
                                        op=Add(),
                                        right=Call(
                                            func=Name(id='_process', ctx=Load()),
                                            args=[
                                                Call(
                                                    func=Attribute(
                                                        value=Constant(value='', kind=None),
                                                        attr='join',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        GeneratorExp(
                                                            elt=Call(
                                                                func=Attribute(
                                                                    value=Name(id='etree', ctx=Load()),
                                                                    attr='tostring',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='n', ctx=Load())],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='encoding',
                                                                        value=Constant(value='unicode', kind=None),
                                                                    ),
                                                                ],
                                                            ),
                                                            generators=[
                                                                comprehension(
                                                                    target=Name(id='n', ctx=Store()),
                                                                    iter=Name(id='node', ctx=Load()),
                                                                    ifs=[],
                                                                    is_async=0,
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Name(id='t', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='html', kind=None)],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Name(id='_process', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Constant(value='', kind=None),
                                                    attr='join',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    GeneratorExp(
                                                        elt=Call(
                                                            func=Attribute(
                                                                value=Name(id='etree', ctx=Load()),
                                                                attr='tostring',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Name(id='n', ctx=Load())],
                                                            keywords=[
                                                                keyword(
                                                                    arg='encoding',
                                                                    value=Constant(value='unicode', kind=None),
                                                                ),
                                                            ],
                                                        ),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='n', ctx=Store()),
                                                                iter=Name(id='node', ctx=Load()),
                                                                ifs=[],
                                                                is_async=0,
                                                            ),
                                                        ],
                                                    ),
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
                        Assign(
                            targets=[Name(id='data', ctx=Store())],
                            value=Attribute(
                                value=Name(id='node', ctx=Load()),
                                attr='text',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='node', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='file', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                func=Name(id='file_open', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='node', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='file', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Constant(value='rb', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            optional_vars=Name(id='f', ctx=Store()),
                                        ),
                                    ],
                                    body=[
                                        Assign(
                                            targets=[Name(id='data', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='f', ctx=Load()),
                                                    attr='read',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Name(id='t', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='base64', kind=None)],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='base64', ctx=Load()),
                                            attr='b64encode',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='data', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='pycompat', ctx=Load()),
                                    attr='to_text',
                                    ctx=Load(),
                                ),
                                args=[Name(id='data', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='t', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='file', kind=None)],
                            ),
                            body=[
                                ImportFrom(
                                    module='modules',
                                    names=[alias(name='module', asname=None)],
                                    level=2,
                                ),
                                Assign(
                                    targets=[Name(id='path', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='data', ctx=Load()),
                                            attr='strip',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Name(id='module', ctx=Load()),
                                                attr='get_module_resource',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='module',
                                                    ctx=Load(),
                                                ),
                                                Name(id='path', ctx=Load()),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='IOError', ctx=Load()),
                                                args=[
                                                    BinOp(
                                                        left=Constant(value="No such file or directory: '%s' in %s", kind=None),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            elts=[
                                                                Name(id='path', ctx=Load()),
                                                                Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='module',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Return(
                                    value=BinOp(
                                        left=Constant(value='%s,%s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='module',
                                                    ctx=Load(),
                                                ),
                                                Name(id='path', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Name(id='t', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='char', kind=None)],
                            ),
                            body=[
                                Return(
                                    value=Name(id='data', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Name(id='t', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='int', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='d', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='data', ctx=Load()),
                                            attr='strip',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='d', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='None', kind=None)],
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
                                        func=Name(id='int', ctx=Load()),
                                        args=[Name(id='d', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Name(id='t', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='float', kind=None)],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Name(id='float', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='data', ctx=Load()),
                                                    attr='strip',
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
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Name(id='t', ctx=Load()),
                                ops=[In()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value='list', kind=None),
                                            Constant(value='tuple', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='res', ctx=Store())],
                                    value=List(elts=[], ctx=Load()),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='n', ctx=Store()),
                                    iter=Call(
                                        func=Attribute(
                                            value=Name(id='node', ctx=Load()),
                                            attr='iterchildren',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='tag',
                                                value=Constant(value='value', kind=None),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='res', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Name(id='_eval_xml', ctx=Load()),
                                                        args=[
                                                            Name(id='self', ctx=Load()),
                                                            Name(id='n', ctx=Load()),
                                                            Name(id='env', ctx=Load()),
                                                        ],
                                                        keywords=[],
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
                                    test=Compare(
                                        left=Name(id='t', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='tuple', kind=None)],
                                    ),
                                    body=[
                                        Return(
                                            value=Call(
                                                func=Name(id='tuple', ctx=Load()),
                                                args=[Name(id='res', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Return(
                                    value=Name(id='res', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    orelse=[
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='node', ctx=Load()),
                                    attr='tag',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='function', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='model_str', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='node', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='model', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='model', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='env', ctx=Load()),
                                        slice=Name(id='model_str', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='method_name', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='node', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='name', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='args', ctx=Store())],
                                    value=List(elts=[], ctx=Load()),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='kwargs', ctx=Store())],
                                    value=Dict(keys=[], values=[]),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='a_eval', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='node', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='eval', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='a_eval', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='idref2', ctx=Store())],
                                            value=Call(
                                                func=Name(id='_get_idref', ctx=Load()),
                                                args=[
                                                    Name(id='self', ctx=Load()),
                                                    Name(id='env', ctx=Load()),
                                                    Name(id='model_str', ctx=Load()),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='idref',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='args', ctx=Store())],
                                            value=Call(
                                                func=Name(id='list', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='safe_eval', ctx=Load()),
                                                        args=[
                                                            Name(id='a_eval', ctx=Load()),
                                                            Name(id='idref2', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                For(
                                    target=Name(id='child', ctx=Store()),
                                    iter=Name(id='node', ctx=Load()),
                                    body=[
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Compare(
                                                        left=Attribute(
                                                            value=Name(id='child', ctx=Load()),
                                                            attr='tag',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='value', kind=None)],
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='child', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='name', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='kwargs', ctx=Load()),
                                                            slice=Call(
                                                                func=Attribute(
                                                                    value=Name(id='child', ctx=Load()),
                                                                    attr='get',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='name', kind=None)],
                                                                keywords=[],
                                                            ),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Call(
                                                        func=Name(id='_eval_xml', ctx=Load()),
                                                        args=[
                                                            Name(id='self', ctx=Load()),
                                                            Name(id='child', ctx=Load()),
                                                            Name(id='env', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='args', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Name(id='_eval_xml', ctx=Load()),
                                                                args=[
                                                                    Name(id='self', ctx=Load()),
                                                                    Name(id='child', ctx=Load()),
                                                                    Name(id='env', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='kwargs', ctx=Load()),
                                            slice=Constant(value='context', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Dict(
                                        keys=[
                                            None,
                                            None,
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='env', ctx=Load()),
                                                attr='context',
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='kwargs', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='context', kind=None),
                                                    Dict(keys=[], values=[]),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='odoo', ctx=Load()),
                                                attr='api',
                                                ctx=Load(),
                                            ),
                                            attr='call_kw',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='model', ctx=Load()),
                                            Name(id='method_name', ctx=Load()),
                                            Name(id='args', ctx=Load()),
                                            Name(id='kwargs', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='node', ctx=Load()),
                                            attr='tag',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='test', kind=None)],
                                    ),
                                    body=[
                                        Return(
                                            value=Attribute(
                                                value=Name(id='node', ctx=Load()),
                                                attr='text',
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                    orelse=[],
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
            name='str2bool',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='value', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Return(
                    value=Compare(
                        left=Call(
                            func=Attribute(
                                value=Name(id='value', ctx=Load()),
                                attr='lower',
                                ctx=Load(),
                            ),
                            args=[],
                            keywords=[],
                        ),
                        ops=[NotIn()],
                        comparators=[
                            Tuple(
                                elts=[
                                    Constant(value='0', kind=None),
                                    Constant(value='false', kind=None),
                                    Constant(value='off', kind=None),
                                ],
                                ctx=Load(),
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
            name='nodeattr2bool',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='node', annotation=None, type_comment=None),
                    arg(arg='attr', annotation=None, type_comment=None),
                    arg(arg='default', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[Constant(value=False, kind=None)],
            ),
            body=[
                If(
                    test=UnaryOp(
                        op=Not(),
                        operand=Call(
                            func=Attribute(
                                value=Name(id='node', ctx=Load()),
                                attr='get',
                                ctx=Load(),
                            ),
                            args=[Name(id='attr', ctx=Load())],
                            keywords=[],
                        ),
                    ),
                    body=[
                        Return(
                            value=Name(id='default', ctx=Load()),
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    targets=[Name(id='val', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='node', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Name(id='attr', ctx=Load())],
                                keywords=[],
                            ),
                            attr='strip',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=UnaryOp(
                        op=Not(),
                        operand=Name(id='val', ctx=Load()),
                    ),
                    body=[
                        Return(
                            value=Name(id='default', ctx=Load()),
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Call(
                        func=Name(id='str2bool', ctx=Load()),
                        args=[Name(id='val', ctx=Load())],
                        keywords=[],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        ClassDef(
            name='xml_import',
            bases=[Name(id='object', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='get_env',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='node', annotation=None, type_comment=None),
                            arg(arg='eval_context', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='uid', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='node', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='uid', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='context', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='node', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='context', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='uid', ctx=Load()),
                                    Name(id='context', ctx=Load()),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='user',
                                                value=BoolOp(
                                                    op=And(),
                                                    values=[
                                                        Name(id='uid', ctx=Load()),
                                                        Call(
                                                            func=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='id_get',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Name(id='uid', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                ),
                                            ),
                                            keyword(
                                                arg='context',
                                                value=BoolOp(
                                                    op=And(),
                                                    values=[
                                                        Name(id='context', ctx=Load()),
                                                        Dict(
                                                            keys=[
                                                                None,
                                                                None,
                                                            ],
                                                            values=[
                                                                Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='env',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='context',
                                                                    ctx=Load(),
                                                                ),
                                                                Call(
                                                                    func=Name(id='safe_eval', ctx=Load()),
                                                                    args=[
                                                                        Name(id='context', ctx=Load()),
                                                                        Dict(
                                                                            keys=[
                                                                                Constant(value='ref', kind=None),
                                                                                None,
                                                                            ],
                                                                            values=[
                                                                                Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='id_get',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                BoolOp(
                                                                                    op=Or(),
                                                                                    values=[
                                                                                        Name(id='eval_context', ctx=Load()),
                                                                                        Dict(keys=[], values=[]),
                                                                                    ],
                                                                                ),
                                                                            ],
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='env',
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='make_xml_id',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='xml_id', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='xml_id', ctx=Load()),
                                    ),
                                    Compare(
                                        left=Constant(value='.', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='xml_id', ctx=Load())],
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Name(id='xml_id', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=BinOp(
                                left=Constant(value='%s.%s', kind=None),
                                op=Mod(),
                                right=Tuple(
                                    elts=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='module',
                                            ctx=Load(),
                                        ),
                                        Name(id='xml_id', ctx=Load()),
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
                    name='_test_xml_id',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='xml_id', annotation=None, type_comment=None),
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
                                left=Constant(value='.', kind=None),
                                ops=[In()],
                                comparators=[Name(id='xml_id', ctx=Load())],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='module', ctx=Store()),
                                                Name(id='id', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='xml_id', ctx=Load()),
                                            attr='split',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='.', kind=None),
                                            Constant(value=1, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assert(
                                    test=Compare(
                                        left=Constant(value='.', kind=None),
                                        ops=[NotIn()],
                                        comparators=[Name(id='id', ctx=Load())],
                                    ),
                                    msg=BinOp(
                                        left=Constant(value='The ID reference "%s" must contain\nmaximum one dot. They are used to refer to other modules ID, in the\nform: module.record_id', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[Name(id='xml_id', ctx=Load())],
                                            ctx=Load(),
                                        ),
                                    ),
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='module', ctx=Load()),
                                        ops=[NotEq()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='module',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='modcnt', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='ir.module.module', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='search_count',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    Name(id='module', ctx=Load()),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='state', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    Constant(value='installed', kind=None),
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
                                        Assert(
                                            test=Compare(
                                                left=Name(id='modcnt', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value=1, kind=None)],
                                            ),
                                            msg=BinOp(
                                                left=Constant(value='The ID "%s" refers to an uninstalled module', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[Name(id='xml_id', ctx=Load())],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ),
                                    ],
                                    orelse=[],
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
                    name='_tag_delete',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='rec', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='d_model', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='rec', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='model', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='records', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Name(id='d_model', ctx=Load()),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='d_search', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='rec', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='search', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='d_search', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='idref', ctx=Store())],
                                    value=Call(
                                        func=Name(id='_get_idref', ctx=Load()),
                                        args=[
                                            Name(id='self', ctx=Load()),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            Name(id='d_model', ctx=Load()),
                                            Dict(keys=[], values=[]),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Try(
                                    body=[
                                        Assign(
                                            targets=[Name(id='records', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='records', ctx=Load()),
                                                    attr='search',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Name(id='safe_eval', ctx=Load()),
                                                        args=[
                                                            Name(id='d_search', ctx=Load()),
                                                            Name(id='idref', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='ValueError', ctx=Load()),
                                            name=None,
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='_logger', ctx=Load()),
                                                            attr='warning',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='Skipping deletion for failed search `%r`', kind=None),
                                                            Name(id='d_search', ctx=Load()),
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
                        ),
                        Assign(
                            targets=[Name(id='d_id', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='rec', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='id', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='d_id', ctx=Load()),
                            body=[
                                Try(
                                    body=[
                                        AugAssign(
                                            target=Name(id='records', ctx=Store()),
                                            op=Add(),
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='records', ctx=Load()),
                                                    attr='browse',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='id_get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='d_id', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='ValueError', ctx=Load()),
                                            name=None,
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='_logger', ctx=Load()),
                                                            attr='warning',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='Skipping deletion for missing XML ID `%r`', kind=None),
                                                            Name(id='d_id', ctx=Load()),
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
                        ),
                        If(
                            test=Name(id='records', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='records', ctx=Load()),
                                            attr='unlink',
                                            ctx=Load(),
                                        ),
                                        args=[],
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
                    name='_tag_report',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='rec', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='dest', ctx=Store()),
                                    Name(id='f', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Tuple(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='name', kind=None),
                                            Constant(value='string', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='model', kind=None),
                                            Constant(value='model', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='report_name', kind=None),
                                            Constant(value='name', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='res', ctx=Load()),
                                            slice=Name(id='dest', ctx=Load()),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='rec', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='f', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assert(
                                    test=Subscript(
                                        value=Name(id='res', ctx=Load()),
                                        slice=Name(id='dest', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    msg=BinOp(
                                        left=Constant(value='Attribute %s of report is empty !', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[Name(id='f', ctx=Load())],
                                            ctx=Load(),
                                        ),
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='field', ctx=Store()),
                                    Name(id='dest', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Tuple(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='attachment', kind=None),
                                            Constant(value='attachment', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='attachment_use', kind=None),
                                            Constant(value='attachment_use', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='usage', kind=None),
                                            Constant(value='usage', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='file', kind=None),
                                            Constant(value='report_file', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='report_type', kind=None),
                                            Constant(value='report_type', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='parser', kind=None),
                                            Constant(value='parser', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='print_report_name', kind=None),
                                            Constant(value='print_report_name', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            body=[
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Name(id='rec', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='field', ctx=Load())],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='res', ctx=Load()),
                                                    slice=Name(id='dest', ctx=Load()),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='rec', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='field', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='rec', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='auto', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='res', ctx=Load()),
                                            slice=Constant(value='auto', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='safe_eval', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='rec', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='auto', kind=None),
                                                    Constant(value='False', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='rec', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='header', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='res', ctx=Load()),
                                            slice=Constant(value='header', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='safe_eval', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='rec', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='header', kind=None),
                                                    Constant(value='False', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='res', ctx=Load()),
                                    slice=Constant(value='multi', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=BoolOp(
                                op=And(),
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='rec', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='multi', kind=None)],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='safe_eval', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='rec', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='multi', kind=None),
                                                    Constant(value='False', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='xml_id', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='rec', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='id', kind=None),
                                    Constant(value='', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_test_xml_id',
                                    ctx=Load(),
                                ),
                                args=[Name(id='xml_id', ctx=Load())],
                                keywords=[],
                            ),
                        ),
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
                                            Constant(value='The <report> tag is deprecated, use a <record> tag for ', kind=None),
                                            FormattedValue(
                                                value=Name(id='xml_id', ctx=Load()),
                                                conversion=114,
                                                format_spec=None,
                                            ),
                                            Constant(value='.', kind=None),
                                        ],
                                    ),
                                    Name(id='DeprecationWarning', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='rec', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='groups', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='g_names', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='rec', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='groups', kind=None),
                                                    Constant(value='', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='split',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value=',', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='groups_value', ctx=Store())],
                                    value=List(elts=[], ctx=Load()),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='group', ctx=Store()),
                                    iter=Name(id='g_names', ctx=Load()),
                                    body=[
                                        If(
                                            test=Call(
                                                func=Attribute(
                                                    value=Name(id='group', ctx=Load()),
                                                    attr='startswith',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='-', kind=None)],
                                                keywords=[],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='group_id', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='id_get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='group', ctx=Load()),
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
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='groups_value', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='odoo', ctx=Load()),
                                                                        attr='Command',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='unlink',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='group_id', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[Name(id='group_id', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='id_get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='group', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='groups_value', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='odoo', ctx=Load()),
                                                                        attr='Command',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='link',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='group_id', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='res', ctx=Load()),
                                            slice=Constant(value='groups_id', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='groups_value', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='rec', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='paperformat', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='pf_name', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='rec', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='paperformat', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='pf_id', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='id_get',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='pf_name', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='res', ctx=Load()),
                                            slice=Constant(value='paperformat_id', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='pf_id', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='xid', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='make_xml_id',
                                    ctx=Load(),
                                ),
                                args=[Name(id='xml_id', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='data', ctx=Store())],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='xml_id',
                                        value=Name(id='xid', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='values',
                                        value=Name(id='res', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='noupdate',
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='noupdate',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='report', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.actions.report', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_load_records',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Name(id='data', ctx=Load())],
                                        ctx=Load(),
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='mode',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='update', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='idref',
                                        ctx=Load(),
                                    ),
                                    slice=Name(id='xml_id', ctx=Load()),
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='report', ctx=Load()),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Name(id='rec', ctx=Load()),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='menu', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                    Call(
                                        func=Name(id='safe_eval', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='rec', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='menu', kind=None),
                                                    Constant(value='False', kind=None),
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
                                            value=Name(id='report', ctx=Load()),
                                            attr='create_action',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='mode',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='update', kind=None)],
                                            ),
                                            Compare(
                                                left=Call(
                                                    func=Name(id='safe_eval', ctx=Load()),
                                                    args=[
                                                        Call(
                                                            func=Attribute(
                                                                value=Name(id='rec', ctx=Load()),
                                                                attr='get',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Constant(value='menu', kind=None),
                                                                Constant(value='False', kind=None),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value=False, kind=None)],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='report', ctx=Load()),
                                                    attr='unlink_action',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                        ),
                        Return(
                            value=Attribute(
                                value=Name(id='report', ctx=Load()),
                                attr='id',
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_tag_function',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='rec', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='noupdate',
                                        ctx=Load(),
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='mode',
                                            ctx=Load(),
                                        ),
                                        ops=[NotEq()],
                                        comparators=[Constant(value='init', kind=None)],
                                    ),
                                ],
                            ),
                            body=[Return(value=None)],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='env', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='get_env',
                                    ctx=Load(),
                                ),
                                args=[Name(id='rec', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='_eval_xml', ctx=Load()),
                                args=[
                                    Name(id='self', ctx=Load()),
                                    Name(id='rec', ctx=Load()),
                                    Name(id='env', ctx=Load()),
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
                    name='_tag_act_window',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='rec', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='name', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='rec', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='name', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='xml_id', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='rec', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='id', kind=None),
                                    Constant(value='', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_test_xml_id',
                                    ctx=Load(),
                                ),
                                args=[Name(id='xml_id', ctx=Load())],
                                keywords=[],
                            ),
                        ),
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
                                            Constant(value='The <act_window> tag is deprecated, use a <record> for ', kind=None),
                                            FormattedValue(
                                                value=Name(id='xml_id', ctx=Load()),
                                                conversion=114,
                                                format_spec=None,
                                            ),
                                            Constant(value='.', kind=None),
                                        ],
                                    ),
                                    Name(id='DeprecationWarning', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='view_id', ctx=Store())],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='rec', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='view_id', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='view_id', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='id_get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='rec', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='view_id', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='domain', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='rec', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='domain', kind=None)],
                                        keywords=[],
                                    ),
                                    Constant(value='[]', kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='res_model', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='rec', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='res_model', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='binding_model', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='rec', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='binding_model', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='view_mode', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='rec', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='view_mode', kind=None)],
                                        keywords=[],
                                    ),
                                    Constant(value='tree,form', kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='usage', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='rec', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='usage', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='limit', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='rec', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='limit', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='uid', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='user',
                                    ctx=Load(),
                                ),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='active_id', ctx=Store())],
                            value=Call(
                                func=Name(id='unquote', ctx=Load()),
                                args=[Constant(value='active_id', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='active_ids', ctx=Store())],
                            value=Call(
                                func=Name(id='unquote', ctx=Load()),
                                args=[Constant(value='active_ids', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='active_model', ctx=Store())],
                            value=Call(
                                func=Name(id='unquote', ctx=Load()),
                                args=[Constant(value='active_model', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='eval_context', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='name', kind=None),
                                    Constant(value='xml_id', kind=None),
                                    Constant(value='type', kind=None),
                                    Constant(value='view_id', kind=None),
                                    Constant(value='domain', kind=None),
                                    Constant(value='res_model', kind=None),
                                    Constant(value='src_model', kind=None),
                                    Constant(value='view_mode', kind=None),
                                    Constant(value='usage', kind=None),
                                    Constant(value='limit', kind=None),
                                    Constant(value='uid', kind=None),
                                    Constant(value='active_id', kind=None),
                                    Constant(value='active_ids', kind=None),
                                    Constant(value='active_model', kind=None),
                                ],
                                values=[
                                    Name(id='name', ctx=Load()),
                                    Name(id='xml_id', ctx=Load()),
                                    Constant(value='ir.actions.act_window', kind=None),
                                    Name(id='view_id', ctx=Load()),
                                    Name(id='domain', ctx=Load()),
                                    Name(id='res_model', ctx=Load()),
                                    Name(id='binding_model', ctx=Load()),
                                    Name(id='view_mode', ctx=Load()),
                                    Name(id='usage', ctx=Load()),
                                    Name(id='limit', ctx=Load()),
                                    Name(id='uid', ctx=Load()),
                                    Name(id='active_id', ctx=Load()),
                                    Name(id='active_ids', ctx=Load()),
                                    Name(id='active_model', ctx=Load()),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='context', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='get_env',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Name(id='rec', ctx=Load()),
                                        Name(id='eval_context', ctx=Load()),
                                    ],
                                    keywords=[],
                                ),
                                attr='context',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id='domain', ctx=Store())],
                                    value=Call(
                                        func=Name(id='safe_eval', ctx=Load()),
                                        args=[
                                            Name(id='domain', ctx=Load()),
                                            Name(id='eval_context', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Tuple(
                                        elts=[
                                            Name(id='ValueError', ctx=Load()),
                                            Name(id='NameError', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                    name=None,
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='debug',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='Domain value (%s) for element with id "%s" does not parse at server-side, keeping original string, in case it\'s meant for client side only', kind=None),
                                                    Name(id='domain', ctx=Load()),
                                                    BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            Name(id='xml_id', ctx=Load()),
                                                            Constant(value='n/a', kind=None),
                                                        ],
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
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='name', kind=None),
                                    Constant(value='type', kind=None),
                                    Constant(value='view_id', kind=None),
                                    Constant(value='domain', kind=None),
                                    Constant(value='context', kind=None),
                                    Constant(value='res_model', kind=None),
                                    Constant(value='view_mode', kind=None),
                                    Constant(value='usage', kind=None),
                                    Constant(value='limit', kind=None),
                                ],
                                values=[
                                    Name(id='name', ctx=Load()),
                                    Constant(value='ir.actions.act_window', kind=None),
                                    Name(id='view_id', ctx=Load()),
                                    Name(id='domain', ctx=Load()),
                                    Name(id='context', ctx=Load()),
                                    Name(id='res_model', ctx=Load()),
                                    Name(id='view_mode', ctx=Load()),
                                    Name(id='usage', ctx=Load()),
                                    Name(id='limit', ctx=Load()),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='rec', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='groups', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='g_names', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='rec', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='groups', kind=None),
                                                    Constant(value='', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='split',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value=',', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='groups_value', ctx=Store())],
                                    value=List(elts=[], ctx=Load()),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='group', ctx=Store()),
                                    iter=Name(id='g_names', ctx=Load()),
                                    body=[
                                        If(
                                            test=Call(
                                                func=Attribute(
                                                    value=Name(id='group', ctx=Load()),
                                                    attr='startswith',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='-', kind=None)],
                                                keywords=[],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='group_id', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='id_get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='group', ctx=Load()),
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
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='groups_value', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='odoo', ctx=Load()),
                                                                        attr='Command',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='unlink',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='group_id', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[Name(id='group_id', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='id_get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='group', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='groups_value', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='odoo', ctx=Load()),
                                                                        attr='Command',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='link',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='group_id', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='res', ctx=Load()),
                                            slice=Constant(value='groups_id', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='groups_value', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='rec', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='target', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='res', ctx=Load()),
                                            slice=Constant(value='target', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='rec', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='target', kind=None),
                                            Constant(value='', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Name(id='binding_model', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='res', ctx=Load()),
                                            slice=Constant(value='binding_model_id', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='ir.model', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='_get',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='binding_model', ctx=Load())],
                                            keywords=[],
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='res', ctx=Load()),
                                            slice=Constant(value='binding_type', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='rec', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='binding_type', kind=None)],
                                                keywords=[],
                                            ),
                                            Constant(value='action', kind=None),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='views', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='rec', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='binding_views', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='views', ctx=Load()),
                                        ops=[IsNot()],
                                        comparators=[Constant(value=None, kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='res', ctx=Load()),
                                                    slice=Constant(value='binding_view_types', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='views', ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='xid', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='make_xml_id',
                                    ctx=Load(),
                                ),
                                args=[Name(id='xml_id', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='data', ctx=Store())],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='xml_id',
                                        value=Name(id='xid', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='values',
                                        value=Name(id='res', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='noupdate',
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='noupdate',
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
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.actions.act_window', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_load_records',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Name(id='data', ctx=Load())],
                                        ctx=Load(),
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='mode',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='update', kind=None)],
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
                    name='_tag_menuitem',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='rec', annotation=None, type_comment=None),
                            arg(arg='parent', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='rec_id', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='rec', ctx=Load()),
                                    attr='attrib',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='id', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_test_xml_id',
                                    ctx=Load(),
                                ),
                                args=[Name(id='rec_id', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='parent_id', kind=None),
                                    Constant(value='active', kind=None),
                                ],
                                values=[
                                    Constant(value=False, kind=None),
                                    Call(
                                        func=Name(id='nodeattr2bool', ctx=Load()),
                                        args=[
                                            Name(id='rec', ctx=Load()),
                                            Constant(value='active', kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='default',
                                                value=Constant(value=True, kind=None),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='rec', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='sequence', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='values', ctx=Load()),
                                            slice=Constant(value='sequence', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='int', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='rec', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='sequence', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Name(id='parent', ctx=Load()),
                                ops=[IsNot()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='values', ctx=Load()),
                                            slice=Constant(value='parent_id', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='parent', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Name(id='rec', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='parent', kind=None)],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='values', ctx=Load()),
                                                    slice=Constant(value='parent_id', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='id_get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Subscript(
                                                        value=Attribute(
                                                            value=Name(id='rec', ctx=Load()),
                                                            attr='attrib',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='parent', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Call(
                                                func=Attribute(
                                                    value=Name(id='rec', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='web_icon', kind=None)],
                                                keywords=[],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='values', ctx=Load()),
                                                            slice=Constant(value='web_icon', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='rec', ctx=Load()),
                                                            attr='attrib',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='web_icon', kind=None),
                                                        ctx=Load(),
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
                            test=Call(
                                func=Attribute(
                                    value=Name(id='rec', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='name', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='values', ctx=Load()),
                                            slice=Constant(value='name', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='rec', ctx=Load()),
                                            attr='attrib',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='name', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='rec', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='action', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='a_action', ctx=Store())],
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='rec', ctx=Load()),
                                            attr='attrib',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='action', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Constant(value='.', kind=None),
                                        ops=[NotIn()],
                                        comparators=[Name(id='a_action', ctx=Load())],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='a_action', ctx=Store())],
                                            value=BinOp(
                                                left=Constant(value='%s.%s', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='module',
                                                            ctx=Load(),
                                                        ),
                                                        Name(id='a_action', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='act', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='ref',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='a_action', ctx=Load())],
                                                keywords=[],
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='values', ctx=Load()),
                                            slice=Constant(value='action', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BinOp(
                                        left=Constant(value='%s,%d', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Attribute(
                                                    value=Name(id='act', ctx=Load()),
                                                    attr='type',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Name(id='act', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Call(
                                                    func=Attribute(
                                                        value=Name(id='values', ctx=Load()),
                                                        attr='get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='name', kind=None)],
                                                    keywords=[],
                                                ),
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='act', ctx=Load()),
                                                        attr='type',
                                                        ctx=Load(),
                                                    ),
                                                    attr='endswith',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='act_window', kind=None),
                                                            Constant(value='wizard', kind=None),
                                                            Constant(value='url', kind=None),
                                                            Constant(value='client', kind=None),
                                                            Constant(value='server', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Attribute(
                                                value=Name(id='act', ctx=Load()),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='values', ctx=Load()),
                                                    slice=Constant(value='name', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Attribute(
                                                value=Name(id='act', ctx=Load()),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Name(id='values', ctx=Load()),
                                        attr='get',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='name', kind=None)],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='values', ctx=Load()),
                                            slice=Constant(value='name', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Name(id='rec_id', ctx=Load()),
                                            Constant(value='?', kind=None),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='groups', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='group', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='rec', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='groups', kind=None),
                                            Constant(value='', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='split',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=',', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Name(id='group', ctx=Load()),
                                            attr='startswith',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='-', kind=None)],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='group_id', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='id_get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='group', ctx=Load()),
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
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='groups', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='odoo', ctx=Load()),
                                                                attr='Command',
                                                                ctx=Load(),
                                                            ),
                                                            attr='unlink',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='group_id', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Name(id='group', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='group_id', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='id_get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='group', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='groups', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='odoo', ctx=Load()),
                                                                        attr='Command',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='link',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='group_id', ctx=Load())],
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
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='groups', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='values', ctx=Load()),
                                            slice=Constant(value='groups_id', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='groups', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='data', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='xml_id', kind=None),
                                    Constant(value='values', kind=None),
                                    Constant(value='noupdate', kind=None),
                                ],
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='make_xml_id',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='rec_id', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Name(id='values', ctx=Load()),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='noupdate',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='menu', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.ui.menu', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_load_records',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Name(id='data', ctx=Load())],
                                        ctx=Load(),
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='mode',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='update', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='child', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='rec', ctx=Load()),
                                    attr='iterchildren',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='menuitem', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_tag_menuitem',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='child', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='parent',
                                                value=Attribute(
                                                    value=Name(id='menu', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
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
                FunctionDef(
                    name='_tag_record',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='rec', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='rec_model', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='rec', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='model', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='env', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='get_env',
                                    ctx=Load(),
                                ),
                                args=[Name(id='rec', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='rec_id', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='rec', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='id', kind=None),
                                    Constant(value='', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='model', ctx=Store())],
                            value=Subscript(
                                value=Name(id='env', ctx=Load()),
                                slice=Name(id='rec_model', ctx=Load()),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='xml_filename',
                                        ctx=Load(),
                                    ),
                                    Name(id='rec_id', ctx=Load()),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='model', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='model', ctx=Load()),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='install_module',
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='module',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='install_filename',
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='xml_filename',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='install_xmlid',
                                                value=Name(id='rec_id', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_test_xml_id',
                                    ctx=Load(),
                                ),
                                args=[Name(id='rec_id', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='xid', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='make_xml_id',
                                    ctx=Load(),
                                ),
                                args=[Name(id='rec_id', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='noupdate',
                                        ctx=Load(),
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='mode',
                                            ctx=Load(),
                                        ),
                                        ops=[NotEq()],
                                        comparators=[Constant(value='init', kind=None)],
                                    ),
                                ],
                            ),
                            body=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='rec_id', ctx=Load()),
                                    ),
                                    body=[
                                        Return(
                                            value=Constant(value=None, kind=None),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='record', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='env', ctx=Load()),
                                                slice=Constant(value='ir.model.data', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='_load_xmlid',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='xid', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='record', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='idref',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Name(id='rec_id', ctx=Load()),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Attribute(
                                                value=Name(id='record', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Return(
                                            value=Constant(value=None, kind=None),
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Call(
                                                    func=Name(id='nodeattr2bool', ctx=Load()),
                                                    args=[
                                                        Name(id='rec', ctx=Load()),
                                                        Constant(value='forcecreate', kind=None),
                                                        Constant(value=True, kind=None),
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
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='xid', ctx=Load()),
                                    Compare(
                                        left=Subscript(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='xid', ctx=Load()),
                                                    attr='partition',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='.', kind=None)],
                                                keywords=[],
                                            ),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        ops=[NotEq()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='module',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='record', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='ir.model.data', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='_load_xmlid',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='xid', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='record', ctx=Load()),
                                    ),
                                    body=[
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='noupdate',
                                                        ctx=Load(),
                                                    ),
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Call(
                                                            func=Name(id='nodeattr2bool', ctx=Load()),
                                                            args=[
                                                                Name(id='rec', ctx=Load()),
                                                                Constant(value='forcecreate', kind=None),
                                                                Constant(value=True, kind=None),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Return(
                                                    value=Constant(value=None, kind=None),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Raise(
                                            exc=Call(
                                                func=Name(id='Exception', ctx=Load()),
                                                args=[
                                                    BinOp(
                                                        left=Constant(value='Cannot update missing record %r', kind=None),
                                                        op=Mod(),
                                                        right=Name(id='xid', ctx=Load()),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='field', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='rec', ctx=Load()),
                                    attr='findall',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='./field', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='f_name', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='field', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='name', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='f_ref', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='field', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='ref', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='f_search', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='field', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='search', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='f_model', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='field', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='model', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Name(id='f_model', ctx=Load()),
                                            ),
                                            Compare(
                                                left=Name(id='f_name', ctx=Load()),
                                                ops=[In()],
                                                comparators=[
                                                    Attribute(
                                                        value=Name(id='model', ctx=Load()),
                                                        attr='_fields',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='f_model', ctx=Store())],
                                            value=Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='model', ctx=Load()),
                                                        attr='_fields',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Name(id='f_name', ctx=Load()),
                                                    ctx=Load(),
                                                ),
                                                attr='comodel_name',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='f_use', ctx=Store())],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='field', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='use', kind=None),
                                                    Constant(value='', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Constant(value='id', kind=None),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='f_val', ctx=Store())],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='f_search', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='idref2', ctx=Store())],
                                            value=Call(
                                                func=Name(id='_get_idref', ctx=Load()),
                                                args=[
                                                    Name(id='self', ctx=Load()),
                                                    Name(id='env', ctx=Load()),
                                                    Name(id='f_model', ctx=Load()),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='idref',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='q', ctx=Store())],
                                            value=Call(
                                                func=Name(id='safe_eval', ctx=Load()),
                                                args=[
                                                    Name(id='f_search', ctx=Load()),
                                                    Name(id='idref2', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assert(
                                            test=Name(id='f_model', ctx=Load()),
                                            msg=Constant(value='Define an attribute model="..." in your .XML file !', kind=None),
                                        ),
                                        Assign(
                                            targets=[Name(id='s', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Name(id='env', ctx=Load()),
                                                        slice=Name(id='f_model', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                    attr='search',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='q', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='_fields', ctx=Store())],
                                            value=Attribute(
                                                value=Subscript(
                                                    value=Name(id='env', ctx=Load()),
                                                    slice=Name(id='rec_model', ctx=Load()),
                                                    ctx=Load(),
                                                ),
                                                attr='_fields',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Compare(
                                                        left=Name(id='f_name', ctx=Load()),
                                                        ops=[In()],
                                                        comparators=[Name(id='_fields', ctx=Load())],
                                                    ),
                                                    Compare(
                                                        left=Attribute(
                                                            value=Subscript(
                                                                value=Name(id='_fields', ctx=Load()),
                                                                slice=Name(id='f_name', ctx=Load()),
                                                                ctx=Load(),
                                                            ),
                                                            attr='type',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='many2many', kind=None)],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='f_val', ctx=Store())],
                                                    value=List(
                                                        elts=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='odoo', ctx=Load()),
                                                                        attr='Command',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='set',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    ListComp(
                                                                        elt=Subscript(
                                                                            value=Name(id='x', ctx=Load()),
                                                                            slice=Name(id='f_use', ctx=Load()),
                                                                            ctx=Load(),
                                                                        ),
                                                                        generators=[
                                                                            comprehension(
                                                                                target=Name(id='x', ctx=Store()),
                                                                                iter=Name(id='s', ctx=Load()),
                                                                                ifs=[],
                                                                                is_async=0,
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Call(
                                                        func=Name(id='len', ctx=Load()),
                                                        args=[Name(id='s', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='f_val', ctx=Store())],
                                                            value=Subscript(
                                                                value=Subscript(
                                                                    value=Name(id='s', ctx=Load()),
                                                                    slice=Constant(value=0, kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Name(id='f_use', ctx=Load()),
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Name(id='f_ref', ctx=Load()),
                                            body=[
                                                If(
                                                    test=BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Compare(
                                                                left=Name(id='f_name', ctx=Load()),
                                                                ops=[In()],
                                                                comparators=[
                                                                    Attribute(
                                                                        value=Name(id='model', ctx=Load()),
                                                                        attr='_fields',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                            Compare(
                                                                left=Attribute(
                                                                    value=Subscript(
                                                                        value=Attribute(
                                                                            value=Name(id='model', ctx=Load()),
                                                                            attr='_fields',
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Name(id='f_name', ctx=Load()),
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='type',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='reference', kind=None)],
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='val', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='model_id_get',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='f_ref', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='f_val', ctx=Store())],
                                                            value=BinOp(
                                                                left=BinOp(
                                                                    left=Subscript(
                                                                        value=Name(id='val', ctx=Load()),
                                                                        slice=Constant(value=0, kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    op=Add(),
                                                                    right=Constant(value=',', kind=None),
                                                                ),
                                                                op=Add(),
                                                                right=Call(
                                                                    func=Name(id='str', ctx=Load()),
                                                                    args=[
                                                                        Subscript(
                                                                            value=Name(id='val', ctx=Load()),
                                                                            slice=Constant(value=1, kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[
                                                        Assign(
                                                            targets=[Name(id='f_val', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='id_get',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='f_ref', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[Name(id='f_val', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='_eval_xml', ctx=Load()),
                                                        args=[
                                                            Name(id='self', ctx=Load()),
                                                            Name(id='field', ctx=Load()),
                                                            Name(id='env', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=Compare(
                                                        left=Name(id='f_name', ctx=Load()),
                                                        ops=[In()],
                                                        comparators=[
                                                            Attribute(
                                                                value=Name(id='model', ctx=Load()),
                                                                attr='_fields',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='field_type', ctx=Store())],
                                                            value=Attribute(
                                                                value=Subscript(
                                                                    value=Attribute(
                                                                        value=Name(id='model', ctx=Load()),
                                                                        attr='_fields',
                                                                        ctx=Load(),
                                                                    ),
                                                                    slice=Name(id='f_name', ctx=Load()),
                                                                    ctx=Load(),
                                                                ),
                                                                attr='type',
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        If(
                                                            test=Compare(
                                                                left=Name(id='field_type', ctx=Load()),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='many2one', kind=None)],
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='f_val', ctx=Store())],
                                                                    value=IfExp(
                                                                        test=Name(id='f_val', ctx=Load()),
                                                                        body=Call(
                                                                            func=Name(id='int', ctx=Load()),
                                                                            args=[Name(id='f_val', ctx=Load())],
                                                                            keywords=[],
                                                                        ),
                                                                        orelse=Constant(value=False, kind=None),
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                            orelse=[
                                                                If(
                                                                    test=Compare(
                                                                        left=Name(id='field_type', ctx=Load()),
                                                                        ops=[Eq()],
                                                                        comparators=[Constant(value='integer', kind=None)],
                                                                    ),
                                                                    body=[
                                                                        Assign(
                                                                            targets=[Name(id='f_val', ctx=Store())],
                                                                            value=Call(
                                                                                func=Name(id='int', ctx=Load()),
                                                                                args=[Name(id='f_val', ctx=Load())],
                                                                                keywords=[],
                                                                            ),
                                                                            type_comment=None,
                                                                        ),
                                                                    ],
                                                                    orelse=[
                                                                        If(
                                                                            test=Compare(
                                                                                left=Name(id='field_type', ctx=Load()),
                                                                                ops=[In()],
                                                                                comparators=[
                                                                                    Tuple(
                                                                                        elts=[
                                                                                            Constant(value='float', kind=None),
                                                                                            Constant(value='monetary', kind=None),
                                                                                        ],
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                            ),
                                                                            body=[
                                                                                Assign(
                                                                                    targets=[Name(id='f_val', ctx=Store())],
                                                                                    value=Call(
                                                                                        func=Name(id='float', ctx=Load()),
                                                                                        args=[Name(id='f_val', ctx=Load())],
                                                                                        keywords=[],
                                                                                    ),
                                                                                    type_comment=None,
                                                                                ),
                                                                            ],
                                                                            orelse=[
                                                                                If(
                                                                                    test=BoolOp(
                                                                                        op=And(),
                                                                                        values=[
                                                                                            Compare(
                                                                                                left=Name(id='field_type', ctx=Load()),
                                                                                                ops=[Eq()],
                                                                                                comparators=[Constant(value='boolean', kind=None)],
                                                                                            ),
                                                                                            Call(
                                                                                                func=Name(id='isinstance', ctx=Load()),
                                                                                                args=[
                                                                                                    Name(id='f_val', ctx=Load()),
                                                                                                    Name(id='str', ctx=Load()),
                                                                                                ],
                                                                                                keywords=[],
                                                                                            ),
                                                                                        ],
                                                                                    ),
                                                                                    body=[
                                                                                        Assign(
                                                                                            targets=[Name(id='f_val', ctx=Store())],
                                                                                            value=Call(
                                                                                                func=Name(id='str2bool', ctx=Load()),
                                                                                                args=[Name(id='f_val', ctx=Load())],
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
                                                            ],
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='res', ctx=Load()),
                                            slice=Name(id='f_name', ctx=Load()),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='f_val', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='data', ctx=Store())],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='xml_id',
                                        value=Name(id='xid', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='values',
                                        value=Name(id='res', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='noupdate',
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='noupdate',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='record', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='model', ctx=Load()),
                                    attr='_load_records',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Name(id='data', ctx=Load())],
                                        ctx=Load(),
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='mode',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='update', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='rec_id', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='idref',
                                                ctx=Load(),
                                            ),
                                            slice=Name(id='rec_id', ctx=Load()),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='record', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='config', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='import_partial', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='env', ctx=Load()),
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
                            orelse=[],
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Name(id='rec_model', ctx=Load()),
                                    Attribute(
                                        value=Name(id='record', ctx=Load()),
                                        attr='id',
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
                FunctionDef(
                    name='_tag_template',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='el', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='tpl_id', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='el', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='id', kind=None),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='el', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='t-name', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='full_tpl_id', ctx=Store())],
                            value=Name(id='tpl_id', ctx=Load()),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Constant(value='.', kind=None),
                                ops=[NotIn()],
                                comparators=[Name(id='full_tpl_id', ctx=Load())],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='full_tpl_id', ctx=Store())],
                                    value=BinOp(
                                        left=Constant(value='%s.%s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='module',
                                                    ctx=Load(),
                                                ),
                                                Name(id='tpl_id', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Name(id='el', ctx=Load()),
                                        attr='get',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='inherit_id', kind=None)],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='el', ctx=Load()),
                                            attr='set',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='t-name', kind=None),
                                            Name(id='full_tpl_id', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='el', ctx=Load()),
                                            attr='tag',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value='t', kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='el', ctx=Load()),
                                            attr='tag',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value='data', kind=None),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='el', ctx=Load()),
                                        attr='attrib',
                                        ctx=Load(),
                                    ),
                                    attr='pop',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='id', kind=None),
                                    Constant(value=None, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='module',
                                        ctx=Load(),
                                    ),
                                    attr='startswith',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='theme_', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='model', ctx=Store())],
                                    value=Constant(value='theme.ir.ui.view', kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='model', ctx=Store())],
                                    value=Constant(value='ir.ui.view', kind=None),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='record_attrs', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='id', kind=None),
                                    Constant(value='model', kind=None),
                                ],
                                values=[
                                    Name(id='tpl_id', ctx=Load()),
                                    Name(id='model', ctx=Load()),
                                ],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='att', ctx=Store()),
                            iter=List(
                                elts=[
                                    Constant(value='forcecreate', kind=None),
                                    Constant(value='context', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Name(id='att', ctx=Load()),
                                        ops=[In()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='el', ctx=Load()),
                                                attr='attrib',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='record_attrs', ctx=Load()),
                                                    slice=Name(id='att', ctx=Load()),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='el', ctx=Load()),
                                                        attr='attrib',
                                                        ctx=Load(),
                                                    ),
                                                    attr='pop',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='att', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='Field', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='builder', ctx=Load()),
                                    attr='E',
                                    ctx=Load(),
                                ),
                                attr='field',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='name', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='el', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='name', kind=None),
                                    Name(id='tpl_id', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='record', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='etree', ctx=Load()),
                                    attr='Element',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='record', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='attrib',
                                        value=Name(id='record_attrs', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='record', ctx=Load()),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='Field', ctx=Load()),
                                        args=[Name(id='name', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='name',
                                                value=Constant(value='name', kind=None),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='record', ctx=Load()),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='Field', ctx=Load()),
                                        args=[Name(id='full_tpl_id', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='name',
                                                value=Constant(value='key', kind=None),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='record', ctx=Load()),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='Field', ctx=Load()),
                                        args=[Constant(value='qweb', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='name',
                                                value=Constant(value='type', kind=None),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Compare(
                                left=Constant(value='track', kind=None),
                                ops=[In()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='el', ctx=Load()),
                                        attr='attrib',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='Field', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='el', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='track', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='name',
                                                        value=Constant(value='track', kind=None),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Constant(value='priority', kind=None),
                                ops=[In()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='el', ctx=Load()),
                                        attr='attrib',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='Field', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='el', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='priority', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='name',
                                                        value=Constant(value='priority', kind=None),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Constant(value='inherit_id', kind=None),
                                ops=[In()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='el', ctx=Load()),
                                        attr='attrib',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='Field', ctx=Load()),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='name',
                                                        value=Constant(value='inherit_id', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='ref',
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Name(id='el', ctx=Load()),
                                                                attr='get',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='inherit_id', kind=None)],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Constant(value='website_id', kind=None),
                                ops=[In()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='el', ctx=Load()),
                                        attr='attrib',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='Field', ctx=Load()),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='name',
                                                        value=Constant(value='website_id', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='ref',
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Name(id='el', ctx=Load()),
                                                                attr='get',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='website_id', kind=None)],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Constant(value='key', kind=None),
                                ops=[In()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='el', ctx=Load()),
                                        attr='attrib',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='Field', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='el', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='key', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='name',
                                                        value=Constant(value='key', kind=None),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Call(
                                    func=Attribute(
                                        value=Name(id='el', ctx=Load()),
                                        attr='get',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='active', kind=None)],
                                    keywords=[],
                                ),
                                ops=[In()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value='True', kind=None),
                                            Constant(value='False', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='view_id', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='id_get',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='tpl_id', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='raise_if_not_found',
                                                value=Constant(value=False, kind=None),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=Or(),
                                        values=[
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='mode',
                                                    ctx=Load(),
                                                ),
                                                ops=[NotEq()],
                                                comparators=[Constant(value='update', kind=None)],
                                            ),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Name(id='view_id', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='record', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Name(id='Field', ctx=Load()),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='name',
                                                                value=Constant(value='active', kind=None),
                                                            ),
                                                            keyword(
                                                                arg='eval',
                                                                value=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='el', ctx=Load()),
                                                                        attr='get',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[Constant(value='active', kind=None)],
                                                                    keywords=[],
                                                                ),
                                                            ),
                                                        ],
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
                        If(
                            test=Compare(
                                left=Call(
                                    func=Attribute(
                                        value=Name(id='el', ctx=Load()),
                                        attr='get',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='customize_show', kind=None)],
                                    keywords=[],
                                ),
                                ops=[In()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value='True', kind=None),
                                            Constant(value='False', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='Field', ctx=Load()),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='name',
                                                        value=Constant(value='customize_show', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='eval',
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Name(id='el', ctx=Load()),
                                                                attr='get',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='customize_show', kind=None)],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='groups', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='el', ctx=Load()),
                                        attr='attrib',
                                        ctx=Load(),
                                    ),
                                    attr='pop',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='groups', kind=None),
                                    Constant(value=None, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='groups', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='grp_lst', ctx=Store())],
                                    value=ListComp(
                                        elt=BinOp(
                                            left=Constant(value="ref('%s')", kind=None),
                                            op=Mod(),
                                            right=Name(id='x', ctx=Load()),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='x', ctx=Store()),
                                                iter=Call(
                                                    func=Attribute(
                                                        value=Name(id='groups', ctx=Load()),
                                                        attr='split',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value=',', kind=None)],
                                                    keywords=[],
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
                                            value=Name(id='record', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='Field', ctx=Load()),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='name',
                                                        value=Constant(value='groups_id', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='eval',
                                                        value=BinOp(
                                                            left=BinOp(
                                                                left=Constant(value='[Command.set([', kind=None),
                                                                op=Add(),
                                                                right=Call(
                                                                    func=Attribute(
                                                                        value=Constant(value=', ', kind=None),
                                                                        attr='join',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[Name(id='grp_lst', ctx=Load())],
                                                                    keywords=[],
                                                                ),
                                                            ),
                                                            op=Add(),
                                                            right=Constant(value='])]', kind=None),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Call(
                                    func=Attribute(
                                        value=Name(id='el', ctx=Load()),
                                        attr='get',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='primary', kind=None)],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='True', kind=None)],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='el', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='builder', ctx=Load()),
                                                        attr='E',
                                                        ctx=Load(),
                                                    ),
                                                    attr='xpath',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='builder', ctx=Load()),
                                                                attr='E',
                                                                ctx=Load(),
                                                            ),
                                                            attr='attribute',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='full_tpl_id', ctx=Load())],
                                                        keywords=[
                                                            keyword(
                                                                arg='name',
                                                                value=Constant(value='t-name', kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='expr',
                                                        value=Constant(value='.', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='position',
                                                        value=Constant(value='attributes', kind=None),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='Field', ctx=Load()),
                                                args=[Constant(value='primary', kind=None)],
                                                keywords=[
                                                    keyword(
                                                        arg='name',
                                                        value=Constant(value='mode', kind=None),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='record', ctx=Load()),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='Field', ctx=Load()),
                                        args=[Name(id='el', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='name',
                                                value=Constant(value='arch', kind=None),
                                            ),
                                            keyword(
                                                arg='type',
                                                value=Constant(value='xml', kind=None),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_tag_record',
                                    ctx=Load(),
                                ),
                                args=[Name(id='record', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='id_get',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='id_str', annotation=None, type_comment=None),
                            arg(arg='raise_if_not_found', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=True, kind=None)],
                    ),
                    body=[
                        If(
                            test=Compare(
                                left=Name(id='id_str', ctx=Load()),
                                ops=[In()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='idref',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='idref',
                                            ctx=Load(),
                                        ),
                                        slice=Name(id='id_str', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='model_id_get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='id_str', ctx=Load()),
                                    Name(id='raise_if_not_found', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='res', ctx=Load()),
                                    Subscript(
                                        value=Name(id='res', ctx=Load()),
                                        slice=Constant(value=1, kind=None),
                                        ctx=Load(),
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
                    name='model_id_get',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='id_str', annotation=None, type_comment=None),
                            arg(arg='raise_if_not_found', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=True, kind=None)],
                    ),
                    body=[
                        If(
                            test=Compare(
                                left=Constant(value='.', kind=None),
                                ops=[NotIn()],
                                comparators=[Name(id='id_str', ctx=Load())],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='id_str', ctx=Store())],
                                    value=BinOp(
                                        left=Constant(value='%s.%s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='module',
                                                    ctx=Load(),
                                                ),
                                                Name(id='id_str', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.model.data', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_xmlid_to_res_model_res_id',
                                    ctx=Load(),
                                ),
                                args=[Name(id='id_str', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='raise_if_not_found',
                                        value=Name(id='raise_if_not_found', ctx=Load()),
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
                    name='_tag_root',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='el', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        For(
                            target=Name(id='rec', ctx=Store()),
                            iter=Name(id='el', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='f', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_tags',
                                                ctx=Load(),
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='rec', ctx=Load()),
                                                attr='tag',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='f', ctx=Load()),
                                        ops=[Is()],
                                        comparators=[Constant(value=None, kind=None)],
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='envs',
                                                ctx=Load(),
                                            ),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='get_env',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='el', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_noupdate',
                                                ctx=Load(),
                                            ),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='nodeattr2bool', ctx=Load()),
                                                args=[
                                                    Name(id='el', ctx=Load()),
                                                    Constant(value='noupdate', kind=None),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='noupdate',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Try(
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Name(id='f', ctx=Load()),
                                                args=[Name(id='rec', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='ParseError', ctx=Load()),
                                            name=None,
                                            body=[Raise(exc=None, cause=None)],
                                        ),
                                        ExceptHandler(
                                            type=Name(id='ValidationError', ctx=Load()),
                                            name='err',
                                            body=[
                                                Assign(
                                                    targets=[Name(id='msg', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Constant(value='while parsing {file}:{viewline}\n{err}\n\nView error context:\n{context}\n', kind=None),
                                                            attr='format',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='file',
                                                                value=Attribute(
                                                                    value=Attribute(
                                                                        value=Call(
                                                                            func=Attribute(
                                                                                value=Name(id='rec', ctx=Load()),
                                                                                attr='getroottree',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[],
                                                                            keywords=[],
                                                                        ),
                                                                        attr='docinfo',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='URL',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            keyword(
                                                                arg='viewline',
                                                                value=Attribute(
                                                                    value=Name(id='rec', ctx=Load()),
                                                                    attr='sourceline',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            keyword(
                                                                arg='context',
                                                                value=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='pprint', ctx=Load()),
                                                                        attr='pformat',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[
                                                                        BoolOp(
                                                                            op=Or(),
                                                                            values=[
                                                                                Call(
                                                                                    func=Name(id='getattr', ctx=Load()),
                                                                                    args=[
                                                                                        Name(id='err', ctx=Load()),
                                                                                        Constant(value='context', kind=None),
                                                                                        Constant(value=None, kind=None),
                                                                                    ],
                                                                                    keywords=[],
                                                                                ),
                                                                                Constant(value='-no context-', kind=None),
                                                                            ],
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                            ),
                                                            keyword(
                                                                arg='err',
                                                                value=Subscript(
                                                                    value=Attribute(
                                                                        value=Name(id='err', ctx=Load()),
                                                                        attr='args',
                                                                        ctx=Load(),
                                                                    ),
                                                                    slice=Constant(value=0, kind=None),
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
                                                            value=Name(id='_logger', ctx=Load()),
                                                            attr='debug',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='msg', ctx=Load())],
                                                        keywords=[
                                                            keyword(
                                                                arg='exc_info',
                                                                value=Constant(value=True, kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                ),
                                                Raise(
                                                    exc=Call(
                                                        func=Name(id='ParseError', ctx=Load()),
                                                        args=[Name(id='msg', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    cause=Constant(value=None, kind=None),
                                                ),
                                            ],
                                        ),
                                        ExceptHandler(
                                            type=Name(id='Exception', ctx=Load()),
                                            name='e',
                                            body=[
                                                Raise(
                                                    exc=Call(
                                                        func=Name(id='ParseError', ctx=Load()),
                                                        args=[
                                                            BinOp(
                                                                left=Constant(value='while parsing %s:%s, somewhere inside\n%s', kind=None),
                                                                op=Mod(),
                                                                right=Tuple(
                                                                    elts=[
                                                                        Attribute(
                                                                            value=Attribute(
                                                                                value=Call(
                                                                                    func=Attribute(
                                                                                        value=Name(id='rec', ctx=Load()),
                                                                                        attr='getroottree',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    args=[],
                                                                                    keywords=[],
                                                                                ),
                                                                                attr='docinfo',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='URL',
                                                                            ctx=Load(),
                                                                        ),
                                                                        Attribute(
                                                                            value=Name(id='rec', ctx=Load()),
                                                                            attr='sourceline',
                                                                            ctx=Load(),
                                                                        ),
                                                                        Call(
                                                                            func=Attribute(
                                                                                value=Call(
                                                                                    func=Attribute(
                                                                                        value=Name(id='etree', ctx=Load()),
                                                                                        attr='tostring',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    args=[Name(id='rec', ctx=Load())],
                                                                                    keywords=[
                                                                                        keyword(
                                                                                            arg='encoding',
                                                                                            value=Constant(value='unicode', kind=None),
                                                                                        ),
                                                                                    ],
                                                                                ),
                                                                                attr='rstrip',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[],
                                                                            keywords=[],
                                                                        ),
                                                                    ],
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    cause=Name(id='e', ctx=Load()),
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                    finalbody=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_noupdate',
                                                        ctx=Load(),
                                                    ),
                                                    attr='pop',
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
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='envs',
                                                        ctx=Load(),
                                                    ),
                                                    attr='pop',
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
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='env',
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
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='envs',
                                    ctx=Load(),
                                ),
                                slice=UnaryOp(
                                    op=USub(),
                                    operand=Constant(value=1, kind=None),
                                ),
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='property', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='noupdate',
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
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_noupdate',
                                    ctx=Load(),
                                ),
                                slice=UnaryOp(
                                    op=USub(),
                                    operand=Constant(value=1, kind=None),
                                ),
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='property', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='cr', annotation=None, type_comment=None),
                            arg(arg='module', annotation=None, type_comment=None),
                            arg(arg='idref', annotation=None, type_comment=None),
                            arg(arg='mode', annotation=None, type_comment=None),
                            arg(arg='noupdate', annotation=None, type_comment=None),
                            arg(arg='xml_filename', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=False, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
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
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='module',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='module', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='envs',
                                    ctx=Store(),
                                ),
                            ],
                            value=List(
                                elts=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='odoo', ctx=Load()),
                                                attr='api',
                                                ctx=Load(),
                                            ),
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
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='idref',
                                    ctx=Store(),
                                ),
                            ],
                            value=IfExp(
                                test=Compare(
                                    left=Name(id='idref', ctx=Load()),
                                    ops=[Is()],
                                    comparators=[Constant(value=None, kind=None)],
                                ),
                                body=Dict(keys=[], values=[]),
                                orelse=Name(id='idref', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_noupdate',
                                    ctx=Store(),
                                ),
                            ],
                            value=List(
                                elts=[Name(id='noupdate', ctx=Load())],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='xml_filename',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='xml_filename', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_tags',
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(
                                keys=[
                                    Constant(value='record', kind=None),
                                    Constant(value='delete', kind=None),
                                    Constant(value='function', kind=None),
                                    Constant(value='menuitem', kind=None),
                                    Constant(value='template', kind=None),
                                    Constant(value='report', kind=None),
                                    Constant(value='act_window', kind=None),
                                    None,
                                ],
                                values=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_tag_record',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_tag_delete',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_tag_function',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_tag_menuitem',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_tag_template',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_tag_report',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_tag_act_window',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='dict', ctx=Load()),
                                            attr='fromkeys',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='DATA_ROOTS',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_tag_root',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='parse',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='de', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assert(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='de', ctx=Load()),
                                    attr='tag',
                                    ctx=Load(),
                                ),
                                ops=[In()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='DATA_ROOTS',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            msg=Constant(value='Root xml tag must be <openerp>, <odoo> or <data>.', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_tag_root',
                                    ctx=Load(),
                                ),
                                args=[Name(id='de', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='DATA_ROOTS', ctx=Store())],
                    value=List(
                        elts=[
                            Constant(value='odoo', kind=None),
                            Constant(value='data', kind=None),
                            Constant(value='openerp', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        FunctionDef(
            name='convert_file',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='cr', annotation=None, type_comment=None),
                    arg(arg='module', annotation=None, type_comment=None),
                    arg(arg='filename', annotation=None, type_comment=None),
                    arg(arg='idref', annotation=None, type_comment=None),
                    arg(arg='mode', annotation=None, type_comment=None),
                    arg(arg='noupdate', annotation=None, type_comment=None),
                    arg(arg='kind', annotation=None, type_comment=None),
                    arg(arg='pathname', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    Constant(value='update', kind=None),
                    Constant(value=False, kind=None),
                    Constant(value=None, kind=None),
                    Constant(value=None, kind=None),
                ],
            ),
            body=[
                If(
                    test=Compare(
                        left=Name(id='pathname', ctx=Load()),
                        ops=[Is()],
                        comparators=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='pathname', ctx=Store())],
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
                                    Name(id='module', ctx=Load()),
                                    Name(id='filename', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    targets=[Name(id='ext', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Subscript(
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
                                    args=[Name(id='filename', ctx=Load())],
                                    keywords=[],
                                ),
                                slice=Constant(value=1, kind=None),
                                ctx=Load(),
                            ),
                            attr='lower',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                With(
                    items=[
                        withitem(
                            context_expr=Call(
                                func=Name(id='file_open', ctx=Load()),
                                args=[
                                    Name(id='pathname', ctx=Load()),
                                    Constant(value='rb', kind=None),
                                ],
                                keywords=[],
                            ),
                            optional_vars=Name(id='fp', ctx=Store()),
                        ),
                    ],
                    body=[
                        If(
                            test=Compare(
                                left=Name(id='ext', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='.csv', kind=None)],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='convert_csv_import', ctx=Load()),
                                        args=[
                                            Name(id='cr', ctx=Load()),
                                            Name(id='module', ctx=Load()),
                                            Name(id='pathname', ctx=Load()),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='fp', ctx=Load()),
                                                    attr='read',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            Name(id='idref', ctx=Load()),
                                            Name(id='mode', ctx=Load()),
                                            Name(id='noupdate', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Name(id='ext', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='.sql', kind=None)],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Name(id='convert_sql_import', ctx=Load()),
                                                args=[
                                                    Name(id='cr', ctx=Load()),
                                                    Name(id='fp', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Name(id='ext', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='.xml', kind=None)],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Name(id='convert_xml_import', ctx=Load()),
                                                        args=[
                                                            Name(id='cr', ctx=Load()),
                                                            Name(id='module', ctx=Load()),
                                                            Name(id='fp', ctx=Load()),
                                                            Name(id='idref', ctx=Load()),
                                                            Name(id='mode', ctx=Load()),
                                                            Name(id='noupdate', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Compare(
                                                        left=Name(id='ext', ctx=Load()),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='.js', kind=None)],
                                                    ),
                                                    body=[Pass()],
                                                    orelse=[
                                                        Raise(
                                                            exc=Call(
                                                                func=Name(id='ValueError', ctx=Load()),
                                                                args=[
                                                                    Constant(value="Can't load unknown file type %s.", kind=None),
                                                                    Name(id='filename', ctx=Load()),
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
                    type_comment=None,
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='convert_sql_import',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='cr', annotation=None, type_comment=None),
                    arg(arg='fp', annotation=None, type_comment=None),
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
                            value=Name(id='cr', ctx=Load()),
                            attr='execute',
                            ctx=Load(),
                        ),
                        args=[
                            Call(
                                func=Attribute(
                                    value=Name(id='fp', ctx=Load()),
                                    attr='read',
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
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='convert_csv_import',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='cr', annotation=None, type_comment=None),
                    arg(arg='module', annotation=None, type_comment=None),
                    arg(arg='fname', annotation=None, type_comment=None),
                    arg(arg='csvcontent', annotation=None, type_comment=None),
                    arg(arg='idref', annotation=None, type_comment=None),
                    arg(arg='mode', annotation=None, type_comment=None),
                    arg(arg='noupdate', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    Constant(value=None, kind=None),
                    Constant(value='init', kind=None),
                    Constant(value=False, kind=None),
                ],
            ),
            body=[
                Expr(
                    value=Constant(value='Import csv file :\n        quote: "\n        delimiter: ,\n        encoding: utf-8', kind=None),
                ),
                Assign(
                    targets=[
                        Tuple(
                            elts=[
                                Name(id='filename', ctx=Store()),
                                Name(id='_ext', ctx=Store()),
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
                        args=[
                            Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='os', ctx=Load()),
                                        attr='path',
                                        ctx=Load(),
                                    ),
                                    attr='basename',
                                    ctx=Load(),
                                ),
                                args=[Name(id='fname', ctx=Load())],
                                keywords=[],
                            ),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='model', ctx=Store())],
                    value=Subscript(
                        value=Call(
                            func=Attribute(
                                value=Name(id='filename', ctx=Load()),
                                attr='split',
                                ctx=Load(),
                            ),
                            args=[Constant(value='-', kind=None)],
                            keywords=[],
                        ),
                        slice=Constant(value=0, kind=None),
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='reader', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='pycompat', ctx=Load()),
                            attr='csv_reader',
                            ctx=Load(),
                        ),
                        args=[
                            Call(
                                func=Attribute(
                                    value=Name(id='io', ctx=Load()),
                                    attr='BytesIO',
                                    ctx=Load(),
                                ),
                                args=[Name(id='csvcontent', ctx=Load())],
                                keywords=[],
                            ),
                        ],
                        keywords=[
                            keyword(
                                arg='quotechar',
                                value=Constant(value='"', kind=None),
                            ),
                            keyword(
                                arg='delimiter',
                                value=Constant(value=',', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='fields', ctx=Store())],
                    value=Call(
                        func=Name(id='next', ctx=Load()),
                        args=[Name(id='reader', ctx=Load())],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=UnaryOp(
                        op=Not(),
                        operand=BoolOp(
                            op=Or(),
                            values=[
                                Compare(
                                    left=Name(id='mode', ctx=Load()),
                                    ops=[Eq()],
                                    comparators=[Constant(value='init', kind=None)],
                                ),
                                Compare(
                                    left=Constant(value='id', kind=None),
                                    ops=[In()],
                                    comparators=[Name(id='fields', ctx=Load())],
                                ),
                            ],
                        ),
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='error',
                                    ctx=Load(),
                                ),
                                args=[Constant(value="Import specification does not contain 'id' and we are in init mode, Cannot continue.", kind=None)],
                                keywords=[],
                            ),
                        ),
                        Return(value=None),
                    ],
                    orelse=[],
                ),
                Assign(
                    targets=[Name(id='datas', ctx=Store())],
                    value=ListComp(
                        elt=Name(id='line', ctx=Load()),
                        generators=[
                            comprehension(
                                target=Name(id='line', ctx=Store()),
                                iter=Name(id='reader', ctx=Load()),
                                ifs=[
                                    Call(
                                        func=Name(id='any', ctx=Load()),
                                        args=[Name(id='line', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                is_async=0,
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='context', ctx=Store())],
                    value=Dict(
                        keys=[
                            Constant(value='mode', kind=None),
                            Constant(value='module', kind=None),
                            Constant(value='install_module', kind=None),
                            Constant(value='install_filename', kind=None),
                            Constant(value='noupdate', kind=None),
                        ],
                        values=[
                            Name(id='mode', ctx=Load()),
                            Name(id='module', ctx=Load()),
                            Name(id='module', ctx=Load()),
                            Name(id='fname', ctx=Load()),
                            Name(id='noupdate', ctx=Load()),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='env', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Attribute(
                                value=Name(id='odoo', ctx=Load()),
                                attr='api',
                                ctx=Load(),
                            ),
                            attr='Environment',
                            ctx=Load(),
                        ),
                        args=[
                            Name(id='cr', ctx=Load()),
                            Name(id='SUPERUSER_ID', ctx=Load()),
                            Name(id='context', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='result', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Subscript(
                                value=Name(id='env', ctx=Load()),
                                slice=Name(id='model', ctx=Load()),
                                ctx=Load(),
                            ),
                            attr='load',
                            ctx=Load(),
                        ),
                        args=[
                            Name(id='fields', ctx=Load()),
                            Name(id='datas', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=Call(
                        func=Name(id='any', ctx=Load()),
                        args=[
                            GeneratorExp(
                                elt=Compare(
                                    left=Subscript(
                                        value=Name(id='msg', ctx=Load()),
                                        slice=Constant(value='type', kind=None),
                                        ctx=Load(),
                                    ),
                                    ops=[Eq()],
                                    comparators=[Constant(value='error', kind=None)],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='msg', ctx=Store()),
                                        iter=Subscript(
                                            value=Name(id='result', ctx=Load()),
                                            slice=Constant(value='messages', kind=None),
                                            ctx=Load(),
                                        ),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                        ],
                        keywords=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='warning_msg', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Constant(value='\n', kind=None),
                                    attr='join',
                                    ctx=Load(),
                                ),
                                args=[
                                    GeneratorExp(
                                        elt=Subscript(
                                            value=Name(id='msg', ctx=Load()),
                                            slice=Constant(value='message', kind=None),
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='msg', ctx=Store()),
                                                iter=Subscript(
                                                    value=Name(id='result', ctx=Load()),
                                                    slice=Constant(value='messages', kind=None),
                                                    ctx=Load(),
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
                        Raise(
                            exc=Call(
                                func=Name(id='Exception', ctx=Load()),
                                args=[
                                    BinOp(
                                        left=Call(
                                            func=Name(id='_', ctx=Load()),
                                            args=[Constant(value='Module loading %s failed: file %s could not be processed:\n %s', kind=None)],
                                            keywords=[],
                                        ),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Name(id='module', ctx=Load()),
                                                Name(id='fname', ctx=Load()),
                                                Name(id='warning_msg', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            cause=None,
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
            name='convert_xml_import',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='cr', annotation=None, type_comment=None),
                    arg(arg='module', annotation=None, type_comment=None),
                    arg(arg='xmlfile', annotation=None, type_comment=None),
                    arg(arg='idref', annotation=None, type_comment=None),
                    arg(arg='mode', annotation=None, type_comment=None),
                    arg(arg='noupdate', annotation=None, type_comment=None),
                    arg(arg='report', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    Constant(value=None, kind=None),
                    Constant(value='init', kind=None),
                    Constant(value=False, kind=None),
                    Constant(value=None, kind=None),
                ],
            ),
            body=[
                Assign(
                    targets=[Name(id='doc', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='etree', ctx=Load()),
                            attr='parse',
                            ctx=Load(),
                        ),
                        args=[Name(id='xmlfile', ctx=Load())],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='schema', ctx=Store())],
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
                            Subscript(
                                value=Name(id='config', ctx=Load()),
                                slice=Constant(value='root_path', kind=None),
                                ctx=Load(),
                            ),
                            Constant(value='import_xml.rng', kind=None),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='relaxng', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='etree', ctx=Load()),
                            attr='RelaxNG',
                            ctx=Load(),
                        ),
                        args=[
                            Call(
                                func=Attribute(
                                    value=Name(id='etree', ctx=Load()),
                                    attr='parse',
                                    ctx=Load(),
                                ),
                                args=[Name(id='schema', ctx=Load())],
                                keywords=[],
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
                                    value=Name(id='relaxng', ctx=Load()),
                                    attr='assert_',
                                    ctx=Load(),
                                ),
                                args=[Name(id='doc', ctx=Load())],
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
                                            Constant(value="The XML file '%s' does not fit the required schema !", kind=None),
                                            Attribute(
                                                value=Name(id='xmlfile', ctx=Load()),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                If(
                                    test=Name(id='jingtrang', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='p', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='subprocess', ctx=Load()),
                                                    attr='run',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Constant(value='pyjing', kind=None),
                                                            Name(id='schema', ctx=Load()),
                                                            Attribute(
                                                                value=Name(id='xmlfile', ctx=Load()),
                                                                attr='name',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='stdout',
                                                        value=Attribute(
                                                            value=Name(id='subprocess', ctx=Load()),
                                                            attr='PIPE',
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
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='warning',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='p', ctx=Load()),
                                                                attr='stdout',
                                                                ctx=Load(),
                                                            ),
                                                            attr='decode',
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
                                    orelse=[
                                        For(
                                            target=Name(id='e', ctx=Store()),
                                            iter=Attribute(
                                                value=Name(id='relaxng', ctx=Load()),
                                                attr='error_log',
                                                ctx=Load(),
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='_logger', ctx=Load()),
                                                            attr='warning',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='e', ctx=Load())],
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
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='info',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value="Install 'jingtrang' for more precise and useful validation messages.", kind=None)],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                ),
                                Raise(exc=None, cause=None),
                            ],
                        ),
                    ],
                    orelse=[],
                    finalbody=[],
                ),
                If(
                    test=Call(
                        func=Name(id='isinstance', ctx=Load()),
                        args=[
                            Name(id='xmlfile', ctx=Load()),
                            Name(id='str', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='xml_filename', ctx=Store())],
                            value=Name(id='xmlfile', ctx=Load()),
                            type_comment=None,
                        ),
                    ],
                    orelse=[
                        Assign(
                            targets=[Name(id='xml_filename', ctx=Store())],
                            value=Attribute(
                                value=Name(id='xmlfile', ctx=Load()),
                                attr='name',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                    ],
                ),
                Assign(
                    targets=[Name(id='obj', ctx=Store())],
                    value=Call(
                        func=Name(id='xml_import', ctx=Load()),
                        args=[
                            Name(id='cr', ctx=Load()),
                            Name(id='module', ctx=Load()),
                            Name(id='idref', ctx=Load()),
                            Name(id='mode', ctx=Load()),
                        ],
                        keywords=[
                            keyword(
                                arg='noupdate',
                                value=Name(id='noupdate', ctx=Load()),
                            ),
                            keyword(
                                arg='xml_filename',
                                value=Name(id='xml_filename', ctx=Load()),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='obj', ctx=Load()),
                            attr='parse',
                            ctx=Load(),
                        ),
                        args=[
                            Call(
                                func=Attribute(
                                    value=Name(id='doc', ctx=Load()),
                                    attr='getroot',
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
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
    ],
    type_ignores=[],
)
