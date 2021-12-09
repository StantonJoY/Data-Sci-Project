Module(
    body=[
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='logging.handlers', asname=None)],
        ),
        Import(
            names=[alias(name='os', asname=None)],
        ),
        Import(
            names=[alias(name='platform', asname=None)],
        ),
        Import(
            names=[alias(name='pprint', asname=None)],
        ),
        Import(
            names=[alias(name='sys', asname=None)],
        ),
        Import(
            names=[alias(name='threading', asname=None)],
        ),
        Import(
            names=[alias(name='time', asname=None)],
        ),
        Import(
            names=[alias(name='traceback', asname=None)],
        ),
        Import(
            names=[alias(name='warnings', asname=None)],
        ),
        ImportFrom(
            module=None,
            names=[alias(name='release', asname=None)],
            level=1,
        ),
        ImportFrom(
            module=None,
            names=[alias(name='sql_db', asname=None)],
            level=1,
        ),
        ImportFrom(
            module=None,
            names=[alias(name='tools', asname=None)],
            level=1,
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
            name='log',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='logger', annotation=None, type_comment=None),
                    arg(arg='level', annotation=None, type_comment=None),
                    arg(arg='prefix', annotation=None, type_comment=None),
                    arg(arg='msg', annotation=None, type_comment=None),
                    arg(arg='depth', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[Constant(value=None, kind=None)],
            ),
            body=[
                Assign(
                    targets=[Name(id='indent', ctx=Store())],
                    value=Constant(value='', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='indent_after', ctx=Store())],
                    value=BinOp(
                        left=Constant(value=' ', kind=None),
                        op=Mult(),
                        right=Call(
                            func=Name(id='len', ctx=Load()),
                            args=[Name(id='prefix', ctx=Load())],
                            keywords=[],
                        ),
                    ),
                    type_comment=None,
                ),
                For(
                    target=Name(id='line', ctx=Store()),
                    iter=Call(
                        func=Attribute(
                            value=BinOp(
                                left=Name(id='prefix', ctx=Load()),
                                op=Add(),
                                right=Call(
                                    func=Attribute(
                                        value=Name(id='pprint', ctx=Load()),
                                        attr='pformat',
                                        ctx=Load(),
                                    ),
                                    args=[Name(id='msg', ctx=Load())],
                                    keywords=[
                                        keyword(
                                            arg='depth',
                                            value=Name(id='depth', ctx=Load()),
                                        ),
                                    ],
                                ),
                            ),
                            attr='split',
                            ctx=Load(),
                        ),
                        args=[Constant(value='\n', kind=None)],
                        keywords=[],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='logger', ctx=Load()),
                                    attr='log',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='level', ctx=Load()),
                                    BinOp(
                                        left=Name(id='indent', ctx=Load()),
                                        op=Add(),
                                        right=Name(id='line', ctx=Load()),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='indent', ctx=Store())],
                            value=Name(id='indent_after', ctx=Load()),
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
        ClassDef(
            name='PostgreSQLHandler',
            bases=[
                Attribute(
                    value=Name(id='logging', ctx=Load()),
                    attr='Handler',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' PostgreSQL Logging Handler will store logs in the database, by default\n    the current database, can be set using --log-db=DBNAME\n    ', kind=None),
                ),
                FunctionDef(
                    name='emit',
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
                            targets=[Name(id='ct', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='threading', ctx=Load()),
                                    attr='current_thread',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='ct_db', ctx=Store())],
                            value=Call(
                                func=Name(id='getattr', ctx=Load()),
                                args=[
                                    Name(id='ct', ctx=Load()),
                                    Constant(value='dbname', kind=None),
                                    Constant(value=None, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='dbname', ctx=Store())],
                            value=IfExp(
                                test=BoolOp(
                                    op=And(),
                                    values=[
                                        Subscript(
                                            value=Attribute(
                                                value=Name(id='tools', ctx=Load()),
                                                attr='config',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='log_db', kind=None),
                                            ctx=Load(),
                                        ),
                                        Compare(
                                            left=Subscript(
                                                value=Attribute(
                                                    value=Name(id='tools', ctx=Load()),
                                                    attr='config',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='log_db', kind=None),
                                                ctx=Load(),
                                            ),
                                            ops=[NotEq()],
                                            comparators=[Constant(value='%d', kind=None)],
                                        ),
                                    ],
                                ),
                                body=Subscript(
                                    value=Attribute(
                                        value=Name(id='tools', ctx=Load()),
                                        attr='config',
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='log_db', kind=None),
                                    ctx=Load(),
                                ),
                                orelse=Name(id='ct_db', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='dbname', ctx=Load()),
                            ),
                            body=[Return(value=None)],
                            orelse=[],
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='tools', ctx=Load()),
                                            attr='ignore',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='Exception', ctx=Load())],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='tools', ctx=Load()),
                                            attr='mute_logger',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='odoo.sql_db', kind=None)],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='sql_db', ctx=Load()),
                                                    attr='db_connect',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='dbname', ctx=Load())],
                                                keywords=[
                                                    keyword(
                                                        arg='allow_uri',
                                                        value=Constant(value=True, kind=None),
                                                    ),
                                                ],
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
                                        func=Attribute(
                                            value=Name(id='cr', ctx=Load()),
                                            attr='execute',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='SET LOCAL statement_timeout = 1000', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='msg', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='tools', ctx=Load()),
                                            attr='ustr',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='record', ctx=Load()),
                                                attr='msg',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Attribute(
                                        value=Name(id='record', ctx=Load()),
                                        attr='args',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='msg', ctx=Store())],
                                            value=BinOp(
                                                left=Name(id='msg', ctx=Load()),
                                                op=Mod(),
                                                right=Attribute(
                                                    value=Name(id='record', ctx=Load()),
                                                    attr='args',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='traceback', ctx=Store())],
                                    value=Call(
                                        func=Name(id='getattr', ctx=Load()),
                                        args=[
                                            Name(id='record', ctx=Load()),
                                            Constant(value='exc_text', kind=None),
                                            Constant(value='', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='traceback', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='msg', ctx=Store())],
                                            value=BinOp(
                                                left=Constant(value='%s\n%s', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Name(id='msg', ctx=Load()),
                                                        Name(id='traceback', ctx=Load()),
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
                                    targets=[Name(id='levelname', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='logging', ctx=Load()),
                                            attr='getLevelName',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='record', ctx=Load()),
                                                attr='levelno',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='val', ctx=Store())],
                                    value=Tuple(
                                        elts=[
                                            Constant(value='server', kind=None),
                                            Name(id='ct_db', ctx=Load()),
                                            Attribute(
                                                value=Name(id='record', ctx=Load()),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                            Name(id='levelname', ctx=Load()),
                                            Name(id='msg', ctx=Load()),
                                            Attribute(
                                                value=Name(id='record', ctx=Load()),
                                                attr='pathname',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='record', ctx=Load()),
                                                attr='lineno',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='record', ctx=Load()),
                                                attr='funcName',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='cr', ctx=Load()),
                                            attr='execute',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value="\n                INSERT INTO ir_logging(create_date, type, dbname, name, level, message, path, line, func)\n                VALUES (NOW() at time zone 'UTC', %s, %s, %s, %s, %s, %s, %s, %s)\n            ", kind=None),
                                            Name(id='val', ctx=Load()),
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
            ],
            decorator_list=[],
        ),
        Assign(
            targets=[
                Tuple(
                    elts=[
                        Name(id='BLACK', ctx=Store()),
                        Name(id='RED', ctx=Store()),
                        Name(id='GREEN', ctx=Store()),
                        Name(id='YELLOW', ctx=Store()),
                        Name(id='BLUE', ctx=Store()),
                        Name(id='MAGENTA', ctx=Store()),
                        Name(id='CYAN', ctx=Store()),
                        Name(id='WHITE', ctx=Store()),
                        Name(id='_NOTHING', ctx=Store()),
                        Name(id='DEFAULT', ctx=Store()),
                    ],
                    ctx=Store(),
                ),
            ],
            value=Call(
                func=Name(id='range', ctx=Load()),
                args=[Constant(value=10, kind=None)],
                keywords=[],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='RESET_SEQ', ctx=Store())],
            value=Constant(value='\x1b[0m', kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='COLOR_SEQ', ctx=Store())],
            value=Constant(value='\x1b[1;%dm', kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='BOLD_SEQ', ctx=Store())],
            value=Constant(value='\x1b[1m', kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='COLOR_PATTERN', ctx=Store())],
            value=BinOp(
                left=Constant(value='%s%s%%s%s', kind=None),
                op=Mod(),
                right=Tuple(
                    elts=[
                        Name(id='COLOR_SEQ', ctx=Load()),
                        Name(id='COLOR_SEQ', ctx=Load()),
                        Name(id='RESET_SEQ', ctx=Load()),
                    ],
                    ctx=Load(),
                ),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='LEVEL_COLOR_MAPPING', ctx=Store())],
            value=Dict(
                keys=[
                    Attribute(
                        value=Name(id='logging', ctx=Load()),
                        attr='DEBUG',
                        ctx=Load(),
                    ),
                    Attribute(
                        value=Name(id='logging', ctx=Load()),
                        attr='INFO',
                        ctx=Load(),
                    ),
                    Attribute(
                        value=Name(id='logging', ctx=Load()),
                        attr='WARNING',
                        ctx=Load(),
                    ),
                    Attribute(
                        value=Name(id='logging', ctx=Load()),
                        attr='ERROR',
                        ctx=Load(),
                    ),
                    Attribute(
                        value=Name(id='logging', ctx=Load()),
                        attr='CRITICAL',
                        ctx=Load(),
                    ),
                ],
                values=[
                    Tuple(
                        elts=[
                            Name(id='BLUE', ctx=Load()),
                            Name(id='DEFAULT', ctx=Load()),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Name(id='GREEN', ctx=Load()),
                            Name(id='DEFAULT', ctx=Load()),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Name(id='YELLOW', ctx=Load()),
                            Name(id='DEFAULT', ctx=Load()),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Name(id='RED', ctx=Load()),
                            Name(id='DEFAULT', ctx=Load()),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Name(id='WHITE', ctx=Load()),
                            Name(id='RED', ctx=Load()),
                        ],
                        ctx=Load(),
                    ),
                ],
            ),
            type_comment=None,
        ),
        ClassDef(
            name='PerfFilter',
            bases=[
                Attribute(
                    value=Name(id='logging', ctx=Load()),
                    attr='Filter',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                FunctionDef(
                    name='format_perf',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='query_count', annotation=None, type_comment=None),
                            arg(arg='query_time', annotation=None, type_comment=None),
                            arg(arg='remaining_time', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Tuple(
                                elts=[
                                    BinOp(
                                        left=Constant(value='%d', kind=None),
                                        op=Mod(),
                                        right=Name(id='query_count', ctx=Load()),
                                    ),
                                    BinOp(
                                        left=Constant(value='%.3f', kind=None),
                                        op=Mod(),
                                        right=Name(id='query_time', ctx=Load()),
                                    ),
                                    BinOp(
                                        left=Constant(value='%.3f', kind=None),
                                        op=Mod(),
                                        right=Name(id='remaining_time', ctx=Load()),
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
                    name='filter',
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
                        If(
                            test=Call(
                                func=Name(id='hasattr', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='threading', ctx=Load()),
                                            attr='current_thread',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Constant(value='query_count', kind=None),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='query_count', ctx=Store())],
                                    value=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='threading', ctx=Load()),
                                                attr='current_thread',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        attr='query_count',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='query_time', ctx=Store())],
                                    value=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='threading', ctx=Load()),
                                                attr='current_thread',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        attr='query_time',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='perf_t0', ctx=Store())],
                                    value=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='threading', ctx=Load()),
                                                attr='current_thread',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        attr='perf_t0',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='remaining_time', ctx=Store())],
                                    value=BinOp(
                                        left=BinOp(
                                            left=Call(
                                                func=Attribute(
                                                    value=Name(id='time', ctx=Load()),
                                                    attr='time',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            op=Sub(),
                                            right=Name(id='perf_t0', ctx=Load()),
                                        ),
                                        op=Sub(),
                                        right=Name(id='query_time', ctx=Load()),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='perf_info',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BinOp(
                                        left=Constant(value='%s %s %s', kind=None),
                                        op=Mod(),
                                        right=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='format_perf',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Name(id='query_count', ctx=Load()),
                                                Name(id='query_time', ctx=Load()),
                                                Name(id='remaining_time', ctx=Load()),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Name(id='delattr', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='threading', ctx=Load()),
                                                    attr='current_thread',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            Constant(value='query_count', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='perf_info',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value='- - -', kind=None),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Return(
                            value=Constant(value=True, kind=None),
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
            name='ColoredPerfFilter',
            bases=[Name(id='PerfFilter', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='format_perf',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='query_count', annotation=None, type_comment=None),
                            arg(arg='query_time', annotation=None, type_comment=None),
                            arg(arg='remaining_time', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        FunctionDef(
                            name='colorize_time',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='time', annotation=None, type_comment=None),
                                    arg(arg='format', annotation=None, type_comment=None),
                                    arg(arg='low', annotation=None, type_comment=None),
                                    arg(arg='high', annotation=None, type_comment=None),
                                ],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[
                                    Constant(value=1, kind=None),
                                    Constant(value=5, kind=None),
                                ],
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Name(id='time', ctx=Load()),
                                        ops=[Gt()],
                                        comparators=[Name(id='high', ctx=Load())],
                                    ),
                                    body=[
                                        Return(
                                            value=BinOp(
                                                left=Name(id='COLOR_PATTERN', ctx=Load()),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        BinOp(
                                                            left=Constant(value=30, kind=None),
                                                            op=Add(),
                                                            right=Name(id='RED', ctx=Load()),
                                                        ),
                                                        BinOp(
                                                            left=Constant(value=40, kind=None),
                                                            op=Add(),
                                                            right=Name(id='DEFAULT', ctx=Load()),
                                                        ),
                                                        BinOp(
                                                            left=Name(id='format', ctx=Load()),
                                                            op=Mod(),
                                                            right=Name(id='time', ctx=Load()),
                                                        ),
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
                                        left=Name(id='time', ctx=Load()),
                                        ops=[Gt()],
                                        comparators=[Name(id='low', ctx=Load())],
                                    ),
                                    body=[
                                        Return(
                                            value=BinOp(
                                                left=Name(id='COLOR_PATTERN', ctx=Load()),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        BinOp(
                                                            left=Constant(value=30, kind=None),
                                                            op=Add(),
                                                            right=Name(id='YELLOW', ctx=Load()),
                                                        ),
                                                        BinOp(
                                                            left=Constant(value=40, kind=None),
                                                            op=Add(),
                                                            right=Name(id='DEFAULT', ctx=Load()),
                                                        ),
                                                        BinOp(
                                                            left=Name(id='format', ctx=Load()),
                                                            op=Mod(),
                                                            right=Name(id='time', ctx=Load()),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Return(
                                    value=BinOp(
                                        left=Name(id='format', ctx=Load()),
                                        op=Mod(),
                                        right=Name(id='time', ctx=Load()),
                                    ),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Call(
                                        func=Name(id='colorize_time', ctx=Load()),
                                        args=[
                                            Name(id='query_count', ctx=Load()),
                                            Constant(value='%d', kind=None),
                                            Constant(value=100, kind=None),
                                            Constant(value=1000, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='colorize_time', ctx=Load()),
                                        args=[
                                            Name(id='query_time', ctx=Load()),
                                            Constant(value='%.3f', kind=None),
                                            Constant(value=0.1, kind=None),
                                            Constant(value=3, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='colorize_time', ctx=Load()),
                                        args=[
                                            Name(id='remaining_time', ctx=Load()),
                                            Constant(value='%.3f', kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=5, kind=None),
                                        ],
                                        keywords=[],
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
        ClassDef(
            name='DBFormatter',
            bases=[
                Attribute(
                    value=Name(id='logging', ctx=Load()),
                    attr='Formatter',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                FunctionDef(
                    name='format',
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
                                    value=Name(id='record', ctx=Load()),
                                    attr='pid',
                                    ctx=Store(),
                                ),
                            ],
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
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='record', ctx=Load()),
                                    attr='dbname',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='getattr', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='threading', ctx=Load()),
                                            attr='current_thread',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Constant(value='dbname', kind=None),
                                    Constant(value='?', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='logging', ctx=Load()),
                                        attr='Formatter',
                                        ctx=Load(),
                                    ),
                                    attr='format',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='self', ctx=Load()),
                                    Name(id='record', ctx=Load()),
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
            name='ColoredFormatter',
            bases=[Name(id='DBFormatter', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='format',
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
                                Tuple(
                                    elts=[
                                        Name(id='fg_color', ctx=Store()),
                                        Name(id='bg_color', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='LEVEL_COLOR_MAPPING', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='record', ctx=Load()),
                                        attr='levelno',
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Name(id='GREEN', ctx=Load()),
                                            Name(id='DEFAULT', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='record', ctx=Load()),
                                    attr='levelname',
                                    ctx=Store(),
                                ),
                            ],
                            value=BinOp(
                                left=Name(id='COLOR_PATTERN', ctx=Load()),
                                op=Mod(),
                                right=Tuple(
                                    elts=[
                                        BinOp(
                                            left=Constant(value=30, kind=None),
                                            op=Add(),
                                            right=Name(id='fg_color', ctx=Load()),
                                        ),
                                        BinOp(
                                            left=Constant(value=40, kind=None),
                                            op=Add(),
                                            right=Name(id='bg_color', ctx=Load()),
                                        ),
                                        Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='levelname',
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='DBFormatter', ctx=Load()),
                                    attr='format',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='self', ctx=Load()),
                                    Name(id='record', ctx=Load()),
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
            targets=[Name(id='_logger_init', ctx=Store())],
            value=Constant(value=False, kind=None),
            type_comment=None,
        ),
        FunctionDef(
            name='init_logger',
            args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
            body=[
                Global(names=['_logger_init']),
                If(
                    test=Name(id='_logger_init', ctx=Load()),
                    body=[Return(value=None)],
                    orelse=[],
                ),
                Assign(
                    targets=[Name(id='_logger_init', ctx=Store())],
                    value=Constant(value=True, kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='old_factory', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='logging', ctx=Load()),
                            attr='getLogRecordFactory',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='record_factory',
                    args=arguments(
                        posonlyargs=[],
                        args=[],
                        vararg=arg(arg='args', annotation=None, type_comment=None),
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='record', ctx=Store())],
                            value=Call(
                                func=Name(id='old_factory', ctx=Load()),
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
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='record', ctx=Load()),
                                    attr='perf_info',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='', kind=None),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='record', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='logging', ctx=Load()),
                            attr='setLogRecordFactory',
                            ctx=Load(),
                        ),
                        args=[Name(id='record_factory', ctx=Load())],
                        keywords=[],
                    ),
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='warnings', ctx=Load()),
                            attr='simplefilter',
                            ctx=Load(),
                        ),
                        args=[Constant(value='default', kind=None)],
                        keywords=[
                            keyword(
                                arg='category',
                                value=Name(id='DeprecationWarning', ctx=Load()),
                            ),
                        ],
                    ),
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='warnings', ctx=Load()),
                            attr='filterwarnings',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='ignore', kind=None),
                            Constant(value='^invalid escape sequence \\\\.', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='category',
                                value=Name(id='DeprecationWarning', ctx=Load()),
                            ),
                        ],
                    ),
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='warnings', ctx=Load()),
                            attr='filterwarnings',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='ignore', kind=None),
                            Constant(value='^Sampling from a set', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='category',
                                value=Name(id='DeprecationWarning', ctx=Load()),
                            ),
                            keyword(
                                arg='module',
                                value=Constant(value='odoo', kind=None),
                            ),
                        ],
                    ),
                ),
                For(
                    target=Name(id='module', ctx=Store()),
                    iter=List(
                        elts=[
                            Constant(value='babel.util', kind=None),
                            Constant(value='zeep.loader', kind=None),
                            Constant(value='reportlab.lib.rl_safe_eval', kind=None),
                            Constant(value='ofxparse', kind=None),
                            Constant(value='astroid', kind=None),
                            Constant(value='requests_toolbelt', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='warnings', ctx=Load()),
                                    attr='filterwarnings',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='ignore', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='category',
                                        value=Name(id='DeprecationWarning', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='module',
                                        value=Name(id='module', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    orelse=[],
                    type_comment=None,
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='warnings', ctx=Load()),
                            attr='filterwarnings',
                            ctx=Load(),
                        ),
                        args=[Constant(value='ignore', kind=None)],
                        keywords=[
                            keyword(
                                arg='category',
                                value=Name(id='BytesWarning', ctx=Load()),
                            ),
                            keyword(
                                arg='module',
                                value=Constant(value='odoo.tools.image', kind=None),
                            ),
                        ],
                    ),
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='warnings', ctx=Load()),
                            attr='filterwarnings',
                            ctx=Load(),
                        ),
                        args=[Constant(value='ignore', kind=None)],
                        keywords=[
                            keyword(
                                arg='category',
                                value=Name(id='BytesWarning', ctx=Load()),
                            ),
                            keyword(
                                arg='module',
                                value=Constant(value='reportlab.platypus.paraparser', kind=None),
                            ),
                        ],
                    ),
                ),
                ImportFrom(
                    module='tools.translate',
                    names=[alias(name='resetlocale', asname=None)],
                    level=1,
                ),
                Expr(
                    value=Call(
                        func=Name(id='resetlocale', ctx=Load()),
                        args=[],
                        keywords=[],
                    ),
                ),
                Assign(
                    targets=[Name(id='format', ctx=Store())],
                    value=Constant(value='%(asctime)s %(pid)s %(levelname)s %(dbname)s %(name)s: %(message)s %(perf_info)s', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='handler', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='logging', ctx=Load()),
                            attr='StreamHandler',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=Subscript(
                        value=Attribute(
                            value=Name(id='tools', ctx=Load()),
                            attr='config',
                            ctx=Load(),
                        ),
                        slice=Constant(value='syslog', kind=None),
                        ctx=Load(),
                    ),
                    body=[
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='os', ctx=Load()),
                                    attr='name',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='nt', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='handler', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='logging', ctx=Load()),
                                                attr='handlers',
                                                ctx=Load(),
                                            ),
                                            attr='NTEventLogHandler',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Constant(value='%s %s', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Attribute(
                                                            value=Name(id='release', ctx=Load()),
                                                            attr='description',
                                                            ctx=Load(),
                                                        ),
                                                        Attribute(
                                                            value=Name(id='release', ctx=Load()),
                                                            attr='version',
                                                            ctx=Load(),
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
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Call(
                                            func=Attribute(
                                                value=Name(id='platform', ctx=Load()),
                                                attr='system',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='Darwin', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='handler', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='logging', ctx=Load()),
                                                        attr='handlers',
                                                        ctx=Load(),
                                                    ),
                                                    attr='SysLogHandler',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='/var/run/log', kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='handler', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='logging', ctx=Load()),
                                                        attr='handlers',
                                                        ctx=Load(),
                                                    ),
                                                    attr='SysLogHandler',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='/dev/log', kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='format', ctx=Store())],
                            value=BinOp(
                                left=BinOp(
                                    left=Constant(value='%s %s', kind=None),
                                    op=Mod(),
                                    right=Tuple(
                                        elts=[
                                            Attribute(
                                                value=Name(id='release', ctx=Load()),
                                                attr='description',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='release', ctx=Load()),
                                                attr='version',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                                op=Add(),
                                right=Constant(value=':%(dbname)s:%(levelname)s:%(name)s:%(message)s', kind=None),
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[
                        If(
                            test=Subscript(
                                value=Attribute(
                                    value=Name(id='tools', ctx=Load()),
                                    attr='config',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='logfile', kind=None),
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='logf', ctx=Store())],
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='tools', ctx=Load()),
                                            attr='config',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='logfile', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Try(
                                    body=[
                                        Assign(
                                            targets=[Name(id='dirname', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='os', ctx=Load()),
                                                        attr='path',
                                                        ctx=Load(),
                                                    ),
                                                    attr='dirname',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='logf', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Name(id='dirname', ctx=Load()),
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Call(
                                                            func=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='os', ctx=Load()),
                                                                    attr='path',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='isdir',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Name(id='dirname', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='os', ctx=Load()),
                                                            attr='makedirs',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='dirname', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='os', ctx=Load()),
                                                    attr='name',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='posix', kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='handler', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='logging', ctx=Load()),
                                                                attr='handlers',
                                                                ctx=Load(),
                                                            ),
                                                            attr='WatchedFileHandler',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='logf', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[Name(id='handler', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='logging', ctx=Load()),
                                                            attr='FileHandler',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='logf', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
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
                                                            value=Attribute(
                                                                value=Name(id='sys', ctx=Load()),
                                                                attr='stderr',
                                                                ctx=Load(),
                                                            ),
                                                            attr='write',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value="ERROR: couldn't create the logfile directory. Logging to the standard output.\n", kind=None)],
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
                        ),
                    ],
                ),
                FunctionDef(
                    name='is_a_tty',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='stream', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=BoolOp(
                                op=And(),
                                values=[
                                    Call(
                                        func=Name(id='hasattr', ctx=Load()),
                                        args=[
                                            Name(id='stream', ctx=Load()),
                                            Constant(value='fileno', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='os', ctx=Load()),
                                            attr='isatty',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='stream', ctx=Load()),
                                                    attr='fileno',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
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
                If(
                    test=BoolOp(
                        op=And(),
                        values=[
                            Compare(
                                left=Attribute(
                                    value=Name(id='os', ctx=Load()),
                                    attr='name',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='posix', kind=None)],
                            ),
                            Call(
                                func=Name(id='isinstance', ctx=Load()),
                                args=[
                                    Name(id='handler', ctx=Load()),
                                    Attribute(
                                        value=Name(id='logging', ctx=Load()),
                                        attr='StreamHandler',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            Call(
                                func=Name(id='is_a_tty', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='handler', ctx=Load()),
                                        attr='stream',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='formatter', ctx=Store())],
                            value=Call(
                                func=Name(id='ColoredFormatter', ctx=Load()),
                                args=[Name(id='format', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='perf_filter', ctx=Store())],
                            value=Call(
                                func=Name(id='ColoredPerfFilter', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[
                        Assign(
                            targets=[Name(id='formatter', ctx=Store())],
                            value=Call(
                                func=Name(id='DBFormatter', ctx=Load()),
                                args=[Name(id='format', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='perf_filter', ctx=Store())],
                            value=Call(
                                func=Name(id='PerfFilter', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='handler', ctx=Load()),
                            attr='setFormatter',
                            ctx=Load(),
                        ),
                        args=[Name(id='formatter', ctx=Load())],
                        keywords=[],
                    ),
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='logging', ctx=Load()),
                                    attr='getLogger',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            attr='addHandler',
                            ctx=Load(),
                        ),
                        args=[Name(id='handler', ctx=Load())],
                        keywords=[],
                    ),
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='logging', ctx=Load()),
                                    attr='getLogger',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='werkzeug', kind=None)],
                                keywords=[],
                            ),
                            attr='addFilter',
                            ctx=Load(),
                        ),
                        args=[Name(id='perf_filter', ctx=Load())],
                        keywords=[],
                    ),
                ),
                If(
                    test=Subscript(
                        value=Attribute(
                            value=Name(id='tools', ctx=Load()),
                            attr='config',
                            ctx=Load(),
                        ),
                        slice=Constant(value='log_db', kind=None),
                        ctx=Load(),
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='db_levels', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='debug', kind=None),
                                    Constant(value='info', kind=None),
                                    Constant(value='warning', kind=None),
                                    Constant(value='error', kind=None),
                                    Constant(value='critical', kind=None),
                                ],
                                values=[
                                    Attribute(
                                        value=Name(id='logging', ctx=Load()),
                                        attr='DEBUG',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='logging', ctx=Load()),
                                        attr='INFO',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='logging', ctx=Load()),
                                        attr='WARNING',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='logging', ctx=Load()),
                                        attr='ERROR',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='logging', ctx=Load()),
                                        attr='CRITICAL',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='postgresqlHandler', ctx=Store())],
                            value=Call(
                                func=Name(id='PostgreSQLHandler', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='postgresqlHandler', ctx=Load()),
                                    attr='setLevel',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='int', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='db_levels', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Subscript(
                                                        value=Attribute(
                                                            value=Name(id='tools', ctx=Load()),
                                                            attr='config',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='log_db_level', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Subscript(
                                                        value=Attribute(
                                                            value=Name(id='tools', ctx=Load()),
                                                            attr='config',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='log_db_level', kind=None),
                                                        ctx=Load(),
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
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='logging', ctx=Load()),
                                            attr='getLogger',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='addHandler',
                                    ctx=Load(),
                                ),
                                args=[Name(id='postgresqlHandler', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    targets=[Name(id='pseudo_config', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='PSEUDOCONFIG_MAPPER', ctx=Load()),
                            attr='get',
                            ctx=Load(),
                        ),
                        args=[
                            Subscript(
                                value=Attribute(
                                    value=Name(id='tools', ctx=Load()),
                                    attr='config',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='log_level', kind=None),
                                ctx=Load(),
                            ),
                            List(elts=[], ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='logconfig', ctx=Store())],
                    value=Subscript(
                        value=Attribute(
                            value=Name(id='tools', ctx=Load()),
                            attr='config',
                            ctx=Load(),
                        ),
                        slice=Constant(value='log_handler', kind=None),
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='logging_configurations', ctx=Store())],
                    value=BinOp(
                        left=BinOp(
                            left=Name(id='DEFAULT_LOG_CONFIGURATION', ctx=Load()),
                            op=Add(),
                            right=Name(id='pseudo_config', ctx=Load()),
                        ),
                        op=Add(),
                        right=Name(id='logconfig', ctx=Load()),
                    ),
                    type_comment=None,
                ),
                For(
                    target=Name(id='logconfig_item', ctx=Store()),
                    iter=Name(id='logging_configurations', ctx=Load()),
                    body=[
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='loggername', ctx=Store()),
                                        Name(id='level', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='logconfig_item', ctx=Load()),
                                            attr='strip',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='split',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=':', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='level', ctx=Store())],
                            value=Call(
                                func=Name(id='getattr', ctx=Load()),
                                args=[
                                    Name(id='logging', ctx=Load()),
                                    Name(id='level', ctx=Load()),
                                    Attribute(
                                        value=Name(id='logging', ctx=Load()),
                                        attr='INFO',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='logger', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='logging', ctx=Load()),
                                    attr='getLogger',
                                    ctx=Load(),
                                ),
                                args=[Name(id='loggername', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='logger', ctx=Load()),
                                    attr='setLevel',
                                    ctx=Load(),
                                ),
                                args=[Name(id='level', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[],
                    type_comment=None,
                ),
                For(
                    target=Name(id='logconfig_item', ctx=Store()),
                    iter=Name(id='logging_configurations', ctx=Load()),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='debug',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='logger level set: "%s"', kind=None),
                                    Name(id='logconfig_item', ctx=Load()),
                                ],
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
        Assign(
            targets=[Name(id='DEFAULT_LOG_CONFIGURATION', ctx=Store())],
            value=List(
                elts=[
                    Constant(value='odoo.http.rpc.request:INFO', kind=None),
                    Constant(value='odoo.http.rpc.response:INFO', kind=None),
                    Constant(value=':INFO', kind=None),
                ],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='PSEUDOCONFIG_MAPPER', ctx=Store())],
            value=Dict(
                keys=[
                    Constant(value='debug_rpc_answer', kind=None),
                    Constant(value='debug_rpc', kind=None),
                    Constant(value='debug', kind=None),
                    Constant(value='debug_sql', kind=None),
                    Constant(value='info', kind=None),
                    Constant(value='runbot', kind=None),
                    Constant(value='warn', kind=None),
                    Constant(value='error', kind=None),
                    Constant(value='critical', kind=None),
                ],
                values=[
                    List(
                        elts=[
                            Constant(value='odoo:DEBUG', kind=None),
                            Constant(value='odoo.sql_db:INFO', kind=None),
                            Constant(value='odoo.http.rpc:DEBUG', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    List(
                        elts=[
                            Constant(value='odoo:DEBUG', kind=None),
                            Constant(value='odoo.sql_db:INFO', kind=None),
                            Constant(value='odoo.http.rpc.request:DEBUG', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    List(
                        elts=[
                            Constant(value='odoo:DEBUG', kind=None),
                            Constant(value='odoo.sql_db:INFO', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    List(
                        elts=[Constant(value='odoo.sql_db:DEBUG', kind=None)],
                        ctx=Load(),
                    ),
                    List(elts=[], ctx=Load()),
                    List(
                        elts=[
                            Constant(value='odoo:RUNBOT', kind=None),
                            Constant(value='werkzeug:WARNING', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    List(
                        elts=[
                            Constant(value='odoo:WARNING', kind=None),
                            Constant(value='werkzeug:WARNING', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    List(
                        elts=[
                            Constant(value='odoo:ERROR', kind=None),
                            Constant(value='werkzeug:ERROR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    List(
                        elts=[
                            Constant(value='odoo:CRITICAL', kind=None),
                            Constant(value='werkzeug:CRITICAL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                ],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[
                Attribute(
                    value=Name(id='logging', ctx=Load()),
                    attr='RUNBOT',
                    ctx=Store(),
                ),
            ],
            value=Constant(value=25, kind=None),
            type_comment=None,
        ),
        Expr(
            value=Call(
                func=Attribute(
                    value=Name(id='logging', ctx=Load()),
                    attr='addLevelName',
                    ctx=Load(),
                ),
                args=[
                    Attribute(
                        value=Name(id='logging', ctx=Load()),
                        attr='RUNBOT',
                        ctx=Load(),
                    ),
                    Constant(value='INFO', kind=None),
                ],
                keywords=[],
            ),
        ),
        Expr(
            value=Call(
                func=Attribute(
                    value=Name(id='logging', ctx=Load()),
                    attr='captureWarnings',
                    ctx=Load(),
                ),
                args=[Constant(value=True, kind=None)],
                keywords=[],
            ),
        ),
        Assign(
            targets=[Name(id='showwarning', ctx=Store())],
            value=Attribute(
                value=Name(id='warnings', ctx=Load()),
                attr='showwarning',
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='IGNORE', ctx=Store())],
            value=Set(
                elts=[Constant(value='Comparison between bytes and int', kind=None)],
            ),
            type_comment=None,
        ),
        FunctionDef(
            name='showwarning_with_traceback',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='message', annotation=None, type_comment=None),
                    arg(arg='category', annotation=None, type_comment=None),
                    arg(arg='filename', annotation=None, type_comment=None),
                    arg(arg='lineno', annotation=None, type_comment=None),
                    arg(arg='file', annotation=None, type_comment=None),
                    arg(arg='line', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    Constant(value=None, kind=None),
                    Constant(value=None, kind=None),
                ],
            ),
            body=[
                If(
                    test=BoolOp(
                        op=And(),
                        values=[
                            Compare(
                                left=Name(id='category', ctx=Load()),
                                ops=[Is()],
                                comparators=[Name(id='BytesWarning', ctx=Load())],
                            ),
                            Compare(
                                left=Subscript(
                                    value=Attribute(
                                        value=Name(id='message', ctx=Load()),
                                        attr='args',
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value=0, kind=None),
                                    ctx=Load(),
                                ),
                                ops=[In()],
                                comparators=[Name(id='IGNORE', ctx=Load())],
                            ),
                        ],
                    ),
                    body=[Return(value=None)],
                    orelse=[],
                ),
                Assign(
                    targets=[Name(id='filtered', ctx=Store())],
                    value=List(elts=[], ctx=Load()),
                    type_comment=None,
                ),
                For(
                    target=Name(id='frame', ctx=Store()),
                    iter=Call(
                        func=Attribute(
                            value=Name(id='traceback', ctx=Load()),
                            attr='extract_stack',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    body=[
                        If(
                            test=Compare(
                                left=Constant(value='importlib', kind=None),
                                ops=[NotIn()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='frame', ctx=Load()),
                                        attr='filename',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='filtered', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='frame', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='frame', ctx=Load()),
                                            attr='filename',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Name(id='filename', ctx=Load())],
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='frame', ctx=Load()),
                                            attr='lineno',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Name(id='lineno', ctx=Load())],
                                    ),
                                ],
                            ),
                            body=[Break()],
                            orelse=[],
                        ),
                    ],
                    orelse=[],
                    type_comment=None,
                ),
                Return(
                    value=Call(
                        func=Name(id='showwarning', ctx=Load()),
                        args=[
                            Name(id='message', ctx=Load()),
                            Name(id='category', ctx=Load()),
                            Name(id='filename', ctx=Load()),
                            Name(id='lineno', ctx=Load()),
                        ],
                        keywords=[
                            keyword(
                                arg='file',
                                value=Name(id='file', ctx=Load()),
                            ),
                            keyword(
                                arg='line',
                                value=Call(
                                    func=Attribute(
                                        value=Constant(value='', kind=None),
                                        attr='join',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Call(
                                            func=Attribute(
                                                value=Name(id='traceback', ctx=Load()),
                                                attr='format_list',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='filtered', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ],
                                    keywords=[],
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
        Assign(
            targets=[
                Attribute(
                    value=Name(id='warnings', ctx=Load()),
                    attr='showwarning',
                    ctx=Store(),
                ),
            ],
            value=Name(id='showwarning_with_traceback', ctx=Load()),
            type_comment=None,
        ),
        FunctionDef(
            name='runbot',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='self', annotation=None, type_comment=None),
                    arg(arg='message', annotation=None, type_comment=None),
                ],
                vararg=arg(arg='args', annotation=None, type_comment=None),
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=arg(arg='kws', annotation=None, type_comment=None),
                defaults=[],
            ),
            body=[
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='self', ctx=Load()),
                            attr='log',
                            ctx=Load(),
                        ),
                        args=[
                            Attribute(
                                value=Name(id='logging', ctx=Load()),
                                attr='RUNBOT',
                                ctx=Load(),
                            ),
                            Name(id='message', ctx=Load()),
                            Starred(
                                value=Name(id='args', ctx=Load()),
                                ctx=Load(),
                            ),
                        ],
                        keywords=[
                            keyword(
                                arg=None,
                                value=Name(id='kws', ctx=Load()),
                            ),
                        ],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        Assign(
            targets=[
                Attribute(
                    value=Attribute(
                        value=Name(id='logging', ctx=Load()),
                        attr='Logger',
                        ctx=Load(),
                    ),
                    attr='runbot',
                    ctx=Store(),
                ),
            ],
            value=Name(id='runbot', ctx=Load()),
            type_comment=None,
        ),
    ],
    type_ignores=[],
)
