Module(
    body=[
        Import(
            names=[alias(name='json', asname=None)],
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
            module='babel.dates',
            names=[
                alias(name='format_datetime', asname=None),
                alias(name='format_date', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='models', asname=None),
                alias(name='api', asname=None),
                alias(name='_', asname=None),
                alias(name='fields', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.osv',
            names=[alias(name='expression', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.release',
            names=[alias(name='version', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[alias(name='DEFAULT_SERVER_DATE_FORMAT', asname='DF')],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.misc',
            names=[
                alias(name='formatLang', asname=None),
                alias(name='format_date', asname='odoo_format_date'),
                alias(name='get_lang', asname=None),
            ],
            level=0,
        ),
        Import(
            names=[alias(name='random', asname=None)],
        ),
        Import(
            names=[alias(name='ast', asname=None)],
        ),
        ClassDef(
            name='account_journal',
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
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='account.journal', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_kanban_dashboard',
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
                            target=Name(id='journal', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='journal', ctx=Load()),
                                            attr='kanban_dashboard',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='json', ctx=Load()),
                                            attr='dumps',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='journal', ctx=Load()),
                                                    attr='get_journal_dashboard_datas',
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
                    name='_kanban_dashboard_graph',
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
                            target=Name(id='journal', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='journal', ctx=Load()),
                                            attr='type',
                                            ctx=Load(),
                                        ),
                                        ops=[In()],
                                        comparators=[
                                            List(
                                                elts=[
                                                    Constant(value='sale', kind=None),
                                                    Constant(value='purchase', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='journal', ctx=Load()),
                                                    attr='kanban_dashboard_graph',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='json', ctx=Load()),
                                                    attr='dumps',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='journal', ctx=Load()),
                                                            attr='get_bar_graph_datas',
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
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='journal', ctx=Load()),
                                                    attr='type',
                                                    ctx=Load(),
                                                ),
                                                ops=[In()],
                                                comparators=[
                                                    List(
                                                        elts=[
                                                            Constant(value='cash', kind=None),
                                                            Constant(value='bank', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='journal', ctx=Load()),
                                                            attr='kanban_dashboard_graph',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='json', ctx=Load()),
                                                            attr='dumps',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='journal', ctx=Load()),
                                                                    attr='get_line_graph_datas',
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
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='journal', ctx=Load()),
                                                            attr='kanban_dashboard_graph',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Constant(value=False, kind=None),
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
                    name='_get_json_activity_data',
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
                            target=Name(id='journal', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='activities', ctx=Store())],
                                    value=List(elts=[], ctx=Load()),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='sql_query', ctx=Store())],
                                    value=Constant(value="\n                SELECT act.id,\n                    act.res_id,\n                    act.res_model,\n                    act.summary,\n                    act_type.name as act_type_name,\n                    act_type.category as activity_category,\n                    act.date_deadline,\n                    m.date,\n                    m.ref,\n                    CASE WHEN act.date_deadline < CURRENT_DATE THEN 'late' ELSE 'future' END as status\n                FROM account_move m\n                    LEFT JOIN mail_activity act ON act.res_id = m.id\n                    LEFT JOIN mail_activity_type act_type ON act.activity_type_id = act_type.id\n                WHERE act.res_model = 'account.move'\n                    AND m.journal_id = %s\n            ", kind=None),
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
                                            Name(id='sql_query', ctx=Load()),
                                            Tuple(
                                                elts=[
                                                    Attribute(
                                                        value=Name(id='journal', ctx=Load()),
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
                                For(
                                    target=Name(id='activity', ctx=Store()),
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
                                            attr='dictfetchall',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='act', ctx=Store())],
                                            value=Dict(
                                                keys=[
                                                    Constant(value='id', kind=None),
                                                    Constant(value='res_id', kind=None),
                                                    Constant(value='res_model', kind=None),
                                                    Constant(value='status', kind=None),
                                                    Constant(value='name', kind=None),
                                                    Constant(value='activity_category', kind=None),
                                                    Constant(value='date', kind=None),
                                                ],
                                                values=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='activity', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='id', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='activity', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='res_id', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='activity', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='res_model', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='activity', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='status', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='activity', ctx=Load()),
                                                                    attr='get',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='summary', kind=None)],
                                                                keywords=[],
                                                            ),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='activity', ctx=Load()),
                                                                    attr='get',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='act_type_name', kind=None)],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='activity', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='activity_category', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Name(id='odoo_format_date', ctx=Load()),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='activity', ctx=Load()),
                                                                    attr='get',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='date_deadline', kind=None)],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Compare(
                                                        left=Call(
                                                            func=Attribute(
                                                                value=Name(id='activity', ctx=Load()),
                                                                attr='get',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='activity_category', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='tax_report', kind=None)],
                                                    ),
                                                    Compare(
                                                        left=Call(
                                                            func=Attribute(
                                                                value=Name(id='activity', ctx=Load()),
                                                                attr='get',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='res_model', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='account.move', kind=None)],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='act', ctx=Load()),
                                                            slice=Constant(value='name', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='activity', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='ref', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='activities', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='act', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='journal', ctx=Load()),
                                            attr='json_activity_data',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='json', ctx=Load()),
                                            attr='dumps',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='activities', kind=None)],
                                                values=[Name(id='activities', ctx=Load())],
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
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='kanban_dashboard', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Text',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_kanban_dashboard', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='kanban_dashboard_graph', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Text',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_kanban_dashboard_graph', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='json_activity_data', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Text',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_get_json_activity_data', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='show_on_dashboard', ctx=Store())],
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
                                value=Constant(value='Show journal on dashboard', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Whether this journal should be displayed on the dashboard or not', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='color', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Color Index', kind=None)],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value=0, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='entries_count', ctx=Store())],
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
                                value=Constant(value='_compute_entries_count', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_entries_count',
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
                            targets=[Name(id='res', ctx=Store())],
                            value=DictComp(
                                key=Subscript(
                                    value=Subscript(
                                        value=Name(id='r', ctx=Load()),
                                        slice=Constant(value='journal_id', kind=None),
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value=0, kind=None),
                                    ctx=Load(),
                                ),
                                value=Subscript(
                                    value=Name(id='r', ctx=Load()),
                                    slice=Constant(value='journal_id_count', kind=None),
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='r', ctx=Store()),
                                        iter=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='account.move', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='read_group',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='domain',
                                                    value=List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='journal_id', kind=None),
                                                                    Constant(value='in', kind=None),
                                                                    Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='ids',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                keyword(
                                                    arg='fields',
                                                    value=List(
                                                        elts=[Constant(value='journal_id', kind=None)],
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                keyword(
                                                    arg='groupby',
                                                    value=List(
                                                        elts=[Constant(value='journal_id', kind=None)],
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='journal', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='journal', ctx=Load()),
                                            attr='entries_count',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='res', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='journal', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
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
                    name='_graph_title_and_key',
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
                                    attr='type',
                                    ctx=Load(),
                                ),
                                ops=[In()],
                                comparators=[
                                    List(
                                        elts=[
                                            Constant(value='sale', kind=None),
                                            Constant(value='purchase', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=List(
                                        elts=[
                                            Constant(value='', kind=None),
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Residual amount', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='type',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='cash', kind=None)],
                                    ),
                                    body=[
                                        Return(
                                            value=List(
                                                elts=[
                                                    Constant(value='', kind=None),
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Cash: Balance', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='type',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='bank', kind=None)],
                                            ),
                                            body=[
                                                Return(
                                                    value=List(
                                                        elts=[
                                                            Constant(value='', kind=None),
                                                            Call(
                                                                func=Name(id='_', ctx=Load()),
                                                                args=[Constant(value='Bank: Balance', kind=None)],
                                                                keywords=[],
                                                            ),
                                                        ],
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
                    name='get_line_graph_datas',
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
                            value=Constant(value='Computes the data used to display the graph for bank and cash journals in the accounting dashboard', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='currency', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='currency_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='company_id',
                                            ctx=Load(),
                                        ),
                                        attr='currency_id',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='build_graph_data',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='date', annotation=None, type_comment=None),
                                    arg(arg='amount', annotation=None, type_comment=None),
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
                                        func=Name(id='format_date', ctx=Load()),
                                        args=[
                                            Name(id='date', ctx=Load()),
                                            Constant(value='d LLLL Y', kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='locale',
                                                value=Name(id='locale', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='short_name', ctx=Store())],
                                    value=Call(
                                        func=Name(id='format_date', ctx=Load()),
                                        args=[
                                            Name(id='date', ctx=Load()),
                                            Constant(value='d MMM', kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='locale',
                                                value=Name(id='locale', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Return(
                                    value=Dict(
                                        keys=[
                                            Constant(value='x', kind=None),
                                            Constant(value='y', kind=None),
                                            Constant(value='name', kind=None),
                                        ],
                                        values=[
                                            Name(id='short_name', ctx=Load()),
                                            Name(id='amount', ctx=Load()),
                                            Name(id='name', ctx=Load()),
                                        ],
                                    ),
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
                            targets=[Name(id='BankStatement', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='account.bank.statement', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='data', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='today', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='datetime', ctx=Load()),
                                    attr='today',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='last_month', ctx=Store())],
                            value=BinOp(
                                left=Name(id='today', ctx=Load()),
                                op=Add(),
                                right=Call(
                                    func=Name(id='timedelta', ctx=Load()),
                                    args=[],
                                    keywords=[
                                        keyword(
                                            arg='days',
                                            value=UnaryOp(
                                                op=USub(),
                                                operand=Constant(value=30, kind=None),
                                            ),
                                        ),
                                    ],
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='locale', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Name(id='get_lang', ctx=Load()),
                                    args=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                attr='code',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='last_stmt', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_last_bank_statement',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='domain',
                                        value=List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='move_id.state', kind=None),
                                                        Constant(value='=', kind=None),
                                                        Constant(value='posted', kind=None),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='last_balance', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='last_stmt', ctx=Load()),
                                            Attribute(
                                                value=Name(id='last_stmt', ctx=Load()),
                                                attr='balance_end_real',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='data', ctx=Load()),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='build_graph_data', ctx=Load()),
                                        args=[
                                            Name(id='today', ctx=Load()),
                                            Name(id='last_balance', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='date', ctx=Store())],
                            value=Name(id='today', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='amount', ctx=Store())],
                            value=Name(id='last_balance', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='query', ctx=Store())],
                            value=Constant(value='\n            SELECT move.date, sum(st_line.amount) as amount\n            FROM account_bank_statement_line st_line\n            JOIN account_move move ON move.id = st_line.move_id\n            WHERE move.journal_id = %s\n            AND move.date > %s\n            AND move.date <= %s\n            GROUP BY move.date\n            ORDER BY move.date desc\n        ', kind=None),
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
                                    Tuple(
                                        elts=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Name(id='last_month', ctx=Load()),
                                            Name(id='today', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='query_result', ctx=Store())],
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
                                    attr='dictfetchall',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='val', ctx=Store()),
                            iter=Name(id='query_result', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='date', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='val', ctx=Load()),
                                        slice=Constant(value='date', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='date', ctx=Load()),
                                        ops=[NotEq()],
                                        comparators=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='today', ctx=Load()),
                                                    attr='strftime',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='DF', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='data', ctx=Load()),
                                                    slice=Slice(
                                                        lower=None,
                                                        upper=Constant(value=0, kind=None),
                                                        step=None,
                                                    ),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=List(
                                                elts=[
                                                    Call(
                                                        func=Name(id='build_graph_data', ctx=Load()),
                                                        args=[
                                                            Name(id='date', ctx=Load()),
                                                            Name(id='amount', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='amount', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='currency', ctx=Load()),
                                            attr='round',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Name(id='amount', ctx=Load()),
                                                op=Sub(),
                                                right=Subscript(
                                                    value=Name(id='val', ctx=Load()),
                                                    slice=Constant(value='amount', kind=None),
                                                    ctx=Load(),
                                                ),
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
                        If(
                            test=Compare(
                                left=Call(
                                    func=Attribute(
                                        value=Name(id='date', ctx=Load()),
                                        attr='strftime',
                                        ctx=Load(),
                                    ),
                                    args=[Name(id='DF', ctx=Load())],
                                    keywords=[],
                                ),
                                ops=[NotEq()],
                                comparators=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='last_month', ctx=Load()),
                                            attr='strftime',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='DF', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='data', ctx=Load()),
                                            slice=Slice(
                                                lower=None,
                                                upper=Constant(value=0, kind=None),
                                                step=None,
                                            ),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=List(
                                        elts=[
                                            Call(
                                                func=Name(id='build_graph_data', ctx=Load()),
                                                args=[
                                                    Name(id='last_month', ctx=Load()),
                                                    Name(id='amount', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[
                                List(
                                    elts=[
                                        Name(id='graph_title', ctx=Store()),
                                        Name(id='graph_key', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_graph_title_and_key',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='color', ctx=Store())],
                            value=IfExp(
                                test=Compare(
                                    left=Constant(value='e', kind=None),
                                    ops=[In()],
                                    comparators=[Name(id='version', ctx=Load())],
                                ),
                                body=Constant(value='#875A7B', kind=None),
                                orelse=Constant(value='#7c7bad', kind=None),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='is_sample_data', ctx=Store())],
                            value=BoolOp(
                                op=And(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='last_stmt', ctx=Load()),
                                    ),
                                    Compare(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[Name(id='query_result', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value=0, kind=None)],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='is_sample_data', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='data', ctx=Store())],
                                    value=List(elts=[], ctx=Load()),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='i', ctx=Store()),
                                    iter=Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=30, kind=None),
                                            Constant(value=0, kind=None),
                                            UnaryOp(
                                                op=USub(),
                                                operand=Constant(value=5, kind=None),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='current_date', ctx=Store())],
                                            value=BinOp(
                                                left=Name(id='today', ctx=Load()),
                                                op=Add(),
                                                right=Call(
                                                    func=Name(id='timedelta', ctx=Load()),
                                                    args=[],
                                                    keywords=[
                                                        keyword(
                                                            arg='days',
                                                            value=UnaryOp(
                                                                op=USub(),
                                                                operand=Name(id='i', ctx=Load()),
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='data', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Name(id='build_graph_data', ctx=Load()),
                                                        args=[
                                                            Name(id='current_date', ctx=Load()),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='random', ctx=Load()),
                                                                    attr='randint',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    UnaryOp(
                                                                        op=USub(),
                                                                        operand=Constant(value=5, kind=None),
                                                                    ),
                                                                    Constant(value=15, kind=None),
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
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=List(
                                elts=[
                                    Dict(
                                        keys=[
                                            Constant(value='values', kind=None),
                                            Constant(value='title', kind=None),
                                            Constant(value='key', kind=None),
                                            Constant(value='area', kind=None),
                                            Constant(value='color', kind=None),
                                            Constant(value='is_sample_data', kind=None),
                                        ],
                                        values=[
                                            Name(id='data', ctx=Load()),
                                            Name(id='graph_title', ctx=Load()),
                                            Name(id='graph_key', ctx=Load()),
                                            Constant(value=True, kind=None),
                                            Name(id='color', ctx=Load()),
                                            Name(id='is_sample_data', ctx=Load()),
                                        ],
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
                    name='get_bar_graph_datas',
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
                            targets=[Name(id='data', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='today', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='fields', ctx=Load()),
                                        attr='Datetime',
                                        ctx=Load(),
                                    ),
                                    attr='now',
                                    ctx=Load(),
                                ),
                                args=[Name(id='self', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='data', ctx=Load()),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='label', kind=None),
                                            Constant(value='value', kind=None),
                                            Constant(value='type', kind=None),
                                        ],
                                        values=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Due', kind=None)],
                                                keywords=[],
                                            ),
                                            Constant(value=0.0, kind=None),
                                            Constant(value='past', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='day_of_week', ctx=Store())],
                            value=Call(
                                func=Name(id='int', ctx=Load()),
                                args=[
                                    Call(
                                        func=Name(id='format_datetime', ctx=Load()),
                                        args=[
                                            Name(id='today', ctx=Load()),
                                            Constant(value='e', kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='locale',
                                                value=Attribute(
                                                    value=Call(
                                                        func=Name(id='get_lang', ctx=Load()),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    attr='code',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='first_day_of_week', ctx=Store())],
                            value=BinOp(
                                left=Name(id='today', ctx=Load()),
                                op=Add(),
                                right=Call(
                                    func=Name(id='timedelta', ctx=Load()),
                                    args=[],
                                    keywords=[
                                        keyword(
                                            arg='days',
                                            value=BinOp(
                                                left=UnaryOp(
                                                    op=USub(),
                                                    operand=Name(id='day_of_week', ctx=Load()),
                                                ),
                                                op=Add(),
                                                right=Constant(value=1, kind=None),
                                            ),
                                        ),
                                    ],
                                ),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='i', ctx=Store()),
                            iter=Call(
                                func=Name(id='range', ctx=Load()),
                                args=[
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=1, kind=None),
                                    ),
                                    Constant(value=4, kind=None),
                                ],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Name(id='i', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value=0, kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='label', ctx=Store())],
                                            value=Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='This Week', kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Name(id='i', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value=3, kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='label', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Not Due', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[Name(id='start_week', ctx=Store())],
                                                    value=BinOp(
                                                        left=Name(id='first_day_of_week', ctx=Load()),
                                                        op=Add(),
                                                        right=Call(
                                                            func=Name(id='timedelta', ctx=Load()),
                                                            args=[],
                                                            keywords=[
                                                                keyword(
                                                                    arg='days',
                                                                    value=BinOp(
                                                                        left=Name(id='i', ctx=Load()),
                                                                        op=Mult(),
                                                                        right=Constant(value=7, kind=None),
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='end_week', ctx=Store())],
                                                    value=BinOp(
                                                        left=Name(id='start_week', ctx=Load()),
                                                        op=Add(),
                                                        right=Call(
                                                            func=Name(id='timedelta', ctx=Load()),
                                                            args=[],
                                                            keywords=[
                                                                keyword(
                                                                    arg='days',
                                                                    value=Constant(value=6, kind=None),
                                                                ),
                                                            ],
                                                        ),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=Compare(
                                                        left=Attribute(
                                                            value=Name(id='start_week', ctx=Load()),
                                                            attr='month',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[
                                                            Attribute(
                                                                value=Name(id='end_week', ctx=Load()),
                                                                attr='month',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='label', ctx=Store())],
                                                            value=BinOp(
                                                                left=BinOp(
                                                                    left=BinOp(
                                                                        left=BinOp(
                                                                            left=Call(
                                                                                func=Name(id='str', ctx=Load()),
                                                                                args=[
                                                                                    Attribute(
                                                                                        value=Name(id='start_week', ctx=Load()),
                                                                                        attr='day',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                            op=Add(),
                                                                            right=Constant(value='-', kind=None),
                                                                        ),
                                                                        op=Add(),
                                                                        right=Call(
                                                                            func=Name(id='str', ctx=Load()),
                                                                            args=[
                                                                                Attribute(
                                                                                    value=Name(id='end_week', ctx=Load()),
                                                                                    attr='day',
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ],
                                                                            keywords=[],
                                                                        ),
                                                                    ),
                                                                    op=Add(),
                                                                    right=Constant(value=' ', kind=None),
                                                                ),
                                                                op=Add(),
                                                                right=Call(
                                                                    func=Name(id='format_date', ctx=Load()),
                                                                    args=[
                                                                        Name(id='end_week', ctx=Load()),
                                                                        Constant(value='MMM', kind=None),
                                                                    ],
                                                                    keywords=[
                                                                        keyword(
                                                                            arg='locale',
                                                                            value=Attribute(
                                                                                value=Call(
                                                                                    func=Name(id='get_lang', ctx=Load()),
                                                                                    args=[
                                                                                        Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='env',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                    ],
                                                                                    keywords=[],
                                                                                ),
                                                                                attr='code',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[
                                                        Assign(
                                                            targets=[Name(id='label', ctx=Store())],
                                                            value=BinOp(
                                                                left=BinOp(
                                                                    left=Call(
                                                                        func=Name(id='format_date', ctx=Load()),
                                                                        args=[
                                                                            Name(id='start_week', ctx=Load()),
                                                                            Constant(value='d MMM', kind=None),
                                                                        ],
                                                                        keywords=[
                                                                            keyword(
                                                                                arg='locale',
                                                                                value=Attribute(
                                                                                    value=Call(
                                                                                        func=Name(id='get_lang', ctx=Load()),
                                                                                        args=[
                                                                                            Attribute(
                                                                                                value=Name(id='self', ctx=Load()),
                                                                                                attr='env',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                        ],
                                                                                        keywords=[],
                                                                                    ),
                                                                                    attr='code',
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                    op=Add(),
                                                                    right=Constant(value='-', kind=None),
                                                                ),
                                                                op=Add(),
                                                                right=Call(
                                                                    func=Name(id='format_date', ctx=Load()),
                                                                    args=[
                                                                        Name(id='end_week', ctx=Load()),
                                                                        Constant(value='d MMM', kind=None),
                                                                    ],
                                                                    keywords=[
                                                                        keyword(
                                                                            arg='locale',
                                                                            value=Attribute(
                                                                                value=Call(
                                                                                    func=Name(id='get_lang', ctx=Load()),
                                                                                    args=[
                                                                                        Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='env',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                    ],
                                                                                    keywords=[],
                                                                                ),
                                                                                attr='code',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='data', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='label', kind=None),
                                                    Constant(value='value', kind=None),
                                                    Constant(value='type', kind=None),
                                                ],
                                                values=[
                                                    Name(id='label', ctx=Load()),
                                                    Constant(value=0.0, kind=None),
                                                    IfExp(
                                                        test=Compare(
                                                            left=Name(id='i', ctx=Load()),
                                                            ops=[Lt()],
                                                            comparators=[Constant(value=0, kind=None)],
                                                        ),
                                                        body=Constant(value='past', kind=None),
                                                        orelse=Constant(value='future', kind=None),
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
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='select_sql_clause', ctx=Store()),
                                        Name(id='query_args', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_bar_graph_select_query',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='query', ctx=Store())],
                            value=Constant(value='', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='start_date', ctx=Store())],
                            value=BinOp(
                                left=Name(id='first_day_of_week', ctx=Load()),
                                op=Add(),
                                right=Call(
                                    func=Name(id='timedelta', ctx=Load()),
                                    args=[],
                                    keywords=[
                                        keyword(
                                            arg='days',
                                            value=UnaryOp(
                                                op=USub(),
                                                operand=Constant(value=7, kind=None),
                                            ),
                                        ),
                                    ],
                                ),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='i', ctx=Store()),
                            iter=Call(
                                func=Name(id='range', ctx=Load()),
                                args=[
                                    Constant(value=0, kind=None),
                                    Constant(value=6, kind=None),
                                ],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Name(id='i', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value=0, kind=None)],
                                    ),
                                    body=[
                                        AugAssign(
                                            target=Name(id='query', ctx=Store()),
                                            op=Add(),
                                            value=BinOp(
                                                left=BinOp(
                                                    left=BinOp(
                                                        left=BinOp(
                                                            left=Constant(value='(', kind=None),
                                                            op=Add(),
                                                            right=Name(id='select_sql_clause', ctx=Load()),
                                                        ),
                                                        op=Add(),
                                                        right=Constant(value=" and invoice_date_due < '", kind=None),
                                                    ),
                                                    op=Add(),
                                                    right=Call(
                                                        func=Attribute(
                                                            value=Name(id='start_date', ctx=Load()),
                                                            attr='strftime',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='DF', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                                op=Add(),
                                                right=Constant(value="')", kind=None),
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Name(id='i', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value=5, kind=None)],
                                            ),
                                            body=[
                                                AugAssign(
                                                    target=Name(id='query', ctx=Store()),
                                                    op=Add(),
                                                    value=BinOp(
                                                        left=BinOp(
                                                            left=BinOp(
                                                                left=BinOp(
                                                                    left=Constant(value=' UNION ALL (', kind=None),
                                                                    op=Add(),
                                                                    right=Name(id='select_sql_clause', ctx=Load()),
                                                                ),
                                                                op=Add(),
                                                                right=Constant(value=" and invoice_date_due >= '", kind=None),
                                                            ),
                                                            op=Add(),
                                                            right=Call(
                                                                func=Attribute(
                                                                    value=Name(id='start_date', ctx=Load()),
                                                                    attr='strftime',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='DF', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        op=Add(),
                                                        right=Constant(value="')", kind=None),
                                                    ),
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[Name(id='next_date', ctx=Store())],
                                                    value=BinOp(
                                                        left=Name(id='start_date', ctx=Load()),
                                                        op=Add(),
                                                        right=Call(
                                                            func=Name(id='timedelta', ctx=Load()),
                                                            args=[],
                                                            keywords=[
                                                                keyword(
                                                                    arg='days',
                                                                    value=Constant(value=7, kind=None),
                                                                ),
                                                            ],
                                                        ),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                AugAssign(
                                                    target=Name(id='query', ctx=Store()),
                                                    op=Add(),
                                                    value=BinOp(
                                                        left=BinOp(
                                                            left=BinOp(
                                                                left=BinOp(
                                                                    left=BinOp(
                                                                        left=BinOp(
                                                                            left=Constant(value=' UNION ALL (', kind=None),
                                                                            op=Add(),
                                                                            right=Name(id='select_sql_clause', ctx=Load()),
                                                                        ),
                                                                        op=Add(),
                                                                        right=Constant(value=" and invoice_date_due >= '", kind=None),
                                                                    ),
                                                                    op=Add(),
                                                                    right=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='start_date', ctx=Load()),
                                                                            attr='strftime',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Name(id='DF', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                                op=Add(),
                                                                right=Constant(value="' and invoice_date_due < '", kind=None),
                                                            ),
                                                            op=Add(),
                                                            right=Call(
                                                                func=Attribute(
                                                                    value=Name(id='next_date', ctx=Load()),
                                                                    attr='strftime',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='DF', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        op=Add(),
                                                        right=Constant(value="')", kind=None),
                                                    ),
                                                ),
                                                Assign(
                                                    targets=[Name(id='start_date', ctx=Store())],
                                                    value=Name(id='next_date', ctx=Load()),
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
                                    Name(id='query_args', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='query_results', ctx=Store())],
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
                                    attr='dictfetchall',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='is_sample_data', ctx=Store())],
                            value=Constant(value=True, kind=None),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='index', ctx=Store()),
                            iter=Call(
                                func=Name(id='range', ctx=Load()),
                                args=[
                                    Constant(value=0, kind=None),
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='query_results', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Name(id='query_results', ctx=Load()),
                                                    slice=Name(id='index', ctx=Load()),
                                                    ctx=Load(),
                                                ),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='aggr_date', kind=None)],
                                            keywords=[],
                                        ),
                                        ops=[NotEq()],
                                        comparators=[Constant(value=None, kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='is_sample_data', ctx=Store())],
                                            value=Constant(value=False, kind=None),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Subscript(
                                                        value=Name(id='data', ctx=Load()),
                                                        slice=Name(id='index', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='value', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Name(id='query_results', ctx=Load()),
                                                        slice=Name(id='index', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='total', kind=None)],
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
                            targets=[
                                List(
                                    elts=[
                                        Name(id='graph_title', ctx=Store()),
                                        Name(id='graph_key', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_graph_title_and_key',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='is_sample_data', ctx=Load()),
                            body=[
                                For(
                                    target=Name(id='index', ctx=Store()),
                                    iter=Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=0, kind=None),
                                            Call(
                                                func=Name(id='len', ctx=Load()),
                                                args=[Name(id='query_results', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Subscript(
                                                        value=Name(id='data', ctx=Load()),
                                                        slice=Name(id='index', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='type', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value='o_sample_data', kind=None),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Subscript(
                                                        value=Name(id='data', ctx=Load()),
                                                        slice=Name(id='index', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='value', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='random', ctx=Load()),
                                                    attr='randint',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value=0, kind=None),
                                                    Constant(value=20, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='graph_key', ctx=Store())],
                                            value=Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Sample data', kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=List(
                                elts=[
                                    Dict(
                                        keys=[
                                            Constant(value='values', kind=None),
                                            Constant(value='title', kind=None),
                                            Constant(value='key', kind=None),
                                            Constant(value='is_sample_data', kind=None),
                                        ],
                                        values=[
                                            Name(id='data', ctx=Load()),
                                            Name(id='graph_title', ctx=Load()),
                                            Name(id='graph_key', ctx=Load()),
                                            Name(id='is_sample_data', ctx=Load()),
                                        ],
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
                    name='_get_bar_graph_select_query',
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
                            value=Constant(value="\n        Returns a tuple containing the base SELECT SQL query used to gather\n        the bar graph's data as its first element, and the arguments dictionary\n        for it as its second.\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='sign', ctx=Store())],
                            value=IfExp(
                                test=Compare(
                                    left=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='type',
                                        ctx=Load(),
                                    ),
                                    ops=[Eq()],
                                    comparators=[Constant(value='sale', kind=None)],
                                ),
                                body=Constant(value='', kind=None),
                                orelse=Constant(value='-', kind=None),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    BinOp(
                                        left=BinOp(
                                            left=Constant(value='\n            SELECT\n                ', kind=None),
                                            op=Add(),
                                            right=Name(id='sign', ctx=Load()),
                                        ),
                                        op=Add(),
                                        right=Constant(value=" + SUM(move.amount_residual_signed) AS total,\n                MIN(invoice_date_due) AS aggr_date\n            FROM account_move move\n            WHERE move.journal_id = %(journal_id)s\n            AND move.state = 'posted'\n            AND move.payment_state in ('not_paid', 'partial')\n            AND move.move_type IN %(invoice_types)s\n        ", kind=None),
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='invoice_types', kind=None),
                                            Constant(value='journal_id', kind=None),
                                        ],
                                        values=[
                                            Call(
                                                func=Name(id='tuple', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='account.move', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='get_invoice_types',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value=True, kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
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
                    name='get_journal_dashboard_datas',
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
                            targets=[Name(id='currency', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='currency_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='company_id',
                                            ctx=Load(),
                                        ),
                                        attr='currency_id',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Name(id='number_to_reconcile', ctx=Store()),
                                Name(id='number_to_check', ctx=Store()),
                                Name(id='last_balance', ctx=Store()),
                            ],
                            value=Constant(value=0, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='has_at_least_one_statement', ctx=Store())],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Name(id='bank_account_balance', ctx=Store()),
                                Name(id='nb_lines_bank_account_balance', ctx=Store()),
                            ],
                            value=Constant(value=0, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Name(id='outstanding_pay_account_balance', ctx=Store()),
                                Name(id='nb_lines_outstanding_pay_account_balance', ctx=Store()),
                            ],
                            value=Constant(value=0, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='title', ctx=Store())],
                            value=Constant(value='', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Name(id='number_draft', ctx=Store()),
                                Name(id='number_waiting', ctx=Store()),
                                Name(id='number_late', ctx=Store()),
                                Name(id='to_check_balance', ctx=Store()),
                            ],
                            value=Constant(value=0, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Name(id='sum_draft', ctx=Store()),
                                Name(id='sum_waiting', ctx=Store()),
                                Name(id='sum_late', ctx=Store()),
                            ],
                            value=Constant(value=0.0, kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='type',
                                    ctx=Load(),
                                ),
                                ops=[In()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value='bank', kind=None),
                                            Constant(value='cash', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='last_statement', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_last_bank_statement',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='domain',
                                                value=List(
                                                    elts=[
                                                        Tuple(
                                                            elts=[
                                                                Constant(value='move_id.state', kind=None),
                                                                Constant(value='=', kind=None),
                                                                Constant(value='posted', kind=None),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='last_balance', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='last_statement', ctx=Load()),
                                        attr='balance_end',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='has_at_least_one_statement', ctx=Store())],
                                    value=Call(
                                        func=Name(id='bool', ctx=Load()),
                                        args=[Name(id='last_statement', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='bank_account_balance', ctx=Store()),
                                                Name(id='nb_lines_bank_account_balance', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_journal_bank_account_balance',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='domain',
                                                value=List(
                                                    elts=[
                                                        Tuple(
                                                            elts=[
                                                                Constant(value='move_id.state', kind=None),
                                                                Constant(value='=', kind=None),
                                                                Constant(value='posted', kind=None),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='outstanding_pay_account_balance', ctx=Store()),
                                                Name(id='nb_lines_outstanding_pay_account_balance', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_journal_outstanding_payments_account_balance',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='domain',
                                                value=List(
                                                    elts=[
                                                        Tuple(
                                                            elts=[
                                                                Constant(value='move_id.state', kind=None),
                                                                Constant(value='=', kind=None),
                                                                Constant(value='posted', kind=None),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ],
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
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_cr',
                                                ctx=Load(),
                                            ),
                                            attr='execute',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value="\n                SELECT COUNT(st_line.id)\n                FROM account_bank_statement_line st_line\n                JOIN account_move st_line_move ON st_line_move.id = st_line.move_id\n                JOIN account_bank_statement st ON st_line.statement_id = st.id\n                WHERE st_line_move.journal_id IN %s\n                AND st.state = 'posted'\n                AND NOT st_line.is_reconciled\n            ", kind=None),
                                            List(
                                                elts=[
                                                    Call(
                                                        func=Name(id='tuple', ctx=Load()),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='ids',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='number_to_reconcile', ctx=Store())],
                                    value=Subscript(
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
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='to_check_ids', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='to_check_ids',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='number_to_check', ctx=Store())],
                                    value=Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='to_check_ids', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='to_check_balance', ctx=Store())],
                                    value=Call(
                                        func=Name(id='sum', ctx=Load()),
                                        args=[
                                            ListComp(
                                                elt=Attribute(
                                                    value=Name(id='r', ctx=Load()),
                                                    attr='amount',
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='r', ctx=Store()),
                                                        iter=Name(id='to_check_ids', ctx=Load()),
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
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='type',
                                            ctx=Load(),
                                        ),
                                        ops=[In()],
                                        comparators=[
                                            List(
                                                elts=[
                                                    Constant(value='sale', kind=None),
                                                    Constant(value='purchase', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='title', ctx=Store())],
                                            value=IfExp(
                                                test=Compare(
                                                    left=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='type',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[Constant(value='purchase', kind=None)],
                                                ),
                                                body=Call(
                                                    func=Name(id='_', ctx=Load()),
                                                    args=[Constant(value='Bills to pay', kind=None)],
                                                    keywords=[],
                                                ),
                                                orelse=Call(
                                                    func=Name(id='_', ctx=Load()),
                                                    args=[Constant(value='Invoices owed to you', kind=None)],
                                                    keywords=[],
                                                ),
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
                                                        slice=Constant(value='account.move', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='flush',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Constant(value='amount_residual', kind=None),
                                                            Constant(value='currency_id', kind=None),
                                                            Constant(value='move_type', kind=None),
                                                            Constant(value='invoice_date', kind=None),
                                                            Constant(value='company_id', kind=None),
                                                            Constant(value='journal_id', kind=None),
                                                            Constant(value='date', kind=None),
                                                            Constant(value='state', kind=None),
                                                            Constant(value='payment_state', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[
                                                Tuple(
                                                    elts=[
                                                        Name(id='query', ctx=Store()),
                                                        Name(id='query_args', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_get_open_bills_to_pay_query',
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
                                                    Name(id='query_args', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[Name(id='query_results_to_pay', ctx=Store())],
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
                                                    attr='dictfetchall',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Tuple(
                                                    elts=[
                                                        Name(id='query', ctx=Store()),
                                                        Name(id='query_args', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_get_draft_bills_query',
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
                                                    Name(id='query_args', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[Name(id='query_results_drafts', ctx=Store())],
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
                                                    attr='dictfetchall',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Tuple(
                                                    elts=[
                                                        Name(id='query', ctx=Store()),
                                                        Name(id='query_args', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_get_late_bills_query',
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
                                                    Name(id='query_args', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[Name(id='late_query_results', ctx=Store())],
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
                                                    attr='dictfetchall',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='curr_cache', ctx=Store())],
                                            value=Dict(keys=[], values=[]),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Tuple(
                                                    elts=[
                                                        Name(id='number_waiting', ctx=Store()),
                                                        Name(id='sum_waiting', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_count_results_and_sum_amounts',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='query_results_to_pay', ctx=Load()),
                                                    Name(id='currency', ctx=Load()),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='curr_cache',
                                                        value=Name(id='curr_cache', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Tuple(
                                                    elts=[
                                                        Name(id='number_draft', ctx=Store()),
                                                        Name(id='sum_draft', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_count_results_and_sum_amounts',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='query_results_drafts', ctx=Load()),
                                                    Name(id='currency', ctx=Load()),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='curr_cache',
                                                        value=Name(id='curr_cache', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Tuple(
                                                    elts=[
                                                        Name(id='number_late', ctx=Store()),
                                                        Name(id='sum_late', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_count_results_and_sum_amounts',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='late_query_results', ctx=Load()),
                                                    Name(id='currency', ctx=Load()),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='curr_cache',
                                                        value=Name(id='curr_cache', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='read', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='account.move', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='read_group',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='journal_id', kind=None),
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
                                                                    Constant(value='to_check', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    Constant(value=True, kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[Constant(value='amount_total', kind=None)],
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='journal_id', kind=None),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='lazy',
                                                        value=Constant(value=False, kind=None),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Name(id='read', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='number_to_check', ctx=Store())],
                                                    value=Subscript(
                                                        value=Subscript(
                                                            value=Name(id='read', ctx=Load()),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='__count', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='to_check_balance', ctx=Store())],
                                                    value=Subscript(
                                                        value=Subscript(
                                                            value=Name(id='read', ctx=Load()),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='amount_total', kind=None),
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
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='type',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='general', kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='read', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='account.move', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='read_group',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value='journal_id', kind=None),
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
                                                                            Constant(value='to_check', kind=None),
                                                                            Constant(value='=', kind=None),
                                                                            Constant(value=True, kind=None),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            List(
                                                                elts=[Constant(value='amount_total', kind=None)],
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='journal_id', kind=None),
                                                        ],
                                                        keywords=[
                                                            keyword(
                                                                arg='lazy',
                                                                value=Constant(value=False, kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=Name(id='read', ctx=Load()),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='number_to_check', ctx=Store())],
                                                            value=Subscript(
                                                                value=Subscript(
                                                                    value=Name(id='read', ctx=Load()),
                                                                    slice=Constant(value=0, kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='__count', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='to_check_balance', ctx=Store())],
                                                            value=Subscript(
                                                                value=Subscript(
                                                                    value=Name(id='read', ctx=Load()),
                                                                    slice=Constant(value=0, kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='amount_total', kind=None),
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
                                    ],
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='is_sample_data', ctx=Store())],
                            value=BoolOp(
                                op=And(),
                                values=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='kanban_dashboard_graph',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='any', ctx=Load()),
                                        args=[
                                            GeneratorExp(
                                                elt=Call(
                                                    func=Attribute(
                                                        value=Name(id='data', ctx=Load()),
                                                        attr='get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Constant(value='is_sample_data', kind=None),
                                                        Constant(value=False, kind=None),
                                                    ],
                                                    keywords=[],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='data', ctx=Store()),
                                                        iter=Call(
                                                            func=Attribute(
                                                                value=Name(id='json', ctx=Load()),
                                                                attr='loads',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='kanban_dashboard_graph',
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
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='number_to_check', kind=None),
                                    Constant(value='to_check_balance', kind=None),
                                    Constant(value='number_to_reconcile', kind=None),
                                    Constant(value='account_balance', kind=None),
                                    Constant(value='has_at_least_one_statement', kind=None),
                                    Constant(value='nb_lines_bank_account_balance', kind=None),
                                    Constant(value='outstanding_pay_account_balance', kind=None),
                                    Constant(value='nb_lines_outstanding_pay_account_balance', kind=None),
                                    Constant(value='last_balance', kind=None),
                                    Constant(value='number_draft', kind=None),
                                    Constant(value='number_waiting', kind=None),
                                    Constant(value='number_late', kind=None),
                                    Constant(value='sum_draft', kind=None),
                                    Constant(value='sum_waiting', kind=None),
                                    Constant(value='sum_late', kind=None),
                                    Constant(value='currency_id', kind=None),
                                    Constant(value='bank_statements_source', kind=None),
                                    Constant(value='title', kind=None),
                                    Constant(value='is_sample_data', kind=None),
                                    Constant(value='company_count', kind=None),
                                ],
                                values=[
                                    Name(id='number_to_check', ctx=Load()),
                                    Call(
                                        func=Name(id='formatLang', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            Name(id='to_check_balance', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='currency_obj',
                                                value=Name(id='currency', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Name(id='number_to_reconcile', ctx=Load()),
                                    Call(
                                        func=Name(id='formatLang', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='currency', ctx=Load()),
                                                    attr='round',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='bank_account_balance', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='currency_obj',
                                                value=Name(id='currency', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Name(id='has_at_least_one_statement', ctx=Load()),
                                    Name(id='nb_lines_bank_account_balance', ctx=Load()),
                                    Call(
                                        func=Name(id='formatLang', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='currency', ctx=Load()),
                                                    attr='round',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='outstanding_pay_account_balance', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='currency_obj',
                                                value=Name(id='currency', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Name(id='nb_lines_outstanding_pay_account_balance', ctx=Load()),
                                    Call(
                                        func=Name(id='formatLang', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            BinOp(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Name(id='currency', ctx=Load()),
                                                        attr='round',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='last_balance', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                op=Add(),
                                                right=Constant(value=0.0, kind=None),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='currency_obj',
                                                value=Name(id='currency', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Name(id='number_draft', ctx=Load()),
                                    Name(id='number_waiting', ctx=Load()),
                                    Name(id='number_late', ctx=Load()),
                                    Call(
                                        func=Name(id='formatLang', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            BinOp(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Name(id='currency', ctx=Load()),
                                                        attr='round',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='sum_draft', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                op=Add(),
                                                right=Constant(value=0.0, kind=None),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='currency_obj',
                                                value=Name(id='currency', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Name(id='formatLang', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            BinOp(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Name(id='currency', ctx=Load()),
                                                        attr='round',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='sum_waiting', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                op=Add(),
                                                right=Constant(value=0.0, kind=None),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='currency_obj',
                                                value=Name(id='currency', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Name(id='formatLang', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            BinOp(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Name(id='currency', ctx=Load()),
                                                        attr='round',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='sum_late', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                op=Add(),
                                                right=Constant(value=0.0, kind=None),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='currency_obj',
                                                value=Name(id='currency', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Attribute(
                                        value=Name(id='currency', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='bank_statements_source',
                                        ctx=Load(),
                                    ),
                                    Name(id='title', ctx=Load()),
                                    Name(id='is_sample_data', ctx=Load()),
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='companies',
                                                ctx=Load(),
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
                FunctionDef(
                    name='_get_open_bills_to_pay_query',
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
                            value=Constant(value='\n        Returns a tuple containing the SQL query used to gather the open bills\n        data as its first element, and the arguments dictionary to use to run\n        it as its second.\n        ', kind=None),
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Constant(value="\n            SELECT\n                (CASE WHEN move.move_type IN ('out_refund', 'in_refund') THEN -1 ELSE 1 END) * move.amount_residual AS amount_total,\n                move.currency_id AS currency,\n                move.move_type,\n                move.invoice_date,\n                move.company_id\n            FROM account_move move\n            WHERE move.journal_id = %(journal_id)s\n            AND move.state = 'posted'\n            AND move.payment_state in ('not_paid', 'partial')\n            AND move.move_type IN ('out_invoice', 'out_refund', 'in_invoice', 'in_refund', 'out_receipt', 'in_receipt');\n        ", kind=None),
                                    Dict(
                                        keys=[Constant(value='journal_id', kind=None)],
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
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
                    name='_get_draft_bills_query',
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
                            value=Constant(value='\n        Returns a tuple containing as its first element the SQL query used to\n        gather the bills in draft state data, and the arguments\n        dictionary to use to run it as its second.\n        ', kind=None),
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Constant(value="\n            SELECT\n                (CASE WHEN move.move_type IN ('out_refund', 'in_refund') THEN -1 ELSE 1 END) * move.amount_total AS amount_total,\n                move.currency_id AS currency,\n                move.move_type,\n                move.invoice_date,\n                move.company_id\n            FROM account_move move\n            WHERE move.journal_id = %(journal_id)s\n            AND move.state = 'draft'\n            AND move.payment_state in ('not_paid', 'partial')\n            AND move.move_type IN ('out_invoice', 'out_refund', 'in_invoice', 'in_refund', 'out_receipt', 'in_receipt');\n        ", kind=None),
                                    Dict(
                                        keys=[Constant(value='journal_id', kind=None)],
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
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
                    name='_get_late_bills_query',
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
                            value=Tuple(
                                elts=[
                                    Constant(value="\n            SELECT\n                (CASE WHEN move_type IN ('out_refund', 'in_refund') THEN -1 ELSE 1 END) * amount_residual AS amount_total,\n                currency_id AS currency,\n                move_type,\n                invoice_date,\n                company_id\n            FROM account_move move\n            WHERE journal_id = %(journal_id)s\n            AND invoice_date_due < %(today)s\n            AND state = 'posted'\n            AND payment_state in ('not_paid', 'partial')\n            AND move_type IN ('out_invoice', 'out_refund', 'in_invoice', 'in_refund', 'out_receipt', 'in_receipt');\n        ", kind=None),
                                    Dict(
                                        keys=[
                                            Constant(value='journal_id', kind=None),
                                            Constant(value='today', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='fields', ctx=Load()),
                                                        attr='Date',
                                                        ctx=Load(),
                                                    ),
                                                    attr='context_today',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='self', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
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
                    name='_count_results_and_sum_amounts',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='results_dict', annotation=None, type_comment=None),
                            arg(arg='target_currency', annotation=None, type_comment=None),
                            arg(arg='curr_cache', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Loops on a query result to count the total number of invoices and sum\n        their amount_total field (expressed in the given target currency).\n        amount_total must be signed !\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='rslt_count', ctx=Store())],
                            value=Constant(value=0, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='rslt_sum', ctx=Store())],
                            value=Constant(value=0.0, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='curr_cache', ctx=Store())],
                            value=IfExp(
                                test=Compare(
                                    left=Name(id='curr_cache', ctx=Load()),
                                    ops=[Is()],
                                    comparators=[Constant(value=None, kind=None)],
                                ),
                                body=Dict(keys=[], values=[]),
                                orelse=Name(id='curr_cache', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='result', ctx=Store()),
                            iter=Name(id='results_dict', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='cur', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='res.currency', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='result', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='currency', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='company', ctx=Store())],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
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
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='result', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='company_id', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='company',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                AugAssign(
                                    target=Name(id='rslt_count', ctx=Store()),
                                    op=Add(),
                                    value=Constant(value=1, kind=None),
                                ),
                                Assign(
                                    targets=[Name(id='date', ctx=Store())],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='result', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='invoice_date', kind=None)],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='fields', ctx=Load()),
                                                        attr='Date',
                                                        ctx=Load(),
                                                    ),
                                                    attr='context_today',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='self', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='amount', ctx=Store())],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='result', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='amount_total', kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Constant(value=0, kind=None),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='cur', ctx=Load()),
                                        ops=[NotEq()],
                                        comparators=[Name(id='target_currency', ctx=Load())],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='key', ctx=Store())],
                                            value=Tuple(
                                                elts=[
                                                    Name(id='cur', ctx=Load()),
                                                    Name(id='target_currency', ctx=Load()),
                                                    Name(id='company', ctx=Load()),
                                                    Name(id='date', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Name(id='key', ctx=Load()),
                                                ops=[NotIn()],
                                                comparators=[Name(id='curr_cache', ctx=Load())],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='curr_cache', ctx=Load()),
                                                            slice=Name(id='key', ctx=Load()),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='res.currency', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='_get_conversion_rate',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Starred(
                                                                value=Name(id='key', ctx=Load()),
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
                                        AugAssign(
                                            target=Name(id='amount', ctx=Store()),
                                            op=Mult(),
                                            value=Subscript(
                                                value=Name(id='curr_cache', ctx=Load()),
                                                slice=Name(id='key', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                AugAssign(
                                    target=Name(id='rslt_sum', ctx=Store()),
                                    op=Add(),
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='target_currency', ctx=Load()),
                                            attr='round',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='amount', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Name(id='rslt_count', ctx=Load()),
                                    Name(id='rslt_sum', ctx=Load()),
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
                    name='action_create_new',
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
                            targets=[Name(id='ctx', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_context',
                                        ctx=Load(),
                                    ),
                                    attr='copy',
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
                                    value=Name(id='ctx', ctx=Load()),
                                    slice=Constant(value='default_journal_id', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
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
                                            value=Name(id='ctx', ctx=Load()),
                                            slice=Constant(value='default_move_type', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=IfExp(
                                        test=Call(
                                            func=Attribute(
                                                value=Name(id='ctx', ctx=Load()),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='refund', kind=None)],
                                            keywords=[],
                                        ),
                                        body=Constant(value='out_refund', kind=None),
                                        orelse=Constant(value='out_invoice', kind=None),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='type',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='purchase', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='ctx', ctx=Load()),
                                                    slice=Constant(value='default_move_type', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=IfExp(
                                                test=Call(
                                                    func=Attribute(
                                                        value=Name(id='ctx', ctx=Load()),
                                                        attr='get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='refund', kind=None)],
                                                    keywords=[],
                                                ),
                                                body=Constant(value='in_refund', kind=None),
                                                orelse=Constant(value='in_invoice', kind=None),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='ctx', ctx=Load()),
                                                    slice=Constant(value='default_move_type', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value='entry', kind=None),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='ctx', ctx=Load()),
                                                    slice=Constant(value='view_no_maturity', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=True, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='name', kind=None),
                                    Constant(value='type', kind=None),
                                    Constant(value='view_mode', kind=None),
                                    Constant(value='res_model', kind=None),
                                    Constant(value='view_id', kind=None),
                                    Constant(value='context', kind=None),
                                ],
                                values=[
                                    Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='Create invoice/bill', kind=None)],
                                        keywords=[],
                                    ),
                                    Constant(value='ir.actions.act_window', kind=None),
                                    Constant(value='form', kind=None),
                                    Constant(value='account.move', kind=None),
                                    Attribute(
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
                                            args=[Constant(value='account.view_move_form', kind=None)],
                                            keywords=[],
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Name(id='ctx', ctx=Load()),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='create_cash_statement',
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
                            targets=[Name(id='ctx', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_context',
                                        ctx=Load(),
                                    ),
                                    attr='copy',
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
                                    value=Name(id='ctx', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='journal_id', kind=None),
                                            Constant(value='default_journal_id', kind=None),
                                            Constant(value='default_journal_type', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='cash', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='open_statements', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.bank.statement', kind=None),
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
                                                    Constant(value='journal_id', kind=None),
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
                                                    Constant(value='state', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='open', kind=None),
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
                        Assign(
                            targets=[Name(id='action', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='name', kind=None),
                                    Constant(value='type', kind=None),
                                    Constant(value='view_mode', kind=None),
                                    Constant(value='res_model', kind=None),
                                    Constant(value='context', kind=None),
                                ],
                                values=[
                                    Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='Create cash statement', kind=None)],
                                        keywords=[],
                                    ),
                                    Constant(value='ir.actions.act_window', kind=None),
                                    Constant(value='form', kind=None),
                                    Constant(value='account.bank.statement', kind=None),
                                    Name(id='ctx', ctx=Load()),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Call(
                                    func=Name(id='len', ctx=Load()),
                                    args=[Name(id='open_statements', ctx=Load())],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value=1, kind=None)],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='action', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='view_mode', kind=None),
                                                    Constant(value='res_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='form', kind=None),
                                                    Attribute(
                                                        value=Name(id='open_statements', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[Name(id='open_statements', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ops=[Gt()],
                                        comparators=[Constant(value=1, kind=None)],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='action', ctx=Load()),
                                                    attr='update',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='view_mode', kind=None),
                                                            Constant(value='domain', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='tree,form', kind=None),
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value='id', kind=None),
                                                                            Constant(value='in', kind=None),
                                                                            Attribute(
                                                                                value=Name(id='open_statements', ctx=Load()),
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
                        Return(
                            value=Name(id='action', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='action_create_vendor_bill',
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
                            value=Constant(value=' This function is called by the "Import" button of Vendor Bills,\n        visible on dashboard if no bill has been created yet.\n        ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='company',
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='set_onboarding_step_done',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='account_setup_bill_state', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='new_wizard', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.tour.upload.bill', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Dict(keys=[], values=[])],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='view_id', ctx=Store())],
                            value=Attribute(
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
                                    args=[Constant(value='account.account_tour_upload_bill', kind=None)],
                                    keywords=[],
                                ),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='type', kind=None),
                                    Constant(value='name', kind=None),
                                    Constant(value='view_mode', kind=None),
                                    Constant(value='res_model', kind=None),
                                    Constant(value='target', kind=None),
                                    Constant(value='res_id', kind=None),
                                    Constant(value='views', kind=None),
                                ],
                                values=[
                                    Constant(value='ir.actions.act_window', kind=None),
                                    Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='Import your first bill', kind=None)],
                                        keywords=[],
                                    ),
                                    Constant(value='form', kind=None),
                                    Constant(value='account.tour.upload.bill', kind=None),
                                    Constant(value='new', kind=None),
                                    Attribute(
                                        value=Name(id='new_wizard', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[
                                                    Name(id='view_id', ctx=Load()),
                                                    Constant(value='form', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
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
                    name='to_check_ids',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='domain', ctx=Store())],
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
                                    attr='_get_suspense_moves_domain',
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
                                    value=Name(id='domain', ctx=Load()),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[
                                    Tuple(
                                        elts=[
                                            Constant(value='journal_id', kind=None),
                                            Constant(value='=', kind=None),
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
                        Assign(
                            targets=[Name(id='statement_line_ids', ctx=Store())],
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
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='domain', ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='mapped',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='statement_line_id', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='statement_line_ids', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_select_action_to_open',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_context',
                                        ctx=Load(),
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='action_name', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_context',
                                                ctx=Load(),
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='action_name', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='type',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='bank', kind=None)],
                                    ),
                                    body=[
                                        Return(
                                            value=Constant(value='action_bank_statement_tree', kind=None),
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='type',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='cash', kind=None)],
                                            ),
                                            body=[
                                                Return(
                                                    value=Constant(value='action_view_bank_statement_tree', kind=None),
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Compare(
                                                        left=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='type',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='sale', kind=None)],
                                                    ),
                                                    body=[
                                                        Return(
                                                            value=Constant(value='action_move_out_invoice_type', kind=None),
                                                        ),
                                                    ],
                                                    orelse=[
                                                        If(
                                                            test=Compare(
                                                                left=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='type',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='purchase', kind=None)],
                                                            ),
                                                            body=[
                                                                Return(
                                                                    value=Constant(value='action_move_in_invoice_type', kind=None),
                                                                ),
                                                            ],
                                                            orelse=[
                                                                Return(
                                                                    value=Constant(value='action_move_journal_line', kind=None),
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
                    name='open_action',
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
                            value=Constant(value='return action based on type for related journals', kind=None),
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
                            targets=[Name(id='action_name', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_select_action_to_open',
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
                                        value=Name(id='action_name', ctx=Load()),
                                        attr='startswith',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='account.', kind=None)],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='action_name', ctx=Store())],
                                    value=BinOp(
                                        left=Constant(value='account.%s', kind=None),
                                        op=Mod(),
                                        right=Name(id='action_name', ctx=Load()),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='action', ctx=Store())],
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
                                    attr='_for_xml_id',
                                    ctx=Load(),
                                ),
                                args=[Name(id='action_name', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='context', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_context',
                                        ctx=Load(),
                                    ),
                                    attr='copy',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Constant(value='context', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='action', ctx=Load())],
                                    ),
                                    Compare(
                                        left=Call(
                                            func=Name(id='type', ctx=Load()),
                                            args=[
                                                Subscript(
                                                    value=Name(id='action', ctx=Load()),
                                                    slice=Constant(value='context', kind=None),
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        ops=[Eq()],
                                        comparators=[Name(id='str', ctx=Load())],
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='context', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='ast', ctx=Load()),
                                                    attr='literal_eval',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='action', ctx=Load()),
                                                        slice=Constant(value='context', kind=None),
                                                        ctx=Load(),
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
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='context', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='action', ctx=Load()),
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
                                        keywords=[],
                                    ),
                                ),
                            ],
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='action', ctx=Load()),
                                    slice=Constant(value='context', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='context', ctx=Load()),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Name(id='action', ctx=Load()),
                                        slice=Constant(value='context', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='default_journal_id', kind=None),
                                            Constant(value='search_default_journal_id', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
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
                        ),
                        Assign(
                            targets=[Name(id='domain_type_field', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Subscript(
                                                    value=Name(id='action', ctx=Load()),
                                                    slice=Constant(value='res_model', kind=None),
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='account.move.line', kind=None)],
                                            ),
                                            Constant(value='move_id.move_type', kind=None),
                                        ],
                                    ),
                                    Constant(value='move_type', kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_context',
                                            ctx=Load(),
                                        ),
                                        attr='get',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='action_name', kind=None)],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
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
                                                    value=Name(id='action', ctx=Load()),
                                                    slice=Constant(value='domain', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Name(id='domain_type_field', ctx=Load()),
                                                            Constant(value='in', kind=None),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='out_invoice', kind=None),
                                                                    Constant(value='out_refund', kind=None),
                                                                    Constant(value='out_receipt', kind=None),
                                                                ],
                                                                ctx=Load(),
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
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='type',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='purchase', kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='action', ctx=Load()),
                                                            slice=Constant(value='domain', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Name(id='domain_type_field', ctx=Load()),
                                                                    Constant(value='in', kind=None),
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value='in_invoice', kind=None),
                                                                            Constant(value='in_refund', kind=None),
                                                                            Constant(value='in_receipt', kind=None),
                                                                            Constant(value='entry', kind=None),
                                                                        ],
                                                                        ctx=Load(),
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
                                            orelse=[],
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='action', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='open_spend_money',
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
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='open_payments_action',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='outbound', kind=None)],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='open_collect_money',
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
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='open_payments_action',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='inbound', kind=None)],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='open_transfer_money',
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
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='open_payments_action',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='transfer', kind=None)],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='open_payments_action',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='payment_type', annotation=None, type_comment=None),
                            arg(arg='mode', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value='tree', kind=None)],
                    ),
                    body=[
                        If(
                            test=Compare(
                                left=Name(id='payment_type', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='outbound', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='action_ref', ctx=Store())],
                                    value=Constant(value='account.action_account_payments_payable', kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Name(id='payment_type', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='transfer', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='action_ref', ctx=Store())],
                                            value=Constant(value='account.action_account_payments_transfer', kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='action_ref', ctx=Store())],
                                            value=Constant(value='account.action_account_payments', kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='action', ctx=Store())],
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
                                    attr='_for_xml_id',
                                    ctx=Load(),
                                ),
                                args=[Name(id='action_ref', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='action', ctx=Load()),
                                    slice=Constant(value='context', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='ast', ctx=Load()),
                                            attr='literal_eval',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='action', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='context', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='default_journal_id',
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='search_default_journal_id',
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='payment_type', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='transfer', kind=None)],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='action', ctx=Load()),
                                                slice=Constant(value='context', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='default_partner_id', kind=None),
                                                    Constant(value='default_is_internal_transfer', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='company_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='partner_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=True, kind=None),
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
                                left=Name(id='mode', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='form', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='action', ctx=Load()),
                                            slice=Constant(value='views', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=List(
                                        elts=[
                                            List(
                                                elts=[
                                                    Constant(value=False, kind=None),
                                                    Constant(value='form', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='action', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='open_action_with_context',
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
                            targets=[Name(id='action_name', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='context',
                                        ctx=Load(),
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='action_name', kind=None),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='action_name', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='ctx', ctx=Store())],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='context',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='default_journal_id',
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='ctx', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='search_default_journal', kind=None),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='ctx', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='search_default_journal_id',
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='ctx', ctx=Load()),
                                            slice=Constant(value='search_default_journal', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='ctx', ctx=Load()),
                                    attr='pop',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='group_by', kind=None),
                                    Constant(value=None, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='action', ctx=Store())],
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
                                    attr='_for_xml_id',
                                    ctx=Load(),
                                ),
                                args=[
                                    JoinedStr(
                                        values=[
                                            Constant(value='account.', kind=None),
                                            FormattedValue(
                                                value=Name(id='action_name', ctx=Load()),
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
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='action', ctx=Load()),
                                    slice=Constant(value='context', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='ctx', ctx=Load()),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='ctx', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='use_domain', kind=None),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='action', ctx=Load()),
                                            slice=Constant(value='domain', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    Call(
                                                        func=Name(id='isinstance', ctx=Load()),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='ctx', ctx=Load()),
                                                                slice=Constant(value='use_domain', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            Name(id='list', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Subscript(
                                                        value=Name(id='ctx', ctx=Load()),
                                                        slice=Constant(value='use_domain', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='|', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='journal_id', kind=None),
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
                                                            Constant(value='journal_id', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Constant(value=False, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='action', ctx=Load()),
                                            slice=Constant(value='name', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='%(action)s for journal %(journal)s', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='action',
                                                value=Subscript(
                                                    value=Name(id='action', ctx=Load()),
                                                    slice=Constant(value='name', kind=None),
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='journal',
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='name',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='action', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='create_bank_statement',
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
                            value=Constant(value="return action to create a bank statements. This button should be called only on journals with type =='bank'", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='action', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.actions.actions', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_for_xml_id',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='account.action_bank_statement_tree', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='action', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='views', kind=None),
                                            Constant(value='context', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    List(
                                                        elts=[
                                                            Constant(value=False, kind=None),
                                                            Constant(value='form', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            BinOp(
                                                left=BinOp(
                                                    left=Constant(value="{'default_journal_id': ", kind=None),
                                                    op=Add(),
                                                    right=Call(
                                                        func=Name(id='str', ctx=Load()),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                op=Add(),
                                                right=Constant(value='}', kind=None),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Name(id='action', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='create_customer_payment',
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
                            value=Constant(value='return action to create a customer payment', kind=None),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='open_payments_action',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='inbound', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='mode',
                                        value=Constant(value='form', kind=None),
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
                    name='create_supplier_payment',
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
                            value=Constant(value='return action to create a supplier payment', kind=None),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='open_payments_action',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='outbound', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='mode',
                                        value=Constant(value='form', kind=None),
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
                    name='create_internal_transfer',
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
                            value=Constant(value='return action to create a internal transfer', kind=None),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='open_payments_action',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='transfer', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='mode',
                                        value=Constant(value='form', kind=None),
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
                    name='mark_bank_setup_as_done_action',
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
                            value=Constant(value=" Marks the 'bank setup' step as done in the setup bar and in the company.", kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='company_id',
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='set_onboarding_step_done',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='account_setup_bank_data_state', kind=None)],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='unmark_bank_setup_as_done_action',
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
                            value=Constant(value=" Marks the 'bank setup' step as not done in the setup bar and in the company.", kind=None),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='company_id',
                                        ctx=Load(),
                                    ),
                                    attr='account_setup_bank_data_state',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='not_done', kind=None),
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
    ],
    type_ignores=[],
)
