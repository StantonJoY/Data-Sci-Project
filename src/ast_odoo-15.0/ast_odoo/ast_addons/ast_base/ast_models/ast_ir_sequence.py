Module(
    body=[
        ImportFrom(
            module='datetime',
            names=[
                alias(name='datetime', asname=None),
                alias(name='timedelta', asname=None),
            ],
            level=0,
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='pytz', asname=None)],
        ),
        ImportFrom(
            module='psycopg2',
            names=[
                alias(name='sql', asname=None),
                alias(name='OperationalError', asname=None),
                alias(name='errorcodes', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[alias(name='UserError', asname=None)],
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
            name='_create_sequence',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='cr', annotation=None, type_comment=None),
                    arg(arg='seq_name', annotation=None, type_comment=None),
                    arg(arg='number_increment', annotation=None, type_comment=None),
                    arg(arg='number_next', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Create a PostreSQL sequence. ', kind=None),
                ),
                If(
                    test=Compare(
                        left=Name(id='number_increment', ctx=Load()),
                        ops=[Eq()],
                        comparators=[Constant(value=0, kind=None)],
                    ),
                    body=[
                        Raise(
                            exc=Call(
                                func=Name(id='UserError', ctx=Load()),
                                args=[
                                    Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='Step must not be zero.', kind=None)],
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
                    targets=[Name(id='sql', ctx=Store())],
                    value=BinOp(
                        left=Constant(value='CREATE SEQUENCE %s INCREMENT BY %%s START WITH %%s', kind=None),
                        op=Mod(),
                        right=Name(id='seq_name', ctx=Load()),
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
                            Name(id='sql', ctx=Load()),
                            Tuple(
                                elts=[
                                    Name(id='number_increment', ctx=Load()),
                                    Name(id='number_next', ctx=Load()),
                                ],
                                ctx=Load(),
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
            name='_drop_sequences',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='cr', annotation=None, type_comment=None),
                    arg(arg='seq_names', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Drop the PostreSQL sequences if they exist. ', kind=None),
                ),
                Assign(
                    targets=[Name(id='names', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='sql', ctx=Load()),
                                    attr='SQL',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=',', kind=None)],
                                keywords=[],
                            ),
                            attr='join',
                            ctx=Load(),
                        ),
                        args=[
                            Call(
                                func=Name(id='map', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='sql', ctx=Load()),
                                        attr='Identifier',
                                        ctx=Load(),
                                    ),
                                    Name(id='seq_names', ctx=Load()),
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
                        func=Attribute(
                            value=Name(id='cr', ctx=Load()),
                            attr='execute',
                            ctx=Load(),
                        ),
                        args=[
                            Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='sql', ctx=Load()),
                                            attr='SQL',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='DROP SEQUENCE IF EXISTS {} RESTRICT', kind=None)],
                                        keywords=[],
                                    ),
                                    attr='format',
                                    ctx=Load(),
                                ),
                                args=[Name(id='names', ctx=Load())],
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
            name='_alter_sequence',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='cr', annotation=None, type_comment=None),
                    arg(arg='seq_name', annotation=None, type_comment=None),
                    arg(arg='number_increment', annotation=None, type_comment=None),
                    arg(arg='number_next', annotation=None, type_comment=None),
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
                Expr(
                    value=Constant(value=' Alter a PostreSQL sequence. ', kind=None),
                ),
                If(
                    test=Compare(
                        left=Name(id='number_increment', ctx=Load()),
                        ops=[Eq()],
                        comparators=[Constant(value=0, kind=None)],
                    ),
                    body=[
                        Raise(
                            exc=Call(
                                func=Name(id='UserError', ctx=Load()),
                                args=[
                                    Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='Step must not be zero.', kind=None)],
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
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='cr', ctx=Load()),
                            attr='execute',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='SELECT relname FROM pg_class WHERE relkind=%s AND relname=%s', kind=None),
                            Tuple(
                                elts=[
                                    Constant(value='S', kind=None),
                                    Name(id='seq_name', ctx=Load()),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                ),
                If(
                    test=UnaryOp(
                        op=Not(),
                        operand=Call(
                            func=Attribute(
                                value=Name(id='cr', ctx=Load()),
                                attr='fetchone',
                                ctx=Load(),
                            ),
                            args=[],
                            keywords=[],
                        ),
                    ),
                    body=[Return(value=None)],
                    orelse=[],
                ),
                Assign(
                    targets=[Name(id='statement', ctx=Store())],
                    value=BinOp(
                        left=Call(
                            func=Attribute(
                                value=Name(id='sql', ctx=Load()),
                                attr='SQL',
                                ctx=Load(),
                            ),
                            args=[Constant(value='ALTER SEQUENCE', kind=None)],
                            keywords=[],
                        ),
                        op=Add(),
                        right=Call(
                            func=Attribute(
                                value=Name(id='sql', ctx=Load()),
                                attr='Identifier',
                                ctx=Load(),
                            ),
                            args=[Name(id='seq_name', ctx=Load())],
                            keywords=[],
                        ),
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='params', ctx=Store())],
                    value=List(elts=[], ctx=Load()),
                    type_comment=None,
                ),
                If(
                    test=Compare(
                        left=Name(id='number_increment', ctx=Load()),
                        ops=[IsNot()],
                        comparators=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        AugAssign(
                            target=Name(id='statement', ctx=Store()),
                            op=Add(),
                            value=BinOp(
                                left=Call(
                                    func=Attribute(
                                        value=Name(id='sql', ctx=Load()),
                                        attr='SQL',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='INCREMENT BY', kind=None)],
                                    keywords=[],
                                ),
                                op=Add(),
                                right=Call(
                                    func=Attribute(
                                        value=Name(id='sql', ctx=Load()),
                                        attr='Placeholder',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='params', ctx=Load()),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[Name(id='number_increment', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    test=Compare(
                        left=Name(id='number_next', ctx=Load()),
                        ops=[IsNot()],
                        comparators=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        AugAssign(
                            target=Name(id='statement', ctx=Store()),
                            op=Add(),
                            value=BinOp(
                                left=Call(
                                    func=Attribute(
                                        value=Name(id='sql', ctx=Load()),
                                        attr='SQL',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='RESTART WITH', kind=None)],
                                    keywords=[],
                                ),
                                op=Add(),
                                right=Call(
                                    func=Attribute(
                                        value=Name(id='sql', ctx=Load()),
                                        attr='Placeholder',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='params', ctx=Load()),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[Name(id='number_next', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[],
                ),
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
                                    value=Name(id='statement', ctx=Load()),
                                    attr='join',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=' ', kind=None)],
                                keywords=[],
                            ),
                            Name(id='params', ctx=Load()),
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
            name='_select_nextval',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='cr', annotation=None, type_comment=None),
                    arg(arg='seq_name', annotation=None, type_comment=None),
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
                            Constant(value='SELECT nextval(%s)', kind=None),
                            List(
                                elts=[Name(id='seq_name', ctx=Load())],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                ),
                Return(
                    value=Call(
                        func=Attribute(
                            value=Name(id='cr', ctx=Load()),
                            attr='fetchone',
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
            name='_update_nogap',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='self', annotation=None, type_comment=None),
                    arg(arg='number_increment', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Assign(
                    targets=[Name(id='number_next', ctx=Store())],
                    value=Attribute(
                        value=Name(id='self', ctx=Load()),
                        attr='number_next',
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='_cr',
                                ctx=Load(),
                            ),
                            attr='execute',
                            ctx=Load(),
                        ),
                        args=[
                            BinOp(
                                left=Constant(value='SELECT number_next FROM %s WHERE id=%%s FOR UPDATE NOWAIT', kind=None),
                                op=Mod(),
                                right=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_table',
                                    ctx=Load(),
                                ),
                            ),
                            List(
                                elts=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
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
                                attr='_cr',
                                ctx=Load(),
                            ),
                            attr='execute',
                            ctx=Load(),
                        ),
                        args=[
                            BinOp(
                                left=Constant(value='UPDATE %s SET number_next=number_next+%%s WHERE id=%%s ', kind=None),
                                op=Mod(),
                                right=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_table',
                                    ctx=Load(),
                                ),
                            ),
                            Tuple(
                                elts=[
                                    Name(id='number_increment', ctx=Load()),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='self', ctx=Load()),
                            attr='invalidate_cache',
                            ctx=Load(),
                        ),
                        args=[
                            List(
                                elts=[Constant(value='number_next', kind=None)],
                                ctx=Load(),
                            ),
                            List(
                                elts=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                ),
                Return(
                    value=Name(id='number_next', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='_predict_nextval',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='self', annotation=None, type_comment=None),
                    arg(arg='seq_id', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value='Predict next value for PostgreSQL sequence without consuming it', kind=None),
                ),
                Assign(
                    targets=[Name(id='seqname', ctx=Store())],
                    value=BinOp(
                        left=Constant(value='ir_sequence_%s', kind=None),
                        op=Mod(),
                        right=Name(id='seq_id', ctx=Load()),
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='seqtable', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='sql', ctx=Load()),
                            attr='Identifier',
                            ctx=Load(),
                        ),
                        args=[Name(id='seqname', ctx=Load())],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='query', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='sql', ctx=Load()),
                            attr='SQL',
                            ctx=Load(),
                        ),
                        args=[Constant(value='SELECT last_value,\n                      (SELECT increment_by\n                       FROM pg_sequences\n                       WHERE sequencename = %s),\n                      is_called\n               FROM {}', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='params', ctx=Store())],
                    value=List(
                        elts=[Name(id='seqname', ctx=Load())],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                If(
                    test=Compare(
                        left=Attribute(
                            value=Attribute(
                                value=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='cr',
                                    ctx=Load(),
                                ),
                                attr='_cnx',
                                ctx=Load(),
                            ),
                            attr='server_version',
                            ctx=Load(),
                        ),
                        ops=[Lt()],
                        comparators=[Constant(value=100000, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='query', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='sql', ctx=Load()),
                                    attr='SQL',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='SELECT last_value, increment_by, is_called FROM {}', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='params', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
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
                            attr='execute',
                            ctx=Load(),
                        ),
                        args=[
                            Call(
                                func=Attribute(
                                    value=Name(id='query', ctx=Load()),
                                    attr='format',
                                    ctx=Load(),
                                ),
                                args=[Name(id='seqtable', ctx=Load())],
                                keywords=[],
                            ),
                            Name(id='params', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                ),
                Assign(
                    targets=[
                        Tuple(
                            elts=[
                                Name(id='last_value', ctx=Store()),
                                Name(id='increment_by', ctx=Store()),
                                Name(id='is_called', ctx=Store()),
                            ],
                            ctx=Store(),
                        ),
                    ],
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
                            attr='fetchone',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=Name(id='is_called', ctx=Load()),
                    body=[
                        Return(
                            value=BinOp(
                                left=Name(id='last_value', ctx=Load()),
                                op=Add(),
                                right=Name(id='increment_by', ctx=Load()),
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Name(id='last_value', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        ClassDef(
            name='IrSequence',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' Sequence model.\n\n    The sequence model allows to define and use so-called sequence objects.\n    Such objects are used to generate unique identifiers in a transaction-safe\n    way.\n\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='ir.sequence', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Sequence', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_order', ctx=Store())],
                    value=Constant(value='name', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_number_next_actual',
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
                            value=Constant(value='Return number from ir_sequence row when no_gap implementation,\n        and number from postgres sequence when standard implementation.', kind=None),
                        ),
                        For(
                            target=Name(id='seq', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='seq', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='seq', ctx=Load()),
                                                    attr='number_next_actual',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=0, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='seq', ctx=Load()),
                                                    attr='implementation',
                                                    ctx=Load(),
                                                ),
                                                ops=[NotEq()],
                                                comparators=[Constant(value='standard', kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='seq', ctx=Load()),
                                                            attr='number_next_actual',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Attribute(
                                                        value=Name(id='seq', ctx=Load()),
                                                        attr='number_next',
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[Name(id='seq_id', ctx=Store())],
                                                    value=BinOp(
                                                        left=Constant(value='%03d', kind=None),
                                                        op=Mod(),
                                                        right=Attribute(
                                                            value=Name(id='seq', ctx=Load()),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='seq', ctx=Load()),
                                                            attr='number_next_actual',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Call(
                                                        func=Name(id='_predict_nextval', ctx=Load()),
                                                        args=[
                                                            Name(id='self', ctx=Load()),
                                                            Name(id='seq_id', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
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
                    name='_set_number_next_actual',
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
                        For(
                            target=Name(id='seq', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='seq', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='number_next', kind=None)],
                                                values=[
                                                    BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='seq', ctx=Load()),
                                                                attr='number_next_actual',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=1, kind=None),
                                                        ],
                                                    ),
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
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_current_sequence',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='sequence_date', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Returns the object on which we can find the number_next to consider for the sequence.\n        It could be an ir.sequence or an ir.sequence.date_range depending if use_date_range is checked\n        or not. This function will also create the ir.sequence.date_range if none exists yet for today\n        ', kind=None),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='use_date_range',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Return(
                                    value=Name(id='self', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='sequence_date', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='sequence_date', ctx=Load()),
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='fields', ctx=Load()),
                                                attr='Date',
                                                ctx=Load(),
                                            ),
                                            attr='today',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='seq_date', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.sequence.date_range', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='sequence_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='date_from', kind=None),
                                                    Constant(value='<=', kind=None),
                                                    Name(id='sequence_date', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='date_to', kind=None),
                                                    Constant(value='>=', kind=None),
                                                    Name(id='sequence_date', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='limit',
                                        value=Constant(value=1, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='seq_date', ctx=Load()),
                            body=[
                                Return(
                                    value=Subscript(
                                        value=Name(id='seq_date', ctx=Load()),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_create_date_range_seq',
                                    ctx=Load(),
                                ),
                                args=[Name(id='sequence_date', ctx=Load())],
                                keywords=[],
                            ),
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
                Assign(
                    targets=[Name(id='name', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='code', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Sequence Code', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='implementation', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[
                            List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='standard', kind=None),
                                            Constant(value='Standard', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='no_gap', kind=None),
                                            Constant(value='No gap', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Implementation', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value='standard', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value="While assigning a sequence number to a record, the 'no gap' sequence implementation ensures that each previous sequence number has been assigned already. While this sequence implementation will not skip any sequence number upon assignment, there can still be gaps in the sequence if records are deleted. The 'no gap' implementation is slower than the standard one.", kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='active', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='prefix', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value='Prefix value of the record for the sequence', kind=None),
                            ),
                            keyword(
                                arg='trim',
                                value=Constant(value=False, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='suffix', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value='Suffix value of the record for the sequence', kind=None),
                            ),
                            keyword(
                                arg='trim',
                                value=Constant(value=False, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='number_next', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Next Number', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value=1, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Next number of this sequence', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='number_next_actual', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_get_number_next_actual', kind=None),
                            ),
                            keyword(
                                arg='inverse',
                                value=Constant(value='_set_number_next_actual', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Actual Next Number', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Next number that will be used. This number can be incremented frequently so the displayed value might already be obsolete', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='number_increment', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Step', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value=1, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='The next number of the sequence will be incremented by this number', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='padding', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Sequence Size', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value=0, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value="Odoo will automatically adds some '0' on the left of the 'Next Number' to get the required padding size.", kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='company_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='res.company', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Company', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Lambda(
                                    args=arguments(
                                        posonlyargs=[],
                                        args=[arg(arg='s', annotation=None, type_comment=None)],
                                        vararg=None,
                                        kwonlyargs=[],
                                        kw_defaults=[],
                                        kwarg=None,
                                        defaults=[],
                                    ),
                                    body=Attribute(
                                        value=Attribute(
                                            value=Name(id='s', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='company',
                                        ctx=Load(),
                                    ),
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='use_date_range', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Use subsequences per date_range', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='date_range_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='One2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='ir.sequence.date_range', kind=None),
                            Constant(value='sequence_id', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Subsequences', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='create',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='values', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Create a sequence, in implementation == standard a fast gaps-allowed PostgreSQL sequence is used.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='seq', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='IrSequence', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Name(id='values', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Call(
                                    func=Attribute(
                                        value=Name(id='values', ctx=Load()),
                                        attr='get',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Constant(value='implementation', kind=None),
                                        Constant(value='standard', kind=None),
                                    ],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='standard', kind=None)],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='_create_sequence', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_cr',
                                                ctx=Load(),
                                            ),
                                            BinOp(
                                                left=Constant(value='ir_sequence_%03d', kind=None),
                                                op=Mod(),
                                                right=Attribute(
                                                    value=Name(id='seq', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='values', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='number_increment', kind=None),
                                                    Constant(value=1, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='values', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='number_next', kind=None),
                                                    Constant(value=1, kind=None),
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
                        Return(
                            value=Name(id='seq', ctx=Load()),
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
                FunctionDef(
                    name='unlink',
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
                                func=Name(id='_drop_sequences', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_cr',
                                        ctx=Load(),
                                    ),
                                    ListComp(
                                        elt=BinOp(
                                            left=Constant(value='ir_sequence_%03d', kind=None),
                                            op=Mod(),
                                            right=Attribute(
                                                value=Name(id='x', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='x', ctx=Store()),
                                                iter=Name(id='self', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
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
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='IrSequence', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='unlink',
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
                    name='write',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='values', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='new_implementation', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='values', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='implementation', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='seq', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='i', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='values', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='number_increment', kind=None),
                                            Attribute(
                                                value=Name(id='seq', ctx=Load()),
                                                attr='number_increment',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='n', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='values', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='number_next', kind=None),
                                            Attribute(
                                                value=Name(id='seq', ctx=Load()),
                                                attr='number_next',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='seq', ctx=Load()),
                                            attr='implementation',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='standard', kind=None)],
                                    ),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Name(id='new_implementation', ctx=Load()),
                                                ops=[In()],
                                                comparators=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='standard', kind=None),
                                                            Constant(value=None, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                If(
                                                    test=Call(
                                                        func=Attribute(
                                                            value=Name(id='values', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='number_next', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Name(id='_alter_sequence', ctx=Load()),
                                                                args=[
                                                                    Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='_cr',
                                                                        ctx=Load(),
                                                                    ),
                                                                    BinOp(
                                                                        left=Constant(value='ir_sequence_%03d', kind=None),
                                                                        op=Mod(),
                                                                        right=Attribute(
                                                                            value=Name(id='seq', ctx=Load()),
                                                                            attr='id',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                ],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='number_next',
                                                                        value=Name(id='n', ctx=Load()),
                                                                    ),
                                                                ],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                                If(
                                                    test=Compare(
                                                        left=Attribute(
                                                            value=Name(id='seq', ctx=Load()),
                                                            attr='number_increment',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[NotEq()],
                                                        comparators=[Name(id='i', ctx=Load())],
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Name(id='_alter_sequence', ctx=Load()),
                                                                args=[
                                                                    Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='_cr',
                                                                        ctx=Load(),
                                                                    ),
                                                                    BinOp(
                                                                        left=Constant(value='ir_sequence_%03d', kind=None),
                                                                        op=Mod(),
                                                                        right=Attribute(
                                                                            value=Name(id='seq', ctx=Load()),
                                                                            attr='id',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                ],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='number_increment',
                                                                        value=Name(id='i', ctx=Load()),
                                                                    ),
                                                                ],
                                                            ),
                                                        ),
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='seq', ctx=Load()),
                                                                        attr='date_range_ids',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='_alter_sequence',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='number_increment',
                                                                        value=Name(id='i', ctx=Load()),
                                                                    ),
                                                                ],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                            orelse=[
                                                Expr(
                                                    value=Call(
                                                        func=Name(id='_drop_sequences', ctx=Load()),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='_cr',
                                                                ctx=Load(),
                                                            ),
                                                            List(
                                                                elts=[
                                                                    BinOp(
                                                                        left=Constant(value='ir_sequence_%03d', kind=None),
                                                                        op=Mod(),
                                                                        right=Attribute(
                                                                            value=Name(id='seq', ctx=Load()),
                                                                            attr='id',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                For(
                                                    target=Name(id='sub_seq', ctx=Store()),
                                                    iter=Attribute(
                                                        value=Name(id='seq', ctx=Load()),
                                                        attr='date_range_ids',
                                                        ctx=Load(),
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Name(id='_drop_sequences', ctx=Load()),
                                                                args=[
                                                                    Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='_cr',
                                                                        ctx=Load(),
                                                                    ),
                                                                    List(
                                                                        elts=[
                                                                            BinOp(
                                                                                left=Constant(value='ir_sequence_%03d_%03d', kind=None),
                                                                                op=Mod(),
                                                                                right=Tuple(
                                                                                    elts=[
                                                                                        Attribute(
                                                                                            value=Name(id='seq', ctx=Load()),
                                                                                            attr='id',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        Attribute(
                                                                                            value=Name(id='sub_seq', ctx=Load()),
                                                                                            attr='id',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                    ],
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ),
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
                                            ],
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Name(id='new_implementation', ctx=Load()),
                                                ops=[In()],
                                                comparators=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='no_gap', kind=None),
                                                            Constant(value=None, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[Pass()],
                                            orelse=[
                                                Expr(
                                                    value=Call(
                                                        func=Name(id='_create_sequence', ctx=Load()),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='_cr',
                                                                ctx=Load(),
                                                            ),
                                                            BinOp(
                                                                left=Constant(value='ir_sequence_%03d', kind=None),
                                                                op=Mod(),
                                                                right=Attribute(
                                                                    value=Name(id='seq', ctx=Load()),
                                                                    attr='id',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            Name(id='i', ctx=Load()),
                                                            Name(id='n', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                For(
                                                    target=Name(id='sub_seq', ctx=Store()),
                                                    iter=Attribute(
                                                        value=Name(id='seq', ctx=Load()),
                                                        attr='date_range_ids',
                                                        ctx=Load(),
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Name(id='_create_sequence', ctx=Load()),
                                                                args=[
                                                                    Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='_cr',
                                                                        ctx=Load(),
                                                                    ),
                                                                    BinOp(
                                                                        left=Constant(value='ir_sequence_%03d_%03d', kind=None),
                                                                        op=Mod(),
                                                                        right=Tuple(
                                                                            elts=[
                                                                                Attribute(
                                                                                    value=Name(id='seq', ctx=Load()),
                                                                                    attr='id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                Attribute(
                                                                                    value=Name(id='sub_seq', ctx=Load()),
                                                                                    attr='id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ],
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                    Name(id='i', ctx=Load()),
                                                                    Name(id='n', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[],
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='IrSequence', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[Name(id='values', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='flush',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='values', ctx=Load()),
                                            attr='keys',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
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
                    name='_next_do',
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
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='implementation',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='standard', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='number_next', ctx=Store())],
                                    value=Call(
                                        func=Name(id='_select_nextval', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_cr',
                                                ctx=Load(),
                                            ),
                                            BinOp(
                                                left=Constant(value='ir_sequence_%03d', kind=None),
                                                op=Mod(),
                                                right=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='id',
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
                                Assign(
                                    targets=[Name(id='number_next', ctx=Store())],
                                    value=Call(
                                        func=Name(id='_update_nogap', ctx=Load()),
                                        args=[
                                            Name(id='self', ctx=Load()),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='number_increment',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='get_next_char',
                                    ctx=Load(),
                                ),
                                args=[Name(id='number_next', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_prefix_suffix',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='date', annotation=None, type_comment=None),
                            arg(arg='date_range', annotation=None, type_comment=None),
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
                        FunctionDef(
                            name='_interpolate',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='s', annotation=None, type_comment=None),
                                    arg(arg='d', annotation=None, type_comment=None),
                                ],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Return(
                                    value=IfExp(
                                        test=Name(id='s', ctx=Load()),
                                        body=BinOp(
                                            left=Name(id='s', ctx=Load()),
                                            op=Mod(),
                                            right=Name(id='d', ctx=Load()),
                                        ),
                                        orelse=Constant(value='', kind=None),
                                    ),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='_interpolation_dict',
                            args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
                            body=[
                                Assign(
                                    targets=[
                                        Name(id='now', ctx=Store()),
                                        Name(id='range_date', ctx=Store()),
                                        Name(id='effective_date', ctx=Store()),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='datetime', ctx=Load()),
                                            attr='now',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='pytz', ctx=Load()),
                                                    attr='timezone',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='_context',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='get',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='tz', kind=None)],
                                                                keywords=[],
                                                            ),
                                                            Constant(value='UTC', kind=None),
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
                                    test=BoolOp(
                                        op=Or(),
                                        values=[
                                            Name(id='date', ctx=Load()),
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_context',
                                                        ctx=Load(),
                                                    ),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='ir_sequence_date', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='effective_date', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='fields', ctx=Load()),
                                                        attr='Datetime',
                                                        ctx=Load(),
                                                    ),
                                                    attr='from_string',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            Name(id='date', ctx=Load()),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='_context',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='get',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='ir_sequence_date', kind=None)],
                                                                keywords=[],
                                                            ),
                                                        ],
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
                                    test=BoolOp(
                                        op=Or(),
                                        values=[
                                            Name(id='date_range', ctx=Load()),
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_context',
                                                        ctx=Load(),
                                                    ),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='ir_sequence_date_range', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='range_date', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='fields', ctx=Load()),
                                                        attr='Datetime',
                                                        ctx=Load(),
                                                    ),
                                                    attr='from_string',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            Name(id='date_range', ctx=Load()),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='_context',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='get',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='ir_sequence_date_range', kind=None)],
                                                                keywords=[],
                                                            ),
                                                        ],
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
                                    targets=[Name(id='sequences', ctx=Store())],
                                    value=Dict(
                                        keys=[
                                            Constant(value='year', kind=None),
                                            Constant(value='month', kind=None),
                                            Constant(value='day', kind=None),
                                            Constant(value='y', kind=None),
                                            Constant(value='doy', kind=None),
                                            Constant(value='woy', kind=None),
                                            Constant(value='weekday', kind=None),
                                            Constant(value='h24', kind=None),
                                            Constant(value='h12', kind=None),
                                            Constant(value='min', kind=None),
                                            Constant(value='sec', kind=None),
                                        ],
                                        values=[
                                            Constant(value='%Y', kind=None),
                                            Constant(value='%m', kind=None),
                                            Constant(value='%d', kind=None),
                                            Constant(value='%y', kind=None),
                                            Constant(value='%j', kind=None),
                                            Constant(value='%W', kind=None),
                                            Constant(value='%w', kind=None),
                                            Constant(value='%H', kind=None),
                                            Constant(value='%I', kind=None),
                                            Constant(value='%M', kind=None),
                                            Constant(value='%S', kind=None),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='res', ctx=Store())],
                                    value=Dict(keys=[], values=[]),
                                    type_comment=None,
                                ),
                                For(
                                    target=Tuple(
                                        elts=[
                                            Name(id='key', ctx=Store()),
                                            Name(id='format', ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                    iter=Call(
                                        func=Attribute(
                                            value=Name(id='sequences', ctx=Load()),
                                            attr='items',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='res', ctx=Load()),
                                                    slice=Name(id='key', ctx=Load()),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='effective_date', ctx=Load()),
                                                    attr='strftime',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='format', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='res', ctx=Load()),
                                                    slice=BinOp(
                                                        left=Constant(value='range_', kind=None),
                                                        op=Add(),
                                                        right=Name(id='key', ctx=Load()),
                                                    ),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='range_date', ctx=Load()),
                                                    attr='strftime',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='format', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='res', ctx=Load()),
                                                    slice=BinOp(
                                                        left=Constant(value='current_', kind=None),
                                                        op=Add(),
                                                        right=Name(id='key', ctx=Load()),
                                                    ),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='now', ctx=Load()),
                                                    attr='strftime',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='format', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='d', ctx=Store())],
                            value=Call(
                                func=Name(id='_interpolation_dict', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id='interpolated_prefix', ctx=Store())],
                                    value=Call(
                                        func=Name(id='_interpolate', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='prefix',
                                                ctx=Load(),
                                            ),
                                            Name(id='d', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='interpolated_suffix', ctx=Store())],
                                    value=Call(
                                        func=Name(id='_interpolate', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='suffix',
                                                ctx=Load(),
                                            ),
                                            Name(id='d', ctx=Load()),
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
                                        Raise(
                                            exc=Call(
                                                func=Name(id='UserError', ctx=Load()),
                                                args=[
                                                    BinOp(
                                                        left=Call(
                                                            func=Name(id='_', ctx=Load()),
                                                            args=[Constant(value="Invalid prefix or suffix for sequence '%s'", kind=None)],
                                                            keywords=[],
                                                        ),
                                                        op=Mod(),
                                                        right=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='name',
                                                            ctx=Load(),
                                                        ),
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
                        Return(
                            value=Tuple(
                                elts=[
                                    Name(id='interpolated_prefix', ctx=Load()),
                                    Name(id='interpolated_suffix', ctx=Load()),
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
                    name='get_next_char',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='number_next', annotation=None, type_comment=None),
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
                                        Name(id='interpolated_prefix', ctx=Store()),
                                        Name(id='interpolated_suffix', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_prefix_suffix',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=BinOp(
                                left=BinOp(
                                    left=Name(id='interpolated_prefix', ctx=Load()),
                                    op=Add(),
                                    right=BinOp(
                                        left=BinOp(
                                            left=Constant(value='%%0%sd', kind=None),
                                            op=Mod(),
                                            right=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='padding',
                                                ctx=Load(),
                                            ),
                                        ),
                                        op=Mod(),
                                        right=Name(id='number_next', ctx=Load()),
                                    ),
                                ),
                                op=Add(),
                                right=Name(id='interpolated_suffix', ctx=Load()),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_create_date_range_seq',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='date', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='year', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='fields', ctx=Load()),
                                                attr='Date',
                                                ctx=Load(),
                                            ),
                                            attr='from_string',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='date', ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='strftime',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='%Y', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='date_from', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Constant(value='{}-01-01', kind=None),
                                    attr='format',
                                    ctx=Load(),
                                ),
                                args=[Name(id='year', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='date_to', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Constant(value='{}-12-31', kind=None),
                                    attr='format',
                                    ctx=Load(),
                                ),
                                args=[Name(id='year', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='date_range', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.sequence.date_range', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='sequence_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='date_from', kind=None),
                                                    Constant(value='>=', kind=None),
                                                    Name(id='date', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='date_from', kind=None),
                                                    Constant(value='<=', kind=None),
                                                    Name(id='date_to', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='order',
                                        value=Constant(value='date_from desc', kind=None),
                                    ),
                                    keyword(
                                        arg='limit',
                                        value=Constant(value=1, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='date_range', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='date_to', ctx=Store())],
                                    value=BinOp(
                                        left=Attribute(
                                            value=Name(id='date_range', ctx=Load()),
                                            attr='date_from',
                                            ctx=Load(),
                                        ),
                                        op=Add(),
                                        right=Call(
                                            func=Name(id='timedelta', ctx=Load()),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='days',
                                                    value=UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=1, kind=None),
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='date_range', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.sequence.date_range', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='sequence_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='date_to', kind=None),
                                                    Constant(value='>=', kind=None),
                                                    Name(id='date_from', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='date_to', kind=None),
                                                    Constant(value='<=', kind=None),
                                                    Name(id='date', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='order',
                                        value=Constant(value='date_to desc', kind=None),
                                    ),
                                    keyword(
                                        arg='limit',
                                        value=Constant(value=1, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='date_range', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='date_from', ctx=Store())],
                                    value=BinOp(
                                        left=Attribute(
                                            value=Name(id='date_range', ctx=Load()),
                                            attr='date_to',
                                            ctx=Load(),
                                        ),
                                        op=Add(),
                                        right=Call(
                                            func=Name(id='timedelta', ctx=Load()),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='days',
                                                    value=Constant(value=1, kind=None),
                                                ),
                                            ],
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='seq_date_range', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='ir.sequence.date_range', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='date_from', kind=None),
                                            Constant(value='date_to', kind=None),
                                            Constant(value='sequence_id', kind=None),
                                        ],
                                        values=[
                                            Name(id='date_from', ctx=Load()),
                                            Name(id='date_to', ctx=Load()),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='seq_date_range', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_next',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='sequence_date', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Returns the next number in the preferred sequence in all the ones given in self.', kind=None),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='use_date_range',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_next_do',
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
                            targets=[Name(id='dt', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='sequence_date', ctx=Load()),
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_context',
                                                ctx=Load(),
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='ir_sequence_date', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='fields', ctx=Load()),
                                                        attr='Date',
                                                        ctx=Load(),
                                                    ),
                                                    attr='today',
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
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='seq_date', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.sequence.date_range', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='sequence_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='date_from', kind=None),
                                                    Constant(value='<=', kind=None),
                                                    Name(id='dt', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='date_to', kind=None),
                                                    Constant(value='>=', kind=None),
                                                    Name(id='dt', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='limit',
                                        value=Constant(value=1, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='seq_date', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='seq_date', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_create_date_range_seq',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='dt', ctx=Load())],
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
                                        func=Attribute(
                                            value=Name(id='seq_date', ctx=Load()),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='ir_sequence_date_range',
                                                value=Attribute(
                                                    value=Name(id='seq_date', ctx=Load()),
                                                    attr='date_from',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    attr='_next',
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
                    name='next_by_id',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='sequence_date', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Draw an interpolated string using the specified sequence.', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='check_access_rights',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='read', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_next',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='sequence_date',
                                        value=Name(id='sequence_date', ctx=Load()),
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
                    name='next_by_code',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='sequence_code', annotation=None, type_comment=None),
                            arg(arg='sequence_date', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Draw an interpolated string using a sequence with the requested code.\n            If several sequences with the correct code are available to the user\n            (multi-company cases), the one from the user's current company will\n            be used.\n        ", kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='check_access_rights',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='read', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='company_id', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='company',
                                    ctx=Load(),
                                ),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='seq_ids', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='code', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Name(id='sequence_code', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='company_id', kind=None),
                                                    Constant(value='in', kind=None),
                                                    List(
                                                        elts=[
                                                            Name(id='company_id', ctx=Load()),
                                                            Constant(value=False, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='order',
                                        value=Constant(value='company_id', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='seq_ids', ctx=Load()),
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
                                            BinOp(
                                                left=Constant(value="No ir.sequence has been found for code '%s'. Please make sure a sequence is set for current company.", kind=None),
                                                op=Mod(),
                                                right=Name(id='sequence_code', ctx=Load()),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Return(
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='seq_id', ctx=Store())],
                            value=Subscript(
                                value=Name(id='seq_ids', ctx=Load()),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='seq_id', ctx=Load()),
                                    attr='_next',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='sequence_date',
                                        value=Name(id='sequence_date', ctx=Load()),
                                    ),
                                ],
                            ),
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
                FunctionDef(
                    name='get_id',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='sequence_code_or_id', annotation=None, type_comment=None),
                            arg(arg='code_or_id', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value='id', kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Draw an interpolated string using the specified sequence.\n\n        The sequence to use is specified by the ``sequence_code_or_id``\n        argument, which can be a code or an id (as controlled by the\n        ``code_or_id`` argument. This method is deprecated.\n        ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='warning',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='ir_sequence.get() and ir_sequence.get_id() are deprecated. Please use ir_sequence.next_by_code() or ir_sequence.next_by_id().', kind=None)],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Compare(
                                left=Name(id='code_or_id', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='id', kind=None)],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='browse',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='sequence_code_or_id', ctx=Load())],
                                                keywords=[],
                                            ),
                                            attr='next_by_id',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='next_by_code',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='sequence_code_or_id', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
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
                FunctionDef(
                    name='get',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='code', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Draw an interpolated string using the specified sequence.\n\n        The sequence to use is specified by its code. This method is\n        deprecated.\n        ', kind=None),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='get_id',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='code', ctx=Load()),
                                    Constant(value='code', kind=None),
                                ],
                                keywords=[],
                            ),
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
        ClassDef(
            name='IrSequenceDateRange',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='ir.sequence.date_range', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Sequence Date Range', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_rec_name', ctx=Store())],
                    value=Constant(value='sequence_id', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_number_next_actual',
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
                            value=Constant(value='Return number from ir_sequence row when no_gap implementation,\n        and number from postgres sequence when standard implementation.', kind=None),
                        ),
                        For(
                            target=Name(id='seq', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Attribute(
                                                value=Name(id='seq', ctx=Load()),
                                                attr='sequence_id',
                                                ctx=Load(),
                                            ),
                                            attr='implementation',
                                            ctx=Load(),
                                        ),
                                        ops=[NotEq()],
                                        comparators=[Constant(value='standard', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='seq', ctx=Load()),
                                                    attr='number_next_actual',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Attribute(
                                                value=Name(id='seq', ctx=Load()),
                                                attr='number_next',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='seq_id', ctx=Store())],
                                            value=BinOp(
                                                left=Constant(value='%03d_%03d', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Attribute(
                                                            value=Attribute(
                                                                value=Name(id='seq', ctx=Load()),
                                                                attr='sequence_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                        Attribute(
                                                            value=Name(id='seq', ctx=Load()),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='seq', ctx=Load()),
                                                    attr='number_next_actual',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Name(id='_predict_nextval', ctx=Load()),
                                                args=[
                                                    Name(id='self', ctx=Load()),
                                                    Name(id='seq_id', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
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
                    name='_set_number_next_actual',
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
                        For(
                            target=Name(id='seq', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='seq', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='number_next', kind=None)],
                                                values=[
                                                    BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='seq', ctx=Load()),
                                                                attr='number_next_actual',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=1, kind=None),
                                                        ],
                                                    ),
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
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='default_get',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='fields', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='IrSequenceDateRange', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='default_get',
                                    ctx=Load(),
                                ),
                                args=[Name(id='fields', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='result', ctx=Load()),
                                    slice=Constant(value='number_next_actual', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=1, kind=None),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='result', ctx=Load()),
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
                Assign(
                    targets=[Name(id='date_from', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Date',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='From', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='date_to', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Date',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='To', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='sequence_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='ir.sequence', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Main Sequence', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='ondelete',
                                value=Constant(value='cascade', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='number_next', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Next Number', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value=1, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Next number of this sequence', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='number_next_actual', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_get_number_next_actual', kind=None),
                            ),
                            keyword(
                                arg='inverse',
                                value=Constant(value='_set_number_next_actual', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Actual Next Number', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Next number that will be used. This number can be incremented frequently so the displayed value might already be obsolete', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_next',
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
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='sequence_id',
                                        ctx=Load(),
                                    ),
                                    attr='implementation',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='standard', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='number_next', ctx=Store())],
                                    value=Call(
                                        func=Name(id='_select_nextval', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_cr',
                                                ctx=Load(),
                                            ),
                                            BinOp(
                                                left=Constant(value='ir_sequence_%03d_%03d', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='sequence_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                        Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='id',
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
                                Assign(
                                    targets=[Name(id='number_next', ctx=Store())],
                                    value=Call(
                                        func=Name(id='_update_nogap', ctx=Load()),
                                        args=[
                                            Name(id='self', ctx=Load()),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='sequence_id',
                                                    ctx=Load(),
                                                ),
                                                attr='number_increment',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='sequence_id',
                                        ctx=Load(),
                                    ),
                                    attr='get_next_char',
                                    ctx=Load(),
                                ),
                                args=[Name(id='number_next', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_alter_sequence',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='number_increment', annotation=None, type_comment=None),
                            arg(arg='number_next', annotation=None, type_comment=None),
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
                        For(
                            target=Name(id='seq', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='_alter_sequence', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_cr',
                                                ctx=Load(),
                                            ),
                                            BinOp(
                                                left=Constant(value='ir_sequence_%03d_%03d', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Attribute(
                                                            value=Attribute(
                                                                value=Name(id='seq', ctx=Load()),
                                                                attr='sequence_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                        Attribute(
                                                            value=Name(id='seq', ctx=Load()),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='number_increment',
                                                value=Name(id='number_increment', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='number_next',
                                                value=Name(id='number_next', ctx=Load()),
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
                    name='create',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='values', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Create a sequence, in implementation == standard a fast gaps-allowed PostgreSQL sequence is used.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='seq', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='IrSequenceDateRange', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Name(id='values', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='main_seq', ctx=Store())],
                            value=Attribute(
                                value=Name(id='seq', ctx=Load()),
                                attr='sequence_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='main_seq', ctx=Load()),
                                    attr='implementation',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='standard', kind=None)],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='_create_sequence', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_cr',
                                                ctx=Load(),
                                            ),
                                            BinOp(
                                                left=Constant(value='ir_sequence_%03d_%03d', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Attribute(
                                                            value=Name(id='main_seq', ctx=Load()),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                        Attribute(
                                                            value=Name(id='seq', ctx=Load()),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                            Attribute(
                                                value=Name(id='main_seq', ctx=Load()),
                                                attr='number_increment',
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='values', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='number_next_actual', kind=None),
                                                    Constant(value=1, kind=None),
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
                        Return(
                            value=Name(id='seq', ctx=Load()),
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
                FunctionDef(
                    name='unlink',
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
                                func=Name(id='_drop_sequences', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_cr',
                                        ctx=Load(),
                                    ),
                                    ListComp(
                                        elt=BinOp(
                                            left=Constant(value='ir_sequence_%03d_%03d', kind=None),
                                            op=Mod(),
                                            right=Tuple(
                                                elts=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='x', ctx=Load()),
                                                            attr='sequence_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='x', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='x', ctx=Store()),
                                                iter=Name(id='self', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
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
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='IrSequenceDateRange', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='unlink',
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
                    name='write',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='values', annotation=None, type_comment=None),
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
                                func=Attribute(
                                    value=Name(id='values', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='number_next', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='seq_to_alter', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='filtered',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Lambda(
                                                args=arguments(
                                                    posonlyargs=[],
                                                    args=[arg(arg='seq', annotation=None, type_comment=None)],
                                                    vararg=None,
                                                    kwonlyargs=[],
                                                    kw_defaults=[],
                                                    kwarg=None,
                                                    defaults=[],
                                                ),
                                                body=Compare(
                                                    left=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='seq', ctx=Load()),
                                                            attr='sequence_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='implementation',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[Constant(value='standard', kind=None)],
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='seq_to_alter', ctx=Load()),
                                            attr='_alter_sequence',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='number_next',
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='values', ctx=Load()),
                                                        attr='get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='number_next', kind=None)],
                                                    keywords=[],
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='IrSequenceDateRange', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[Name(id='values', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='flush',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='values', ctx=Load()),
                                            attr='keys',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Name(id='res', ctx=Load()),
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
