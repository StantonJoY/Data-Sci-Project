Module(
    body=[
        Import(
            names=[alias(name='uuid', asname=None)],
        ),
        ImportFrom(
            module='werkzeug.urls',
            names=[alias(name='url_encode', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='exceptions', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='PortalMixin',
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
                    value=Constant(value='portal.mixin', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Portal Mixin', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='access_url', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Portal Access URL', kind=None)],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_access_url', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Customer Portal URL', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='access_token', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Security Token', kind=None)],
                        keywords=[
                            keyword(
                                arg='copy',
                                value=Constant(value=False, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='access_warning', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Text',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Access warning', kind=None)],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_access_warning', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_access_warning',
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
                            target=Name(id='mixin', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='mixin', ctx=Load()),
                                            attr='access_warning',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value='', kind=None),
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
                    name='_compute_access_url',
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
                            target=Name(id='record', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='access_url',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value='#', kind=None),
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
                    name='_portal_ensure_token',
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
                            value=Constant(value=' Get the current record access token ', kind=None),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='access_token',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='access_token', kind=None)],
                                                values=[
                                                    Call(
                                                        func=Name(id='str', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='uuid', ctx=Load()),
                                                                    attr='uuid4',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
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
                        ),
                        Return(
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='access_token',
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_share_url',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='redirect', annotation=None, type_comment=None),
                            arg(arg='signup_partner', annotation=None, type_comment=None),
                            arg(arg='pid', annotation=None, type_comment=None),
                            arg(arg='share_token', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=False, kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=True, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value="\n        Build the url of the record  that will be sent by mail and adds additional parameters such as\n        access_token to bypass the recipient's rights,\n        signup_partner to allows the user to create easily an account,\n        hash token to allow the user to be authenticated in the chatter of the record portal view, if applicable\n        :param redirect : Send the redirect url instead of the direct portal share url\n        :param signup_partner: allows the user to create an account with pre-filled fields.\n        :param pid: = partner_id - when given, a hash is generated to allow the user to be authenticated\n            in the portal chatter, if any in the target page,\n            if the user is redirected to the portal instead of the backend.\n        :return: the url of the record with access parameters, if any.\n        ", kind=None),
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
                            targets=[Name(id='params', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='model', kind=None),
                                    Constant(value='res_id', kind=None),
                                ],
                                values=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_name',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='share_token', ctx=Load()),
                                    Call(
                                        func=Name(id='hasattr', ctx=Load()),
                                        args=[
                                            Name(id='self', ctx=Load()),
                                            Constant(value='access_token', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='params', ctx=Load()),
                                            slice=Constant(value='access_token', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_portal_ensure_token',
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
                        If(
                            test=Name(id='pid', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='params', ctx=Load()),
                                            slice=Constant(value='pid', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='pid', ctx=Load()),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='params', ctx=Load()),
                                            slice=Constant(value='hash', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_sign_token',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='pid', ctx=Load())],
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
                                    Name(id='signup_partner', ctx=Load()),
                                    Call(
                                        func=Name(id='hasattr', ctx=Load()),
                                        args=[
                                            Name(id='self', ctx=Load()),
                                            Constant(value='partner_id', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='partner_id',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='params', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='partner_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='signup_get_auth_param',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                slice=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='partner_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
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
                        Return(
                            value=BinOp(
                                left=Constant(value='%s?%s', kind=None),
                                op=Mod(),
                                right=Tuple(
                                    elts=[
                                        IfExp(
                                            test=Name(id='redirect', ctx=Load()),
                                            body=Constant(value='/mail/view', kind=None),
                                            orelse=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='access_url',
                                                ctx=Load(),
                                            ),
                                        ),
                                        Call(
                                            func=Name(id='url_encode', ctx=Load()),
                                            args=[Name(id='params', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_notify_get_groups',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='msg_vals', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='access_token', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_portal_ensure_token',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='groups', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='PortalMixin', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_notify_get_groups',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='msg_vals',
                                        value=Name(id='msg_vals', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='local_msg_vals', ctx=Store())],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Name(id='msg_vals', ctx=Load()),
                                            Dict(keys=[], values=[]),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='access_token', ctx=Load()),
                                    Compare(
                                        left=Constant(value='partner_id', kind=None),
                                        ops=[In()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_fields',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Subscript(
                                        value=Name(id='self', ctx=Load()),
                                        slice=Constant(value='partner_id', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='customer', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='self', ctx=Load()),
                                        slice=Constant(value='partner_id', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='local_msg_vals', ctx=Load()),
                                            slice=Constant(value='access_token', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='access_token',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='local_msg_vals', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='customer', ctx=Load()),
                                                        attr='signup_get_auth_param',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                slice=Attribute(
                                                    value=Name(id='customer', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='access_link', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_notify_get_action_link',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='view', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg=None,
                                                value=Name(id='local_msg_vals', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='new_group', ctx=Store())],
                                    value=List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='portal_customer', kind=None),
                                                    Lambda(
                                                        args=arguments(
                                                            posonlyargs=[],
                                                            args=[arg(arg='pdata', annotation=None, type_comment=None)],
                                                            vararg=None,
                                                            kwonlyargs=[],
                                                            kw_defaults=[],
                                                            kwarg=None,
                                                            defaults=[],
                                                        ),
                                                        body=Compare(
                                                            left=Subscript(
                                                                value=Name(id='pdata', ctx=Load()),
                                                                slice=Constant(value='id', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            ops=[Eq()],
                                                            comparators=[
                                                                Attribute(
                                                                    value=Name(id='customer', ctx=Load()),
                                                                    attr='id',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                        ),
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='has_button_access', kind=None),
                                                            Constant(value='button_access', kind=None),
                                                            Constant(value='notification_is_customer', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value=False, kind=None),
                                                            Dict(
                                                                keys=[Constant(value='url', kind=None)],
                                                                values=[Name(id='access_link', ctx=Load())],
                                                            ),
                                                            Constant(value=True, kind=None),
                                                        ],
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
                                Assign(
                                    targets=[Name(id='new_group', ctx=Store())],
                                    value=List(elts=[], ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Return(
                            value=BinOp(
                                left=Name(id='new_group', ctx=Load()),
                                op=Add(),
                                right=Name(id='groups', ctx=Load()),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_access_action',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='access_uid', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Instead of the classic form view, redirect to the online document for\n        portal users or if force_website=True in the context. ', kind=None),
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
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='user', ctx=Store()),
                                        Name(id='record', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Tuple(
                                elts=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='user',
                                        ctx=Load(),
                                    ),
                                    Name(id='self', ctx=Load()),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='access_uid', ctx=Load()),
                            body=[
                                Try(
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='record', ctx=Load()),
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
                                                    value=Name(id='record', ctx=Load()),
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
                                            type=Attribute(
                                                value=Name(id='exceptions', ctx=Load()),
                                                attr='AccessError',
                                                ctx=Load(),
                                            ),
                                            name=None,
                                            body=[
                                                Return(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Name(id='super', ctx=Load()),
                                                                args=[
                                                                    Name(id='PortalMixin', ctx=Load()),
                                                                    Name(id='self', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            attr='get_access_action',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='access_uid', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                    finalbody=[],
                                ),
                                Assign(
                                    targets=[Name(id='user', ctx=Store())],
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
                                                        slice=Constant(value='res.users', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='access_uid', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='record', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='with_user',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='user', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Attribute(
                                        value=Name(id='user', ctx=Load()),
                                        attr='share',
                                        ctx=Load(),
                                    ),
                                    Call(
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
                                        args=[Constant(value='force_website', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Try(
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='record', ctx=Load()),
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
                                                    value=Name(id='record', ctx=Load()),
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
                                            type=Attribute(
                                                value=Name(id='exceptions', ctx=Load()),
                                                attr='AccessError',
                                                ctx=Load(),
                                            ),
                                            name=None,
                                            body=[
                                                If(
                                                    test=Call(
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
                                                        args=[Constant(value='force_website', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    body=[
                                                        Return(
                                                            value=Dict(
                                                                keys=[
                                                                    Constant(value='type', kind=None),
                                                                    Constant(value='url', kind=None),
                                                                    Constant(value='target', kind=None),
                                                                    Constant(value='res_id', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='ir.actions.act_url', kind=None),
                                                                    Attribute(
                                                                        value=Name(id='record', ctx=Load()),
                                                                        attr='access_url',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value='self', kind=None),
                                                                    Attribute(
                                                                        value=Name(id='record', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[Pass()],
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[
                                        Return(
                                            value=Dict(
                                                keys=[
                                                    Constant(value='type', kind=None),
                                                    Constant(value='url', kind=None),
                                                    Constant(value='target', kind=None),
                                                    Constant(value='res_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='ir.actions.act_url', kind=None),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='record', ctx=Load()),
                                                            attr='_get_share_url',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    Constant(value='self', kind=None),
                                                    Attribute(
                                                        value=Name(id='record', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                    finalbody=[],
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
                                            Name(id='PortalMixin', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='get_access_action',
                                    ctx=Load(),
                                ),
                                args=[Name(id='access_uid', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='action_share',
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
                                args=[Constant(value='portal.portal_share_action', kind=None)],
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
                            value=Dict(
                                keys=[
                                    Constant(value='active_id', kind=None),
                                    Constant(value='active_model', kind=None),
                                ],
                                values=[
                                    Subscript(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='context',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='active_id', kind=None),
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='context',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='active_model', kind=None),
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
                    name='get_portal_url',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='suffix', annotation=None, type_comment=None),
                            arg(arg='report_type', annotation=None, type_comment=None),
                            arg(arg='download', annotation=None, type_comment=None),
                            arg(arg='query_string', annotation=None, type_comment=None),
                            arg(arg='anchor', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n            Get a portal url for this model, including access_token.\n            The associated route must handle the flags for them to have any effect.\n            - suffix: string to append to the url, before the query string\n            - report_type: report_type query string, often one of: html, pdf, text\n            - download: set the download query string to true\n            - query_string: additional query string\n            - anchor: string to append after the anchor #\n        ', kind=None),
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
                            targets=[Name(id='url', ctx=Store())],
                            value=BinOp(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='access_url',
                                    ctx=Load(),
                                ),
                                op=Add(),
                                right=BinOp(
                                    left=Constant(value='%s?access_token=%s%s%s%s%s', kind=None),
                                    op=Mod(),
                                    right=Tuple(
                                        elts=[
                                            IfExp(
                                                test=Name(id='suffix', ctx=Load()),
                                                body=Name(id='suffix', ctx=Load()),
                                                orelse=Constant(value='', kind=None),
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_portal_ensure_token',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            IfExp(
                                                test=Name(id='report_type', ctx=Load()),
                                                body=BinOp(
                                                    left=Constant(value='&report_type=%s', kind=None),
                                                    op=Mod(),
                                                    right=Name(id='report_type', ctx=Load()),
                                                ),
                                                orelse=Constant(value='', kind=None),
                                            ),
                                            IfExp(
                                                test=Name(id='download', ctx=Load()),
                                                body=Constant(value='&download=true', kind=None),
                                                orelse=Constant(value='', kind=None),
                                            ),
                                            IfExp(
                                                test=Name(id='query_string', ctx=Load()),
                                                body=Name(id='query_string', ctx=Load()),
                                                orelse=Constant(value='', kind=None),
                                            ),
                                            IfExp(
                                                test=Name(id='anchor', ctx=Load()),
                                                body=BinOp(
                                                    left=Constant(value='#%s', kind=None),
                                                    op=Mod(),
                                                    right=Name(id='anchor', ctx=Load()),
                                                ),
                                                orelse=Constant(value='', kind=None),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='url', ctx=Load()),
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
