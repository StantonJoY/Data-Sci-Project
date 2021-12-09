Module(
    body=[
        Import(
            names=[alias(name='re', asname=None)],
        ),
        Import(
            names=[alias(name='base64', asname=None)],
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='api', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.iap.tools',
            names=[alias(name='iap_tools', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.safe_eval',
            names=[alias(name='safe_eval', asname=None)],
            level=0,
        ),
        Assign(
            targets=[Name(id='DEFAULT_ENDPOINT', ctx=Store())],
            value=Constant(value='https://iap-snailmail.odoo.com', kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='PRINT_ENDPOINT', ctx=Store())],
            value=Constant(value='/iap/snailmail/1/print', kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='DEFAULT_TIMEOUT', ctx=Store())],
            value=Constant(value=30, kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='ERROR_CODES', ctx=Store())],
            value=List(
                elts=[
                    Constant(value='MISSING_REQUIRED_FIELDS', kind=None),
                    Constant(value='CREDIT_ERROR', kind=None),
                    Constant(value='TRIAL_ERROR', kind=None),
                    Constant(value='NO_PRICE_AVAILABLE', kind=None),
                    Constant(value='FORMAT_ERROR', kind=None),
                    Constant(value='UNKNOWN_ERROR', kind=None),
                ],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        ClassDef(
            name='SnailmailLetter',
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
                    value=Constant(value='snailmail.letter', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Snailmail Letter', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='user_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='res.users', kind=None),
                            Constant(value='Sent by', kind=None),
                        ],
                        keywords=[],
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
                        args=[Constant(value='Model', kind=None)],
                        keywords=[
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='res_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Document ID', kind=None)],
                        keywords=[
                            keyword(
                                arg='required',
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
                                value=Constant(value='Recipient', kind=None),
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
                    targets=[Name(id='company_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='res.company', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Company', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Lambda(
                                    args=arguments(
                                        posonlyargs=[],
                                        args=[arg(arg='self', annotation=None, type_comment=None)],
                                        vararg=None,
                                        kwonlyargs=[],
                                        kw_defaults=[],
                                        kwarg=None,
                                        defaults=[],
                                    ),
                                    body=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='company',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ),
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
                    targets=[Name(id='attachment_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='ir.attachment', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Attachment', kind=None),
                            ),
                            keyword(
                                arg='ondelete',
                                value=Constant(value='cascade', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='attachment_datas', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Binary',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Document', kind=None)],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='attachment_id.datas', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='attachment_fname', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Attachment Filename', kind=None)],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='attachment_id.name', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='color', ctx=Store())],
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
                                value=Constant(value='Color', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Lambda(
                                    args=arguments(
                                        posonlyargs=[],
                                        args=[arg(arg='self', annotation=None, type_comment=None)],
                                        vararg=None,
                                        kwonlyargs=[],
                                        kw_defaults=[],
                                        kwarg=None,
                                        defaults=[],
                                    ),
                                    body=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='company',
                                            ctx=Load(),
                                        ),
                                        attr='snailmail_color',
                                        ctx=Load(),
                                    ),
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='cover', ctx=Store())],
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
                                value=Constant(value='Cover Page', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Lambda(
                                    args=arguments(
                                        posonlyargs=[],
                                        args=[arg(arg='self', annotation=None, type_comment=None)],
                                        vararg=None,
                                        kwonlyargs=[],
                                        kw_defaults=[],
                                        kwarg=None,
                                        defaults=[],
                                    ),
                                    body=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='company',
                                            ctx=Load(),
                                        ),
                                        attr='snailmail_cover',
                                        ctx=Load(),
                                    ),
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='duplex', ctx=Store())],
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
                                value=Constant(value='Both side', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Lambda(
                                    args=arguments(
                                        posonlyargs=[],
                                        args=[arg(arg='self', annotation=None, type_comment=None)],
                                        vararg=None,
                                        kwonlyargs=[],
                                        kw_defaults=[],
                                        kwarg=None,
                                        defaults=[],
                                    ),
                                    body=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='company',
                                            ctx=Load(),
                                        ),
                                        attr='snailmail_duplex',
                                        ctx=Load(),
                                    ),
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='state', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[
                            List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='pending', kind=None),
                                            Constant(value='In Queue', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='sent', kind=None),
                                            Constant(value='Sent', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='error', kind=None),
                                            Constant(value='Error', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='canceled', kind=None),
                                            Constant(value='Canceled', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            Constant(value='Status', kind=None),
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
                                arg='default',
                                value=Constant(value='pending', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value="When a letter is created, the status is 'Pending'.\nIf the letter is correctly sent, the status goes in 'Sent',\nIf not, it will got in state 'Error' and the error message will be displayed in the field 'Error Message'.", kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='error_code', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[
                            ListComp(
                                elt=Tuple(
                                    elts=[
                                        Name(id='err_code', ctx=Load()),
                                        Name(id='err_code', ctx=Load()),
                                    ],
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='err_code', ctx=Store()),
                                        iter=Name(id='ERROR_CODES', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                        ],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Error', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='info_msg', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Information', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='display_name', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Display Name', kind=None)],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_display_name', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='reference', ctx=Store())],
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
                                value=Constant(value='Related Record', kind=None),
                            ),
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_reference', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=False, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='message_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='mail.message', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Snailmail Status Message', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='notification_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='One2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='mail.notification', kind=None),
                            Constant(value='letter_id', kind=None),
                            Constant(value='Notifications', kind=None),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='street', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Street', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='street2', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Street2', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='zip', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Zip', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='city', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='City', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='state_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='res.country.state', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='State', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='country_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='res.country', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Country', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_display_name',
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
                            target=Name(id='letter', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=Attribute(
                                        value=Name(id='letter', ctx=Load()),
                                        attr='attachment_id',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='letter', ctx=Load()),
                                                    attr='display_name',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=BinOp(
                                                left=Constant(value='%s - %s', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Attribute(
                                                            value=Attribute(
                                                                value=Name(id='letter', ctx=Load()),
                                                                attr='attachment_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='name',
                                                            ctx=Load(),
                                                        ),
                                                        Attribute(
                                                            value=Attribute(
                                                                value=Name(id='letter', ctx=Load()),
                                                                attr='partner_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='name',
                                                            ctx=Load(),
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
                                                    value=Name(id='letter', ctx=Load()),
                                                    attr='display_name',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='letter', ctx=Load()),
                                                    attr='partner_id',
                                                    ctx=Load(),
                                                ),
                                                attr='name',
                                                ctx=Load(),
                                            ),
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
                                Constant(value='reference', kind=None),
                                Constant(value='partner_id', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_reference',
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
                            target=Name(id='res', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='res', ctx=Load()),
                                            attr='reference',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BinOp(
                                        left=Constant(value='%s,%s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Attribute(
                                                    value=Name(id='res', ctx=Load()),
                                                    attr='model',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Name(id='res', ctx=Load()),
                                                    attr='res_id',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
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
                                Constant(value='model', kind=None),
                                Constant(value='res_id', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='create',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='vals_list', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        For(
                            target=Name(id='vals', ctx=Store()),
                            iter=Name(id='vals_list', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='msg_id', ctx=Store())],
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
                                                        slice=Subscript(
                                                            value=Name(id='vals', ctx=Load()),
                                                            slice=Constant(value='model', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    attr='browse',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='vals', ctx=Load()),
                                                        slice=Constant(value='res_id', kind=None),
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
                                                    args=[Constant(value='Letter sent by post with Snailmail', kind=None)],
                                                    keywords=[],
                                                ),
                                            ),
                                            keyword(
                                                arg='message_type',
                                                value=Constant(value='snailmail', kind=None),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='partner_id', ctx=Store())],
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
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='vals', ctx=Load()),
                                                slice=Constant(value='partner_id', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='vals', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='message_id', kind=None),
                                                    Constant(value='street', kind=None),
                                                    Constant(value='street2', kind=None),
                                                    Constant(value='zip', kind=None),
                                                    Constant(value='city', kind=None),
                                                    Constant(value='state_id', kind=None),
                                                    Constant(value='country_id', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='msg_id', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='partner_id', ctx=Load()),
                                                        attr='street',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='partner_id', ctx=Load()),
                                                        attr='street2',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='partner_id', ctx=Load()),
                                                        attr='zip',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='partner_id', ctx=Load()),
                                                        attr='city',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='partner_id', ctx=Load()),
                                                            attr='state_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='partner_id', ctx=Load()),
                                                            attr='country_id',
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
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='letters', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Name(id='vals_list', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='notification_vals', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='letter', ctx=Store()),
                            iter=Name(id='letters', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='notification_vals', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='mail_message_id', kind=None),
                                                    Constant(value='res_partner_id', kind=None),
                                                    Constant(value='notification_type', kind=None),
                                                    Constant(value='letter_id', kind=None),
                                                    Constant(value='is_read', kind=None),
                                                    Constant(value='notification_status', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='letter', ctx=Load()),
                                                            attr='message_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='letter', ctx=Load()),
                                                            attr='partner_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='snail', kind=None),
                                                    Attribute(
                                                        value=Name(id='letter', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=True, kind=None),
                                                    Constant(value='ready', kind=None),
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
                        Expr(
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
                                                slice=Constant(value='mail.notification', kind=None),
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
                                args=[Name(id='notification_vals', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Name(id='letters', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model_create_multi',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_fetch_attachment',
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
                            value=Constant(value='\n        This method will check if we have any existent attachement matching the model\n        and res_ids and create them if not found.\n        ', kind=None),
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
                            targets=[Name(id='obj', ctx=Store())],
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
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='res_id',
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
                                operand=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='attachment_id',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='report', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='report_template',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='report', ctx=Load()),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='report_name', ctx=Store())],
                                            value=Call(
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
                                                args=[Constant(value='report_name', kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='report', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='ir.actions.report', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='_get_report_from_name',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='report_name', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Name(id='report', ctx=Load()),
                                            ),
                                            body=[
                                                Return(
                                                    value=Constant(value=False, kind=None),
                                                ),
                                            ],
                                            orelse=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='write',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[Constant(value='report_template', kind=None)],
                                                                values=[
                                                                    Attribute(
                                                                        value=Name(id='report', ctx=Load()),
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
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Attribute(
                                        value=Name(id='report', ctx=Load()),
                                        attr='print_report_name',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='report_name', ctx=Store())],
                                            value=Call(
                                                func=Name(id='safe_eval', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='report', ctx=Load()),
                                                        attr='print_report_name',
                                                        ctx=Load(),
                                                    ),
                                                    Dict(
                                                        keys=[Constant(value='object', kind=None)],
                                                        values=[Name(id='obj', ctx=Load())],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Attribute(
                                                value=Name(id='report', ctx=Load()),
                                                attr='attachment',
                                                ctx=Load(),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='report_name', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='safe_eval', ctx=Load()),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='report', ctx=Load()),
                                                                attr='attachment',
                                                                ctx=Load(),
                                                            ),
                                                            Dict(
                                                                keys=[Constant(value='object', kind=None)],
                                                                values=[Name(id='obj', ctx=Load())],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[Name(id='report_name', ctx=Store())],
                                                    value=Constant(value='Document', kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                Assign(
                                    targets=[Name(id='filename', ctx=Store())],
                                    value=BinOp(
                                        left=Constant(value='%s.%s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Name(id='report_name', ctx=Load()),
                                                Constant(value='pdf', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='pdf_bin', ctx=Store()),
                                                Name(id='_', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='report', ctx=Load()),
                                                    attr='with_context',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='snailmail_layout',
                                                        value=UnaryOp(
                                                            op=Not(),
                                                            operand=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='cover',
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            attr='_render_qweb_pdf',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='res_id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='attachment', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='ir.attachment', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='datas', kind=None),
                                                    Constant(value='res_model', kind=None),
                                                    Constant(value='res_id', kind=None),
                                                    Constant(value='type', kind=None),
                                                ],
                                                values=[
                                                    Name(id='filename', ctx=Load()),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='base64', ctx=Load()),
                                                            attr='b64encode',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='pdf_bin', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    Constant(value='snailmail.letter', kind=None),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='binary', kind=None),
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
                                            value=Name(id='self', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='attachment_id', kind=None)],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='attachment', ctx=Load()),
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
                        ),
                        Return(
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='attachment_id',
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_count_pages_pdf',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='bin_pdf', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Count the number of pages of the given pdf file.\n            :param bin_pdf : binary content of the pdf file\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='pages', ctx=Store())],
                            value=Constant(value=0, kind=None),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='match', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='re', ctx=Load()),
                                            attr='compile',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value=b'/Count\\s+(\\d+)', kind=None)],
                                        keywords=[],
                                    ),
                                    attr='finditer',
                                    ctx=Load(),
                                ),
                                args=[Name(id='bin_pdf', ctx=Load())],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='pages', ctx=Store())],
                                    value=Call(
                                        func=Name(id='int', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='match', ctx=Load()),
                                                    attr='group',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value=1, kind=None)],
                                                keywords=[],
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
                        Return(
                            value=Name(id='pages', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_snailmail_create',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='route', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n        Create a dictionnary object to send to snailmail server.\n\n        :return: Dict in the form:\n        {\n            account_token: string,    //IAP Account token of the user\n            documents: [{\n                pages: int,\n                pdf_bin: pdf file\n                res_id: int (client-side res_id),\n                res_model: char (client-side res_model),\n                address: {\n                    name: char,\n                    street: char,\n                    street2: char (OPTIONAL),\n                    zip: int,\n                    city: char,\n                    state: char (state code (OPTIONAL)),\n                    country_code: char (country code)\n                }\n                return_address: {\n                    name: char,\n                    street: char,\n                    street2: char (OPTIONAL),\n                    zip: int,\n                    city: char,at\n                    state: char (state code (OPTIONAL)),\n                    country_code: char (country code)\n                }\n            }],\n            options: {\n                color: boolean (true if color, false if black-white),\n                duplex: boolean (true if duplex, false otherwise),\n                currency_name: char\n            }\n        }\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='account_token', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='iap.account', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='get',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='snailmail', kind=None)],
                                    keywords=[],
                                ),
                                attr='account_token',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='dbuuid', ctx=Store())],
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
                                                slice=Constant(value='ir.config_parameter', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='get_param',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='database.uuid', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='documents', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='batch', ctx=Store())],
                            value=Compare(
                                left=Call(
                                    func=Name(id='len', ctx=Load()),
                                    args=[Name(id='self', ctx=Load())],
                                    keywords=[],
                                ),
                                ops=[Gt()],
                                comparators=[Constant(value=1, kind=None)],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='letter', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='document', ctx=Store())],
                                    value=Dict(
                                        keys=[
                                            Constant(value='letter_id', kind=None),
                                            Constant(value='res_model', kind=None),
                                            Constant(value='res_id', kind=None),
                                            Constant(value='contact_address', kind=None),
                                            Constant(value='address', kind=None),
                                            Constant(value='return_address', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='letter', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='letter', ctx=Load()),
                                                attr='model',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='letter', ctx=Load()),
                                                attr='res_id',
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Subscript(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='letter', ctx=Load()),
                                                                        attr='partner_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='with_context',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='snailmail_layout',
                                                                        value=Constant(value=True, kind=None),
                                                                    ),
                                                                    keyword(
                                                                        arg='show_address',
                                                                        value=Constant(value=True, kind=None),
                                                                    ),
                                                                ],
                                                            ),
                                                            attr='name_get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value=1, kind=None),
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='street', kind=None),
                                                    Constant(value='street2', kind=None),
                                                    Constant(value='zip', kind=None),
                                                    Constant(value='state', kind=None),
                                                    Constant(value='city', kind=None),
                                                    Constant(value='country_code', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='letter', ctx=Load()),
                                                            attr='partner_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='name',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='letter', ctx=Load()),
                                                            attr='partner_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='street',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='letter', ctx=Load()),
                                                            attr='partner_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='street2',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='letter', ctx=Load()),
                                                            attr='partner_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='zip',
                                                        ctx=Load(),
                                                    ),
                                                    IfExp(
                                                        test=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='letter', ctx=Load()),
                                                                attr='partner_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='state_id',
                                                            ctx=Load(),
                                                        ),
                                                        body=Attribute(
                                                            value=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='letter', ctx=Load()),
                                                                    attr='partner_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='state_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='code',
                                                            ctx=Load(),
                                                        ),
                                                        orelse=Constant(value=False, kind=None),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='letter', ctx=Load()),
                                                            attr='partner_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='city',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='letter', ctx=Load()),
                                                                attr='partner_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='country_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='code',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='street', kind=None),
                                                    Constant(value='street2', kind=None),
                                                    Constant(value='zip', kind=None),
                                                    Constant(value='state', kind=None),
                                                    Constant(value='city', kind=None),
                                                    Constant(value='country_code', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='letter', ctx=Load()),
                                                                attr='company_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='partner_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='name',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='letter', ctx=Load()),
                                                                attr='company_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='partner_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='street',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='letter', ctx=Load()),
                                                                attr='company_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='partner_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='street2',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='letter', ctx=Load()),
                                                                attr='company_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='partner_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='zip',
                                                        ctx=Load(),
                                                    ),
                                                    IfExp(
                                                        test=Attribute(
                                                            value=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='letter', ctx=Load()),
                                                                    attr='company_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='partner_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='state_id',
                                                            ctx=Load(),
                                                        ),
                                                        body=Attribute(
                                                            value=Attribute(
                                                                value=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='letter', ctx=Load()),
                                                                        attr='company_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='partner_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='state_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='code',
                                                            ctx=Load(),
                                                        ),
                                                        orelse=Constant(value=False, kind=None),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='letter', ctx=Load()),
                                                                attr='company_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='partner_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='city',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='letter', ctx=Load()),
                                                                    attr='company_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='partner_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='country_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='code',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='route', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='estimate', kind=None)],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='document', ctx=Load()),
                                                    attr='update',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='pages',
                                                        value=Constant(value=1, kind=None),
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='document', ctx=Load()),
                                                    attr='update',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[Constant(value='company_logo', kind=None)],
                                                        values=[
                                                            BoolOp(
                                                                op=Or(),
                                                                values=[
                                                                    BoolOp(
                                                                        op=And(),
                                                                        values=[
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='letter', ctx=Load()),
                                                                                    attr='company_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='logo_web',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='letter', ctx=Load()),
                                                                                            attr='company_id',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='logo_web',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='decode',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[Constant(value='utf-8', kind=None)],
                                                                                keywords=[],
                                                                            ),
                                                                        ],
                                                                    ),
                                                                    Constant(value=False, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[Name(id='attachment', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='letter', ctx=Load()),
                                                    attr='_fetch_attachment',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Name(id='attachment', ctx=Load()),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='document', ctx=Load()),
                                                            attr='update',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='pdf_bin', kind=None),
                                                                    Constant(value='pages', kind=None),
                                                                ],
                                                                values=[
                                                                    BoolOp(
                                                                        op=And(),
                                                                        values=[
                                                                            Compare(
                                                                                left=Name(id='route', ctx=Load()),
                                                                                ops=[Eq()],
                                                                                comparators=[Constant(value='print', kind=None)],
                                                                            ),
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Attribute(
                                                                                        value=Name(id='attachment', ctx=Load()),
                                                                                        attr='datas',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='decode',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[Constant(value='utf-8', kind=None)],
                                                                                keywords=[],
                                                                            ),
                                                                        ],
                                                                    ),
                                                                    BoolOp(
                                                                        op=And(),
                                                                        values=[
                                                                            Compare(
                                                                                left=Name(id='route', ctx=Load()),
                                                                                ops=[Eq()],
                                                                                comparators=[Constant(value='estimate', kind=None)],
                                                                            ),
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='_count_pages_pdf',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[
                                                                                    Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='base64', ctx=Load()),
                                                                                            attr='b64decode',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[
                                                                                            Attribute(
                                                                                                value=Name(id='attachment', ctx=Load()),
                                                                                                attr='datas',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                        ],
                                                                                        keywords=[],
                                                                                    ),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='letter', ctx=Load()),
                                                            attr='write',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='info_msg', kind=None),
                                                                    Constant(value='state', kind=None),
                                                                    Constant(value='error_code', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='The attachment could not be generated.', kind=None),
                                                                    Constant(value='error', kind=None),
                                                                    Constant(value='ATTACHMENT_ERROR', kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Continue(),
                                            ],
                                        ),
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='letter', ctx=Load()),
                                                        attr='company_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='external_report_layout_id',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            attr='ref',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='l10n_de.external_layout_din5008', kind=None),
                                                            Constant(value=False, kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='document', ctx=Load()),
                                                            attr='update',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[Constant(value='rightaddress', kind=None)],
                                                                values=[Constant(value=0, kind=None)],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='documents', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='document', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='account_token', kind=None),
                                    Constant(value='dbuuid', kind=None),
                                    Constant(value='documents', kind=None),
                                    Constant(value='options', kind=None),
                                    Constant(value='batch', kind=None),
                                ],
                                values=[
                                    Name(id='account_token', ctx=Load()),
                                    Name(id='dbuuid', ctx=Load()),
                                    Name(id='documents', ctx=Load()),
                                    Dict(
                                        keys=[
                                            Constant(value='color', kind=None),
                                            Constant(value='cover', kind=None),
                                            Constant(value='duplex', kind=None),
                                            Constant(value='currency_name', kind=None),
                                        ],
                                        values=[
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    Name(id='self', ctx=Load()),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Name(id='self', ctx=Load()),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='color',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    Name(id='self', ctx=Load()),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Name(id='self', ctx=Load()),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='cover',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    Name(id='self', ctx=Load()),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Name(id='self', ctx=Load()),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='duplex',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Constant(value='EUR', kind=None),
                                        ],
                                    ),
                                    Constant(value=True, kind=None),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_error_message',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='error', annotation=None, type_comment=None),
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
                                left=Name(id='error', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='CREDIT_ERROR', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='link', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='iap.account', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='get_credits_url',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='service_name',
                                                value=Constant(value='snailmail', kind=None),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Return(
                                    value=Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[
                                            Constant(value='You don\'t have enough credits to perform this operation.<br>Please go to your <a href=%s target="new">iap account</a>.', kind=None),
                                            Name(id='link', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Name(id='error', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='TRIAL_ERROR', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='link', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='iap.account', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='get_credits_url',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='service_name',
                                                value=Constant(value='snailmail', kind=None),
                                            ),
                                            keyword(
                                                arg='trial',
                                                value=Constant(value=True, kind=None),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Return(
                                    value=Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[
                                            Constant(value='You don\'t have an IAP account registered for this service.<br>Please go to <a href=%s target="new">iap.odoo.com</a> to claim your free credits.', kind=None),
                                            Name(id='link', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Name(id='error', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='NO_PRICE_AVAILABLE', kind=None)],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='The country of the partner is not covered by Snailmail.', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Name(id='error', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='MISSING_REQUIRED_FIELDS', kind=None)],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='One or more required fields are empty.', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Name(id='error', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='FORMAT_ERROR', kind=None)],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='The attachment of the letter could not be sent. Please check its content and contact the support if the problem persists.', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                Return(
                                    value=Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='An unknown error happened. Please contact the support.', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                            ],
                        ),
                        Return(
                            value=Name(id='error', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_failure_type',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='error', annotation=None, type_comment=None),
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
                                left=Name(id='error', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='CREDIT_ERROR', kind=None)],
                            ),
                            body=[
                                Return(
                                    value=Constant(value='sn_credit', kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Name(id='error', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='TRIAL_ERROR', kind=None)],
                            ),
                            body=[
                                Return(
                                    value=Constant(value='sn_trial', kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Name(id='error', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='NO_PRICE_AVAILABLE', kind=None)],
                            ),
                            body=[
                                Return(
                                    value=Constant(value='sn_price', kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Name(id='error', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='MISSING_REQUIRED_FIELDS', kind=None)],
                            ),
                            body=[
                                Return(
                                    value=Constant(value='sn_fields', kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Name(id='error', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='FORMAT_ERROR', kind=None)],
                            ),
                            body=[
                                Return(
                                    value=Constant(value='sn_format', kind=None),
                                ),
                            ],
                            orelse=[
                                Return(
                                    value=Constant(value='sn_error', kind=None),
                                ),
                            ],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_snailmail_print',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='immediate', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=True, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='valid_address_letters', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='l', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Call(
                                            func=Attribute(
                                                value=Name(id='l', ctx=Load()),
                                                attr='_is_valid_address',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='l', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='invalid_address_letters', ctx=Store())],
                            value=BinOp(
                                left=Name(id='self', ctx=Load()),
                                op=Sub(),
                                right=Name(id='valid_address_letters', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='invalid_address_letters', ctx=Load()),
                                    attr='_snailmail_print_invalid_address',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='valid_address_letters', ctx=Load()),
                                    Name(id='immediate', ctx=Load()),
                                ],
                            ),
                            body=[
                                For(
                                    target=Name(id='letter', ctx=Store()),
                                    iter=Name(id='valid_address_letters', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='letter', ctx=Load()),
                                                    attr='_snailmail_print_valid_address',
                                                    ctx=Load(),
                                                ),
                                                args=[],
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
                                                    attr='commit',
                                                    ctx=Load(),
                                                ),
                                                args=[],
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
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_snailmail_print_invalid_address',
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
                            targets=[Name(id='error', ctx=Store())],
                            value=Constant(value='MISSING_REQUIRED_FIELDS', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='error_message', ctx=Store())],
                            value=Call(
                                func=Name(id='_', ctx=Load()),
                                args=[Constant(value='The address of the recipient is not complete', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
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
                                        keys=[
                                            Constant(value='state', kind=None),
                                            Constant(value='error_code', kind=None),
                                            Constant(value='info_msg', kind=None),
                                        ],
                                        values=[
                                            Constant(value='error', kind=None),
                                            Name(id='error', ctx=Load()),
                                            Name(id='error_message', ctx=Load()),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='notification_ids',
                                                ctx=Load(),
                                            ),
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
                                        keys=[
                                            Constant(value='notification_status', kind=None),
                                            Constant(value='failure_type', kind=None),
                                            Constant(value='failure_reason', kind=None),
                                        ],
                                        values=[
                                            Constant(value='exception', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_get_failure_type',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='error', ctx=Load())],
                                                keywords=[],
                                            ),
                                            Name(id='error_message', ctx=Load()),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='message_id',
                                        ctx=Load(),
                                    ),
                                    attr='_notify_message_notification_update',
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
                    name='_snailmail_print_valid_address',
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
                            value=Constant(value="\n        get response\n        {\n            'request_code': RESPONSE_OK, # because we receive 200 if good or fail\n            'total_cost': total_cost,\n            'credit_error': credit_error,\n            'request': {\n                'documents': documents,\n                'options': options\n                }\n            }\n        }\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='endpoint', ctx=Store())],
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
                                                slice=Constant(value='ir.config_parameter', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='get_param',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='snailmail.endpoint', kind=None),
                                    Name(id='DEFAULT_ENDPOINT', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='timeout', ctx=Store())],
                            value=Call(
                                func=Name(id='int', ctx=Load()),
                                args=[
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
                                                        slice=Constant(value='ir.config_parameter', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='get_param',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='snailmail.timeout', kind=None),
                                            Name(id='DEFAULT_TIMEOUT', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='params', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_snailmail_create',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='print', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='response', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='iap_tools', ctx=Load()),
                                    attr='iap_jsonrpc',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Name(id='endpoint', ctx=Load()),
                                        op=Add(),
                                        right=Name(id='PRINT_ENDPOINT', ctx=Load()),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='params',
                                        value=Name(id='params', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='timeout',
                                        value=Name(id='timeout', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='doc', ctx=Store()),
                            iter=Subscript(
                                value=Subscript(
                                    value=Name(id='response', ctx=Load()),
                                    slice=Constant(value='request', kind=None),
                                    ctx=Load(),
                                ),
                                slice=Constant(value='documents', kind=None),
                                ctx=Load(),
                            ),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='doc', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='sent', kind=None)],
                                                keywords=[],
                                            ),
                                            Compare(
                                                left=Subscript(
                                                    value=Name(id='response', ctx=Load()),
                                                    slice=Constant(value='request_code', kind=None),
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value=200, kind=None)],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='note', ctx=Store())],
                                            value=Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[
                                                    Constant(value='The document was correctly sent by post.<br>The tracking id is %s', kind=None),
                                                    Subscript(
                                                        value=Name(id='doc', ctx=Load()),
                                                        slice=Constant(value='send_id', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='letter_data', ctx=Store())],
                                            value=Dict(
                                                keys=[
                                                    Constant(value='info_msg', kind=None),
                                                    Constant(value='state', kind=None),
                                                    Constant(value='error_code', kind=None),
                                                ],
                                                values=[
                                                    Name(id='note', ctx=Load()),
                                                    Constant(value='sent', kind=None),
                                                    Constant(value=False, kind=None),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='notification_data', ctx=Store())],
                                            value=Dict(
                                                keys=[
                                                    Constant(value='notification_status', kind=None),
                                                    Constant(value='failure_type', kind=None),
                                                    Constant(value='failure_reason', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='sent', kind=None),
                                                    Constant(value=False, kind=None),
                                                    Constant(value=False, kind=None),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='error', ctx=Store())],
                                            value=IfExp(
                                                test=Compare(
                                                    left=Subscript(
                                                        value=Name(id='response', ctx=Load()),
                                                        slice=Constant(value='request_code', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[Constant(value=200, kind=None)],
                                                ),
                                                body=Subscript(
                                                    value=Name(id='doc', ctx=Load()),
                                                    slice=Constant(value='error', kind=None),
                                                    ctx=Load(),
                                                ),
                                                orelse=Subscript(
                                                    value=Name(id='response', ctx=Load()),
                                                    slice=Constant(value='reason', kind=None),
                                                    ctx=Load(),
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='note', ctx=Store())],
                                            value=Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[
                                                    Constant(value='An error occured when sending the document by post.<br>Error: %s', kind=None),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_get_error_message',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='error', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='letter_data', ctx=Store())],
                                            value=Dict(
                                                keys=[
                                                    Constant(value='info_msg', kind=None),
                                                    Constant(value='state', kind=None),
                                                    Constant(value='error_code', kind=None),
                                                ],
                                                values=[
                                                    Name(id='note', ctx=Load()),
                                                    Constant(value='error', kind=None),
                                                    IfExp(
                                                        test=Compare(
                                                            left=Name(id='error', ctx=Load()),
                                                            ops=[In()],
                                                            comparators=[Name(id='ERROR_CODES', ctx=Load())],
                                                        ),
                                                        body=Name(id='error', ctx=Load()),
                                                        orelse=Constant(value='UNKNOWN_ERROR', kind=None),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='notification_data', ctx=Store())],
                                            value=Dict(
                                                keys=[
                                                    Constant(value='notification_status', kind=None),
                                                    Constant(value='failure_type', kind=None),
                                                    Constant(value='failure_reason', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='exception', kind=None),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_get_failure_type',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='error', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    Name(id='note', ctx=Load()),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                                Assign(
                                    targets=[Name(id='letter', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='doc', ctx=Load()),
                                                slice=Constant(value='letter_id', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='letter', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='letter_data', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='letter', ctx=Load()),
                                                        attr='notification_ids',
                                                        ctx=Load(),
                                                    ),
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='notification_data', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='message_id',
                                        ctx=Load(),
                                    ),
                                    attr='_notify_message_notification_update',
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
                    name='snailmail_print',
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
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='state', kind=None)],
                                        values=[Constant(value='pending', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='notification_ids',
                                                ctx=Load(),
                                            ),
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
                                        keys=[
                                            Constant(value='notification_status', kind=None),
                                            Constant(value='failure_type', kind=None),
                                            Constant(value='failure_reason', kind=None),
                                        ],
                                        values=[
                                            Constant(value='ready', kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='message_id',
                                        ctx=Load(),
                                    ),
                                    attr='_notify_message_notification_update',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Compare(
                                left=Call(
                                    func=Name(id='len', ctx=Load()),
                                    args=[Name(id='self', ctx=Load())],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value=1, kind=None)],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_snailmail_print',
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
                    name='cancel',
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
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='state', kind=None),
                                            Constant(value='error_code', kind=None),
                                        ],
                                        values=[
                                            Constant(value='canceled', kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='notification_ids',
                                                ctx=Load(),
                                            ),
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
                                        keys=[Constant(value='notification_status', kind=None)],
                                        values=[Constant(value='canceled', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='message_id',
                                        ctx=Load(),
                                    ),
                                    attr='_notify_message_notification_update',
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
                    name='_snailmail_cron',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='autocommit', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=True, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='letters_send', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='|', kind=None),
                                            Tuple(
                                                elts=[
                                                    Constant(value='state', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='pending', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value='&', kind=None),
                                            Tuple(
                                                elts=[
                                                    Constant(value='state', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='error', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='error_code', kind=None),
                                                    Constant(value='in', kind=None),
                                                    List(
                                                        elts=[
                                                            Constant(value='TRIAL_ERROR', kind=None),
                                                            Constant(value='CREDIT_ERROR', kind=None),
                                                            Constant(value='ATTACHMENT_ERROR', kind=None),
                                                            Constant(value='MISSING_REQUIRED_FIELDS', kind=None),
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
                        For(
                            target=Name(id='letter', ctx=Store()),
                            iter=Name(id='letters_send', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='letter', ctx=Load()),
                                            attr='_snailmail_print',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                If(
                                    test=Name(id='autocommit', ctx=Load()),
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
                                                    attr='commit',
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
                    name='_is_valid_address',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='record', annotation=None, type_comment=None),
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
                                    value=Name(id='record', ctx=Load()),
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='required_keys', ctx=Store())],
                            value=List(
                                elts=[
                                    Constant(value='street', kind=None),
                                    Constant(value='city', kind=None),
                                    Constant(value='zip', kind=None),
                                    Constant(value='country_id', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Name(id='all', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Subscript(
                                            value=Name(id='record', ctx=Load()),
                                            slice=Name(id='key', ctx=Load()),
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='key', ctx=Store()),
                                                iter=Name(id='required_keys', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
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
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
