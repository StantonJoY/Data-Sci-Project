Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[alias(name='UserError', asname=None)],
            level=0,
        ),
        ClassDef(
            name='ApplicantGetRefuseReason',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='TransientModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='applicant.get.refuse.reason', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Get Refuse Reason', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='refuse_reason_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='hr.applicant.refuse.reason', kind=None),
                            Constant(value='Refuse Reason', kind=None),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='applicant_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2many',
                            ctx=Load(),
                        ),
                        args=[Constant(value='hr.applicant', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='send_mail', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Send Email', kind=None)],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_send_mail', kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=False, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='template_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='mail.template', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Email Template', kind=None),
                            ),
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_send_mail', kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='domain',
                                value=Constant(value="[('model', '=', 'hr.applicant')]", kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='applicant_without_email', ctx=Store())],
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
                                value=Constant(value='_compute_applicant_without_email', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Applicant(s) not having email', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_send_mail',
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
                            target=Name(id='wizard', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='template', ctx=Store())],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='wizard', ctx=Load()),
                                            attr='refuse_reason_id',
                                            ctx=Load(),
                                        ),
                                        attr='template_id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='wizard', ctx=Load()),
                                            attr='send_mail',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='bool', ctx=Load()),
                                        args=[Name(id='template', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='wizard', ctx=Load()),
                                            attr='template_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='template', ctx=Load()),
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
                            args=[Constant(value='refuse_reason_id', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_applicant_without_email',
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
                            target=Name(id='wizard', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='applicants', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='wizard', ctx=Load()),
                                                attr='applicant_ids',
                                                ctx=Load(),
                                            ),
                                            attr='filtered',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Lambda(
                                                args=arguments(
                                                    posonlyargs=[],
                                                    args=[arg(arg='x', annotation=None, type_comment=None)],
                                                    vararg=None,
                                                    kwonlyargs=[],
                                                    kw_defaults=[],
                                                    kwarg=None,
                                                    defaults=[],
                                                ),
                                                body=BoolOp(
                                                    op=And(),
                                                    values=[
                                                        UnaryOp(
                                                            op=Not(),
                                                            operand=Attribute(
                                                                value=Name(id='x', ctx=Load()),
                                                                attr='email_from',
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                        UnaryOp(
                                                            op=Not(),
                                                            operand=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='x', ctx=Load()),
                                                                    attr='partner_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='email',
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                    ],
                                                ),
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
                                            Name(id='applicants', ctx=Load()),
                                            Attribute(
                                                value=Name(id='wizard', ctx=Load()),
                                                attr='send_mail',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='wizard', ctx=Load()),
                                                    attr='applicant_without_email',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=BinOp(
                                                left=Constant(value='%s\n%s', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Call(
                                                            func=Name(id='_', ctx=Load()),
                                                            args=[Constant(value="The email will not be sent to the following applicant(s) as they don't have email address.", kind=None)],
                                                            keywords=[],
                                                        ),
                                                        Call(
                                                            func=Attribute(
                                                                value=Constant(value='\n', kind=None),
                                                                attr='join',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                ListComp(
                                                                    elt=Attribute(
                                                                        value=Name(id='i', ctx=Load()),
                                                                        attr='partner_name',
                                                                        ctx=Load(),
                                                                    ),
                                                                    generators=[
                                                                        comprehension(
                                                                            target=Name(id='i', ctx=Store()),
                                                                            iter=Name(id='applicants', ctx=Load()),
                                                                            ifs=[],
                                                                            is_async=0,
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='wizard', ctx=Load()),
                                                    attr='applicant_without_email',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=False, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
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
                                Constant(value='applicant_ids', kind=None),
                                Constant(value='send_mail', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='action_refuse_reason_apply',
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
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='send_mail',
                                ctx=Load(),
                            ),
                            body=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='template_id',
                                            ctx=Load(),
                                        ),
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='UserError', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Email template must be selected to send a mail', kind=None)],
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
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='applicant_ids',
                                                    ctx=Load(),
                                                ),
                                                attr='filtered',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Lambda(
                                                    args=arguments(
                                                        posonlyargs=[],
                                                        args=[arg(arg='x', annotation=None, type_comment=None)],
                                                        vararg=None,
                                                        kwonlyargs=[],
                                                        kw_defaults=[],
                                                        kwarg=None,
                                                        defaults=[],
                                                    ),
                                                    body=BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='x', ctx=Load()),
                                                                attr='email_from',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='x', ctx=Load()),
                                                                    attr='partner_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='email',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='UserError', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value="Email of the applicant is not set, email won't be sent.", kind=None)],
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='applicant_ids',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='refuse_reason_id', kind=None),
                                            Constant(value='active', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='refuse_reason_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='send_mail',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='applicants', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='applicant_ids',
                                                ctx=Load(),
                                            ),
                                            attr='filtered',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Lambda(
                                                args=arguments(
                                                    posonlyargs=[],
                                                    args=[arg(arg='x', annotation=None, type_comment=None)],
                                                    vararg=None,
                                                    kwonlyargs=[],
                                                    kw_defaults=[],
                                                    kwarg=None,
                                                    defaults=[],
                                                ),
                                                body=BoolOp(
                                                    op=Or(),
                                                    values=[
                                                        Attribute(
                                                            value=Name(id='x', ctx=Load()),
                                                            attr='email_from',
                                                            ctx=Load(),
                                                        ),
                                                        Attribute(
                                                            value=Attribute(
                                                                value=Name(id='x', ctx=Load()),
                                                                attr='partner_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='email',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='applicants', ctx=Load()),
                                            attr='message_post_with_template',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='template_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg=None,
                                                value=Dict(
                                                    keys=[
                                                        Constant(value='auto_delete_message', kind=None),
                                                        Constant(value='subtype_id', kind=None),
                                                        Constant(value='email_layout_xmlid', kind=None),
                                                    ],
                                                    values=[
                                                        Constant(value=True, kind=None),
                                                        Call(
                                                            func=Attribute(
                                                                value=Subscript(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='env',
                                                                        ctx=Load(),
                                                                    ),
                                                                    slice=Constant(value='ir.model.data', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                attr='_xmlid_to_res_id',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='mail.mt_note', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        Constant(value='mail.mail_notification_light', kind=None),
                                                    ],
                                                ),
                                            ),
                                        ],
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
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
