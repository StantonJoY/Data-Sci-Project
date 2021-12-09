Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='tools', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[
                alias(name='AccessError', asname=None),
                alias(name='UserError', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='MailBlackListMixin',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='AbstractModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=" Mixin that is inherited by all model with opt out. This mixin stores a normalized\n    email based on primary_email field.\n\n    A normalized email is considered as :\n        - having a left part + @ + a right part (the domain can be without '.something')\n        - being lower case\n        - having no name before the address. Typically, having no 'Name <>'\n    Ex:\n        - Formatted Email : 'Name <NaMe@DoMaIn.CoM>'\n        - Normalized Email : 'name@domain.com'\n\n    The primary email field can be specified on the parent model, if it differs from the default one ('email')\n    The email_normalized field can than be used on that model to search quickly on emails (by simple comparison\n    and not using time consuming regex anymore).\n\n    Using this email_normalized field, blacklist status is computed.\n\n    Mail Thread capabilities are required for this mixin. ", kind=None),
                ),
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='mail.thread.blacklist', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=List(
                        elts=[Constant(value='mail.thread', kind=None)],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Mail Blacklist mixin', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_primary_email', ctx=Store())],
                    value=Constant(value='email', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='email_normalized', ctx=Store())],
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
                                value=Constant(value='Normalized Email', kind=None),
                            ),
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_email_normalized', kind=None),
                            ),
                            keyword(
                                arg='compute_sudo',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='invisible',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='This field is used to search on email address as the primary email field can contain more than strictly an email address.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='is_blacklisted', ctx=Store())],
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
                                value=Constant(value='Blacklist', kind=None),
                            ),
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_is_blacklisted', kind=None),
                            ),
                            keyword(
                                arg='compute_sudo',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='search',
                                value=Constant(value='_search_is_blacklisted', kind=None),
                            ),
                            keyword(
                                arg='groups',
                                value=Constant(value='base.group_user', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value="If the email address is on the blacklist, the contact won't receive mass mailing anymore, from any list", kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='message_bounce', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Bounce', kind=None)],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value='Counter of the number of bounced emails for this contact', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value=0, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_email_normalized',
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
                                    attr='_assert_primary_email',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        For(
                            target=Name(id='record', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='email_normalized',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='tools', ctx=Load()),
                                            attr='email_normalize',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='record', ctx=Load()),
                                                slice=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_primary_email',
                                                    ctx=Load(),
                                                ),
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
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[
                                Lambda(
                                    args=arguments(
                                        posonlyargs=[],
                                        args=[arg(arg='self', annotation=None, type_comment=None)],
                                        vararg=None,
                                        kwonlyargs=[],
                                        kw_defaults=[],
                                        kwarg=None,
                                        defaults=[],
                                    ),
                                    body=List(
                                        elts=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_primary_email',
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
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_search_is_blacklisted',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='operator', annotation=None, type_comment=None),
                            arg(arg='value', annotation=None, type_comment=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='flush',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='email_normalized', kind=None)],
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
                                        slice=Constant(value='mail.blacklist', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='flush',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='email', kind=None),
                                            Constant(value='active', kind=None),
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
                                    attr='_assert_primary_email',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Compare(
                                left=Name(id='operator', ctx=Load()),
                                ops=[NotEq()],
                                comparators=[Constant(value='=', kind=None)],
                            ),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Name(id='operator', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='!=', kind=None)],
                                            ),
                                            Call(
                                                func=Name(id='isinstance', ctx=Load()),
                                                args=[
                                                    Name(id='value', ctx=Load()),
                                                    Name(id='bool', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='value', ctx=Store())],
                                            value=UnaryOp(
                                                op=Not(),
                                                operand=Name(id='value', ctx=Load()),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='NotImplementedError', ctx=Load()),
                                                args=[],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Name(id='value', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='query', ctx=Store())],
                                    value=Constant(value='\n                SELECT m.id\n                    FROM mail_blacklist bl\n                    JOIN %s m\n                    ON m.email_normalized = bl.email AND bl.active\n            ', kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='query', ctx=Store())],
                                    value=Constant(value='\n                SELECT m.id\n                    FROM %s m\n                    LEFT JOIN mail_blacklist bl\n                    ON m.email_normalized = bl.email AND bl.active\n                    WHERE bl.id IS NULL\n            ', kind=None),
                                    type_comment=None,
                                ),
                            ],
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
                                        left=Name(id='query', ctx=Load()),
                                        op=Mod(),
                                        right=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_table',
                                            ctx=Load(),
                                        ),
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
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='res', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=0, kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value=1, kind=None),
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
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='id', kind=None),
                                            Constant(value='in', kind=None),
                                            ListComp(
                                                elt=Subscript(
                                                    value=Name(id='r', ctx=Load()),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='r', ctx=Store()),
                                                        iter=Name(id='res', ctx=Load()),
                                                        ifs=[],
                                                        is_async=0,
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
                    name='_compute_is_blacklisted',
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
                            targets=[Name(id='blacklist', ctx=Store())],
                            value=Call(
                                func=Name(id='set', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
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
                                                                slice=Constant(value='mail.blacklist', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='sudo',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    attr='search',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='email', kind=None),
                                                                    Constant(value='in', kind=None),
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='mapped',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Constant(value='email_normalized', kind=None)],
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
                                            attr='mapped',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='email', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='record', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='is_blacklisted',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Compare(
                                        left=Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='email_normalized',
                                            ctx=Load(),
                                        ),
                                        ops=[In()],
                                        comparators=[Name(id='blacklist', ctx=Load())],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[Constant(value='email_normalized', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_assert_primary_email',
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
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Name(id='hasattr', ctx=Load()),
                                            args=[
                                                Name(id='self', ctx=Load()),
                                                Constant(value='_primary_email', kind=None),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Name(id='isinstance', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_primary_email',
                                                    ctx=Load(),
                                                ),
                                                Name(id='str', ctx=Load()),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='UserError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[
                                                    Constant(value='Invalid primary email field on model %s', kind=None),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_name',
                                                        ctx=Load(),
                                                    ),
                                                ],
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
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_primary_email',
                                            ctx=Load(),
                                        ),
                                        ops=[NotIn()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_fields',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_fields',
                                                    ctx=Load(),
                                                ),
                                                slice=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_primary_email',
                                                    ctx=Load(),
                                                ),
                                                ctx=Load(),
                                            ),
                                            attr='type',
                                            ctx=Load(),
                                        ),
                                        ops=[NotEq()],
                                        comparators=[Constant(value='char', kind=None)],
                                    ),
                                ],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='UserError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[
                                                    Constant(value='Invalid primary email field on model %s', kind=None),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_name',
                                                        ctx=Load(),
                                                    ),
                                                ],
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_message_receive_bounce',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='email', annotation=None, type_comment=None),
                            arg(arg='partner', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Override of mail.thread generic method. Purpose is to increment the\n        bounce counter of the record. ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='MailBlackListMixin', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_message_receive_bounce',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='email', ctx=Load()),
                                    Name(id='partner', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        For(
                            target=Name(id='record', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='message_bounce',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BinOp(
                                        left=Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='message_bounce',
                                            ctx=Load(),
                                        ),
                                        op=Add(),
                                        right=Constant(value=1, kind=None),
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
                    name='_message_reset_bounce',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='email', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Override of mail.thread generic method. Purpose is to reset the\n        bounce counter of the record. ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='MailBlackListMixin', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_message_reset_bounce',
                                    ctx=Load(),
                                ),
                                args=[Name(id='email', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='message_bounce', kind=None)],
                                        values=[Constant(value=0, kind=None)],
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
                    name='mail_action_blacklist_remove',
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
                            targets=[Name(id='can_access', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.blacklist', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='check_access_rights',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='write', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='raise_exception',
                                        value=Constant(value=False, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='can_access', ctx=Load()),
                            body=[
                                Return(
                                    value=Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='type', kind=None),
                                            Constant(value='view_mode', kind=None),
                                            Constant(value='res_model', kind=None),
                                            Constant(value='target', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Are you sure you want to unblacklist this Email Address?', kind=None),
                                            Constant(value='ir.actions.act_window', kind=None),
                                            Constant(value='form', kind=None),
                                            Constant(value='mail.blacklist.remove', kind=None),
                                            Constant(value='new', kind=None),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='AccessError', ctx=Load()),
                                        args=[Constant(value='You do not have the access right to unblacklist emails. Please contact your administrator.', kind=None)],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
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
