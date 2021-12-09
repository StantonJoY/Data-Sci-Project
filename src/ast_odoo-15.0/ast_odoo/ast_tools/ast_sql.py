Module(
    body=[
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='psycopg2', asname=None)],
        ),
        Assign(
            targets=[Name(id='_schema', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='logging', ctx=Load()),
                    attr='getLogger',
                    ctx=Load(),
                ),
                args=[Constant(value='odoo.schema', kind=None)],
                keywords=[],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='_CONFDELTYPES', ctx=Store())],
            value=Dict(
                keys=[
                    Constant(value='RESTRICT', kind=None),
                    Constant(value='NO ACTION', kind=None),
                    Constant(value='CASCADE', kind=None),
                    Constant(value='SET NULL', kind=None),
                    Constant(value='SET DEFAULT', kind=None),
                ],
                values=[
                    Constant(value='r', kind=None),
                    Constant(value='a', kind=None),
                    Constant(value='c', kind=None),
                    Constant(value='n', kind=None),
                    Constant(value='d', kind=None),
                ],
            ),
            type_comment=None,
        ),
        FunctionDef(
            name='existing_tables',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='cr', annotation=None, type_comment=None),
                    arg(arg='tablenames', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Return the names of existing tables among ``tablenames``. ', kind=None),
                ),
                Assign(
                    targets=[Name(id='query', ctx=Store())],
                    value=Constant(value="\n        SELECT c.relname\n          FROM pg_class c\n          JOIN pg_namespace n ON (n.oid = c.relnamespace)\n         WHERE c.relname IN %s\n           AND c.relkind IN ('r', 'v', 'm')\n           AND n.nspname = current_schema\n    ", kind=None),
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
                            Name(id='query', ctx=Load()),
                            List(
                                elts=[
                                    Call(
                                        func=Name(id='tuple', ctx=Load()),
                                        args=[Name(id='tablenames', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                ),
                Return(
                    value=ListComp(
                        elt=Subscript(
                            value=Name(id='row', ctx=Load()),
                            slice=Constant(value=0, kind=None),
                            ctx=Load(),
                        ),
                        generators=[
                            comprehension(
                                target=Name(id='row', ctx=Store()),
                                iter=Call(
                                    func=Attribute(
                                        value=Name(id='cr', ctx=Load()),
                                        attr='fetchall',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                ifs=[],
                                is_async=0,
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
            name='table_exists',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='cr', annotation=None, type_comment=None),
                    arg(arg='tablename', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Return whether the given table exists. ', kind=None),
                ),
                Return(
                    value=Compare(
                        left=Call(
                            func=Name(id='len', ctx=Load()),
                            args=[
                                Call(
                                    func=Name(id='existing_tables', ctx=Load()),
                                    args=[
                                        Name(id='cr', ctx=Load()),
                                        Set(
                                            elts=[Name(id='tablename', ctx=Load())],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                            ],
                            keywords=[],
                        ),
                        ops=[Eq()],
                        comparators=[Constant(value=1, kind=None)],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='table_kind',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='cr', annotation=None, type_comment=None),
                    arg(arg='tablename', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=" Return the kind of a table: ``'r'`` (regular table), ``'v'`` (view),\n        ``'f'`` (foreign table), ``'t'`` (temporary table),\n        ``'m'`` (materialized view), or ``None``.\n    ", kind=None),
                ),
                Assign(
                    targets=[Name(id='query', ctx=Store())],
                    value=Constant(value='\n        SELECT c.relkind\n          FROM pg_class c\n          JOIN pg_namespace n ON (n.oid = c.relnamespace)\n         WHERE c.relname = %s\n           AND n.nspname = current_schema\n    ', kind=None),
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
                            Name(id='query', ctx=Load()),
                            Tuple(
                                elts=[Name(id='tablename', ctx=Load())],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                ),
                Return(
                    value=IfExp(
                        test=Attribute(
                            value=Name(id='cr', ctx=Load()),
                            attr='rowcount',
                            ctx=Load(),
                        ),
                        body=Subscript(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cr', ctx=Load()),
                                    attr='fetchone',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            slice=Constant(value=0, kind=None),
                            ctx=Load(),
                        ),
                        orelse=Constant(value=None, kind=None),
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='create_model_table',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='cr', annotation=None, type_comment=None),
                    arg(arg='tablename', annotation=None, type_comment=None),
                    arg(arg='comment', annotation=None, type_comment=None),
                    arg(arg='columns', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    Constant(value=None, kind=None),
                    Tuple(elts=[], ctx=Load()),
                ],
            ),
            body=[
                Expr(
                    value=Constant(value=' Create the table for a model. ', kind=None),
                ),
                Assign(
                    targets=[Name(id='colspecs', ctx=Store())],
                    value=BinOp(
                        left=List(
                            elts=[Constant(value='id SERIAL NOT NULL', kind=None)],
                            ctx=Load(),
                        ),
                        op=Add(),
                        right=ListComp(
                            elt=Call(
                                func=Attribute(
                                    value=Constant(value='"{}" {}', kind=None),
                                    attr='format',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='columnname', ctx=Load()),
                                    Name(id='columntype', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            generators=[
                                comprehension(
                                    target=Tuple(
                                        elts=[
                                            Name(id='columnname', ctx=Store()),
                                            Name(id='columntype', ctx=Store()),
                                            Name(id='columncomment', ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                    iter=Name(id='columns', ctx=Load()),
                                    ifs=[],
                                    is_async=0,
                                ),
                            ],
                        ),
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
                                    value=Constant(value='CREATE TABLE "{}" ({}, PRIMARY KEY(id))', kind=None),
                                    attr='format',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='tablename', ctx=Load()),
                                    Call(
                                        func=Attribute(
                                            value=Constant(value=', ', kind=None),
                                            attr='join',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='colspecs', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ],
                        keywords=[],
                    ),
                ),
                Assign(
                    targets=[
                        Tuple(
                            elts=[
                                Name(id='queries', ctx=Store()),
                                Name(id='params', ctx=Store()),
                            ],
                            ctx=Store(),
                        ),
                    ],
                    value=Tuple(
                        elts=[
                            List(elts=[], ctx=Load()),
                            List(elts=[], ctx=Load()),
                        ],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                If(
                    test=Name(id='comment', ctx=Load()),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='queries', ctx=Load()),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Constant(value='COMMENT ON TABLE "{}" IS %s', kind=None),
                                            attr='format',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='tablename', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='params', ctx=Load()),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[Name(id='comment', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                For(
                    target=Tuple(
                        elts=[
                            Name(id='columnname', ctx=Store()),
                            Name(id='columntype', ctx=Store()),
                            Name(id='columncomment', ctx=Store()),
                        ],
                        ctx=Store(),
                    ),
                    iter=Name(id='columns', ctx=Load()),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='queries', ctx=Load()),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Constant(value='COMMENT ON COLUMN "{}"."{}" IS %s', kind=None),
                                            attr='format',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='tablename', ctx=Load()),
                                            Name(id='columnname', ctx=Load()),
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
                                    value=Name(id='params', ctx=Load()),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[Name(id='columncomment', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[],
                    type_comment=None,
                ),
                If(
                    test=Name(id='queries', ctx=Load()),
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
                                            value=Constant(value='; ', kind=None),
                                            attr='join',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='queries', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Name(id='params', ctx=Load()),
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
                            value=Name(id='_schema', ctx=Load()),
                            attr='debug',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='Table %r: created', kind=None),
                            Name(id='tablename', ctx=Load()),
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
            name='table_columns',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='cr', annotation=None, type_comment=None),
                    arg(arg='tablename', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Return a dict mapping column names to their configuration. The latter is\n        a dict with the data from the table ``information_schema.columns``.\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='query', ctx=Store())],
                    value=Constant(value='SELECT column_name, udt_name, character_maximum_length, is_nullable\n               FROM information_schema.columns WHERE table_name=%s', kind=None),
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
                            Name(id='query', ctx=Load()),
                            Tuple(
                                elts=[Name(id='tablename', ctx=Load())],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                ),
                Return(
                    value=DictComp(
                        key=Subscript(
                            value=Name(id='row', ctx=Load()),
                            slice=Constant(value='column_name', kind=None),
                            ctx=Load(),
                        ),
                        value=Name(id='row', ctx=Load()),
                        generators=[
                            comprehension(
                                target=Name(id='row', ctx=Store()),
                                iter=Call(
                                    func=Attribute(
                                        value=Name(id='cr', ctx=Load()),
                                        attr='dictfetchall',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                ifs=[],
                                is_async=0,
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
            name='column_exists',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='cr', annotation=None, type_comment=None),
                    arg(arg='tablename', annotation=None, type_comment=None),
                    arg(arg='columnname', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Return whether the given column exists. ', kind=None),
                ),
                Assign(
                    targets=[Name(id='query', ctx=Store())],
                    value=Constant(value=' SELECT 1 FROM information_schema.columns\n                WHERE table_name=%s AND column_name=%s ', kind=None),
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
                            Name(id='query', ctx=Load()),
                            Tuple(
                                elts=[
                                    Name(id='tablename', ctx=Load()),
                                    Name(id='columnname', ctx=Load()),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                ),
                Return(
                    value=Attribute(
                        value=Name(id='cr', ctx=Load()),
                        attr='rowcount',
                        ctx=Load(),
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='create_column',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='cr', annotation=None, type_comment=None),
                    arg(arg='tablename', annotation=None, type_comment=None),
                    arg(arg='columnname', annotation=None, type_comment=None),
                    arg(arg='columntype', annotation=None, type_comment=None),
                    arg(arg='comment', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[Constant(value=None, kind=None)],
            ),
            body=[
                Expr(
                    value=Constant(value=' Create a column with the given type. ', kind=None),
                ),
                Assign(
                    targets=[Name(id='coldefault', ctx=Store())],
                    value=BoolOp(
                        op=Or(),
                        values=[
                            BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Call(
                                            func=Attribute(
                                                value=Name(id='columntype', ctx=Load()),
                                                attr='upper',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='BOOLEAN', kind=None)],
                                    ),
                                    Constant(value='DEFAULT false', kind=None),
                                ],
                            ),
                            Constant(value='', kind=None),
                        ],
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
                                    value=Constant(value='ALTER TABLE "{}" ADD COLUMN "{}" {} {}', kind=None),
                                    attr='format',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='tablename', ctx=Load()),
                                    Name(id='columnname', ctx=Load()),
                                    Name(id='columntype', ctx=Load()),
                                    Name(id='coldefault', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ],
                        keywords=[],
                    ),
                ),
                If(
                    test=Name(id='comment', ctx=Load()),
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
                                            value=Constant(value='COMMENT ON COLUMN "{}"."{}" IS %s', kind=None),
                                            attr='format',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='tablename', ctx=Load()),
                                            Name(id='columnname', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    Tuple(
                                        elts=[Name(id='comment', ctx=Load())],
                                        ctx=Load(),
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
                            value=Name(id='_schema', ctx=Load()),
                            attr='debug',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='Table %r: added column %r of type %s', kind=None),
                            Name(id='tablename', ctx=Load()),
                            Name(id='columnname', ctx=Load()),
                            Name(id='columntype', ctx=Load()),
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
            name='rename_column',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='cr', annotation=None, type_comment=None),
                    arg(arg='tablename', annotation=None, type_comment=None),
                    arg(arg='columnname1', annotation=None, type_comment=None),
                    arg(arg='columnname2', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Rename the given column. ', kind=None),
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
                                    value=Constant(value='ALTER TABLE "{}" RENAME COLUMN "{}" TO "{}"', kind=None),
                                    attr='format',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='tablename', ctx=Load()),
                                    Name(id='columnname1', ctx=Load()),
                                    Name(id='columnname2', ctx=Load()),
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
                            value=Name(id='_schema', ctx=Load()),
                            attr='debug',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='Table %r: renamed column %r to %r', kind=None),
                            Name(id='tablename', ctx=Load()),
                            Name(id='columnname1', ctx=Load()),
                            Name(id='columnname2', ctx=Load()),
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
            name='convert_column',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='cr', annotation=None, type_comment=None),
                    arg(arg='tablename', annotation=None, type_comment=None),
                    arg(arg='columnname', annotation=None, type_comment=None),
                    arg(arg='columntype', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Convert the column to the given type. ', kind=None),
                ),
                Try(
                    body=[
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='cr', ctx=Load()),
                                            attr='savepoint',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='flush',
                                                value=Constant(value=False, kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
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
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Constant(value='ALTER TABLE "{}" ALTER COLUMN "{}" TYPE {}', kind=None),
                                                    attr='format',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='tablename', ctx=Load()),
                                                    Name(id='columnname', ctx=Load()),
                                                    Name(id='columntype', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='log_exceptions',
                                                value=Constant(value=False, kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    handlers=[
                        ExceptHandler(
                            type=Attribute(
                                value=Name(id='psycopg2', ctx=Load()),
                                attr='NotSupportedError',
                                ctx=Load(),
                            ),
                            name=None,
                            body=[
                                Assign(
                                    targets=[Name(id='query', ctx=Store())],
                                    value=Constant(value='\n            ALTER TABLE "{0}" RENAME COLUMN "{1}" TO __temp_type_cast;\n            ALTER TABLE "{0}" ADD COLUMN "{1}" {2};\n            UPDATE "{0}" SET "{1}"= __temp_type_cast::{2};\n            ALTER TABLE "{0}" DROP COLUMN  __temp_type_cast CASCADE;\n        ', kind=None),
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
                                                    value=Name(id='query', ctx=Load()),
                                                    attr='format',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='tablename', ctx=Load()),
                                                    Name(id='columnname', ctx=Load()),
                                                    Name(id='columntype', ctx=Load()),
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
                    finalbody=[],
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='_schema', ctx=Load()),
                            attr='debug',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='Table %r: column %r changed to type %s', kind=None),
                            Name(id='tablename', ctx=Load()),
                            Name(id='columnname', ctx=Load()),
                            Name(id='columntype', ctx=Load()),
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
            name='set_not_null',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='cr', annotation=None, type_comment=None),
                    arg(arg='tablename', annotation=None, type_comment=None),
                    arg(arg='columnname', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Add a NOT NULL constraint on the given column. ', kind=None),
                ),
                Assign(
                    targets=[Name(id='query', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Constant(value='ALTER TABLE "{}" ALTER COLUMN "{}" SET NOT NULL', kind=None),
                            attr='format',
                            ctx=Load(),
                        ),
                        args=[
                            Name(id='tablename', ctx=Load()),
                            Name(id='columnname', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Try(
                    body=[
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='cr', ctx=Load()),
                                            attr='savepoint',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='flush',
                                                value=Constant(value=False, kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
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
                                        args=[Name(id='query', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='log_exceptions',
                                                value=Constant(value=False, kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_schema', ctx=Load()),
                                            attr='debug',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='Table %r: column %r: added constraint NOT NULL', kind=None),
                                            Name(id='tablename', ctx=Load()),
                                            Name(id='columnname', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
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
                                Raise(
                                    exc=Call(
                                        func=Name(id='Exception', ctx=Load()),
                                        args=[
                                            Constant(value='Table %r: unable to set NOT NULL on column %r', kind=None),
                                            Name(id='tablename', ctx=Load()),
                                            Name(id='columnname', ctx=Load()),
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
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='drop_not_null',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='cr', annotation=None, type_comment=None),
                    arg(arg='tablename', annotation=None, type_comment=None),
                    arg(arg='columnname', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Drop the NOT NULL constraint on the given column. ', kind=None),
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
                                    value=Constant(value='ALTER TABLE "{}" ALTER COLUMN "{}" DROP NOT NULL', kind=None),
                                    attr='format',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='tablename', ctx=Load()),
                                    Name(id='columnname', ctx=Load()),
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
                            value=Name(id='_schema', ctx=Load()),
                            attr='debug',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='Table %r: column %r: dropped constraint NOT NULL', kind=None),
                            Name(id='tablename', ctx=Load()),
                            Name(id='columnname', ctx=Load()),
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
            name='constraint_definition',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='cr', annotation=None, type_comment=None),
                    arg(arg='tablename', annotation=None, type_comment=None),
                    arg(arg='constraintname', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=" Return the given constraint's definition. ", kind=None),
                ),
                Assign(
                    targets=[Name(id='query', ctx=Store())],
                    value=Constant(value='\n        SELECT COALESCE(d.description, pg_get_constraintdef(c.oid))\n        FROM pg_constraint c\n        JOIN pg_class t ON t.oid = c.conrelid\n        LEFT JOIN pg_description d ON c.oid = d.objoid\n        WHERE t.relname = %s AND conname = %s;', kind=None),
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
                            Name(id='query', ctx=Load()),
                            Tuple(
                                elts=[
                                    Name(id='tablename', ctx=Load()),
                                    Name(id='constraintname', ctx=Load()),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                ),
                Return(
                    value=IfExp(
                        test=Attribute(
                            value=Name(id='cr', ctx=Load()),
                            attr='rowcount',
                            ctx=Load(),
                        ),
                        body=Subscript(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cr', ctx=Load()),
                                    attr='fetchone',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            slice=Constant(value=0, kind=None),
                            ctx=Load(),
                        ),
                        orelse=Constant(value=None, kind=None),
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='add_constraint',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='cr', annotation=None, type_comment=None),
                    arg(arg='tablename', annotation=None, type_comment=None),
                    arg(arg='constraintname', annotation=None, type_comment=None),
                    arg(arg='definition', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Add a constraint on the given table. ', kind=None),
                ),
                Assign(
                    targets=[Name(id='query1', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Constant(value='ALTER TABLE "{}" ADD CONSTRAINT "{}" {}', kind=None),
                            attr='format',
                            ctx=Load(),
                        ),
                        args=[
                            Name(id='tablename', ctx=Load()),
                            Name(id='constraintname', ctx=Load()),
                            Name(id='definition', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='query2', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Constant(value='COMMENT ON CONSTRAINT "{}" ON "{}" IS %s', kind=None),
                            attr='format',
                            ctx=Load(),
                        ),
                        args=[
                            Name(id='constraintname', ctx=Load()),
                            Name(id='tablename', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Try(
                    body=[
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='cr', ctx=Load()),
                                            attr='savepoint',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='flush',
                                                value=Constant(value=False, kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
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
                                        args=[Name(id='query1', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='log_exceptions',
                                                value=Constant(value=False, kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='cr', ctx=Load()),
                                            attr='execute',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='query2', ctx=Load()),
                                            Tuple(
                                                elts=[Name(id='definition', ctx=Load())],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='log_exceptions',
                                                value=Constant(value=False, kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_schema', ctx=Load()),
                                            attr='debug',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='Table %r: added constraint %r as %s', kind=None),
                                            Name(id='tablename', ctx=Load()),
                                            Name(id='constraintname', ctx=Load()),
                                            Name(id='definition', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
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
                                Raise(
                                    exc=Call(
                                        func=Name(id='Exception', ctx=Load()),
                                        args=[
                                            Constant(value='Table %r: unable to add constraint %r as %s', kind=None),
                                            Name(id='tablename', ctx=Load()),
                                            Name(id='constraintname', ctx=Load()),
                                            Name(id='definition', ctx=Load()),
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
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='drop_constraint',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='cr', annotation=None, type_comment=None),
                    arg(arg='tablename', annotation=None, type_comment=None),
                    arg(arg='constraintname', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' drop the given constraint. ', kind=None),
                ),
                Try(
                    body=[
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='cr', ctx=Load()),
                                            attr='savepoint',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='flush',
                                                value=Constant(value=False, kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
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
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Constant(value='ALTER TABLE "{}" DROP CONSTRAINT "{}"', kind=None),
                                                    attr='format',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='tablename', ctx=Load()),
                                                    Name(id='constraintname', ctx=Load()),
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
                                            value=Name(id='_schema', ctx=Load()),
                                            attr='debug',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='Table %r: dropped constraint %r', kind=None),
                                            Name(id='tablename', ctx=Load()),
                                            Name(id='constraintname', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
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
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_schema', ctx=Load()),
                                            attr='warning',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='Table %r: unable to drop constraint %r!', kind=None),
                                            Name(id='tablename', ctx=Load()),
                                            Name(id='constraintname', ctx=Load()),
                                        ],
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
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='add_foreign_key',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='cr', annotation=None, type_comment=None),
                    arg(arg='tablename1', annotation=None, type_comment=None),
                    arg(arg='columnname1', annotation=None, type_comment=None),
                    arg(arg='tablename2', annotation=None, type_comment=None),
                    arg(arg='columnname2', annotation=None, type_comment=None),
                    arg(arg='ondelete', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Create the given foreign key, and return ``True``. ', kind=None),
                ),
                Assign(
                    targets=[Name(id='query', ctx=Store())],
                    value=Constant(value='ALTER TABLE "{}" ADD FOREIGN KEY ("{}") REFERENCES "{}"("{}") ON DELETE {}', kind=None),
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
                                    value=Name(id='query', ctx=Load()),
                                    attr='format',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='tablename1', ctx=Load()),
                                    Name(id='columnname1', ctx=Load()),
                                    Name(id='tablename2', ctx=Load()),
                                    Name(id='columnname2', ctx=Load()),
                                    Name(id='ondelete', ctx=Load()),
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
                            value=Name(id='_schema', ctx=Load()),
                            attr='debug',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='Table %r: added foreign key %r references %r(%r) ON DELETE %s', kind=None),
                            Name(id='tablename1', ctx=Load()),
                            Name(id='columnname1', ctx=Load()),
                            Name(id='tablename2', ctx=Load()),
                            Name(id='columnname2', ctx=Load()),
                            Name(id='ondelete', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                ),
                Return(
                    value=Constant(value=True, kind=None),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='get_foreign_keys',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='cr', annotation=None, type_comment=None),
                    arg(arg='tablename1', annotation=None, type_comment=None),
                    arg(arg='columnname1', annotation=None, type_comment=None),
                    arg(arg='tablename2', annotation=None, type_comment=None),
                    arg(arg='columnname2', annotation=None, type_comment=None),
                    arg(arg='ondelete', annotation=None, type_comment=None),
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
                            Constant(value="\n            SELECT fk.conname as name\n            FROM pg_constraint AS fk\n            JOIN pg_class AS c1 ON fk.conrelid = c1.oid\n            JOIN pg_class AS c2 ON fk.confrelid = c2.oid\n            JOIN pg_attribute AS a1 ON a1.attrelid = c1.oid AND fk.conkey[1] = a1.attnum\n            JOIN pg_attribute AS a2 ON a2.attrelid = c2.oid AND fk.confkey[1] = a2.attnum\n            WHERE fk.contype = 'f'\n            AND c1.relname = %s\n            AND a1.attname = %s\n            AND c2.relname = %s\n            AND a2.attname = %s\n            AND fk.confdeltype = %s\n        ", kind=None),
                            List(
                                elts=[
                                    Name(id='tablename1', ctx=Load()),
                                    Name(id='columnname1', ctx=Load()),
                                    Name(id='tablename2', ctx=Load()),
                                    Name(id='columnname2', ctx=Load()),
                                    Subscript(
                                        value=Name(id='_CONFDELTYPES', ctx=Load()),
                                        slice=Call(
                                            func=Attribute(
                                                value=Name(id='ondelete', ctx=Load()),
                                                attr='upper',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
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
                    value=ListComp(
                        elt=Subscript(
                            value=Name(id='r', ctx=Load()),
                            slice=Constant(value=0, kind=None),
                            ctx=Load(),
                        ),
                        generators=[
                            comprehension(
                                target=Name(id='r', ctx=Store()),
                                iter=Call(
                                    func=Attribute(
                                        value=Name(id='cr', ctx=Load()),
                                        attr='fetchall',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                ifs=[],
                                is_async=0,
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
            name='fix_foreign_key',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='cr', annotation=None, type_comment=None),
                    arg(arg='tablename1', annotation=None, type_comment=None),
                    arg(arg='columnname1', annotation=None, type_comment=None),
                    arg(arg='tablename2', annotation=None, type_comment=None),
                    arg(arg='columnname2', annotation=None, type_comment=None),
                    arg(arg='ondelete', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Update the foreign keys between tables to match the given one, and\n        return ``True`` if the given foreign key has been recreated.\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='deltype', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='_CONFDELTYPES', ctx=Load()),
                            attr='get',
                            ctx=Load(),
                        ),
                        args=[
                            Call(
                                func=Attribute(
                                    value=Name(id='ondelete', ctx=Load()),
                                    attr='upper',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            Constant(value='a', kind=None),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='query', ctx=Store())],
                    value=Constant(value=" SELECT con.conname, c2.relname, a2.attname, con.confdeltype as deltype\n                  FROM pg_constraint as con, pg_class as c1, pg_class as c2,\n                       pg_attribute as a1, pg_attribute as a2\n                 WHERE con.contype='f' AND con.conrelid=c1.oid AND con.confrelid=c2.oid\n                   AND array_lower(con.conkey, 1)=1 AND con.conkey[1]=a1.attnum\n                   AND array_lower(con.confkey, 1)=1 AND con.confkey[1]=a2.attnum\n                   AND a1.attrelid=c1.oid AND a2.attrelid=c2.oid\n                   AND c1.relname=%s AND a1.attname=%s ", kind=None),
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
                            Name(id='query', ctx=Load()),
                            Tuple(
                                elts=[
                                    Name(id='tablename1', ctx=Load()),
                                    Name(id='columnname1', ctx=Load()),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                ),
                Assign(
                    targets=[Name(id='found', ctx=Store())],
                    value=Constant(value=False, kind=None),
                    type_comment=None,
                ),
                For(
                    target=Name(id='fk', ctx=Store()),
                    iter=Call(
                        func=Attribute(
                            value=Name(id='cr', ctx=Load()),
                            attr='fetchall',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    body=[
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='found', ctx=Load()),
                                    ),
                                    Compare(
                                        left=Subscript(
                                            value=Name(id='fk', ctx=Load()),
                                            slice=Slice(
                                                lower=Constant(value=1, kind=None),
                                                upper=None,
                                                step=None,
                                            ),
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[
                                            Tuple(
                                                elts=[
                                                    Name(id='tablename2', ctx=Load()),
                                                    Name(id='columnname2', ctx=Load()),
                                                    Name(id='deltype', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='found', ctx=Store())],
                                    value=Constant(value=True, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Expr(
                                    value=Call(
                                        func=Name(id='drop_constraint', ctx=Load()),
                                        args=[
                                            Name(id='cr', ctx=Load()),
                                            Name(id='tablename1', ctx=Load()),
                                            Subscript(
                                                value=Name(id='fk', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
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
                If(
                    test=UnaryOp(
                        op=Not(),
                        operand=Name(id='found', ctx=Load()),
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Name(id='add_foreign_key', ctx=Load()),
                                args=[
                                    Name(id='cr', ctx=Load()),
                                    Name(id='tablename1', ctx=Load()),
                                    Name(id='columnname1', ctx=Load()),
                                    Name(id='tablename2', ctx=Load()),
                                    Name(id='columnname2', ctx=Load()),
                                    Name(id='ondelete', ctx=Load()),
                                ],
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
            name='index_exists',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='cr', annotation=None, type_comment=None),
                    arg(arg='indexname', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Return whether the given index exists. ', kind=None),
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='cr', ctx=Load()),
                            attr='execute',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='SELECT 1 FROM pg_indexes WHERE indexname=%s', kind=None),
                            Tuple(
                                elts=[Name(id='indexname', ctx=Load())],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                ),
                Return(
                    value=Attribute(
                        value=Name(id='cr', ctx=Load()),
                        attr='rowcount',
                        ctx=Load(),
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='create_index',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='cr', annotation=None, type_comment=None),
                    arg(arg='indexname', annotation=None, type_comment=None),
                    arg(arg='tablename', annotation=None, type_comment=None),
                    arg(arg='expressions', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Create the given index unless it exists. ', kind=None),
                ),
                If(
                    test=Call(
                        func=Name(id='index_exists', ctx=Load()),
                        args=[
                            Name(id='cr', ctx=Load()),
                            Name(id='indexname', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    body=[Return(value=None)],
                    orelse=[],
                ),
                Assign(
                    targets=[Name(id='args', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Constant(value=', ', kind=None),
                            attr='join',
                            ctx=Load(),
                        ),
                        args=[Name(id='expressions', ctx=Load())],
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
                                    value=Constant(value='CREATE INDEX "{}" ON "{}" ({})', kind=None),
                                    attr='format',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='indexname', ctx=Load()),
                                    Name(id='tablename', ctx=Load()),
                                    Name(id='args', ctx=Load()),
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
                            value=Name(id='_schema', ctx=Load()),
                            attr='debug',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='Table %r: created index %r (%s)', kind=None),
                            Name(id='tablename', ctx=Load()),
                            Name(id='indexname', ctx=Load()),
                            Name(id='args', ctx=Load()),
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
            name='create_unique_index',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='cr', annotation=None, type_comment=None),
                    arg(arg='indexname', annotation=None, type_comment=None),
                    arg(arg='tablename', annotation=None, type_comment=None),
                    arg(arg='expressions', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Create the given index unless it exists. ', kind=None),
                ),
                If(
                    test=Call(
                        func=Name(id='index_exists', ctx=Load()),
                        args=[
                            Name(id='cr', ctx=Load()),
                            Name(id='indexname', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    body=[Return(value=None)],
                    orelse=[],
                ),
                Assign(
                    targets=[Name(id='args', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Constant(value=', ', kind=None),
                            attr='join',
                            ctx=Load(),
                        ),
                        args=[Name(id='expressions', ctx=Load())],
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
                                    value=Constant(value='CREATE UNIQUE INDEX "{}" ON "{}" ({})', kind=None),
                                    attr='format',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='indexname', ctx=Load()),
                                    Name(id='tablename', ctx=Load()),
                                    Name(id='args', ctx=Load()),
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
                            value=Name(id='_schema', ctx=Load()),
                            attr='debug',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='Table %r: created index %r (%s)', kind=None),
                            Name(id='tablename', ctx=Load()),
                            Name(id='indexname', ctx=Load()),
                            Name(id='args', ctx=Load()),
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
            name='drop_index',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='cr', annotation=None, type_comment=None),
                    arg(arg='indexname', annotation=None, type_comment=None),
                    arg(arg='tablename', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Drop the given index if it exists. ', kind=None),
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
                                    value=Constant(value='DROP INDEX IF EXISTS "{}"', kind=None),
                                    attr='format',
                                    ctx=Load(),
                                ),
                                args=[Name(id='indexname', ctx=Load())],
                                keywords=[],
                            ),
                        ],
                        keywords=[],
                    ),
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='_schema', ctx=Load()),
                            attr='debug',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='Table %r: dropped index %r', kind=None),
                            Name(id='tablename', ctx=Load()),
                            Name(id='indexname', ctx=Load()),
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
            name='drop_view_if_exists',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='cr', annotation=None, type_comment=None),
                    arg(arg='viewname', annotation=None, type_comment=None),
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
                            BinOp(
                                left=Constant(value='DROP view IF EXISTS %s CASCADE', kind=None),
                                op=Mod(),
                                right=Tuple(
                                    elts=[Name(id='viewname', ctx=Load())],
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
        FunctionDef(
            name='escape_psql',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='to_escape', annotation=None, type_comment=None)],
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
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='to_escape', ctx=Load()),
                                            attr='replace',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='\\', kind=None),
                                            Constant(value='\\\\', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='replace',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='%', kind=None),
                                    Constant(value='\\%', kind=None),
                                ],
                                keywords=[],
                            ),
                            attr='replace',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='_', kind=None),
                            Constant(value='\\_', kind=None),
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
            name='pg_varchar',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='size', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[Constant(value=0, kind=None)],
            ),
            body=[
                Expr(
                    value=Constant(value=" Returns the VARCHAR declaration for the provided size:\n\n    * If no size (or an empty or negative size is provided) return an\n      'infinite' VARCHAR\n    * Otherwise return a VARCHAR(n)\n\n    :type int size: varchar size, optional\n    :rtype: str\n    ", kind=None),
                ),
                If(
                    test=Name(id='size', ctx=Load()),
                    body=[
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Name(id='isinstance', ctx=Load()),
                                    args=[
                                        Name(id='size', ctx=Load()),
                                        Name(id='int', ctx=Load()),
                                    ],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='ValueError', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Constant(value='VARCHAR parameter should be an int, got %s', kind=None),
                                                op=Mod(),
                                                right=Call(
                                                    func=Name(id='type', ctx=Load()),
                                                    args=[Name(id='size', ctx=Load())],
                                                    keywords=[],
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
                        If(
                            test=Compare(
                                left=Name(id='size', ctx=Load()),
                                ops=[Gt()],
                                comparators=[Constant(value=0, kind=None)],
                            ),
                            body=[
                                Return(
                                    value=BinOp(
                                        left=Constant(value='VARCHAR(%d)', kind=None),
                                        op=Mod(),
                                        right=Name(id='size', ctx=Load()),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Constant(value='VARCHAR', kind=None),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='reverse_order',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='order', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Reverse an ORDER BY clause ', kind=None),
                ),
                Assign(
                    targets=[Name(id='items', ctx=Store())],
                    value=List(elts=[], ctx=Load()),
                    type_comment=None,
                ),
                For(
                    target=Name(id='item', ctx=Store()),
                    iter=Call(
                        func=Attribute(
                            value=Name(id='order', ctx=Load()),
                            attr='split',
                            ctx=Load(),
                        ),
                        args=[Constant(value=',', kind=None)],
                        keywords=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='item', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='item', ctx=Load()),
                                            attr='lower',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='split',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='direction', ctx=Store())],
                            value=IfExp(
                                test=Compare(
                                    left=Subscript(
                                        value=Name(id='item', ctx=Load()),
                                        slice=Slice(
                                            lower=Constant(value=1, kind=None),
                                            upper=None,
                                            step=None,
                                        ),
                                        ctx=Load(),
                                    ),
                                    ops=[Eq()],
                                    comparators=[
                                        List(
                                            elts=[Constant(value='desc', kind=None)],
                                            ctx=Load(),
                                        ),
                                    ],
                                ),
                                body=Constant(value='asc', kind=None),
                                orelse=Constant(value='desc', kind=None),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='items', ctx=Load()),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Constant(value='%s %s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Subscript(
                                                    value=Name(id='item', ctx=Load()),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                                Name(id='direction', ctx=Load()),
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
                Return(
                    value=Call(
                        func=Attribute(
                            value=Constant(value=', ', kind=None),
                            attr='join',
                            ctx=Load(),
                        ),
                        args=[Name(id='items', ctx=Load())],
                        keywords=[],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='increment_field_skiplock',
            args=arguments(
                posonlyargs=[],
                args=[
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
                    value=Constant(value="\n        Increment 'friendly' the [field] of the current [record](s)\n        If record is locked, we just skip the update.\n        It doesn't invalidate the cache since the update is not critical.\n\n        :rtype: bool - if field has been incremented or not\n    ", kind=None),
                ),
                If(
                    test=UnaryOp(
                        op=Not(),
                        operand=Name(id='record', ctx=Load()),
                    ),
                    body=[
                        Return(
                            value=Constant(value=False, kind=None),
                        ),
                    ],
                    orelse=[],
                ),
                Assert(
                    test=Compare(
                        left=Attribute(
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='record', ctx=Load()),
                                    attr='_fields',
                                    ctx=Load(),
                                ),
                                slice=Name(id='field', ctx=Load()),
                                ctx=Load(),
                            ),
                            attr='type',
                            ctx=Load(),
                        ),
                        ops=[Eq()],
                        comparators=[Constant(value='integer', kind=None)],
                    ),
                    msg=None,
                ),
                Assign(
                    targets=[Name(id='cr', ctx=Store())],
                    value=Attribute(
                        value=Name(id='record', ctx=Load()),
                        attr='_cr',
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='query', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Constant(value='\n        UPDATE {table} SET {field} = {field} + 1 WHERE id IN (\n            SELECT id from {table} WHERE id in %(ids)s FOR UPDATE SKIP LOCKED\n        ) RETURNING id\n    ', kind=None),
                            attr='format',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='table',
                                value=Attribute(
                                    value=Name(id='record', ctx=Load()),
                                    attr='_table',
                                    ctx=Load(),
                                ),
                            ),
                            keyword(
                                arg='field',
                                value=Name(id='field', ctx=Load()),
                            ),
                        ],
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
                            Name(id='query', ctx=Load()),
                            Dict(
                                keys=[Constant(value='ids', kind=None)],
                                values=[
                                    Call(
                                        func=Name(id='tuple', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='record', ctx=Load()),
                                                attr='ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                        ],
                        keywords=[],
                    ),
                ),
                Return(
                    value=Call(
                        func=Name(id='bool', ctx=Load()),
                        args=[
                            Call(
                                func=Attribute(
                                    value=Name(id='cr', ctx=Load()),
                                    attr='fetchone',
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
