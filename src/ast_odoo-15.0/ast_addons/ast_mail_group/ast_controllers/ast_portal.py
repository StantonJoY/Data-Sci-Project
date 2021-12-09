Module(
    body=[
        Import(
            names=[alias(name='werkzeug', asname=None)],
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='http', asname=None),
                alias(name='fields', asname=None),
                alias(name='tools', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.http_routing.models.ir_http',
            names=[alias(name='slug', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.portal.controllers.portal',
            names=[alias(name='pager', asname='portal_pager')],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[alias(name='AccessError', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.http',
            names=[alias(name='request', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.osv',
            names=[alias(name='expression', asname=None)],
            level=0,
        ),
        ClassDef(
            name='PortalMailGroup',
            bases=[
                Attribute(
                    value=Name(id='http', ctx=Load()),
                    attr='Controller',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_thread_per_page', ctx=Store())],
                    value=Constant(value=20, kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_replies_per_page', ctx=Store())],
                    value=Constant(value=5, kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_website_domain',
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
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='moderation_status', kind=None),
                                            Constant(value='!=', kind=None),
                                            Constant(value='rejected', kind=None),
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
                    name='_get_archives',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='group_id', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Return the different date range and message count for the group messages.', kind=None),
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
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_get_website_domain',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='mail_group_id', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Name(id='group_id', ctx=Load()),
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
                        Assign(
                            targets=[Name(id='results', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.group.message', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_read_group_raw',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='domain', ctx=Load()),
                                    List(
                                        elts=[
                                            Constant(value='subject', kind=None),
                                            Constant(value='create_date', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='groupby',
                                        value=List(
                                            elts=[Constant(value='create_date', kind=None)],
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='orderby',
                                        value=Constant(value='create_date', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='date_groups', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='result', ctx=Store()),
                            iter=Name(id='results', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='dates_range', ctx=Store()),
                                                Name(id='label', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='create_date', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='start', ctx=Store()),
                                                Name(id='end', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='dates_range', ctx=Load()),
                                            attr='split',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='/', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='date_groups', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='date', kind=None),
                                                    Constant(value='date_begin', kind=None),
                                                    Constant(value='date_end', kind=None),
                                                    Constant(value='messages_count', kind=None),
                                                ],
                                                values=[
                                                    Name(id='label', ctx=Load()),
                                                    Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='fields', ctx=Load()),
                                                                attr='Date',
                                                                ctx=Load(),
                                                            ),
                                                            attr='to_string',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='fields', ctx=Load()),
                                                                        attr='Date',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='to_date',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='start', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='fields', ctx=Load()),
                                                                attr='Date',
                                                                ctx=Load(),
                                                            ),
                                                            attr='to_string',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='fields', ctx=Load()),
                                                                        attr='Date',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='to_date',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='end', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Subscript(
                                                        value=Name(id='result', ctx=Load()),
                                                        slice=Constant(value='create_date_count', kind=None),
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
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='thread_domain', ctx=Store())],
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
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='group_message_parent_id', kind=None),
                                                            Constant(value='=', kind=None),
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
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='threads_count', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.group.message', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search_count',
                                    ctx=Load(),
                                ),
                                args=[Name(id='thread_domain', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='threads_count', kind=None),
                                    Constant(value='threads_time_data', kind=None),
                                ],
                                values=[
                                    Name(id='threads_count', ctx=Load()),
                                    Name(id='date_groups', ctx=Load()),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='groups_index',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='email', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kw', annotation=None, type_comment=None),
                        defaults=[Constant(value='', kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='View of the group lists. Allow the users to subscribe and unsubscribe.', kind=None),
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='kw', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='group_id', kind=None)],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='kw', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='token', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='group_id', ctx=Store())],
                                    value=Call(
                                        func=Name(id='int', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='kw', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='group_id', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='token', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='kw', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='token', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='group', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='request', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='mail.group', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='browse',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='group_id', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    attr='exists',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='sudo',
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
                                        operand=Name(id='group', ctx=Load()),
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='werkzeug', ctx=Load()),
                                                        attr='exceptions',
                                                        ctx=Load(),
                                                    ),
                                                    attr='NotFound',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='token', ctx=Load()),
                                        ops=[NotEq()],
                                        comparators=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='group', ctx=Load()),
                                                    attr='_generate_group_access_token',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='werkzeug', ctx=Load()),
                                                        attr='exceptions',
                                                        ctx=Load(),
                                                    ),
                                                    attr='NotFound',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='mail_groups', ctx=Store())],
                                    value=Name(id='group', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='mail_groups', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='request', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='mail.group', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='search',
                                                    ctx=Load(),
                                                ),
                                                args=[List(elts=[], ctx=Load())],
                                                keywords=[],
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='request', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='user',
                                            ctx=Load(),
                                        ),
                                        attr='_is_public',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='email_normalized', ctx=Store())],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='request', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='user',
                                            ctx=Load(),
                                        ),
                                        attr='email_normalized',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='partner_id', ctx=Store())],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='user',
                                                ctx=Load(),
                                            ),
                                            attr='partner_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='email_normalized', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='tools', ctx=Load()),
                                            attr='email_normalize',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='email', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='partner_id', ctx=Store())],
                                    value=Constant(value=None, kind=None),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='members_data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='mail_groups', ctx=Load()),
                                    attr='_find_members',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='email_normalized', ctx=Load()),
                                    Name(id='partner_id', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='render',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='mail_group.mail_groups', kind=None),
                                    Dict(
                                        keys=[
                                            Constant(value='mail_groups', kind=None),
                                            Constant(value='email', kind=None),
                                            Constant(value='is_mail_group_manager', kind=None),
                                        ],
                                        values=[
                                            ListComp(
                                                elt=Dict(
                                                    keys=[
                                                        Constant(value='group', kind=None),
                                                        Constant(value='is_member', kind=None),
                                                    ],
                                                    values=[
                                                        Name(id='group', ctx=Load()),
                                                        Call(
                                                            func=Name(id='bool', ctx=Load()),
                                                            args=[
                                                                Call(
                                                                    func=Attribute(
                                                                        value=Name(id='members_data', ctx=Load()),
                                                                        attr='get',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[
                                                                        Attribute(
                                                                            value=Name(id='group', ctx=Load()),
                                                                            attr='id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        Constant(value=False, kind=None),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='group', ctx=Store()),
                                                        iter=Name(id='mail_groups', ctx=Load()),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                            Name(id='email_normalized', ctx=Load()),
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='request', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='user',
                                                        ctx=Load(),
                                                    ),
                                                    attr='has_group',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='mail_group.group_mail_group_manager', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[Constant(value='/groups', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='public', kind=None),
                                ),
                                keyword(
                                    arg='sitemap',
                                    value=Constant(value=True, kind=None),
                                ),
                                keyword(
                                    arg='website',
                                    value=Constant(value=True, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='group_view_messages',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='group', annotation=None, type_comment=None),
                            arg(arg='page', annotation=None, type_comment=None),
                            arg(arg='mode', annotation=None, type_comment=None),
                            arg(arg='date_begin', annotation=None, type_comment=None),
                            arg(arg='date_end', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='post', annotation=None, type_comment=None),
                        defaults=[
                            Constant(value=1, kind=None),
                            Constant(value='thread', kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='GroupMessage', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='mail.group.message', kind=None),
                                ctx=Load(),
                            ),
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
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_get_website_domain',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='mail_group_id', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Attribute(
                                                                value=Name(id='group', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
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
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='mode', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='thread', kind=None)],
                            ),
                            body=[
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
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='group_message_parent_id', kind=None),
                                                                    Constant(value='=', kind=None),
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
                                    Name(id='date_begin', ctx=Load()),
                                    Name(id='date_end', ctx=Load()),
                                ],
                            ),
                            body=[
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
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='create_date', kind=None),
                                                                    Constant(value='>', kind=None),
                                                                    Name(id='date_begin', ctx=Load()),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='create_date', kind=None),
                                                                    Constant(value='<=', kind=None),
                                                                    Name(id='date_end', ctx=Load()),
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
                        ),
                        Assign(
                            targets=[Name(id='messages_sudo', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='GroupMessage', ctx=Load()),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='domain', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='limit',
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_thread_per_page',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='offset',
                                                value=BinOp(
                                                    left=BinOp(
                                                        left=Name(id='page', ctx=Load()),
                                                        op=Sub(),
                                                        right=Constant(value=1, kind=None),
                                                    ),
                                                    op=Mult(),
                                                    right=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_thread_per_page',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ),
                                        ],
                                    ),
                                    attr='sudo',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='pager', ctx=Store())],
                            value=Call(
                                func=Name(id='portal_pager', ctx=Load()),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='url',
                                        value=JoinedStr(
                                            values=[
                                                Constant(value='/groups/', kind=None),
                                                FormattedValue(
                                                    value=Call(
                                                        func=Name(id='slug', ctx=Load()),
                                                        args=[Name(id='group', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    conversion=-1,
                                                    format_spec=None,
                                                ),
                                            ],
                                        ),
                                    ),
                                    keyword(
                                        arg='total',
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='GroupMessage', ctx=Load()),
                                                attr='search_count',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='domain', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ),
                                    keyword(
                                        arg='page',
                                        value=Name(id='page', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='step',
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_thread_per_page',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='scope',
                                        value=Constant(value=5, kind=None),
                                    ),
                                    keyword(
                                        arg='url_args',
                                        value=Dict(
                                            keys=[
                                                Constant(value='date_begin', kind=None),
                                                Constant(value='date_end', kind=None),
                                                Constant(value='mode', kind=None),
                                            ],
                                            values=[
                                                Name(id='date_begin', ctx=Load()),
                                                Name(id='date_end', ctx=Load()),
                                                Name(id='mode', ctx=Load()),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_generate_attachments_access_token',
                                    ctx=Load(),
                                ),
                                args=[Name(id='messages_sudo', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='render',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='mail_group.group_messages', kind=None),
                                    Dict(
                                        keys=[
                                            Constant(value='page_name', kind=None),
                                            Constant(value='group', kind=None),
                                            Constant(value='messages', kind=None),
                                            Constant(value='archives', kind=None),
                                            Constant(value='date_begin', kind=None),
                                            Constant(value='date_end', kind=None),
                                            Constant(value='pager', kind=None),
                                            Constant(value='replies_per_page', kind=None),
                                            Constant(value='mode', kind=None),
                                        ],
                                        values=[
                                            Constant(value='groups', kind=None),
                                            Name(id='group', ctx=Load()),
                                            Name(id='messages_sudo', ctx=Load()),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_get_archives',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='group', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Name(id='date_begin', ctx=Load()),
                                            Name(id='date_end', ctx=Load()),
                                            Name(id='pager', ctx=Load()),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_replies_per_page',
                                                ctx=Load(),
                                            ),
                                            Name(id='mode', ctx=Load()),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[
                                List(
                                    elts=[
                                        Constant(value='/groups/<model("mail.group"):group>', kind=None),
                                        Constant(value='/groups/<model("mail.group"):group>/page/<int:page>', kind=None),
                                    ],
                                    ctx=Load(),
                                ),
                            ],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='public', kind=None),
                                ),
                                keyword(
                                    arg='sitemap',
                                    value=Constant(value=True, kind=None),
                                ),
                                keyword(
                                    arg='website',
                                    value=Constant(value=True, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='group_view_message',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='group', annotation=None, type_comment=None),
                            arg(arg='message', annotation=None, type_comment=None),
                            arg(arg='mode', annotation=None, type_comment=None),
                            arg(arg='date_begin', annotation=None, type_comment=None),
                            arg(arg='date_end', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='post', annotation=None, type_comment=None),
                        defaults=[
                            Constant(value='thread', kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        If(
                            test=Compare(
                                left=Name(id='group', ctx=Load()),
                                ops=[NotEq()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='message', ctx=Load()),
                                        attr='mail_group_id',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='werkzeug', ctx=Load()),
                                                attr='exceptions',
                                                ctx=Load(),
                                            ),
                                            attr='NotFound',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='GroupMessage', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='mail.group.message', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='base_domain', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='expression', ctx=Load()),
                                    attr='AND',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_get_website_domain',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='mail_group_id', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Attribute(
                                                                value=Name(id='group', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='group_message_parent_id', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='message', ctx=Load()),
                                                                    attr='group_message_parent_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
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
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='next_message', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='GroupMessage', ctx=Load()),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='expression', ctx=Load()),
                                            attr='AND',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Name(id='base_domain', ctx=Load()),
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='id', kind=None),
                                                                    Constant(value='>', kind=None),
                                                                    Attribute(
                                                                        value=Name(id='message', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
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
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='order',
                                        value=Constant(value='id ASC', kind=None),
                                    ),
                                    keyword(
                                        arg='limit',
                                        value=Constant(value=1, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='prev_message', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='GroupMessage', ctx=Load()),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='expression', ctx=Load()),
                                            attr='AND',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Name(id='base_domain', ctx=Load()),
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='id', kind=None),
                                                                    Constant(value='<', kind=None),
                                                                    Attribute(
                                                                        value=Name(id='message', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
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
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='order',
                                        value=Constant(value='id DESC', kind=None),
                                    ),
                                    keyword(
                                        arg='limit',
                                        value=Constant(value=1, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='message_sudo', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='message', ctx=Load()),
                                    attr='sudo',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='_generate_attachments_access_token',
                                    ctx=Load(),
                                ),
                                args=[Name(id='message_sudo', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='page_name', kind=None),
                                    Constant(value='message', kind=None),
                                    Constant(value='group', kind=None),
                                    Constant(value='mode', kind=None),
                                    Constant(value='archives', kind=None),
                                    Constant(value='date_begin', kind=None),
                                    Constant(value='date_end', kind=None),
                                    Constant(value='replies_per_page', kind=None),
                                    Constant(value='next_message', kind=None),
                                    Constant(value='prev_message', kind=None),
                                ],
                                values=[
                                    Constant(value='groups', kind=None),
                                    Name(id='message_sudo', ctx=Load()),
                                    Name(id='group', ctx=Load()),
                                    Name(id='mode', ctx=Load()),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_archives',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='group', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Name(id='date_begin', ctx=Load()),
                                    Name(id='date_end', ctx=Load()),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_replies_per_page',
                                        ctx=Load(),
                                    ),
                                    Name(id='next_message', ctx=Load()),
                                    Name(id='prev_message', ctx=Load()),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='render',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='mail_group.group_message', kind=None),
                                    Name(id='values', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[Constant(value='/groups/<model("mail.group"):group>/<model("mail.group.message"):message>', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='public', kind=None),
                                ),
                                keyword(
                                    arg='sitemap',
                                    value=Constant(value=True, kind=None),
                                ),
                                keyword(
                                    arg='website',
                                    value=Constant(value=True, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='group_message_get_replies',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='group', annotation=None, type_comment=None),
                            arg(arg='message', annotation=None, type_comment=None),
                            arg(arg='last_displayed_id', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='post', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=Compare(
                                left=Name(id='group', ctx=Load()),
                                ops=[NotEq()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='message', ctx=Load()),
                                        attr='mail_group_id',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='werkzeug', ctx=Load()),
                                                attr='exceptions',
                                                ctx=Load(),
                                            ),
                                            attr='NotFound',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='replies_domain', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='expression', ctx=Load()),
                                    attr='AND',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_get_website_domain',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='id', kind=None),
                                                            Constant(value='>', kind=None),
                                                            Call(
                                                                func=Name(id='int', ctx=Load()),
                                                                args=[Name(id='last_displayed_id', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='group_message_parent_id', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Attribute(
                                                                value=Name(id='message', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
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
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='replies_sudo', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='mail.group.message', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='replies_domain', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='limit',
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_replies_per_page',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    attr='sudo',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='message_count', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.group.message', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search_count',
                                    ctx=Load(),
                                ),
                                args=[Name(id='replies_domain', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='replies_sudo', ctx=Load()),
                            ),
                            body=[Return(value=None)],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='message_sudo', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='message', ctx=Load()),
                                    attr='sudo',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='_generate_attachments_access_token',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Name(id='message_sudo', ctx=Load()),
                                        op=BitOr(),
                                        right=Name(id='replies_sudo', ctx=Load()),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='group', kind=None),
                                    Constant(value='parent_message', kind=None),
                                    Constant(value='messages', kind=None),
                                    Constant(value='msg_more_count', kind=None),
                                    Constant(value='replies_per_page', kind=None),
                                ],
                                values=[
                                    Name(id='group', ctx=Load()),
                                    Name(id='message_sudo', ctx=Load()),
                                    Name(id='replies_sudo', ctx=Load()),
                                    BinOp(
                                        left=Name(id='message_count', ctx=Load()),
                                        op=Sub(),
                                        right=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_replies_per_page',
                                            ctx=Load(),
                                        ),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_replies_per_page',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='request', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='ref',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='mail_group.messages_short', kind=None)],
                                        keywords=[],
                                    ),
                                    attr='_render',
                                    ctx=Load(),
                                ),
                                args=[Name(id='values', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='engine',
                                        value=Constant(value='ir.qweb', kind=None),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[Constant(value='/groups/<model("mail.group"):group>/<model("mail.group.message"):message>/get_replies', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='json', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='public', kind=None),
                                ),
                                keyword(
                                    arg='methods',
                                    value=List(
                                        elts=[Constant(value='POST', kind=None)],
                                        ctx=Load(),
                                    ),
                                ),
                                keyword(
                                    arg='website',
                                    value=Constant(value=True, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='group_subscribe',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='group_id', annotation=None, type_comment=None),
                            arg(arg='email', annotation=None, type_comment=None),
                            arg(arg='token', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kw', annotation=None, type_comment=None),
                        defaults=[
                            Constant(value=0, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value="Subscribe the current logged user or the given email address to the mailing list.\n\n        If the user is logged, the action is automatically done.\n\n        But if the user is not logged (public user) an email will be send with a token\n        to confirm the action.\n\n        :param group_id: Id of the group\n        :param email: Email to add in the member list\n        :param token: An access token to bypass the <mail.group> access rule\n        :return:\n            'added'\n                if the member was added in the mailing list\n            'email_sent'\n                if we send a confirmation email\n            'is_already_member'\n                if we try to subscribe but we are already member\n        ", kind=None),
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='group_sudo', ctx=Store()),
                                        Name(id='is_member', ctx=Store()),
                                        Name(id='partner_id', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_group_subscription_get_group',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='group_id', ctx=Load()),
                                    Name(id='email', ctx=Load()),
                                    Name(id='token', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='is_member', ctx=Load()),
                            body=[
                                Return(
                                    value=Constant(value='is_already_member', kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='request', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='user',
                                            ctx=Load(),
                                        ),
                                        attr='_is_public',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='group_sudo', ctx=Load()),
                                            attr='_join_group',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='request', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='user',
                                                    ctx=Load(),
                                                ),
                                                attr='email',
                                                ctx=Load(),
                                            ),
                                            Name(id='partner_id', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Return(
                                    value=Constant(value='added', kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='group_sudo', ctx=Load()),
                                    attr='_send_subscribe_confirmation_email',
                                    ctx=Load(),
                                ),
                                args=[Name(id='email', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Constant(value='email_sent', kind=None),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[Constant(value='/group/subscribe', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='json', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='public', kind=None),
                                ),
                                keyword(
                                    arg='website',
                                    value=Constant(value=True, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='group_unsubscribe',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='group_id', annotation=None, type_comment=None),
                            arg(arg='email', annotation=None, type_comment=None),
                            arg(arg='token', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kw', annotation=None, type_comment=None),
                        defaults=[
                            Constant(value=0, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value="Unsubscribe the current logged user or the given email address to the mailing list.\n\n        If the user is logged, the action is automatically done.\n\n        But if the user is not logged (public user) an email will be send with a token\n        to confirm the action.\n\n        :param group_id: Id of the group\n        :param email: Email to add in the member list\n        :param token: An access token to bypass the <mail.group> access rule\n        :return:\n            'removed'\n                if the member was removed from the mailing list\n            'email_sent'\n                if we send a confirmation email\n            'is_not_member'\n                if we try to unsubscribe but we are not member\n        ", kind=None),
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='group_sudo', ctx=Store()),
                                        Name(id='is_member', ctx=Store()),
                                        Name(id='partner_id', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_group_subscription_get_group',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='group_id', ctx=Load()),
                                    Name(id='email', ctx=Load()),
                                    Name(id='token', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='is_member', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Constant(value='is_not_member', kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='request', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='user',
                                            ctx=Load(),
                                        ),
                                        attr='_is_public',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='group_sudo', ctx=Load()),
                                            attr='_leave_group',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='request', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='user',
                                                    ctx=Load(),
                                                ),
                                                attr='email',
                                                ctx=Load(),
                                            ),
                                            Name(id='partner_id', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Return(
                                    value=Constant(value='removed', kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='group_sudo', ctx=Load()),
                                    attr='_send_unsubscribe_confirmation_email',
                                    ctx=Load(),
                                ),
                                args=[Name(id='email', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Constant(value='email_sent', kind=None),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[Constant(value='/group/unsubscribe', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='json', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='public', kind=None),
                                ),
                                keyword(
                                    arg='website',
                                    value=Constant(value=True, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_group_subscription_get_group',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='group_id', annotation=None, type_comment=None),
                            arg(arg='email', annotation=None, type_comment=None),
                            arg(arg='token', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Check the given token and return,\n\n        :return:\n            - The group sudo-ed\n            - True if the email is member of the group\n            - The partner of the current user\n        :raise NotFound: if the given token is not valid\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='group', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='mail.group', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='int', ctx=Load()),
                                                args=[Name(id='group_id', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='exists',
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
                                operand=Name(id='group', ctx=Load()),
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='werkzeug', ctx=Load()),
                                                attr='exceptions',
                                                ctx=Load(),
                                            ),
                                            attr='NotFound',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='group_sudo', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='group', ctx=Load()),
                                    attr='sudo',
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
                                    Name(id='token', ctx=Load()),
                                    Compare(
                                        left=Name(id='token', ctx=Load()),
                                        ops=[NotEq()],
                                        comparators=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='group_sudo', ctx=Load()),
                                                    attr='_generate_group_access_token',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='werkzeug', ctx=Load()),
                                                attr='exceptions',
                                                ctx=Load(),
                                            ),
                                            attr='NotFound',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='token', ctx=Load()),
                                    ),
                                    body=[
                                        Try(
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='group', ctx=Load()),
                                                            attr='check_access_rights',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='read', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='group', ctx=Load()),
                                                            attr='check_access_rule',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='read', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            handlers=[
                                                ExceptHandler(
                                                    type=Name(id='AccessError', ctx=Load()),
                                                    name=None,
                                                    body=[
                                                        Raise(
                                                            exc=Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='werkzeug', ctx=Load()),
                                                                        attr='exceptions',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='NotFound',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
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
                                    orelse=[],
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='partner_id', ctx=Store())],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='request', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='user',
                                            ctx=Load(),
                                        ),
                                        attr='_is_public',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='partner_id', ctx=Store())],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='user',
                                                ctx=Load(),
                                            ),
                                            attr='partner_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='is_member', ctx=Store())],
                            value=Call(
                                func=Name(id='bool', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='group_sudo', ctx=Load()),
                                            attr='_find_member',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='email', ctx=Load()),
                                            Name(id='partner_id', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Name(id='group_sudo', ctx=Load()),
                                    Name(id='is_member', ctx=Load()),
                                    Name(id='partner_id', ctx=Load()),
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
                    name='group_subscribe_confirm',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='group_id', annotation=None, type_comment=None),
                            arg(arg='email', annotation=None, type_comment=None),
                            arg(arg='token', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kw', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Confirm the subscribe / unsubscribe action which was sent by email.', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='group', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_group_subscription_confirm_get_group',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='group_id', ctx=Load()),
                                    Name(id='email', ctx=Load()),
                                    Name(id='token', ctx=Load()),
                                    Constant(value='subscribe', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='group', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='render',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='mail_group.invalid_token_subscription', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='partners', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='mail.thread', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_mail_find_partner_from_emails',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Name(id='email', ctx=Load())],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='partner_id', ctx=Store())],
                            value=IfExp(
                                test=Name(id='partners', ctx=Load()),
                                body=Attribute(
                                    value=Subscript(
                                        value=Name(id='partners', ctx=Load()),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                orelse=Constant(value=None, kind=None),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='group', ctx=Load()),
                                    attr='_join_group',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='email', ctx=Load()),
                                    Name(id='partner_id', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='render',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='mail_group.confirmation_subscription', kind=None),
                                    Dict(
                                        keys=[
                                            Constant(value='group', kind=None),
                                            Constant(value='email', kind=None),
                                            Constant(value='subscribing', kind=None),
                                        ],
                                        values=[
                                            Name(id='group', ctx=Load()),
                                            Name(id='email', ctx=Load()),
                                            Constant(value=True, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[Constant(value='/group/subscribe-confirm', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='public', kind=None),
                                ),
                                keyword(
                                    arg='website',
                                    value=Constant(value=True, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='group_unsubscribe_confirm',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='group_id', annotation=None, type_comment=None),
                            arg(arg='email', annotation=None, type_comment=None),
                            arg(arg='token', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kw', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Confirm the subscribe / unsubscribe action which was sent by email.', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='group', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_group_subscription_confirm_get_group',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='group_id', ctx=Load()),
                                    Name(id='email', ctx=Load()),
                                    Name(id='token', ctx=Load()),
                                    Constant(value='unsubscribe', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='group', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='render',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='mail_group.invalid_token_subscription', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='group', ctx=Load()),
                                    attr='_leave_group',
                                    ctx=Load(),
                                ),
                                args=[Name(id='email', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='all_members',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='render',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='mail_group.confirmation_subscription', kind=None),
                                    Dict(
                                        keys=[
                                            Constant(value='group', kind=None),
                                            Constant(value='email', kind=None),
                                            Constant(value='subscribing', kind=None),
                                        ],
                                        values=[
                                            Name(id='group', ctx=Load()),
                                            Name(id='email', ctx=Load()),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[Constant(value='/group/unsubscribe-confirm', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='public', kind=None),
                                ),
                                keyword(
                                    arg='website',
                                    value=Constant(value=True, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_group_subscription_confirm_get_group',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='group_id', annotation=None, type_comment=None),
                            arg(arg='email', annotation=None, type_comment=None),
                            arg(arg='token', annotation=None, type_comment=None),
                            arg(arg='action', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Retrieve the group and check the token use to perform the given action.', kind=None),
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='group_id', ctx=Load()),
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='email', ctx=Load()),
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='token', ctx=Load()),
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='group', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='request', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='mail.group', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='browse',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Name(id='int', ctx=Load()),
                                                        args=[Name(id='group_id', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='exists',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='sudo',
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
                                operand=Name(id='group', ctx=Load()),
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='werkzeug', ctx=Load()),
                                                attr='exceptions',
                                                ctx=Load(),
                                            ),
                                            attr='NotFound',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='excepted_token', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='group', ctx=Load()),
                                    attr='_generate_action_token',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='email', ctx=Load()),
                                    Name(id='action', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=IfExp(
                                test=Compare(
                                    left=Name(id='token', ctx=Load()),
                                    ops=[Eq()],
                                    comparators=[Name(id='excepted_token', ctx=Load())],
                                ),
                                body=Name(id='group', ctx=Load()),
                                orelse=Constant(value=False, kind=None),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_generate_attachments_access_token',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='messages', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        For(
                            target=Name(id='message', ctx=Store()),
                            iter=Name(id='messages', ctx=Load()),
                            body=[
                                If(
                                    test=Attribute(
                                        value=Name(id='message', ctx=Load()),
                                        attr='attachment_ids',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='message', ctx=Load()),
                                                        attr='attachment_ids',
                                                        ctx=Load(),
                                                    ),
                                                    attr='generate_access_token',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_generate_attachments_access_token',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='message', ctx=Load()),
                                                attr='group_message_child_ids',
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
