Module(
    body=[
        Import(
            names=[alias(name='ipaddress', asname=None)],
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='_', asname=None),
                alias(name='SUPERUSER_ID', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.http',
            names=[alias(name='request', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.web.controllers',
            names=[alias(name='main', asname='web')],
            level=0,
        ),
        FunctionDef(
            name='_admin_password_warn',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='uid', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Admin still has `admin` password, flash a message via chatter.\n\n    Uses a private mail.channel from the system (/ odoobot) to the user, as\n    using a more generic mail.thread could send an email which is undesirable\n\n    Uses mail.channel directly because using mail.thread might send an email instead.\n    ', kind=None),
                ),
                If(
                    test=Compare(
                        left=Subscript(
                            value=Attribute(
                                value=Name(id='request', ctx=Load()),
                                attr='params',
                                ctx=Load(),
                            ),
                            slice=Constant(value='password', kind=None),
                            ctx=Load(),
                        ),
                        ops=[NotEq()],
                        comparators=[Constant(value='admin', kind=None)],
                    ),
                    body=[Return(value=None)],
                    orelse=[],
                ),
                If(
                    test=Attribute(
                        value=Call(
                            func=Attribute(
                                value=Name(id='ipaddress', ctx=Load()),
                                attr='ip_address',
                                ctx=Load(),
                            ),
                            args=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='request', ctx=Load()),
                                        attr='httprequest',
                                        ctx=Load(),
                                    ),
                                    attr='remote_addr',
                                    ctx=Load(),
                                ),
                            ],
                            keywords=[],
                        ),
                        attr='is_private',
                        ctx=Load(),
                    ),
                    body=[Return(value=None)],
                    orelse=[],
                ),
                Assign(
                    targets=[Name(id='env', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='request', ctx=Load()),
                            attr='env',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='user',
                                value=Name(id='SUPERUSER_ID', ctx=Load()),
                            ),
                            keyword(
                                arg='su',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='admin', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='env', ctx=Load()),
                            attr='ref',
                            ctx=Load(),
                        ),
                        args=[Constant(value='base.partner_admin', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=Compare(
                        left=Name(id='uid', ctx=Load()),
                        ops=[NotIn()],
                        comparators=[
                            Attribute(
                                value=Attribute(
                                    value=Name(id='admin', ctx=Load()),
                                    attr='user_ids',
                                    ctx=Load(),
                                ),
                                attr='ids',
                                ctx=Load(),
                            ),
                        ],
                    ),
                    body=[Return(value=None)],
                    orelse=[],
                ),
                Assign(
                    targets=[Name(id='has_demo', ctx=Store())],
                    value=Call(
                        func=Name(id='bool', ctx=Load()),
                        args=[
                            Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Name(id='env', ctx=Load()),
                                        slice=Constant(value='ir.module.module', kind=None),
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
                                                    Constant(value='demo', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value=True, kind=None),
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
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=Name(id='has_demo', ctx=Load()),
                    body=[Return(value=None)],
                    orelse=[],
                ),
                Assign(
                    targets=[Name(id='user', ctx=Store())],
                    value=Subscript(
                        value=Call(
                            func=Attribute(
                                value=Name(id='request', ctx=Load()),
                                attr='env',
                                ctx=Load(),
                            ),
                            args=[],
                            keywords=[
                                keyword(
                                    arg='user',
                                    value=Name(id='uid', ctx=Load()),
                                ),
                            ],
                        ),
                        slice=Constant(value='res.users', kind=None),
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='MailChannel', ctx=Store())],
                    value=Subscript(
                        value=Call(
                            func=Name(id='env', ctx=Load()),
                            args=[],
                            keywords=[
                                keyword(
                                    arg='context',
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='user', ctx=Load()),
                                            attr='context_get',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                        ),
                        slice=Constant(value='mail.channel', kind=None),
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='MailChannel', ctx=Load()),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='MailChannel', ctx=Load()),
                                                attr='channel_get',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                List(
                                                    elts=[
                                                        Attribute(
                                                            value=Name(id='admin', ctx=Load()),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        slice=Constant(value='id', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            attr='message_post',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='body',
                                value=Call(
                                    func=Name(id='_', ctx=Load()),
                                    args=[Constant(value='Your password is the default (admin)! If this system is exposed to untrusted users it is important to change it immediately for security reasons. I will keep nagging you about it!', kind=None)],
                                    keywords=[],
                                ),
                            ),
                            keyword(
                                arg='message_type',
                                value=Constant(value='comment', kind=None),
                            ),
                            keyword(
                                arg='subtype_xmlid',
                                value=Constant(value='mail.mt_comment', kind=None),
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
            name='Home',
            bases=[
                Attribute(
                    value=Name(id='web', ctx=Load()),
                    attr='Home',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                FunctionDef(
                    name='_login_redirect',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='uid', annotation=None, type_comment=None),
                            arg(arg='redirect', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='request', ctx=Load()),
                                        attr='params',
                                        ctx=Load(),
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='login_success', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='_admin_password_warn', ctx=Load()),
                                        args=[Name(id='uid', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_login_redirect',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='uid', ctx=Load()),
                                    Name(id='redirect', ctx=Load()),
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
