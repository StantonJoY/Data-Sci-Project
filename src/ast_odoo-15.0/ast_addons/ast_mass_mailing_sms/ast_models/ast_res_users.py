Module(
    body=[
        Import(
            names=[alias(name='json', asname=None)],
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='modules', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='Users',
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
                    value=Constant(value='res.users', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=List(
                        elts=[Constant(value='res.users', kind=None)],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='systray_get_activities',
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
                            value=Constant(value=' Split mass_mailing and mass_mailing_sms activities in systray by \n            removing the single mailing.mailing activity represented and\n            doing a new query to split them by mailing_type.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='activities', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='Users', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='systray_get_activities',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='activity', ctx=Store()),
                            iter=Name(id='activities', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Call(
                                            func=Attribute(
                                                value=Name(id='activity', ctx=Load()),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='model', kind=None)],
                                            keywords=[],
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='mailing.mailing', kind=None)],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='activities', ctx=Load()),
                                                    attr='remove',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='activity', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[Name(id='query', ctx=Store())],
                                            value=Constant(value="SELECT m.mailing_type, count(*), act.res_model as model, act.res_id,\n                            CASE\n                                WHEN %(today)s::date - act.date_deadline::date = 0 Then 'today'\n                                WHEN %(today)s::date - act.date_deadline::date > 0 Then 'overdue'\n                                WHEN %(today)s::date - act.date_deadline::date < 0 Then 'planned'\n                            END AS states\n                        FROM mail_activity AS act\n                        JOIN mailing_mailing AS m ON act.res_id = m.id\n                        WHERE act.res_model = 'mailing.mailing' AND act.user_id = %(user_id)s  \n                        GROUP BY m.mailing_type, states, act.res_model, act.res_id;\n                        ", kind=None),
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
                                                    Dict(
                                                        keys=[
                                                            Constant(value='today', kind=None),
                                                            Constant(value='user_id', kind=None),
                                                        ],
                                                        values=[
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
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='uid',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[Name(id='activity_data', ctx=Store())],
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
                                            targets=[Name(id='user_activities', ctx=Store())],
                                            value=Dict(keys=[], values=[]),
                                            type_comment=None,
                                        ),
                                        For(
                                            target=Name(id='act', ctx=Store()),
                                            iter=Name(id='activity_data', ctx=Load()),
                                            body=[
                                                If(
                                                    test=UnaryOp(
                                                        op=Not(),
                                                        operand=Call(
                                                            func=Attribute(
                                                                value=Name(id='user_activities', ctx=Load()),
                                                                attr='get',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Subscript(
                                                                    value=Name(id='act', ctx=Load()),
                                                                    slice=Constant(value='mailing_type', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                    body=[
                                                        If(
                                                            test=Compare(
                                                                left=Subscript(
                                                                    value=Name(id='act', ctx=Load()),
                                                                    slice=Constant(value='mailing_type', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='sms', kind=None)],
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='module', ctx=Store())],
                                                                    value=Constant(value='mass_mailing_sms', kind=None),
                                                                    type_comment=None,
                                                                ),
                                                                Assign(
                                                                    targets=[Name(id='name', ctx=Store())],
                                                                    value=Call(
                                                                        func=Name(id='_', ctx=Load()),
                                                                        args=[Constant(value='SMS Marketing', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                            orelse=[
                                                                Assign(
                                                                    targets=[Name(id='module', ctx=Store())],
                                                                    value=Constant(value='mass_mailing', kind=None),
                                                                    type_comment=None,
                                                                ),
                                                                Assign(
                                                                    targets=[Name(id='name', ctx=Store())],
                                                                    value=Call(
                                                                        func=Name(id='_', ctx=Load()),
                                                                        args=[Constant(value='Email Marketing', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='icon', ctx=Store())],
                                                            value=BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    Name(id='module', ctx=Load()),
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='modules', ctx=Load()),
                                                                                attr='module',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='get_module_icon',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Name(id='module', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='res_ids', ctx=Store())],
                                                            value=Call(
                                                                func=Name(id='set', ctx=Load()),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[
                                                                Subscript(
                                                                    value=Name(id='user_activities', ctx=Load()),
                                                                    slice=Subscript(
                                                                        value=Name(id='act', ctx=Load()),
                                                                        slice=Constant(value='mailing_type', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='model', kind=None),
                                                                    Constant(value='type', kind=None),
                                                                    Constant(value='icon', kind=None),
                                                                    Constant(value='total_count', kind=None),
                                                                    Constant(value='today_count', kind=None),
                                                                    Constant(value='overdue_count', kind=None),
                                                                    Constant(value='planned_count', kind=None),
                                                                    Constant(value='res_ids', kind=None),
                                                                ],
                                                                values=[
                                                                    Name(id='name', ctx=Load()),
                                                                    Constant(value='mailing.mailing', kind=None),
                                                                    Constant(value='activity', kind=None),
                                                                    Name(id='icon', ctx=Load()),
                                                                    Constant(value=0, kind=None),
                                                                    Constant(value=0, kind=None),
                                                                    Constant(value=0, kind=None),
                                                                    Constant(value=0, kind=None),
                                                                    Name(id='res_ids', ctx=Load()),
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
                                                            value=Subscript(
                                                                value=Subscript(
                                                                    value=Name(id='user_activities', ctx=Load()),
                                                                    slice=Subscript(
                                                                        value=Name(id='act', ctx=Load()),
                                                                        slice=Constant(value='mailing_type', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='res_ids', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='add',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='act', ctx=Load()),
                                                                slice=Constant(value='res_id', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                AugAssign(
                                                    target=Subscript(
                                                        value=Subscript(
                                                            value=Name(id='user_activities', ctx=Load()),
                                                            slice=Subscript(
                                                                value=Name(id='act', ctx=Load()),
                                                                slice=Constant(value='mailing_type', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            ctx=Load(),
                                                        ),
                                                        slice=BinOp(
                                                            left=Constant(value='%s_count', kind=None),
                                                            op=Mod(),
                                                            right=Subscript(
                                                                value=Name(id='act', ctx=Load()),
                                                                slice=Constant(value='states', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                        ctx=Store(),
                                                    ),
                                                    op=Add(),
                                                    value=Subscript(
                                                        value=Name(id='act', ctx=Load()),
                                                        slice=Constant(value='count', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                If(
                                                    test=Compare(
                                                        left=Subscript(
                                                            value=Name(id='act', ctx=Load()),
                                                            slice=Constant(value='states', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        ops=[In()],
                                                        comparators=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='today', kind=None),
                                                                    Constant(value='overdue', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        AugAssign(
                                                            target=Subscript(
                                                                value=Subscript(
                                                                    value=Name(id='user_activities', ctx=Load()),
                                                                    slice=Subscript(
                                                                        value=Name(id='act', ctx=Load()),
                                                                        slice=Constant(value='mailing_type', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='total_count', kind=None),
                                                                ctx=Store(),
                                                            ),
                                                            op=Add(),
                                                            value=Subscript(
                                                                value=Name(id='act', ctx=Load()),
                                                                slice=Constant(value='count', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                        For(
                                            target=Name(id='mailing_type', ctx=Store()),
                                            iter=Call(
                                                func=Attribute(
                                                    value=Name(id='user_activities', ctx=Load()),
                                                    attr='keys',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Name(id='user_activities', ctx=Load()),
                                                                slice=Name(id='mailing_type', ctx=Load()),
                                                                ctx=Load(),
                                                            ),
                                                            attr='update',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='actions', kind=None),
                                                                    Constant(value='domain', kind=None),
                                                                ],
                                                                values=[
                                                                    List(
                                                                        elts=[
                                                                            Dict(
                                                                                keys=[
                                                                                    Constant(value='icon', kind=None),
                                                                                    Constant(value='name', kind=None),
                                                                                ],
                                                                                values=[
                                                                                    Constant(value='fa-clock-o', kind=None),
                                                                                    Constant(value='Summary', kind=None),
                                                                                ],
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Name(id='json', ctx=Load()),
                                                                            attr='dumps',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            List(
                                                                                elts=[
                                                                                    List(
                                                                                        elts=[
                                                                                            Constant(value='activity_ids.res_id', kind=None),
                                                                                            Constant(value='in', kind=None),
                                                                                            Call(
                                                                                                func=Name(id='list', ctx=Load()),
                                                                                                args=[
                                                                                                    Subscript(
                                                                                                        value=Subscript(
                                                                                                            value=Name(id='user_activities', ctx=Load()),
                                                                                                            slice=Name(id='mailing_type', ctx=Load()),
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        slice=Constant(value='res_ids', kind=None),
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                ],
                                                                                                keywords=[],
                                                                                            ),
                                                                                        ],
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
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
                                            ],
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='activities', ctx=Load()),
                                                    attr='extend',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Name(id='list', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='user_activities', ctx=Load()),
                                                                    attr='values',
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
                                        Break(),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='activities', ctx=Load()),
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
