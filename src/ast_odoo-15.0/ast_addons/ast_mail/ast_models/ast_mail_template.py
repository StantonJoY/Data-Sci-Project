Module(
    body=[
        Import(
            names=[alias(name='base64', asname=None)],
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='_', asname=None),
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='tools', asname=None),
                alias(name='Command', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[alias(name='UserError', asname=None)],
            level=0,
        ),
        Assign(
            targets=[Name(id='_logger', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='logging', ctx=Load()),
                    attr='getLogger',
                    ctx=Load(),
                ),
                args=[Name(id='__name__', ctx=Load())],
                keywords=[],
            ),
            type_comment=None,
        ),
        ClassDef(
            name='MailTemplate',
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
                    value=Constant(value='Templates for sending email', kind=None),
                ),
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='mail.template', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=List(
                        elts=[Constant(value='mail.render.mixin', kind=None)],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Email Templates', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_order', ctx=Store())],
                    value=Constant(value='name', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_unrestricted_rendering', ctx=Store())],
                    value=Constant(value=True, kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='default_get',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='fields', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='MailTemplate', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='default_get',
                                    ctx=Load(),
                                ),
                                args=[Name(id='fields', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='res', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='model', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='res', ctx=Load()),
                                            slice=Constant(value='model_id', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='ir.model', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='_get',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Call(
                                                    func=Attribute(
                                                        value=Name(id='res', ctx=Load()),
                                                        attr='pop',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='model', kind=None)],
                                                    keywords=[],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
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
                Assign(
                    targets=[Name(id='name', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Name', kind=None)],
                        keywords=[
                            keyword(
                                arg='translate',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='model_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='ir.model', kind=None),
                            Constant(value='Applies to', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value='The type of document this template can be used with', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='model', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Related Document Model', kind=None)],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='model_id.model', kind=None),
                            ),
                            keyword(
                                arg='index',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
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
                    targets=[Name(id='subject', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Subject', kind=None)],
                        keywords=[
                            keyword(
                                arg='translate',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Subject (placeholders may be used here)', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='email_from', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='From', kind=None)],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value="Sender address (placeholders may be used here). If not set, the default value will be the author's email alias if configured, or email address.", kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='use_default_to', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Default recipients', kind=None)],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value='Default recipients of the record:\n- partner (using id on a partner or the partner_id field) OR\n- email (using email_from or email field)', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='email_to', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='To (Emails)', kind=None)],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value='Comma-separated recipient addresses (placeholders may be used here)', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='partner_to', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='To (Partners)', kind=None)],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value='Comma-separated ids of recipient partners (placeholders may be used here)', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='email_cc', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Cc', kind=None)],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value='Carbon copy recipients (placeholders may be used here)', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='reply_to', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Reply To', kind=None)],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value='Email address to which replies will be redirected when sending emails in mass; only used when the reply is not logged in the original discussion thread.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='body_html', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Html',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Body', kind=None)],
                        keywords=[
                            keyword(
                                arg='render_engine',
                                value=Constant(value='qweb', kind=None),
                            ),
                            keyword(
                                arg='translate',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='sanitize',
                                value=Constant(value=False, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='attachment_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='ir.attachment', kind=None),
                            Constant(value='email_template_attachment_rel', kind=None),
                            Constant(value='email_template_id', kind=None),
                            Constant(value='attachment_id', kind=None),
                            Constant(value='Attachments', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value='You may attach files to this template, to be added to all emails created from this template', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='report_name', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Report Filename', kind=None)],
                        keywords=[
                            keyword(
                                arg='translate',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Name to use for the generated report file (may contain placeholders)\nThe extension can be omitted and will then come from the report type.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='report_template', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='ir.actions.report', kind=None),
                            Constant(value='Optional report to print and attach', kind=None),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='mail_server_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='ir.mail_server', kind=None),
                            Constant(value='Outgoing Mail Server', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='readonly',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Optional preferred server for outgoing mails. If not set, the highest priority one will be used.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='scheduled_date', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Scheduled Date', kind=None)],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value='If set, the queue manager will send the email after the date. If not set, the email will be send as soon as possible. You can use dynamic expressions expression.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='auto_delete', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Auto Delete', kind=None)],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value="This option permanently removes any track of email after it's been sent, including from the Technical menu in the Settings, in order to preserve storage space of your Odoo database.", kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='ref_ir_act_window', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='ir.actions.act_window', kind=None),
                            Constant(value='Sidebar action', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='copy',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Sidebar action to make this template available on records of the related document model', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_render_model',
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
                            target=Name(id='template', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='template', ctx=Load()),
                                            attr='render_model',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='template', ctx=Load()),
                                        attr='model',
                                        ctx=Load(),
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
                            args=[Constant(value='model', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='unlink',
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
                                    attr='unlink_action',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='MailTemplate', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='unlink',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
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
                                            Name(id='MailTemplate', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='copy',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='default',
                                        value=Name(id='default', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='returns',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='self', kind=None),
                                Lambda(
                                    args=arguments(
                                        posonlyargs=[],
                                        args=[arg(arg='value', annotation=None, type_comment=None)],
                                        vararg=None,
                                        kwonlyargs=[],
                                        kw_defaults=[],
                                        kwarg=None,
                                        defaults=[],
                                    ),
                                    body=Attribute(
                                        value=Name(id='value', ctx=Load()),
                                        attr='id',
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
                    name='unlink_action',
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
                            target=Name(id='template', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=Attribute(
                                        value=Name(id='template', ctx=Load()),
                                        attr='ref_ir_act_window',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='template', ctx=Load()),
                                                        attr='ref_ir_act_window',
                                                        ctx=Load(),
                                                    ),
                                                    attr='unlink',
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
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Constant(value=True, kind=None),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='create_action',
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
                            targets=[Name(id='ActWindow', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='ir.actions.act_window', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='view', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='ref',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='mail.email_compose_message_wizard_form', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='template', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='button_name', ctx=Store())],
                                    value=Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[
                                            Constant(value='Send Mail (%s)', kind=None),
                                            Attribute(
                                                value=Name(id='template', ctx=Load()),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='action', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='ActWindow', ctx=Load()),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='type', kind=None),
                                                    Constant(value='res_model', kind=None),
                                                    Constant(value='context', kind=None),
                                                    Constant(value='view_mode', kind=None),
                                                    Constant(value='view_id', kind=None),
                                                    Constant(value='target', kind=None),
                                                    Constant(value='binding_model_id', kind=None),
                                                ],
                                                values=[
                                                    Name(id='button_name', ctx=Load()),
                                                    Constant(value='ir.actions.act_window', kind=None),
                                                    Constant(value='mail.compose.message', kind=None),
                                                    BinOp(
                                                        left=Constant(value="{'default_composition_mode': 'mass_mail', 'default_template_id' : %d, 'default_use_template': True}", kind=None),
                                                        op=Mod(),
                                                        right=Attribute(
                                                            value=Name(id='template', ctx=Load()),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    Constant(value='form,tree', kind=None),
                                                    Attribute(
                                                        value=Name(id='view', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='new', kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='template', ctx=Load()),
                                                            attr='model_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='template', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='ref_ir_act_window', kind=None)],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='action', ctx=Load()),
                                                        attr='id',
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
                        Return(
                            value=Constant(value=True, kind=None),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='generate_recipients',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='results', annotation=None, type_comment=None),
                            arg(arg='res_ids', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Generates the recipients of the template. Default values can ben generated\n        instead of the template values if requested by template or context.\n        Emails (email_to, email_cc) can be transformed into partners if requested\n        in the context. ', kind=None),
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
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='use_default_to',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_context',
                                                ctx=Load(),
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='tpl_force_default_to', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='records', ctx=Store())],
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
                                                        slice=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='model',
                                                            ctx=Load(),
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    attr='browse',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='res_ids', ctx=Load())],
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
                                Assign(
                                    targets=[Name(id='default_recipients', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='records', ctx=Load()),
                                            attr='_message_get_default_recipients',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Tuple(
                                        elts=[
                                            Name(id='res_id', ctx=Store()),
                                            Name(id='recipients', ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                    iter=Call(
                                        func=Attribute(
                                            value=Name(id='default_recipients', ctx=Load()),
                                            attr='items',
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
                                                        value=Name(id='results', ctx=Load()),
                                                        slice=Name(id='res_id', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                    attr='pop',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='partner_to', kind=None),
                                                    Constant(value=None, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Name(id='results', ctx=Load()),
                                                        slice=Name(id='res_id', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                    attr='update',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='recipients', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='records_company', ctx=Store())],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_context',
                                                ctx=Load(),
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='tpl_partners_only', kind=None)],
                                        keywords=[],
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='model',
                                        ctx=Load(),
                                    ),
                                    Name(id='results', ctx=Load()),
                                    Compare(
                                        left=Constant(value='company_id', kind=None),
                                        ops=[In()],
                                        comparators=[
                                            Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='model',
                                                        ctx=Load(),
                                                    ),
                                                    ctx=Load(),
                                                ),
                                                attr='_fields',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='records', ctx=Store())],
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
                                                        slice=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='model',
                                                            ctx=Load(),
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    attr='browse',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='results', ctx=Load()),
                                                            attr='keys',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='read',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[Constant(value='company_id', kind=None)],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='records_company', ctx=Store())],
                                    value=DictComp(
                                        key=Subscript(
                                            value=Name(id='rec', ctx=Load()),
                                            slice=Constant(value='id', kind=None),
                                            ctx=Load(),
                                        ),
                                        value=IfExp(
                                            test=Subscript(
                                                value=Name(id='rec', ctx=Load()),
                                                slice=Constant(value='company_id', kind=None),
                                                ctx=Load(),
                                            ),
                                            body=Subscript(
                                                value=Subscript(
                                                    value=Name(id='rec', ctx=Load()),
                                                    slice=Constant(value='company_id', kind=None),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            orelse=Constant(value=None, kind=None),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='rec', ctx=Store()),
                                                iter=Name(id='records', ctx=Load()),
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
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='res_id', ctx=Store()),
                                    Name(id='values', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='results', ctx=Load()),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='partner_ids', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='values', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='partner_ids', kind=None),
                                            Call(
                                                func=Name(id='list', ctx=Load()),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_context',
                                                ctx=Load(),
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='tpl_partners_only', kind=None)],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='mails', ctx=Store())],
                                            value=BinOp(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Name(id='tools', ctx=Load()),
                                                        attr='email_split',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Call(
                                                            func=Attribute(
                                                                value=Name(id='values', ctx=Load()),
                                                                attr='pop',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Constant(value='email_to', kind=None),
                                                                Constant(value='', kind=None),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                op=Add(),
                                                right=Call(
                                                    func=Attribute(
                                                        value=Name(id='tools', ctx=Load()),
                                                        attr='email_split',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Call(
                                                            func=Attribute(
                                                                value=Name(id='values', ctx=Load()),
                                                                attr='pop',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Constant(value='email_cc', kind=None),
                                                                Constant(value='', kind=None),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='Partner', ctx=Store())],
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='res.partner', kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Name(id='records_company', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='Partner', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='Partner', ctx=Load()),
                                                            attr='with_context',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='default_company_id',
                                                                value=Subscript(
                                                                    value=Name(id='records_company', ctx=Load()),
                                                                    slice=Name(id='res_id', ctx=Load()),
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        For(
                                            target=Name(id='mail', ctx=Store()),
                                            iter=Name(id='mails', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='partner', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='Partner', ctx=Load()),
                                                            attr='find_or_create',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='mail', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='partner_ids', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='partner', ctx=Load()),
                                                                attr='id',
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
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='partner_to', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='values', ctx=Load()),
                                            attr='pop',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='partner_to', kind=None),
                                            Constant(value='', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='partner_to', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='tpl_partner_ids', ctx=Store())],
                                            value=ListComp(
                                                elt=Call(
                                                    func=Name(id='int', ctx=Load()),
                                                    args=[Name(id='pid', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='pid', ctx=Store()),
                                                        iter=Call(
                                                            func=Attribute(
                                                                value=Name(id='partner_to', ctx=Load()),
                                                                attr='split',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value=',', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        ifs=[Name(id='pid', ctx=Load())],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        AugAssign(
                                            target=Name(id='partner_ids', ctx=Store()),
                                            op=Add(),
                                            value=Attribute(
                                                value=Call(
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
                                                            args=[Name(id='tpl_partner_ids', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                        attr='exists',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                attr='ids',
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Subscript(
                                                value=Name(id='results', ctx=Load()),
                                                slice=Name(id='res_id', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='partner_ids', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='partner_ids', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='results', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='generate_email',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='res_ids', annotation=None, type_comment=None),
                            arg(arg='fields', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Generates an email from the template for given the given model based on\n        records given by res_ids.\n\n        :param res_id: id of the record to use for rendering the template (model\n                       is taken from template definition)\n        :returns: a dict containing all relevant fields for creating a new\n                  mail.mail entry, with one extra key ``attachments``, in the\n                  format [(report_name, data)] where data is base64 encoded.\n        ', kind=None),
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
                            targets=[Name(id='multi_mode', ctx=Store())],
                            value=Constant(value=True, kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Name(id='isinstance', ctx=Load()),
                                args=[
                                    Name(id='res_ids', ctx=Load()),
                                    Name(id='int', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='res_ids', ctx=Store())],
                                    value=List(
                                        elts=[Name(id='res_ids', ctx=Load())],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='multi_mode', ctx=Store())],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='results', ctx=Store())],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='lang', ctx=Store()),
                                    Tuple(
                                        elts=[
                                            Name(id='template', ctx=Store()),
                                            Name(id='template_res_ids', ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_classify_per_lang',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='res_ids', ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                For(
                                    target=Name(id='field', ctx=Store()),
                                    iter=Name(id='fields', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='generated_field_values', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='template', ctx=Load()),
                                                    attr='_render_field',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='field', ctx=Load()),
                                                    Name(id='template_res_ids', ctx=Load()),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='options',
                                                        value=Dict(
                                                            keys=[Constant(value='render_safe', kind=None)],
                                                            values=[
                                                                Compare(
                                                                    left=Name(id='field', ctx=Load()),
                                                                    ops=[Eq()],
                                                                    comparators=[Constant(value='subject', kind=None)],
                                                                ),
                                                            ],
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='post_process',
                                                        value=Compare(
                                                            left=Name(id='field', ctx=Load()),
                                                            ops=[Eq()],
                                                            comparators=[Constant(value='body_html', kind=None)],
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        For(
                                            target=Tuple(
                                                elts=[
                                                    Name(id='res_id', ctx=Store()),
                                                    Name(id='field_value', ctx=Store()),
                                                ],
                                                ctx=Store(),
                                            ),
                                            iter=Call(
                                                func=Attribute(
                                                    value=Name(id='generated_field_values', ctx=Load()),
                                                    attr='items',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='results', ctx=Load()),
                                                                    attr='setdefault',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Name(id='res_id', ctx=Load()),
                                                                    Call(
                                                                        func=Name(id='dict', ctx=Load()),
                                                                        args=[],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            slice=Name(id='field', ctx=Load()),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Name(id='field_value', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                If(
                                    test=Call(
                                        func=Name(id='any', ctx=Load()),
                                        args=[
                                            GeneratorExp(
                                                elt=Compare(
                                                    left=Name(id='field', ctx=Load()),
                                                    ops=[In()],
                                                    comparators=[Name(id='fields', ctx=Load())],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='field', ctx=Store()),
                                                        iter=List(
                                                            elts=[
                                                                Constant(value='email_to', kind=None),
                                                                Constant(value='partner_to', kind=None),
                                                                Constant(value='email_cc', kind=None),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='results', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='template', ctx=Load()),
                                                    attr='generate_recipients',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='results', ctx=Load()),
                                                    Name(id='template_res_ids', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                For(
                                    target=Name(id='res_id', ctx=Store()),
                                    iter=Name(id='template_res_ids', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='values', ctx=Store())],
                                            value=Subscript(
                                                value=Name(id='results', ctx=Load()),
                                                slice=Name(id='res_id', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Call(
                                                func=Attribute(
                                                    value=Name(id='values', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='body_html', kind=None)],
                                                keywords=[],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='values', ctx=Load()),
                                                            slice=Constant(value='body', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='tools', ctx=Load()),
                                                            attr='html_sanitize',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='values', ctx=Load()),
                                                                slice=Constant(value='body_html', kind=None),
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
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='values', ctx=Load()),
                                                    attr='update',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='mail_server_id',
                                                        value=BoolOp(
                                                            op=Or(),
                                                            values=[
                                                                Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='template', ctx=Load()),
                                                                        attr='mail_server_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='id',
                                                                    ctx=Load(),
                                                                ),
                                                                Constant(value=False, kind=None),
                                                            ],
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='auto_delete',
                                                        value=Attribute(
                                                            value=Name(id='template', ctx=Load()),
                                                            attr='auto_delete',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='model',
                                                        value=Attribute(
                                                            value=Name(id='template', ctx=Load()),
                                                            attr='model',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='res_id',
                                                        value=BoolOp(
                                                            op=Or(),
                                                            values=[
                                                                Name(id='res_id', ctx=Load()),
                                                                Constant(value=False, kind=None),
                                                            ],
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='attachment_ids',
                                                        value=ListComp(
                                                            elt=Attribute(
                                                                value=Name(id='attach', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            generators=[
                                                                comprehension(
                                                                    target=Name(id='attach', ctx=Store()),
                                                                    iter=Attribute(
                                                                        value=Name(id='template', ctx=Load()),
                                                                        attr='attachment_ids',
                                                                        ctx=Load(),
                                                                    ),
                                                                    ifs=[],
                                                                    is_async=0,
                                                                ),
                                                            ],
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                If(
                                    test=Attribute(
                                        value=Name(id='template', ctx=Load()),
                                        attr='report_template',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        For(
                                            target=Name(id='res_id', ctx=Store()),
                                            iter=Name(id='template_res_ids', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='attachments', ctx=Store())],
                                                    value=List(elts=[], ctx=Load()),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='report_name', ctx=Store())],
                                                    value=Subscript(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Name(id='template', ctx=Load()),
                                                                attr='_render_field',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Constant(value='report_name', kind=None),
                                                                List(
                                                                    elts=[Name(id='res_id', ctx=Load())],
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        slice=Name(id='res_id', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='report', ctx=Store())],
                                                    value=Attribute(
                                                        value=Name(id='template', ctx=Load()),
                                                        attr='report_template',
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='report_service', ctx=Store())],
                                                    value=Attribute(
                                                        value=Name(id='report', ctx=Load()),
                                                        attr='report_name',
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=Compare(
                                                        left=Attribute(
                                                            value=Name(id='report', ctx=Load()),
                                                            attr='report_type',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[In()],
                                                        comparators=[
                                                            List(
                                                                elts=[
                                                                    Constant(value='qweb-html', kind=None),
                                                                    Constant(value='qweb-pdf', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[
                                                                Tuple(
                                                                    elts=[
                                                                        Name(id='result', ctx=Store()),
                                                                        Name(id='format', ctx=Store()),
                                                                    ],
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='report', ctx=Load()),
                                                                    attr='_render_qweb_pdf',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    List(
                                                                        elts=[Name(id='res_id', ctx=Load())],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[
                                                        Assign(
                                                            targets=[Name(id='res', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='report', ctx=Load()),
                                                                    attr='_render',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    List(
                                                                        elts=[Name(id='res_id', ctx=Load())],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
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
                                                                Raise(
                                                                    exc=Call(
                                                                        func=Name(id='UserError', ctx=Load()),
                                                                        args=[
                                                                            Call(
                                                                                func=Name(id='_', ctx=Load()),
                                                                                args=[
                                                                                    Constant(value='Unsupported report type %s found.', kind=None),
                                                                                    Attribute(
                                                                                        value=Name(id='report', ctx=Load()),
                                                                                        attr='report_type',
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
                                                        Assign(
                                                            targets=[
                                                                Tuple(
                                                                    elts=[
                                                                        Name(id='result', ctx=Store()),
                                                                        Name(id='format', ctx=Store()),
                                                                    ],
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Name(id='res', ctx=Load()),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                ),
                                                Assign(
                                                    targets=[Name(id='result', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='base64', ctx=Load()),
                                                            attr='b64encode',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='result', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=UnaryOp(
                                                        op=Not(),
                                                        operand=Name(id='report_name', ctx=Load()),
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='report_name', ctx=Store())],
                                                            value=BinOp(
                                                                left=Constant(value='report.', kind=None),
                                                                op=Add(),
                                                                right=Name(id='report_service', ctx=Load()),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                                Assign(
                                                    targets=[Name(id='ext', ctx=Store())],
                                                    value=BinOp(
                                                        left=Constant(value='.', kind=None),
                                                        op=Add(),
                                                        right=Name(id='format', ctx=Load()),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=UnaryOp(
                                                        op=Not(),
                                                        operand=Call(
                                                            func=Attribute(
                                                                value=Name(id='report_name', ctx=Load()),
                                                                attr='endswith',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Name(id='ext', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                    body=[
                                                        AugAssign(
                                                            target=Name(id='report_name', ctx=Store()),
                                                            op=Add(),
                                                            value=Name(id='ext', ctx=Load()),
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='attachments', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Tuple(
                                                                elts=[
                                                                    Name(id='report_name', ctx=Load()),
                                                                    Name(id='result', ctx=Load()),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Subscript(
                                                                value=Name(id='results', ctx=Load()),
                                                                slice=Name(id='res_id', ctx=Load()),
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='attachments', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Name(id='attachments', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
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
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='multi_mode', ctx=Load()),
                                            Name(id='results', ctx=Load()),
                                        ],
                                    ),
                                    Subscript(
                                        value=Name(id='results', ctx=Load()),
                                        slice=Subscript(
                                            value=Name(id='res_ids', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        ctx=Load(),
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
                    name='_send_check_access',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='res_ids', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='records', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='model',
                                            ctx=Load(),
                                        ),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[Name(id='res_ids', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='records', ctx=Load()),
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
                                    value=Name(id='records', ctx=Load()),
                                    attr='check_access_rule',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='read', kind=None)],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='send_mail',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='res_id', annotation=None, type_comment=None),
                            arg(arg='force_send', annotation=None, type_comment=None),
                            arg(arg='raise_exception', annotation=None, type_comment=None),
                            arg(arg='email_values', annotation=None, type_comment=None),
                            arg(arg='notif_layout', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=False, kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=False, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Generates a new mail.mail. Template is rendered on record given by\n        res_id and model coming from template.\n\n        :param int res_id: id of the record to render the template\n        :param bool force_send: send email immediately; otherwise use the mail\n            queue (recommended);\n        :param dict email_values: update generated mail with those values to further\n            customize the mail;\n        :param str notif_layout: optional notification layout to encapsulate the\n            generated email;\n        :returns: id of the mail.mail that was created ', kind=None),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_send_check_access',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Name(id='res_id', ctx=Load())],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='Attachment', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='ir.attachment', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='generate_email',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='res_id', ctx=Load()),
                                    List(
                                        elts=[
                                            Constant(value='subject', kind=None),
                                            Constant(value='body_html', kind=None),
                                            Constant(value='email_from', kind=None),
                                            Constant(value='email_to', kind=None),
                                            Constant(value='partner_to', kind=None),
                                            Constant(value='email_cc', kind=None),
                                            Constant(value='reply_to', kind=None),
                                            Constant(value='scheduled_date', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='values', ctx=Load()),
                                    slice=Constant(value='recipient_ids', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=ListComp(
                                elt=Call(
                                    func=Attribute(
                                        value=Name(id='Command', ctx=Load()),
                                        attr='link',
                                        ctx=Load(),
                                    ),
                                    args=[Name(id='pid', ctx=Load())],
                                    keywords=[],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='pid', ctx=Store()),
                                        iter=Call(
                                            func=Attribute(
                                                value=Name(id='values', ctx=Load()),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Constant(value='partner_ids', kind=None),
                                                Call(
                                                    func=Name(id='list', ctx=Load()),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='values', ctx=Load()),
                                    slice=Constant(value='attachment_ids', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=ListComp(
                                elt=Call(
                                    func=Attribute(
                                        value=Name(id='Command', ctx=Load()),
                                        attr='link',
                                        ctx=Load(),
                                    ),
                                    args=[Name(id='aid', ctx=Load())],
                                    keywords=[],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='aid', ctx=Store()),
                                        iter=Call(
                                            func=Attribute(
                                                value=Name(id='values', ctx=Load()),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Constant(value='attachment_ids', kind=None),
                                                Call(
                                                    func=Name(id='list', ctx=Load()),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='values', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Name(id='email_values', ctx=Load()),
                                            Dict(keys=[], values=[]),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='attachment_ids', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='values', ctx=Load()),
                                    attr='pop',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='attachment_ids', kind=None),
                                    List(elts=[], ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='attachments', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='values', ctx=Load()),
                                    attr='pop',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='attachments', kind=None),
                                    List(elts=[], ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Constant(value='email_from', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='values', ctx=Load())],
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Name(id='values', ctx=Load()),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='email_from', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='values', ctx=Load()),
                                            attr='pop',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='email_from', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='notif_layout', ctx=Load()),
                                    Subscript(
                                        value=Name(id='values', ctx=Load()),
                                        slice=Constant(value='body_html', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Try(
                                    body=[
                                        Assign(
                                            targets=[Name(id='template', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='ref',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='notif_layout', ctx=Load())],
                                                keywords=[
                                                    keyword(
                                                        arg='raise_if_not_found',
                                                        value=Constant(value=True, kind=None),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='ValueError', ctx=Load()),
                                            name=None,
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='_logger', ctx=Load()),
                                                            attr='warning',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            BinOp(
                                                                left=Constant(value='QWeb template %s not found when sending template %s. Sending without layouting.', kind=None),
                                                                op=Mod(),
                                                                right=Tuple(
                                                                    elts=[
                                                                        Name(id='notif_layout', ctx=Load()),
                                                                        Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='name',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='record', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='model',
                                                            ctx=Load(),
                                                        ),
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
                                            targets=[Name(id='model', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='ir.model', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='_get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='record', ctx=Load()),
                                                        attr='_name',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='lang',
                                                ctx=Load(),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='lang', ctx=Store())],
                                                    value=Subscript(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='_render_lang',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                List(
                                                                    elts=[Name(id='res_id', ctx=Load())],
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        slice=Name(id='res_id', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='template', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='template', ctx=Load()),
                                                            attr='with_context',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='lang',
                                                                value=Name(id='lang', ctx=Load()),
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='model', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='model', ctx=Load()),
                                                            attr='with_context',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='lang',
                                                                value=Name(id='lang', ctx=Load()),
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='template_ctx', ctx=Store())],
                                            value=Dict(
                                                keys=[
                                                    Constant(value='message', kind=None),
                                                    Constant(value='model_description', kind=None),
                                                    Constant(value='company', kind=None),
                                                    Constant(value='record', kind=None),
                                                ],
                                                values=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Subscript(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
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
                                                            attr='new',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Name(id='dict', ctx=Load()),
                                                                args=[],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='body',
                                                                        value=Subscript(
                                                                            value=Name(id='values', ctx=Load()),
                                                                            slice=Constant(value='body_html', kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                    keyword(
                                                                        arg='record_name',
                                                                        value=Attribute(
                                                                            value=Name(id='record', ctx=Load()),
                                                                            attr='display_name',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Attribute(
                                                        value=Name(id='model', ctx=Load()),
                                                        attr='display_name',
                                                        ctx=Load(),
                                                    ),
                                                    BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    Compare(
                                                                        left=Constant(value='company_id', kind=None),
                                                                        ops=[In()],
                                                                        comparators=[Name(id='record', ctx=Load())],
                                                                    ),
                                                                    Subscript(
                                                                        value=Name(id='record', ctx=Load()),
                                                                        slice=Constant(value='company_id', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='company',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    Name(id='record', ctx=Load()),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='body', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='template', ctx=Load()),
                                                    attr='_render',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='template_ctx', ctx=Load())],
                                                keywords=[
                                                    keyword(
                                                        arg='engine',
                                                        value=Constant(value='ir.qweb', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='minimal_qcontext',
                                                        value=Constant(value=True, kind=None),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='values', ctx=Load()),
                                                    slice=Constant(value='body_html', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='mail.render.mixin', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='_replace_local_links',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='body', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    finalbody=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='mail', ctx=Store())],
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
                                                slice=Constant(value='mail.mail', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Name(id='values', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='attachment', ctx=Store()),
                            iter=Name(id='attachments', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='attachment_data', ctx=Store())],
                                    value=Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='datas', kind=None),
                                            Constant(value='type', kind=None),
                                            Constant(value='res_model', kind=None),
                                            Constant(value='res_id', kind=None),
                                        ],
                                        values=[
                                            Subscript(
                                                value=Name(id='attachment', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='attachment', ctx=Load()),
                                                slice=Constant(value=1, kind=None),
                                                ctx=Load(),
                                            ),
                                            Constant(value='binary', kind=None),
                                            Constant(value='mail.message', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='mail', ctx=Load()),
                                                    attr='mail_message_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='attachment_ids', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=4, kind=None),
                                                    Attribute(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Name(id='Attachment', ctx=Load()),
                                                                attr='create',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Name(id='attachment_data', ctx=Load())],
                                                            keywords=[],
                                                        ),
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
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='attachment_ids', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='mail', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='attachment_ids', kind=None)],
                                                values=[Name(id='attachment_ids', ctx=Load())],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Name(id='force_send', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='mail', ctx=Load()),
                                            attr='send',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='raise_exception',
                                                value=Name(id='raise_exception', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Attribute(
                                value=Name(id='mail', ctx=Load()),
                                attr='id',
                                ctx=Load(),
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
