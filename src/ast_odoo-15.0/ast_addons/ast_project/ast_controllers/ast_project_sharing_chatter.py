Module(
    body=[
        ImportFrom(
            module='werkzeug.exceptions',
            names=[alias(name='Forbidden', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.http',
            names=[
                alias(name='request', asname=None),
                alias(name='route', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.portal.controllers.mail',
            names=[alias(name='PortalChatter', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='portal',
            names=[alias(name='ProjectCustomerPortal', asname=None)],
            level=1,
        ),
        ClassDef(
            name='ProjectSharingChatter',
            bases=[Name(id='PortalChatter', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='_check_project_access_and_get_token',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='project_id', annotation=None, type_comment=None),
                            arg(arg='res_model', annotation=None, type_comment=None),
                            arg(arg='res_id', annotation=None, type_comment=None),
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
                            value=Constant(value=' Check if the chatter in project sharing can be accessed\n\n            If the portal user is in the project sharing, then we do not have the access token of the task\n            but we can have the one of the project (if the user accessed to the project sharing views via the shared link).\n            So, we need to check if the chatter is for a task and if the res_id is a task\n            in the project shared. Then, if we had the project token and this one is the one in the project\n            then we return the token of the task to continue the portal chatter process.\n            If we do not have any token, then we need to check if the portal user is a follower of the project shared.\n            If it is the case, then we give the access token of the task.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='project_sudo', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='ProjectCustomerPortal', ctx=Load()),
                                    attr='_document_check_access',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='self', ctx=Load()),
                                    Constant(value='project.project', kind=None),
                                    Name(id='project_id', ctx=Load()),
                                    Name(id='token', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='can_access', ctx=Store())],
                            value=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='project_sudo', ctx=Load()),
                                    Compare(
                                        left=Name(id='res_model', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='project.task', kind=None)],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='project_sudo', ctx=Load()),
                                                    attr='with_user',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='request', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='user',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='_check_project_sharing_access',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='task', ctx=Store())],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='can_access', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='task', ctx=Store())],
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
                                                        slice=Constant(value='project.task', kind=None),
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
                                                            Constant(value='id', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Name(id='res_id', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='project_id', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Attribute(
                                                                value=Name(id='project_sudo', ctx=Load()),
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
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='can_access', ctx=Load()),
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='task', ctx=Load()),
                                    ),
                                ],
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
                        Return(
                            value=Subscript(
                                value=Name(id='task', ctx=Load()),
                                slice=Attribute(
                                    value=Name(id='task', ctx=Load()),
                                    attr='_mail_post_token_field',
                                    ctx=Load(),
                                ),
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
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
                            targets=[Name(id='project_sharing_id', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='kwargs', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='project_sharing_id', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='project_sharing_id', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='token', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_check_project_access_and_get_token',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='project_sharing_id', ctx=Load()),
                                            Name(id='res_model', ctx=Load()),
                                            Name(id='res_id', ctx=Load()),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='kwargs', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='token', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='token', ctx=Load()),
                                    body=[
                                        Delete(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='kwargs', ctx=Load()),
                                                    slice=Constant(value='project_sharing_id', kind=None),
                                                    ctx=Del(),
                                                ),
                                            ],
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='kwargs', ctx=Load()),
                                                    slice=Constant(value='token', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='token', ctx=Load()),
                                            type_comment=None,
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
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='portal_chatter_init',
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
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='route', ctx=Load()),
                            args=[],
                            keywords=[],
                        ),
                    ],
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
                        Assign(
                            targets=[Name(id='project_sharing_id', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='kw', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='project_sharing_id', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='project_sharing_id', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='token', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_check_project_access_and_get_token',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='project_sharing_id', ctx=Load()),
                                            Name(id='res_model', ctx=Load()),
                                            Name(id='res_id', ctx=Load()),
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
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='token', ctx=Load()),
                                    body=[
                                        Delete(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='kw', ctx=Load()),
                                                    slice=Constant(value='project_sharing_id', kind=None),
                                                    ctx=Del(),
                                                ),
                                            ],
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='kw', ctx=Load()),
                                                    slice=Constant(value='token', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='token', ctx=Load()),
                                            type_comment=None,
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
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='portal_chatter_post',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='res_model', ctx=Load()),
                                    Name(id='res_id', ctx=Load()),
                                    Name(id='message', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='attachment_ids',
                                        value=Name(id='attachment_ids', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='attachment_tokens',
                                        value=Name(id='attachment_tokens', ctx=Load()),
                                    ),
                                    keyword(
                                        arg=None,
                                        value=Name(id='kw', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='route', ctx=Load()),
                            args=[],
                            keywords=[],
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
                        Assign(
                            targets=[Name(id='project_sharing_id', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='kw', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='project_sharing_id', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='project_sharing_id', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='token', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_check_project_access_and_get_token',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='project_sharing_id', ctx=Load()),
                                            Name(id='res_model', ctx=Load()),
                                            Name(id='res_id', ctx=Load()),
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
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='token', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='kw', ctx=Load()),
                                                    slice=Constant(value='token', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='token', ctx=Load()),
                                            type_comment=None,
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
                                        args=[],
                                        keywords=[],
                                    ),
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
                                        arg='offset',
                                        value=Name(id='offset', ctx=Load()),
                                    ),
                                    keyword(
                                        arg=None,
                                        value=Name(id='kw', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='route', ctx=Load()),
                            args=[],
                            keywords=[],
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
