Module(
    body=[
        Import(
            names=[alias(name='time', asname=None)],
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
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
        ClassDef(
            name='ReportJournal',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='AbstractModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='report.account.report_journal', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Account Journal Report', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='lines',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='target_move', annotation=None, type_comment=None),
                            arg(arg='journal_ids', annotation=None, type_comment=None),
                            arg(arg='sort_selection', annotation=None, type_comment=None),
                            arg(arg='data', annotation=None, type_comment=None),
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
                                func=Name(id='isinstance', ctx=Load()),
                                args=[
                                    Name(id='journal_ids', ctx=Load()),
                                    Name(id='int', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='journal_ids', ctx=Store())],
                                    value=List(
                                        elts=[Name(id='journal_ids', ctx=Load())],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='move_state', ctx=Store())],
                            value=List(
                                elts=[
                                    Constant(value='draft', kind=None),
                                    Constant(value='posted', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='target_move', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='posted', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='move_state', ctx=Store())],
                                    value=List(
                                        elts=[Constant(value='posted', kind=None)],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='query_get_clause', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_query_get_clause',
                                    ctx=Load(),
                                ),
                                args=[Name(id='data', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='params', ctx=Store())],
                            value=BinOp(
                                left=List(
                                    elts=[
                                        Call(
                                            func=Name(id='tuple', ctx=Load()),
                                            args=[Name(id='move_state', ctx=Load())],
                                            keywords=[],
                                        ),
                                        Call(
                                            func=Name(id='tuple', ctx=Load()),
                                            args=[Name(id='journal_ids', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                                op=Add(),
                                right=Subscript(
                                    value=Name(id='query_get_clause', ctx=Load()),
                                    slice=Constant(value=2, kind=None),
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='query', ctx=Store())],
                            value=BinOp(
                                left=BinOp(
                                    left=BinOp(
                                        left=BinOp(
                                            left=Constant(value='SELECT "account_move_line".id FROM ', kind=None),
                                            op=Add(),
                                            right=Subscript(
                                                value=Name(id='query_get_clause', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                        ),
                                        op=Add(),
                                        right=Constant(value=', account_move am, account_account acc WHERE "account_move_line".account_id = acc.id AND "account_move_line".move_id=am.id AND am.state IN %s AND "account_move_line".journal_id IN %s AND ', kind=None),
                                    ),
                                    op=Add(),
                                    right=Subscript(
                                        value=Name(id='query_get_clause', ctx=Load()),
                                        slice=Constant(value=1, kind=None),
                                        ctx=Load(),
                                    ),
                                ),
                                op=Add(),
                                right=Constant(value=' ORDER BY ', kind=None),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='sort_selection', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='date', kind=None)],
                            ),
                            body=[
                                AugAssign(
                                    target=Name(id='query', ctx=Store()),
                                    op=Add(),
                                    value=Constant(value='"account_move_line".date', kind=None),
                                ),
                            ],
                            orelse=[
                                AugAssign(
                                    target=Name(id='query', ctx=Store()),
                                    op=Add(),
                                    value=Constant(value='am.name', kind=None),
                                ),
                            ],
                        ),
                        AugAssign(
                            target=Name(id='query', ctx=Store()),
                            op=Add(),
                            value=Constant(value=', "account_move_line".move_id, acc.code', kind=None),
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
                                    Name(id='query', ctx=Load()),
                                    Call(
                                        func=Name(id='tuple', ctx=Load()),
                                        args=[Name(id='params', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='ids', ctx=Store())],
                            value=GeneratorExp(
                                elt=Subscript(
                                    value=Name(id='x', ctx=Load()),
                                    slice=Constant(value=0, kind=None),
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='x', ctx=Store()),
                                        iter=Call(
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
                            type_comment=None,
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
                                        slice=Constant(value='account.move.line', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[Name(id='ids', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_sum_debit',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='data', annotation=None, type_comment=None),
                            arg(arg='journal_id', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='move_state', ctx=Store())],
                            value=List(
                                elts=[
                                    Constant(value='draft', kind=None),
                                    Constant(value='posted', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Name(id='data', ctx=Load()),
                                            slice=Constant(value='form', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='get',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Constant(value='target_move', kind=None),
                                        Constant(value='all', kind=None),
                                    ],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='posted', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='move_state', ctx=Store())],
                                    value=List(
                                        elts=[Constant(value='posted', kind=None)],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='query_get_clause', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_query_get_clause',
                                    ctx=Load(),
                                ),
                                args=[Name(id='data', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='params', ctx=Store())],
                            value=BinOp(
                                left=List(
                                    elts=[
                                        Call(
                                            func=Name(id='tuple', ctx=Load()),
                                            args=[Name(id='move_state', ctx=Load())],
                                            keywords=[],
                                        ),
                                        Call(
                                            func=Name(id='tuple', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Name(id='journal_id', ctx=Load()),
                                                    attr='ids',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                                op=Add(),
                                right=Subscript(
                                    value=Name(id='query_get_clause', ctx=Load()),
                                    slice=Constant(value=2, kind=None),
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
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
                                    BinOp(
                                        left=BinOp(
                                            left=BinOp(
                                                left=BinOp(
                                                    left=Constant(value='SELECT SUM(debit) FROM ', kind=None),
                                                    op=Add(),
                                                    right=Subscript(
                                                        value=Name(id='query_get_clause', ctx=Load()),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                op=Add(),
                                                right=Constant(value=', account_move am WHERE "account_move_line".move_id=am.id AND am.state IN %s AND "account_move_line".journal_id IN %s AND ', kind=None),
                                            ),
                                            op=Add(),
                                            right=Subscript(
                                                value=Name(id='query_get_clause', ctx=Load()),
                                                slice=Constant(value=1, kind=None),
                                                ctx=Load(),
                                            ),
                                        ),
                                        op=Add(),
                                        right=Constant(value=' ', kind=None),
                                    ),
                                    Call(
                                        func=Name(id='tuple', ctx=Load()),
                                        args=[Name(id='params', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Subscript(
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
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=0.0, kind=None),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_sum_credit',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='data', annotation=None, type_comment=None),
                            arg(arg='journal_id', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='move_state', ctx=Store())],
                            value=List(
                                elts=[
                                    Constant(value='draft', kind=None),
                                    Constant(value='posted', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Name(id='data', ctx=Load()),
                                            slice=Constant(value='form', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='get',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Constant(value='target_move', kind=None),
                                        Constant(value='all', kind=None),
                                    ],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='posted', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='move_state', ctx=Store())],
                                    value=List(
                                        elts=[Constant(value='posted', kind=None)],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='query_get_clause', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_query_get_clause',
                                    ctx=Load(),
                                ),
                                args=[Name(id='data', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='params', ctx=Store())],
                            value=BinOp(
                                left=List(
                                    elts=[
                                        Call(
                                            func=Name(id='tuple', ctx=Load()),
                                            args=[Name(id='move_state', ctx=Load())],
                                            keywords=[],
                                        ),
                                        Call(
                                            func=Name(id='tuple', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Name(id='journal_id', ctx=Load()),
                                                    attr='ids',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                                op=Add(),
                                right=Subscript(
                                    value=Name(id='query_get_clause', ctx=Load()),
                                    slice=Constant(value=2, kind=None),
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
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
                                    BinOp(
                                        left=BinOp(
                                            left=BinOp(
                                                left=BinOp(
                                                    left=Constant(value='SELECT SUM(credit) FROM ', kind=None),
                                                    op=Add(),
                                                    right=Subscript(
                                                        value=Name(id='query_get_clause', ctx=Load()),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                op=Add(),
                                                right=Constant(value=', account_move am WHERE "account_move_line".move_id=am.id AND am.state IN %s AND "account_move_line".journal_id IN %s AND ', kind=None),
                                            ),
                                            op=Add(),
                                            right=Subscript(
                                                value=Name(id='query_get_clause', ctx=Load()),
                                                slice=Constant(value=1, kind=None),
                                                ctx=Load(),
                                            ),
                                        ),
                                        op=Add(),
                                        right=Constant(value=' ', kind=None),
                                    ),
                                    Call(
                                        func=Name(id='tuple', ctx=Load()),
                                        args=[Name(id='params', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Subscript(
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
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=0.0, kind=None),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_taxes',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='data', annotation=None, type_comment=None),
                            arg(arg='journal_id', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='move_state', ctx=Store())],
                            value=List(
                                elts=[
                                    Constant(value='draft', kind=None),
                                    Constant(value='posted', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Name(id='data', ctx=Load()),
                                            slice=Constant(value='form', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='get',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Constant(value='target_move', kind=None),
                                        Constant(value='all', kind=None),
                                    ],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='posted', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='move_state', ctx=Store())],
                                    value=List(
                                        elts=[Constant(value='posted', kind=None)],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='query_get_clause', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_query_get_clause',
                                    ctx=Load(),
                                ),
                                args=[Name(id='data', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='params', ctx=Store())],
                            value=BinOp(
                                left=List(
                                    elts=[
                                        Call(
                                            func=Name(id='tuple', ctx=Load()),
                                            args=[Name(id='move_state', ctx=Load())],
                                            keywords=[],
                                        ),
                                        Call(
                                            func=Name(id='tuple', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Name(id='journal_id', ctx=Load()),
                                                    attr='ids',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                                op=Add(),
                                right=Subscript(
                                    value=Name(id='query_get_clause', ctx=Load()),
                                    slice=Constant(value=2, kind=None),
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='query', ctx=Store())],
                            value=BinOp(
                                left=BinOp(
                                    left=BinOp(
                                        left=BinOp(
                                            left=Constant(value='\n            SELECT rel.account_tax_id, SUM("account_move_line".balance) AS base_amount\n            FROM account_move_line_account_tax_rel rel, ', kind=None),
                                            op=Add(),
                                            right=Subscript(
                                                value=Name(id='query_get_clause', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                        ),
                                        op=Add(),
                                        right=Constant(value=' \n            LEFT JOIN account_move am ON "account_move_line".move_id = am.id\n            WHERE "account_move_line".id = rel.account_move_line_id\n                AND am.state IN %s\n                AND "account_move_line".journal_id IN %s\n                AND ', kind=None),
                                    ),
                                    op=Add(),
                                    right=Subscript(
                                        value=Name(id='query_get_clause', ctx=Load()),
                                        slice=Constant(value=1, kind=None),
                                        ctx=Load(),
                                    ),
                                ),
                                op=Add(),
                                right=Constant(value='\n           GROUP BY rel.account_tax_id', kind=None),
                            ),
                            type_comment=None,
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
                                    Name(id='query', ctx=Load()),
                                    Call(
                                        func=Name(id='tuple', ctx=Load()),
                                        args=[Name(id='params', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='ids', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='base_amounts', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='row', ctx=Store()),
                            iter=Call(
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
                                    attr='fetchall',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='ids', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='row', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='base_amounts', ctx=Load()),
                                            slice=Subscript(
                                                value=Name(id='row', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Name(id='row', ctx=Load()),
                                        slice=Constant(value=1, kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='tax', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.tax', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[Name(id='ids', ctx=Load())],
                                keywords=[],
                            ),
                            body=[
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
                                            BinOp(
                                                left=BinOp(
                                                    left=BinOp(
                                                        left=BinOp(
                                                            left=Constant(value='SELECT sum(debit - credit) FROM ', kind=None),
                                                            op=Add(),
                                                            right=Subscript(
                                                                value=Name(id='query_get_clause', ctx=Load()),
                                                                slice=Constant(value=0, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                        op=Add(),
                                                        right=Constant(value=', account_move am WHERE "account_move_line".move_id=am.id AND am.state IN %s AND "account_move_line".journal_id IN %s AND ', kind=None),
                                                    ),
                                                    op=Add(),
                                                    right=Subscript(
                                                        value=Name(id='query_get_clause', ctx=Load()),
                                                        slice=Constant(value=1, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                op=Add(),
                                                right=Constant(value=' AND tax_line_id = %s', kind=None),
                                            ),
                                            Call(
                                                func=Name(id='tuple', ctx=Load()),
                                                args=[
                                                    BinOp(
                                                        left=Name(id='params', ctx=Load()),
                                                        op=Add(),
                                                        right=List(
                                                            elts=[
                                                                Attribute(
                                                                    value=Name(id='tax', ctx=Load()),
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
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='res', ctx=Load()),
                                            slice=Name(id='tax', ctx=Load()),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Dict(
                                        keys=[
                                            Constant(value='base_amount', kind=None),
                                            Constant(value='tax_amount', kind=None),
                                        ],
                                        values=[
                                            Subscript(
                                                value=Name(id='base_amounts', ctx=Load()),
                                                slice=Attribute(
                                                    value=Name(id='tax', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                ctx=Load(),
                                            ),
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    Subscript(
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
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=0.0, kind=None),
                                                ],
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='journal_id', ctx=Load()),
                                            attr='type',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='sale', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Subscript(
                                                        value=Name(id='res', ctx=Load()),
                                                        slice=Name(id='tax', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='base_amount', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=BinOp(
                                                left=Subscript(
                                                    value=Subscript(
                                                        value=Name(id='res', ctx=Load()),
                                                        slice=Name(id='tax', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='base_amount', kind=None),
                                                    ctx=Load(),
                                                ),
                                                op=Mult(),
                                                right=UnaryOp(
                                                    op=USub(),
                                                    operand=Constant(value=1, kind=None),
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Subscript(
                                                        value=Name(id='res', ctx=Load()),
                                                        slice=Name(id='tax', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='tax_amount', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=BinOp(
                                                left=Subscript(
                                                    value=Subscript(
                                                        value=Name(id='res', ctx=Load()),
                                                        slice=Name(id='tax', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='tax_amount', kind=None),
                                                    ctx=Load(),
                                                ),
                                                op=Mult(),
                                                right=UnaryOp(
                                                    op=USub(),
                                                    operand=Constant(value=1, kind=None),
                                                ),
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
                        Return(
                            value=Name(id='res', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_query_get_clause',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='data', annotation=None, type_comment=None),
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
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='account.move.line', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Name(id='data', ctx=Load()),
                                                        slice=Constant(value='form', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='used_context', kind=None),
                                                    Dict(keys=[], values=[]),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_query_get',
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
                    name='_get_report_values',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='docids', annotation=None, type_comment=None),
                            arg(arg='data', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Name(id='data', ctx=Load()),
                                        attr='get',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='form', kind=None)],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='UserError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Form content is missing, this report cannot be printed.', kind=None)],
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
                            targets=[Name(id='target_move', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Name(id='data', ctx=Load()),
                                        slice=Constant(value='form', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='target_move', kind=None),
                                    Constant(value='all', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='sort_selection', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Name(id='data', ctx=Load()),
                                        slice=Constant(value='form', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='sort_selection', kind=None),
                                    Constant(value='date', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='journal', ctx=Store()),
                            iter=Subscript(
                                value=Subscript(
                                    value=Name(id='data', ctx=Load()),
                                    slice=Constant(value='form', kind=None),
                                    ctx=Load(),
                                ),
                                slice=Constant(value='journal_ids', kind=None),
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='res', ctx=Load()),
                                            slice=Name(id='journal', ctx=Load()),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='with_context',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Name(id='data', ctx=Load()),
                                                                slice=Constant(value='form', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='used_context', kind=None),
                                                            Dict(keys=[], values=[]),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='lines',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='target_move', ctx=Load()),
                                            Name(id='journal', ctx=Load()),
                                            Name(id='sort_selection', ctx=Load()),
                                            Name(id='data', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='doc_ids', kind=None),
                                    Constant(value='doc_model', kind=None),
                                    Constant(value='data', kind=None),
                                    Constant(value='docs', kind=None),
                                    Constant(value='time', kind=None),
                                    Constant(value='lines', kind=None),
                                    Constant(value='sum_credit', kind=None),
                                    Constant(value='sum_debit', kind=None),
                                    Constant(value='get_taxes', kind=None),
                                    Constant(value='company_id', kind=None),
                                ],
                                values=[
                                    Subscript(
                                        value=Subscript(
                                            value=Name(id='data', ctx=Load()),
                                            slice=Constant(value='form', kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='journal_ids', kind=None),
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.journal', kind=None),
                                        ctx=Load(),
                                    ),
                                    Name(id='data', ctx=Load()),
                                    Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='account.journal', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Subscript(
                                                    value=Name(id='data', ctx=Load()),
                                                    slice=Constant(value='form', kind=None),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='journal_ids', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Name(id='time', ctx=Load()),
                                    Name(id='res', ctx=Load()),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_sum_credit',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_sum_debit',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_get_taxes',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='res.company', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Subscript(
                                                    value=Subscript(
                                                        value=Name(id='data', ctx=Load()),
                                                        slice=Constant(value='form', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='company_id', kind=None),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
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
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
