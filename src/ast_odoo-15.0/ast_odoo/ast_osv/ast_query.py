Module(
    body=[
        Import(
            names=[alias(name='re', asname=None)],
        ),
        Import(
            names=[alias(name='warnings', asname=None)],
        ),
        ImportFrom(
            module='zlib',
            names=[alias(name='crc32', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[alias(name='lazy_property', asname=None)],
            level=0,
        ),
        Assign(
            targets=[Name(id='IDENT_RE', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='re', ctx=Load()),
                    attr='compile',
                    ctx=Load(),
                ),
                args=[
                    Constant(value='^[a-z_][a-z0-9_$]*$', kind=None),
                    Attribute(
                        value=Name(id='re', ctx=Load()),
                        attr='I',
                        ctx=Load(),
                    ),
                ],
                keywords=[],
            ),
            type_comment=None,
        ),
        FunctionDef(
            name='_from_table',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='table', annotation=None, type_comment=None),
                    arg(arg='alias', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Return a FROM clause element from ``table`` and ``alias``. ', kind=None),
                ),
                If(
                    test=Compare(
                        left=Name(id='alias', ctx=Load()),
                        ops=[Eq()],
                        comparators=[Name(id='table', ctx=Load())],
                    ),
                    body=[
                        Return(
                            value=JoinedStr(
                                values=[
                                    Constant(value='"', kind=None),
                                    FormattedValue(
                                        value=Name(id='alias', ctx=Load()),
                                        conversion=-1,
                                        format_spec=None,
                                    ),
                                    Constant(value='"', kind=None),
                                ],
                            ),
                        ),
                    ],
                    orelse=[
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='IDENT_RE', ctx=Load()),
                                    attr='match',
                                    ctx=Load(),
                                ),
                                args=[Name(id='table', ctx=Load())],
                                keywords=[],
                            ),
                            body=[
                                Return(
                                    value=JoinedStr(
                                        values=[
                                            Constant(value='"', kind=None),
                                            FormattedValue(
                                                value=Name(id='table', ctx=Load()),
                                                conversion=-1,
                                                format_spec=None,
                                            ),
                                            Constant(value='" AS "', kind=None),
                                            FormattedValue(
                                                value=Name(id='alias', ctx=Load()),
                                                conversion=-1,
                                                format_spec=None,
                                            ),
                                            Constant(value='"', kind=None),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[
                                Return(
                                    value=JoinedStr(
                                        values=[
                                            Constant(value='(', kind=None),
                                            FormattedValue(
                                                value=Name(id='table', ctx=Load()),
                                                conversion=-1,
                                                format_spec=None,
                                            ),
                                            Constant(value=') AS "', kind=None),
                                            FormattedValue(
                                                value=Name(id='alias', ctx=Load()),
                                                conversion=-1,
                                                format_spec=None,
                                            ),
                                            Constant(value='"', kind=None),
                                        ],
                                    ),
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
            name='_generate_table_alias',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='src_table_alias', annotation=None, type_comment=None),
                    arg(arg='link', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=" Generate a standard table alias name. An alias is generated as following:\n        - the base is the source table name (that can already be an alias)\n        - then, the joined table is added in the alias using a 'link field name'\n          that is used to render unique aliases for a given path\n        - the name is shortcut if it goes beyond PostgreSQL's identifier limits\n\n        Examples:\n        - src_table_alias='res_users', link='parent_id'\n            alias = 'res_users__parent_id'\n\n        :param str src_table_alias: alias of the source table\n        :param str link: field name\n        :return str: alias\n    ", kind=None),
                ),
                Assign(
                    targets=[Name(id='alias', ctx=Store())],
                    value=BinOp(
                        left=Constant(value='%s__%s', kind=None),
                        op=Mod(),
                        right=Tuple(
                            elts=[
                                Name(id='src_table_alias', ctx=Load()),
                                Name(id='link', ctx=Load()),
                            ],
                            ctx=Load(),
                        ),
                    ),
                    type_comment=None,
                ),
                If(
                    test=Compare(
                        left=Call(
                            func=Name(id='len', ctx=Load()),
                            args=[Name(id='alias', ctx=Load())],
                            keywords=[],
                        ),
                        ops=[GtE()],
                        comparators=[Constant(value=64, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='alias', ctx=Store())],
                            value=BinOp(
                                left=Constant(value='%s_%08x', kind=None),
                                op=Mod(),
                                right=Tuple(
                                    elts=[
                                        Subscript(
                                            value=Name(id='alias', ctx=Load()),
                                            slice=Slice(
                                                lower=None,
                                                upper=Constant(value=54, kind=None),
                                                step=None,
                                            ),
                                            ctx=Load(),
                                        ),
                                        Call(
                                            func=Name(id='crc32', ctx=Load()),
                                            args=[
                                                Call(
                                                    func=Attribute(
                                                        value=Name(id='alias', ctx=Load()),
                                                        attr='encode',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='utf-8', kind=None)],
                                                    keywords=[],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
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
                    value=Name(id='alias', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        ClassDef(
            name='Query',
            bases=[Name(id='object', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' Simple implementation of a query object, managing tables with aliases,\n    join clauses (with aliases, condition and parameters), where clauses (with\n    parameters), order, limit and offset.\n\n    :param cr: database cursor (for lazy evaluation)\n    :param alias: name or alias of the table\n    :param table: if given, a table expression (identifier or query)\n    ', kind=None),
                ),
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='cr', annotation=None, type_comment=None),
                            arg(arg='alias', annotation=None, type_comment=None),
                            arg(arg='table', annotation=None, type_comment=None),
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
                                    attr='_cr',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='cr', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_tables',
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(
                                keys=[Name(id='alias', ctx=Load())],
                                values=[
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Name(id='table', ctx=Load()),
                                            Name(id='alias', ctx=Load()),
                                        ],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_joins',
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_where_clauses',
                                    ctx=Store(),
                                ),
                            ],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_where_params',
                                    ctx=Store(),
                                ),
                            ],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='order',
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
                                    attr='limit',
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
                                    attr='offset',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='add_table',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='alias', annotation=None, type_comment=None),
                            arg(arg='table', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Add a table with a given alias to the from clause. ', kind=None),
                        ),
                        Assert(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Name(id='alias', ctx=Load()),
                                        ops=[NotIn()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_tables',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Compare(
                                        left=Name(id='alias', ctx=Load()),
                                        ops=[NotIn()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_joins',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            msg=BinOp(
                                left=Constant(value='Alias %r already in %s', kind=None),
                                op=Mod(),
                                right=Tuple(
                                    elts=[
                                        Name(id='alias', ctx=Load()),
                                        Call(
                                            func=Name(id='str', ctx=Load()),
                                            args=[Name(id='self', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_tables',
                                        ctx=Load(),
                                    ),
                                    slice=Name(id='alias', ctx=Load()),
                                    ctx=Store(),
                                ),
                            ],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='table', ctx=Load()),
                                    Name(id='alias', ctx=Load()),
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
                    name='add_where',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='where_clause', annotation=None, type_comment=None),
                            arg(arg='where_params', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Tuple(elts=[], ctx=Load())],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Add a condition to the where clause. ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_where_clauses',
                                        ctx=Load(),
                                    ),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[Name(id='where_clause', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_where_params',
                                        ctx=Load(),
                                    ),
                                    attr='extend',
                                    ctx=Load(),
                                ),
                                args=[Name(id='where_params', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='join',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='lhs_alias', annotation=None, type_comment=None),
                            arg(arg='lhs_column', annotation=None, type_comment=None),
                            arg(arg='rhs_table', annotation=None, type_comment=None),
                            arg(arg='rhs_column', annotation=None, type_comment=None),
                            arg(arg='link', annotation=None, type_comment=None),
                            arg(arg='extra', annotation=None, type_comment=None),
                            arg(arg='extra_params', annotation=None, type_comment=None),
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
                            value=Constant(value='\n        Perform a join between a table already present in the current Query object and\n        another table.\n\n        :param str lhs_alias: alias of a table already defined in the current Query object.\n        :param str lhs_column: column of `lhs_alias` to be used for the join\'s ON condition.\n        :param str rhs_table: name of the table to join to `lhs_alias`.\n        :param str rhs_column: column of `rhs_alias` to be used for the join\'s ON condition.\n        :param str link: used to generate the alias for the joined table, this string should\n            represent the relationship (the link) between both tables.\n        :param str extra: an sql string of a predicate or series of predicates to append to the\n            join\'s ON condition, `lhs_alias` and `rhs_alias` can be injected if the string uses\n            the `lhs` and `rhs` variables with the `str.format` syntax. e.g.::\n\n                query.join(..., extra="{lhs}.name != {rhs}.name OR ...", ...)\n\n        :param tuple extra_params: a tuple of values to be interpolated into `extra`, this is\n            done by psycopg2.\n\n        Full example:\n\n        >>> rhs_alias = query.join(\n        ...     "res_users",\n        ...     "partner_id",\n        ...     "res_partner",\n        ...     "id",\n        ...     "partner_id",           # partner_id is the "link" from res_users to res_partner\n        ...     "{lhs}."name" != %s",\n        ...     ("Mitchell Admin",),\n        ... )\n        >>> rhs_alias\n        res_users_res_partner__partner_id\n\n        From the example above, the resulting query would be something like::\n\n            SELECT ...\n            FROM "res_users" AS "res_users"\n            JOIN "res_partner" AS "res_users_res_partner__partner_id"\n                ON "res_users"."partner_id" = "res_users_res_partner__partner_id"."id"\n                AND "res_users"."name" != \'Mitchell Admin\'\n            WHERE ...\n\n        ', kind=None),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_join',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='JOIN', kind=None),
                                    Name(id='lhs_alias', ctx=Load()),
                                    Name(id='lhs_column', ctx=Load()),
                                    Name(id='rhs_table', ctx=Load()),
                                    Name(id='rhs_column', ctx=Load()),
                                    Name(id='link', ctx=Load()),
                                    Name(id='extra', ctx=Load()),
                                    Name(id='extra_params', ctx=Load()),
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
                    name='left_join',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='lhs_alias', annotation=None, type_comment=None),
                            arg(arg='lhs_column', annotation=None, type_comment=None),
                            arg(arg='rhs_table', annotation=None, type_comment=None),
                            arg(arg='rhs_column', annotation=None, type_comment=None),
                            arg(arg='link', annotation=None, type_comment=None),
                            arg(arg='extra', annotation=None, type_comment=None),
                            arg(arg='extra_params', annotation=None, type_comment=None),
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
                            value=Constant(value=' Add a LEFT JOIN to the current table (if necessary), and return the\n        alias corresponding to ``rhs_table``.\n\n        See the documentation of :meth:`~odoo.osv.query.Query.join` for a better overview of the\n        arguments and what they do.\n        ', kind=None),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_join',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='LEFT JOIN', kind=None),
                                    Name(id='lhs_alias', ctx=Load()),
                                    Name(id='lhs_column', ctx=Load()),
                                    Name(id='rhs_table', ctx=Load()),
                                    Name(id='rhs_column', ctx=Load()),
                                    Name(id='link', ctx=Load()),
                                    Name(id='extra', ctx=Load()),
                                    Name(id='extra_params', ctx=Load()),
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
                    name='_join',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='kind', annotation=None, type_comment=None),
                            arg(arg='lhs_alias', annotation=None, type_comment=None),
                            arg(arg='lhs_column', annotation=None, type_comment=None),
                            arg(arg='rhs_table', annotation=None, type_comment=None),
                            arg(arg='rhs_column', annotation=None, type_comment=None),
                            arg(arg='link', annotation=None, type_comment=None),
                            arg(arg='extra', annotation=None, type_comment=None),
                            arg(arg='extra_params', annotation=None, type_comment=None),
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
                        Assert(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Compare(
                                        left=Name(id='lhs_alias', ctx=Load()),
                                        ops=[In()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_tables',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Compare(
                                        left=Name(id='lhs_alias', ctx=Load()),
                                        ops=[In()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_joins',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            msg=BinOp(
                                left=Constant(value='Alias %r not in %s', kind=None),
                                op=Mod(),
                                right=Tuple(
                                    elts=[
                                        Name(id='lhs_alias', ctx=Load()),
                                        Call(
                                            func=Name(id='str', ctx=Load()),
                                            args=[Name(id='self', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                        ),
                        Assign(
                            targets=[Name(id='rhs_alias', ctx=Store())],
                            value=Call(
                                func=Name(id='_generate_table_alias', ctx=Load()),
                                args=[
                                    Name(id='lhs_alias', ctx=Load()),
                                    Name(id='link', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assert(
                            test=Compare(
                                left=Name(id='rhs_alias', ctx=Load()),
                                ops=[NotIn()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_tables',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            msg=BinOp(
                                left=Constant(value='Alias %r already in %s', kind=None),
                                op=Mod(),
                                right=Tuple(
                                    elts=[
                                        Name(id='rhs_alias', ctx=Load()),
                                        Call(
                                            func=Name(id='str', ctx=Load()),
                                            args=[Name(id='self', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                        ),
                        If(
                            test=Compare(
                                left=Name(id='rhs_alias', ctx=Load()),
                                ops=[NotIn()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_joins',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='condition', ctx=Store())],
                                    value=JoinedStr(
                                        values=[
                                            Constant(value='"', kind=None),
                                            FormattedValue(
                                                value=Name(id='lhs_alias', ctx=Load()),
                                                conversion=-1,
                                                format_spec=None,
                                            ),
                                            Constant(value='"."', kind=None),
                                            FormattedValue(
                                                value=Name(id='lhs_column', ctx=Load()),
                                                conversion=-1,
                                                format_spec=None,
                                            ),
                                            Constant(value='" = "', kind=None),
                                            FormattedValue(
                                                value=Name(id='rhs_alias', ctx=Load()),
                                                conversion=-1,
                                                format_spec=None,
                                            ),
                                            Constant(value='"."', kind=None),
                                            FormattedValue(
                                                value=Name(id='rhs_column', ctx=Load()),
                                                conversion=-1,
                                                format_spec=None,
                                            ),
                                            Constant(value='"', kind=None),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='condition_params', ctx=Store())],
                                    value=List(elts=[], ctx=Load()),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='extra', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='condition', ctx=Store())],
                                            value=BinOp(
                                                left=BinOp(
                                                    left=Name(id='condition', ctx=Load()),
                                                    op=Add(),
                                                    right=Constant(value=' AND ', kind=None),
                                                ),
                                                op=Add(),
                                                right=Call(
                                                    func=Attribute(
                                                        value=Name(id='extra', ctx=Load()),
                                                        attr='format',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[
                                                        keyword(
                                                            arg='lhs',
                                                            value=Name(id='lhs_alias', ctx=Load()),
                                                        ),
                                                        keyword(
                                                            arg='rhs',
                                                            value=Name(id='rhs_alias', ctx=Load()),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='condition_params', ctx=Store())],
                                            value=Call(
                                                func=Name(id='list', ctx=Load()),
                                                args=[Name(id='extra_params', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Name(id='kind', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_joins',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Name(id='rhs_alias', ctx=Load()),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Tuple(
                                                elts=[
                                                    Name(id='kind', ctx=Load()),
                                                    Name(id='rhs_table', ctx=Load()),
                                                    Name(id='condition', ctx=Load()),
                                                    Name(id='condition_params', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_tables',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Name(id='rhs_alias', ctx=Load()),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='rhs_table', ctx=Load()),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='add_where',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='condition', ctx=Load()),
                                                    Name(id='condition_params', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='rhs_alias', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='select',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=arg(arg='args', annotation=None, type_comment=None),
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Return the SELECT query as a pair ``(query_string, query_params)``. ', kind=None),
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='from_clause', ctx=Store()),
                                        Name(id='where_clause', ctx=Store()),
                                        Name(id='params', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='get_sql',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='query_str', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Constant(value='SELECT {} FROM {} WHERE {}{}{}{}', kind=None),
                                    attr='format',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Constant(value=', ', kind=None),
                                            attr='join',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    Name(id='args', ctx=Load()),
                                                    List(
                                                        elts=[
                                                            JoinedStr(
                                                                values=[
                                                                    Constant(value='"', kind=None),
                                                                    FormattedValue(
                                                                        value=Call(
                                                                            func=Name(id='next', ctx=Load()),
                                                                            args=[
                                                                                Call(
                                                                                    func=Name(id='iter', ctx=Load()),
                                                                                    args=[
                                                                                        Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='_tables',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                    ],
                                                                                    keywords=[],
                                                                                ),
                                                                            ],
                                                                            keywords=[],
                                                                        ),
                                                                        conversion=-1,
                                                                        format_spec=None,
                                                                    ),
                                                                    Constant(value='".id', kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Name(id='from_clause', ctx=Load()),
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Name(id='where_clause', ctx=Load()),
                                            Constant(value='TRUE', kind=None),
                                        ],
                                    ),
                                    IfExp(
                                        test=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='order',
                                            ctx=Load(),
                                        ),
                                        body=BinOp(
                                            left=Constant(value=' ORDER BY %s', kind=None),
                                            op=Mod(),
                                            right=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='order',
                                                ctx=Load(),
                                            ),
                                        ),
                                        orelse=Constant(value='', kind=None),
                                    ),
                                    IfExp(
                                        test=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='limit',
                                            ctx=Load(),
                                        ),
                                        body=BinOp(
                                            left=Constant(value=' LIMIT %d', kind=None),
                                            op=Mod(),
                                            right=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='limit',
                                                ctx=Load(),
                                            ),
                                        ),
                                        orelse=Constant(value='', kind=None),
                                    ),
                                    IfExp(
                                        test=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='offset',
                                            ctx=Load(),
                                        ),
                                        body=BinOp(
                                            left=Constant(value=' OFFSET %d', kind=None),
                                            op=Mod(),
                                            right=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='offset',
                                                ctx=Load(),
                                            ),
                                        ),
                                        orelse=Constant(value='', kind=None),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Name(id='query_str', ctx=Load()),
                                    Name(id='params', ctx=Load()),
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
                    name='subselect',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=arg(arg='args', annotation=None, type_comment=None),
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Similar to :meth:`.select`, but for sub-queries.\n            This one avoids the ORDER BY clause when possible.\n        ', kind=None),
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='limit',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='offset',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='select',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Starred(
                                                value=Name(id='args', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='from_clause', ctx=Store()),
                                        Name(id='where_clause', ctx=Store()),
                                        Name(id='params', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='get_sql',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='query_str', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Constant(value='SELECT {} FROM {} WHERE {}', kind=None),
                                    attr='format',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Constant(value=', ', kind=None),
                                            attr='join',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    Name(id='args', ctx=Load()),
                                                    List(
                                                        elts=[
                                                            JoinedStr(
                                                                values=[
                                                                    Constant(value='"', kind=None),
                                                                    FormattedValue(
                                                                        value=Call(
                                                                            func=Name(id='next', ctx=Load()),
                                                                            args=[
                                                                                Call(
                                                                                    func=Name(id='iter', ctx=Load()),
                                                                                    args=[
                                                                                        Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='_tables',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                    ],
                                                                                    keywords=[],
                                                                                ),
                                                                            ],
                                                                            keywords=[],
                                                                        ),
                                                                        conversion=-1,
                                                                        format_spec=None,
                                                                    ),
                                                                    Constant(value='".id', kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Name(id='from_clause', ctx=Load()),
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Name(id='where_clause', ctx=Load()),
                                            Constant(value='TRUE', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Name(id='query_str', ctx=Load()),
                                    Name(id='params', ctx=Load()),
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
                    name='get_sql',
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
                            value=Constant(value=' Returns (query_from, query_where, query_params). ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='tables', ctx=Store())],
                            value=ListComp(
                                elt=Call(
                                    func=Name(id='_from_table', ctx=Load()),
                                    args=[
                                        Name(id='table', ctx=Load()),
                                        Name(id='alias', ctx=Load()),
                                    ],
                                    keywords=[],
                                ),
                                generators=[
                                    comprehension(
                                        target=Tuple(
                                            elts=[
                                                Name(id='alias', ctx=Store()),
                                                Name(id='table', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                        iter=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_tables',
                                                    ctx=Load(),
                                                ),
                                                attr='items',
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
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='joins', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='params', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='alias', ctx=Store()),
                                    Tuple(
                                        elts=[
                                            Name(id='kind', ctx=Store()),
                                            Name(id='table', ctx=Store()),
                                            Name(id='condition', ctx=Store()),
                                            Name(id='condition_params', ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_joins',
                                        ctx=Load(),
                                    ),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='joins', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            JoinedStr(
                                                values=[
                                                    FormattedValue(
                                                        value=Name(id='kind', ctx=Load()),
                                                        conversion=-1,
                                                        format_spec=None,
                                                    ),
                                                    Constant(value=' ', kind=None),
                                                    FormattedValue(
                                                        value=Call(
                                                            func=Name(id='_from_table', ctx=Load()),
                                                            args=[
                                                                Name(id='table', ctx=Load()),
                                                                Name(id='alias', ctx=Load()),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        conversion=-1,
                                                        format_spec=None,
                                                    ),
                                                    Constant(value=' ON (', kind=None),
                                                    FormattedValue(
                                                        value=Name(id='condition', ctx=Load()),
                                                        conversion=-1,
                                                        format_spec=None,
                                                    ),
                                                    Constant(value=')', kind=None),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='params', ctx=Load()),
                                            attr='extend',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='condition_params', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='from_clause', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Constant(value=' ', kind=None),
                                    attr='join',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=List(
                                            elts=[
                                                Call(
                                                    func=Attribute(
                                                        value=Constant(value=', ', kind=None),
                                                        attr='join',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='tables', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                        op=Add(),
                                        right=Name(id='joins', ctx=Load()),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='where_clause', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Constant(value=' AND ', kind=None),
                                    attr='join',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_where_clauses',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Name(id='from_clause', ctx=Load()),
                                    Name(id='where_clause', ctx=Load()),
                                    BinOp(
                                        left=Name(id='params', ctx=Load()),
                                        op=Add(),
                                        right=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_where_params',
                                            ctx=Load(),
                                        ),
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
                    name='_result',
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
                                Tuple(
                                    elts=[
                                        Name(id='query_str', ctx=Store()),
                                        Name(id='params', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='select',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
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
                                    Name(id='query_str', ctx=Load()),
                                    Name(id='params', ctx=Load()),
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
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_cr',
                                                    ctx=Load(),
                                                ),
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
                    decorator_list=[Name(id='lazy_property', ctx=Load())],
                    returns=None,
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
                            value=BinOp(
                                left=Constant(value='<osv.Query: %r with params: %r>', kind=None),
                                op=Mod(),
                                right=Call(
                                    func=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='select',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='__bool__',
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
                                func=Name(id='bool', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_result',
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
                    name='__len__',
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
                                func=Name(id='len', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_result',
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
                    name='__iter__',
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
                                func=Name(id='iter', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_result',
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
                    name='tables',
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
                                    Constant(value='deprecated Query.tables, use Query.get_sql() instead', kind=None),
                                    Name(id='DeprecationWarning', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Name(id='tuple', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Call(
                                            func=Name(id='_from_table', ctx=Load()),
                                            args=[
                                                Name(id='table', ctx=Load()),
                                                Name(id='alias', ctx=Load()),
                                            ],
                                            keywords=[],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Tuple(
                                                    elts=[
                                                        Name(id='alias', ctx=Store()),
                                                        Name(id='table', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                                iter=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_tables',
                                                            ctx=Load(),
                                                        ),
                                                        attr='items',
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
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='property', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='where_clause',
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
                                func=Name(id='tuple', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_where_clauses',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='property', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='where_clause_params',
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
                                func=Name(id='tuple', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_where_params',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='property', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='add_join',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='connection', annotation=None, type_comment=None),
                            arg(arg='implicit', annotation=None, type_comment=None),
                            arg(arg='outer', annotation=None, type_comment=None),
                            arg(arg='extra', annotation=None, type_comment=None),
                            arg(arg='extra_params', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=True, kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=None, kind=None),
                            Tuple(elts=[], ctx=Load()),
                        ],
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
                                    Constant(value='deprecated Query.add_join, use Query.join() or Query.left_join() instead', kind=None),
                                    Name(id='DeprecationWarning', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='lhs_alias', ctx=Store()),
                                        Name(id='rhs_table', ctx=Store()),
                                        Name(id='lhs_column', ctx=Store()),
                                        Name(id='rhs_column', ctx=Store()),
                                        Name(id='link', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='connection', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='kind', ctx=Store())],
                            value=IfExp(
                                test=Name(id='implicit', ctx=Load()),
                                body=Constant(value='', kind=None),
                                orelse=IfExp(
                                    test=Name(id='outer', ctx=Load()),
                                    body=Constant(value='LEFT JOIN', kind=None),
                                    orelse=Constant(value='JOIN', kind=None),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='rhs_alias', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_join',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='kind', ctx=Load()),
                                    Name(id='lhs_alias', ctx=Load()),
                                    Name(id='lhs_column', ctx=Load()),
                                    Name(id='rhs_table', ctx=Load()),
                                    Name(id='rhs_column', ctx=Load()),
                                    Name(id='link', ctx=Load()),
                                    Name(id='extra', ctx=Load()),
                                    Name(id='extra_params', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Name(id='rhs_alias', ctx=Load()),
                                    Call(
                                        func=Name(id='_from_table', ctx=Load()),
                                        args=[
                                            Name(id='rhs_table', ctx=Load()),
                                            Name(id='rhs_alias', ctx=Load()),
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
    ],
    type_ignores=[],
)
