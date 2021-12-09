Module(
    body=[
        Expr(
            value=Constant(value=' Domain expression processing\n\nThe main duty of this module is to compile a domain expression into a\nSQL query. A lot of things should be documented here, but as a first\nstep in the right direction, some tests in test_expression.py\nmight give you some additional information.\n\nFor legacy reasons, a domain uses an inconsistent two-levels abstract\nsyntax (domains are regular Python data structures). At the first\nlevel, a domain is an expression made of terms (sometimes called\nleaves) and (domain) operators used in prefix notation. The available\noperators at this level are \'!\', \'&\', and \'|\'. \'!\' is a unary \'not\',\n\'&\' is a binary \'and\', and \'|\' is a binary \'or\'.  For instance, here\nis a possible domain. (<term> stands for an arbitrary term, more on\nthis later.)::\n\n    [\'&\', \'!\', <term1>, \'|\', <term2>, <term3>]\n\nIt is equivalent to this pseudo code using infix notation::\n\n    (not <term1>) and (<term2> or <term3>)\n\nThe second level of syntax deals with the term representation. A term\nis a triple of the form (left, operator, right). That is, a term uses\nan infix notation, and the available operators, and possible left and\nright operands differ with those of the previous level. Here is a\npossible term::\n\n    (\'company_id.name\', \'=\', \'OpenERP\')\n\nThe left and right operand don\'t have the same possible values. The\nleft operand is field name (related to the model for which the domain\napplies).  Actually, the field name can use the dot-notation to\ntraverse relationships.  The right operand is a Python value whose\ntype should match the used operator and field type. In the above\nexample, a string is used because the name field of a company has type\nstring, and because we use the \'=\' operator. When appropriate, a \'in\'\noperator can be used, and thus the right operand should be a list.\n\nNote: the non-uniform syntax could have been more uniform, but this\nwould hide an important limitation of the domain syntax. Say that the\nterm representation was [\'=\', \'company_id.name\', \'OpenERP\']. Used in a\ncomplete domain, this would look like::\n\n    [\'!\', [\'=\', \'company_id.name\', \'OpenERP\']]\n\nand you would be tempted to believe something like this would be\npossible::\n\n    [\'!\', [\'=\', \'company_id.name\', [\'&\', ..., ...]]]\n\nThat is, a domain could be a valid operand. But this is not the\ncase. A domain is really limited to a two-level nature, and can not\ntake a recursive form: a domain is not a valid second-level operand.\n\nUnaccent - Accent-insensitive search\n\nOpenERP will use the SQL function \'unaccent\' when available for the\n\'ilike\' and \'not ilike\' operators, and enabled in the configuration.\nNormally the \'unaccent\' function is obtained from `the PostgreSQL\n\'unaccent\' contrib module\n<http://developer.postgresql.org/pgdocs/postgres/unaccent.html>`_.\n\n.. todo: The following explanation should be moved in some external\n         installation guide\n\nThe steps to install the module might differ on specific PostgreSQL\nversions.  We give here some instruction for PostgreSQL 9.x on a\nUbuntu system.\n\nUbuntu doesn\'t come yet with PostgreSQL 9.x, so an alternative package\nsource is used. We use Martin Pitt\'s PPA available at\n`ppa:pitti/postgresql\n<https://launchpad.net/~pitti/+archive/postgresql>`_.\n\n.. code-block:: sh\n\n    > sudo add-apt-repository ppa:pitti/postgresql\n    > sudo apt-get update\n\nOnce the package list is up-to-date, you have to install PostgreSQL\n9.0 and its contrib modules.\n\n.. code-block:: sh\n\n    > sudo apt-get install postgresql-9.0 postgresql-contrib-9.0\n\nWhen you want to enable unaccent on some database:\n\n.. code-block:: sh\n\n    > psql9 <database> -f /usr/share/postgresql/9.0/contrib/unaccent.sql\n\nHere :program:`psql9` is an alias for the newly installed PostgreSQL\n9.0 tool, together with the correct port if necessary (for instance if\nPostgreSQL 8.4 is running on 5432). (Other aliases can be used for\ncreatedb and dropdb.)\n\n.. code-block:: sh\n\n    > alias psql9=\'/usr/lib/postgresql/9.0/bin/psql -p 5433\'\n\nYou can check unaccent is working:\n\n.. code-block:: sh\n\n    > psql9 <database> -c"select unaccent(\'hélène\')"\n\nFinally, to instruct OpenERP to really use the unaccent function, you have to\nstart the server specifying the ``--unaccent`` flag.\n\n', kind=None),
        ),
        Import(
            names=[alias(name='collections.abc', asname=None)],
        ),
        Import(
            names=[alias(name='warnings', asname=None)],
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='reprlib', asname=None)],
        ),
        Import(
            names=[alias(name='traceback', asname=None)],
        ),
        ImportFrom(
            module='functools',
            names=[alias(name='partial', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='datetime',
            names=[
                alias(name='date', asname=None),
                alias(name='datetime', asname=None),
                alias(name='time', asname=None),
            ],
            level=0,
        ),
        Import(
            names=[alias(name='odoo.modules', asname=None)],
        ),
        ImportFrom(
            module='odoo.osv.query',
            names=[alias(name='Query', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[alias(name='pycompat', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.misc',
            names=[alias(name='get_lang', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='models',
            names=[
                alias(name='MAGIC_COLUMNS', asname=None),
                alias(name='BaseModel', asname=None),
            ],
            level=2,
        ),
        Import(
            names=[alias(name='odoo.tools', asname='tools')],
        ),
        Assign(
            targets=[Name(id='NOT_OPERATOR', ctx=Store())],
            value=Constant(value='!', kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='OR_OPERATOR', ctx=Store())],
            value=Constant(value='|', kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='AND_OPERATOR', ctx=Store())],
            value=Constant(value='&', kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='DOMAIN_OPERATORS', ctx=Store())],
            value=Tuple(
                elts=[
                    Name(id='NOT_OPERATOR', ctx=Load()),
                    Name(id='OR_OPERATOR', ctx=Load()),
                    Name(id='AND_OPERATOR', ctx=Load()),
                ],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='TERM_OPERATORS', ctx=Store())],
            value=Tuple(
                elts=[
                    Constant(value='=', kind=None),
                    Constant(value='!=', kind=None),
                    Constant(value='<=', kind=None),
                    Constant(value='<', kind=None),
                    Constant(value='>', kind=None),
                    Constant(value='>=', kind=None),
                    Constant(value='=?', kind=None),
                    Constant(value='=like', kind=None),
                    Constant(value='=ilike', kind=None),
                    Constant(value='like', kind=None),
                    Constant(value='not like', kind=None),
                    Constant(value='ilike', kind=None),
                    Constant(value='not ilike', kind=None),
                    Constant(value='in', kind=None),
                    Constant(value='not in', kind=None),
                    Constant(value='child_of', kind=None),
                    Constant(value='parent_of', kind=None),
                ],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='NEGATIVE_TERM_OPERATORS', ctx=Store())],
            value=Tuple(
                elts=[
                    Constant(value='!=', kind=None),
                    Constant(value='not like', kind=None),
                    Constant(value='not ilike', kind=None),
                    Constant(value='not in', kind=None),
                ],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='DOMAIN_OPERATORS_NEGATION', ctx=Store())],
            value=Dict(
                keys=[
                    Name(id='AND_OPERATOR', ctx=Load()),
                    Name(id='OR_OPERATOR', ctx=Load()),
                ],
                values=[
                    Name(id='OR_OPERATOR', ctx=Load()),
                    Name(id='AND_OPERATOR', ctx=Load()),
                ],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='TERM_OPERATORS_NEGATION', ctx=Store())],
            value=Dict(
                keys=[
                    Constant(value='<', kind=None),
                    Constant(value='>', kind=None),
                    Constant(value='<=', kind=None),
                    Constant(value='>=', kind=None),
                    Constant(value='=', kind=None),
                    Constant(value='!=', kind=None),
                    Constant(value='in', kind=None),
                    Constant(value='like', kind=None),
                    Constant(value='ilike', kind=None),
                    Constant(value='not in', kind=None),
                    Constant(value='not like', kind=None),
                    Constant(value='not ilike', kind=None),
                ],
                values=[
                    Constant(value='>=', kind=None),
                    Constant(value='<=', kind=None),
                    Constant(value='>', kind=None),
                    Constant(value='<', kind=None),
                    Constant(value='!=', kind=None),
                    Constant(value='=', kind=None),
                    Constant(value='not in', kind=None),
                    Constant(value='not like', kind=None),
                    Constant(value='not ilike', kind=None),
                    Constant(value='in', kind=None),
                    Constant(value='like', kind=None),
                    Constant(value='ilike', kind=None),
                ],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='TRUE_LEAF', ctx=Store())],
            value=Tuple(
                elts=[
                    Constant(value=1, kind=None),
                    Constant(value='=', kind=None),
                    Constant(value=1, kind=None),
                ],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='FALSE_LEAF', ctx=Store())],
            value=Tuple(
                elts=[
                    Constant(value=0, kind=None),
                    Constant(value='=', kind=None),
                    Constant(value=1, kind=None),
                ],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='TRUE_DOMAIN', ctx=Store())],
            value=List(
                elts=[Name(id='TRUE_LEAF', ctx=Load())],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='FALSE_DOMAIN', ctx=Store())],
            value=List(
                elts=[Name(id='FALSE_LEAF', ctx=Load())],
                ctx=Load(),
            ),
            type_comment=None,
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
            name='normalize_domain',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='domain', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value="Returns a normalized version of ``domain_expr``, where all implicit '&' operators\n       have been made explicit. One property of normalized domain expressions is that they\n       can be easily combined together as if they were single domain components.\n    ", kind=None),
                ),
                Assert(
                    test=Call(
                        func=Name(id='isinstance', ctx=Load()),
                        args=[
                            Name(id='domain', ctx=Load()),
                            Tuple(
                                elts=[
                                    Name(id='list', ctx=Load()),
                                    Name(id='tuple', ctx=Load()),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                    msg=Constant(value="Domains to normalize must have a 'domain' form: a list or tuple of domain components", kind=None),
                ),
                If(
                    test=UnaryOp(
                        op=Not(),
                        operand=Name(id='domain', ctx=Load()),
                    ),
                    body=[
                        Return(
                            value=List(
                                elts=[Name(id='TRUE_LEAF', ctx=Load())],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    targets=[Name(id='result', ctx=Store())],
                    value=List(elts=[], ctx=Load()),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='expected', ctx=Store())],
                    value=Constant(value=1, kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='op_arity', ctx=Store())],
                    value=Dict(
                        keys=[
                            Name(id='NOT_OPERATOR', ctx=Load()),
                            Name(id='AND_OPERATOR', ctx=Load()),
                            Name(id='OR_OPERATOR', ctx=Load()),
                        ],
                        values=[
                            Constant(value=1, kind=None),
                            Constant(value=2, kind=None),
                            Constant(value=2, kind=None),
                        ],
                    ),
                    type_comment=None,
                ),
                For(
                    target=Name(id='token', ctx=Store()),
                    iter=Name(id='domain', ctx=Load()),
                    body=[
                        If(
                            test=Compare(
                                left=Name(id='expected', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value=0, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='result', ctx=Load()),
                                            slice=Slice(
                                                lower=Constant(value=0, kind=None),
                                                upper=Constant(value=0, kind=None),
                                                step=None,
                                            ),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=List(
                                        elts=[Name(id='AND_OPERATOR', ctx=Load())],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='expected', ctx=Store())],
                                    value=Constant(value=1, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Call(
                                func=Name(id='isinstance', ctx=Load()),
                                args=[
                                    Name(id='token', ctx=Load()),
                                    Tuple(
                                        elts=[
                                            Name(id='list', ctx=Load()),
                                            Name(id='tuple', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                AugAssign(
                                    target=Name(id='expected', ctx=Store()),
                                    op=Sub(),
                                    value=Constant(value=1, kind=None),
                                ),
                                Assign(
                                    targets=[Name(id='token', ctx=Store())],
                                    value=Call(
                                        func=Name(id='tuple', ctx=Load()),
                                        args=[Name(id='token', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                AugAssign(
                                    target=Name(id='expected', ctx=Store()),
                                    op=Add(),
                                    value=BinOp(
                                        left=Call(
                                            func=Attribute(
                                                value=Name(id='op_arity', ctx=Load()),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Name(id='token', ctx=Load()),
                                                Constant(value=0, kind=None),
                                            ],
                                            keywords=[],
                                        ),
                                        op=Sub(),
                                        right=Constant(value=1, kind=None),
                                    ),
                                ),
                            ],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='result', ctx=Load()),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[Name(id='token', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[],
                    type_comment=None,
                ),
                Assert(
                    test=Compare(
                        left=Name(id='expected', ctx=Load()),
                        ops=[Eq()],
                        comparators=[Constant(value=0, kind=None)],
                    ),
                    msg=BinOp(
                        left=Constant(value='This domain is syntactically not correct: %s', kind=None),
                        op=Mod(),
                        right=Name(id='domain', ctx=Load()),
                    ),
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
            name='is_false',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='model', annotation=None, type_comment=None),
                    arg(arg='domain', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Return whether ``domain`` is logically equivalent to false. ', kind=None),
                ),
                Assign(
                    targets=[Name(id='stack', ctx=Store())],
                    value=List(elts=[], ctx=Load()),
                    type_comment=None,
                ),
                For(
                    target=Name(id='token', ctx=Store()),
                    iter=Call(
                        func=Name(id='reversed', ctx=Load()),
                        args=[
                            Call(
                                func=Name(id='normalize_domain', ctx=Load()),
                                args=[Name(id='domain', ctx=Load())],
                                keywords=[],
                            ),
                        ],
                        keywords=[],
                    ),
                    body=[
                        If(
                            test=Compare(
                                left=Name(id='token', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='&', kind=None)],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='stack', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='min', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='stack', ctx=Load()),
                                                            attr='pop',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='stack', ctx=Load()),
                                                            attr='pop',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
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
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Name(id='token', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='|', kind=None)],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='stack', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Name(id='max', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='stack', ctx=Load()),
                                                                    attr='pop',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='stack', ctx=Load()),
                                                                    attr='pop',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
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
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Name(id='token', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='!', kind=None)],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='stack', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            UnaryOp(
                                                                op=USub(),
                                                                operand=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='stack', ctx=Load()),
                                                                        attr='pop',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[],
                                                                    keywords=[],
                                                                ),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Compare(
                                                        left=Name(id='token', ctx=Load()),
                                                        ops=[Eq()],
                                                        comparators=[Name(id='TRUE_LEAF', ctx=Load())],
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='stack', ctx=Load()),
                                                                    attr='append',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    UnaryOp(
                                                                        op=UAdd(),
                                                                        operand=Constant(value=1, kind=None),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[
                                                        If(
                                                            test=Compare(
                                                                left=Name(id='token', ctx=Load()),
                                                                ops=[Eq()],
                                                                comparators=[Name(id='FALSE_LEAF', ctx=Load())],
                                                            ),
                                                            body=[
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='stack', ctx=Load()),
                                                                            attr='append',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            UnaryOp(
                                                                                op=USub(),
                                                                                operand=Constant(value=1, kind=None),
                                                                            ),
                                                                        ],
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
                                                                                left=Subscript(
                                                                                    value=Name(id='token', ctx=Load()),
                                                                                    slice=Constant(value=1, kind=None),
                                                                                    ctx=Load(),
                                                                                ),
                                                                                ops=[Eq()],
                                                                                comparators=[Constant(value='in', kind=None)],
                                                                            ),
                                                                            UnaryOp(
                                                                                op=Not(),
                                                                                operand=BoolOp(
                                                                                    op=Or(),
                                                                                    values=[
                                                                                        Call(
                                                                                            func=Name(id='isinstance', ctx=Load()),
                                                                                            args=[
                                                                                                Subscript(
                                                                                                    value=Name(id='token', ctx=Load()),
                                                                                                    slice=Constant(value=2, kind=None),
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                Name(id='Query', ctx=Load()),
                                                                                            ],
                                                                                            keywords=[],
                                                                                        ),
                                                                                        Subscript(
                                                                                            value=Name(id='token', ctx=Load()),
                                                                                            slice=Constant(value=2, kind=None),
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                    ],
                                                                                ),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                    body=[
                                                                        Expr(
                                                                            value=Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='stack', ctx=Load()),
                                                                                    attr='append',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[
                                                                                    UnaryOp(
                                                                                        op=USub(),
                                                                                        operand=Constant(value=1, kind=None),
                                                                                    ),
                                                                                ],
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
                                                                                        left=Subscript(
                                                                                            value=Name(id='token', ctx=Load()),
                                                                                            slice=Constant(value=1, kind=None),
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        ops=[Eq()],
                                                                                        comparators=[Constant(value='not in', kind=None)],
                                                                                    ),
                                                                                    UnaryOp(
                                                                                        op=Not(),
                                                                                        operand=BoolOp(
                                                                                            op=Or(),
                                                                                            values=[
                                                                                                Call(
                                                                                                    func=Name(id='isinstance', ctx=Load()),
                                                                                                    args=[
                                                                                                        Subscript(
                                                                                                            value=Name(id='token', ctx=Load()),
                                                                                                            slice=Constant(value=2, kind=None),
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        Name(id='Query', ctx=Load()),
                                                                                                    ],
                                                                                                    keywords=[],
                                                                                                ),
                                                                                                Subscript(
                                                                                                    value=Name(id='token', ctx=Load()),
                                                                                                    slice=Constant(value=2, kind=None),
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                            ],
                                                                                        ),
                                                                                    ),
                                                                                ],
                                                                            ),
                                                                            body=[
                                                                                Expr(
                                                                                    value=Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='stack', ctx=Load()),
                                                                                            attr='append',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[
                                                                                            UnaryOp(
                                                                                                op=UAdd(),
                                                                                                operand=Constant(value=1, kind=None),
                                                                                            ),
                                                                                        ],
                                                                                        keywords=[],
                                                                                    ),
                                                                                ),
                                                                            ],
                                                                            orelse=[
                                                                                Expr(
                                                                                    value=Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='stack', ctx=Load()),
                                                                                            attr='append',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[Constant(value=0, kind=None)],
                                                                                        keywords=[],
                                                                                    ),
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
                    orelse=[],
                    type_comment=None,
                ),
                Return(
                    value=Compare(
                        left=Call(
                            func=Attribute(
                                value=Name(id='stack', ctx=Load()),
                                attr='pop',
                                ctx=Load(),
                            ),
                            args=[],
                            keywords=[],
                        ),
                        ops=[Eq()],
                        comparators=[
                            UnaryOp(
                                op=USub(),
                                operand=Constant(value=1, kind=None),
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
            name='combine',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='operator', annotation=None, type_comment=None),
                    arg(arg='unit', annotation=None, type_comment=None),
                    arg(arg='zero', annotation=None, type_comment=None),
                    arg(arg='domains', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value='Returns a new domain expression where all domain components from ``domains``\n       have been added together using the binary operator ``operator``.\n\n       It is guaranteed to return a normalized domain.\n\n       :param unit: the identity element of the domains "set" with regard to the operation\n                    performed by ``operator``, i.e the domain component ``i`` which, when\n                    combined with any domain ``x`` via ``operator``, yields ``x``.\n                    E.g. [(1,\'=\',1)] is the typical unit for AND_OPERATOR: adding it\n                    to any domain component gives the same domain.\n       :param zero: the absorbing element of the domains "set" with regard to the operation\n                    performed by ``operator``, i.e the domain component ``z`` which, when\n                    combined with any domain ``x`` via ``operator``, yields ``z``.\n                    E.g. [(1,\'=\',1)] is the typical zero for OR_OPERATOR: as soon as\n                    you see it in a domain component the resulting domain is the zero.\n       :param domains: a list of normalized domains.\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='result', ctx=Store())],
                    value=List(elts=[], ctx=Load()),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='count', ctx=Store())],
                    value=Constant(value=0, kind=None),
                    type_comment=None,
                ),
                If(
                    test=Compare(
                        left=Name(id='domains', ctx=Load()),
                        ops=[Eq()],
                        comparators=[
                            List(
                                elts=[Name(id='unit', ctx=Load())],
                                ctx=Load(),
                            ),
                        ],
                    ),
                    body=[
                        Return(
                            value=Name(id='unit', ctx=Load()),
                        ),
                    ],
                    orelse=[],
                ),
                For(
                    target=Name(id='domain', ctx=Store()),
                    iter=Name(id='domains', ctx=Load()),
                    body=[
                        If(
                            test=Compare(
                                left=Name(id='domain', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Name(id='unit', ctx=Load())],
                            ),
                            body=[Continue()],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Name(id='domain', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Name(id='zero', ctx=Load())],
                            ),
                            body=[
                                Return(
                                    value=Name(id='zero', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Name(id='domain', ctx=Load()),
                            body=[
                                AugAssign(
                                    target=Name(id='result', ctx=Store()),
                                    op=Add(),
                                    value=Call(
                                        func=Name(id='normalize_domain', ctx=Load()),
                                        args=[Name(id='domain', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                AugAssign(
                                    target=Name(id='count', ctx=Store()),
                                    op=Add(),
                                    value=Constant(value=1, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    orelse=[],
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='result', ctx=Store())],
                    value=BinOp(
                        left=BinOp(
                            left=List(
                                elts=[Name(id='operator', ctx=Load())],
                                ctx=Load(),
                            ),
                            op=Mult(),
                            right=BinOp(
                                left=Name(id='count', ctx=Load()),
                                op=Sub(),
                                right=Constant(value=1, kind=None),
                            ),
                        ),
                        op=Add(),
                        right=Name(id='result', ctx=Load()),
                    ),
                    type_comment=None,
                ),
                Return(
                    value=BoolOp(
                        op=Or(),
                        values=[
                            Name(id='result', ctx=Load()),
                            Name(id='unit', ctx=Load()),
                        ],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='AND',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='domains', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value='AND([D1,D2,...]) returns a domain representing D1 and D2 and ... ', kind=None),
                ),
                Return(
                    value=Call(
                        func=Name(id='combine', ctx=Load()),
                        args=[
                            Name(id='AND_OPERATOR', ctx=Load()),
                            List(
                                elts=[Name(id='TRUE_LEAF', ctx=Load())],
                                ctx=Load(),
                            ),
                            List(
                                elts=[Name(id='FALSE_LEAF', ctx=Load())],
                                ctx=Load(),
                            ),
                            Name(id='domains', ctx=Load()),
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
            name='OR',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='domains', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value='OR([D1,D2,...]) returns a domain representing D1 or D2 or ... ', kind=None),
                ),
                Return(
                    value=Call(
                        func=Name(id='combine', ctx=Load()),
                        args=[
                            Name(id='OR_OPERATOR', ctx=Load()),
                            List(
                                elts=[Name(id='FALSE_LEAF', ctx=Load())],
                                ctx=Load(),
                            ),
                            List(
                                elts=[Name(id='TRUE_LEAF', ctx=Load())],
                                ctx=Load(),
                            ),
                            Name(id='domains', ctx=Load()),
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
            name='distribute_not',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='domain', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=" Distribute any '!' domain operators found inside a normalized domain.\n\n    Because we don't use SQL semantic for processing a 'left not in right'\n    query (i.e. our 'not in' is not simply translated to a SQL 'not in'),\n    it means that a '! left in right' can not be simply processed\n    by __leaf_to_sql by first emitting code for 'left in right' then wrapping\n    the result with 'not (...)', as it would result in a 'not in' at the SQL\n    level.\n\n    This function is thus responsible for pushing any '!' domain operators\n    inside the terms themselves. For example::\n\n         ['!','&',('user_id','=',4),('partner_id','in',[1,2])]\n            will be turned into:\n         ['|',('user_id','!=',4),('partner_id','not in',[1,2])]\n\n    ", kind=None),
                ),
                Assign(
                    targets=[Name(id='result', ctx=Store())],
                    value=List(elts=[], ctx=Load()),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='stack', ctx=Store())],
                    value=List(
                        elts=[Constant(value=False, kind=None)],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                For(
                    target=Name(id='token', ctx=Store()),
                    iter=Name(id='domain', ctx=Load()),
                    body=[
                        Assign(
                            targets=[Name(id='negate', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='stack', ctx=Load()),
                                    attr='pop',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Name(id='is_leaf', ctx=Load()),
                                args=[Name(id='token', ctx=Load())],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=Name(id='negate', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Tuple(
                                                    elts=[
                                                        Name(id='left', ctx=Store()),
                                                        Name(id='operator', ctx=Store()),
                                                        Name(id='right', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='token', ctx=Load()),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Name(id='operator', ctx=Load()),
                                                ops=[In()],
                                                comparators=[Name(id='TERM_OPERATORS_NEGATION', ctx=Load())],
                                            ),
                                            body=[
                                                If(
                                                    test=Compare(
                                                        left=Name(id='token', ctx=Load()),
                                                        ops=[In()],
                                                        comparators=[
                                                            Tuple(
                                                                elts=[
                                                                    Name(id='TRUE_LEAF', ctx=Load()),
                                                                    Name(id='FALSE_LEAF', ctx=Load()),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
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
                                                                    IfExp(
                                                                        test=Compare(
                                                                            left=Name(id='token', ctx=Load()),
                                                                            ops=[Eq()],
                                                                            comparators=[Name(id='TRUE_LEAF', ctx=Load())],
                                                                        ),
                                                                        body=Name(id='FALSE_LEAF', ctx=Load()),
                                                                        orelse=Name(id='TRUE_LEAF', ctx=Load()),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='result', ctx=Load()),
                                                                    attr='append',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Name(id='left', ctx=Load()),
                                                                            Subscript(
                                                                                value=Name(id='TERM_OPERATORS_NEGATION', ctx=Load()),
                                                                                slice=Name(id='operator', ctx=Load()),
                                                                                ctx=Load(),
                                                                            ),
                                                                            Name(id='right', ctx=Load()),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            orelse=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='result', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='NOT_OPERATOR', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='result', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='token', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='result', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='token', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Name(id='token', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Name(id='NOT_OPERATOR', ctx=Load())],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='stack', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Name(id='negate', ctx=Load()),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Name(id='token', ctx=Load()),
                                                ops=[In()],
                                                comparators=[Name(id='DOMAIN_OPERATORS_NEGATION', ctx=Load())],
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
                                                            IfExp(
                                                                test=Name(id='negate', ctx=Load()),
                                                                body=Subscript(
                                                                    value=Name(id='DOMAIN_OPERATORS_NEGATION', ctx=Load()),
                                                                    slice=Name(id='token', ctx=Load()),
                                                                    ctx=Load(),
                                                                ),
                                                                orelse=Name(id='token', ctx=Load()),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='stack', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='negate', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='stack', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='negate', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='result', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='token', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
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
            name='_quote',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='to_quote', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                If(
                    test=Compare(
                        left=Constant(value='"', kind=None),
                        ops=[NotIn()],
                        comparators=[Name(id='to_quote', ctx=Load())],
                    ),
                    body=[
                        Return(
                            value=BinOp(
                                left=Constant(value='"%s"', kind=None),
                                op=Mod(),
                                right=Name(id='to_quote', ctx=Load()),
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Name(id='to_quote', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='normalize_leaf',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='element', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=" Change a term's operator to some canonical form, simplifying later\n        processing. ", kind=None),
                ),
                If(
                    test=UnaryOp(
                        op=Not(),
                        operand=Call(
                            func=Name(id='is_leaf', ctx=Load()),
                            args=[Name(id='element', ctx=Load())],
                            keywords=[],
                        ),
                    ),
                    body=[
                        Return(
                            value=Name(id='element', ctx=Load()),
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    targets=[
                        Tuple(
                            elts=[
                                Name(id='left', ctx=Store()),
                                Name(id='operator', ctx=Store()),
                                Name(id='right', ctx=Store()),
                            ],
                            ctx=Store(),
                        ),
                    ],
                    value=Name(id='element', ctx=Load()),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='original', ctx=Store())],
                    value=Name(id='operator', ctx=Load()),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='operator', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='operator', ctx=Load()),
                            attr='lower',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=Compare(
                        left=Name(id='operator', ctx=Load()),
                        ops=[Eq()],
                        comparators=[Constant(value='<>', kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='operator', ctx=Store())],
                            value=Constant(value='!=', kind=None),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    test=BoolOp(
                        op=And(),
                        values=[
                            Call(
                                func=Name(id='isinstance', ctx=Load()),
                                args=[
                                    Name(id='right', ctx=Load()),
                                    Name(id='bool', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            Compare(
                                left=Name(id='operator', ctx=Load()),
                                ops=[In()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value='in', kind=None),
                                            Constant(value='not in', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='warning',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Constant(value="The domain term '%s' should use the '=' or '!=' operator.", kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Name(id='left', ctx=Load()),
                                                        Name(id='original', ctx=Load()),
                                                        Name(id='right', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='operator', ctx=Store())],
                            value=IfExp(
                                test=Compare(
                                    left=Name(id='operator', ctx=Load()),
                                    ops=[Eq()],
                                    comparators=[Constant(value='in', kind=None)],
                                ),
                                body=Constant(value='=', kind=None),
                                orelse=Constant(value='!=', kind=None),
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    test=BoolOp(
                        op=And(),
                        values=[
                            Call(
                                func=Name(id='isinstance', ctx=Load()),
                                args=[
                                    Name(id='right', ctx=Load()),
                                    Tuple(
                                        elts=[
                                            Name(id='list', ctx=Load()),
                                            Name(id='tuple', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            Compare(
                                left=Name(id='operator', ctx=Load()),
                                ops=[In()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value='=', kind=None),
                                            Constant(value='!=', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='warning',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Constant(value="The domain term '%s' should use the 'in' or 'not in' operator.", kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Name(id='left', ctx=Load()),
                                                        Name(id='original', ctx=Load()),
                                                        Name(id='right', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='operator', ctx=Store())],
                            value=IfExp(
                                test=Compare(
                                    left=Name(id='operator', ctx=Load()),
                                    ops=[Eq()],
                                    comparators=[Constant(value='=', kind=None)],
                                ),
                                body=Constant(value='in', kind=None),
                                orelse=Constant(value='not in', kind=None),
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Tuple(
                        elts=[
                            Name(id='left', ctx=Load()),
                            Name(id='operator', ctx=Load()),
                            Name(id='right', ctx=Load()),
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
            name='is_operator',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='element', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Test whether an object is a valid domain operator. ', kind=None),
                ),
                Return(
                    value=BoolOp(
                        op=And(),
                        values=[
                            Call(
                                func=Name(id='isinstance', ctx=Load()),
                                args=[
                                    Name(id='element', ctx=Load()),
                                    Name(id='str', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            Compare(
                                left=Name(id='element', ctx=Load()),
                                ops=[In()],
                                comparators=[Name(id='DOMAIN_OPERATORS', ctx=Load())],
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
            name='is_leaf',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='element', annotation=None, type_comment=None),
                    arg(arg='internal', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[Constant(value=False, kind=None)],
            ),
            body=[
                Expr(
                    value=Constant(value=" Test whether an object is a valid domain term:\n        - is a list or tuple\n        - with 3 elements\n        - second element if a valid op\n\n        :param tuple element: a leaf in form (left, operator, right)\n        :param boolean internal: allow or not the 'inselect' internal operator\n            in the term. This should be always left to False.\n\n        Note: OLD TODO change the share wizard to use this function.\n    ", kind=None),
                ),
                Assign(
                    targets=[Name(id='INTERNAL_OPS', ctx=Store())],
                    value=BinOp(
                        left=Name(id='TERM_OPERATORS', ctx=Load()),
                        op=Add(),
                        right=Tuple(
                            elts=[Constant(value='<>', kind=None)],
                            ctx=Load(),
                        ),
                    ),
                    type_comment=None,
                ),
                If(
                    test=Name(id='internal', ctx=Load()),
                    body=[
                        AugAssign(
                            target=Name(id='INTERNAL_OPS', ctx=Store()),
                            op=Add(),
                            value=Tuple(
                                elts=[
                                    Constant(value='inselect', kind=None),
                                    Constant(value='not inselect', kind=None),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=BoolOp(
                        op=And(),
                        values=[
                            BoolOp(
                                op=Or(),
                                values=[
                                    Call(
                                        func=Name(id='isinstance', ctx=Load()),
                                        args=[
                                            Name(id='element', ctx=Load()),
                                            Name(id='tuple', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='isinstance', ctx=Load()),
                                        args=[
                                            Name(id='element', ctx=Load()),
                                            Name(id='list', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            Compare(
                                left=Call(
                                    func=Name(id='len', ctx=Load()),
                                    args=[Name(id='element', ctx=Load())],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value=3, kind=None)],
                            ),
                            Compare(
                                left=Subscript(
                                    value=Name(id='element', ctx=Load()),
                                    slice=Constant(value=1, kind=None),
                                    ctx=Load(),
                                ),
                                ops=[In()],
                                comparators=[Name(id='INTERNAL_OPS', ctx=Load())],
                            ),
                            BoolOp(
                                op=Or(),
                                values=[
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Call(
                                                func=Name(id='isinstance', ctx=Load()),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='element', ctx=Load()),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='str', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            Subscript(
                                                value=Name(id='element', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Compare(
                                        left=Call(
                                            func=Name(id='tuple', ctx=Load()),
                                            args=[Name(id='element', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ops=[In()],
                                        comparators=[
                                            Tuple(
                                                elts=[
                                                    Name(id='TRUE_LEAF', ctx=Load()),
                                                    Name(id='FALSE_LEAF', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
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
            name='is_boolean',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='element', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Return(
                    value=BoolOp(
                        op=Or(),
                        values=[
                            Compare(
                                left=Name(id='element', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Name(id='TRUE_LEAF', ctx=Load())],
                            ),
                            Compare(
                                left=Name(id='element', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Name(id='FALSE_LEAF', ctx=Load())],
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
            name='check_leaf',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='element', annotation=None, type_comment=None),
                    arg(arg='internal', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[Constant(value=False, kind=None)],
            ),
            body=[
                If(
                    test=BoolOp(
                        op=And(),
                        values=[
                            UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Name(id='is_operator', ctx=Load()),
                                    args=[Name(id='element', ctx=Load())],
                                    keywords=[],
                                ),
                            ),
                            UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Name(id='is_leaf', ctx=Load()),
                                    args=[
                                        Name(id='element', ctx=Load()),
                                        Name(id='internal', ctx=Load()),
                                    ],
                                    keywords=[],
                                ),
                            ),
                        ],
                    ),
                    body=[
                        Raise(
                            exc=Call(
                                func=Name(id='ValueError', ctx=Load()),
                                args=[
                                    BinOp(
                                        left=Constant(value='Invalid leaf %s', kind=None),
                                        op=Mod(),
                                        right=Call(
                                            func=Name(id='str', ctx=Load()),
                                            args=[Name(id='element', ctx=Load())],
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
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='get_unaccent_wrapper',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='cr', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                If(
                    test=Attribute(
                        value=Call(
                            func=Attribute(
                                value=Name(id='odoo', ctx=Load()),
                                attr='registry',
                                ctx=Load(),
                            ),
                            args=[
                                Attribute(
                                    value=Name(id='cr', ctx=Load()),
                                    attr='dbname',
                                    ctx=Load(),
                                ),
                            ],
                            keywords=[],
                        ),
                        attr='has_unaccent',
                        ctx=Load(),
                    ),
                    body=[
                        Return(
                            value=Lambda(
                                args=arguments(
                                    posonlyargs=[],
                                    args=[arg(arg='x', annotation=None, type_comment=None)],
                                    vararg=None,
                                    kwonlyargs=[],
                                    kw_defaults=[],
                                    kwarg=None,
                                    defaults=[],
                                ),
                                body=BinOp(
                                    left=Constant(value='unaccent(%s)', kind=None),
                                    op=Mod(),
                                    right=Tuple(
                                        elts=[Name(id='x', ctx=Load())],
                                        ctx=Load(),
                                    ),
                                ),
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Lambda(
                        args=arguments(
                            posonlyargs=[],
                            args=[arg(arg='x', annotation=None, type_comment=None)],
                            vararg=None,
                            kwonlyargs=[],
                            kw_defaults=[],
                            kwarg=None,
                            defaults=[],
                        ),
                        body=Name(id='x', ctx=Load()),
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        ClassDef(
            name='expression',
            bases=[Name(id='object', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=" Parse a domain expression\n        Use a real polish notation\n        Leafs are still in a ('foo', '=', 'bar') format\n        For more info: http://christophe-simonis-at-tiny.blogspot.com/2008/08/new-new-domain-notation.html\n    ", kind=None),
                ),
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='domain', annotation=None, type_comment=None),
                            arg(arg='model', annotation=None, type_comment=None),
                            arg(arg='alias', annotation=None, type_comment=None),
                            arg(arg='query', annotation=None, type_comment=None),
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
                            value=Constant(value=" Initialize expression object and automatically parse the expression\n            right after initialization.\n\n            :param domain: expression (using domain ('foo', '=', 'bar') format)\n            :param model: root model\n            :param alias: alias for the model table if query is provided\n            :param query: optional query object holding the final result\n\n            :attr root_model: base model for the query\n            :attr expression: the domain to parse, normalized and prepared\n            :attr result: the result of the parsing, as a pair (query, params)\n            :attr query: Query object holding the final result\n        ", kind=None),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_unaccent',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='get_unaccent_wrapper', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='model', ctx=Load()),
                                        attr='_cr',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='root_model',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='model', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='root_alias',
                                    ctx=Store(),
                                ),
                            ],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='alias', ctx=Load()),
                                    Attribute(
                                        value=Name(id='model', ctx=Load()),
                                        attr='_table',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='expression',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='distribute_not', ctx=Load()),
                                args=[
                                    Call(
                                        func=Name(id='normalize_domain', ctx=Load()),
                                        args=[Name(id='domain', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='query',
                                    ctx=Store(),
                                ),
                            ],
                            value=IfExp(
                                test=Compare(
                                    left=Name(id='query', ctx=Load()),
                                    ops=[Is()],
                                    comparators=[Constant(value=None, kind=None)],
                                ),
                                body=Call(
                                    func=Name(id='Query', ctx=Load()),
                                    args=[
                                        Attribute(
                                            value=Attribute(
                                                value=Name(id='model', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='cr',
                                            ctx=Load(),
                                        ),
                                        Attribute(
                                            value=Name(id='model', ctx=Load()),
                                            attr='_table',
                                            ctx=Load(),
                                        ),
                                        Attribute(
                                            value=Name(id='model', ctx=Load()),
                                            attr='_table_query',
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                orelse=Name(id='query', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='parse',
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
                    name='get_tables',
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
                                    Constant(value='deprecated expression.get_tables(), use expression.query instead', kind=None),
                                    Name(id='DeprecationWarning', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='query',
                                    ctx=Load(),
                                ),
                                attr='tables',
                                ctx=Load(),
                            ),
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
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Transform the leaves of the expression\n\n            The principle is to pop elements from a leaf stack one at a time.\n            Each leaf is processed. The processing is a if/elif list of various\n            cases that appear in the leafs (many2one, function fields, ...).\n            Three things can happen as a processing result:\n            - the leaf is a logic operator, and updates the result stack\n              accordingly;\n            - the leaf has been modified and/or new leafs have to be introduced\n              in the expression; they are pushed into the leaf stack, to be\n              processed right after;\n            - the leaf is converted to SQL and added to the result stack\n\n            Here is a suggested execution:\n\n                step                stack               result_stack\n\n                                    [\'&\', A, B]         []\n                substitute B        [\'&\', A, B1]        []\n                convert B1 in SQL   [\'&\', A]            ["B1"]\n                substitute A        [\'&\', \'|\', A1, A2]  ["B1"]\n                convert A2 in SQL   [\'&\', \'|\', A1]      ["B1", "A2"]\n                convert A1 in SQL   [\'&\', \'|\']          ["B1", "A2", "A1"]\n                apply operator OR   [\'&\']               ["B1", "A1 or A2"]\n                apply operator AND  []                  ["(A1 or A2) and B1"]\n\n            Some internal var explanation:\n                :var list path: left operand seen as a sequence of field names\n                    ("foo.bar" -> ["foo", "bar"])\n                :var obj model: model object, model containing the field\n                    (the name provided in the left operand)\n                :var obj field: the field corresponding to `path[0]`\n                :var obj column: the column corresponding to `path[0]`\n                :var obj comodel: relational model of field (field.comodel)\n                    (res_partner.bank_ids -> res.partner.bank)\n        ', kind=None),
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='cr', ctx=Store()),
                                        Name(id='uid', ctx=Store()),
                                        Name(id='context', ctx=Store()),
                                        Name(id='su', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='root_model',
                                        ctx=Load(),
                                    ),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                attr='args',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='to_ids',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='value', annotation=None, type_comment=None),
                                    arg(arg='comodel', annotation=None, type_comment=None),
                                    arg(arg='leaf', annotation=None, type_comment=None),
                                ],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Expr(
                                    value=Constant(value=' Normalize a single id or name, or a list of those, into a list of ids\n                :param {int,long,basestring,list,tuple} value:\n                    if int, long -> return [value]\n                    if basestring, convert it into a list of basestrings, then\n                    if list of basestring ->\n                        perform a name_search on comodel for each name\n                        return the list of related ids\n            ', kind=None),
                                ),
                                Assign(
                                    targets=[Name(id='names', ctx=Store())],
                                    value=List(elts=[], ctx=Load()),
                                    type_comment=None,
                                ),
                                If(
                                    test=Call(
                                        func=Name(id='isinstance', ctx=Load()),
                                        args=[
                                            Name(id='value', ctx=Load()),
                                            Name(id='str', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='names', ctx=Store())],
                                            value=List(
                                                elts=[Name(id='value', ctx=Load())],
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
                                                    Name(id='value', ctx=Load()),
                                                    Call(
                                                        func=Name(id='isinstance', ctx=Load()),
                                                        args=[
                                                            Name(id='value', ctx=Load()),
                                                            Tuple(
                                                                elts=[
                                                                    Name(id='tuple', ctx=Load()),
                                                                    Name(id='list', ctx=Load()),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Name(id='all', ctx=Load()),
                                                        args=[
                                                            GeneratorExp(
                                                                elt=Call(
                                                                    func=Name(id='isinstance', ctx=Load()),
                                                                    args=[
                                                                        Name(id='item', ctx=Load()),
                                                                        Name(id='str', ctx=Load()),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                                generators=[
                                                                    comprehension(
                                                                        target=Name(id='item', ctx=Store()),
                                                                        iter=Name(id='value', ctx=Load()),
                                                                        ifs=[],
                                                                        is_async=0,
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='names', ctx=Store())],
                                                    value=Name(id='value', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Call(
                                                        func=Name(id='isinstance', ctx=Load()),
                                                        args=[
                                                            Name(id='value', ctx=Load()),
                                                            Name(id='int', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    body=[
                                                        If(
                                                            test=UnaryOp(
                                                                op=Not(),
                                                                operand=Name(id='value', ctx=Load()),
                                                            ),
                                                            body=[
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='_logger', ctx=Load()),
                                                                            attr='warning',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Constant(value='Unexpected domain [%s], interpreted as False', kind=None),
                                                                            Name(id='leaf', ctx=Load()),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                                Return(
                                                                    value=List(elts=[], ctx=Load()),
                                                                ),
                                                            ],
                                                            orelse=[],
                                                        ),
                                                        Return(
                                                            value=List(
                                                                elts=[Name(id='value', ctx=Load())],
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
                                If(
                                    test=Name(id='names', ctx=Load()),
                                    body=[
                                        Return(
                                            value=Call(
                                                func=Name(id='list', ctx=Load()),
                                                args=[
                                                    SetComp(
                                                        elt=Name(id='rid', ctx=Load()),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='name', ctx=Store()),
                                                                iter=Name(id='names', ctx=Load()),
                                                                ifs=[],
                                                                is_async=0,
                                                            ),
                                                            comprehension(
                                                                target=Name(id='rid', ctx=Store()),
                                                                iter=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='comodel', ctx=Load()),
                                                                        attr='_name_search',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[
                                                                        Name(id='name', ctx=Load()),
                                                                        List(elts=[], ctx=Load()),
                                                                        Constant(value='ilike', kind=None),
                                                                    ],
                                                                    keywords=[
                                                                        keyword(
                                                                            arg='limit',
                                                                            value=Constant(value=None, kind=None),
                                                                        ),
                                                                    ],
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
                                    orelse=[],
                                ),
                                Return(
                                    value=Call(
                                        func=Name(id='list', ctx=Load()),
                                        args=[Name(id='value', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='child_of_domain',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='left', annotation=None, type_comment=None),
                                    arg(arg='ids', annotation=None, type_comment=None),
                                    arg(arg='left_model', annotation=None, type_comment=None),
                                    arg(arg='parent', annotation=None, type_comment=None),
                                    arg(arg='prefix', annotation=None, type_comment=None),
                                ],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[
                                    Constant(value=None, kind=None),
                                    Constant(value='', kind=None),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Constant(value=' Return a domain implementing the child_of operator for [(left,child_of,ids)],\n                either as a range using the parent_path tree lookup field\n                (when available), or as an expanded [(left,in,child_ids)] ', kind=None),
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='ids', ctx=Load()),
                                    ),
                                    body=[
                                        Return(
                                            value=List(
                                                elts=[Name(id='FALSE_LEAF', ctx=Load())],
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Attribute(
                                        value=Name(id='left_model', ctx=Load()),
                                        attr='_parent_store',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='domain', ctx=Store())],
                                            value=Call(
                                                func=Name(id='OR', ctx=Load()),
                                                args=[
                                                    ListComp(
                                                        elt=List(
                                                            elts=[
                                                                Tuple(
                                                                    elts=[
                                                                        Constant(value='parent_path', kind=None),
                                                                        Constant(value='=like', kind=None),
                                                                        BinOp(
                                                                            left=Attribute(
                                                                                value=Name(id='rec', ctx=Load()),
                                                                                attr='parent_path',
                                                                                ctx=Load(),
                                                                            ),
                                                                            op=Add(),
                                                                            right=Constant(value='%', kind=None),
                                                                        ),
                                                                    ],
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='rec', ctx=Store()),
                                                                iter=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='left_model', ctx=Load()),
                                                                        attr='browse',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[Name(id='ids', ctx=Load())],
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
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='parent_name', ctx=Store())],
                                            value=BoolOp(
                                                op=Or(),
                                                values=[
                                                    Name(id='parent', ctx=Load()),
                                                    Attribute(
                                                        value=Name(id='left_model', ctx=Load()),
                                                        attr='_parent_name',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='child_ids', ctx=Store())],
                                            value=Call(
                                                func=Name(id='set', ctx=Load()),
                                                args=[],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='records', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='left_model', ctx=Load()),
                                                            attr='sudo',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    attr='browse',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='ids', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        While(
                                            test=Name(id='records', ctx=Load()),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='child_ids', ctx=Load()),
                                                            attr='update',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='records', ctx=Load()),
                                                                attr='_ids',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Assign(
                                                    targets=[Name(id='records', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='records', ctx=Load()),
                                                            attr='search',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Name(id='parent_name', ctx=Load()),
                                                                            Constant(value='in', kind=None),
                                                                            Attribute(
                                                                                value=Name(id='records', ctx=Load()),
                                                                                attr='ids',
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
                                                                value=Constant(value='id', kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='domain', ctx=Store())],
                                            value=List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='id', kind=None),
                                                            Constant(value='in', kind=None),
                                                            Call(
                                                                func=Name(id='list', ctx=Load()),
                                                                args=[Name(id='child_ids', ctx=Load())],
                                                                keywords=[],
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
                                ),
                                If(
                                    test=Name(id='prefix', ctx=Load()),
                                    body=[
                                        Return(
                                            value=List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Name(id='left', ctx=Load()),
                                                            Constant(value='in', kind=None),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='left_model', ctx=Load()),
                                                                    attr='_search',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='domain', ctx=Load())],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='order',
                                                                        value=Constant(value='id', kind=None),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
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
                                    value=Name(id='domain', ctx=Load()),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='parent_of_domain',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='left', annotation=None, type_comment=None),
                                    arg(arg='ids', annotation=None, type_comment=None),
                                    arg(arg='left_model', annotation=None, type_comment=None),
                                    arg(arg='parent', annotation=None, type_comment=None),
                                    arg(arg='prefix', annotation=None, type_comment=None),
                                ],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[
                                    Constant(value=None, kind=None),
                                    Constant(value='', kind=None),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Constant(value=' Return a domain implementing the parent_of operator for [(left,parent_of,ids)],\n                either as a range using the parent_path tree lookup field\n                (when available), or as an expanded [(left,in,parent_ids)] ', kind=None),
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='ids', ctx=Load()),
                                    ),
                                    body=[
                                        Return(
                                            value=List(
                                                elts=[Name(id='FALSE_LEAF', ctx=Load())],
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Attribute(
                                        value=Name(id='left_model', ctx=Load()),
                                        attr='_parent_store',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='parent_ids', ctx=Store())],
                                            value=ListComp(
                                                elt=Call(
                                                    func=Name(id='int', ctx=Load()),
                                                    args=[Name(id='label', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='rec', ctx=Store()),
                                                        iter=Call(
                                                            func=Attribute(
                                                                value=Name(id='left_model', ctx=Load()),
                                                                attr='browse',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Name(id='ids', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                    comprehension(
                                                        target=Name(id='label', ctx=Store()),
                                                        iter=Subscript(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='rec', ctx=Load()),
                                                                        attr='parent_path',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='split',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='/', kind=None)],
                                                                keywords=[],
                                                            ),
                                                            slice=Slice(
                                                                lower=None,
                                                                upper=UnaryOp(
                                                                    op=USub(),
                                                                    operand=Constant(value=1, kind=None),
                                                                ),
                                                                step=None,
                                                            ),
                                                            ctx=Load(),
                                                        ),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='domain', ctx=Store())],
                                            value=List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='id', kind=None),
                                                            Constant(value='in', kind=None),
                                                            Name(id='parent_ids', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='parent_name', ctx=Store())],
                                            value=BoolOp(
                                                op=Or(),
                                                values=[
                                                    Name(id='parent', ctx=Load()),
                                                    Attribute(
                                                        value=Name(id='left_model', ctx=Load()),
                                                        attr='_parent_name',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='parent_ids', ctx=Store())],
                                            value=Call(
                                                func=Name(id='set', ctx=Load()),
                                                args=[],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='records', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='left_model', ctx=Load()),
                                                            attr='sudo',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    attr='browse',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='ids', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        While(
                                            test=Name(id='records', ctx=Load()),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='parent_ids', ctx=Load()),
                                                            attr='update',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='records', ctx=Load()),
                                                                attr='_ids',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Assign(
                                                    targets=[Name(id='records', ctx=Store())],
                                                    value=Subscript(
                                                        value=Name(id='records', ctx=Load()),
                                                        slice=Name(id='parent_name', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='domain', ctx=Store())],
                                            value=List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='id', kind=None),
                                                            Constant(value='in', kind=None),
                                                            Call(
                                                                func=Name(id='list', ctx=Load()),
                                                                args=[Name(id='parent_ids', ctx=Load())],
                                                                keywords=[],
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
                                ),
                                If(
                                    test=Name(id='prefix', ctx=Load()),
                                    body=[
                                        Return(
                                            value=List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Name(id='left', ctx=Load()),
                                                            Constant(value='in', kind=None),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='left_model', ctx=Load()),
                                                                    attr='_search',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='domain', ctx=Load())],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='order',
                                                                        value=Constant(value='id', kind=None),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
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
                                    value=Name(id='domain', ctx=Load()),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='HIERARCHY_FUNCS', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='child_of', kind=None),
                                    Constant(value='parent_of', kind=None),
                                ],
                                values=[
                                    Name(id='child_of_domain', ctx=Load()),
                                    Name(id='parent_of_domain', ctx=Load()),
                                ],
                            ),
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='pop',
                            args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
                            body=[
                                Expr(
                                    value=Constant(value=' Pop a leaf to process. ', kind=None),
                                ),
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='stack', ctx=Load()),
                                            attr='pop',
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
                            name='push',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='leaf', annotation=None, type_comment=None),
                                    arg(arg='model', annotation=None, type_comment=None),
                                    arg(arg='alias', annotation=None, type_comment=None),
                                    arg(arg='internal', annotation=None, type_comment=None),
                                ],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[Constant(value=False, kind=None)],
                            ),
                            body=[
                                Expr(
                                    value=Constant(value=' Push a leaf to be processed right after. ', kind=None),
                                ),
                                Assign(
                                    targets=[Name(id='leaf', ctx=Store())],
                                    value=Call(
                                        func=Name(id='normalize_leaf', ctx=Load()),
                                        args=[Name(id='leaf', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Name(id='check_leaf', ctx=Load()),
                                        args=[
                                            Name(id='leaf', ctx=Load()),
                                            Name(id='internal', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='stack', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Tuple(
                                                elts=[
                                                    Name(id='leaf', ctx=Load()),
                                                    Name(id='model', ctx=Load()),
                                                    Name(id='alias', ctx=Load()),
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
                            name='pop_result',
                            args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='result_stack', ctx=Load()),
                                            attr='pop',
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
                            name='push_result',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='query', annotation=None, type_comment=None),
                                    arg(arg='params', annotation=None, type_comment=None),
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
                                            value=Name(id='result_stack', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Tuple(
                                                elts=[
                                                    Name(id='query', ctx=Load()),
                                                    Name(id='params', ctx=Load()),
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
                        Assign(
                            targets=[Name(id='stack', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='leaf', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='expression',
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='push', ctx=Load()),
                                        args=[
                                            Name(id='leaf', ctx=Load()),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='root_model',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='root_alias',
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
                        Assign(
                            targets=[Name(id='result_stack', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        While(
                            test=Name(id='stack', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='leaf', ctx=Store()),
                                                Name(id='model', ctx=Store()),
                                                Name(id='alias', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='pop', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Call(
                                        func=Name(id='is_operator', ctx=Load()),
                                        args=[Name(id='leaf', ctx=Load())],
                                        keywords=[],
                                    ),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Name(id='leaf', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Name(id='NOT_OPERATOR', ctx=Load())],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Tuple(
                                                            elts=[
                                                                Name(id='expr', ctx=Store()),
                                                                Name(id='params', ctx=Store()),
                                                            ],
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Call(
                                                        func=Name(id='pop_result', ctx=Load()),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Name(id='push_result', ctx=Load()),
                                                        args=[
                                                            BinOp(
                                                                left=Constant(value='(NOT (%s))', kind=None),
                                                                op=Mod(),
                                                                right=Name(id='expr', ctx=Load()),
                                                            ),
                                                            Name(id='params', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[Name(id='ops', ctx=Store())],
                                                    value=Dict(
                                                        keys=[
                                                            Name(id='AND_OPERATOR', ctx=Load()),
                                                            Name(id='OR_OPERATOR', ctx=Load()),
                                                        ],
                                                        values=[
                                                            Constant(value='(%s AND %s)', kind=None),
                                                            Constant(value='(%s OR %s)', kind=None),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[
                                                        Tuple(
                                                            elts=[
                                                                Name(id='lhs', ctx=Store()),
                                                                Name(id='lhs_params', ctx=Store()),
                                                            ],
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Call(
                                                        func=Name(id='pop_result', ctx=Load()),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[
                                                        Tuple(
                                                            elts=[
                                                                Name(id='rhs', ctx=Store()),
                                                                Name(id='rhs_params', ctx=Store()),
                                                            ],
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Call(
                                                        func=Name(id='pop_result', ctx=Load()),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Name(id='push_result', ctx=Load()),
                                                        args=[
                                                            BinOp(
                                                                left=Subscript(
                                                                    value=Name(id='ops', ctx=Load()),
                                                                    slice=Name(id='leaf', ctx=Load()),
                                                                    ctx=Load(),
                                                                ),
                                                                op=Mod(),
                                                                right=Tuple(
                                                                    elts=[
                                                                        Name(id='lhs', ctx=Load()),
                                                                        Name(id='rhs', ctx=Load()),
                                                                    ],
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            BinOp(
                                                                left=Name(id='lhs_params', ctx=Load()),
                                                                op=Add(),
                                                                right=Name(id='rhs_params', ctx=Load()),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                        Continue(),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Call(
                                        func=Name(id='is_boolean', ctx=Load()),
                                        args=[Name(id='leaf', ctx=Load())],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Tuple(
                                                    elts=[
                                                        Name(id='expr', ctx=Store()),
                                                        Name(id='params', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='__leaf_to_sql',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='leaf', ctx=Load()),
                                                    Name(id='model', ctx=Load()),
                                                    Name(id='alias', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Name(id='push_result', ctx=Load()),
                                                args=[
                                                    Name(id='expr', ctx=Load()),
                                                    Name(id='params', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Continue(),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='left', ctx=Store()),
                                                Name(id='operator', ctx=Store()),
                                                Name(id='right', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='leaf', ctx=Load()),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='path', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='left', ctx=Load()),
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
                                            Subscript(
                                                value=Name(id='path', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='comodel', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='model', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='getattr', ctx=Load()),
                                                args=[
                                                    Name(id='field', ctx=Load()),
                                                    Constant(value='comodel_name', kind=None),
                                                    Constant(value=None, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='field', ctx=Load()),
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='ValueError', ctx=Load()),
                                                args=[
                                                    BinOp(
                                                        left=Constant(value='Invalid field %s.%s in leaf %s', kind=None),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            elts=[
                                                                Attribute(
                                                                    value=Name(id='model', ctx=Load()),
                                                                    attr='_name',
                                                                    ctx=Load(),
                                                                ),
                                                                Subscript(
                                                                    value=Name(id='path', ctx=Load()),
                                                                    slice=Constant(value=0, kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                Call(
                                                                    func=Name(id='str', ctx=Load()),
                                                                    args=[Name(id='leaf', ctx=Load())],
                                                                    keywords=[],
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
                                    orelse=[
                                        If(
                                            test=Attribute(
                                                value=Name(id='field', ctx=Load()),
                                                attr='inherited',
                                                ctx=Load(),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='parent_model', ctx=Store())],
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='model', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='field', ctx=Load()),
                                                                attr='related_field',
                                                                ctx=Load(),
                                                            ),
                                                            attr='model_name',
                                                            ctx=Load(),
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='parent_fname', ctx=Store())],
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='model', ctx=Load()),
                                                            attr='_inherits',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Attribute(
                                                            value=Name(id='parent_model', ctx=Load()),
                                                            attr='_name',
                                                            ctx=Load(),
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='parent_alias', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='query',
                                                                ctx=Load(),
                                                            ),
                                                            attr='left_join',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='alias', ctx=Load()),
                                                            Name(id='parent_fname', ctx=Load()),
                                                            Attribute(
                                                                value=Name(id='parent_model', ctx=Load()),
                                                                attr='_table',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='id', kind=None),
                                                            Name(id='parent_fname', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Name(id='push', ctx=Load()),
                                                        args=[
                                                            Name(id='leaf', ctx=Load()),
                                                            Name(id='parent_model', ctx=Load()),
                                                            Name(id='parent_alias', ctx=Load()),
                                                        ],
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
                                                                left=Name(id='left', ctx=Load()),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='id', kind=None)],
                                                            ),
                                                            Compare(
                                                                left=Name(id='operator', ctx=Load()),
                                                                ops=[In()],
                                                                comparators=[Name(id='HIERARCHY_FUNCS', ctx=Load())],
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='ids2', ctx=Store())],
                                                            value=Call(
                                                                func=Name(id='to_ids', ctx=Load()),
                                                                args=[
                                                                    Name(id='right', ctx=Load()),
                                                                    Name(id='model', ctx=Load()),
                                                                    Name(id='leaf', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='dom', ctx=Store())],
                                                            value=Call(
                                                                func=Subscript(
                                                                    value=Name(id='HIERARCHY_FUNCS', ctx=Load()),
                                                                    slice=Name(id='operator', ctx=Load()),
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Name(id='left', ctx=Load()),
                                                                    Name(id='ids2', ctx=Load()),
                                                                    Name(id='model', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        For(
                                                            target=Name(id='dom_leaf', ctx=Store()),
                                                            iter=Name(id='dom', ctx=Load()),
                                                            body=[
                                                                Expr(
                                                                    value=Call(
                                                                        func=Name(id='push', ctx=Load()),
                                                                        args=[
                                                                            Name(id='dom_leaf', ctx=Load()),
                                                                            Name(id='model', ctx=Load()),
                                                                            Name(id='alias', ctx=Load()),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                            ],
                                                            orelse=[],
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[
                                                        If(
                                                            test=BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    Compare(
                                                                        left=Call(
                                                                            func=Name(id='len', ctx=Load()),
                                                                            args=[Name(id='path', ctx=Load())],
                                                                            keywords=[],
                                                                        ),
                                                                        ops=[Gt()],
                                                                        comparators=[Constant(value=1, kind=None)],
                                                                    ),
                                                                    Attribute(
                                                                        value=Name(id='field', ctx=Load()),
                                                                        attr='store',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Compare(
                                                                        left=Attribute(
                                                                            value=Name(id='field', ctx=Load()),
                                                                            attr='type',
                                                                            ctx=Load(),
                                                                        ),
                                                                        ops=[Eq()],
                                                                        comparators=[Constant(value='many2one', kind=None)],
                                                                    ),
                                                                    Attribute(
                                                                        value=Name(id='field', ctx=Load()),
                                                                        attr='auto_join',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='coalias', ctx=Store())],
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='query',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='left_join',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Name(id='alias', ctx=Load()),
                                                                            Subscript(
                                                                                value=Name(id='path', ctx=Load()),
                                                                                slice=Constant(value=0, kind=None),
                                                                                ctx=Load(),
                                                                            ),
                                                                            Attribute(
                                                                                value=Name(id='comodel', ctx=Load()),
                                                                                attr='_table',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value='id', kind=None),
                                                                            Subscript(
                                                                                value=Name(id='path', ctx=Load()),
                                                                                slice=Constant(value=0, kind=None),
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                                Expr(
                                                                    value=Call(
                                                                        func=Name(id='push', ctx=Load()),
                                                                        args=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Subscript(
                                                                                        value=Name(id='path', ctx=Load()),
                                                                                        slice=Constant(value=1, kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Name(id='operator', ctx=Load()),
                                                                                    Name(id='right', ctx=Load()),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                            Name(id='comodel', ctx=Load()),
                                                                            Name(id='coalias', ctx=Load()),
                                                                        ],
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
                                                                                left=Call(
                                                                                    func=Name(id='len', ctx=Load()),
                                                                                    args=[Name(id='path', ctx=Load())],
                                                                                    keywords=[],
                                                                                ),
                                                                                ops=[Gt()],
                                                                                comparators=[Constant(value=1, kind=None)],
                                                                            ),
                                                                            Attribute(
                                                                                value=Name(id='field', ctx=Load()),
                                                                                attr='store',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Compare(
                                                                                left=Attribute(
                                                                                    value=Name(id='field', ctx=Load()),
                                                                                    attr='type',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                ops=[Eq()],
                                                                                comparators=[Constant(value='one2many', kind=None)],
                                                                            ),
                                                                            Attribute(
                                                                                value=Name(id='field', ctx=Load()),
                                                                                attr='auto_join',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                    body=[
                                                                        Assign(
                                                                            targets=[Name(id='domain', ctx=Store())],
                                                                            value=BinOp(
                                                                                left=List(
                                                                                    elts=[
                                                                                        Tuple(
                                                                                            elts=[
                                                                                                Subscript(
                                                                                                    value=Name(id='path', ctx=Load()),
                                                                                                    slice=Constant(value=1, kind=None),
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                Name(id='operator', ctx=Load()),
                                                                                                Name(id='right', ctx=Load()),
                                                                                            ],
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                    ],
                                                                                    ctx=Load(),
                                                                                ),
                                                                                op=Add(),
                                                                                right=Call(
                                                                                    func=Attribute(
                                                                                        value=Name(id='field', ctx=Load()),
                                                                                        attr='get_domain_list',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    args=[Name(id='model', ctx=Load())],
                                                                                    keywords=[],
                                                                                ),
                                                                            ),
                                                                            type_comment=None,
                                                                        ),
                                                                        Assign(
                                                                            targets=[Name(id='query', ctx=Store())],
                                                                            value=Call(
                                                                                func=Attribute(
                                                                                    value=Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='comodel', ctx=Load()),
                                                                                            attr='with_context',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[],
                                                                                        keywords=[
                                                                                            keyword(
                                                                                                arg=None,
                                                                                                value=Attribute(
                                                                                                    value=Name(id='field', ctx=Load()),
                                                                                                    attr='context',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                            ),
                                                                                        ],
                                                                                    ),
                                                                                    attr='_where_calc',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[Name(id='domain', ctx=Load())],
                                                                                keywords=[],
                                                                            ),
                                                                            type_comment=None,
                                                                        ),
                                                                        Assign(
                                                                            targets=[
                                                                                Tuple(
                                                                                    elts=[
                                                                                        Name(id='subquery', ctx=Store()),
                                                                                        Name(id='subparams', ctx=Store()),
                                                                                    ],
                                                                                    ctx=Store(),
                                                                                ),
                                                                            ],
                                                                            value=Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='query', ctx=Load()),
                                                                                    attr='select',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[
                                                                                    BinOp(
                                                                                        left=Constant(value='"%s"."%s"', kind=None),
                                                                                        op=Mod(),
                                                                                        right=Tuple(
                                                                                            elts=[
                                                                                                Attribute(
                                                                                                    value=Name(id='comodel', ctx=Load()),
                                                                                                    attr='_table',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                Attribute(
                                                                                                    value=Name(id='field', ctx=Load()),
                                                                                                    attr='inverse_name',
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
                                                                        Expr(
                                                                            value=Call(
                                                                                func=Name(id='push', ctx=Load()),
                                                                                args=[
                                                                                    Tuple(
                                                                                        elts=[
                                                                                            Constant(value='id', kind=None),
                                                                                            Constant(value='inselect', kind=None),
                                                                                            Tuple(
                                                                                                elts=[
                                                                                                    Name(id='subquery', ctx=Load()),
                                                                                                    Name(id='subparams', ctx=Load()),
                                                                                                ],
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                        ],
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Name(id='model', ctx=Load()),
                                                                                    Name(id='alias', ctx=Load()),
                                                                                ],
                                                                                keywords=[
                                                                                    keyword(
                                                                                        arg='internal',
                                                                                        value=Constant(value=True, kind=None),
                                                                                    ),
                                                                                ],
                                                                            ),
                                                                        ),
                                                                    ],
                                                                    orelse=[
                                                                        If(
                                                                            test=BoolOp(
                                                                                op=And(),
                                                                                values=[
                                                                                    Compare(
                                                                                        left=Call(
                                                                                            func=Name(id='len', ctx=Load()),
                                                                                            args=[Name(id='path', ctx=Load())],
                                                                                            keywords=[],
                                                                                        ),
                                                                                        ops=[Gt()],
                                                                                        comparators=[Constant(value=1, kind=None)],
                                                                                    ),
                                                                                    Attribute(
                                                                                        value=Name(id='field', ctx=Load()),
                                                                                        attr='store',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Attribute(
                                                                                        value=Name(id='field', ctx=Load()),
                                                                                        attr='auto_join',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                            ),
                                                                            body=[
                                                                                Raise(
                                                                                    exc=Call(
                                                                                        func=Name(id='NotImplementedError', ctx=Load()),
                                                                                        args=[
                                                                                            BinOp(
                                                                                                left=Constant(value='auto_join attribute not supported on field %s', kind=None),
                                                                                                op=Mod(),
                                                                                                right=Name(id='field', ctx=Load()),
                                                                                            ),
                                                                                        ],
                                                                                        keywords=[],
                                                                                    ),
                                                                                    cause=None,
                                                                                ),
                                                                            ],
                                                                            orelse=[
                                                                                If(
                                                                                    test=BoolOp(
                                                                                        op=And(),
                                                                                        values=[
                                                                                            Compare(
                                                                                                left=Call(
                                                                                                    func=Name(id='len', ctx=Load()),
                                                                                                    args=[Name(id='path', ctx=Load())],
                                                                                                    keywords=[],
                                                                                                ),
                                                                                                ops=[Gt()],
                                                                                                comparators=[Constant(value=1, kind=None)],
                                                                                            ),
                                                                                            Attribute(
                                                                                                value=Name(id='field', ctx=Load()),
                                                                                                attr='store',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Compare(
                                                                                                left=Attribute(
                                                                                                    value=Name(id='field', ctx=Load()),
                                                                                                    attr='type',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                ops=[Eq()],
                                                                                                comparators=[Constant(value='many2one', kind=None)],
                                                                                            ),
                                                                                        ],
                                                                                    ),
                                                                                    body=[
                                                                                        Assign(
                                                                                            targets=[Name(id='right_ids', ctx=Store())],
                                                                                            value=Call(
                                                                                                func=Attribute(
                                                                                                    value=Call(
                                                                                                        func=Attribute(
                                                                                                            value=Name(id='comodel', ctx=Load()),
                                                                                                            attr='with_context',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        args=[],
                                                                                                        keywords=[
                                                                                                            keyword(
                                                                                                                arg='active_test',
                                                                                                                value=Constant(value=False, kind=None),
                                                                                                            ),
                                                                                                        ],
                                                                                                    ),
                                                                                                    attr='_search',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                args=[
                                                                                                    List(
                                                                                                        elts=[
                                                                                                            Tuple(
                                                                                                                elts=[
                                                                                                                    Subscript(
                                                                                                                        value=Name(id='path', ctx=Load()),
                                                                                                                        slice=Constant(value=1, kind=None),
                                                                                                                        ctx=Load(),
                                                                                                                    ),
                                                                                                                    Name(id='operator', ctx=Load()),
                                                                                                                    Name(id='right', ctx=Load()),
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
                                                                                                        value=Constant(value='id', kind=None),
                                                                                                    ),
                                                                                                ],
                                                                                            ),
                                                                                            type_comment=None,
                                                                                        ),
                                                                                        Expr(
                                                                                            value=Call(
                                                                                                func=Name(id='push', ctx=Load()),
                                                                                                args=[
                                                                                                    Tuple(
                                                                                                        elts=[
                                                                                                            Subscript(
                                                                                                                value=Name(id='path', ctx=Load()),
                                                                                                                slice=Constant(value=0, kind=None),
                                                                                                                ctx=Load(),
                                                                                                            ),
                                                                                                            Constant(value='in', kind=None),
                                                                                                            Name(id='right_ids', ctx=Load()),
                                                                                                        ],
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Name(id='model', ctx=Load()),
                                                                                                    Name(id='alias', ctx=Load()),
                                                                                                ],
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
                                                                                                        left=Call(
                                                                                                            func=Name(id='len', ctx=Load()),
                                                                                                            args=[Name(id='path', ctx=Load())],
                                                                                                            keywords=[],
                                                                                                        ),
                                                                                                        ops=[Gt()],
                                                                                                        comparators=[Constant(value=1, kind=None)],
                                                                                                    ),
                                                                                                    Attribute(
                                                                                                        value=Name(id='field', ctx=Load()),
                                                                                                        attr='store',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Compare(
                                                                                                        left=Attribute(
                                                                                                            value=Name(id='field', ctx=Load()),
                                                                                                            attr='type',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        ops=[In()],
                                                                                                        comparators=[
                                                                                                            Tuple(
                                                                                                                elts=[
                                                                                                                    Constant(value='many2many', kind=None),
                                                                                                                    Constant(value='one2many', kind=None),
                                                                                                                ],
                                                                                                                ctx=Load(),
                                                                                                            ),
                                                                                                        ],
                                                                                                    ),
                                                                                                ],
                                                                                            ),
                                                                                            body=[
                                                                                                Assign(
                                                                                                    targets=[Name(id='right_ids', ctx=Store())],
                                                                                                    value=Call(
                                                                                                        func=Attribute(
                                                                                                            value=Call(
                                                                                                                func=Attribute(
                                                                                                                    value=Name(id='comodel', ctx=Load()),
                                                                                                                    attr='with_context',
                                                                                                                    ctx=Load(),
                                                                                                                ),
                                                                                                                args=[],
                                                                                                                keywords=[
                                                                                                                    keyword(
                                                                                                                        arg=None,
                                                                                                                        value=Attribute(
                                                                                                                            value=Name(id='field', ctx=Load()),
                                                                                                                            attr='context',
                                                                                                                            ctx=Load(),
                                                                                                                        ),
                                                                                                                    ),
                                                                                                                ],
                                                                                                            ),
                                                                                                            attr='_search',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        args=[
                                                                                                            List(
                                                                                                                elts=[
                                                                                                                    Tuple(
                                                                                                                        elts=[
                                                                                                                            Subscript(
                                                                                                                                value=Name(id='path', ctx=Load()),
                                                                                                                                slice=Constant(value=1, kind=None),
                                                                                                                                ctx=Load(),
                                                                                                                            ),
                                                                                                                            Name(id='operator', ctx=Load()),
                                                                                                                            Name(id='right', ctx=Load()),
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
                                                                                                                value=Constant(value='id', kind=None),
                                                                                                            ),
                                                                                                        ],
                                                                                                    ),
                                                                                                    type_comment=None,
                                                                                                ),
                                                                                                Expr(
                                                                                                    value=Call(
                                                                                                        func=Name(id='push', ctx=Load()),
                                                                                                        args=[
                                                                                                            Tuple(
                                                                                                                elts=[
                                                                                                                    Subscript(
                                                                                                                        value=Name(id='path', ctx=Load()),
                                                                                                                        slice=Constant(value=0, kind=None),
                                                                                                                        ctx=Load(),
                                                                                                                    ),
                                                                                                                    Constant(value='in', kind=None),
                                                                                                                    Name(id='right_ids', ctx=Load()),
                                                                                                                ],
                                                                                                                ctx=Load(),
                                                                                                            ),
                                                                                                            Name(id='model', ctx=Load()),
                                                                                                            Name(id='alias', ctx=Load()),
                                                                                                        ],
                                                                                                        keywords=[],
                                                                                                    ),
                                                                                                ),
                                                                                            ],
                                                                                            orelse=[
                                                                                                If(
                                                                                                    test=UnaryOp(
                                                                                                        op=Not(),
                                                                                                        operand=Attribute(
                                                                                                            value=Name(id='field', ctx=Load()),
                                                                                                            attr='store',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                    ),
                                                                                                    body=[
                                                                                                        If(
                                                                                                            test=UnaryOp(
                                                                                                                op=Not(),
                                                                                                                operand=Attribute(
                                                                                                                    value=Name(id='field', ctx=Load()),
                                                                                                                    attr='search',
                                                                                                                    ctx=Load(),
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
                                                                                                                        args=[
                                                                                                                            Constant(value='Non-stored field %s cannot be searched.', kind=None),
                                                                                                                            Name(id='field', ctx=Load()),
                                                                                                                        ],
                                                                                                                        keywords=[],
                                                                                                                    ),
                                                                                                                ),
                                                                                                                If(
                                                                                                                    test=Call(
                                                                                                                        func=Attribute(
                                                                                                                            value=Name(id='_logger', ctx=Load()),
                                                                                                                            attr='isEnabledFor',
                                                                                                                            ctx=Load(),
                                                                                                                        ),
                                                                                                                        args=[
                                                                                                                            Attribute(
                                                                                                                                value=Name(id='logging', ctx=Load()),
                                                                                                                                attr='DEBUG',
                                                                                                                                ctx=Load(),
                                                                                                                            ),
                                                                                                                        ],
                                                                                                                        keywords=[],
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
                                                                                                                                    Call(
                                                                                                                                        func=Attribute(
                                                                                                                                            value=Constant(value='', kind=None),
                                                                                                                                            attr='join',
                                                                                                                                            ctx=Load(),
                                                                                                                                        ),
                                                                                                                                        args=[
                                                                                                                                            Call(
                                                                                                                                                func=Attribute(
                                                                                                                                                    value=Name(id='traceback', ctx=Load()),
                                                                                                                                                    attr='format_stack',
                                                                                                                                                    ctx=Load(),
                                                                                                                                                ),
                                                                                                                                                args=[],
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
                                                                                                                    orelse=[],
                                                                                                                ),
                                                                                                                Assign(
                                                                                                                    targets=[Name(id='domain', ctx=Store())],
                                                                                                                    value=List(elts=[], ctx=Load()),
                                                                                                                    type_comment=None,
                                                                                                                ),
                                                                                                            ],
                                                                                                            orelse=[
                                                                                                                If(
                                                                                                                    test=Compare(
                                                                                                                        left=Call(
                                                                                                                            func=Name(id='len', ctx=Load()),
                                                                                                                            args=[Name(id='path', ctx=Load())],
                                                                                                                            keywords=[],
                                                                                                                        ),
                                                                                                                        ops=[Gt()],
                                                                                                                        comparators=[Constant(value=1, kind=None)],
                                                                                                                    ),
                                                                                                                    body=[
                                                                                                                        Assign(
                                                                                                                            targets=[Name(id='right', ctx=Store())],
                                                                                                                            value=Call(
                                                                                                                                func=Attribute(
                                                                                                                                    value=Name(id='comodel', ctx=Load()),
                                                                                                                                    attr='_search',
                                                                                                                                    ctx=Load(),
                                                                                                                                ),
                                                                                                                                args=[
                                                                                                                                    List(
                                                                                                                                        elts=[
                                                                                                                                            Tuple(
                                                                                                                                                elts=[
                                                                                                                                                    Subscript(
                                                                                                                                                        value=Name(id='path', ctx=Load()),
                                                                                                                                                        slice=Constant(value=1, kind=None),
                                                                                                                                                        ctx=Load(),
                                                                                                                                                    ),
                                                                                                                                                    Name(id='operator', ctx=Load()),
                                                                                                                                                    Name(id='right', ctx=Load()),
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
                                                                                                                                        value=Constant(value='id', kind=None),
                                                                                                                                    ),
                                                                                                                                ],
                                                                                                                            ),
                                                                                                                            type_comment=None,
                                                                                                                        ),
                                                                                                                        Assign(
                                                                                                                            targets=[Name(id='operator', ctx=Store())],
                                                                                                                            value=Constant(value='in', kind=None),
                                                                                                                            type_comment=None,
                                                                                                                        ),
                                                                                                                    ],
                                                                                                                    orelse=[],
                                                                                                                ),
                                                                                                                Assign(
                                                                                                                    targets=[Name(id='domain', ctx=Store())],
                                                                                                                    value=Call(
                                                                                                                        func=Attribute(
                                                                                                                            value=Name(id='field', ctx=Load()),
                                                                                                                            attr='determine_domain',
                                                                                                                            ctx=Load(),
                                                                                                                        ),
                                                                                                                        args=[
                                                                                                                            Name(id='model', ctx=Load()),
                                                                                                                            Name(id='operator', ctx=Load()),
                                                                                                                            Name(id='right', ctx=Load()),
                                                                                                                        ],
                                                                                                                        keywords=[],
                                                                                                                    ),
                                                                                                                    type_comment=None,
                                                                                                                ),
                                                                                                                Expr(
                                                                                                                    value=Call(
                                                                                                                        func=Attribute(
                                                                                                                            value=Name(id='model', ctx=Load()),
                                                                                                                            attr='_flush_search',
                                                                                                                            ctx=Load(),
                                                                                                                        ),
                                                                                                                        args=[Name(id='domain', ctx=Load())],
                                                                                                                        keywords=[
                                                                                                                            keyword(
                                                                                                                                arg='order',
                                                                                                                                value=Constant(value='id', kind=None),
                                                                                                                            ),
                                                                                                                        ],
                                                                                                                    ),
                                                                                                                ),
                                                                                                            ],
                                                                                                        ),
                                                                                                        For(
                                                                                                            target=Name(id='elem', ctx=Store()),
                                                                                                            iter=Call(
                                                                                                                func=Name(id='normalize_domain', ctx=Load()),
                                                                                                                args=[Name(id='domain', ctx=Load())],
                                                                                                                keywords=[],
                                                                                                            ),
                                                                                                            body=[
                                                                                                                Expr(
                                                                                                                    value=Call(
                                                                                                                        func=Name(id='push', ctx=Load()),
                                                                                                                        args=[
                                                                                                                            Name(id='elem', ctx=Load()),
                                                                                                                            Name(id='model', ctx=Load()),
                                                                                                                            Name(id='alias', ctx=Load()),
                                                                                                                        ],
                                                                                                                        keywords=[
                                                                                                                            keyword(
                                                                                                                                arg='internal',
                                                                                                                                value=Constant(value=True, kind=None),
                                                                                                                            ),
                                                                                                                        ],
                                                                                                                    ),
                                                                                                                ),
                                                                                                            ],
                                                                                                            orelse=[],
                                                                                                            type_comment=None,
                                                                                                        ),
                                                                                                    ],
                                                                                                    orelse=[
                                                                                                        If(
                                                                                                            test=BoolOp(
                                                                                                                op=And(),
                                                                                                                values=[
                                                                                                                    Compare(
                                                                                                                        left=Attribute(
                                                                                                                            value=Name(id='field', ctx=Load()),
                                                                                                                            attr='type',
                                                                                                                            ctx=Load(),
                                                                                                                        ),
                                                                                                                        ops=[Eq()],
                                                                                                                        comparators=[Constant(value='one2many', kind=None)],
                                                                                                                    ),
                                                                                                                    Compare(
                                                                                                                        left=Name(id='operator', ctx=Load()),
                                                                                                                        ops=[In()],
                                                                                                                        comparators=[Name(id='HIERARCHY_FUNCS', ctx=Load())],
                                                                                                                    ),
                                                                                                                ],
                                                                                                            ),
                                                                                                            body=[
                                                                                                                Assign(
                                                                                                                    targets=[Name(id='ids2', ctx=Store())],
                                                                                                                    value=Call(
                                                                                                                        func=Name(id='to_ids', ctx=Load()),
                                                                                                                        args=[
                                                                                                                            Name(id='right', ctx=Load()),
                                                                                                                            Name(id='comodel', ctx=Load()),
                                                                                                                            Name(id='leaf', ctx=Load()),
                                                                                                                        ],
                                                                                                                        keywords=[],
                                                                                                                    ),
                                                                                                                    type_comment=None,
                                                                                                                ),
                                                                                                                If(
                                                                                                                    test=Compare(
                                                                                                                        left=Attribute(
                                                                                                                            value=Name(id='field', ctx=Load()),
                                                                                                                            attr='comodel_name',
                                                                                                                            ctx=Load(),
                                                                                                                        ),
                                                                                                                        ops=[NotEq()],
                                                                                                                        comparators=[
                                                                                                                            Attribute(
                                                                                                                                value=Name(id='model', ctx=Load()),
                                                                                                                                attr='_name',
                                                                                                                                ctx=Load(),
                                                                                                                            ),
                                                                                                                        ],
                                                                                                                    ),
                                                                                                                    body=[
                                                                                                                        Assign(
                                                                                                                            targets=[Name(id='dom', ctx=Store())],
                                                                                                                            value=Call(
                                                                                                                                func=Subscript(
                                                                                                                                    value=Name(id='HIERARCHY_FUNCS', ctx=Load()),
                                                                                                                                    slice=Name(id='operator', ctx=Load()),
                                                                                                                                    ctx=Load(),
                                                                                                                                ),
                                                                                                                                args=[
                                                                                                                                    Name(id='left', ctx=Load()),
                                                                                                                                    Name(id='ids2', ctx=Load()),
                                                                                                                                    Name(id='comodel', ctx=Load()),
                                                                                                                                ],
                                                                                                                                keywords=[
                                                                                                                                    keyword(
                                                                                                                                        arg='prefix',
                                                                                                                                        value=Attribute(
                                                                                                                                            value=Name(id='field', ctx=Load()),
                                                                                                                                            attr='comodel_name',
                                                                                                                                            ctx=Load(),
                                                                                                                                        ),
                                                                                                                                    ),
                                                                                                                                ],
                                                                                                                            ),
                                                                                                                            type_comment=None,
                                                                                                                        ),
                                                                                                                    ],
                                                                                                                    orelse=[
                                                                                                                        Assign(
                                                                                                                            targets=[Name(id='dom', ctx=Store())],
                                                                                                                            value=Call(
                                                                                                                                func=Subscript(
                                                                                                                                    value=Name(id='HIERARCHY_FUNCS', ctx=Load()),
                                                                                                                                    slice=Name(id='operator', ctx=Load()),
                                                                                                                                    ctx=Load(),
                                                                                                                                ),
                                                                                                                                args=[
                                                                                                                                    Constant(value='id', kind=None),
                                                                                                                                    Name(id='ids2', ctx=Load()),
                                                                                                                                    Name(id='model', ctx=Load()),
                                                                                                                                ],
                                                                                                                                keywords=[
                                                                                                                                    keyword(
                                                                                                                                        arg='parent',
                                                                                                                                        value=Name(id='left', ctx=Load()),
                                                                                                                                    ),
                                                                                                                                ],
                                                                                                                            ),
                                                                                                                            type_comment=None,
                                                                                                                        ),
                                                                                                                    ],
                                                                                                                ),
                                                                                                                For(
                                                                                                                    target=Name(id='dom_leaf', ctx=Store()),
                                                                                                                    iter=Name(id='dom', ctx=Load()),
                                                                                                                    body=[
                                                                                                                        Expr(
                                                                                                                            value=Call(
                                                                                                                                func=Name(id='push', ctx=Load()),
                                                                                                                                args=[
                                                                                                                                    Name(id='dom_leaf', ctx=Load()),
                                                                                                                                    Name(id='model', ctx=Load()),
                                                                                                                                    Name(id='alias', ctx=Load()),
                                                                                                                                ],
                                                                                                                                keywords=[],
                                                                                                                            ),
                                                                                                                        ),
                                                                                                                    ],
                                                                                                                    orelse=[],
                                                                                                                    type_comment=None,
                                                                                                                ),
                                                                                                            ],
                                                                                                            orelse=[
                                                                                                                If(
                                                                                                                    test=Compare(
                                                                                                                        left=Attribute(
                                                                                                                            value=Name(id='field', ctx=Load()),
                                                                                                                            attr='type',
                                                                                                                            ctx=Load(),
                                                                                                                        ),
                                                                                                                        ops=[Eq()],
                                                                                                                        comparators=[Constant(value='one2many', kind=None)],
                                                                                                                    ),
                                                                                                                    body=[
                                                                                                                        Assign(
                                                                                                                            targets=[Name(id='domain', ctx=Store())],
                                                                                                                            value=Call(
                                                                                                                                func=Attribute(
                                                                                                                                    value=Name(id='field', ctx=Load()),
                                                                                                                                    attr='get_domain_list',
                                                                                                                                    ctx=Load(),
                                                                                                                                ),
                                                                                                                                args=[Name(id='model', ctx=Load())],
                                                                                                                                keywords=[],
                                                                                                                            ),
                                                                                                                            type_comment=None,
                                                                                                                        ),
                                                                                                                        Assign(
                                                                                                                            targets=[Name(id='inverse_is_int', ctx=Store())],
                                                                                                                            value=Compare(
                                                                                                                                left=Attribute(
                                                                                                                                    value=Subscript(
                                                                                                                                        value=Attribute(
                                                                                                                                            value=Name(id='comodel', ctx=Load()),
                                                                                                                                            attr='_fields',
                                                                                                                                            ctx=Load(),
                                                                                                                                        ),
                                                                                                                                        slice=Attribute(
                                                                                                                                            value=Name(id='field', ctx=Load()),
                                                                                                                                            attr='inverse_name',
                                                                                                                                            ctx=Load(),
                                                                                                                                        ),
                                                                                                                                        ctx=Load(),
                                                                                                                                    ),
                                                                                                                                    attr='type',
                                                                                                                                    ctx=Load(),
                                                                                                                                ),
                                                                                                                                ops=[In()],
                                                                                                                                comparators=[
                                                                                                                                    Tuple(
                                                                                                                                        elts=[
                                                                                                                                            Constant(value='integer', kind=None),
                                                                                                                                            Constant(value='many2one_reference', kind=None),
                                                                                                                                        ],
                                                                                                                                        ctx=Load(),
                                                                                                                                    ),
                                                                                                                                ],
                                                                                                                            ),
                                                                                                                            type_comment=None,
                                                                                                                        ),
                                                                                                                        Assign(
                                                                                                                            targets=[Name(id='unwrap_inverse', ctx=Store())],
                                                                                                                            value=IfExp(
                                                                                                                                test=Name(id='inverse_is_int', ctx=Load()),
                                                                                                                                body=Lambda(
                                                                                                                                    args=arguments(
                                                                                                                                        posonlyargs=[],
                                                                                                                                        args=[arg(arg='ids', annotation=None, type_comment=None)],
                                                                                                                                        vararg=None,
                                                                                                                                        kwonlyargs=[],
                                                                                                                                        kw_defaults=[],
                                                                                                                                        kwarg=None,
                                                                                                                                        defaults=[],
                                                                                                                                    ),
                                                                                                                                    body=Name(id='ids', ctx=Load()),
                                                                                                                                ),
                                                                                                                                orelse=Lambda(
                                                                                                                                    args=arguments(
                                                                                                                                        posonlyargs=[],
                                                                                                                                        args=[arg(arg='recs', annotation=None, type_comment=None)],
                                                                                                                                        vararg=None,
                                                                                                                                        kwonlyargs=[],
                                                                                                                                        kw_defaults=[],
                                                                                                                                        kwarg=None,
                                                                                                                                        defaults=[],
                                                                                                                                    ),
                                                                                                                                    body=Attribute(
                                                                                                                                        value=Name(id='recs', ctx=Load()),
                                                                                                                                        attr='ids',
                                                                                                                                        ctx=Load(),
                                                                                                                                    ),
                                                                                                                                ),
                                                                                                                            ),
                                                                                                                            type_comment=None,
                                                                                                                        ),
                                                                                                                        If(
                                                                                                                            test=Compare(
                                                                                                                                left=Name(id='right', ctx=Load()),
                                                                                                                                ops=[IsNot()],
                                                                                                                                comparators=[Constant(value=False, kind=None)],
                                                                                                                            ),
                                                                                                                            body=[
                                                                                                                                If(
                                                                                                                                    test=Call(
                                                                                                                                        func=Name(id='isinstance', ctx=Load()),
                                                                                                                                        args=[
                                                                                                                                            Name(id='right', ctx=Load()),
                                                                                                                                            Name(id='str', ctx=Load()),
                                                                                                                                        ],
                                                                                                                                        keywords=[],
                                                                                                                                    ),
                                                                                                                                    body=[
                                                                                                                                        Assign(
                                                                                                                                            targets=[Name(id='op2', ctx=Store())],
                                                                                                                                            value=IfExp(
                                                                                                                                                test=Compare(
                                                                                                                                                    left=Name(id='operator', ctx=Load()),
                                                                                                                                                    ops=[In()],
                                                                                                                                                    comparators=[Name(id='NEGATIVE_TERM_OPERATORS', ctx=Load())],
                                                                                                                                                ),
                                                                                                                                                body=Subscript(
                                                                                                                                                    value=Name(id='TERM_OPERATORS_NEGATION', ctx=Load()),
                                                                                                                                                    slice=Name(id='operator', ctx=Load()),
                                                                                                                                                    ctx=Load(),
                                                                                                                                                ),
                                                                                                                                                orelse=Name(id='operator', ctx=Load()),
                                                                                                                                            ),
                                                                                                                                            type_comment=None,
                                                                                                                                        ),
                                                                                                                                        Assign(
                                                                                                                                            targets=[Name(id='ids2', ctx=Store())],
                                                                                                                                            value=Call(
                                                                                                                                                func=Attribute(
                                                                                                                                                    value=Name(id='comodel', ctx=Load()),
                                                                                                                                                    attr='_name_search',
                                                                                                                                                    ctx=Load(),
                                                                                                                                                ),
                                                                                                                                                args=[
                                                                                                                                                    Name(id='right', ctx=Load()),
                                                                                                                                                    BoolOp(
                                                                                                                                                        op=Or(),
                                                                                                                                                        values=[
                                                                                                                                                            Name(id='domain', ctx=Load()),
                                                                                                                                                            List(elts=[], ctx=Load()),
                                                                                                                                                        ],
                                                                                                                                                    ),
                                                                                                                                                    Name(id='op2', ctx=Load()),
                                                                                                                                                ],
                                                                                                                                                keywords=[
                                                                                                                                                    keyword(
                                                                                                                                                        arg='limit',
                                                                                                                                                        value=Constant(value=None, kind=None),
                                                                                                                                                    ),
                                                                                                                                                ],
                                                                                                                                            ),
                                                                                                                                            type_comment=None,
                                                                                                                                        ),
                                                                                                                                    ],
                                                                                                                                    orelse=[
                                                                                                                                        If(
                                                                                                                                            test=Call(
                                                                                                                                                func=Name(id='isinstance', ctx=Load()),
                                                                                                                                                args=[
                                                                                                                                                    Name(id='right', ctx=Load()),
                                                                                                                                                    Attribute(
                                                                                                                                                        value=Attribute(
                                                                                                                                                            value=Name(id='collections', ctx=Load()),
                                                                                                                                                            attr='abc',
                                                                                                                                                            ctx=Load(),
                                                                                                                                                        ),
                                                                                                                                                        attr='Iterable',
                                                                                                                                                        ctx=Load(),
                                                                                                                                                    ),
                                                                                                                                                ],
                                                                                                                                                keywords=[],
                                                                                                                                            ),
                                                                                                                                            body=[
                                                                                                                                                Assign(
                                                                                                                                                    targets=[Name(id='ids2', ctx=Store())],
                                                                                                                                                    value=Name(id='right', ctx=Load()),
                                                                                                                                                    type_comment=None,
                                                                                                                                                ),
                                                                                                                                            ],
                                                                                                                                            orelse=[
                                                                                                                                                Assign(
                                                                                                                                                    targets=[Name(id='ids2', ctx=Store())],
                                                                                                                                                    value=List(
                                                                                                                                                        elts=[Name(id='right', ctx=Load())],
                                                                                                                                                        ctx=Load(),
                                                                                                                                                    ),
                                                                                                                                                    type_comment=None,
                                                                                                                                                ),
                                                                                                                                            ],
                                                                                                                                        ),
                                                                                                                                    ],
                                                                                                                                ),
                                                                                                                                If(
                                                                                                                                    test=BoolOp(
                                                                                                                                        op=And(),
                                                                                                                                        values=[
                                                                                                                                            Name(id='inverse_is_int', ctx=Load()),
                                                                                                                                            Name(id='domain', ctx=Load()),
                                                                                                                                        ],
                                                                                                                                    ),
                                                                                                                                    body=[
                                                                                                                                        Assign(
                                                                                                                                            targets=[Name(id='ids2', ctx=Store())],
                                                                                                                                            value=Call(
                                                                                                                                                func=Attribute(
                                                                                                                                                    value=Name(id='comodel', ctx=Load()),
                                                                                                                                                    attr='_search',
                                                                                                                                                    ctx=Load(),
                                                                                                                                                ),
                                                                                                                                                args=[
                                                                                                                                                    BinOp(
                                                                                                                                                        left=List(
                                                                                                                                                            elts=[
                                                                                                                                                                Tuple(
                                                                                                                                                                    elts=[
                                                                                                                                                                        Constant(value='id', kind=None),
                                                                                                                                                                        Constant(value='in', kind=None),
                                                                                                                                                                        Name(id='ids2', ctx=Load()),
                                                                                                                                                                    ],
                                                                                                                                                                    ctx=Load(),
                                                                                                                                                                ),
                                                                                                                                                            ],
                                                                                                                                                            ctx=Load(),
                                                                                                                                                        ),
                                                                                                                                                        op=Add(),
                                                                                                                                                        right=Name(id='domain', ctx=Load()),
                                                                                                                                                    ),
                                                                                                                                                ],
                                                                                                                                                keywords=[
                                                                                                                                                    keyword(
                                                                                                                                                        arg='order',
                                                                                                                                                        value=Constant(value='id', kind=None),
                                                                                                                                                    ),
                                                                                                                                                ],
                                                                                                                                            ),
                                                                                                                                            type_comment=None,
                                                                                                                                        ),
                                                                                                                                    ],
                                                                                                                                    orelse=[],
                                                                                                                                ),
                                                                                                                                If(
                                                                                                                                    test=BoolOp(
                                                                                                                                        op=And(),
                                                                                                                                        values=[
                                                                                                                                            Call(
                                                                                                                                                func=Name(id='isinstance', ctx=Load()),
                                                                                                                                                args=[
                                                                                                                                                    Name(id='ids2', ctx=Load()),
                                                                                                                                                    Name(id='Query', ctx=Load()),
                                                                                                                                                ],
                                                                                                                                                keywords=[],
                                                                                                                                            ),
                                                                                                                                            Attribute(
                                                                                                                                                value=Subscript(
                                                                                                                                                    value=Attribute(
                                                                                                                                                        value=Name(id='comodel', ctx=Load()),
                                                                                                                                                        attr='_fields',
                                                                                                                                                        ctx=Load(),
                                                                                                                                                    ),
                                                                                                                                                    slice=Attribute(
                                                                                                                                                        value=Name(id='field', ctx=Load()),
                                                                                                                                                        attr='inverse_name',
                                                                                                                                                        ctx=Load(),
                                                                                                                                                    ),
                                                                                                                                                    ctx=Load(),
                                                                                                                                                ),
                                                                                                                                                attr='store',
                                                                                                                                                ctx=Load(),
                                                                                                                                            ),
                                                                                                                                        ],
                                                                                                                                    ),
                                                                                                                                    body=[
                                                                                                                                        Assign(
                                                                                                                                            targets=[Name(id='op1', ctx=Store())],
                                                                                                                                            value=IfExp(
                                                                                                                                                test=Compare(
                                                                                                                                                    left=Name(id='operator', ctx=Load()),
                                                                                                                                                    ops=[In()],
                                                                                                                                                    comparators=[Name(id='NEGATIVE_TERM_OPERATORS', ctx=Load())],
                                                                                                                                                ),
                                                                                                                                                body=Constant(value='not inselect', kind=None),
                                                                                                                                                orelse=Constant(value='inselect', kind=None),
                                                                                                                                            ),
                                                                                                                                            type_comment=None,
                                                                                                                                        ),
                                                                                                                                        Assign(
                                                                                                                                            targets=[
                                                                                                                                                Tuple(
                                                                                                                                                    elts=[
                                                                                                                                                        Name(id='subquery', ctx=Store()),
                                                                                                                                                        Name(id='subparams', ctx=Store()),
                                                                                                                                                    ],
                                                                                                                                                    ctx=Store(),
                                                                                                                                                ),
                                                                                                                                            ],
                                                                                                                                            value=Call(
                                                                                                                                                func=Attribute(
                                                                                                                                                    value=Name(id='ids2', ctx=Load()),
                                                                                                                                                    attr='subselect',
                                                                                                                                                    ctx=Load(),
                                                                                                                                                ),
                                                                                                                                                args=[
                                                                                                                                                    BinOp(
                                                                                                                                                        left=Constant(value='"%s"."%s"', kind=None),
                                                                                                                                                        op=Mod(),
                                                                                                                                                        right=Tuple(
                                                                                                                                                            elts=[
                                                                                                                                                                Attribute(
                                                                                                                                                                    value=Name(id='comodel', ctx=Load()),
                                                                                                                                                                    attr='_table',
                                                                                                                                                                    ctx=Load(),
                                                                                                                                                                ),
                                                                                                                                                                Attribute(
                                                                                                                                                                    value=Name(id='field', ctx=Load()),
                                                                                                                                                                    attr='inverse_name',
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
                                                                                                                                        Expr(
                                                                                                                                            value=Call(
                                                                                                                                                func=Name(id='push', ctx=Load()),
                                                                                                                                                args=[
                                                                                                                                                    Tuple(
                                                                                                                                                        elts=[
                                                                                                                                                            Constant(value='id', kind=None),
                                                                                                                                                            Name(id='op1', ctx=Load()),
                                                                                                                                                            Tuple(
                                                                                                                                                                elts=[
                                                                                                                                                                    Name(id='subquery', ctx=Load()),
                                                                                                                                                                    Name(id='subparams', ctx=Load()),
                                                                                                                                                                ],
                                                                                                                                                                ctx=Load(),
                                                                                                                                                            ),
                                                                                                                                                        ],
                                                                                                                                                        ctx=Load(),
                                                                                                                                                    ),
                                                                                                                                                    Name(id='model', ctx=Load()),
                                                                                                                                                    Name(id='alias', ctx=Load()),
                                                                                                                                                ],
                                                                                                                                                keywords=[
                                                                                                                                                    keyword(
                                                                                                                                                        arg='internal',
                                                                                                                                                        value=Constant(value=True, kind=None),
                                                                                                                                                    ),
                                                                                                                                                ],
                                                                                                                                            ),
                                                                                                                                        ),
                                                                                                                                    ],
                                                                                                                                    orelse=[
                                                                                                                                        If(
                                                                                                                                            test=BoolOp(
                                                                                                                                                op=And(),
                                                                                                                                                values=[
                                                                                                                                                    Name(id='ids2', ctx=Load()),
                                                                                                                                                    Attribute(
                                                                                                                                                        value=Subscript(
                                                                                                                                                            value=Attribute(
                                                                                                                                                                value=Name(id='comodel', ctx=Load()),
                                                                                                                                                                attr='_fields',
                                                                                                                                                                ctx=Load(),
                                                                                                                                                            ),
                                                                                                                                                            slice=Attribute(
                                                                                                                                                                value=Name(id='field', ctx=Load()),
                                                                                                                                                                attr='inverse_name',
                                                                                                                                                                ctx=Load(),
                                                                                                                                                            ),
                                                                                                                                                            ctx=Load(),
                                                                                                                                                        ),
                                                                                                                                                        attr='store',
                                                                                                                                                        ctx=Load(),
                                                                                                                                                    ),
                                                                                                                                                ],
                                                                                                                                            ),
                                                                                                                                            body=[
                                                                                                                                                Assign(
                                                                                                                                                    targets=[Name(id='op1', ctx=Store())],
                                                                                                                                                    value=IfExp(
                                                                                                                                                        test=Compare(
                                                                                                                                                            left=Name(id='operator', ctx=Load()),
                                                                                                                                                            ops=[In()],
                                                                                                                                                            comparators=[Name(id='NEGATIVE_TERM_OPERATORS', ctx=Load())],
                                                                                                                                                        ),
                                                                                                                                                        body=Constant(value='not inselect', kind=None),
                                                                                                                                                        orelse=Constant(value='inselect', kind=None),
                                                                                                                                                    ),
                                                                                                                                                    type_comment=None,
                                                                                                                                                ),
                                                                                                                                                Assign(
                                                                                                                                                    targets=[Name(id='subquery', ctx=Store())],
                                                                                                                                                    value=BinOp(
                                                                                                                                                        left=Constant(value='SELECT "%s" FROM "%s" WHERE "id" IN %%s', kind=None),
                                                                                                                                                        op=Mod(),
                                                                                                                                                        right=Tuple(
                                                                                                                                                            elts=[
                                                                                                                                                                Attribute(
                                                                                                                                                                    value=Name(id='field', ctx=Load()),
                                                                                                                                                                    attr='inverse_name',
                                                                                                                                                                    ctx=Load(),
                                                                                                                                                                ),
                                                                                                                                                                Attribute(
                                                                                                                                                                    value=Name(id='comodel', ctx=Load()),
                                                                                                                                                                    attr='_table',
                                                                                                                                                                    ctx=Load(),
                                                                                                                                                                ),
                                                                                                                                                            ],
                                                                                                                                                            ctx=Load(),
                                                                                                                                                        ),
                                                                                                                                                    ),
                                                                                                                                                    type_comment=None,
                                                                                                                                                ),
                                                                                                                                                Assign(
                                                                                                                                                    targets=[Name(id='subparams', ctx=Store())],
                                                                                                                                                    value=List(
                                                                                                                                                        elts=[
                                                                                                                                                            Call(
                                                                                                                                                                func=Name(id='tuple', ctx=Load()),
                                                                                                                                                                args=[Name(id='ids2', ctx=Load())],
                                                                                                                                                                keywords=[],
                                                                                                                                                            ),
                                                                                                                                                        ],
                                                                                                                                                        ctx=Load(),
                                                                                                                                                    ),
                                                                                                                                                    type_comment=None,
                                                                                                                                                ),
                                                                                                                                                Expr(
                                                                                                                                                    value=Call(
                                                                                                                                                        func=Name(id='push', ctx=Load()),
                                                                                                                                                        args=[
                                                                                                                                                            Tuple(
                                                                                                                                                                elts=[
                                                                                                                                                                    Constant(value='id', kind=None),
                                                                                                                                                                    Name(id='op1', ctx=Load()),
                                                                                                                                                                    Tuple(
                                                                                                                                                                        elts=[
                                                                                                                                                                            Name(id='subquery', ctx=Load()),
                                                                                                                                                                            Name(id='subparams', ctx=Load()),
                                                                                                                                                                        ],
                                                                                                                                                                        ctx=Load(),
                                                                                                                                                                    ),
                                                                                                                                                                ],
                                                                                                                                                                ctx=Load(),
                                                                                                                                                            ),
                                                                                                                                                            Name(id='model', ctx=Load()),
                                                                                                                                                            Name(id='alias', ctx=Load()),
                                                                                                                                                        ],
                                                                                                                                                        keywords=[
                                                                                                                                                            keyword(
                                                                                                                                                                arg='internal',
                                                                                                                                                                value=Constant(value=True, kind=None),
                                                                                                                                                            ),
                                                                                                                                                        ],
                                                                                                                                                    ),
                                                                                                                                                ),
                                                                                                                                            ],
                                                                                                                                            orelse=[
                                                                                                                                                Assign(
                                                                                                                                                    targets=[Name(id='recs', ctx=Store())],
                                                                                                                                                    value=Call(
                                                                                                                                                        func=Attribute(
                                                                                                                                                            value=Call(
                                                                                                                                                                func=Attribute(
                                                                                                                                                                    value=Call(
                                                                                                                                                                        func=Attribute(
                                                                                                                                                                            value=Name(id='comodel', ctx=Load()),
                                                                                                                                                                            attr='browse',
                                                                                                                                                                            ctx=Load(),
                                                                                                                                                                        ),
                                                                                                                                                                        args=[Name(id='ids2', ctx=Load())],
                                                                                                                                                                        keywords=[],
                                                                                                                                                                    ),
                                                                                                                                                                    attr='sudo',
                                                                                                                                                                    ctx=Load(),
                                                                                                                                                                ),
                                                                                                                                                                args=[],
                                                                                                                                                                keywords=[],
                                                                                                                                                            ),
                                                                                                                                                            attr='with_context',
                                                                                                                                                            ctx=Load(),
                                                                                                                                                        ),
                                                                                                                                                        args=[],
                                                                                                                                                        keywords=[
                                                                                                                                                            keyword(
                                                                                                                                                                arg='prefetch_fields',
                                                                                                                                                                value=Constant(value=False, kind=None),
                                                                                                                                                            ),
                                                                                                                                                        ],
                                                                                                                                                    ),
                                                                                                                                                    type_comment=None,
                                                                                                                                                ),
                                                                                                                                                Assign(
                                                                                                                                                    targets=[Name(id='ids1', ctx=Store())],
                                                                                                                                                    value=Call(
                                                                                                                                                        func=Name(id='unwrap_inverse', ctx=Load()),
                                                                                                                                                        args=[
                                                                                                                                                            Call(
                                                                                                                                                                func=Attribute(
                                                                                                                                                                    value=Name(id='recs', ctx=Load()),
                                                                                                                                                                    attr='mapped',
                                                                                                                                                                    ctx=Load(),
                                                                                                                                                                ),
                                                                                                                                                                args=[
                                                                                                                                                                    Attribute(
                                                                                                                                                                        value=Name(id='field', ctx=Load()),
                                                                                                                                                                        attr='inverse_name',
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
                                                                                                                                                    targets=[Name(id='op1', ctx=Store())],
                                                                                                                                                    value=IfExp(
                                                                                                                                                        test=Compare(
                                                                                                                                                            left=Name(id='operator', ctx=Load()),
                                                                                                                                                            ops=[In()],
                                                                                                                                                            comparators=[Name(id='NEGATIVE_TERM_OPERATORS', ctx=Load())],
                                                                                                                                                        ),
                                                                                                                                                        body=Constant(value='not in', kind=None),
                                                                                                                                                        orelse=Constant(value='in', kind=None),
                                                                                                                                                    ),
                                                                                                                                                    type_comment=None,
                                                                                                                                                ),
                                                                                                                                                Expr(
                                                                                                                                                    value=Call(
                                                                                                                                                        func=Name(id='push', ctx=Load()),
                                                                                                                                                        args=[
                                                                                                                                                            Tuple(
                                                                                                                                                                elts=[
                                                                                                                                                                    Constant(value='id', kind=None),
                                                                                                                                                                    Name(id='op1', ctx=Load()),
                                                                                                                                                                    Name(id='ids1', ctx=Load()),
                                                                                                                                                                ],
                                                                                                                                                                ctx=Load(),
                                                                                                                                                            ),
                                                                                                                                                            Name(id='model', ctx=Load()),
                                                                                                                                                            Name(id='alias', ctx=Load()),
                                                                                                                                                        ],
                                                                                                                                                        keywords=[],
                                                                                                                                                    ),
                                                                                                                                                ),
                                                                                                                                            ],
                                                                                                                                        ),
                                                                                                                                    ],
                                                                                                                                ),
                                                                                                                            ],
                                                                                                                            orelse=[
                                                                                                                                If(
                                                                                                                                    test=BoolOp(
                                                                                                                                        op=And(),
                                                                                                                                        values=[
                                                                                                                                            Attribute(
                                                                                                                                                value=Subscript(
                                                                                                                                                    value=Attribute(
                                                                                                                                                        value=Name(id='comodel', ctx=Load()),
                                                                                                                                                        attr='_fields',
                                                                                                                                                        ctx=Load(),
                                                                                                                                                    ),
                                                                                                                                                    slice=Attribute(
                                                                                                                                                        value=Name(id='field', ctx=Load()),
                                                                                                                                                        attr='inverse_name',
                                                                                                                                                        ctx=Load(),
                                                                                                                                                    ),
                                                                                                                                                    ctx=Load(),
                                                                                                                                                ),
                                                                                                                                                attr='store',
                                                                                                                                                ctx=Load(),
                                                                                                                                            ),
                                                                                                                                            UnaryOp(
                                                                                                                                                op=Not(),
                                                                                                                                                operand=BoolOp(
                                                                                                                                                    op=And(),
                                                                                                                                                    values=[
                                                                                                                                                        Name(id='inverse_is_int', ctx=Load()),
                                                                                                                                                        Name(id='domain', ctx=Load()),
                                                                                                                                                    ],
                                                                                                                                                ),
                                                                                                                                            ),
                                                                                                                                        ],
                                                                                                                                    ),
                                                                                                                                    body=[
                                                                                                                                        Assign(
                                                                                                                                            targets=[Name(id='op1', ctx=Store())],
                                                                                                                                            value=IfExp(
                                                                                                                                                test=Compare(
                                                                                                                                                    left=Name(id='operator', ctx=Load()),
                                                                                                                                                    ops=[In()],
                                                                                                                                                    comparators=[Name(id='NEGATIVE_TERM_OPERATORS', ctx=Load())],
                                                                                                                                                ),
                                                                                                                                                body=Constant(value='inselect', kind=None),
                                                                                                                                                orelse=Constant(value='not inselect', kind=None),
                                                                                                                                            ),
                                                                                                                                            type_comment=None,
                                                                                                                                        ),
                                                                                                                                        Assign(
                                                                                                                                            targets=[Name(id='subquery', ctx=Store())],
                                                                                                                                            value=BinOp(
                                                                                                                                                left=Constant(value='SELECT "%s" FROM "%s" where "%s" is not null', kind=None),
                                                                                                                                                op=Mod(),
                                                                                                                                                right=Tuple(
                                                                                                                                                    elts=[
                                                                                                                                                        Attribute(
                                                                                                                                                            value=Name(id='field', ctx=Load()),
                                                                                                                                                            attr='inverse_name',
                                                                                                                                                            ctx=Load(),
                                                                                                                                                        ),
                                                                                                                                                        Attribute(
                                                                                                                                                            value=Name(id='comodel', ctx=Load()),
                                                                                                                                                            attr='_table',
                                                                                                                                                            ctx=Load(),
                                                                                                                                                        ),
                                                                                                                                                        Attribute(
                                                                                                                                                            value=Name(id='field', ctx=Load()),
                                                                                                                                                            attr='inverse_name',
                                                                                                                                                            ctx=Load(),
                                                                                                                                                        ),
                                                                                                                                                    ],
                                                                                                                                                    ctx=Load(),
                                                                                                                                                ),
                                                                                                                                            ),
                                                                                                                                            type_comment=None,
                                                                                                                                        ),
                                                                                                                                        Expr(
                                                                                                                                            value=Call(
                                                                                                                                                func=Name(id='push', ctx=Load()),
                                                                                                                                                args=[
                                                                                                                                                    Tuple(
                                                                                                                                                        elts=[
                                                                                                                                                            Constant(value='id', kind=None),
                                                                                                                                                            Name(id='op1', ctx=Load()),
                                                                                                                                                            Tuple(
                                                                                                                                                                elts=[
                                                                                                                                                                    Name(id='subquery', ctx=Load()),
                                                                                                                                                                    List(elts=[], ctx=Load()),
                                                                                                                                                                ],
                                                                                                                                                                ctx=Load(),
                                                                                                                                                            ),
                                                                                                                                                        ],
                                                                                                                                                        ctx=Load(),
                                                                                                                                                    ),
                                                                                                                                                    Name(id='model', ctx=Load()),
                                                                                                                                                    Name(id='alias', ctx=Load()),
                                                                                                                                                ],
                                                                                                                                                keywords=[
                                                                                                                                                    keyword(
                                                                                                                                                        arg='internal',
                                                                                                                                                        value=Constant(value=True, kind=None),
                                                                                                                                                    ),
                                                                                                                                                ],
                                                                                                                                            ),
                                                                                                                                        ),
                                                                                                                                    ],
                                                                                                                                    orelse=[
                                                                                                                                        Assign(
                                                                                                                                            targets=[Name(id='comodel_domain', ctx=Store())],
                                                                                                                                            value=List(
                                                                                                                                                elts=[
                                                                                                                                                    Tuple(
                                                                                                                                                        elts=[
                                                                                                                                                            Attribute(
                                                                                                                                                                value=Name(id='field', ctx=Load()),
                                                                                                                                                                attr='inverse_name',
                                                                                                                                                                ctx=Load(),
                                                                                                                                                            ),
                                                                                                                                                            Constant(value='!=', kind=None),
                                                                                                                                                            Constant(value=False, kind=None),
                                                                                                                                                        ],
                                                                                                                                                        ctx=Load(),
                                                                                                                                                    ),
                                                                                                                                                ],
                                                                                                                                                ctx=Load(),
                                                                                                                                            ),
                                                                                                                                            type_comment=None,
                                                                                                                                        ),
                                                                                                                                        If(
                                                                                                                                            test=BoolOp(
                                                                                                                                                op=And(),
                                                                                                                                                values=[
                                                                                                                                                    Name(id='inverse_is_int', ctx=Load()),
                                                                                                                                                    Name(id='domain', ctx=Load()),
                                                                                                                                                ],
                                                                                                                                            ),
                                                                                                                                            body=[
                                                                                                                                                AugAssign(
                                                                                                                                                    target=Name(id='comodel_domain', ctx=Store()),
                                                                                                                                                    op=Add(),
                                                                                                                                                    value=Name(id='domain', ctx=Load()),
                                                                                                                                                ),
                                                                                                                                            ],
                                                                                                                                            orelse=[],
                                                                                                                                        ),
                                                                                                                                        Assign(
                                                                                                                                            targets=[Name(id='recs', ctx=Store())],
                                                                                                                                            value=Call(
                                                                                                                                                func=Attribute(
                                                                                                                                                    value=Call(
                                                                                                                                                        func=Attribute(
                                                                                                                                                            value=Call(
                                                                                                                                                                func=Attribute(
                                                                                                                                                                    value=Name(id='comodel', ctx=Load()),
                                                                                                                                                                    attr='search',
                                                                                                                                                                    ctx=Load(),
                                                                                                                                                                ),
                                                                                                                                                                args=[Name(id='comodel_domain', ctx=Load())],
                                                                                                                                                                keywords=[
                                                                                                                                                                    keyword(
                                                                                                                                                                        arg='order',
                                                                                                                                                                        value=Constant(value='id', kind=None),
                                                                                                                                                                    ),
                                                                                                                                                                ],
                                                                                                                                                            ),
                                                                                                                                                            attr='sudo',
                                                                                                                                                            ctx=Load(),
                                                                                                                                                        ),
                                                                                                                                                        args=[],
                                                                                                                                                        keywords=[],
                                                                                                                                                    ),
                                                                                                                                                    attr='with_context',
                                                                                                                                                    ctx=Load(),
                                                                                                                                                ),
                                                                                                                                                args=[],
                                                                                                                                                keywords=[
                                                                                                                                                    keyword(
                                                                                                                                                        arg='prefetch_fields',
                                                                                                                                                        value=Constant(value=False, kind=None),
                                                                                                                                                    ),
                                                                                                                                                ],
                                                                                                                                            ),
                                                                                                                                            type_comment=None,
                                                                                                                                        ),
                                                                                                                                        Assign(
                                                                                                                                            targets=[Name(id='ids1', ctx=Store())],
                                                                                                                                            value=Call(
                                                                                                                                                func=Name(id='unwrap_inverse', ctx=Load()),
                                                                                                                                                args=[
                                                                                                                                                    Call(
                                                                                                                                                        func=Attribute(
                                                                                                                                                            value=Name(id='recs', ctx=Load()),
                                                                                                                                                            attr='mapped',
                                                                                                                                                            ctx=Load(),
                                                                                                                                                        ),
                                                                                                                                                        args=[
                                                                                                                                                            Attribute(
                                                                                                                                                                value=Name(id='field', ctx=Load()),
                                                                                                                                                                attr='inverse_name',
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
                                                                                                                                            targets=[Name(id='op1', ctx=Store())],
                                                                                                                                            value=IfExp(
                                                                                                                                                test=Compare(
                                                                                                                                                    left=Name(id='operator', ctx=Load()),
                                                                                                                                                    ops=[In()],
                                                                                                                                                    comparators=[Name(id='NEGATIVE_TERM_OPERATORS', ctx=Load())],
                                                                                                                                                ),
                                                                                                                                                body=Constant(value='in', kind=None),
                                                                                                                                                orelse=Constant(value='not in', kind=None),
                                                                                                                                            ),
                                                                                                                                            type_comment=None,
                                                                                                                                        ),
                                                                                                                                        Expr(
                                                                                                                                            value=Call(
                                                                                                                                                func=Name(id='push', ctx=Load()),
                                                                                                                                                args=[
                                                                                                                                                    Tuple(
                                                                                                                                                        elts=[
                                                                                                                                                            Constant(value='id', kind=None),
                                                                                                                                                            Name(id='op1', ctx=Load()),
                                                                                                                                                            Name(id='ids1', ctx=Load()),
                                                                                                                                                        ],
                                                                                                                                                        ctx=Load(),
                                                                                                                                                    ),
                                                                                                                                                    Name(id='model', ctx=Load()),
                                                                                                                                                    Name(id='alias', ctx=Load()),
                                                                                                                                                ],
                                                                                                                                                keywords=[],
                                                                                                                                            ),
                                                                                                                                        ),
                                                                                                                                    ],
                                                                                                                                ),
                                                                                                                            ],
                                                                                                                        ),
                                                                                                                    ],
                                                                                                                    orelse=[
                                                                                                                        If(
                                                                                                                            test=Compare(
                                                                                                                                left=Attribute(
                                                                                                                                    value=Name(id='field', ctx=Load()),
                                                                                                                                    attr='type',
                                                                                                                                    ctx=Load(),
                                                                                                                                ),
                                                                                                                                ops=[Eq()],
                                                                                                                                comparators=[Constant(value='many2many', kind=None)],
                                                                                                                            ),
                                                                                                                            body=[
                                                                                                                                Assign(
                                                                                                                                    targets=[
                                                                                                                                        Tuple(
                                                                                                                                            elts=[
                                                                                                                                                Name(id='rel_table', ctx=Store()),
                                                                                                                                                Name(id='rel_id1', ctx=Store()),
                                                                                                                                                Name(id='rel_id2', ctx=Store()),
                                                                                                                                            ],
                                                                                                                                            ctx=Store(),
                                                                                                                                        ),
                                                                                                                                    ],
                                                                                                                                    value=Tuple(
                                                                                                                                        elts=[
                                                                                                                                            Attribute(
                                                                                                                                                value=Name(id='field', ctx=Load()),
                                                                                                                                                attr='relation',
                                                                                                                                                ctx=Load(),
                                                                                                                                            ),
                                                                                                                                            Attribute(
                                                                                                                                                value=Name(id='field', ctx=Load()),
                                                                                                                                                attr='column1',
                                                                                                                                                ctx=Load(),
                                                                                                                                            ),
                                                                                                                                            Attribute(
                                                                                                                                                value=Name(id='field', ctx=Load()),
                                                                                                                                                attr='column2',
                                                                                                                                                ctx=Load(),
                                                                                                                                            ),
                                                                                                                                        ],
                                                                                                                                        ctx=Load(),
                                                                                                                                    ),
                                                                                                                                    type_comment=None,
                                                                                                                                ),
                                                                                                                                If(
                                                                                                                                    test=Compare(
                                                                                                                                        left=Name(id='operator', ctx=Load()),
                                                                                                                                        ops=[In()],
                                                                                                                                        comparators=[Name(id='HIERARCHY_FUNCS', ctx=Load())],
                                                                                                                                    ),
                                                                                                                                    body=[
                                                                                                                                        Assign(
                                                                                                                                            targets=[Name(id='ids2', ctx=Store())],
                                                                                                                                            value=Call(
                                                                                                                                                func=Name(id='to_ids', ctx=Load()),
                                                                                                                                                args=[
                                                                                                                                                    Name(id='right', ctx=Load()),
                                                                                                                                                    Name(id='comodel', ctx=Load()),
                                                                                                                                                    Name(id='leaf', ctx=Load()),
                                                                                                                                                ],
                                                                                                                                                keywords=[],
                                                                                                                                            ),
                                                                                                                                            type_comment=None,
                                                                                                                                        ),
                                                                                                                                        Assign(
                                                                                                                                            targets=[Name(id='domain', ctx=Store())],
                                                                                                                                            value=Call(
                                                                                                                                                func=Subscript(
                                                                                                                                                    value=Name(id='HIERARCHY_FUNCS', ctx=Load()),
                                                                                                                                                    slice=Name(id='operator', ctx=Load()),
                                                                                                                                                    ctx=Load(),
                                                                                                                                                ),
                                                                                                                                                args=[
                                                                                                                                                    Constant(value='id', kind=None),
                                                                                                                                                    Name(id='ids2', ctx=Load()),
                                                                                                                                                    Name(id='comodel', ctx=Load()),
                                                                                                                                                ],
                                                                                                                                                keywords=[],
                                                                                                                                            ),
                                                                                                                                            type_comment=None,
                                                                                                                                        ),
                                                                                                                                        Assign(
                                                                                                                                            targets=[Name(id='ids2', ctx=Store())],
                                                                                                                                            value=Call(
                                                                                                                                                func=Attribute(
                                                                                                                                                    value=Name(id='comodel', ctx=Load()),
                                                                                                                                                    attr='_search',
                                                                                                                                                    ctx=Load(),
                                                                                                                                                ),
                                                                                                                                                args=[Name(id='domain', ctx=Load())],
                                                                                                                                                keywords=[
                                                                                                                                                    keyword(
                                                                                                                                                        arg='order',
                                                                                                                                                        value=Constant(value='id', kind=None),
                                                                                                                                                    ),
                                                                                                                                                ],
                                                                                                                                            ),
                                                                                                                                            type_comment=None,
                                                                                                                                        ),
                                                                                                                                        If(
                                                                                                                                            test=Compare(
                                                                                                                                                left=Name(id='comodel', ctx=Load()),
                                                                                                                                                ops=[Eq()],
                                                                                                                                                comparators=[Name(id='model', ctx=Load())],
                                                                                                                                            ),
                                                                                                                                            body=[
                                                                                                                                                Expr(
                                                                                                                                                    value=Call(
                                                                                                                                                        func=Name(id='push', ctx=Load()),
                                                                                                                                                        args=[
                                                                                                                                                            Tuple(
                                                                                                                                                                elts=[
                                                                                                                                                                    Constant(value='id', kind=None),
                                                                                                                                                                    Constant(value='in', kind=None),
                                                                                                                                                                    Name(id='ids2', ctx=Load()),
                                                                                                                                                                ],
                                                                                                                                                                ctx=Load(),
                                                                                                                                                            ),
                                                                                                                                                            Name(id='model', ctx=Load()),
                                                                                                                                                            Name(id='alias', ctx=Load()),
                                                                                                                                                        ],
                                                                                                                                                        keywords=[],
                                                                                                                                                    ),
                                                                                                                                                ),
                                                                                                                                            ],
                                                                                                                                            orelse=[
                                                                                                                                                Assign(
                                                                                                                                                    targets=[Name(id='subquery', ctx=Store())],
                                                                                                                                                    value=BinOp(
                                                                                                                                                        left=Constant(value='SELECT "%s" FROM "%s" WHERE "%s" IN %%s', kind=None),
                                                                                                                                                        op=Mod(),
                                                                                                                                                        right=Tuple(
                                                                                                                                                            elts=[
                                                                                                                                                                Name(id='rel_id1', ctx=Load()),
                                                                                                                                                                Name(id='rel_table', ctx=Load()),
                                                                                                                                                                Name(id='rel_id2', ctx=Load()),
                                                                                                                                                            ],
                                                                                                                                                            ctx=Load(),
                                                                                                                                                        ),
                                                                                                                                                    ),
                                                                                                                                                    type_comment=None,
                                                                                                                                                ),
                                                                                                                                                Expr(
                                                                                                                                                    value=Call(
                                                                                                                                                        func=Name(id='push', ctx=Load()),
                                                                                                                                                        args=[
                                                                                                                                                            Tuple(
                                                                                                                                                                elts=[
                                                                                                                                                                    Constant(value='id', kind=None),
                                                                                                                                                                    Constant(value='inselect', kind=None),
                                                                                                                                                                    Tuple(
                                                                                                                                                                        elts=[
                                                                                                                                                                            Name(id='subquery', ctx=Load()),
                                                                                                                                                                            List(
                                                                                                                                                                                elts=[
                                                                                                                                                                                    BoolOp(
                                                                                                                                                                                        op=Or(),
                                                                                                                                                                                        values=[
                                                                                                                                                                                            Call(
                                                                                                                                                                                                func=Name(id='tuple', ctx=Load()),
                                                                                                                                                                                                args=[Name(id='ids2', ctx=Load())],
                                                                                                                                                                                                keywords=[],
                                                                                                                                                                                            ),
                                                                                                                                                                                            Tuple(
                                                                                                                                                                                                elts=[Constant(value=None, kind=None)],
                                                                                                                                                                                                ctx=Load(),
                                                                                                                                                                                            ),
                                                                                                                                                                                        ],
                                                                                                                                                                                    ),
                                                                                                                                                                                ],
                                                                                                                                                                                ctx=Load(),
                                                                                                                                                                            ),
                                                                                                                                                                        ],
                                                                                                                                                                        ctx=Load(),
                                                                                                                                                                    ),
                                                                                                                                                                ],
                                                                                                                                                                ctx=Load(),
                                                                                                                                                            ),
                                                                                                                                                            Name(id='model', ctx=Load()),
                                                                                                                                                            Name(id='alias', ctx=Load()),
                                                                                                                                                        ],
                                                                                                                                                        keywords=[
                                                                                                                                                            keyword(
                                                                                                                                                                arg='internal',
                                                                                                                                                                value=Constant(value=True, kind=None),
                                                                                                                                                            ),
                                                                                                                                                        ],
                                                                                                                                                    ),
                                                                                                                                                ),
                                                                                                                                            ],
                                                                                                                                        ),
                                                                                                                                    ],
                                                                                                                                    orelse=[
                                                                                                                                        If(
                                                                                                                                            test=Compare(
                                                                                                                                                left=Name(id='right', ctx=Load()),
                                                                                                                                                ops=[IsNot()],
                                                                                                                                                comparators=[Constant(value=False, kind=None)],
                                                                                                                                            ),
                                                                                                                                            body=[
                                                                                                                                                If(
                                                                                                                                                    test=Call(
                                                                                                                                                        func=Name(id='isinstance', ctx=Load()),
                                                                                                                                                        args=[
                                                                                                                                                            Name(id='right', ctx=Load()),
                                                                                                                                                            Name(id='str', ctx=Load()),
                                                                                                                                                        ],
                                                                                                                                                        keywords=[],
                                                                                                                                                    ),
                                                                                                                                                    body=[
                                                                                                                                                        Assign(
                                                                                                                                                            targets=[Name(id='domain', ctx=Store())],
                                                                                                                                                            value=Call(
                                                                                                                                                                func=Attribute(
                                                                                                                                                                    value=Name(id='field', ctx=Load()),
                                                                                                                                                                    attr='get_domain_list',
                                                                                                                                                                    ctx=Load(),
                                                                                                                                                                ),
                                                                                                                                                                args=[Name(id='model', ctx=Load())],
                                                                                                                                                                keywords=[],
                                                                                                                                                            ),
                                                                                                                                                            type_comment=None,
                                                                                                                                                        ),
                                                                                                                                                        Assign(
                                                                                                                                                            targets=[Name(id='op2', ctx=Store())],
                                                                                                                                                            value=IfExp(
                                                                                                                                                                test=Compare(
                                                                                                                                                                    left=Name(id='operator', ctx=Load()),
                                                                                                                                                                    ops=[In()],
                                                                                                                                                                    comparators=[Name(id='NEGATIVE_TERM_OPERATORS', ctx=Load())],
                                                                                                                                                                ),
                                                                                                                                                                body=Subscript(
                                                                                                                                                                    value=Name(id='TERM_OPERATORS_NEGATION', ctx=Load()),
                                                                                                                                                                    slice=Name(id='operator', ctx=Load()),
                                                                                                                                                                    ctx=Load(),
                                                                                                                                                                ),
                                                                                                                                                                orelse=Name(id='operator', ctx=Load()),
                                                                                                                                                            ),
                                                                                                                                                            type_comment=None,
                                                                                                                                                        ),
                                                                                                                                                        Assign(
                                                                                                                                                            targets=[Name(id='ids2', ctx=Store())],
                                                                                                                                                            value=Call(
                                                                                                                                                                func=Attribute(
                                                                                                                                                                    value=Name(id='comodel', ctx=Load()),
                                                                                                                                                                    attr='_name_search',
                                                                                                                                                                    ctx=Load(),
                                                                                                                                                                ),
                                                                                                                                                                args=[
                                                                                                                                                                    Name(id='right', ctx=Load()),
                                                                                                                                                                    BoolOp(
                                                                                                                                                                        op=Or(),
                                                                                                                                                                        values=[
                                                                                                                                                                            Name(id='domain', ctx=Load()),
                                                                                                                                                                            List(elts=[], ctx=Load()),
                                                                                                                                                                        ],
                                                                                                                                                                    ),
                                                                                                                                                                    Name(id='op2', ctx=Load()),
                                                                                                                                                                ],
                                                                                                                                                                keywords=[
                                                                                                                                                                    keyword(
                                                                                                                                                                        arg='limit',
                                                                                                                                                                        value=Constant(value=None, kind=None),
                                                                                                                                                                    ),
                                                                                                                                                                ],
                                                                                                                                                            ),
                                                                                                                                                            type_comment=None,
                                                                                                                                                        ),
                                                                                                                                                    ],
                                                                                                                                                    orelse=[
                                                                                                                                                        If(
                                                                                                                                                            test=Call(
                                                                                                                                                                func=Name(id='isinstance', ctx=Load()),
                                                                                                                                                                args=[
                                                                                                                                                                    Name(id='right', ctx=Load()),
                                                                                                                                                                    Attribute(
                                                                                                                                                                        value=Attribute(
                                                                                                                                                                            value=Name(id='collections', ctx=Load()),
                                                                                                                                                                            attr='abc',
                                                                                                                                                                            ctx=Load(),
                                                                                                                                                                        ),
                                                                                                                                                                        attr='Iterable',
                                                                                                                                                                        ctx=Load(),
                                                                                                                                                                    ),
                                                                                                                                                                ],
                                                                                                                                                                keywords=[],
                                                                                                                                                            ),
                                                                                                                                                            body=[
                                                                                                                                                                Assign(
                                                                                                                                                                    targets=[Name(id='ids2', ctx=Store())],
                                                                                                                                                                    value=Name(id='right', ctx=Load()),
                                                                                                                                                                    type_comment=None,
                                                                                                                                                                ),
                                                                                                                                                            ],
                                                                                                                                                            orelse=[
                                                                                                                                                                Assign(
                                                                                                                                                                    targets=[Name(id='ids2', ctx=Store())],
                                                                                                                                                                    value=List(
                                                                                                                                                                        elts=[Name(id='right', ctx=Load())],
                                                                                                                                                                        ctx=Load(),
                                                                                                                                                                    ),
                                                                                                                                                                    type_comment=None,
                                                                                                                                                                ),
                                                                                                                                                            ],
                                                                                                                                                        ),
                                                                                                                                                    ],
                                                                                                                                                ),
                                                                                                                                                If(
                                                                                                                                                    test=Call(
                                                                                                                                                        func=Name(id='isinstance', ctx=Load()),
                                                                                                                                                        args=[
                                                                                                                                                            Name(id='ids2', ctx=Load()),
                                                                                                                                                            Name(id='Query', ctx=Load()),
                                                                                                                                                        ],
                                                                                                                                                        keywords=[],
                                                                                                                                                    ),
                                                                                                                                                    body=[
                                                                                                                                                        Assign(
                                                                                                                                                            targets=[Name(id='subop', ctx=Store())],
                                                                                                                                                            value=IfExp(
                                                                                                                                                                test=Compare(
                                                                                                                                                                    left=Name(id='operator', ctx=Load()),
                                                                                                                                                                    ops=[In()],
                                                                                                                                                                    comparators=[Name(id='NEGATIVE_TERM_OPERATORS', ctx=Load())],
                                                                                                                                                                ),
                                                                                                                                                                body=Constant(value='not inselect', kind=None),
                                                                                                                                                                orelse=Constant(value='inselect', kind=None),
                                                                                                                                                            ),
                                                                                                                                                            type_comment=None,
                                                                                                                                                        ),
                                                                                                                                                        Assign(
                                                                                                                                                            targets=[
                                                                                                                                                                Tuple(
                                                                                                                                                                    elts=[
                                                                                                                                                                        Name(id='subquery', ctx=Store()),
                                                                                                                                                                        Name(id='subparams', ctx=Store()),
                                                                                                                                                                    ],
                                                                                                                                                                    ctx=Store(),
                                                                                                                                                                ),
                                                                                                                                                            ],
                                                                                                                                                            value=Call(
                                                                                                                                                                func=Attribute(
                                                                                                                                                                    value=Name(id='ids2', ctx=Load()),
                                                                                                                                                                    attr='subselect',
                                                                                                                                                                    ctx=Load(),
                                                                                                                                                                ),
                                                                                                                                                                args=[],
                                                                                                                                                                keywords=[],
                                                                                                                                                            ),
                                                                                                                                                            type_comment=None,
                                                                                                                                                        ),
                                                                                                                                                        Assign(
                                                                                                                                                            targets=[Name(id='query', ctx=Store())],
                                                                                                                                                            value=BinOp(
                                                                                                                                                                left=Constant(value='SELECT "%s" FROM "%s" WHERE "%s" IN (%s)', kind=None),
                                                                                                                                                                op=Mod(),
                                                                                                                                                                right=Tuple(
                                                                                                                                                                    elts=[
                                                                                                                                                                        Name(id='rel_id1', ctx=Load()),
                                                                                                                                                                        Name(id='rel_table', ctx=Load()),
                                                                                                                                                                        Name(id='rel_id2', ctx=Load()),
                                                                                                                                                                        Name(id='subquery', ctx=Load()),
                                                                                                                                                                    ],
                                                                                                                                                                    ctx=Load(),
                                                                                                                                                                ),
                                                                                                                                                            ),
                                                                                                                                                            type_comment=None,
                                                                                                                                                        ),
                                                                                                                                                        Expr(
                                                                                                                                                            value=Call(
                                                                                                                                                                func=Name(id='push', ctx=Load()),
                                                                                                                                                                args=[
                                                                                                                                                                    Tuple(
                                                                                                                                                                        elts=[
                                                                                                                                                                            Constant(value='id', kind=None),
                                                                                                                                                                            Name(id='subop', ctx=Load()),
                                                                                                                                                                            Tuple(
                                                                                                                                                                                elts=[
                                                                                                                                                                                    Name(id='query', ctx=Load()),
                                                                                                                                                                                    Name(id='subparams', ctx=Load()),
                                                                                                                                                                                ],
                                                                                                                                                                                ctx=Load(),
                                                                                                                                                                            ),
                                                                                                                                                                        ],
                                                                                                                                                                        ctx=Load(),
                                                                                                                                                                    ),
                                                                                                                                                                    Name(id='model', ctx=Load()),
                                                                                                                                                                    Name(id='alias', ctx=Load()),
                                                                                                                                                                ],
                                                                                                                                                                keywords=[
                                                                                                                                                                    keyword(
                                                                                                                                                                        arg='internal',
                                                                                                                                                                        value=Constant(value=True, kind=None),
                                                                                                                                                                    ),
                                                                                                                                                                ],
                                                                                                                                                            ),
                                                                                                                                                        ),
                                                                                                                                                    ],
                                                                                                                                                    orelse=[
                                                                                                                                                        Assign(
                                                                                                                                                            targets=[Name(id='subop', ctx=Store())],
                                                                                                                                                            value=IfExp(
                                                                                                                                                                test=Compare(
                                                                                                                                                                    left=Name(id='operator', ctx=Load()),
                                                                                                                                                                    ops=[In()],
                                                                                                                                                                    comparators=[Name(id='NEGATIVE_TERM_OPERATORS', ctx=Load())],
                                                                                                                                                                ),
                                                                                                                                                                body=Constant(value='not inselect', kind=None),
                                                                                                                                                                orelse=Constant(value='inselect', kind=None),
                                                                                                                                                            ),
                                                                                                                                                            type_comment=None,
                                                                                                                                                        ),
                                                                                                                                                        Assign(
                                                                                                                                                            targets=[Name(id='subquery', ctx=Store())],
                                                                                                                                                            value=BinOp(
                                                                                                                                                                left=Constant(value='SELECT "%s" FROM "%s" WHERE "%s" IN %%s', kind=None),
                                                                                                                                                                op=Mod(),
                                                                                                                                                                right=Tuple(
                                                                                                                                                                    elts=[
                                                                                                                                                                        Name(id='rel_id1', ctx=Load()),
                                                                                                                                                                        Name(id='rel_table', ctx=Load()),
                                                                                                                                                                        Name(id='rel_id2', ctx=Load()),
                                                                                                                                                                    ],
                                                                                                                                                                    ctx=Load(),
                                                                                                                                                                ),
                                                                                                                                                            ),
                                                                                                                                                            type_comment=None,
                                                                                                                                                        ),
                                                                                                                                                        Assign(
                                                                                                                                                            targets=[Name(id='ids2', ctx=Store())],
                                                                                                                                                            value=BoolOp(
                                                                                                                                                                op=Or(),
                                                                                                                                                                values=[
                                                                                                                                                                    Call(
                                                                                                                                                                        func=Name(id='tuple', ctx=Load()),
                                                                                                                                                                        args=[
                                                                                                                                                                            GeneratorExp(
                                                                                                                                                                                elt=Name(id='it', ctx=Load()),
                                                                                                                                                                                generators=[
                                                                                                                                                                                    comprehension(
                                                                                                                                                                                        target=Name(id='it', ctx=Store()),
                                                                                                                                                                                        iter=Name(id='ids2', ctx=Load()),
                                                                                                                                                                                        ifs=[Name(id='it', ctx=Load())],
                                                                                                                                                                                        is_async=0,
                                                                                                                                                                                    ),
                                                                                                                                                                                ],
                                                                                                                                                                            ),
                                                                                                                                                                        ],
                                                                                                                                                                        keywords=[],
                                                                                                                                                                    ),
                                                                                                                                                                    Tuple(
                                                                                                                                                                        elts=[Constant(value=None, kind=None)],
                                                                                                                                                                        ctx=Load(),
                                                                                                                                                                    ),
                                                                                                                                                                ],
                                                                                                                                                            ),
                                                                                                                                                            type_comment=None,
                                                                                                                                                        ),
                                                                                                                                                        Expr(
                                                                                                                                                            value=Call(
                                                                                                                                                                func=Name(id='push', ctx=Load()),
                                                                                                                                                                args=[
                                                                                                                                                                    Tuple(
                                                                                                                                                                        elts=[
                                                                                                                                                                            Constant(value='id', kind=None),
                                                                                                                                                                            Name(id='subop', ctx=Load()),
                                                                                                                                                                            Tuple(
                                                                                                                                                                                elts=[
                                                                                                                                                                                    Name(id='subquery', ctx=Load()),
                                                                                                                                                                                    List(
                                                                                                                                                                                        elts=[Name(id='ids2', ctx=Load())],
                                                                                                                                                                                        ctx=Load(),
                                                                                                                                                                                    ),
                                                                                                                                                                                ],
                                                                                                                                                                                ctx=Load(),
                                                                                                                                                                            ),
                                                                                                                                                                        ],
                                                                                                                                                                        ctx=Load(),
                                                                                                                                                                    ),
                                                                                                                                                                    Name(id='model', ctx=Load()),
                                                                                                                                                                    Name(id='alias', ctx=Load()),
                                                                                                                                                                ],
                                                                                                                                                                keywords=[
                                                                                                                                                                    keyword(
                                                                                                                                                                        arg='internal',
                                                                                                                                                                        value=Constant(value=True, kind=None),
                                                                                                                                                                    ),
                                                                                                                                                                ],
                                                                                                                                                            ),
                                                                                                                                                        ),
                                                                                                                                                    ],
                                                                                                                                                ),
                                                                                                                                            ],
                                                                                                                                            orelse=[
                                                                                                                                                Assign(
                                                                                                                                                    targets=[Name(id='op1', ctx=Store())],
                                                                                                                                                    value=IfExp(
                                                                                                                                                        test=Compare(
                                                                                                                                                            left=Name(id='operator', ctx=Load()),
                                                                                                                                                            ops=[In()],
                                                                                                                                                            comparators=[Name(id='NEGATIVE_TERM_OPERATORS', ctx=Load())],
                                                                                                                                                        ),
                                                                                                                                                        body=Constant(value='inselect', kind=None),
                                                                                                                                                        orelse=Constant(value='not inselect', kind=None),
                                                                                                                                                    ),
                                                                                                                                                    type_comment=None,
                                                                                                                                                ),
                                                                                                                                                Assign(
                                                                                                                                                    targets=[Name(id='subquery', ctx=Store())],
                                                                                                                                                    value=BinOp(
                                                                                                                                                        left=Constant(value='SELECT "%s" FROM "%s" where "%s" is not null', kind=None),
                                                                                                                                                        op=Mod(),
                                                                                                                                                        right=Tuple(
                                                                                                                                                            elts=[
                                                                                                                                                                Name(id='rel_id1', ctx=Load()),
                                                                                                                                                                Name(id='rel_table', ctx=Load()),
                                                                                                                                                                Name(id='rel_id1', ctx=Load()),
                                                                                                                                                            ],
                                                                                                                                                            ctx=Load(),
                                                                                                                                                        ),
                                                                                                                                                    ),
                                                                                                                                                    type_comment=None,
                                                                                                                                                ),
                                                                                                                                                Expr(
                                                                                                                                                    value=Call(
                                                                                                                                                        func=Name(id='push', ctx=Load()),
                                                                                                                                                        args=[
                                                                                                                                                            Tuple(
                                                                                                                                                                elts=[
                                                                                                                                                                    Constant(value='id', kind=None),
                                                                                                                                                                    Name(id='op1', ctx=Load()),
                                                                                                                                                                    Tuple(
                                                                                                                                                                        elts=[
                                                                                                                                                                            Name(id='subquery', ctx=Load()),
                                                                                                                                                                            List(elts=[], ctx=Load()),
                                                                                                                                                                        ],
                                                                                                                                                                        ctx=Load(),
                                                                                                                                                                    ),
                                                                                                                                                                ],
                                                                                                                                                                ctx=Load(),
                                                                                                                                                            ),
                                                                                                                                                            Name(id='model', ctx=Load()),
                                                                                                                                                            Name(id='alias', ctx=Load()),
                                                                                                                                                        ],
                                                                                                                                                        keywords=[
                                                                                                                                                            keyword(
                                                                                                                                                                arg='internal',
                                                                                                                                                                value=Constant(value=True, kind=None),
                                                                                                                                                            ),
                                                                                                                                                        ],
                                                                                                                                                    ),
                                                                                                                                                ),
                                                                                                                                            ],
                                                                                                                                        ),
                                                                                                                                    ],
                                                                                                                                ),
                                                                                                                            ],
                                                                                                                            orelse=[
                                                                                                                                If(
                                                                                                                                    test=Compare(
                                                                                                                                        left=Attribute(
                                                                                                                                            value=Name(id='field', ctx=Load()),
                                                                                                                                            attr='type',
                                                                                                                                            ctx=Load(),
                                                                                                                                        ),
                                                                                                                                        ops=[Eq()],
                                                                                                                                        comparators=[Constant(value='many2one', kind=None)],
                                                                                                                                    ),
                                                                                                                                    body=[
                                                                                                                                        If(
                                                                                                                                            test=Compare(
                                                                                                                                                left=Name(id='operator', ctx=Load()),
                                                                                                                                                ops=[In()],
                                                                                                                                                comparators=[Name(id='HIERARCHY_FUNCS', ctx=Load())],
                                                                                                                                            ),
                                                                                                                                            body=[
                                                                                                                                                Assign(
                                                                                                                                                    targets=[Name(id='ids2', ctx=Store())],
                                                                                                                                                    value=Call(
                                                                                                                                                        func=Name(id='to_ids', ctx=Load()),
                                                                                                                                                        args=[
                                                                                                                                                            Name(id='right', ctx=Load()),
                                                                                                                                                            Name(id='comodel', ctx=Load()),
                                                                                                                                                            Name(id='leaf', ctx=Load()),
                                                                                                                                                        ],
                                                                                                                                                        keywords=[],
                                                                                                                                                    ),
                                                                                                                                                    type_comment=None,
                                                                                                                                                ),
                                                                                                                                                If(
                                                                                                                                                    test=Compare(
                                                                                                                                                        left=Attribute(
                                                                                                                                                            value=Name(id='field', ctx=Load()),
                                                                                                                                                            attr='comodel_name',
                                                                                                                                                            ctx=Load(),
                                                                                                                                                        ),
                                                                                                                                                        ops=[NotEq()],
                                                                                                                                                        comparators=[
                                                                                                                                                            Attribute(
                                                                                                                                                                value=Name(id='model', ctx=Load()),
                                                                                                                                                                attr='_name',
                                                                                                                                                                ctx=Load(),
                                                                                                                                                            ),
                                                                                                                                                        ],
                                                                                                                                                    ),
                                                                                                                                                    body=[
                                                                                                                                                        Assign(
                                                                                                                                                            targets=[Name(id='dom', ctx=Store())],
                                                                                                                                                            value=Call(
                                                                                                                                                                func=Subscript(
                                                                                                                                                                    value=Name(id='HIERARCHY_FUNCS', ctx=Load()),
                                                                                                                                                                    slice=Name(id='operator', ctx=Load()),
                                                                                                                                                                    ctx=Load(),
                                                                                                                                                                ),
                                                                                                                                                                args=[
                                                                                                                                                                    Name(id='left', ctx=Load()),
                                                                                                                                                                    Name(id='ids2', ctx=Load()),
                                                                                                                                                                    Name(id='comodel', ctx=Load()),
                                                                                                                                                                ],
                                                                                                                                                                keywords=[
                                                                                                                                                                    keyword(
                                                                                                                                                                        arg='prefix',
                                                                                                                                                                        value=Attribute(
                                                                                                                                                                            value=Name(id='field', ctx=Load()),
                                                                                                                                                                            attr='comodel_name',
                                                                                                                                                                            ctx=Load(),
                                                                                                                                                                        ),
                                                                                                                                                                    ),
                                                                                                                                                                ],
                                                                                                                                                            ),
                                                                                                                                                            type_comment=None,
                                                                                                                                                        ),
                                                                                                                                                    ],
                                                                                                                                                    orelse=[
                                                                                                                                                        Assign(
                                                                                                                                                            targets=[Name(id='dom', ctx=Store())],
                                                                                                                                                            value=Call(
                                                                                                                                                                func=Subscript(
                                                                                                                                                                    value=Name(id='HIERARCHY_FUNCS', ctx=Load()),
                                                                                                                                                                    slice=Name(id='operator', ctx=Load()),
                                                                                                                                                                    ctx=Load(),
                                                                                                                                                                ),
                                                                                                                                                                args=[
                                                                                                                                                                    Constant(value='id', kind=None),
                                                                                                                                                                    Name(id='ids2', ctx=Load()),
                                                                                                                                                                    Name(id='model', ctx=Load()),
                                                                                                                                                                ],
                                                                                                                                                                keywords=[
                                                                                                                                                                    keyword(
                                                                                                                                                                        arg='parent',
                                                                                                                                                                        value=Name(id='left', ctx=Load()),
                                                                                                                                                                    ),
                                                                                                                                                                ],
                                                                                                                                                            ),
                                                                                                                                                            type_comment=None,
                                                                                                                                                        ),
                                                                                                                                                    ],
                                                                                                                                                ),
                                                                                                                                                For(
                                                                                                                                                    target=Name(id='dom_leaf', ctx=Store()),
                                                                                                                                                    iter=Name(id='dom', ctx=Load()),
                                                                                                                                                    body=[
                                                                                                                                                        Expr(
                                                                                                                                                            value=Call(
                                                                                                                                                                func=Name(id='push', ctx=Load()),
                                                                                                                                                                args=[
                                                                                                                                                                    Name(id='dom_leaf', ctx=Load()),
                                                                                                                                                                    Name(id='model', ctx=Load()),
                                                                                                                                                                    Name(id='alias', ctx=Load()),
                                                                                                                                                                ],
                                                                                                                                                                keywords=[],
                                                                                                                                                            ),
                                                                                                                                                        ),
                                                                                                                                                    ],
                                                                                                                                                    orelse=[],
                                                                                                                                                    type_comment=None,
                                                                                                                                                ),
                                                                                                                                            ],
                                                                                                                                            orelse=[
                                                                                                                                                FunctionDef(
                                                                                                                                                    name='_get_expression',
                                                                                                                                                    args=arguments(
                                                                                                                                                        posonlyargs=[],
                                                                                                                                                        args=[
                                                                                                                                                            arg(arg='comodel', annotation=None, type_comment=None),
                                                                                                                                                            arg(arg='left', annotation=None, type_comment=None),
                                                                                                                                                            arg(arg='right', annotation=None, type_comment=None),
                                                                                                                                                            arg(arg='operator', annotation=None, type_comment=None),
                                                                                                                                                        ],
                                                                                                                                                        vararg=None,
                                                                                                                                                        kwonlyargs=[],
                                                                                                                                                        kw_defaults=[],
                                                                                                                                                        kwarg=None,
                                                                                                                                                        defaults=[],
                                                                                                                                                    ),
                                                                                                                                                    body=[
                                                                                                                                                        Assign(
                                                                                                                                                            targets=[Name(id='operator', ctx=Store())],
                                                                                                                                                            value=BoolOp(
                                                                                                                                                                op=Or(),
                                                                                                                                                                values=[
                                                                                                                                                                    BoolOp(
                                                                                                                                                                        op=And(),
                                                                                                                                                                        values=[
                                                                                                                                                                            Compare(
                                                                                                                                                                                left=Name(id='operator', ctx=Load()),
                                                                                                                                                                                ops=[In()],
                                                                                                                                                                                comparators=[
                                                                                                                                                                                    List(
                                                                                                                                                                                        elts=[
                                                                                                                                                                                            Constant(value='<', kind=None),
                                                                                                                                                                                            Constant(value='>', kind=None),
                                                                                                                                                                                            Constant(value='<=', kind=None),
                                                                                                                                                                                            Constant(value='>=', kind=None),
                                                                                                                                                                                        ],
                                                                                                                                                                                        ctx=Load(),
                                                                                                                                                                                    ),
                                                                                                                                                                                ],
                                                                                                                                                                            ),
                                                                                                                                                                            Constant(value='in', kind=None),
                                                                                                                                                                        ],
                                                                                                                                                                    ),
                                                                                                                                                                    Name(id='operator', ctx=Load()),
                                                                                                                                                                ],
                                                                                                                                                            ),
                                                                                                                                                            type_comment=None,
                                                                                                                                                        ),
                                                                                                                                                        Assign(
                                                                                                                                                            targets=[Name(id='dict_op', ctx=Store())],
                                                                                                                                                            value=Dict(
                                                                                                                                                                keys=[
                                                                                                                                                                    Constant(value='not in', kind=None),
                                                                                                                                                                    Constant(value='in', kind=None),
                                                                                                                                                                    Constant(value='=', kind=None),
                                                                                                                                                                    Constant(value='!=', kind=None),
                                                                                                                                                                ],
                                                                                                                                                                values=[
                                                                                                                                                                    Constant(value='!=', kind=None),
                                                                                                                                                                    Constant(value='=', kind=None),
                                                                                                                                                                    Constant(value='in', kind=None),
                                                                                                                                                                    Constant(value='not in', kind=None),
                                                                                                                                                                ],
                                                                                                                                                            ),
                                                                                                                                                            type_comment=None,
                                                                                                                                                        ),
                                                                                                                                                        If(
                                                                                                                                                            test=Call(
                                                                                                                                                                func=Name(id='isinstance', ctx=Load()),
                                                                                                                                                                args=[
                                                                                                                                                                    Name(id='right', ctx=Load()),
                                                                                                                                                                    Name(id='tuple', ctx=Load()),
                                                                                                                                                                ],
                                                                                                                                                                keywords=[],
                                                                                                                                                            ),
                                                                                                                                                            body=[
                                                                                                                                                                Assign(
                                                                                                                                                                    targets=[Name(id='right', ctx=Store())],
                                                                                                                                                                    value=Call(
                                                                                                                                                                        func=Name(id='list', ctx=Load()),
                                                                                                                                                                        args=[Name(id='right', ctx=Load())],
                                                                                                                                                                        keywords=[],
                                                                                                                                                                    ),
                                                                                                                                                                    type_comment=None,
                                                                                                                                                                ),
                                                                                                                                                            ],
                                                                                                                                                            orelse=[],
                                                                                                                                                        ),
                                                                                                                                                        If(
                                                                                                                                                            test=BoolOp(
                                                                                                                                                                op=And(),
                                                                                                                                                                values=[
                                                                                                                                                                    UnaryOp(
                                                                                                                                                                        op=Not(),
                                                                                                                                                                        operand=Call(
                                                                                                                                                                            func=Name(id='isinstance', ctx=Load()),
                                                                                                                                                                            args=[
                                                                                                                                                                                Name(id='right', ctx=Load()),
                                                                                                                                                                                Name(id='list', ctx=Load()),
                                                                                                                                                                            ],
                                                                                                                                                                            keywords=[],
                                                                                                                                                                        ),
                                                                                                                                                                    ),
                                                                                                                                                                    Compare(
                                                                                                                                                                        left=Name(id='operator', ctx=Load()),
                                                                                                                                                                        ops=[In()],
                                                                                                                                                                        comparators=[
                                                                                                                                                                            List(
                                                                                                                                                                                elts=[
                                                                                                                                                                                    Constant(value='not in', kind=None),
                                                                                                                                                                                    Constant(value='in', kind=None),
                                                                                                                                                                                ],
                                                                                                                                                                                ctx=Load(),
                                                                                                                                                                            ),
                                                                                                                                                                        ],
                                                                                                                                                                    ),
                                                                                                                                                                ],
                                                                                                                                                            ),
                                                                                                                                                            body=[
                                                                                                                                                                Assign(
                                                                                                                                                                    targets=[Name(id='operator', ctx=Store())],
                                                                                                                                                                    value=Subscript(
                                                                                                                                                                        value=Name(id='dict_op', ctx=Load()),
                                                                                                                                                                        slice=Name(id='operator', ctx=Load()),
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
                                                                                                                                                                            Call(
                                                                                                                                                                                func=Name(id='isinstance', ctx=Load()),
                                                                                                                                                                                args=[
                                                                                                                                                                                    Name(id='right', ctx=Load()),
                                                                                                                                                                                    Name(id='list', ctx=Load()),
                                                                                                                                                                                ],
                                                                                                                                                                                keywords=[],
                                                                                                                                                                            ),
                                                                                                                                                                            Compare(
                                                                                                                                                                                left=Name(id='operator', ctx=Load()),
                                                                                                                                                                                ops=[In()],
                                                                                                                                                                                comparators=[
                                                                                                                                                                                    List(
                                                                                                                                                                                        elts=[
                                                                                                                                                                                            Constant(value='!=', kind=None),
                                                                                                                                                                                            Constant(value='=', kind=None),
                                                                                                                                                                                        ],
                                                                                                                                                                                        ctx=Load(),
                                                                                                                                                                                    ),
                                                                                                                                                                                ],
                                                                                                                                                                            ),
                                                                                                                                                                        ],
                                                                                                                                                                    ),
                                                                                                                                                                    body=[
                                                                                                                                                                        Assign(
                                                                                                                                                                            targets=[Name(id='operator', ctx=Store())],
                                                                                                                                                                            value=Subscript(
                                                                                                                                                                                value=Name(id='dict_op', ctx=Load()),
                                                                                                                                                                                slice=Name(id='operator', ctx=Load()),
                                                                                                                                                                                ctx=Load(),
                                                                                                                                                                            ),
                                                                                                                                                                            type_comment=None,
                                                                                                                                                                        ),
                                                                                                                                                                    ],
                                                                                                                                                                    orelse=[],
                                                                                                                                                                ),
                                                                                                                                                            ],
                                                                                                                                                        ),
                                                                                                                                                        Assign(
                                                                                                                                                            targets=[Name(id='res_ids', ctx=Store())],
                                                                                                                                                            value=Call(
                                                                                                                                                                func=Attribute(
                                                                                                                                                                    value=Call(
                                                                                                                                                                        func=Attribute(
                                                                                                                                                                            value=Name(id='comodel', ctx=Load()),
                                                                                                                                                                            attr='with_context',
                                                                                                                                                                            ctx=Load(),
                                                                                                                                                                        ),
                                                                                                                                                                        args=[],
                                                                                                                                                                        keywords=[
                                                                                                                                                                            keyword(
                                                                                                                                                                                arg='active_test',
                                                                                                                                                                                value=Constant(value=False, kind=None),
                                                                                                                                                                            ),
                                                                                                                                                                        ],
                                                                                                                                                                    ),
                                                                                                                                                                    attr='_name_search',
                                                                                                                                                                    ctx=Load(),
                                                                                                                                                                ),
                                                                                                                                                                args=[
                                                                                                                                                                    Name(id='right', ctx=Load()),
                                                                                                                                                                    List(elts=[], ctx=Load()),
                                                                                                                                                                    Name(id='operator', ctx=Load()),
                                                                                                                                                                ],
                                                                                                                                                                keywords=[
                                                                                                                                                                    keyword(
                                                                                                                                                                        arg='limit',
                                                                                                                                                                        value=Constant(value=None, kind=None),
                                                                                                                                                                    ),
                                                                                                                                                                ],
                                                                                                                                                            ),
                                                                                                                                                            type_comment=None,
                                                                                                                                                        ),
                                                                                                                                                        If(
                                                                                                                                                            test=Compare(
                                                                                                                                                                left=Name(id='operator', ctx=Load()),
                                                                                                                                                                ops=[In()],
                                                                                                                                                                comparators=[Name(id='NEGATIVE_TERM_OPERATORS', ctx=Load())],
                                                                                                                                                            ),
                                                                                                                                                            body=[
                                                                                                                                                                Assign(
                                                                                                                                                                    targets=[Name(id='res_ids', ctx=Store())],
                                                                                                                                                                    value=BinOp(
                                                                                                                                                                        left=Call(
                                                                                                                                                                            func=Name(id='list', ctx=Load()),
                                                                                                                                                                            args=[Name(id='res_ids', ctx=Load())],
                                                                                                                                                                            keywords=[],
                                                                                                                                                                        ),
                                                                                                                                                                        op=Add(),
                                                                                                                                                                        right=List(
                                                                                                                                                                            elts=[Constant(value=False, kind=None)],
                                                                                                                                                                            ctx=Load(),
                                                                                                                                                                        ),
                                                                                                                                                                    ),
                                                                                                                                                                    type_comment=None,
                                                                                                                                                                ),
                                                                                                                                                            ],
                                                                                                                                                            orelse=[],
                                                                                                                                                        ),
                                                                                                                                                        Return(
                                                                                                                                                            value=Tuple(
                                                                                                                                                                elts=[
                                                                                                                                                                    Name(id='left', ctx=Load()),
                                                                                                                                                                    Constant(value='in', kind=None),
                                                                                                                                                                    Name(id='res_ids', ctx=Load()),
                                                                                                                                                                ],
                                                                                                                                                                ctx=Load(),
                                                                                                                                                            ),
                                                                                                                                                        ),
                                                                                                                                                    ],
                                                                                                                                                    decorator_list=[],
                                                                                                                                                    returns=None,
                                                                                                                                                    type_comment=None,
                                                                                                                                                ),
                                                                                                                                                If(
                                                                                                                                                    test=BoolOp(
                                                                                                                                                        op=Or(),
                                                                                                                                                        values=[
                                                                                                                                                            Call(
                                                                                                                                                                func=Name(id='isinstance', ctx=Load()),
                                                                                                                                                                args=[
                                                                                                                                                                    Name(id='right', ctx=Load()),
                                                                                                                                                                    Name(id='str', ctx=Load()),
                                                                                                                                                                ],
                                                                                                                                                                keywords=[],
                                                                                                                                                            ),
                                                                                                                                                            BoolOp(
                                                                                                                                                                op=And(),
                                                                                                                                                                values=[
                                                                                                                                                                    Call(
                                                                                                                                                                        func=Name(id='isinstance', ctx=Load()),
                                                                                                                                                                        args=[
                                                                                                                                                                            Name(id='right', ctx=Load()),
                                                                                                                                                                            Tuple(
                                                                                                                                                                                elts=[
                                                                                                                                                                                    Name(id='tuple', ctx=Load()),
                                                                                                                                                                                    Name(id='list', ctx=Load()),
                                                                                                                                                                                ],
                                                                                                                                                                                ctx=Load(),
                                                                                                                                                                            ),
                                                                                                                                                                        ],
                                                                                                                                                                        keywords=[],
                                                                                                                                                                    ),
                                                                                                                                                                    Name(id='right', ctx=Load()),
                                                                                                                                                                    Call(
                                                                                                                                                                        func=Name(id='all', ctx=Load()),
                                                                                                                                                                        args=[
                                                                                                                                                                            GeneratorExp(
                                                                                                                                                                                elt=Call(
                                                                                                                                                                                    func=Name(id='isinstance', ctx=Load()),
                                                                                                                                                                                    args=[
                                                                                                                                                                                        Name(id='item', ctx=Load()),
                                                                                                                                                                                        Name(id='str', ctx=Load()),
                                                                                                                                                                                    ],
                                                                                                                                                                                    keywords=[],
                                                                                                                                                                                ),
                                                                                                                                                                                generators=[
                                                                                                                                                                                    comprehension(
                                                                                                                                                                                        target=Name(id='item', ctx=Store()),
                                                                                                                                                                                        iter=Name(id='right', ctx=Load()),
                                                                                                                                                                                        ifs=[],
                                                                                                                                                                                        is_async=0,
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
                                                                                                                                                    body=[
                                                                                                                                                        Expr(
                                                                                                                                                            value=Call(
                                                                                                                                                                func=Name(id='push', ctx=Load()),
                                                                                                                                                                args=[
                                                                                                                                                                    Call(
                                                                                                                                                                        func=Name(id='_get_expression', ctx=Load()),
                                                                                                                                                                        args=[
                                                                                                                                                                            Name(id='comodel', ctx=Load()),
                                                                                                                                                                            Name(id='left', ctx=Load()),
                                                                                                                                                                            Name(id='right', ctx=Load()),
                                                                                                                                                                            Name(id='operator', ctx=Load()),
                                                                                                                                                                        ],
                                                                                                                                                                        keywords=[],
                                                                                                                                                                    ),
                                                                                                                                                                    Name(id='model', ctx=Load()),
                                                                                                                                                                    Name(id='alias', ctx=Load()),
                                                                                                                                                                ],
                                                                                                                                                                keywords=[],
                                                                                                                                                            ),
                                                                                                                                                        ),
                                                                                                                                                    ],
                                                                                                                                                    orelse=[
                                                                                                                                                        Assign(
                                                                                                                                                            targets=[
                                                                                                                                                                Tuple(
                                                                                                                                                                    elts=[
                                                                                                                                                                        Name(id='expr', ctx=Store()),
                                                                                                                                                                        Name(id='params', ctx=Store()),
                                                                                                                                                                    ],
                                                                                                                                                                    ctx=Store(),
                                                                                                                                                                ),
                                                                                                                                                            ],
                                                                                                                                                            value=Call(
                                                                                                                                                                func=Attribute(
                                                                                                                                                                    value=Name(id='self', ctx=Load()),
                                                                                                                                                                    attr='__leaf_to_sql',
                                                                                                                                                                    ctx=Load(),
                                                                                                                                                                ),
                                                                                                                                                                args=[
                                                                                                                                                                    Name(id='leaf', ctx=Load()),
                                                                                                                                                                    Name(id='model', ctx=Load()),
                                                                                                                                                                    Name(id='alias', ctx=Load()),
                                                                                                                                                                ],
                                                                                                                                                                keywords=[],
                                                                                                                                                            ),
                                                                                                                                                            type_comment=None,
                                                                                                                                                        ),
                                                                                                                                                        Expr(
                                                                                                                                                            value=Call(
                                                                                                                                                                func=Name(id='push_result', ctx=Load()),
                                                                                                                                                                args=[
                                                                                                                                                                    Name(id='expr', ctx=Load()),
                                                                                                                                                                    Name(id='params', ctx=Load()),
                                                                                                                                                                ],
                                                                                                                                                                keywords=[],
                                                                                                                                                            ),
                                                                                                                                                        ),
                                                                                                                                                    ],
                                                                                                                                                ),
                                                                                                                                            ],
                                                                                                                                        ),
                                                                                                                                    ],
                                                                                                                                    orelse=[
                                                                                                                                        If(
                                                                                                                                            test=BoolOp(
                                                                                                                                                op=And(),
                                                                                                                                                values=[
                                                                                                                                                    Compare(
                                                                                                                                                        left=Attribute(
                                                                                                                                                            value=Name(id='field', ctx=Load()),
                                                                                                                                                            attr='type',
                                                                                                                                                            ctx=Load(),
                                                                                                                                                        ),
                                                                                                                                                        ops=[Eq()],
                                                                                                                                                        comparators=[Constant(value='binary', kind=None)],
                                                                                                                                                    ),
                                                                                                                                                    Attribute(
                                                                                                                                                        value=Name(id='field', ctx=Load()),
                                                                                                                                                        attr='attachment',
                                                                                                                                                        ctx=Load(),
                                                                                                                                                    ),
                                                                                                                                                ],
                                                                                                                                            ),
                                                                                                                                            body=[
                                                                                                                                                If(
                                                                                                                                                    test=BoolOp(
                                                                                                                                                        op=And(),
                                                                                                                                                        values=[
                                                                                                                                                            Compare(
                                                                                                                                                                left=Name(id='operator', ctx=Load()),
                                                                                                                                                                ops=[In()],
                                                                                                                                                                comparators=[
                                                                                                                                                                    Tuple(
                                                                                                                                                                        elts=[
                                                                                                                                                                            Constant(value='=', kind=None),
                                                                                                                                                                            Constant(value='!=', kind=None),
                                                                                                                                                                        ],
                                                                                                                                                                        ctx=Load(),
                                                                                                                                                                    ),
                                                                                                                                                                ],
                                                                                                                                                            ),
                                                                                                                                                            UnaryOp(
                                                                                                                                                                op=Not(),
                                                                                                                                                                operand=Name(id='right', ctx=Load()),
                                                                                                                                                            ),
                                                                                                                                                        ],
                                                                                                                                                    ),
                                                                                                                                                    body=[
                                                                                                                                                        Assign(
                                                                                                                                                            targets=[Name(id='inselect_operator', ctx=Store())],
                                                                                                                                                            value=IfExp(
                                                                                                                                                                test=Compare(
                                                                                                                                                                    left=Name(id='operator', ctx=Load()),
                                                                                                                                                                    ops=[In()],
                                                                                                                                                                    comparators=[Name(id='NEGATIVE_TERM_OPERATORS', ctx=Load())],
                                                                                                                                                                ),
                                                                                                                                                                body=Constant(value='inselect', kind=None),
                                                                                                                                                                orelse=Constant(value='not inselect', kind=None),
                                                                                                                                                            ),
                                                                                                                                                            type_comment=None,
                                                                                                                                                        ),
                                                                                                                                                        Assign(
                                                                                                                                                            targets=[Name(id='subselect', ctx=Store())],
                                                                                                                                                            value=Constant(value='SELECT res_id FROM ir_attachment WHERE res_model=%s AND res_field=%s', kind=None),
                                                                                                                                                            type_comment=None,
                                                                                                                                                        ),
                                                                                                                                                        Assign(
                                                                                                                                                            targets=[Name(id='params', ctx=Store())],
                                                                                                                                                            value=Tuple(
                                                                                                                                                                elts=[
                                                                                                                                                                    Attribute(
                                                                                                                                                                        value=Name(id='model', ctx=Load()),
                                                                                                                                                                        attr='_name',
                                                                                                                                                                        ctx=Load(),
                                                                                                                                                                    ),
                                                                                                                                                                    Name(id='left', ctx=Load()),
                                                                                                                                                                ],
                                                                                                                                                                ctx=Load(),
                                                                                                                                                            ),
                                                                                                                                                            type_comment=None,
                                                                                                                                                        ),
                                                                                                                                                        Expr(
                                                                                                                                                            value=Call(
                                                                                                                                                                func=Name(id='push', ctx=Load()),
                                                                                                                                                                args=[
                                                                                                                                                                    Tuple(
                                                                                                                                                                        elts=[
                                                                                                                                                                            Constant(value='id', kind=None),
                                                                                                                                                                            Name(id='inselect_operator', ctx=Load()),
                                                                                                                                                                            Tuple(
                                                                                                                                                                                elts=[
                                                                                                                                                                                    Name(id='subselect', ctx=Load()),
                                                                                                                                                                                    Name(id='params', ctx=Load()),
                                                                                                                                                                                ],
                                                                                                                                                                                ctx=Load(),
                                                                                                                                                                            ),
                                                                                                                                                                        ],
                                                                                                                                                                        ctx=Load(),
                                                                                                                                                                    ),
                                                                                                                                                                    Name(id='model', ctx=Load()),
                                                                                                                                                                    Name(id='alias', ctx=Load()),
                                                                                                                                                                ],
                                                                                                                                                                keywords=[
                                                                                                                                                                    keyword(
                                                                                                                                                                        arg='internal',
                                                                                                                                                                        value=Constant(value=True, kind=None),
                                                                                                                                                                    ),
                                                                                                                                                                ],
                                                                                                                                                            ),
                                                                                                                                                        ),
                                                                                                                                                    ],
                                                                                                                                                    orelse=[
                                                                                                                                                        Expr(
                                                                                                                                                            value=Call(
                                                                                                                                                                func=Attribute(
                                                                                                                                                                    value=Name(id='_logger', ctx=Load()),
                                                                                                                                                                    attr='error',
                                                                                                                                                                    ctx=Load(),
                                                                                                                                                                ),
                                                                                                                                                                args=[
                                                                                                                                                                    Constant(value="Binary field '%s' stored in attachment: ignore %s %s %s", kind=None),
                                                                                                                                                                    Attribute(
                                                                                                                                                                        value=Name(id='field', ctx=Load()),
                                                                                                                                                                        attr='string',
                                                                                                                                                                        ctx=Load(),
                                                                                                                                                                    ),
                                                                                                                                                                    Name(id='left', ctx=Load()),
                                                                                                                                                                    Name(id='operator', ctx=Load()),
                                                                                                                                                                    Call(
                                                                                                                                                                        func=Attribute(
                                                                                                                                                                            value=Name(id='reprlib', ctx=Load()),
                                                                                                                                                                            attr='repr',
                                                                                                                                                                            ctx=Load(),
                                                                                                                                                                        ),
                                                                                                                                                                        args=[Name(id='right', ctx=Load())],
                                                                                                                                                                        keywords=[],
                                                                                                                                                                    ),
                                                                                                                                                                ],
                                                                                                                                                                keywords=[],
                                                                                                                                                            ),
                                                                                                                                                        ),
                                                                                                                                                        Expr(
                                                                                                                                                            value=Call(
                                                                                                                                                                func=Name(id='push', ctx=Load()),
                                                                                                                                                                args=[
                                                                                                                                                                    Name(id='TRUE_LEAF', ctx=Load()),
                                                                                                                                                                    Name(id='model', ctx=Load()),
                                                                                                                                                                    Name(id='alias', ctx=Load()),
                                                                                                                                                                ],
                                                                                                                                                                keywords=[],
                                                                                                                                                            ),
                                                                                                                                                        ),
                                                                                                                                                    ],
                                                                                                                                                ),
                                                                                                                                            ],
                                                                                                                                            orelse=[
                                                                                                                                                If(
                                                                                                                                                    test=BoolOp(
                                                                                                                                                        op=And(),
                                                                                                                                                        values=[
                                                                                                                                                            Compare(
                                                                                                                                                                left=Attribute(
                                                                                                                                                                    value=Name(id='field', ctx=Load()),
                                                                                                                                                                    attr='type',
                                                                                                                                                                    ctx=Load(),
                                                                                                                                                                ),
                                                                                                                                                                ops=[Eq()],
                                                                                                                                                                comparators=[Constant(value='datetime', kind=None)],
                                                                                                                                                            ),
                                                                                                                                                            Name(id='right', ctx=Load()),
                                                                                                                                                        ],
                                                                                                                                                    ),
                                                                                                                                                    body=[
                                                                                                                                                        If(
                                                                                                                                                            test=BoolOp(
                                                                                                                                                                op=And(),
                                                                                                                                                                values=[
                                                                                                                                                                    Call(
                                                                                                                                                                        func=Name(id='isinstance', ctx=Load()),
                                                                                                                                                                        args=[
                                                                                                                                                                            Name(id='right', ctx=Load()),
                                                                                                                                                                            Name(id='str', ctx=Load()),
                                                                                                                                                                        ],
                                                                                                                                                                        keywords=[],
                                                                                                                                                                    ),
                                                                                                                                                                    Compare(
                                                                                                                                                                        left=Call(
                                                                                                                                                                            func=Name(id='len', ctx=Load()),
                                                                                                                                                                            args=[Name(id='right', ctx=Load())],
                                                                                                                                                                            keywords=[],
                                                                                                                                                                        ),
                                                                                                                                                                        ops=[Eq()],
                                                                                                                                                                        comparators=[Constant(value=10, kind=None)],
                                                                                                                                                                    ),
                                                                                                                                                                ],
                                                                                                                                                            ),
                                                                                                                                                            body=[
                                                                                                                                                                If(
                                                                                                                                                                    test=Compare(
                                                                                                                                                                        left=Name(id='operator', ctx=Load()),
                                                                                                                                                                        ops=[In()],
                                                                                                                                                                        comparators=[
                                                                                                                                                                            Tuple(
                                                                                                                                                                                elts=[
                                                                                                                                                                                    Constant(value='>', kind=None),
                                                                                                                                                                                    Constant(value='<=', kind=None),
                                                                                                                                                                                ],
                                                                                                                                                                                ctx=Load(),
                                                                                                                                                                            ),
                                                                                                                                                                        ],
                                                                                                                                                                    ),
                                                                                                                                                                    body=[
                                                                                                                                                                        AugAssign(
                                                                                                                                                                            target=Name(id='right', ctx=Store()),
                                                                                                                                                                            op=Add(),
                                                                                                                                                                            value=Constant(value=' 23:59:59', kind=None),
                                                                                                                                                                        ),
                                                                                                                                                                    ],
                                                                                                                                                                    orelse=[
                                                                                                                                                                        AugAssign(
                                                                                                                                                                            target=Name(id='right', ctx=Store()),
                                                                                                                                                                            op=Add(),
                                                                                                                                                                            value=Constant(value=' 00:00:00', kind=None),
                                                                                                                                                                        ),
                                                                                                                                                                    ],
                                                                                                                                                                ),
                                                                                                                                                                Expr(
                                                                                                                                                                    value=Call(
                                                                                                                                                                        func=Name(id='push', ctx=Load()),
                                                                                                                                                                        args=[
                                                                                                                                                                            Tuple(
                                                                                                                                                                                elts=[
                                                                                                                                                                                    Name(id='left', ctx=Load()),
                                                                                                                                                                                    Name(id='operator', ctx=Load()),
                                                                                                                                                                                    Name(id='right', ctx=Load()),
                                                                                                                                                                                ],
                                                                                                                                                                                ctx=Load(),
                                                                                                                                                                            ),
                                                                                                                                                                            Name(id='model', ctx=Load()),
                                                                                                                                                                            Name(id='alias', ctx=Load()),
                                                                                                                                                                        ],
                                                                                                                                                                        keywords=[],
                                                                                                                                                                    ),
                                                                                                                                                                ),
                                                                                                                                                            ],
                                                                                                                                                            orelse=[
                                                                                                                                                                If(
                                                                                                                                                                    test=BoolOp(
                                                                                                                                                                        op=And(),
                                                                                                                                                                        values=[
                                                                                                                                                                            Call(
                                                                                                                                                                                func=Name(id='isinstance', ctx=Load()),
                                                                                                                                                                                args=[
                                                                                                                                                                                    Name(id='right', ctx=Load()),
                                                                                                                                                                                    Name(id='date', ctx=Load()),
                                                                                                                                                                                ],
                                                                                                                                                                                keywords=[],
                                                                                                                                                                            ),
                                                                                                                                                                            UnaryOp(
                                                                                                                                                                                op=Not(),
                                                                                                                                                                                operand=Call(
                                                                                                                                                                                    func=Name(id='isinstance', ctx=Load()),
                                                                                                                                                                                    args=[
                                                                                                                                                                                        Name(id='right', ctx=Load()),
                                                                                                                                                                                        Name(id='datetime', ctx=Load()),
                                                                                                                                                                                    ],
                                                                                                                                                                                    keywords=[],
                                                                                                                                                                                ),
                                                                                                                                                                            ),
                                                                                                                                                                        ],
                                                                                                                                                                    ),
                                                                                                                                                                    body=[
                                                                                                                                                                        If(
                                                                                                                                                                            test=Compare(
                                                                                                                                                                                left=Name(id='operator', ctx=Load()),
                                                                                                                                                                                ops=[In()],
                                                                                                                                                                                comparators=[
                                                                                                                                                                                    Tuple(
                                                                                                                                                                                        elts=[
                                                                                                                                                                                            Constant(value='>', kind=None),
                                                                                                                                                                                            Constant(value='<=', kind=None),
                                                                                                                                                                                        ],
                                                                                                                                                                                        ctx=Load(),
                                                                                                                                                                                    ),
                                                                                                                                                                                ],
                                                                                                                                                                            ),
                                                                                                                                                                            body=[
                                                                                                                                                                                Assign(
                                                                                                                                                                                    targets=[Name(id='right', ctx=Store())],
                                                                                                                                                                                    value=Call(
                                                                                                                                                                                        func=Attribute(
                                                                                                                                                                                            value=Name(id='datetime', ctx=Load()),
                                                                                                                                                                                            attr='combine',
                                                                                                                                                                                            ctx=Load(),
                                                                                                                                                                                        ),
                                                                                                                                                                                        args=[
                                                                                                                                                                                            Name(id='right', ctx=Load()),
                                                                                                                                                                                            Attribute(
                                                                                                                                                                                                value=Name(id='time', ctx=Load()),
                                                                                                                                                                                                attr='max',
                                                                                                                                                                                                ctx=Load(),
                                                                                                                                                                                            ),
                                                                                                                                                                                        ],
                                                                                                                                                                                        keywords=[],
                                                                                                                                                                                    ),
                                                                                                                                                                                    type_comment=None,
                                                                                                                                                                                ),
                                                                                                                                                                            ],
                                                                                                                                                                            orelse=[
                                                                                                                                                                                Assign(
                                                                                                                                                                                    targets=[Name(id='right', ctx=Store())],
                                                                                                                                                                                    value=Call(
                                                                                                                                                                                        func=Attribute(
                                                                                                                                                                                            value=Name(id='datetime', ctx=Load()),
                                                                                                                                                                                            attr='combine',
                                                                                                                                                                                            ctx=Load(),
                                                                                                                                                                                        ),
                                                                                                                                                                                        args=[
                                                                                                                                                                                            Name(id='right', ctx=Load()),
                                                                                                                                                                                            Attribute(
                                                                                                                                                                                                value=Name(id='time', ctx=Load()),
                                                                                                                                                                                                attr='min',
                                                                                                                                                                                                ctx=Load(),
                                                                                                                                                                                            ),
                                                                                                                                                                                        ],
                                                                                                                                                                                        keywords=[],
                                                                                                                                                                                    ),
                                                                                                                                                                                    type_comment=None,
                                                                                                                                                                                ),
                                                                                                                                                                            ],
                                                                                                                                                                        ),
                                                                                                                                                                        Expr(
                                                                                                                                                                            value=Call(
                                                                                                                                                                                func=Name(id='push', ctx=Load()),
                                                                                                                                                                                args=[
                                                                                                                                                                                    Tuple(
                                                                                                                                                                                        elts=[
                                                                                                                                                                                            Name(id='left', ctx=Load()),
                                                                                                                                                                                            Name(id='operator', ctx=Load()),
                                                                                                                                                                                            Name(id='right', ctx=Load()),
                                                                                                                                                                                        ],
                                                                                                                                                                                        ctx=Load(),
                                                                                                                                                                                    ),
                                                                                                                                                                                    Name(id='model', ctx=Load()),
                                                                                                                                                                                    Name(id='alias', ctx=Load()),
                                                                                                                                                                                ],
                                                                                                                                                                                keywords=[],
                                                                                                                                                                            ),
                                                                                                                                                                        ),
                                                                                                                                                                    ],
                                                                                                                                                                    orelse=[
                                                                                                                                                                        Assign(
                                                                                                                                                                            targets=[
                                                                                                                                                                                Tuple(
                                                                                                                                                                                    elts=[
                                                                                                                                                                                        Name(id='expr', ctx=Store()),
                                                                                                                                                                                        Name(id='params', ctx=Store()),
                                                                                                                                                                                    ],
                                                                                                                                                                                    ctx=Store(),
                                                                                                                                                                                ),
                                                                                                                                                                            ],
                                                                                                                                                                            value=Call(
                                                                                                                                                                                func=Attribute(
                                                                                                                                                                                    value=Name(id='self', ctx=Load()),
                                                                                                                                                                                    attr='__leaf_to_sql',
                                                                                                                                                                                    ctx=Load(),
                                                                                                                                                                                ),
                                                                                                                                                                                args=[
                                                                                                                                                                                    Name(id='leaf', ctx=Load()),
                                                                                                                                                                                    Name(id='model', ctx=Load()),
                                                                                                                                                                                    Name(id='alias', ctx=Load()),
                                                                                                                                                                                ],
                                                                                                                                                                                keywords=[],
                                                                                                                                                                            ),
                                                                                                                                                                            type_comment=None,
                                                                                                                                                                        ),
                                                                                                                                                                        Expr(
                                                                                                                                                                            value=Call(
                                                                                                                                                                                func=Name(id='push_result', ctx=Load()),
                                                                                                                                                                                args=[
                                                                                                                                                                                    Name(id='expr', ctx=Load()),
                                                                                                                                                                                    Name(id='params', ctx=Load()),
                                                                                                                                                                                ],
                                                                                                                                                                                keywords=[],
                                                                                                                                                                            ),
                                                                                                                                                                        ),
                                                                                                                                                                    ],
                                                                                                                                                                ),
                                                                                                                                                            ],
                                                                                                                                                        ),
                                                                                                                                                    ],
                                                                                                                                                    orelse=[
                                                                                                                                                        If(
                                                                                                                                                            test=BoolOp(
                                                                                                                                                                op=And(),
                                                                                                                                                                values=[
                                                                                                                                                                    Compare(
                                                                                                                                                                        left=Attribute(
                                                                                                                                                                            value=Name(id='field', ctx=Load()),
                                                                                                                                                                            attr='translate',
                                                                                                                                                                            ctx=Load(),
                                                                                                                                                                        ),
                                                                                                                                                                        ops=[Is()],
                                                                                                                                                                        comparators=[Constant(value=True, kind=None)],
                                                                                                                                                                    ),
                                                                                                                                                                    Name(id='right', ctx=Load()),
                                                                                                                                                                ],
                                                                                                                                                            ),
                                                                                                                                                            body=[
                                                                                                                                                                Assign(
                                                                                                                                                                    targets=[Name(id='need_wildcard', ctx=Store())],
                                                                                                                                                                    value=Compare(
                                                                                                                                                                        left=Name(id='operator', ctx=Load()),
                                                                                                                                                                        ops=[In()],
                                                                                                                                                                        comparators=[
                                                                                                                                                                            Tuple(
                                                                                                                                                                                elts=[
                                                                                                                                                                                    Constant(value='like', kind=None),
                                                                                                                                                                                    Constant(value='ilike', kind=None),
                                                                                                                                                                                    Constant(value='not like', kind=None),
                                                                                                                                                                                    Constant(value='not ilike', kind=None),
                                                                                                                                                                                ],
                                                                                                                                                                                ctx=Load(),
                                                                                                                                                                            ),
                                                                                                                                                                        ],
                                                                                                                                                                    ),
                                                                                                                                                                    type_comment=None,
                                                                                                                                                                ),
                                                                                                                                                                Assign(
                                                                                                                                                                    targets=[Name(id='sql_operator', ctx=Store())],
                                                                                                                                                                    value=Call(
                                                                                                                                                                        func=Attribute(
                                                                                                                                                                            value=Dict(
                                                                                                                                                                                keys=[
                                                                                                                                                                                    Constant(value='=like', kind=None),
                                                                                                                                                                                    Constant(value='=ilike', kind=None),
                                                                                                                                                                                ],
                                                                                                                                                                                values=[
                                                                                                                                                                                    Constant(value='like', kind=None),
                                                                                                                                                                                    Constant(value='ilike', kind=None),
                                                                                                                                                                                ],
                                                                                                                                                                            ),
                                                                                                                                                                            attr='get',
                                                                                                                                                                            ctx=Load(),
                                                                                                                                                                        ),
                                                                                                                                                                        args=[
                                                                                                                                                                            Name(id='operator', ctx=Load()),
                                                                                                                                                                            Name(id='operator', ctx=Load()),
                                                                                                                                                                        ],
                                                                                                                                                                        keywords=[],
                                                                                                                                                                    ),
                                                                                                                                                                    type_comment=None,
                                                                                                                                                                ),
                                                                                                                                                                If(
                                                                                                                                                                    test=Name(id='need_wildcard', ctx=Load()),
                                                                                                                                                                    body=[
                                                                                                                                                                        Assign(
                                                                                                                                                                            targets=[Name(id='right', ctx=Store())],
                                                                                                                                                                            value=BinOp(
                                                                                                                                                                                left=Constant(value='%%%s%%', kind=None),
                                                                                                                                                                                op=Mod(),
                                                                                                                                                                                right=Name(id='right', ctx=Load()),
                                                                                                                                                                            ),
                                                                                                                                                                            type_comment=None,
                                                                                                                                                                        ),
                                                                                                                                                                    ],
                                                                                                                                                                    orelse=[],
                                                                                                                                                                ),
                                                                                                                                                                If(
                                                                                                                                                                    test=Compare(
                                                                                                                                                                        left=Name(id='sql_operator', ctx=Load()),
                                                                                                                                                                        ops=[In()],
                                                                                                                                                                        comparators=[
                                                                                                                                                                            Tuple(
                                                                                                                                                                                elts=[
                                                                                                                                                                                    Constant(value='in', kind=None),
                                                                                                                                                                                    Constant(value='not in', kind=None),
                                                                                                                                                                                ],
                                                                                                                                                                                ctx=Load(),
                                                                                                                                                                            ),
                                                                                                                                                                        ],
                                                                                                                                                                    ),
                                                                                                                                                                    body=[
                                                                                                                                                                        Assign(
                                                                                                                                                                            targets=[Name(id='right', ctx=Store())],
                                                                                                                                                                            value=Call(
                                                                                                                                                                                func=Name(id='tuple', ctx=Load()),
                                                                                                                                                                                args=[Name(id='right', ctx=Load())],
                                                                                                                                                                                keywords=[],
                                                                                                                                                                            ),
                                                                                                                                                                            type_comment=None,
                                                                                                                                                                        ),
                                                                                                                                                                    ],
                                                                                                                                                                    orelse=[],
                                                                                                                                                                ),
                                                                                                                                                                Assign(
                                                                                                                                                                    targets=[Name(id='unaccent', ctx=Store())],
                                                                                                                                                                    value=IfExp(
                                                                                                                                                                        test=Call(
                                                                                                                                                                            func=Attribute(
                                                                                                                                                                                value=Name(id='sql_operator', ctx=Load()),
                                                                                                                                                                                attr='endswith',
                                                                                                                                                                                ctx=Load(),
                                                                                                                                                                            ),
                                                                                                                                                                            args=[Constant(value='like', kind=None)],
                                                                                                                                                                            keywords=[],
                                                                                                                                                                        ),
                                                                                                                                                                        body=Attribute(
                                                                                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                                                                                            attr='_unaccent',
                                                                                                                                                                            ctx=Load(),
                                                                                                                                                                        ),
                                                                                                                                                                        orelse=Lambda(
                                                                                                                                                                            args=arguments(
                                                                                                                                                                                posonlyargs=[],
                                                                                                                                                                                args=[arg(arg='x', annotation=None, type_comment=None)],
                                                                                                                                                                                vararg=None,
                                                                                                                                                                                kwonlyargs=[],
                                                                                                                                                                                kw_defaults=[],
                                                                                                                                                                                kwarg=None,
                                                                                                                                                                                defaults=[],
                                                                                                                                                                            ),
                                                                                                                                                                            body=Name(id='x', ctx=Load()),
                                                                                                                                                                        ),
                                                                                                                                                                    ),
                                                                                                                                                                    type_comment=None,
                                                                                                                                                                ),
                                                                                                                                                                Assign(
                                                                                                                                                                    targets=[Name(id='left', ctx=Store())],
                                                                                                                                                                    value=Call(
                                                                                                                                                                        func=Name(id='unaccent', ctx=Load()),
                                                                                                                                                                        args=[
                                                                                                                                                                            Call(
                                                                                                                                                                                func=Attribute(
                                                                                                                                                                                    value=Name(id='model', ctx=Load()),
                                                                                                                                                                                    attr='_generate_translated_field',
                                                                                                                                                                                    ctx=Load(),
                                                                                                                                                                                ),
                                                                                                                                                                                args=[
                                                                                                                                                                                    Name(id='alias', ctx=Load()),
                                                                                                                                                                                    Name(id='left', ctx=Load()),
                                                                                                                                                                                    Attribute(
                                                                                                                                                                                        value=Name(id='self', ctx=Load()),
                                                                                                                                                                                        attr='query',
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
                                                                                                                                                                    targets=[Name(id='instr', ctx=Store())],
                                                                                                                                                                    value=Call(
                                                                                                                                                                        func=Name(id='unaccent', ctx=Load()),
                                                                                                                                                                        args=[Constant(value='%s', kind=None)],
                                                                                                                                                                        keywords=[],
                                                                                                                                                                    ),
                                                                                                                                                                    type_comment=None,
                                                                                                                                                                ),
                                                                                                                                                                Expr(
                                                                                                                                                                    value=Call(
                                                                                                                                                                        func=Name(id='push_result', ctx=Load()),
                                                                                                                                                                        args=[
                                                                                                                                                                            JoinedStr(
                                                                                                                                                                                values=[
                                                                                                                                                                                    FormattedValue(
                                                                                                                                                                                        value=Name(id='left', ctx=Load()),
                                                                                                                                                                                        conversion=-1,
                                                                                                                                                                                        format_spec=None,
                                                                                                                                                                                    ),
                                                                                                                                                                                    Constant(value=' ', kind=None),
                                                                                                                                                                                    FormattedValue(
                                                                                                                                                                                        value=Name(id='sql_operator', ctx=Load()),
                                                                                                                                                                                        conversion=-1,
                                                                                                                                                                                        format_spec=None,
                                                                                                                                                                                    ),
                                                                                                                                                                                    Constant(value=' ', kind=None),
                                                                                                                                                                                    FormattedValue(
                                                                                                                                                                                        value=Name(id='instr', ctx=Load()),
                                                                                                                                                                                        conversion=-1,
                                                                                                                                                                                        format_spec=None,
                                                                                                                                                                                    ),
                                                                                                                                                                                ],
                                                                                                                                                                            ),
                                                                                                                                                                            List(
                                                                                                                                                                                elts=[Name(id='right', ctx=Load())],
                                                                                                                                                                                ctx=Load(),
                                                                                                                                                                            ),
                                                                                                                                                                        ],
                                                                                                                                                                        keywords=[],
                                                                                                                                                                    ),
                                                                                                                                                                ),
                                                                                                                                                            ],
                                                                                                                                                            orelse=[
                                                                                                                                                                Assign(
                                                                                                                                                                    targets=[
                                                                                                                                                                        Tuple(
                                                                                                                                                                            elts=[
                                                                                                                                                                                Name(id='expr', ctx=Store()),
                                                                                                                                                                                Name(id='params', ctx=Store()),
                                                                                                                                                                            ],
                                                                                                                                                                            ctx=Store(),
                                                                                                                                                                        ),
                                                                                                                                                                    ],
                                                                                                                                                                    value=Call(
                                                                                                                                                                        func=Attribute(
                                                                                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                                                                                            attr='__leaf_to_sql',
                                                                                                                                                                            ctx=Load(),
                                                                                                                                                                        ),
                                                                                                                                                                        args=[
                                                                                                                                                                            Name(id='leaf', ctx=Load()),
                                                                                                                                                                            Name(id='model', ctx=Load()),
                                                                                                                                                                            Name(id='alias', ctx=Load()),
                                                                                                                                                                        ],
                                                                                                                                                                        keywords=[],
                                                                                                                                                                    ),
                                                                                                                                                                    type_comment=None,
                                                                                                                                                                ),
                                                                                                                                                                Expr(
                                                                                                                                                                    value=Call(
                                                                                                                                                                        func=Name(id='push_result', ctx=Load()),
                                                                                                                                                                        args=[
                                                                                                                                                                            Name(id='expr', ctx=Load()),
                                                                                                                                                                            Name(id='params', ctx=Load()),
                                                                                                                                                                        ],
                                                                                                                                                                        keywords=[],
                                                                                                                                                                    ),
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
                            orelse=[],
                        ),
                        Assign(
                            targets=[
                                List(
                                    elts=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='result',
                                            ctx=Store(),
                                        ),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='result_stack', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='where_clause', ctx=Store()),
                                        Name(id='where_params', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='result',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='query',
                                        ctx=Load(),
                                    ),
                                    attr='add_where',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='where_clause', ctx=Load()),
                                    Name(id='where_params', ctx=Load()),
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
                    name='__leaf_to_sql',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='leaf', annotation=None, type_comment=None),
                            arg(arg='model', annotation=None, type_comment=None),
                            arg(arg='alias', annotation=None, type_comment=None),
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
                                        Name(id='left', ctx=Store()),
                                        Name(id='operator', ctx=Store()),
                                        Name(id='right', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='leaf', ctx=Load()),
                            type_comment=None,
                        ),
                        Assert(
                            test=Compare(
                                left=Name(id='operator', ctx=Load()),
                                ops=[In()],
                                comparators=[
                                    BinOp(
                                        left=Name(id='TERM_OPERATORS', ctx=Load()),
                                        op=Add(),
                                        right=Tuple(
                                            elts=[
                                                Constant(value='inselect', kind=None),
                                                Constant(value='not inselect', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            msg=BinOp(
                                left=Constant(value='Invalid operator %r in domain term %r', kind=None),
                                op=Mod(),
                                right=Tuple(
                                    elts=[
                                        Name(id='operator', ctx=Load()),
                                        Name(id='leaf', ctx=Load()),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                        ),
                        Assert(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Compare(
                                        left=Name(id='leaf', ctx=Load()),
                                        ops=[In()],
                                        comparators=[
                                            Tuple(
                                                elts=[
                                                    Name(id='TRUE_LEAF', ctx=Load()),
                                                    Name(id='FALSE_LEAF', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Compare(
                                        left=Name(id='left', ctx=Load()),
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
                            msg=BinOp(
                                left=Constant(value='Invalid field %r in domain term %r', kind=None),
                                op=Mod(),
                                right=Tuple(
                                    elts=[
                                        Name(id='left', ctx=Load()),
                                        Name(id='leaf', ctx=Load()),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                        ),
                        Assert(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Name(id='isinstance', ctx=Load()),
                                    args=[
                                        Name(id='right', ctx=Load()),
                                        Name(id='BaseModel', ctx=Load()),
                                    ],
                                    keywords=[],
                                ),
                            ),
                            msg=BinOp(
                                left=Constant(value='Invalid value %r in domain term %r', kind=None),
                                op=Mod(),
                                right=Tuple(
                                    elts=[
                                        Name(id='right', ctx=Load()),
                                        Name(id='leaf', ctx=Load()),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                        ),
                        Assign(
                            targets=[Name(id='table_alias', ctx=Store())],
                            value=BinOp(
                                left=Constant(value='"%s"', kind=None),
                                op=Mod(),
                                right=Name(id='alias', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='leaf', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Name(id='TRUE_LEAF', ctx=Load())],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='query', ctx=Store())],
                                    value=Constant(value='TRUE', kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='params', ctx=Store())],
                                    value=List(elts=[], ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Name(id='leaf', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Name(id='FALSE_LEAF', ctx=Load())],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='query', ctx=Store())],
                                            value=Constant(value='FALSE', kind=None),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='params', ctx=Store())],
                                            value=List(elts=[], ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Name(id='operator', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='inselect', kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='query', ctx=Store())],
                                                    value=BinOp(
                                                        left=Constant(value='(%s."%s" in (%s))', kind=None),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            elts=[
                                                                Name(id='table_alias', ctx=Load()),
                                                                Name(id='left', ctx=Load()),
                                                                Subscript(
                                                                    value=Name(id='right', ctx=Load()),
                                                                    slice=Constant(value=0, kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='params', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='list', ctx=Load()),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='right', ctx=Load()),
                                                                slice=Constant(value=1, kind=None),
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
                                                    test=Compare(
                                                        left=Name(id='operator', ctx=Load()),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='not inselect', kind=None)],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='query', ctx=Store())],
                                                            value=BinOp(
                                                                left=Constant(value='(%s."%s" not in (%s))', kind=None),
                                                                op=Mod(),
                                                                right=Tuple(
                                                                    elts=[
                                                                        Name(id='table_alias', ctx=Load()),
                                                                        Name(id='left', ctx=Load()),
                                                                        Subscript(
                                                                            value=Name(id='right', ctx=Load()),
                                                                            slice=Constant(value=0, kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='params', ctx=Store())],
                                                            value=Call(
                                                                func=Name(id='list', ctx=Load()),
                                                                args=[
                                                                    Subscript(
                                                                        value=Name(id='right', ctx=Load()),
                                                                        slice=Constant(value=1, kind=None),
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
                                                            test=Compare(
                                                                left=Name(id='operator', ctx=Load()),
                                                                ops=[In()],
                                                                comparators=[
                                                                    List(
                                                                        elts=[
                                                                            Constant(value='in', kind=None),
                                                                            Constant(value='not in', kind=None),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                            body=[
                                                                If(
                                                                    test=Call(
                                                                        func=Name(id='isinstance', ctx=Load()),
                                                                        args=[
                                                                            Name(id='right', ctx=Load()),
                                                                            Name(id='bool', ctx=Load()),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                    body=[
                                                                        Expr(
                                                                            value=Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='_logger', ctx=Load()),
                                                                                    attr='warning',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[
                                                                                    BinOp(
                                                                                        left=Constant(value="The domain term '%s' should use the '=' or '!=' operator.", kind=None),
                                                                                        op=Mod(),
                                                                                        right=Tuple(
                                                                                            elts=[Name(id='leaf', ctx=Load())],
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                    ),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                        ),
                                                                        If(
                                                                            test=BoolOp(
                                                                                op=Or(),
                                                                                values=[
                                                                                    BoolOp(
                                                                                        op=And(),
                                                                                        values=[
                                                                                            Compare(
                                                                                                left=Name(id='operator', ctx=Load()),
                                                                                                ops=[Eq()],
                                                                                                comparators=[Constant(value='in', kind=None)],
                                                                                            ),
                                                                                            Name(id='right', ctx=Load()),
                                                                                        ],
                                                                                    ),
                                                                                    BoolOp(
                                                                                        op=And(),
                                                                                        values=[
                                                                                            Compare(
                                                                                                left=Name(id='operator', ctx=Load()),
                                                                                                ops=[Eq()],
                                                                                                comparators=[Constant(value='not in', kind=None)],
                                                                                            ),
                                                                                            UnaryOp(
                                                                                                op=Not(),
                                                                                                operand=Name(id='right', ctx=Load()),
                                                                                            ),
                                                                                        ],
                                                                                    ),
                                                                                ],
                                                                            ),
                                                                            body=[
                                                                                Assign(
                                                                                    targets=[Name(id='query', ctx=Store())],
                                                                                    value=BinOp(
                                                                                        left=Constant(value='(%s."%s" IS NOT NULL)', kind=None),
                                                                                        op=Mod(),
                                                                                        right=Tuple(
                                                                                            elts=[
                                                                                                Name(id='table_alias', ctx=Load()),
                                                                                                Name(id='left', ctx=Load()),
                                                                                            ],
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                    ),
                                                                                    type_comment=None,
                                                                                ),
                                                                            ],
                                                                            orelse=[
                                                                                Assign(
                                                                                    targets=[Name(id='query', ctx=Store())],
                                                                                    value=BinOp(
                                                                                        left=Constant(value='(%s."%s" IS NULL)', kind=None),
                                                                                        op=Mod(),
                                                                                        right=Tuple(
                                                                                            elts=[
                                                                                                Name(id='table_alias', ctx=Load()),
                                                                                                Name(id='left', ctx=Load()),
                                                                                            ],
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                    ),
                                                                                    type_comment=None,
                                                                                ),
                                                                            ],
                                                                        ),
                                                                        Assign(
                                                                            targets=[Name(id='params', ctx=Store())],
                                                                            value=List(elts=[], ctx=Load()),
                                                                            type_comment=None,
                                                                        ),
                                                                    ],
                                                                    orelse=[
                                                                        If(
                                                                            test=Call(
                                                                                func=Name(id='isinstance', ctx=Load()),
                                                                                args=[
                                                                                    Name(id='right', ctx=Load()),
                                                                                    Name(id='Query', ctx=Load()),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                            body=[
                                                                                Assign(
                                                                                    targets=[
                                                                                        Tuple(
                                                                                            elts=[
                                                                                                Name(id='subquery', ctx=Store()),
                                                                                                Name(id='subparams', ctx=Store()),
                                                                                            ],
                                                                                            ctx=Store(),
                                                                                        ),
                                                                                    ],
                                                                                    value=Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='right', ctx=Load()),
                                                                                            attr='subselect',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[],
                                                                                        keywords=[],
                                                                                    ),
                                                                                    type_comment=None,
                                                                                ),
                                                                                Assign(
                                                                                    targets=[Name(id='query', ctx=Store())],
                                                                                    value=BinOp(
                                                                                        left=Constant(value='(%s."%s" %s (%s))', kind=None),
                                                                                        op=Mod(),
                                                                                        right=Tuple(
                                                                                            elts=[
                                                                                                Name(id='table_alias', ctx=Load()),
                                                                                                Name(id='left', ctx=Load()),
                                                                                                Name(id='operator', ctx=Load()),
                                                                                                Name(id='subquery', ctx=Load()),
                                                                                            ],
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                    ),
                                                                                    type_comment=None,
                                                                                ),
                                                                                Assign(
                                                                                    targets=[Name(id='params', ctx=Store())],
                                                                                    value=Name(id='subparams', ctx=Load()),
                                                                                    type_comment=None,
                                                                                ),
                                                                            ],
                                                                            orelse=[
                                                                                If(
                                                                                    test=Call(
                                                                                        func=Name(id='isinstance', ctx=Load()),
                                                                                        args=[
                                                                                            Name(id='right', ctx=Load()),
                                                                                            Tuple(
                                                                                                elts=[
                                                                                                    Name(id='list', ctx=Load()),
                                                                                                    Name(id='tuple', ctx=Load()),
                                                                                                ],
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                        ],
                                                                                        keywords=[],
                                                                                    ),
                                                                                    body=[
                                                                                        If(
                                                                                            test=Compare(
                                                                                                left=Attribute(
                                                                                                    value=Subscript(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='model', ctx=Load()),
                                                                                                            attr='_fields',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        slice=Name(id='left', ctx=Load()),
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    attr='type',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                ops=[Eq()],
                                                                                                comparators=[Constant(value='boolean', kind=None)],
                                                                                            ),
                                                                                            body=[
                                                                                                Assign(
                                                                                                    targets=[Name(id='params', ctx=Store())],
                                                                                                    value=ListComp(
                                                                                                        elt=Name(id='it', ctx=Load()),
                                                                                                        generators=[
                                                                                                            comprehension(
                                                                                                                target=Name(id='it', ctx=Store()),
                                                                                                                iter=Tuple(
                                                                                                                    elts=[
                                                                                                                        Constant(value=True, kind=None),
                                                                                                                        Constant(value=False, kind=None),
                                                                                                                    ],
                                                                                                                    ctx=Load(),
                                                                                                                ),
                                                                                                                ifs=[
                                                                                                                    Compare(
                                                                                                                        left=Name(id='it', ctx=Load()),
                                                                                                                        ops=[In()],
                                                                                                                        comparators=[Name(id='right', ctx=Load())],
                                                                                                                    ),
                                                                                                                ],
                                                                                                                is_async=0,
                                                                                                            ),
                                                                                                        ],
                                                                                                    ),
                                                                                                    type_comment=None,
                                                                                                ),
                                                                                                Assign(
                                                                                                    targets=[Name(id='check_null', ctx=Store())],
                                                                                                    value=Compare(
                                                                                                        left=Constant(value=False, kind=None),
                                                                                                        ops=[In()],
                                                                                                        comparators=[Name(id='right', ctx=Load())],
                                                                                                    ),
                                                                                                    type_comment=None,
                                                                                                ),
                                                                                            ],
                                                                                            orelse=[
                                                                                                Assign(
                                                                                                    targets=[Name(id='params', ctx=Store())],
                                                                                                    value=ListComp(
                                                                                                        elt=Name(id='it', ctx=Load()),
                                                                                                        generators=[
                                                                                                            comprehension(
                                                                                                                target=Name(id='it', ctx=Store()),
                                                                                                                iter=Name(id='right', ctx=Load()),
                                                                                                                ifs=[
                                                                                                                    Compare(
                                                                                                                        left=Name(id='it', ctx=Load()),
                                                                                                                        ops=[NotEq()],
                                                                                                                        comparators=[Constant(value=False, kind=None)],
                                                                                                                    ),
                                                                                                                ],
                                                                                                                is_async=0,
                                                                                                            ),
                                                                                                        ],
                                                                                                    ),
                                                                                                    type_comment=None,
                                                                                                ),
                                                                                                Assign(
                                                                                                    targets=[Name(id='check_null', ctx=Store())],
                                                                                                    value=Compare(
                                                                                                        left=Call(
                                                                                                            func=Name(id='len', ctx=Load()),
                                                                                                            args=[Name(id='params', ctx=Load())],
                                                                                                            keywords=[],
                                                                                                        ),
                                                                                                        ops=[Lt()],
                                                                                                        comparators=[
                                                                                                            Call(
                                                                                                                func=Name(id='len', ctx=Load()),
                                                                                                                args=[Name(id='right', ctx=Load())],
                                                                                                                keywords=[],
                                                                                                            ),
                                                                                                        ],
                                                                                                    ),
                                                                                                    type_comment=None,
                                                                                                ),
                                                                                            ],
                                                                                        ),
                                                                                        If(
                                                                                            test=Name(id='params', ctx=Load()),
                                                                                            body=[
                                                                                                If(
                                                                                                    test=Compare(
                                                                                                        left=Name(id='left', ctx=Load()),
                                                                                                        ops=[Eq()],
                                                                                                        comparators=[Constant(value='id', kind=None)],
                                                                                                    ),
                                                                                                    body=[
                                                                                                        Assign(
                                                                                                            targets=[Name(id='instr', ctx=Store())],
                                                                                                            value=Call(
                                                                                                                func=Attribute(
                                                                                                                    value=Constant(value=',', kind=None),
                                                                                                                    attr='join',
                                                                                                                    ctx=Load(),
                                                                                                                ),
                                                                                                                args=[
                                                                                                                    BinOp(
                                                                                                                        left=List(
                                                                                                                            elts=[Constant(value='%s', kind=None)],
                                                                                                                            ctx=Load(),
                                                                                                                        ),
                                                                                                                        op=Mult(),
                                                                                                                        right=Call(
                                                                                                                            func=Name(id='len', ctx=Load()),
                                                                                                                            args=[Name(id='params', ctx=Load())],
                                                                                                                            keywords=[],
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
                                                                                                            targets=[Name(id='field', ctx=Store())],
                                                                                                            value=Subscript(
                                                                                                                value=Attribute(
                                                                                                                    value=Name(id='model', ctx=Load()),
                                                                                                                    attr='_fields',
                                                                                                                    ctx=Load(),
                                                                                                                ),
                                                                                                                slice=Name(id='left', ctx=Load()),
                                                                                                                ctx=Load(),
                                                                                                            ),
                                                                                                            type_comment=None,
                                                                                                        ),
                                                                                                        Assign(
                                                                                                            targets=[Name(id='instr', ctx=Store())],
                                                                                                            value=Call(
                                                                                                                func=Attribute(
                                                                                                                    value=Constant(value=',', kind=None),
                                                                                                                    attr='join',
                                                                                                                    ctx=Load(),
                                                                                                                ),
                                                                                                                args=[
                                                                                                                    BinOp(
                                                                                                                        left=List(
                                                                                                                            elts=[
                                                                                                                                Attribute(
                                                                                                                                    value=Name(id='field', ctx=Load()),
                                                                                                                                    attr='column_format',
                                                                                                                                    ctx=Load(),
                                                                                                                                ),
                                                                                                                            ],
                                                                                                                            ctx=Load(),
                                                                                                                        ),
                                                                                                                        op=Mult(),
                                                                                                                        right=Call(
                                                                                                                            func=Name(id='len', ctx=Load()),
                                                                                                                            args=[Name(id='params', ctx=Load())],
                                                                                                                            keywords=[],
                                                                                                                        ),
                                                                                                                    ),
                                                                                                                ],
                                                                                                                keywords=[],
                                                                                                            ),
                                                                                                            type_comment=None,
                                                                                                        ),
                                                                                                        Assign(
                                                                                                            targets=[Name(id='params', ctx=Store())],
                                                                                                            value=ListComp(
                                                                                                                elt=Call(
                                                                                                                    func=Attribute(
                                                                                                                        value=Name(id='field', ctx=Load()),
                                                                                                                        attr='convert_to_column',
                                                                                                                        ctx=Load(),
                                                                                                                    ),
                                                                                                                    args=[
                                                                                                                        Name(id='p', ctx=Load()),
                                                                                                                        Name(id='model', ctx=Load()),
                                                                                                                    ],
                                                                                                                    keywords=[
                                                                                                                        keyword(
                                                                                                                            arg='validate',
                                                                                                                            value=Constant(value=False, kind=None),
                                                                                                                        ),
                                                                                                                    ],
                                                                                                                ),
                                                                                                                generators=[
                                                                                                                    comprehension(
                                                                                                                        target=Name(id='p', ctx=Store()),
                                                                                                                        iter=Name(id='params', ctx=Load()),
                                                                                                                        ifs=[],
                                                                                                                        is_async=0,
                                                                                                                    ),
                                                                                                                ],
                                                                                                            ),
                                                                                                            type_comment=None,
                                                                                                        ),
                                                                                                    ],
                                                                                                ),
                                                                                                Assign(
                                                                                                    targets=[Name(id='query', ctx=Store())],
                                                                                                    value=BinOp(
                                                                                                        left=Constant(value='(%s."%s" %s (%s))', kind=None),
                                                                                                        op=Mod(),
                                                                                                        right=Tuple(
                                                                                                            elts=[
                                                                                                                Name(id='table_alias', ctx=Load()),
                                                                                                                Name(id='left', ctx=Load()),
                                                                                                                Name(id='operator', ctx=Load()),
                                                                                                                Name(id='instr', ctx=Load()),
                                                                                                            ],
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                    ),
                                                                                                    type_comment=None,
                                                                                                ),
                                                                                            ],
                                                                                            orelse=[
                                                                                                Assign(
                                                                                                    targets=[Name(id='query', ctx=Store())],
                                                                                                    value=IfExp(
                                                                                                        test=Compare(
                                                                                                            left=Name(id='operator', ctx=Load()),
                                                                                                            ops=[Eq()],
                                                                                                            comparators=[Constant(value='in', kind=None)],
                                                                                                        ),
                                                                                                        body=Constant(value='FALSE', kind=None),
                                                                                                        orelse=Constant(value='TRUE', kind=None),
                                                                                                    ),
                                                                                                    type_comment=None,
                                                                                                ),
                                                                                            ],
                                                                                        ),
                                                                                        If(
                                                                                            test=BoolOp(
                                                                                                op=Or(),
                                                                                                values=[
                                                                                                    BoolOp(
                                                                                                        op=And(),
                                                                                                        values=[
                                                                                                            Compare(
                                                                                                                left=Name(id='operator', ctx=Load()),
                                                                                                                ops=[Eq()],
                                                                                                                comparators=[Constant(value='in', kind=None)],
                                                                                                            ),
                                                                                                            Name(id='check_null', ctx=Load()),
                                                                                                        ],
                                                                                                    ),
                                                                                                    BoolOp(
                                                                                                        op=And(),
                                                                                                        values=[
                                                                                                            Compare(
                                                                                                                left=Name(id='operator', ctx=Load()),
                                                                                                                ops=[Eq()],
                                                                                                                comparators=[Constant(value='not in', kind=None)],
                                                                                                            ),
                                                                                                            UnaryOp(
                                                                                                                op=Not(),
                                                                                                                operand=Name(id='check_null', ctx=Load()),
                                                                                                            ),
                                                                                                        ],
                                                                                                    ),
                                                                                                ],
                                                                                            ),
                                                                                            body=[
                                                                                                Assign(
                                                                                                    targets=[Name(id='query', ctx=Store())],
                                                                                                    value=BinOp(
                                                                                                        left=Constant(value='(%s OR %s."%s" IS NULL)', kind=None),
                                                                                                        op=Mod(),
                                                                                                        right=Tuple(
                                                                                                            elts=[
                                                                                                                Name(id='query', ctx=Load()),
                                                                                                                Name(id='table_alias', ctx=Load()),
                                                                                                                Name(id='left', ctx=Load()),
                                                                                                            ],
                                                                                                            ctx=Load(),
                                                                                                        ),
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
                                                                                                                left=Name(id='operator', ctx=Load()),
                                                                                                                ops=[Eq()],
                                                                                                                comparators=[Constant(value='not in', kind=None)],
                                                                                                            ),
                                                                                                            Name(id='check_null', ctx=Load()),
                                                                                                        ],
                                                                                                    ),
                                                                                                    body=[
                                                                                                        Assign(
                                                                                                            targets=[Name(id='query', ctx=Store())],
                                                                                                            value=BinOp(
                                                                                                                left=Constant(value='(%s AND %s."%s" IS NOT NULL)', kind=None),
                                                                                                                op=Mod(),
                                                                                                                right=Tuple(
                                                                                                                    elts=[
                                                                                                                        Name(id='query', ctx=Load()),
                                                                                                                        Name(id='table_alias', ctx=Load()),
                                                                                                                        Name(id='left', ctx=Load()),
                                                                                                                    ],
                                                                                                                    ctx=Load(),
                                                                                                                ),
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
                                                                                        Raise(
                                                                                            exc=Call(
                                                                                                func=Name(id='ValueError', ctx=Load()),
                                                                                                args=[
                                                                                                    BinOp(
                                                                                                        left=Constant(value='Invalid domain term %r', kind=None),
                                                                                                        op=Mod(),
                                                                                                        right=Tuple(
                                                                                                            elts=[Name(id='leaf', ctx=Load())],
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
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                            orelse=[
                                                                If(
                                                                    test=BoolOp(
                                                                        op=And(),
                                                                        values=[
                                                                            Compare(
                                                                                left=Name(id='left', ctx=Load()),
                                                                                ops=[In()],
                                                                                comparators=[Name(id='model', ctx=Load())],
                                                                            ),
                                                                            Compare(
                                                                                left=Attribute(
                                                                                    value=Subscript(
                                                                                        value=Attribute(
                                                                                            value=Name(id='model', ctx=Load()),
                                                                                            attr='_fields',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        slice=Name(id='left', ctx=Load()),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='type',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                ops=[Eq()],
                                                                                comparators=[Constant(value='boolean', kind=None)],
                                                                            ),
                                                                            BoolOp(
                                                                                op=Or(),
                                                                                values=[
                                                                                    BoolOp(
                                                                                        op=And(),
                                                                                        values=[
                                                                                            Compare(
                                                                                                left=Name(id='operator', ctx=Load()),
                                                                                                ops=[Eq()],
                                                                                                comparators=[Constant(value='=', kind=None)],
                                                                                            ),
                                                                                            Compare(
                                                                                                left=Name(id='right', ctx=Load()),
                                                                                                ops=[Is()],
                                                                                                comparators=[Constant(value=False, kind=None)],
                                                                                            ),
                                                                                        ],
                                                                                    ),
                                                                                    BoolOp(
                                                                                        op=And(),
                                                                                        values=[
                                                                                            Compare(
                                                                                                left=Name(id='operator', ctx=Load()),
                                                                                                ops=[Eq()],
                                                                                                comparators=[Constant(value='!=', kind=None)],
                                                                                            ),
                                                                                            Compare(
                                                                                                left=Name(id='right', ctx=Load()),
                                                                                                ops=[Is()],
                                                                                                comparators=[Constant(value=True, kind=None)],
                                                                                            ),
                                                                                        ],
                                                                                    ),
                                                                                ],
                                                                            ),
                                                                        ],
                                                                    ),
                                                                    body=[
                                                                        Assign(
                                                                            targets=[Name(id='query', ctx=Store())],
                                                                            value=BinOp(
                                                                                left=Constant(value='(%s."%s" IS NULL or %s."%s" = false )', kind=None),
                                                                                op=Mod(),
                                                                                right=Tuple(
                                                                                    elts=[
                                                                                        Name(id='table_alias', ctx=Load()),
                                                                                        Name(id='left', ctx=Load()),
                                                                                        Name(id='table_alias', ctx=Load()),
                                                                                        Name(id='left', ctx=Load()),
                                                                                    ],
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ),
                                                                            type_comment=None,
                                                                        ),
                                                                        Assign(
                                                                            targets=[Name(id='params', ctx=Store())],
                                                                            value=List(elts=[], ctx=Load()),
                                                                            type_comment=None,
                                                                        ),
                                                                    ],
                                                                    orelse=[
                                                                        If(
                                                                            test=BoolOp(
                                                                                op=And(),
                                                                                values=[
                                                                                    BoolOp(
                                                                                        op=Or(),
                                                                                        values=[
                                                                                            Compare(
                                                                                                left=Name(id='right', ctx=Load()),
                                                                                                ops=[Is()],
                                                                                                comparators=[Constant(value=False, kind=None)],
                                                                                            ),
                                                                                            Compare(
                                                                                                left=Name(id='right', ctx=Load()),
                                                                                                ops=[Is()],
                                                                                                comparators=[Constant(value=None, kind=None)],
                                                                                            ),
                                                                                        ],
                                                                                    ),
                                                                                    Compare(
                                                                                        left=Name(id='operator', ctx=Load()),
                                                                                        ops=[Eq()],
                                                                                        comparators=[Constant(value='=', kind=None)],
                                                                                    ),
                                                                                ],
                                                                            ),
                                                                            body=[
                                                                                Assign(
                                                                                    targets=[Name(id='query', ctx=Store())],
                                                                                    value=BinOp(
                                                                                        left=Constant(value='%s."%s" IS NULL ', kind=None),
                                                                                        op=Mod(),
                                                                                        right=Tuple(
                                                                                            elts=[
                                                                                                Name(id='table_alias', ctx=Load()),
                                                                                                Name(id='left', ctx=Load()),
                                                                                            ],
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                    ),
                                                                                    type_comment=None,
                                                                                ),
                                                                                Assign(
                                                                                    targets=[Name(id='params', ctx=Store())],
                                                                                    value=List(elts=[], ctx=Load()),
                                                                                    type_comment=None,
                                                                                ),
                                                                            ],
                                                                            orelse=[
                                                                                If(
                                                                                    test=BoolOp(
                                                                                        op=And(),
                                                                                        values=[
                                                                                            Compare(
                                                                                                left=Name(id='left', ctx=Load()),
                                                                                                ops=[In()],
                                                                                                comparators=[Name(id='model', ctx=Load())],
                                                                                            ),
                                                                                            Compare(
                                                                                                left=Attribute(
                                                                                                    value=Subscript(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='model', ctx=Load()),
                                                                                                            attr='_fields',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        slice=Name(id='left', ctx=Load()),
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    attr='type',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                ops=[Eq()],
                                                                                                comparators=[Constant(value='boolean', kind=None)],
                                                                                            ),
                                                                                            BoolOp(
                                                                                                op=Or(),
                                                                                                values=[
                                                                                                    BoolOp(
                                                                                                        op=And(),
                                                                                                        values=[
                                                                                                            Compare(
                                                                                                                left=Name(id='operator', ctx=Load()),
                                                                                                                ops=[Eq()],
                                                                                                                comparators=[Constant(value='!=', kind=None)],
                                                                                                            ),
                                                                                                            Compare(
                                                                                                                left=Name(id='right', ctx=Load()),
                                                                                                                ops=[Is()],
                                                                                                                comparators=[Constant(value=False, kind=None)],
                                                                                                            ),
                                                                                                        ],
                                                                                                    ),
                                                                                                    BoolOp(
                                                                                                        op=And(),
                                                                                                        values=[
                                                                                                            Compare(
                                                                                                                left=Name(id='operator', ctx=Load()),
                                                                                                                ops=[Eq()],
                                                                                                                comparators=[Constant(value='==', kind=None)],
                                                                                                            ),
                                                                                                            Compare(
                                                                                                                left=Name(id='right', ctx=Load()),
                                                                                                                ops=[Is()],
                                                                                                                comparators=[Constant(value=True, kind=None)],
                                                                                                            ),
                                                                                                        ],
                                                                                                    ),
                                                                                                ],
                                                                                            ),
                                                                                        ],
                                                                                    ),
                                                                                    body=[
                                                                                        Assign(
                                                                                            targets=[Name(id='query', ctx=Store())],
                                                                                            value=BinOp(
                                                                                                left=Constant(value='(%s."%s" IS NOT NULL and %s."%s" != false)', kind=None),
                                                                                                op=Mod(),
                                                                                                right=Tuple(
                                                                                                    elts=[
                                                                                                        Name(id='table_alias', ctx=Load()),
                                                                                                        Name(id='left', ctx=Load()),
                                                                                                        Name(id='table_alias', ctx=Load()),
                                                                                                        Name(id='left', ctx=Load()),
                                                                                                    ],
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                            ),
                                                                                            type_comment=None,
                                                                                        ),
                                                                                        Assign(
                                                                                            targets=[Name(id='params', ctx=Store())],
                                                                                            value=List(elts=[], ctx=Load()),
                                                                                            type_comment=None,
                                                                                        ),
                                                                                    ],
                                                                                    orelse=[
                                                                                        If(
                                                                                            test=BoolOp(
                                                                                                op=And(),
                                                                                                values=[
                                                                                                    BoolOp(
                                                                                                        op=Or(),
                                                                                                        values=[
                                                                                                            Compare(
                                                                                                                left=Name(id='right', ctx=Load()),
                                                                                                                ops=[Is()],
                                                                                                                comparators=[Constant(value=False, kind=None)],
                                                                                                            ),
                                                                                                            Compare(
                                                                                                                left=Name(id='right', ctx=Load()),
                                                                                                                ops=[Is()],
                                                                                                                comparators=[Constant(value=None, kind=None)],
                                                                                                            ),
                                                                                                        ],
                                                                                                    ),
                                                                                                    Compare(
                                                                                                        left=Name(id='operator', ctx=Load()),
                                                                                                        ops=[Eq()],
                                                                                                        comparators=[Constant(value='!=', kind=None)],
                                                                                                    ),
                                                                                                ],
                                                                                            ),
                                                                                            body=[
                                                                                                Assign(
                                                                                                    targets=[Name(id='query', ctx=Store())],
                                                                                                    value=BinOp(
                                                                                                        left=Constant(value='%s."%s" IS NOT NULL', kind=None),
                                                                                                        op=Mod(),
                                                                                                        right=Tuple(
                                                                                                            elts=[
                                                                                                                Name(id='table_alias', ctx=Load()),
                                                                                                                Name(id='left', ctx=Load()),
                                                                                                            ],
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                    ),
                                                                                                    type_comment=None,
                                                                                                ),
                                                                                                Assign(
                                                                                                    targets=[Name(id='params', ctx=Store())],
                                                                                                    value=List(elts=[], ctx=Load()),
                                                                                                    type_comment=None,
                                                                                                ),
                                                                                            ],
                                                                                            orelse=[
                                                                                                If(
                                                                                                    test=Compare(
                                                                                                        left=Name(id='operator', ctx=Load()),
                                                                                                        ops=[Eq()],
                                                                                                        comparators=[Constant(value='=?', kind=None)],
                                                                                                    ),
                                                                                                    body=[
                                                                                                        If(
                                                                                                            test=BoolOp(
                                                                                                                op=Or(),
                                                                                                                values=[
                                                                                                                    Compare(
                                                                                                                        left=Name(id='right', ctx=Load()),
                                                                                                                        ops=[Is()],
                                                                                                                        comparators=[Constant(value=False, kind=None)],
                                                                                                                    ),
                                                                                                                    Compare(
                                                                                                                        left=Name(id='right', ctx=Load()),
                                                                                                                        ops=[Is()],
                                                                                                                        comparators=[Constant(value=None, kind=None)],
                                                                                                                    ),
                                                                                                                ],
                                                                                                            ),
                                                                                                            body=[
                                                                                                                Assign(
                                                                                                                    targets=[Name(id='query', ctx=Store())],
                                                                                                                    value=Constant(value='TRUE', kind=None),
                                                                                                                    type_comment=None,
                                                                                                                ),
                                                                                                                Assign(
                                                                                                                    targets=[Name(id='params', ctx=Store())],
                                                                                                                    value=List(elts=[], ctx=Load()),
                                                                                                                    type_comment=None,
                                                                                                                ),
                                                                                                            ],
                                                                                                            orelse=[
                                                                                                                Assign(
                                                                                                                    targets=[
                                                                                                                        Tuple(
                                                                                                                            elts=[
                                                                                                                                Name(id='query', ctx=Store()),
                                                                                                                                Name(id='params', ctx=Store()),
                                                                                                                            ],
                                                                                                                            ctx=Store(),
                                                                                                                        ),
                                                                                                                    ],
                                                                                                                    value=Call(
                                                                                                                        func=Attribute(
                                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                                            attr='__leaf_to_sql',
                                                                                                                            ctx=Load(),
                                                                                                                        ),
                                                                                                                        args=[
                                                                                                                            Tuple(
                                                                                                                                elts=[
                                                                                                                                    Name(id='left', ctx=Load()),
                                                                                                                                    Constant(value='=', kind=None),
                                                                                                                                    Name(id='right', ctx=Load()),
                                                                                                                                ],
                                                                                                                                ctx=Load(),
                                                                                                                            ),
                                                                                                                            Name(id='model', ctx=Load()),
                                                                                                                            Name(id='alias', ctx=Load()),
                                                                                                                        ],
                                                                                                                        keywords=[],
                                                                                                                    ),
                                                                                                                    type_comment=None,
                                                                                                                ),
                                                                                                            ],
                                                                                                        ),
                                                                                                    ],
                                                                                                    orelse=[
                                                                                                        Assign(
                                                                                                            targets=[Name(id='need_wildcard', ctx=Store())],
                                                                                                            value=Compare(
                                                                                                                left=Name(id='operator', ctx=Load()),
                                                                                                                ops=[In()],
                                                                                                                comparators=[
                                                                                                                    Tuple(
                                                                                                                        elts=[
                                                                                                                            Constant(value='like', kind=None),
                                                                                                                            Constant(value='ilike', kind=None),
                                                                                                                            Constant(value='not like', kind=None),
                                                                                                                            Constant(value='not ilike', kind=None),
                                                                                                                        ],
                                                                                                                        ctx=Load(),
                                                                                                                    ),
                                                                                                                ],
                                                                                                            ),
                                                                                                            type_comment=None,
                                                                                                        ),
                                                                                                        Assign(
                                                                                                            targets=[Name(id='sql_operator', ctx=Store())],
                                                                                                            value=Call(
                                                                                                                func=Attribute(
                                                                                                                    value=Dict(
                                                                                                                        keys=[
                                                                                                                            Constant(value='=like', kind=None),
                                                                                                                            Constant(value='=ilike', kind=None),
                                                                                                                        ],
                                                                                                                        values=[
                                                                                                                            Constant(value='like', kind=None),
                                                                                                                            Constant(value='ilike', kind=None),
                                                                                                                        ],
                                                                                                                    ),
                                                                                                                    attr='get',
                                                                                                                    ctx=Load(),
                                                                                                                ),
                                                                                                                args=[
                                                                                                                    Name(id='operator', ctx=Load()),
                                                                                                                    Name(id='operator', ctx=Load()),
                                                                                                                ],
                                                                                                                keywords=[],
                                                                                                            ),
                                                                                                            type_comment=None,
                                                                                                        ),
                                                                                                        Assign(
                                                                                                            targets=[Name(id='cast', ctx=Store())],
                                                                                                            value=IfExp(
                                                                                                                test=Call(
                                                                                                                    func=Attribute(
                                                                                                                        value=Name(id='sql_operator', ctx=Load()),
                                                                                                                        attr='endswith',
                                                                                                                        ctx=Load(),
                                                                                                                    ),
                                                                                                                    args=[Constant(value='like', kind=None)],
                                                                                                                    keywords=[],
                                                                                                                ),
                                                                                                                body=Constant(value='::text', kind=None),
                                                                                                                orelse=Constant(value='', kind=None),
                                                                                                            ),
                                                                                                            type_comment=None,
                                                                                                        ),
                                                                                                        If(
                                                                                                            test=Compare(
                                                                                                                left=Name(id='left', ctx=Load()),
                                                                                                                ops=[NotIn()],
                                                                                                                comparators=[Name(id='model', ctx=Load())],
                                                                                                            ),
                                                                                                            body=[
                                                                                                                Raise(
                                                                                                                    exc=Call(
                                                                                                                        func=Name(id='ValueError', ctx=Load()),
                                                                                                                        args=[
                                                                                                                            BinOp(
                                                                                                                                left=Constant(value='Invalid field %r in domain term %r', kind=None),
                                                                                                                                op=Mod(),
                                                                                                                                right=Tuple(
                                                                                                                                    elts=[
                                                                                                                                        Name(id='left', ctx=Load()),
                                                                                                                                        Name(id='leaf', ctx=Load()),
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
                                                                                                        Assign(
                                                                                                            targets=[Name(id='format', ctx=Store())],
                                                                                                            value=IfExp(
                                                                                                                test=Name(id='need_wildcard', ctx=Load()),
                                                                                                                body=Constant(value='%s', kind=None),
                                                                                                                orelse=Attribute(
                                                                                                                    value=Subscript(
                                                                                                                        value=Attribute(
                                                                                                                            value=Name(id='model', ctx=Load()),
                                                                                                                            attr='_fields',
                                                                                                                            ctx=Load(),
                                                                                                                        ),
                                                                                                                        slice=Name(id='left', ctx=Load()),
                                                                                                                        ctx=Load(),
                                                                                                                    ),
                                                                                                                    attr='column_format',
                                                                                                                    ctx=Load(),
                                                                                                                ),
                                                                                                            ),
                                                                                                            type_comment=None,
                                                                                                        ),
                                                                                                        Assign(
                                                                                                            targets=[Name(id='unaccent', ctx=Store())],
                                                                                                            value=IfExp(
                                                                                                                test=Call(
                                                                                                                    func=Attribute(
                                                                                                                        value=Name(id='sql_operator', ctx=Load()),
                                                                                                                        attr='endswith',
                                                                                                                        ctx=Load(),
                                                                                                                    ),
                                                                                                                    args=[Constant(value='like', kind=None)],
                                                                                                                    keywords=[],
                                                                                                                ),
                                                                                                                body=Attribute(
                                                                                                                    value=Name(id='self', ctx=Load()),
                                                                                                                    attr='_unaccent',
                                                                                                                    ctx=Load(),
                                                                                                                ),
                                                                                                                orelse=Lambda(
                                                                                                                    args=arguments(
                                                                                                                        posonlyargs=[],
                                                                                                                        args=[arg(arg='x', annotation=None, type_comment=None)],
                                                                                                                        vararg=None,
                                                                                                                        kwonlyargs=[],
                                                                                                                        kw_defaults=[],
                                                                                                                        kwarg=None,
                                                                                                                        defaults=[],
                                                                                                                    ),
                                                                                                                    body=Name(id='x', ctx=Load()),
                                                                                                                ),
                                                                                                            ),
                                                                                                            type_comment=None,
                                                                                                        ),
                                                                                                        Assign(
                                                                                                            targets=[Name(id='column', ctx=Store())],
                                                                                                            value=BinOp(
                                                                                                                left=Constant(value='%s.%s', kind=None),
                                                                                                                op=Mod(),
                                                                                                                right=Tuple(
                                                                                                                    elts=[
                                                                                                                        Name(id='table_alias', ctx=Load()),
                                                                                                                        Call(
                                                                                                                            func=Name(id='_quote', ctx=Load()),
                                                                                                                            args=[Name(id='left', ctx=Load())],
                                                                                                                            keywords=[],
                                                                                                                        ),
                                                                                                                    ],
                                                                                                                    ctx=Load(),
                                                                                                                ),
                                                                                                            ),
                                                                                                            type_comment=None,
                                                                                                        ),
                                                                                                        Assign(
                                                                                                            targets=[Name(id='query', ctx=Store())],
                                                                                                            value=BinOp(
                                                                                                                left=Constant(value='(%s %s %s)', kind=None),
                                                                                                                op=Mod(),
                                                                                                                right=Tuple(
                                                                                                                    elts=[
                                                                                                                        Call(
                                                                                                                            func=Name(id='unaccent', ctx=Load()),
                                                                                                                            args=[
                                                                                                                                BinOp(
                                                                                                                                    left=Name(id='column', ctx=Load()),
                                                                                                                                    op=Add(),
                                                                                                                                    right=Name(id='cast', ctx=Load()),
                                                                                                                                ),
                                                                                                                            ],
                                                                                                                            keywords=[],
                                                                                                                        ),
                                                                                                                        Name(id='sql_operator', ctx=Load()),
                                                                                                                        Call(
                                                                                                                            func=Name(id='unaccent', ctx=Load()),
                                                                                                                            args=[Name(id='format', ctx=Load())],
                                                                                                                            keywords=[],
                                                                                                                        ),
                                                                                                                    ],
                                                                                                                    ctx=Load(),
                                                                                                                ),
                                                                                                            ),
                                                                                                            type_comment=None,
                                                                                                        ),
                                                                                                        If(
                                                                                                            test=BoolOp(
                                                                                                                op=Or(),
                                                                                                                values=[
                                                                                                                    BoolOp(
                                                                                                                        op=And(),
                                                                                                                        values=[
                                                                                                                            Name(id='need_wildcard', ctx=Load()),
                                                                                                                            UnaryOp(
                                                                                                                                op=Not(),
                                                                                                                                operand=Name(id='right', ctx=Load()),
                                                                                                                            ),
                                                                                                                        ],
                                                                                                                    ),
                                                                                                                    BoolOp(
                                                                                                                        op=And(),
                                                                                                                        values=[
                                                                                                                            Name(id='right', ctx=Load()),
                                                                                                                            Compare(
                                                                                                                                left=Name(id='operator', ctx=Load()),
                                                                                                                                ops=[In()],
                                                                                                                                comparators=[Name(id='NEGATIVE_TERM_OPERATORS', ctx=Load())],
                                                                                                                            ),
                                                                                                                        ],
                                                                                                                    ),
                                                                                                                ],
                                                                                                            ),
                                                                                                            body=[
                                                                                                                Assign(
                                                                                                                    targets=[Name(id='query', ctx=Store())],
                                                                                                                    value=BinOp(
                                                                                                                        left=Constant(value='(%s OR %s."%s" IS NULL)', kind=None),
                                                                                                                        op=Mod(),
                                                                                                                        right=Tuple(
                                                                                                                            elts=[
                                                                                                                                Name(id='query', ctx=Load()),
                                                                                                                                Name(id='table_alias', ctx=Load()),
                                                                                                                                Name(id='left', ctx=Load()),
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
                                                                                                            test=Name(id='need_wildcard', ctx=Load()),
                                                                                                            body=[
                                                                                                                Assign(
                                                                                                                    targets=[Name(id='params', ctx=Store())],
                                                                                                                    value=List(
                                                                                                                        elts=[
                                                                                                                            BinOp(
                                                                                                                                left=Constant(value='%%%s%%', kind=None),
                                                                                                                                op=Mod(),
                                                                                                                                right=Call(
                                                                                                                                    func=Attribute(
                                                                                                                                        value=Name(id='pycompat', ctx=Load()),
                                                                                                                                        attr='to_text',
                                                                                                                                        ctx=Load(),
                                                                                                                                    ),
                                                                                                                                    args=[Name(id='right', ctx=Load())],
                                                                                                                                    keywords=[],
                                                                                                                                ),
                                                                                                                            ),
                                                                                                                        ],
                                                                                                                        ctx=Load(),
                                                                                                                    ),
                                                                                                                    type_comment=None,
                                                                                                                ),
                                                                                                            ],
                                                                                                            orelse=[
                                                                                                                Assign(
                                                                                                                    targets=[Name(id='field', ctx=Store())],
                                                                                                                    value=Subscript(
                                                                                                                        value=Attribute(
                                                                                                                            value=Name(id='model', ctx=Load()),
                                                                                                                            attr='_fields',
                                                                                                                            ctx=Load(),
                                                                                                                        ),
                                                                                                                        slice=Name(id='left', ctx=Load()),
                                                                                                                        ctx=Load(),
                                                                                                                    ),
                                                                                                                    type_comment=None,
                                                                                                                ),
                                                                                                                Assign(
                                                                                                                    targets=[Name(id='params', ctx=Store())],
                                                                                                                    value=List(
                                                                                                                        elts=[
                                                                                                                            Call(
                                                                                                                                func=Attribute(
                                                                                                                                    value=Name(id='field', ctx=Load()),
                                                                                                                                    attr='convert_to_column',
                                                                                                                                    ctx=Load(),
                                                                                                                                ),
                                                                                                                                args=[
                                                                                                                                    Name(id='right', ctx=Load()),
                                                                                                                                    Name(id='model', ctx=Load()),
                                                                                                                                ],
                                                                                                                                keywords=[
                                                                                                                                    keyword(
                                                                                                                                        arg='validate',
                                                                                                                                        value=Constant(value=False, kind=None),
                                                                                                                                    ),
                                                                                                                                ],
                                                                                                                            ),
                                                                                                                        ],
                                                                                                                        ctx=Load(),
                                                                                                                    ),
                                                                                                                    type_comment=None,
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
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Name(id='query', ctx=Load()),
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
                    name='to_sql',
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
                                    Constant(value='deprecated expression.to_sql(), use expression.query instead', kind=None),
                                    Name(id='DeprecationWarning', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='result',
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
