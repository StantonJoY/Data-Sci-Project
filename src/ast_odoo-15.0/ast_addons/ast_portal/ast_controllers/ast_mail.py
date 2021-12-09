Module(
    body=[
        ImportFrom(
            module='werkzeug',
            names=[alias(name='urls', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='werkzeug.exceptions',
            names=[
                alias(name='NotFound', asname=None),
                alias(name='Forbidden', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='http', asname=None),
                alias(name='_', asname=None),
            ],
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
        ImportFrom(
            module='odoo.tools',
            names=[
                alias(name='consteq', asname=None),
                alias(name='plaintext2html', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.mail.controllers',
            names=[alias(name='mail', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.portal.controllers.portal',
            names=[alias(name='CustomerPortal', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[
                alias(name='AccessError', asname=None),
                alias(name='MissingError', asname=None),
                alias(name='UserError', asname=None),
            ],
            level=0,
        ),
        FunctionDef(
            name='_check_special_access',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='res_model', annotation=None, type_comment=None),
                    arg(arg='res_id', annotation=None, type_comment=None),
                    arg(arg='token', annotation=None, type_comment=None),
                    arg(arg='_hash', annotation=None, type_comment=None),
                    arg(arg='pid', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    Constant(value='', kind=None),
                    Constant(value='', kind=None),
                    Constant(value=False, kind=None),
                ],
            ),
            body=[
                Assign(
                    targets=[Name(id='record', ctx=Store())],
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
                                        slice=Name(id='res_model', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[Name(id='res_id', ctx=Load())],
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
                    test=Name(id='token', ctx=Load()),
                    body=[
                        Assign(
                            targets=[Name(id='token_field', ctx=Store())],
                            value=Attribute(
                                value=Subscript(
                                    value=Attribute(
                                        value=Name(id='request', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    slice=Name(id='res_model', ctx=Load()),
                                    ctx=Load(),
                                ),
                                attr='_mail_post_token_field',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='token', ctx=Load()),
                                    Name(id='record', ctx=Load()),
                                    Call(
                                        func=Name(id='consteq', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='record', ctx=Load()),
                                                slice=Name(id='token_field', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            Name(id='token', ctx=Load()),
                                        ],
                                        keywords=[],
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
                                    Name(id='_hash', ctx=Load()),
                                    Name(id='pid', ctx=Load()),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Name(id='consteq', ctx=Load()),
                                        args=[
                                            Name(id='_hash', ctx=Load()),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='record', ctx=Load()),
                                                    attr='_sign_token',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='pid', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='Forbidden', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    cause=None,
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
            name='_message_post_helper',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='res_model', annotation=None, type_comment=None),
                    arg(arg='res_id', annotation=None, type_comment=None),
                    arg(arg='message', annotation=None, type_comment=None),
                    arg(arg='token', annotation=None, type_comment=None),
                    arg(arg='_hash', annotation=None, type_comment=None),
                    arg(arg='pid', annotation=None, type_comment=None),
                    arg(arg='nosubscribe', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=arg(arg='kw', annotation=None, type_comment=None),
                defaults=[
                    Constant(value='', kind=None),
                    Constant(value=False, kind=None),
                    Constant(value=False, kind=None),
                    Constant(value=True, kind=None),
                ],
            ),
            body=[
                Expr(
                    value=Constant(value=" Generic chatter function, allowing to write on *any* object that inherits mail.thread. We\n        distinguish 2 cases:\n            1/ If a token is specified, all logged in users will be able to write a message regardless\n            of access rights; if the user is the public user, the message will be posted under the name\n            of the partner_id of the object (or the public user if there is no partner_id on the object).\n\n            2/ If a signed token is specified (`hash`) and also a partner_id (`pid`), all post message will\n            be done under the name of the partner_id (as it is signed). This should be used to avoid leaking\n            token to all users.\n\n        Required parameters\n        :param string res_model: model name of the object\n        :param int res_id: id of the object\n        :param string message: content of the message\n\n        Optional keywords arguments:\n        :param string token: access token if the object's model uses some kind of public access\n                             using tokens (usually a uuid4) to bypass access rules\n        :param string hash: signed token by a partner if model uses some token field to bypass access right\n                            post messages.\n        :param string pid: identifier of the res.partner used to sign the hash\n        :param bool nosubscribe: set False if you want the partner to be set as follower of the object when posting (default to True)\n\n        The rest of the kwargs are passed on to message_post()\n    ", kind=None),
                ),
                Assign(
                    targets=[Name(id='record', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Name(id='res_model', ctx=Load()),
                                ctx=Load(),
                            ),
                            attr='browse',
                            ctx=Load(),
                        ),
                        args=[Name(id='res_id', ctx=Load())],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=BoolOp(
                        op=Or(),
                        values=[
                            Name(id='token', ctx=Load()),
                            BoolOp(
                                op=And(),
                                values=[
                                    Name(id='_hash', ctx=Load()),
                                    Name(id='pid', ctx=Load()),
                                ],
                            ),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='pid', ctx=Store())],
                            value=IfExp(
                                test=Name(id='pid', ctx=Load()),
                                body=Call(
                                    func=Name(id='int', ctx=Load()),
                                    args=[Name(id='pid', ctx=Load())],
                                    keywords=[],
                                ),
                                orelse=Constant(value=False, kind=None),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Name(id='_check_special_access', ctx=Load()),
                                args=[
                                    Name(id='res_model', ctx=Load()),
                                    Name(id='res_id', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='token',
                                        value=Name(id='token', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='_hash',
                                        value=Name(id='_hash', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='pid',
                                        value=Name(id='pid', ctx=Load()),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='record', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='Forbidden', ctx=Load()),
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
                Assign(
                    targets=[Name(id='author_id', ctx=Store())],
                    value=IfExp(
                        test=Attribute(
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
                        body=Attribute(
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
                        orelse=Constant(value=False, kind=None),
                    ),
                    type_comment=None,
                ),
                If(
                    test=Name(id='token', ctx=Load()),
                    body=[
                        If(
                            test=Call(
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
                            body=[
                                Assign(
                                    targets=[Name(id='author_id', ctx=Store())],
                                    value=IfExp(
                                        test=BoolOp(
                                            op=And(),
                                            values=[
                                                Call(
                                                    func=Name(id='hasattr', ctx=Load()),
                                                    args=[
                                                        Name(id='record', ctx=Load()),
                                                        Constant(value='partner_id', kind=None),
                                                    ],
                                                    keywords=[],
                                                ),
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='record', ctx=Load()),
                                                        attr='partner_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                        body=Attribute(
                                            value=Attribute(
                                                value=Name(id='record', ctx=Load()),
                                                attr='partner_id',
                                                ctx=Load(),
                                            ),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        orelse=Name(id='author_id', ctx=Load()),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='author_id', ctx=Load()),
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='NotFound', ctx=Load()),
                                                args=[],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                        ),
                    ],
                    orelse=[
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='_hash', ctx=Load()),
                                    Name(id='pid', ctx=Load()),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='author_id', ctx=Store())],
                                    value=Name(id='pid', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                ),
                Assign(
                    targets=[Name(id='email_from', ctx=Store())],
                    value=Constant(value=None, kind=None),
                    type_comment=None,
                ),
                If(
                    test=BoolOp(
                        op=And(),
                        values=[
                            Name(id='author_id', ctx=Load()),
                            Compare(
                                left=Constant(value='email_from', kind=None),
                                ops=[NotIn()],
                                comparators=[Name(id='kw', ctx=Load())],
                            ),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='partner', ctx=Store())],
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
                                                slice=Constant(value='res.partner', kind=None),
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
                                args=[Name(id='author_id', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='email_from', ctx=Store())],
                            value=IfExp(
                                test=Attribute(
                                    value=Name(id='partner', ctx=Load()),
                                    attr='email',
                                    ctx=Load(),
                                ),
                                body=Attribute(
                                    value=Name(id='partner', ctx=Load()),
                                    attr='email_formatted',
                                    ctx=Load(),
                                ),
                                orelse=Constant(value=None, kind=None),
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    targets=[Name(id='message_post_args', ctx=Store())],
                    value=Call(
                        func=Name(id='dict', ctx=Load()),
                        args=[],
                        keywords=[
                            keyword(
                                arg='body',
                                value=Name(id='message', ctx=Load()),
                            ),
                            keyword(
                                arg='message_type',
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='kw', ctx=Load()),
                                        attr='pop',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Constant(value='message_type', kind=None),
                                        Constant(value='comment', kind=None),
                                    ],
                                    keywords=[],
                                ),
                            ),
                            keyword(
                                arg='subtype_xmlid',
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='kw', ctx=Load()),
                                        attr='pop',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Constant(value='subtype_xmlid', kind=None),
                                        Constant(value='mail.mt_comment', kind=None),
                                    ],
                                    keywords=[],
                                ),
                            ),
                            keyword(
                                arg='author_id',
                                value=Name(id='author_id', ctx=Load()),
                            ),
                            keyword(
                                arg=None,
                                value=Name(id='kw', ctx=Load()),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                If(
                    test=Name(id='email_from', ctx=Load()),
                    body=[
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='message_post_args', ctx=Load()),
                                    slice=Constant(value='email_from', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='email_from', ctx=Load()),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Call(
                        func=Attribute(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='record', ctx=Load()),
                                    attr='with_context',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='mail_create_nosubscribe',
                                        value=Name(id='nosubscribe', ctx=Load()),
                                    ),
                                ],
                            ),
                            attr='message_post',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg=None,
                                value=Name(id='message_post_args', ctx=Load()),
                            ),
                        ],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        ClassDef(
            name='PortalChatter',
            bases=[
                Attribute(
                    value=Name(id='http', ctx=Load()),
                    attr='Controller',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                FunctionDef(
                    name='_portal_post_filter_params',
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
                                    Constant(value='token', kind=None),
                                    Constant(value='hash', kind=None),
                                    Constant(value='pid', kind=None),
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
                    name='_portal_post_check_attachments',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='attachment_ids', annotation=None, type_comment=None),
                            arg(arg='attachment_tokens', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=Compare(
                                left=Call(
                                    func=Name(id='len', ctx=Load()),
                                    args=[Name(id='attachment_tokens', ctx=Load())],
                                    keywords=[],
                                ),
                                ops=[NotEq()],
                                comparators=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='attachment_ids', ctx=Load())],
                                        keywords=[],
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
                                                args=[Constant(value='An access token must be provided for each attachment.', kind=None)],
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
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='attachment_id', ctx=Store()),
                                    Name(id='access_token', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Name(id='zip', ctx=Load()),
                                args=[
                                    Name(id='attachment_ids', ctx=Load()),
                                    Name(id='attachment_tokens', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Try(
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='CustomerPortal', ctx=Load()),
                                                    attr='_document_check_access',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='self', ctx=Load()),
                                                    Constant(value='ir.attachment', kind=None),
                                                    Name(id='attachment_id', ctx=Load()),
                                                    Name(id='access_token', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Tuple(
                                                elts=[
                                                    Name(id='AccessError', ctx=Load()),
                                                    Name(id='MissingError', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            name=None,
                                            body=[
                                                Raise(
                                                    exc=Call(
                                                        func=Name(id='UserError', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                func=Name(id='_', ctx=Load()),
                                                                args=[
                                                                    Constant(value='The attachment %s does not exist or you do not have the rights to access it.', kind=None),
                                                                    Name(id='attachment_id', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
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
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='portal_chatter_post',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='res_model', annotation=None, type_comment=None),
                            arg(arg='res_id', annotation=None, type_comment=None),
                            arg(arg='message', annotation=None, type_comment=None),
                            arg(arg='attachment_ids', annotation=None, type_comment=None),
                            arg(arg='attachment_tokens', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kw', annotation=None, type_comment=None),
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Create a new `mail.message` with the given `message` and/or `attachment_ids` and return new message values.\n\n        The message will be associated to the record `res_id` of the model\n        `res_model`. The user must have access rights on this target document or\n        must provide valid identifiers through `kw`. See `_message_post_helper`.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='res_id', ctx=Store())],
                            value=Call(
                                func=Name(id='int', ctx=Load()),
                                args=[Name(id='res_id', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_portal_post_check_attachments',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='attachment_ids', ctx=Load()),
                                    Name(id='attachment_tokens', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='message', ctx=Load()),
                                    Name(id='attachment_ids', ctx=Load()),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='result', ctx=Store())],
                                    value=Dict(
                                        keys=[Constant(value='default_message', kind=None)],
                                        values=[Name(id='message', ctx=Load())],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='message', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='message', ctx=Store())],
                                            value=Call(
                                                func=Name(id='plaintext2html', ctx=Load()),
                                                args=[Name(id='message', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='post_values', ctx=Store())],
                                    value=Dict(
                                        keys=[
                                            Constant(value='res_model', kind=None),
                                            Constant(value='res_id', kind=None),
                                            Constant(value='message', kind=None),
                                            Constant(value='send_after_commit', kind=None),
                                            Constant(value='attachment_ids', kind=None),
                                        ],
                                        values=[
                                            Name(id='res_model', ctx=Load()),
                                            Name(id='res_id', ctx=Load()),
                                            Name(id='message', ctx=Load()),
                                            Constant(value=False, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='post_values', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            GeneratorExp(
                                                elt=Tuple(
                                                    elts=[
                                                        Name(id='fname', ctx=Load()),
                                                        Call(
                                                            func=Attribute(
                                                                value=Name(id='kw', ctx=Load()),
                                                                attr='get',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Name(id='fname', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='fname', ctx=Store()),
                                                        iter=Call(
                                                            func=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='_portal_post_filter_params',
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
                                Assign(
                                    targets=[Name(id='message', ctx=Store())],
                                    value=Call(
                                        func=Name(id='_message_post_helper', ctx=Load()),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg=None,
                                                value=Name(id='post_values', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='result', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='default_message_id', kind=None)],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='message', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                If(
                                    test=Name(id='attachment_ids', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='record', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='request', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Name(id='res_model', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                    attr='browse',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='res_id', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='message_values', ctx=Store())],
                                            value=Dict(
                                                keys=[
                                                    Constant(value='res_id', kind=None),
                                                    Constant(value='model', kind=None),
                                                ],
                                                values=[
                                                    Name(id='res_id', ctx=Load()),
                                                    Name(id='res_model', ctx=Load()),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='attachments', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='record', ctx=Load()),
                                                    attr='_message_post_process_attachments',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(elts=[], ctx=Load()),
                                                    Name(id='attachment_ids', ctx=Load()),
                                                    Name(id='message_values', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Call(
                                                func=Attribute(
                                                    value=Name(id='attachments', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='attachment_ids', kind=None)],
                                                keywords=[],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='message', ctx=Load()),
                                                                    attr='sudo',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                            attr='write',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='attachments', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='result', ctx=Load()),
                                                    attr='update',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[Constant(value='default_attachment_ids', kind=None)],
                                                        values=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='message', ctx=Load()),
                                                                                attr='attachment_ids',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='sudo',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[],
                                                                        keywords=[],
                                                                    ),
                                                                    attr='read',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    List(
                                                                        elts=[
                                                                            Constant(value='id', kind=None),
                                                                            Constant(value='name', kind=None),
                                                                            Constant(value='mimetype', kind=None),
                                                                            Constant(value='file_size', kind=None),
                                                                            Constant(value='access_token', kind=None),
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
                                ),
                                Return(
                                    value=Name(id='result', ctx=Load()),
                                ),
                            ],
                            orelse=[],
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
                                    elts=[Constant(value='/mail/chatter_post', kind=None)],
                                    ctx=Load(),
                                ),
                            ],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='json', kind=None),
                                ),
                                keyword(
                                    arg='methods',
                                    value=List(
                                        elts=[Constant(value='POST', kind=None)],
                                        ctx=Load(),
                                    ),
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
                    name='portal_chatter_init',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='res_model', annotation=None, type_comment=None),
                            arg(arg='res_id', annotation=None, type_comment=None),
                            arg(arg='domain', annotation=None, type_comment=None),
                            arg(arg='limit', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[
                            Constant(value=False, kind=None),
                            Constant(value=False, kind=None),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='is_user_public', ctx=Store())],
                            value=Call(
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
                                args=[Constant(value='base.group_public', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='message_data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='portal_message_fetch',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='res_model', ctx=Load()),
                                    Name(id='res_id', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='domain',
                                        value=Name(id='domain', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='limit',
                                        value=Name(id='limit', ctx=Load()),
                                    ),
                                    keyword(
                                        arg=None,
                                        value=Name(id='kwargs', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='display_composer', ctx=Store())],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='kwargs', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='allow_composer', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='display_composer', ctx=Store())],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='kwargs', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='token', kind=None)],
                                                keywords=[],
                                            ),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Name(id='is_user_public', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='messages', kind=None),
                                    Constant(value='options', kind=None),
                                ],
                                values=[
                                    Subscript(
                                        value=Name(id='message_data', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='message_count', kind=None),
                                            Constant(value='is_user_public', kind=None),
                                            Constant(value='is_user_employee', kind=None),
                                            Constant(value='is_user_publisher', kind=None),
                                            Constant(value='display_composer', kind=None),
                                            Constant(value='partner_id', kind=None),
                                        ],
                                        values=[
                                            Subscript(
                                                value=Name(id='message_data', ctx=Load()),
                                                slice=Constant(value='message_count', kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='is_user_public', ctx=Load()),
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
                                                args=[Constant(value='base.group_user', kind=None)],
                                                keywords=[],
                                            ),
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
                                                args=[Constant(value='website.group_website_publisher', kind=None)],
                                                keywords=[],
                                            ),
                                            Name(id='display_composer', ctx=Load()),
                                            Attribute(
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
                                        ],
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
                            args=[Constant(value='/mail/chatter_init', kind=None)],
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
                    name='portal_message_fetch',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='res_model', annotation=None, type_comment=None),
                            arg(arg='res_id', annotation=None, type_comment=None),
                            arg(arg='domain', annotation=None, type_comment=None),
                            arg(arg='limit', annotation=None, type_comment=None),
                            arg(arg='offset', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kw', annotation=None, type_comment=None),
                        defaults=[
                            Constant(value=False, kind=None),
                            Constant(value=10, kind=None),
                            Constant(value=0, kind=None),
                        ],
                    ),
                    body=[
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='domain', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='domain', ctx=Store())],
                                    value=List(elts=[], ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='model', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Name(id='res_model', ctx=Load()),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='field', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='model', ctx=Load()),
                                    attr='_fields',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='website_message_ids', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='field_domain', ctx=Store())],
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
                                            Name(id='field_domain', ctx=Load()),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='res_id', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Name(id='res_id', ctx=Load()),
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
                            targets=[Name(id='Message', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='mail.message', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='kw', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='token', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='access_as_sudo', ctx=Store())],
                                    value=Call(
                                        func=Name(id='_check_special_access', ctx=Load()),
                                        args=[
                                            Name(id='res_model', ctx=Load()),
                                            Name(id='res_id', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='token',
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='kw', ctx=Load()),
                                                        attr='get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='token', kind=None)],
                                                    keywords=[],
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='access_as_sudo', ctx=Load()),
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='Forbidden', ctx=Load()),
                                                args=[],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='request', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='res.users', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='has_group',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='base.group_user', kind=None)],
                                            keywords=[],
                                        ),
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
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='Message', ctx=Load()),
                                                                    attr='_get_search_domain_share',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                            Name(id='domain', ctx=Load()),
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
                                    targets=[Name(id='Message', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='mail.message', kind=None),
                                                ctx=Load(),
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
                            orelse=[],
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='messages', kind=None),
                                    Constant(value='message_count', kind=None),
                                ],
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='Message', ctx=Load()),
                                                    attr='search',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='domain', ctx=Load())],
                                                keywords=[
                                                    keyword(
                                                        arg='limit',
                                                        value=Name(id='limit', ctx=Load()),
                                                    ),
                                                    keyword(
                                                        arg='offset',
                                                        value=Name(id='offset', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                            attr='portal_message_format',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='Message', ctx=Load()),
                                            attr='search_count',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='domain', ctx=Load())],
                                        keywords=[],
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
                            args=[Constant(value='/mail/chatter_fetch', kind=None)],
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
                    name='portal_message_update_is_internal',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='message_id', annotation=None, type_comment=None),
                            arg(arg='is_internal', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='message', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.message', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='int', ctx=Load()),
                                        args=[Name(id='message_id', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='message', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='is_internal', kind=None)],
                                        values=[Name(id='is_internal', ctx=Load())],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Attribute(
                                value=Name(id='message', ctx=Load()),
                                attr='is_internal',
                                ctx=Load(),
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
                                    elts=[Constant(value='/mail/update_is_internal', kind=None)],
                                    ctx=Load(),
                                ),
                            ],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='json', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='user', kind=None),
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
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='MailController',
            bases=[
                Attribute(
                    value=Name(id='mail', ctx=Load()),
                    attr='MailController',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                FunctionDef(
                    name='_redirect_to_record',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='cls', annotation=None, type_comment=None),
                            arg(arg='model', annotation=None, type_comment=None),
                            arg(arg='res_id', annotation=None, type_comment=None),
                            arg(arg='access_token', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" If the current user doesn't have access to the document, but provided\n        a valid access token, redirect him to the front-end view.\n        If the partner_id and hash parameters are given, add those parameters to the redirect url\n        to authentify the recipient in the chatter, if any.\n\n        :param model: the model name of the record that will be visualized\n        :param res_id: the id of the record\n        :param access_token: token that gives access to the record\n            bypassing the rights and rules restriction of the user.\n        :param kwargs: Typically, it can receive a partner_id and a hash (sign_token).\n            If so, those two parameters are used to authentify the recipient in the chatter, if any.\n        :return:\n        ", kind=None),
                        ),
                        If(
                            test=Call(
                                func=Name(id='issubclass', ctx=Load()),
                                args=[
                                    Call(
                                        func=Name(id='type', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Name(id='model', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Subscript(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='request', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='registry',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='portal.mixin', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='uid', ctx=Store())],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='session',
                                                    ctx=Load(),
                                                ),
                                                attr='uid',
                                                ctx=Load(),
                                            ),
                                            Attribute(
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
                                                    args=[Constant(value='base.public_user', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='record_sudo', ctx=Store())],
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
                                                                slice=Name(id='model', ctx=Load()),
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
                                                args=[Name(id='res_id', ctx=Load())],
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
                                Try(
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='record_sudo', ctx=Load()),
                                                            attr='with_user',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='uid', ctx=Load())],
                                                        keywords=[],
                                                    ),
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
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='record_sudo', ctx=Load()),
                                                            attr='with_user',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='uid', ctx=Load())],
                                                        keywords=[],
                                                    ),
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
                                                If(
                                                    test=BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='record_sudo', ctx=Load()),
                                                                attr='access_token',
                                                                ctx=Load(),
                                                            ),
                                                            Name(id='access_token', ctx=Load()),
                                                            Call(
                                                                func=Name(id='consteq', ctx=Load()),
                                                                args=[
                                                                    Attribute(
                                                                        value=Name(id='record_sudo', ctx=Load()),
                                                                        attr='access_token',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Name(id='access_token', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='record_action', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='record_sudo', ctx=Load()),
                                                                            attr='with_context',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[],
                                                                        keywords=[
                                                                            keyword(
                                                                                arg='force_website',
                                                                                value=Constant(value=True, kind=None),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                    attr='get_access_action',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        If(
                                                            test=Compare(
                                                                left=Subscript(
                                                                    value=Name(id='record_action', ctx=Load()),
                                                                    slice=Constant(value='type', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='ir.actions.act_url', kind=None)],
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='pid', ctx=Store())],
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='kwargs', ctx=Load()),
                                                                            attr='get',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Constant(value='pid', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                                Assign(
                                                                    targets=[Name(id='hash', ctx=Store())],
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='kwargs', ctx=Load()),
                                                                            attr='get',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Constant(value='hash', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                                Assign(
                                                                    targets=[Name(id='url', ctx=Store())],
                                                                    value=Subscript(
                                                                        value=Name(id='record_action', ctx=Load()),
                                                                        slice=Constant(value='url', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                                If(
                                                                    test=BoolOp(
                                                                        op=And(),
                                                                        values=[
                                                                            Name(id='pid', ctx=Load()),
                                                                            Name(id='hash', ctx=Load()),
                                                                        ],
                                                                    ),
                                                                    body=[
                                                                        Assign(
                                                                            targets=[Name(id='url', ctx=Store())],
                                                                            value=Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='urls', ctx=Load()),
                                                                                    attr='url_parse',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[Name(id='url', ctx=Load())],
                                                                                keywords=[],
                                                                            ),
                                                                            type_comment=None,
                                                                        ),
                                                                        Assign(
                                                                            targets=[Name(id='url_params', ctx=Store())],
                                                                            value=Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='url', ctx=Load()),
                                                                                    attr='decode_query',
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
                                                                                    value=Name(id='url_params', ctx=Load()),
                                                                                    attr='update',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[
                                                                                    List(
                                                                                        elts=[
                                                                                            Tuple(
                                                                                                elts=[
                                                                                                    Constant(value='pid', kind=None),
                                                                                                    Name(id='pid', ctx=Load()),
                                                                                                ],
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Tuple(
                                                                                                elts=[
                                                                                                    Constant(value='hash', kind=None),
                                                                                                    Name(id='hash', ctx=Load()),
                                                                                                ],
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
                                                                            targets=[Name(id='url', ctx=Store())],
                                                                            value=Call(
                                                                                func=Attribute(
                                                                                    value=Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='url', ctx=Load()),
                                                                                            attr='replace',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[],
                                                                                        keywords=[
                                                                                            keyword(
                                                                                                arg='query',
                                                                                                value=Call(
                                                                                                    func=Attribute(
                                                                                                        value=Name(id='urls', ctx=Load()),
                                                                                                        attr='url_encode',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    args=[Name(id='url_params', ctx=Load())],
                                                                                                    keywords=[],
                                                                                                ),
                                                                                            ),
                                                                                        ],
                                                                                    ),
                                                                                    attr='to_url',
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
                                                                Return(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='request', ctx=Load()),
                                                                            attr='redirect',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Name(id='url', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
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
                                    orelse=[],
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
                                            Name(id='MailController', ctx=Load()),
                                            Name(id='cls', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_redirect_to_record',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='model', ctx=Load()),
                                    Name(id='res_id', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='access_token',
                                        value=Name(id='access_token', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
