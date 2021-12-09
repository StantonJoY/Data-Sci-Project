Module(
    body=[
        ImportFrom(
            module='contextlib',
            names=[alias(name='closing', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='functools',
            names=[alias(name='wraps', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        ImportFrom(
            module='psycopg2',
            names=[
                alias(name='IntegrityError', asname=None),
                alias(name='OperationalError', asname=None),
                alias(name='errorcodes', asname=None),
            ],
            level=0,
        ),
        Import(
            names=[alias(name='random', asname=None)],
        ),
        Import(
            names=[alias(name='threading', asname=None)],
        ),
        Import(
            names=[alias(name='time', asname=None)],
        ),
        Import(
            names=[alias(name='odoo', asname=None)],
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[
                alias(name='UserError', asname=None),
                alias(name='ValidationError', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.models',
            names=[alias(name='check_method_name', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.translate',
            names=[
                alias(name='translate', asname=None),
                alias(name='translate_sql_constraint', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.translate',
            names=[alias(name='_', asname=None)],
            level=0,
        ),
        ImportFrom(
            module=None,
            names=[alias(name='security', asname=None)],
            level=1,
        ),
        ImportFrom(
            module='tools',
            names=[
                alias(name='traverse_containers', asname=None),
                alias(name='lazy', asname=None),
            ],
            level=2,
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
            targets=[Name(id='PG_CONCURRENCY_ERRORS_TO_RETRY', ctx=Store())],
            value=Tuple(
                elts=[
                    Attribute(
                        value=Name(id='errorcodes', ctx=Load()),
                        attr='LOCK_NOT_AVAILABLE',
                        ctx=Load(),
                    ),
                    Attribute(
                        value=Name(id='errorcodes', ctx=Load()),
                        attr='SERIALIZATION_FAILURE',
                        ctx=Load(),
                    ),
                    Attribute(
                        value=Name(id='errorcodes', ctx=Load()),
                        attr='DEADLOCK_DETECTED',
                        ctx=Load(),
                    ),
                ],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='MAX_TRIES_ON_CONCURRENCY_FAILURE', ctx=Store())],
            value=Constant(value=5, kind=None),
            type_comment=None,
        ),
        FunctionDef(
            name='dispatch',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='method', annotation=None, type_comment=None),
                    arg(arg='params', annotation=None, type_comment=None),
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
                                Name(id='db', ctx=Store()),
                                Name(id='uid', ctx=Store()),
                                Name(id='passwd', ctx=Store()),
                            ],
                            ctx=Store(),
                        ),
                    ],
                    value=Tuple(
                        elts=[
                            Subscript(
                                value=Name(id='params', ctx=Load()),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            Call(
                                func=Name(id='int', ctx=Load()),
                                args=[
                                    Subscript(
                                        value=Name(id='params', ctx=Load()),
                                        slice=Constant(value=1, kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            Subscript(
                                value=Name(id='params', ctx=Load()),
                                slice=Constant(value=2, kind=None),
                                ctx=Load(),
                            ),
                        ],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[
                        Attribute(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='threading', ctx=Load()),
                                    attr='current_thread',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            attr='uid',
                            ctx=Store(),
                        ),
                    ],
                    value=Name(id='uid', ctx=Load()),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='params', ctx=Store())],
                    value=Subscript(
                        value=Name(id='params', ctx=Load()),
                        slice=Slice(
                            lower=Constant(value=3, kind=None),
                            upper=None,
                            step=None,
                        ),
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                If(
                    test=Compare(
                        left=Name(id='method', ctx=Load()),
                        ops=[Eq()],
                        comparators=[Constant(value='obj_list', kind=None)],
                    ),
                    body=[
                        Raise(
                            exc=Call(
                                func=Name(id='NameError', ctx=Load()),
                                args=[Constant(value='obj_list has been discontinued via RPC as of 6.0, please query ir.model directly!', kind=None)],
                                keywords=[],
                            ),
                            cause=None,
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    test=Compare(
                        left=Name(id='method', ctx=Load()),
                        ops=[NotIn()],
                        comparators=[
                            List(
                                elts=[
                                    Constant(value='execute', kind=None),
                                    Constant(value='execute_kw', kind=None),
                                ],
                                ctx=Load(),
                            ),
                        ],
                    ),
                    body=[
                        Raise(
                            exc=Call(
                                func=Name(id='NameError', ctx=Load()),
                                args=[
                                    BinOp(
                                        left=Constant(value='Method not available %s', kind=None),
                                        op=Mod(),
                                        right=Name(id='method', ctx=Load()),
                                    ),
                                ],
                                keywords=[],
                            ),
                            cause=None,
                        ),
                    ],
                    orelse=[],
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='security', ctx=Load()),
                            attr='check',
                            ctx=Load(),
                        ),
                        args=[
                            Name(id='db', ctx=Load()),
                            Name(id='uid', ctx=Load()),
                            Name(id='passwd', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                ),
                Assign(
                    targets=[Name(id='registry', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='odoo', ctx=Load()),
                                    attr='registry',
                                    ctx=Load(),
                                ),
                                args=[Name(id='db', ctx=Load())],
                                keywords=[],
                            ),
                            attr='check_signaling',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='fn', ctx=Store())],
                    value=Subscript(
                        value=Call(
                            func=Name(id='globals', ctx=Load()),
                            args=[],
                            keywords=[],
                        ),
                        slice=Name(id='method', ctx=Load()),
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                With(
                    items=[
                        withitem(
                            context_expr=Call(
                                func=Attribute(
                                    value=Name(id='registry', ctx=Load()),
                                    attr='manage_changes',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            optional_vars=None,
                        ),
                    ],
                    body=[
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Name(id='fn', ctx=Load()),
                                args=[
                                    Name(id='db', ctx=Load()),
                                    Name(id='uid', ctx=Load()),
                                    Starred(
                                        value=Name(id='params', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
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
            name='check',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='f', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                FunctionDef(
                    name='wrapper',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='___dbname', annotation=None, type_comment=None)],
                        vararg=arg(arg='args', annotation=None, type_comment=None),
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Wraps around OSV functions and normalises a few exceptions\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='dbname', ctx=Store())],
                            value=Name(id='___dbname', ctx=Load()),
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='tr',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='src', annotation=None, type_comment=None),
                                    arg(arg='ttype', annotation=None, type_comment=None),
                                ],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='ctx', ctx=Store())],
                                    value=Dict(keys=[], values=[]),
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='kwargs', ctx=Load()),
                                    ),
                                    body=[
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Name(id='args', ctx=Load()),
                                                    Call(
                                                        func=Name(id='isinstance', ctx=Load()),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='args', ctx=Load()),
                                                                slice=UnaryOp(
                                                                    op=USub(),
                                                                    operand=Constant(value=1, kind=None),
                                                                ),
                                                                ctx=Load(),
                                                            ),
                                                            Name(id='dict', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='ctx', ctx=Store())],
                                                    value=Subscript(
                                                        value=Name(id='args', ctx=Load()),
                                                        slice=UnaryOp(
                                                            op=USub(),
                                                            operand=Constant(value=1, kind=None),
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Call(
                                                func=Name(id='isinstance', ctx=Load()),
                                                args=[
                                                    Name(id='kwargs', ctx=Load()),
                                                    Name(id='dict', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            body=[
                                                If(
                                                    test=Compare(
                                                        left=Constant(value='context', kind=None),
                                                        ops=[In()],
                                                        comparators=[Name(id='kwargs', ctx=Load())],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='ctx', ctx=Store())],
                                                            value=Subscript(
                                                                value=Name(id='kwargs', ctx=Load()),
                                                                slice=Constant(value='context', kind=None),
                                                                ctx=Load(),
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
                                                                        left=Constant(value='kwargs', kind=None),
                                                                        ops=[In()],
                                                                        comparators=[Name(id='kwargs', ctx=Load())],
                                                                    ),
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Subscript(
                                                                                value=Name(id='kwargs', ctx=Load()),
                                                                                slice=Constant(value='kwargs', kind=None),
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='get',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Constant(value='context', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='ctx', ctx=Store())],
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Subscript(
                                                                                value=Name(id='kwargs', ctx=Load()),
                                                                                slice=Constant(value='kwargs', kind=None),
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='get',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Constant(value='context', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                            orelse=[
                                                                Try(
                                                                    body=[
                                                                        ImportFrom(
                                                                            module='odoo.http',
                                                                            names=[alias(name='request', asname=None)],
                                                                            level=0,
                                                                        ),
                                                                        Assign(
                                                                            targets=[Name(id='ctx', ctx=Store())],
                                                                            value=Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='request', ctx=Load()),
                                                                                    attr='env',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='context',
                                                                                ctx=Load(),
                                                                            ),
                                                                            type_comment=None,
                                                                        ),
                                                                    ],
                                                                    handlers=[
                                                                        ExceptHandler(
                                                                            type=Name(id='Exception', ctx=Load()),
                                                                            name=None,
                                                                            body=[Pass()],
                                                                        ),
                                                                    ],
                                                                    orelse=[],
                                                                    finalbody=[],
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
                                Assign(
                                    targets=[Name(id='lang', ctx=Store())],
                                    value=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='ctx', ctx=Load()),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='ctx', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='lang', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=BoolOp(
                                            op=Or(),
                                            values=[
                                                Name(id='lang', ctx=Load()),
                                                Call(
                                                    func=Name(id='hasattr', ctx=Load()),
                                                    args=[
                                                        Name(id='src', ctx=Load()),
                                                        Constant(value='__call__', kind=None),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ],
                                        ),
                                    ),
                                    body=[
                                        Return(
                                            value=Name(id='src', ctx=Load()),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                func=Name(id='closing', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='odoo', ctx=Load()),
                                                                        attr='sql_db',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='db_connect',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='dbname', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                            attr='cursor',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            optional_vars=Name(id='cr', ctx=Store()),
                                        ),
                                    ],
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Name(id='ttype', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='sql_constraint', kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='res', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='translate_sql_constraint', ctx=Load()),
                                                        args=[Name(id='cr', ctx=Load())],
                                                        keywords=[
                                                            keyword(
                                                                arg='key',
                                                                value=Name(id='key', ctx=Load()),
                                                            ),
                                                            keyword(
                                                                arg='lang',
                                                                value=Name(id='lang', ctx=Load()),
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[Name(id='res', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='translate', ctx=Load()),
                                                        args=[Name(id='cr', ctx=Load())],
                                                        keywords=[
                                                            keyword(
                                                                arg='name',
                                                                value=Constant(value=False, kind=None),
                                                            ),
                                                            keyword(
                                                                arg='source_type',
                                                                value=Name(id='ttype', ctx=Load()),
                                                            ),
                                                            keyword(
                                                                arg='lang',
                                                                value=Name(id='lang', ctx=Load()),
                                                            ),
                                                            keyword(
                                                                arg='source',
                                                                value=Name(id='src', ctx=Load()),
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                        Return(
                                            value=BoolOp(
                                                op=Or(),
                                                values=[
                                                    Name(id='res', ctx=Load()),
                                                    Name(id='src', ctx=Load()),
                                                ],
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
                            name='_',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='src', annotation=None, type_comment=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Name(id='tr', ctx=Load()),
                                        args=[
                                            Name(id='src', ctx=Load()),
                                            Constant(value='code', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='tries', ctx=Store())],
                            value=Constant(value=0, kind=None),
                            type_comment=None,
                        ),
                        While(
                            test=Constant(value=True, kind=None),
                            body=[
                                Try(
                                    body=[
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Attribute(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Name(id='odoo', ctx=Load()),
                                                                attr='registry',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Name(id='dbname', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                        attr='_init',
                                                        ctx=Load(),
                                                    ),
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Subscript(
                                                            value=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='odoo', ctx=Load()),
                                                                    attr='tools',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='config',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='test_enable', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Raise(
                                                    exc=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='odoo', ctx=Load()),
                                                                attr='exceptions',
                                                                ctx=Load(),
                                                            ),
                                                            attr='Warning',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='Currently, this database is not fully loaded and can not be used.', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    cause=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Return(
                                            value=Call(
                                                func=Name(id='f', ctx=Load()),
                                                args=[
                                                    Name(id='dbname', ctx=Load()),
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
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='OperationalError', ctx=Load()),
                                            name='e',
                                            body=[
                                                If(
                                                    test=Compare(
                                                        left=Attribute(
                                                            value=Name(id='e', ctx=Load()),
                                                            attr='pgcode',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[NotIn()],
                                                        comparators=[Name(id='PG_CONCURRENCY_ERRORS_TO_RETRY', ctx=Load())],
                                                    ),
                                                    body=[Raise(exc=None, cause=None)],
                                                    orelse=[],
                                                ),
                                                If(
                                                    test=Compare(
                                                        left=Name(id='tries', ctx=Load()),
                                                        ops=[GtE()],
                                                        comparators=[Name(id='MAX_TRIES_ON_CONCURRENCY_FAILURE', ctx=Load())],
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='_logger', ctx=Load()),
                                                                    attr='info',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    BinOp(
                                                                        left=Constant(value='%s, maximum number of tries reached', kind=None),
                                                                        op=Mod(),
                                                                        right=Call(
                                                                            func=Attribute(
                                                                                value=Name(id='errorcodes', ctx=Load()),
                                                                                attr='lookup',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[
                                                                                Attribute(
                                                                                    value=Name(id='e', ctx=Load()),
                                                                                    attr='pgcode',
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ],
                                                                            keywords=[],
                                                                        ),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        Raise(exc=None, cause=None),
                                                    ],
                                                    orelse=[],
                                                ),
                                                Assign(
                                                    targets=[Name(id='wait_time', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='random', ctx=Load()),
                                                            attr='uniform',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value=0.0, kind=None),
                                                            BinOp(
                                                                left=Constant(value=2, kind=None),
                                                                op=Pow(),
                                                                right=Name(id='tries', ctx=Load()),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                AugAssign(
                                                    target=Name(id='tries', ctx=Store()),
                                                    op=Add(),
                                                    value=Constant(value=1, kind=None),
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
                                                                left=Constant(value='%s, retry %d/%d in %.04f sec...', kind=None),
                                                                op=Mod(),
                                                                right=Tuple(
                                                                    elts=[
                                                                        Call(
                                                                            func=Attribute(
                                                                                value=Name(id='errorcodes', ctx=Load()),
                                                                                attr='lookup',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[
                                                                                Attribute(
                                                                                    value=Name(id='e', ctx=Load()),
                                                                                    attr='pgcode',
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ],
                                                                            keywords=[],
                                                                        ),
                                                                        Name(id='tries', ctx=Load()),
                                                                        Name(id='MAX_TRIES_ON_CONCURRENCY_FAILURE', ctx=Load()),
                                                                        Name(id='wait_time', ctx=Load()),
                                                                    ],
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='time', ctx=Load()),
                                                            attr='sleep',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='wait_time', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                        ExceptHandler(
                                            type=Name(id='IntegrityError', ctx=Load()),
                                            name='inst',
                                            body=[
                                                Assign(
                                                    targets=[Name(id='registry', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='odoo', ctx=Load()),
                                                            attr='registry',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='dbname', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='key', ctx=Store())],
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='inst', ctx=Load()),
                                                            attr='diag',
                                                            ctx=Load(),
                                                        ),
                                                        attr='constraint_name',
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=Compare(
                                                        left=Name(id='key', ctx=Load()),
                                                        ops=[In()],
                                                        comparators=[
                                                            Attribute(
                                                                value=Name(id='registry', ctx=Load()),
                                                                attr='_sql_constraints',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Raise(
                                                            exc=Call(
                                                                func=Name(id='ValidationError', ctx=Load()),
                                                                args=[
                                                                    BoolOp(
                                                                        op=Or(),
                                                                        values=[
                                                                            Call(
                                                                                func=Name(id='tr', ctx=Load()),
                                                                                args=[
                                                                                    Name(id='key', ctx=Load()),
                                                                                    Constant(value='sql_constraint', kind=None),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                            Attribute(
                                                                                value=Name(id='inst', ctx=Load()),
                                                                                attr='pgerror',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            cause=None,
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                                If(
                                                    test=Compare(
                                                        left=Attribute(
                                                            value=Name(id='inst', ctx=Load()),
                                                            attr='pgcode',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[In()],
                                                        comparators=[
                                                            Tuple(
                                                                elts=[
                                                                    Attribute(
                                                                        value=Name(id='errorcodes', ctx=Load()),
                                                                        attr='NOT_NULL_VIOLATION',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Name(id='errorcodes', ctx=Load()),
                                                                        attr='FOREIGN_KEY_VIOLATION',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Name(id='errorcodes', ctx=Load()),
                                                                        attr='RESTRICT_VIOLATION',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='msg', ctx=Store())],
                                                            value=Call(
                                                                func=Name(id='_', ctx=Load()),
                                                                args=[Constant(value='The operation cannot be completed:', kind=None)],
                                                                keywords=[],
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
                                                                args=[Constant(value='IntegrityError', kind=None)],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='exc_info',
                                                                        value=Constant(value=True, kind=None),
                                                                    ),
                                                                ],
                                                            ),
                                                        ),
                                                        Try(
                                                            body=[
                                                                Assign(
                                                                    targets=[
                                                                        Name(id='model', ctx=Store()),
                                                                        Name(id='field', ctx=Store()),
                                                                    ],
                                                                    value=Constant(value=None, kind=None),
                                                                    type_comment=None,
                                                                ),
                                                                For(
                                                                    target=Tuple(
                                                                        elts=[
                                                                            Name(id='name', ctx=Store()),
                                                                            Name(id='rclass', ctx=Store()),
                                                                        ],
                                                                        ctx=Store(),
                                                                    ),
                                                                    iter=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='registry', ctx=Load()),
                                                                            attr='items',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[],
                                                                        keywords=[],
                                                                    ),
                                                                    body=[
                                                                        If(
                                                                            test=Compare(
                                                                                left=Attribute(
                                                                                    value=Attribute(
                                                                                        value=Name(id='inst', ctx=Load()),
                                                                                        attr='diag',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='table_name',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                ops=[Eq()],
                                                                                comparators=[
                                                                                    Attribute(
                                                                                        value=Name(id='rclass', ctx=Load()),
                                                                                        attr='_table',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                            ),
                                                                            body=[
                                                                                Assign(
                                                                                    targets=[Name(id='model', ctx=Store())],
                                                                                    value=Name(id='rclass', ctx=Load()),
                                                                                    type_comment=None,
                                                                                ),
                                                                                Assign(
                                                                                    targets=[Name(id='field', ctx=Store())],
                                                                                    value=Call(
                                                                                        func=Attribute(
                                                                                            value=Attribute(
                                                                                                value=Name(id='model', ctx=Load()),
                                                                                                attr='_fields',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            attr='get',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[
                                                                                            Attribute(
                                                                                                value=Attribute(
                                                                                                    value=Name(id='inst', ctx=Load()),
                                                                                                    attr='diag',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='column_name',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                        ],
                                                                                        keywords=[],
                                                                                    ),
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
                                                                    test=Compare(
                                                                        left=Attribute(
                                                                            value=Name(id='inst', ctx=Load()),
                                                                            attr='pgcode',
                                                                            ctx=Load(),
                                                                        ),
                                                                        ops=[Eq()],
                                                                        comparators=[
                                                                            Attribute(
                                                                                value=Name(id='errorcodes', ctx=Load()),
                                                                                attr='NOT_NULL_VIOLATION',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                    body=[
                                                                        AugAssign(
                                                                            target=Name(id='msg', ctx=Store()),
                                                                            op=Add(),
                                                                            value=Constant(value='\n', kind=None),
                                                                        ),
                                                                        AugAssign(
                                                                            target=Name(id='msg', ctx=Store()),
                                                                            op=Add(),
                                                                            value=Call(
                                                                                func=Name(id='_', ctx=Load()),
                                                                                args=[Constant(value='- Create/update: a mandatory field is not set.\n- Delete: another model requires the record being deleted. If possible, archive it instead.', kind=None)],
                                                                                keywords=[],
                                                                            ),
                                                                        ),
                                                                        If(
                                                                            test=Name(id='model', ctx=Load()),
                                                                            body=[
                                                                                AugAssign(
                                                                                    target=Name(id='msg', ctx=Store()),
                                                                                    op=Add(),
                                                                                    value=Call(
                                                                                        func=Attribute(
                                                                                            value=Constant(value='\n\n{} {} ({}), {} {} ({})', kind=None),
                                                                                            attr='format',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[
                                                                                            Call(
                                                                                                func=Name(id='_', ctx=Load()),
                                                                                                args=[Constant(value='Model:', kind=None)],
                                                                                                keywords=[],
                                                                                            ),
                                                                                            Attribute(
                                                                                                value=Name(id='model', ctx=Load()),
                                                                                                attr='_description',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Attribute(
                                                                                                value=Name(id='model', ctx=Load()),
                                                                                                attr='_name',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Call(
                                                                                                func=Name(id='_', ctx=Load()),
                                                                                                args=[Constant(value='Field:', kind=None)],
                                                                                                keywords=[],
                                                                                            ),
                                                                                            IfExp(
                                                                                                test=Name(id='field', ctx=Load()),
                                                                                                body=Attribute(
                                                                                                    value=Name(id='field', ctx=Load()),
                                                                                                    attr='string',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                orelse=Call(
                                                                                                    func=Name(id='_', ctx=Load()),
                                                                                                    args=[Constant(value='Unknown', kind=None)],
                                                                                                    keywords=[],
                                                                                                ),
                                                                                            ),
                                                                                            IfExp(
                                                                                                test=Name(id='field', ctx=Load()),
                                                                                                body=Attribute(
                                                                                                    value=Name(id='field', ctx=Load()),
                                                                                                    attr='name',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                orelse=Call(
                                                                                                    func=Name(id='_', ctx=Load()),
                                                                                                    args=[Constant(value='Unknown', kind=None)],
                                                                                                    keywords=[],
                                                                                                ),
                                                                                            ),
                                                                                        ],
                                                                                        keywords=[],
                                                                                    ),
                                                                                ),
                                                                            ],
                                                                            orelse=[],
                                                                        ),
                                                                    ],
                                                                    orelse=[
                                                                        If(
                                                                            test=Compare(
                                                                                left=Attribute(
                                                                                    value=Name(id='inst', ctx=Load()),
                                                                                    attr='pgcode',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                ops=[Eq()],
                                                                                comparators=[
                                                                                    Attribute(
                                                                                        value=Name(id='errorcodes', ctx=Load()),
                                                                                        attr='FOREIGN_KEY_VIOLATION',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                            ),
                                                                            body=[
                                                                                AugAssign(
                                                                                    target=Name(id='msg', ctx=Store()),
                                                                                    op=Add(),
                                                                                    value=Call(
                                                                                        func=Name(id='_', ctx=Load()),
                                                                                        args=[Constant(value=' another model requires the record being deleted. If possible, archive it instead.', kind=None)],
                                                                                        keywords=[],
                                                                                    ),
                                                                                ),
                                                                                Assign(
                                                                                    targets=[Name(id='constraint', ctx=Store())],
                                                                                    value=Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='inst', ctx=Load()),
                                                                                            attr='diag',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='constraint_name',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    type_comment=None,
                                                                                ),
                                                                                If(
                                                                                    test=BoolOp(
                                                                                        op=Or(),
                                                                                        values=[
                                                                                            Name(id='model', ctx=Load()),
                                                                                            Name(id='constraint', ctx=Load()),
                                                                                        ],
                                                                                    ),
                                                                                    body=[
                                                                                        AugAssign(
                                                                                            target=Name(id='msg', ctx=Store()),
                                                                                            op=Add(),
                                                                                            value=Call(
                                                                                                func=Attribute(
                                                                                                    value=Constant(value='\n\n{} {} ({}), {} {}', kind=None),
                                                                                                    attr='format',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                args=[
                                                                                                    Call(
                                                                                                        func=Name(id='_', ctx=Load()),
                                                                                                        args=[Constant(value='Model:', kind=None)],
                                                                                                        keywords=[],
                                                                                                    ),
                                                                                                    IfExp(
                                                                                                        test=Name(id='model', ctx=Load()),
                                                                                                        body=Attribute(
                                                                                                            value=Name(id='model', ctx=Load()),
                                                                                                            attr='_description',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        orelse=Call(
                                                                                                            func=Name(id='_', ctx=Load()),
                                                                                                            args=[Constant(value='Unknown', kind=None)],
                                                                                                            keywords=[],
                                                                                                        ),
                                                                                                    ),
                                                                                                    IfExp(
                                                                                                        test=Name(id='model', ctx=Load()),
                                                                                                        body=Attribute(
                                                                                                            value=Name(id='model', ctx=Load()),
                                                                                                            attr='_name',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        orelse=Call(
                                                                                                            func=Name(id='_', ctx=Load()),
                                                                                                            args=[Constant(value='Unknown', kind=None)],
                                                                                                            keywords=[],
                                                                                                        ),
                                                                                                    ),
                                                                                                    Call(
                                                                                                        func=Name(id='_', ctx=Load()),
                                                                                                        args=[Constant(value='Constraint:', kind=None)],
                                                                                                        keywords=[],
                                                                                                    ),
                                                                                                    IfExp(
                                                                                                        test=Name(id='constraint', ctx=Load()),
                                                                                                        body=Name(id='constraint', ctx=Load()),
                                                                                                        orelse=Call(
                                                                                                            func=Name(id='_', ctx=Load()),
                                                                                                            args=[Constant(value='Unknown', kind=None)],
                                                                                                            keywords=[],
                                                                                                        ),
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
                                                                ),
                                                            ],
                                                            handlers=[
                                                                ExceptHandler(
                                                                    type=Name(id='Exception', ctx=Load()),
                                                                    name=None,
                                                                    body=[Pass()],
                                                                ),
                                                            ],
                                                            orelse=[],
                                                            finalbody=[],
                                                        ),
                                                        Raise(
                                                            exc=Call(
                                                                func=Name(id='ValidationError', ctx=Load()),
                                                                args=[Name(id='msg', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                            cause=None,
                                                        ),
                                                    ],
                                                    orelse=[
                                                        Raise(
                                                            exc=Call(
                                                                func=Name(id='ValidationError', ctx=Load()),
                                                                args=[
                                                                    Subscript(
                                                                        value=Attribute(
                                                                            value=Name(id='inst', ctx=Load()),
                                                                            attr='args',
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Constant(value=0, kind=None),
                                                                        ctx=Load(),
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
                                    orelse=[],
                                    finalbody=[],
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='wraps', ctx=Load()),
                            args=[Name(id='f', ctx=Load())],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                Return(
                    value=Name(id='wrapper', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='execute_cr',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='cr', annotation=None, type_comment=None),
                    arg(arg='uid', annotation=None, type_comment=None),
                    arg(arg='obj', annotation=None, type_comment=None),
                    arg(arg='method', annotation=None, type_comment=None),
                ],
                vararg=arg(arg='args', annotation=None, type_comment=None),
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=arg(arg='kw', annotation=None, type_comment=None),
                defaults=[],
            ),
            body=[
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='cr', ctx=Load()),
                            attr='reset',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                ),
                Assign(
                    targets=[Name(id='recs', ctx=Store())],
                    value=Call(
                        func=Attribute(
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
                                    Name(id='uid', ctx=Load()),
                                    Dict(keys=[], values=[]),
                                ],
                                keywords=[],
                            ),
                            attr='get',
                            ctx=Load(),
                        ),
                        args=[Name(id='obj', ctx=Load())],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=Compare(
                        left=Name(id='recs', ctx=Load()),
                        ops=[Is()],
                        comparators=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Raise(
                            exc=Call(
                                func=Name(id='UserError', ctx=Load()),
                                args=[
                                    Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[
                                            Constant(value="Object %s doesn't exist", kind=None),
                                            Name(id='obj', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            cause=None,
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    targets=[Name(id='result', ctx=Store())],
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
                            Name(id='recs', ctx=Load()),
                            Name(id='method', ctx=Load()),
                            Name(id='args', ctx=Load()),
                            Name(id='kw', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                For(
                    target=Name(id='l', ctx=Store()),
                    iter=Call(
                        func=Name(id='traverse_containers', ctx=Load()),
                        args=[
                            Name(id='result', ctx=Load()),
                            Name(id='lazy', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='_0', ctx=Store())],
                            value=Attribute(
                                value=Name(id='l', ctx=Load()),
                                attr='_value',
                                ctx=Load(),
                            ),
                            type_comment=None,
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
            name='execute_kw',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='db', annotation=None, type_comment=None),
                    arg(arg='uid', annotation=None, type_comment=None),
                    arg(arg='obj', annotation=None, type_comment=None),
                    arg(arg='method', annotation=None, type_comment=None),
                    arg(arg='args', annotation=None, type_comment=None),
                    arg(arg='kw', annotation=None, type_comment=None),
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
                        func=Name(id='execute', ctx=Load()),
                        args=[
                            Name(id='db', ctx=Load()),
                            Name(id='uid', ctx=Load()),
                            Name(id='obj', ctx=Load()),
                            Name(id='method', ctx=Load()),
                            Starred(
                                value=Name(id='args', ctx=Load()),
                                ctx=Load(),
                            ),
                        ],
                        keywords=[
                            keyword(
                                arg=None,
                                value=BoolOp(
                                    op=Or(),
                                    values=[
                                        Name(id='kw', ctx=Load()),
                                        Dict(keys=[], values=[]),
                                    ],
                                ),
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
            name='execute',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='db', annotation=None, type_comment=None),
                    arg(arg='uid', annotation=None, type_comment=None),
                    arg(arg='obj', annotation=None, type_comment=None),
                    arg(arg='method', annotation=None, type_comment=None),
                ],
                vararg=arg(arg='args', annotation=None, type_comment=None),
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=arg(arg='kw', annotation=None, type_comment=None),
                defaults=[],
            ),
            body=[
                Assign(
                    targets=[
                        Attribute(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='threading', ctx=Load()),
                                    attr='currentThread',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            attr='dbname',
                            ctx=Store(),
                        ),
                    ],
                    value=Name(id='db', ctx=Load()),
                    type_comment=None,
                ),
                With(
                    items=[
                        withitem(
                            context_expr=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='odoo', ctx=Load()),
                                            attr='registry',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='db', ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='cursor',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            optional_vars=Name(id='cr', ctx=Store()),
                        ),
                    ],
                    body=[
                        Expr(
                            value=Call(
                                func=Name(id='check_method_name', ctx=Load()),
                                args=[Name(id='method', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Name(id='execute_cr', ctx=Load()),
                                args=[
                                    Name(id='cr', ctx=Load()),
                                    Name(id='uid', ctx=Load()),
                                    Name(id='obj', ctx=Load()),
                                    Name(id='method', ctx=Load()),
                                    Starred(
                                        value=Name(id='args', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg=None,
                                        value=Name(id='kw', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='res', ctx=Load()),
                                ops=[Is()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='info',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='The method %s of the object %s can not return `None` !', kind=None),
                                            Name(id='method', ctx=Load()),
                                            Name(id='obj', ctx=Load()),
                                        ],
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
                    type_comment=None,
                ),
            ],
            decorator_list=[Name(id='check', ctx=Load())],
            returns=None,
            type_comment=None,
        ),
    ],
    type_ignores=[],
)
