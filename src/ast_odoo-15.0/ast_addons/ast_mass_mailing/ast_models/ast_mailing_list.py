Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='_', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[alias(name='UserError', asname=None)],
            level=0,
        ),
        ClassDef(
            name='MassMailingList',
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
                    value=Constant(value='Model of a contact list. ', kind=None),
                ),
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='mailing.list', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_order', ctx=Store())],
                    value=Constant(value='name', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Mailing List', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_mailing_enabled', ctx=Store())],
                    value=Constant(value=True, kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_disable_data_merge', ctx=Store())],
                    value=Constant(value=True, kind=None),
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
                                arg='string',
                                value=Constant(value='Mailing List', kind=None),
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
                    targets=[Name(id='contact_count', ctx=Store())],
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
                                value=Constant(value='_compute_mailing_list_statistics', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Number of Contacts', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='contact_count_email', ctx=Store())],
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
                                value=Constant(value='_compute_mailing_list_statistics', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Number of Emails', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='contact_count_opt_out', ctx=Store())],
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
                                value=Constant(value='_compute_mailing_list_statistics', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Number of Opted-out', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='contact_pct_opt_out', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_mailing_list_statistics', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Percentage of Opted-out', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='contact_count_blacklisted', ctx=Store())],
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
                                value=Constant(value='_compute_mailing_list_statistics', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Number of Blacklisted', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='contact_pct_blacklisted', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_mailing_list_statistics', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Percentage of Blacklisted', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='contact_pct_bounce', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_mailing_list_statistics', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Percentage of Bouncing', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='contact_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='mailing.contact', kind=None),
                            Constant(value='mailing_contact_list_rel', kind=None),
                            Constant(value='list_id', kind=None),
                            Constant(value='contact_id', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Mailing Lists', kind=None),
                            ),
                            keyword(
                                arg='copy',
                                value=Constant(value=False, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='mailing_count', ctx=Store())],
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
                                value=Constant(value='_compute_mailing_list_count', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Number of Mailing', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='mailing_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='mailing.mailing', kind=None),
                            Constant(value='mail_mass_mailing_list_rel', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Mass Mailings', kind=None),
                            ),
                            keyword(
                                arg='copy',
                                value=Constant(value=False, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='subscription_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='One2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='mailing.contact.subscription', kind=None),
                            Constant(value='list_id', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Subscription Information', kind=None),
                            ),
                            keyword(
                                arg='copy',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='depends',
                                value=List(
                                    elts=[Constant(value='contact_ids', kind=None)],
                                    ctx=Load(),
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='is_public', ctx=Store())],
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
                            keyword(
                                arg='help',
                                value=Constant(value='The mailing list can be accessible by recipient in the unsubscription page to allows him to update his subscription preferences.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_mailing_list_count',
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
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='ids',
                                ctx=Load(),
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
                                            Constant(value='\n                SELECT mailing_list_id, count(*)\n                FROM mail_mass_mailing_list_rel\n                WHERE mailing_list_id IN %s\n                GROUP BY mailing_list_id', kind=None),
                                            Tuple(
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
                                    targets=[Name(id='data', ctx=Store())],
                                    value=Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[
                                            Call(
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
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        For(
                            target=Name(id='mailing_list', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='mailing_list', ctx=Load()),
                                            attr='mailing_count',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='data', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='mailing_list', ctx=Load()),
                                                    attr='_origin',
                                                    ctx=Load(),
                                                ),
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
                    name='_compute_mailing_list_statistics',
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
                            value=Constant(value=' Computes various statistics for this mailing.list that allow users\n        to have a global idea of its quality (based on blacklist, opt-outs, ...).\n\n        As some fields depend on the value of each other (mainly percentages),\n        we compute everything in a single method. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='contact_statistics_per_mailing', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_fetch_contact_statistics',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='bounce_per_mailing', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='ids',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='sql', ctx=Store())],
                                    value=Constant(value='\n                SELECT mclr.list_id, COUNT(DISTINCT mc.id)\n                FROM mailing_contact mc\n                LEFT OUTER JOIN mailing_contact_list_rel mclr\n                ON mc.id = mclr.contact_id\n                WHERE mc.message_bounce > 0\n                AND mclr.list_id in %s\n                GROUP BY mclr.list_id\n            ', kind=None),
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
                                            Name(id='sql', ctx=Load()),
                                            Tuple(
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
                                    targets=[Name(id='bounce_per_mailing', ctx=Store())],
                                    value=Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[
                                            Call(
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
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        For(
                            target=Name(id='mailing_list', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='contact_counts', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='contact_statistics_per_mailing', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='mailing_list', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Dict(keys=[], values=[]),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Tuple(
                                        elts=[
                                            Name(id='field', ctx=Store()),
                                            Name(id='value', ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                    iter=Call(
                                        func=Attribute(
                                            value=Name(id='contact_counts', ctx=Load()),
                                            attr='items',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Name(id='field', ctx=Load()),
                                                ops=[In()],
                                                comparators=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_fields',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='mailing_list', ctx=Load()),
                                                            slice=Name(id='field', ctx=Load()),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Name(id='value', ctx=Load()),
                                                    type_comment=None,
                                                ),
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
                                            value=Name(id='mailing_list', ctx=Load()),
                                            attr='contact_count',
                                            ctx=Load(),
                                        ),
                                        ops=[NotEq()],
                                        comparators=[Constant(value=0, kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='mailing_list', ctx=Load()),
                                                    attr='contact_pct_opt_out',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=BinOp(
                                                left=Constant(value=100, kind=None),
                                                op=Mult(),
                                                right=BinOp(
                                                    left=Attribute(
                                                        value=Name(id='mailing_list', ctx=Load()),
                                                        attr='contact_count_opt_out',
                                                        ctx=Load(),
                                                    ),
                                                    op=Div(),
                                                    right=Attribute(
                                                        value=Name(id='mailing_list', ctx=Load()),
                                                        attr='contact_count',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='mailing_list', ctx=Load()),
                                                    attr='contact_pct_blacklisted',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=BinOp(
                                                left=Constant(value=100, kind=None),
                                                op=Mult(),
                                                right=BinOp(
                                                    left=Attribute(
                                                        value=Name(id='mailing_list', ctx=Load()),
                                                        attr='contact_count_blacklisted',
                                                        ctx=Load(),
                                                    ),
                                                    op=Div(),
                                                    right=Attribute(
                                                        value=Name(id='mailing_list', ctx=Load()),
                                                        attr='contact_count',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='mailing_list', ctx=Load()),
                                                    attr='contact_pct_bounce',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=BinOp(
                                                left=Constant(value=100, kind=None),
                                                op=Mult(),
                                                right=BinOp(
                                                    left=Call(
                                                        func=Attribute(
                                                            value=Name(id='bounce_per_mailing', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='mailing_list', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=0, kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    op=Div(),
                                                    right=Attribute(
                                                        value=Name(id='mailing_list', ctx=Load()),
                                                        attr='contact_count',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='mailing_list', ctx=Load()),
                                                    attr='contact_pct_opt_out',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=0, kind=None),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='mailing_list', ctx=Load()),
                                                    attr='contact_pct_blacklisted',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=0, kind=None),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='mailing_list', ctx=Load()),
                                                    attr='contact_pct_bounce',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=0, kind=None),
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
                    name='write',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='vals', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Constant(value='active', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='vals', ctx=Load())],
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Name(id='vals', ctx=Load()),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='active', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='mass_mailings', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='mailing.mailing', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='search_count',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='state', kind=None),
                                                            Constant(value='!=', kind=None),
                                                            Constant(value='done', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='contact_list_ids', kind=None),
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
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='mass_mailings', ctx=Load()),
                                        ops=[Gt()],
                                        comparators=[Constant(value=0, kind=None)],
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='UserError', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='At least one of the mailing list you are trying to archive is used in an ongoing mailing campaign.', kind=None)],
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
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='MassMailingList', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[Name(id='vals', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='name_get',
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
                            value=ListComp(
                                elt=Tuple(
                                    elts=[
                                        Attribute(
                                            value=Name(id='list', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        BinOp(
                                            left=Constant(value='%s (%s)', kind=None),
                                            op=Mod(),
                                            right=Tuple(
                                                elts=[
                                                    Attribute(
                                                        value=Name(id='list', ctx=Load()),
                                                        attr='name',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='list', ctx=Load()),
                                                        attr='contact_count',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='list', ctx=Store()),
                                        iter=Name(id='self', ctx=Load()),
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
                    name='copy',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='default', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
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
                            targets=[Name(id='default', ctx=Store())],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Name(id='default', ctx=Load()),
                                            Dict(keys=[], values=[]),
                                        ],
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='name',
                                        value=Call(
                                            func=Name(id='_', ctx=Load()),
                                            args=[
                                                Constant(value='%s (copy)', kind=None),
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='name',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='MassMailingList', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='copy',
                                    ctx=Load(),
                                ),
                                args=[Name(id='default', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='action_view_contacts',
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
                                args=[Constant(value='mass_mailing.action_view_mass_mailing_contacts', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
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
                                            Constant(value='list_ids', kind=None),
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
                            value=Dict(
                                keys=[Constant(value='default_list_ids', kind=None)],
                                values=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='ids',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
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
                    name='action_view_contacts_email',
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
                            targets=[Name(id='action', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='action_view_contacts',
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
                                keywords=[
                                    keyword(
                                        arg='search_default_filter_valid_email_recipient',
                                        value=Constant(value=1, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
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
                    name='action_view_mailings',
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
                                args=[Constant(value='mass_mailing.mailing_mailing_action_mail', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
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
                                            Constant(value='contact_list_ids', kind=None),
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
                            value=Dict(
                                keys=[
                                    Constant(value='default_mailing_type', kind=None),
                                    Constant(value='default_contact_list_ids', kind=None),
                                ],
                                values=[
                                    Constant(value='mail', kind=None),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='ids',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
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
                    name='action_view_contacts_opt_out',
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
                                args=[Constant(value='mass_mailing.action_view_mass_mailing_contacts', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
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
                                            Constant(value='list_ids', kind=None),
                                            Constant(value='in', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='id',
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
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='action', ctx=Load()),
                                    slice=Constant(value='context', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(
                                keys=[
                                    Constant(value='default_list_ids', kind=None),
                                    Constant(value='create', kind=None),
                                    Constant(value='search_default_filter_opt_out', kind=None),
                                ],
                                values=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='ids',
                                        ctx=Load(),
                                    ),
                                    Constant(value=False, kind=None),
                                    Constant(value=1, kind=None),
                                ],
                            ),
                            type_comment=None,
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
                    name='action_view_contacts_blacklisted',
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
                                args=[Constant(value='mass_mailing.action_view_mass_mailing_contacts', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
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
                                            Constant(value='list_ids', kind=None),
                                            Constant(value='in', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='id',
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
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='action', ctx=Load()),
                                    slice=Constant(value='context', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(
                                keys=[
                                    Constant(value='default_list_ids', kind=None),
                                    Constant(value='create', kind=None),
                                    Constant(value='search_default_filter_blacklisted', kind=None),
                                ],
                                values=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='ids',
                                        ctx=Load(),
                                    ),
                                    Constant(value=False, kind=None),
                                    Constant(value=1, kind=None),
                                ],
                            ),
                            type_comment=None,
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
                    name='action_view_contacts_bouncing',
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
                                args=[Constant(value='mass_mailing.action_view_mass_mailing_contacts', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
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
                                            Constant(value='list_ids', kind=None),
                                            Constant(value='in', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='id',
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
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='action', ctx=Load()),
                                    slice=Constant(value='context', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(
                                keys=[
                                    Constant(value='default_list_ids', kind=None),
                                    Constant(value='create', kind=None),
                                    Constant(value='search_default_filter_bounce', kind=None),
                                ],
                                values=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='ids',
                                        ctx=Load(),
                                    ),
                                    Constant(value=False, kind=None),
                                    Constant(value=1, kind=None),
                                ],
                            ),
                            type_comment=None,
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
                    name='action_merge',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='src_lists', annotation=None, type_comment=None),
                            arg(arg='archive', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value="\n            Insert all the contact from the mailing lists 'src_lists' to the\n            mailing list in 'self'. Possibility to archive the mailing lists\n            'src_lists' after the merge except the destination mailing list 'self'.\n        ", kind=None),
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
                        AugAssign(
                            target=Name(id='src_lists', ctx=Store()),
                            op=BitOr(),
                            value=Name(id='self', ctx=Load()),
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
                                        slice=Constant(value='mailing.contact', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='flush',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='email', kind=None),
                                            Constant(value='email_normalized', kind=None),
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
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mailing.contact.subscription', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='flush',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='contact_id', kind=None),
                                            Constant(value='opt_out', kind=None),
                                            Constant(value='list_id', kind=None),
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
                                    Constant(value='\n            INSERT INTO mailing_contact_list_rel (contact_id, list_id)\n            SELECT st.contact_id AS contact_id, %s AS list_id\n            FROM\n                (\n                SELECT\n                    contact.id AS contact_id,\n                    contact.email AS email,\n                    list.id AS list_id,\n                    row_number() OVER (PARTITION BY email ORDER BY email) AS rn\n                FROM\n                    mailing_contact contact,\n                    mailing_contact_list_rel contact_list_rel,\n                    mailing_list list\n                WHERE contact.id=contact_list_rel.contact_id\n                AND COALESCE(contact_list_rel.opt_out,FALSE) = FALSE\n                AND contact.email_normalized NOT IN (select email from mail_blacklist where active = TRUE)\n                AND list.id=contact_list_rel.list_id\n                AND list.id IN %s\n                AND NOT EXISTS\n                    (\n                    SELECT 1\n                    FROM\n                        mailing_contact contact2,\n                        mailing_contact_list_rel contact_list_rel2\n                    WHERE contact2.email = contact.email\n                    AND contact_list_rel2.contact_id = contact2.id\n                    AND contact_list_rel2.list_id = %s\n                    )\n                ) st\n            WHERE st.rn = 1;', kind=None),
                                    Tuple(
                                        elts=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Name(id='tuple', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='src_lists', ctx=Load()),
                                                        attr='ids',
                                                        ctx=Load(),
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
                                    attr='flush',
                                    ctx=Load(),
                                ),
                                args=[],
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
                                args=[],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Name(id='archive', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=BinOp(
                                                left=Name(id='src_lists', ctx=Load()),
                                                op=Sub(),
                                                right=Name(id='self', ctx=Load()),
                                            ),
                                            attr='action_archive',
                                            ctx=Load(),
                                        ),
                                        args=[],
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
                    name='close_dialog',
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
                            value=Dict(
                                keys=[Constant(value='type', kind=None)],
                                values=[Constant(value='ir.actions.act_window_close', kind=None)],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_mailing_get_default_domain',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='mailing', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='list_ids', kind=None),
                                            Constant(value='in', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='mailing', ctx=Load()),
                                                    attr='contact_list_ids',
                                                    ctx=Load(),
                                                ),
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
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_mailing_get_opt_out_list',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='mailing', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Check subscription on all involved mailing lists. If user is opt_out\n        on one list but not on another if two users with same email address, one\n        opted in and the other one opted out, send the mail anyway. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='subscriptions', ctx=Store())],
                            value=IfExp(
                                test=Name(id='self', ctx=Load()),
                                body=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='subscription_ids',
                                    ctx=Load(),
                                ),
                                orelse=Attribute(
                                    value=Attribute(
                                        value=Name(id='mailing', ctx=Load()),
                                        attr='contact_list_ids',
                                        ctx=Load(),
                                    ),
                                    attr='subscription_ids',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='opt_out_contacts', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='subscriptions', ctx=Load()),
                                            attr='filtered',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Lambda(
                                                args=arguments(
                                                    posonlyargs=[],
                                                    args=[arg(arg='rel', annotation=None, type_comment=None)],
                                                    vararg=None,
                                                    kwonlyargs=[],
                                                    kw_defaults=[],
                                                    kwarg=None,
                                                    defaults=[],
                                                ),
                                                body=Attribute(
                                                    value=Name(id='rel', ctx=Load()),
                                                    attr='opt_out',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='mapped',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='contact_id.email_normalized', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='opt_in_contacts', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='subscriptions', ctx=Load()),
                                            attr='filtered',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Lambda(
                                                args=arguments(
                                                    posonlyargs=[],
                                                    args=[arg(arg='rel', annotation=None, type_comment=None)],
                                                    vararg=None,
                                                    kwonlyargs=[],
                                                    kw_defaults=[],
                                                    kwarg=None,
                                                    defaults=[],
                                                ),
                                                body=UnaryOp(
                                                    op=Not(),
                                                    operand=Attribute(
                                                        value=Name(id='rel', ctx=Load()),
                                                        attr='opt_out',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='mapped',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='contact_id.email_normalized', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='opt_out', ctx=Store())],
                            value=Call(
                                func=Name(id='set', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Name(id='c', ctx=Load()),
                                        generators=[
                                            comprehension(
                                                target=Name(id='c', ctx=Store()),
                                                iter=Name(id='opt_out_contacts', ctx=Load()),
                                                ifs=[
                                                    Compare(
                                                        left=Name(id='c', ctx=Load()),
                                                        ops=[NotIn()],
                                                        comparators=[Name(id='opt_in_contacts', ctx=Load())],
                                                    ),
                                                ],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='opt_out', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_fetch_contact_statistics',
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
                            value=Constant(value=" Compute number of contacts matching various conditions.\n        (see '_get_contact_count_select_fields' for details)\n\n        Will return a dict under the form:\n        {\n            42: { # 42 being the mailing list ID\n                'contact_count': 52,\n                'contact_count_email': 35,\n                'contact_count_opt_out': 5,\n                'contact_count_blacklisted': 2\n            },\n            ...\n        } ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='ids',
                                ctx=Load(),
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
                                            JoinedStr(
                                                values=[
                                                    Constant(value='\n                SELECT\n                    ', kind=None),
                                                    FormattedValue(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Constant(value=',', kind=None),
                                                                attr='join',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Call(
                                                                    func=Attribute(
                                                                        value=Call(
                                                                            func=Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='_get_contact_statistics_fields',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[],
                                                                            keywords=[],
                                                                        ),
                                                                        attr='values',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[],
                                                                    keywords=[],
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        conversion=-1,
                                                        format_spec=None,
                                                    ),
                                                    Constant(value='\n                FROM\n                    mailing_contact_list_rel r\n                    ', kind=None),
                                                    FormattedValue(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='_get_contact_statistics_joins',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                        conversion=-1,
                                                        format_spec=None,
                                                    ),
                                                    Constant(value='\n                WHERE list_id IN %s\n                GROUP BY\n                    list_id;\n            ', kind=None),
                                                ],
                                            ),
                                            Tuple(
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
                                    targets=[Name(id='res', ctx=Store())],
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
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='contact_counts', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='res_item', ctx=Store()),
                            iter=Name(id='res', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='mailing_list_id', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='res_item', ctx=Load()),
                                            attr='pop',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='mailing_list_id', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='contact_counts', ctx=Load()),
                                            slice=Name(id='mailing_list_id', ctx=Load()),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='res_item', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='mass_mailing', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='mass_mailing', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        ops=[NotIn()],
                                        comparators=[Name(id='contact_counts', ctx=Load())],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='contact_counts', ctx=Load()),
                                                    slice=Attribute(
                                                        value=Name(id='mass_mailing', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=DictComp(
                                                key=Name(id='field', ctx=Load()),
                                                value=Constant(value=0, kind=None),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='field', ctx=Store()),
                                                        iter=Call(
                                                            func=Attribute(
                                                                value=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='_get_contact_statistics_fields',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[],
                                                                    keywords=[],
                                                                ),
                                                                attr='keys',
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
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='contact_counts', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_contact_statistics_fields',
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
                            value=Constant(value=' Returns fields and SQL query select path in a dictionnary.\n        This is done to be easily overridable in subsequent modules.\n\n        - mailing_list_id             id of the associated mailing.list\n        - contact_count:              all contacts\n        - contact_count_email:        all valid emails\n        - contact_count_opt_out:      all opted-out contacts\n        - contact_count_blacklisted:  all blacklisted contacts ', kind=None),
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='mailing_list_id', kind=None),
                                    Constant(value='contact_count', kind=None),
                                    Constant(value='contact_count_email', kind=None),
                                    Constant(value='contact_count_opt_out', kind=None),
                                    Constant(value='contact_count_blacklisted', kind=None),
                                ],
                                values=[
                                    Constant(value='list_id AS mailing_list_id', kind=None),
                                    Constant(value='COUNT(*) AS contact_count', kind=None),
                                    Constant(value='\n                SUM(CASE WHEN\n                        (c.email_normalized IS NOT NULL\n                        AND COALESCE(r.opt_out,FALSE) = FALSE\n                        AND bl.id IS NULL)\n                        THEN 1 ELSE 0 END) AS contact_count_email', kind=None),
                                    Constant(value='\n                SUM(CASE WHEN COALESCE(r.opt_out,FALSE) = TRUE\n                    THEN 1 ELSE 0 END) AS contact_count_opt_out', kind=None),
                                    JoinedStr(
                                        values=[Constant(value='\n                SUM(CASE WHEN bl.id IS NOT NULL\n                THEN 1 ELSE 0 END) AS contact_count_blacklisted', kind=None)],
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
                    name='_get_contact_statistics_joins',
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
                            value=Constant(value=' Extracted to be easily overridable by sub-modules (such as mass_mailing_sms). ', kind=None),
                        ),
                        Return(
                            value=Constant(value='\n            LEFT JOIN mailing_contact c ON (r.contact_id=c.id)\n            LEFT JOIN mail_blacklist bl on c.email_normalized = bl.email and bl.active', kind=None),
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
