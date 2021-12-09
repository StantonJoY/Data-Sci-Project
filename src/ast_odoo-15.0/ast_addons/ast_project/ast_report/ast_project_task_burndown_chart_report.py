Module(
    body=[
        ImportFrom(
            module='psycopg2',
            names=[alias(name='sql', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='tools', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.osv',
            names=[alias(name='expression', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[alias(name='OrderedSet', asname=None)],
            level=0,
        ),
        ClassDef(
            name='ReportProjectTaskBurndownChart',
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
                    value=Constant(value='project.task.burndown.chart.report', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Burndown Chart', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_auto', ctx=Store())],
                    value=Constant(value=False, kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_order', ctx=Store())],
                    value=Constant(value='date', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='project_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='project.project', kind=None)],
                        keywords=[
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='display_project_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='project.project', kind=None)],
                        keywords=[
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='stage_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='project.task.type', kind=None)],
                        keywords=[
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='date', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Datetime',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Date', kind=None)],
                        keywords=[
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='user_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2many',
                            ctx=Load(),
                        ),
                        args=[Constant(value='res.users', kind=None)],
                        keywords=[
                            keyword(
                                arg='relation',
                                value=Constant(value='project_task_user_rel', kind=None),
                            ),
                            keyword(
                                arg='column1',
                                value=Constant(value='task_id', kind=None),
                            ),
                            keyword(
                                arg='column2',
                                value=Constant(value='user_id', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Assignees', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='date_assign', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Datetime',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Assignment Date', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='date_deadline', ctx=Store())],
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
                                value=Constant(value='Deadline', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='partner_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='res.partner', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Customer', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='nb_tasks', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[Constant(value='# of Tasks', kind=None)],
                        keywords=[
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='group_operator',
                                value=Constant(value='sum', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='date_group_by', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[
                            Tuple(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='day', kind=None),
                                            Constant(value='By Day', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='month', kind=None),
                                            Constant(value='By Month', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='quarter', kind=None),
                                            Constant(value='By quarter', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='year', kind=None),
                                            Constant(value='By Year', kind=None),
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
                                value=Constant(value='Date Group By', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='read_group',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='domain', annotation=None, type_comment=None),
                            arg(arg='fields', annotation=None, type_comment=None),
                            arg(arg='groupby', annotation=None, type_comment=None),
                            arg(arg='offset', annotation=None, type_comment=None),
                            arg(arg='limit', annotation=None, type_comment=None),
                            arg(arg='orderby', annotation=None, type_comment=None),
                            arg(arg='lazy', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=0, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=True, kind=None),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='date_group_bys', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='groupby', ctx=Store())],
                            value=IfExp(
                                test=Call(
                                    func=Name(id='isinstance', ctx=Load()),
                                    args=[
                                        Name(id='groupby', ctx=Load()),
                                        Name(id='str', ctx=Load()),
                                    ],
                                    keywords=[],
                                ),
                                body=List(
                                    elts=[Name(id='groupby', ctx=Load())],
                                    ctx=Load(),
                                ),
                                orelse=Call(
                                    func=Name(id='list', ctx=Load()),
                                    args=[
                                        Call(
                                            func=Name(id='OrderedSet', ctx=Load()),
                                            args=[Name(id='groupby', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='gb', ctx=Store()),
                            iter=Name(id='groupby', ctx=Load()),
                            body=[
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Name(id='gb', ctx=Load()),
                                            attr='startswith',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='date:', kind=None)],
                                        keywords=[],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='date_group_bys', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Subscript(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Name(id='gb', ctx=Load()),
                                                                attr='split',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value=':', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        slice=UnaryOp(
                                                            op=USub(),
                                                            operand=Constant(value=1, kind=None),
                                                        ),
                                                        ctx=Load(),
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
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='date_domains', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='gb', ctx=Store()),
                            iter=Name(id='date_group_bys', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='date_domains', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='expression', ctx=Load()),
                                            attr='OR',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Name(id='date_domains', ctx=Load()),
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='date_group_by', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    Name(id='gb', ctx=Load()),
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
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='domain', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='expression', ctx=Load()),
                                    attr='AND',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Name(id='domain', ctx=Load()),
                                            Name(id='date_domains', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='read_group',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='domain', ctx=Load()),
                                    Name(id='fields', ctx=Load()),
                                    Name(id='groupby', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='offset',
                                        value=Name(id='offset', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='limit',
                                        value=Name(id='limit', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='orderby',
                                        value=Name(id='orderby', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='lazy',
                                        value=Name(id='lazy', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='res', ctx=Load()),
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
                    name='init',
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
                            targets=[Name(id='query', ctx=Store())],
                            value=Constant(value="\nWITH all_moves_stage_task AS (\n    -- Here we compute all previous stage in tracking values\n    -- We're missing the last reached stage\n    -- And the tasks without any stage change (which, by definition, are at the last stage)\n    SELECT pt.project_id,\n           pt.id as task_id,\n           pt.display_project_id,\n           COALESCE(LAG(mm.date) OVER (PARTITION BY mm.res_id ORDER BY mm.id), pt.create_date) as date_begin,\n           mm.date as date_end,\n           mtv.old_value_integer as stage_id,\n           pt.date_assign,\n           pt.date_deadline,\n           pt.partner_id\n      FROM project_task pt\n      JOIN mail_message mm ON mm.res_id = pt.id\n                          AND mm.message_type = 'notification'\n                          AND mm.model = 'project.task'\n      JOIN mail_tracking_value mtv ON mm.id = mtv.mail_message_id\n      JOIN ir_model_fields imf ON mtv.field = imf.id\n                              AND imf.model = 'project.task'\n                              AND imf.name = 'stage_id'\n      JOIN project_task_type_rel pttr ON pttr.type_id = mtv.old_value_integer\n                              AND pttr.project_id = pt.project_id\n     WHERE pt.active\n\n    --We compute the last reached stage\n    UNION ALL\n\n    SELECT pt.project_id,\n           pt.id as task_id,\n           pt.display_project_id,\n           COALESCE(md.date, pt.create_date) as date_begin,\n           (CURRENT_DATE + interval '1 month')::date as date_end,\n           pt.stage_id,\n           pt.date_assign,\n           pt.date_deadline,\n           pt.partner_id\n      FROM project_task pt\n      LEFT JOIN LATERAL (SELECT mm.date\n                      FROM mail_message mm\n                      JOIN mail_tracking_value mtv ON mm.id = mtv.mail_message_id\n                      JOIN ir_model_fields imf ON mtv.field = imf.id\n                                              AND imf.model = 'project.task'\n                                              AND imf.name = 'stage_id'\n                     WHERE mm.res_id = pt.id\n                       AND mm.message_type = 'notification'\n                       AND mm.model = 'project.task'\n                  ORDER BY mm.id DESC\n                     FETCH FIRST ROW ONLY) md ON TRUE\n     WHERE pt.active\n)\nSELECT (task_id*10^7 + 10^6 + to_char(d, 'YYMMDD')::integer)::bigint as id,\n       project_id,\n       task_id,\n       display_project_id,\n       stage_id,\n       d as date,\n       date_assign,\n       date_deadline,\n       partner_id,\n       'day' AS date_group_by,\n       1 AS nb_tasks\n  FROM all_moves_stage_task t\n  JOIN LATERAL generate_series(t.date_begin, t.date_end-interval '1 day', '1 day') d ON TRUE\n\nUNION ALL\n\nSELECT (task_id*10^7 + 2*10^6 + to_char(d, 'YYMMDD')::integer)::bigint as id,\n       project_id,\n       task_id,\n       display_project_id,\n       stage_id,\n       date_trunc('week', d) as date,\n       date_assign,\n       date_deadline,\n       partner_id,\n       'week' AS date_group_by,\n       1 AS nb_tasks\n  FROM all_moves_stage_task t\n  JOIN LATERAL generate_series(t.date_begin, t.date_end, '1 week') d ON TRUE\n WHERE date_trunc('week', t.date_begin) <= date_trunc('week', d)\n   AND date_trunc('week', t.date_end) > date_trunc('week', d)\n\nUNION ALL\n\nSELECT (task_id*10^7 + 3*10^6 + to_char(d, 'YYMMDD')::integer)::bigint as id,\n       project_id,\n       task_id,\n       display_project_id,\n       stage_id,\n       date_trunc('month', d) as date,\n       date_assign,\n       date_deadline,\n       partner_id,\n       'month' AS date_group_by,\n       1 AS nb_tasks\n  FROM all_moves_stage_task t\n  JOIN LATERAL generate_series(t.date_begin, t.date_end, '1 month') d ON TRUE\n WHERE date_trunc('month', t.date_begin) <= date_trunc('month', d)\n   AND date_trunc('month', t.date_end) > date_trunc('month', d)\n\nUNION ALL\n\nSELECT (task_id*10^7 + 4*10^6 + to_char(d, 'YYMMDD')::integer)::bigint as id,\n       project_id,\n       task_id,\n       display_project_id,\n       stage_id,\n       date_trunc('quarter', d) as date,\n       date_assign,\n       date_deadline,\n       partner_id,\n       'quarter' AS date_group_by,\n       1 AS nb_tasks\n  FROM all_moves_stage_task t\n  JOIN LATERAL generate_series(t.date_begin, t.date_end, '3 month') d ON TRUE\n WHERE date_trunc('quarter', t.date_begin) <= date_trunc('quarter', d)\n   AND date_trunc('quarter', t.date_end) > date_trunc('quarter', d)\n\nUNION ALL\n\nSELECT (task_id*10^7 + 5*10^6 + to_char(d, 'YYMMDD')::integer)::bigint as id,\n       project_id,\n       task_id,\n       display_project_id,\n       stage_id,\n       date_trunc('year', d) as date,\n       date_assign,\n       date_deadline,\n       partner_id,\n       'year' AS date_group_by,\n       1 AS nb_tasks\n  FROM all_moves_stage_task t\n  JOIN LATERAL generate_series(t.date_begin, t.date_end, '1 year') d ON TRUE\n WHERE date_trunc('year', t.date_begin) <= date_trunc('year', d)\n   AND date_trunc('year', t.date_end) > date_trunc('year', d)\n        ", kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='tools', ctx=Load()),
                                    attr='drop_view_if_exists',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='cr',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_table',
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
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='sql', ctx=Load()),
                                                    attr='SQL',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='CREATE or REPLACE VIEW {} as ({})', kind=None)],
                                                keywords=[],
                                            ),
                                            attr='format',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='sql', ctx=Load()),
                                                    attr='Identifier',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_table',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='sql', ctx=Load()),
                                                    attr='SQL',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='query', ctx=Load())],
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
